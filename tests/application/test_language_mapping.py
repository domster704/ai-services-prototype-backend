from src.application.grammar_checker.language_mapping import to_textgears, to_trinka


def test_textgears_known_languages():
    assert to_textgears("en") == "en-US"
    assert to_textgears("es") == "es-ES"
    assert to_textgears("de") == "de-DE"


def test_textgears_already_full_code():
    assert to_textgears("en-US") == "en-US"
    assert to_textgears("es-ES") == "es-ES"


def test_textgears_unknown_language():
    assert to_textgears("fr") == "fr"
    assert to_textgears("ru-RU") == "ru-RU"


def test_trinka_from_full_code():
    assert to_trinka("en-US") == "en"
    assert to_trinka("es-ES") == "es"
    assert to_trinka("de-DE") == "de"


def test_trinka_from_short_code():
    assert to_trinka("en") == "en"
    assert to_trinka("es") == "es"
    assert to_trinka("de") == "de"
