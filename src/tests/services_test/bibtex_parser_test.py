import unittest

from src.services.bibtex_parser import (
    BibtexParser,
    BibtexTokenizer,
    Token,
    TokenType,
    parse_bibtex,
    tokenize_bibtex,
)


class TestBibtexTokenizer(unittest.TestCase):
    def test_tokenize_simple_entry(self):
        text = '@article{key, author = "Test"}'
        tokens = tokenize_bibtex(text)

        self.assertEqual(tokens[0].type, TokenType.AT)
        self.assertEqual(tokens[1].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[1].value, "article")
        self.assertEqual(tokens[2].type, TokenType.LBRACE)
        self.assertEqual(tokens[3].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[3].value, "key")
        self.assertEqual(tokens[4].type, TokenType.COMMA)
        self.assertEqual(tokens[5].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[5].value, "author")
        self.assertEqual(tokens[6].type, TokenType.EQUALS)
        self.assertEqual(tokens[7].type, TokenType.STRING)
        self.assertEqual(tokens[7].value, "Test")
        self.assertEqual(tokens[8].type, TokenType.RBRACE)
        self.assertEqual(tokens[9].type, TokenType.EOF)

    def test_tokenize_number_value(self):
        text = "@book{key, year = 2024}"
        tokens = tokenize_bibtex(text)

        # Find the number token
        number_token = None
        for token in tokens:
            if token.type == TokenType.NUMBER:
                number_token = token
                break

        self.assertIsNotNone(number_token)
        self.assertEqual(number_token.value, "2024")

    def test_tokenize_with_comments(self):
        text = """% This is a comment
@article{key, title = "Test"}"""
        tokens = tokenize_bibtex(text)

        # Should skip comment and start with @
        self.assertEqual(tokens[0].type, TokenType.AT)

    def test_tokenize_escaped_characters_in_string(self):
        text = '@article{key, title = "Test \\"Quote\\""}'
        tokens = tokenize_bibtex(text)

        # Find the string token
        string_token = None
        for token in tokens:
            if token.type == TokenType.STRING:
                string_token = token
                break

        self.assertIsNotNone(string_token)
        self.assertIn('"', string_token.value)


class TestBibtexParser(unittest.TestCase):
    def test_parse_simple_article(self):
        text = """@article{testkey,
  author = "John Doe",
  title = "Test Article",
  journaltitle = "Test Journal",
  year = 2024,
}"""
        entries = parse_bibtex(text)

        self.assertEqual(len(entries), 1)
        entry = entries[0]
        self.assertEqual(entry["type"], "article")
        self.assertEqual(entry["name"], "testkey")
        self.assertEqual(entry["fields"]["author"], "John Doe")
        self.assertEqual(entry["fields"]["title"], "Test Article")
        self.assertEqual(entry["fields"]["journaltitle"], "Test Journal")
        self.assertEqual(entry["fields"]["year"], "2024")

    def test_parse_book_entry(self):
        text = """@book{bookkey,
  author = "Jane Smith",
  title = "A Great Book",
  year = 2023,
  publisher = "Test Publisher",
}"""
        entries = parse_bibtex(text)

        self.assertEqual(len(entries), 1)
        entry = entries[0]
        self.assertEqual(entry["type"], "book")
        self.assertEqual(entry["name"], "bookkey")
        self.assertEqual(entry["fields"]["author"], "Jane Smith")
        self.assertEqual(entry["fields"]["publisher"], "Test Publisher")

    def test_parse_multiple_entries(self):
        text = """@article{first,
  author = "Author One",
  title = "First",
  journaltitle = "Journal",
  year = 2020,
}

@book{second,
  author = "Author Two",
  title = "Second",
  year = 2021,
}"""
        entries = parse_bibtex(text)

        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0]["name"], "first")
        self.assertEqual(entries[1]["name"], "second")

    def test_parse_case_insensitive_fields(self):
        text = """@article{key,
  AUTHOR = "Test",
  Title = "Test",
  journaltitle = "Journal",
  YEAR = 2024,
}"""
        entries = parse_bibtex(text)

        self.assertEqual(len(entries), 1)
        entry = entries[0]
        # Fields should be lowercased
        self.assertIn("author", entry["fields"])
        self.assertIn("title", entry["fields"])
        self.assertIn("year", entry["fields"])

    def test_parse_entry_with_special_characters(self):
        text = """@article{key2024,
  author = "O'Brien",
  title = "Test & Analysis",
  journaltitle = "Journal",
  year = 2024,
}"""
        entries = parse_bibtex(text)

        self.assertEqual(len(entries), 1)
        entry = entries[0]
        self.assertEqual(entry["fields"]["author"], "O'Brien")
        self.assertEqual(entry["fields"]["title"], "Test & Analysis")

    def test_parse_example_from_issue(self):
        text = """@article{CitekeyArticle,
  author   = "P. J. Cohen",
  title    = "The independence of the continuum hypothesis",
  journal  = "Proceedings of the National Academy of Sciences",
  year     = 1963,
  volume   = "50",
  number   = "6",
  pages    = "1143--1148",
}"""
        entries = parse_bibtex(text)

        self.assertEqual(len(entries), 1)
        entry = entries[0]
        self.assertEqual(entry["type"], "article")
        self.assertEqual(entry["name"], "CitekeyArticle")
        self.assertEqual(entry["fields"]["author"], "P. J. Cohen")
        self.assertEqual(
            entry["fields"]["title"], "The independence of the continuum hypothesis"
        )
        self.assertEqual(
            entry["fields"]["journal"], "Proceedings of the National Academy of Sciences"
        )
        self.assertEqual(entry["fields"]["year"], "1963")

    def test_parse_empty_string(self):
        entries = parse_bibtex("")
        self.assertEqual(len(entries), 0)

    def test_parse_only_whitespace(self):
        entries = parse_bibtex("   \n\t  ")
        self.assertEqual(len(entries), 0)


class TestTokenClass(unittest.TestCase):
    def test_token_repr(self):
        token = Token(TokenType.IDENTIFIER, "test", 0)
        repr_str = repr(token)
        self.assertIn("IDENTIFIER", repr_str)
        self.assertIn("test", repr_str)
