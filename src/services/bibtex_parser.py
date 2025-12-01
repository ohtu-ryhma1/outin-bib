"""BibTeX tokenizer and parser for importing BibTeX entries."""

from enum import Enum, auto


class TokenType(Enum):
    """Token types for BibTeX lexer."""

    AT = auto()
    LBRACE = auto()
    RBRACE = auto()
    COMMA = auto()
    EQUALS = auto()
    STRING = auto()
    NUMBER = auto()
    IDENTIFIER = auto()
    EOF = auto()


class Token:
    """A token from the BibTeX lexer."""

    def __init__(self, token_type: TokenType, value: str, position: int):
        self.type = token_type
        self.value = value
        self.position = position

    def __repr__(self):
        return f"Token({self.type}, {self.value!r})"


class BibtexTokenizer:
    """Tokenizer for BibTeX format."""

    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.length = len(text)

    def _skip_whitespace_and_comments(self):
        """Skip whitespace and % comments."""
        while self.pos < self.length:
            if self.text[self.pos].isspace():
                self.pos += 1
            elif self.text[self.pos] == "%":
                # Skip to end of line
                while self.pos < self.length and self.text[self.pos] != "\n":
                    self.pos += 1
            else:
                break

    def _read_string(self, quote_char: str) -> str:
        """Read a quoted string."""
        result = []
        self.pos += 1  # Skip opening quote
        while self.pos < self.length:
            char = self.text[self.pos]
            if char == quote_char:
                self.pos += 1
                return "".join(result)
            if char == "\\":
                self.pos += 1
                if self.pos < self.length:
                    result.append(self.text[self.pos])
            else:
                result.append(char)
            self.pos += 1
        raise ValueError("Unterminated string")

    def _read_braced_value(self) -> str:
        """Read a braced value, handling nested braces."""
        result = []
        depth = 1
        self.pos += 1  # Skip opening brace
        while self.pos < self.length and depth > 0:
            char = self.text[self.pos]
            if char == "{":
                depth += 1
                result.append(char)
            elif char == "}":
                depth -= 1
                if depth > 0:
                    result.append(char)
            else:
                result.append(char)
            self.pos += 1
        if depth != 0:
            raise ValueError("Unterminated braced value")
        return "".join(result)

    def _read_identifier(self) -> str:
        """Read an identifier (field name, entry type, or key)."""
        start = self.pos
        while self.pos < self.length:
            char = self.text[self.pos]
            if char.isalnum() or char in "_-:/":
                self.pos += 1
            else:
                break
        return self.text[start : self.pos]

    def _read_number(self) -> str:
        """Read a number."""
        start = self.pos
        while self.pos < self.length and self.text[self.pos].isdigit():
            self.pos += 1
        return self.text[start : self.pos]

    def tokenize(self) -> list:
        """Tokenize the BibTeX text and return list of tokens."""
        tokens = []
        while self.pos < self.length:
            self._skip_whitespace_and_comments()
            if self.pos >= self.length:
                break

            start_pos = self.pos
            char = self.text[self.pos]

            if char == "@":
                self.pos += 1
                tokens.append(Token(TokenType.AT, "@", start_pos))
            elif char == "{":
                self.pos += 1
                tokens.append(Token(TokenType.LBRACE, "{", start_pos))
            elif char == "}":
                self.pos += 1
                tokens.append(Token(TokenType.RBRACE, "}", start_pos))
            elif char == ",":
                self.pos += 1
                tokens.append(Token(TokenType.COMMA, ",", start_pos))
            elif char == "=":
                self.pos += 1
                tokens.append(Token(TokenType.EQUALS, "=", start_pos))
            elif char == '"':
                value = self._read_string('"')
                tokens.append(Token(TokenType.STRING, value, start_pos))
            elif char.isdigit():
                value = self._read_number()
                tokens.append(Token(TokenType.NUMBER, value, start_pos))
            elif char.isalpha() or char == "_":
                value = self._read_identifier()
                tokens.append(Token(TokenType.IDENTIFIER, value, start_pos))
            else:
                self.pos += 1

        tokens.append(Token(TokenType.EOF, "", self.pos))
        return tokens


class BibtexParser:
    """Parser for BibTeX format."""

    def __init__(self, tokens: list):
        self.tokens = tokens
        self.pos = 0

    def _current(self) -> Token:
        """Get current token."""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return self.tokens[-1]

    def _advance(self) -> Token:
        """Advance to next token and return current."""
        token = self._current()
        self.pos += 1
        return token

    def _expect(self, token_type: TokenType) -> Token:
        """Expect a specific token type and advance."""
        token = self._current()
        if token.type != token_type:
            raise ValueError(
                f"Expected {token_type}, got {token.type} at position {token.position}"
            )
        return self._advance()

    def _parse_value(self) -> str:
        """Parse a field value (string, number, or braced content)."""
        token = self._current()

        if token.type == TokenType.STRING:
            self._advance()
            return token.value
        if token.type == TokenType.NUMBER:
            self._advance()
            return token.value
        if token.type == TokenType.IDENTIFIER:
            self._advance()
            return token.value
        if token.type == TokenType.LBRACE:
            # Need to re-parse from original text for braced values
            # For now, handle simple cases
            self._advance()
            result = []
            depth = 1
            while depth > 0 and self._current().type != TokenType.EOF:
                token = self._current()
                if token.type == TokenType.LBRACE:
                    depth += 1
                    result.append("{")
                elif token.type == TokenType.RBRACE:
                    depth -= 1
                    if depth > 0:
                        result.append("}")
                elif token.type == TokenType.COMMA:
                    if depth > 0:
                        result.append(",")
                elif token.type == TokenType.EQUALS:
                    result.append("=")
                else:
                    result.append(token.value)
                self._advance()
            return "".join(result)

        raise ValueError(f"Unexpected token {token.type} when parsing value")

    def _parse_field(self) -> tuple:
        """Parse a field name = value pair."""
        name_token = self._expect(TokenType.IDENTIFIER)
        field_name = name_token.value.lower()
        self._expect(TokenType.EQUALS)
        field_value = self._parse_value()
        return field_name, field_value

    def _parse_entry(self) -> dict:
        """Parse a single BibTeX entry."""
        self._expect(TokenType.AT)
        type_token = self._expect(TokenType.IDENTIFIER)
        entry_type = type_token.value.lower()

        self._expect(TokenType.LBRACE)

        # Parse entry key
        key_token = self._expect(TokenType.IDENTIFIER)
        entry_key = key_token.value

        fields = {}
        while self._current().type == TokenType.COMMA:
            self._advance()  # Skip comma
            if self._current().type == TokenType.RBRACE:
                break
            if self._current().type == TokenType.IDENTIFIER:
                field_name, field_value = self._parse_field()
                fields[field_name] = field_value

        self._expect(TokenType.RBRACE)

        return {
            "type": entry_type,
            "name": entry_key,
            "fields": fields,
        }

    def parse(self) -> list:
        """Parse all BibTeX entries from the tokens."""
        entries = []
        while self._current().type != TokenType.EOF:
            if self._current().type == TokenType.AT:
                entry = self._parse_entry()
                entries.append(entry)
            else:
                self._advance()
        return entries


def tokenize_bibtex(text: str) -> list:
    """Tokenize BibTeX text."""
    tokenizer = BibtexTokenizer(text)
    return tokenizer.tokenize()


def parse_bibtex(text: str) -> list:
    """Parse BibTeX text and return list of entry dictionaries."""
    tokenizer = BibtexTokenizer(text)
    tokens = tokenizer.tokenize()
    parser = BibtexParser(tokens)
    return parser.parse()
