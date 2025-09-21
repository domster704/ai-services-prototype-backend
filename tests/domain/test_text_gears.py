import pytest
from src.domain.text_gears.entities import (
    TextGearsTextToCheck,
    SUPPORTED_LANGUAGES,
    MAX_TEXT_GEARS_STR_LENGTH,
)


def test_textgears_text_to_check_valid():
    lang = "en-US"
    text = "Hello, world!"
    obj = TextGearsTextToCheck(text=text, language=lang)

    assert obj.text == text
    assert obj.language == lang


def test_textgears_text_to_check_too_long_text():
    lang = "en-US"
    text = "a" * (MAX_TEXT_GEARS_STR_LENGTH + 1)
    with pytest.raises(
        ValueError, match="Длина текста не должна превышать 8192 символов"
    ):
        TextGearsTextToCheck(text=text, language=lang)


def test_textgears_text_to_check_unsupported_language():
    text = "Hello!"
    lang = "xx-YY"
    with pytest.raises(ValueError, match="Неподдерживаемый язык"):
        TextGearsTextToCheck(text=text, language=lang)
