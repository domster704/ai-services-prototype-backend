import pytest

from src.domain.trinka_grammar_checker.entities import TrinkaTextToCheck


def test_trinka_text_to_check_valid():
    language = "en"
    paragraph = "This is a test paragraph"
    obj = TrinkaTextToCheck(paragraph=paragraph, language=language)

    assert obj.paragraph == paragraph
    assert obj.language == language


def test_trinka_text_to_check_unsupported_language():
    paragraph = "Texto de prueba"
    language = "fr"

    with pytest.raises(ValueError, match="Неподдерживаемый язык"):
        TrinkaTextToCheck(paragraph=paragraph, language=language)
