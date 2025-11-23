from src.scripts.bibtex_types import types


def test_each_reference_has_required_and_optional():
    for _, fields in types.items():
        assert "required" in fields
        assert "optional" in fields
        assert isinstance(fields["required"], list)
        assert isinstance(fields["optional"], list)


def test_all_fields_are_nonempty_strings():
    for _, fields in types.items():
        for f in fields["required"] + fields["optional"]:
            assert isinstance(f, str)
            assert f.strip() != ""
