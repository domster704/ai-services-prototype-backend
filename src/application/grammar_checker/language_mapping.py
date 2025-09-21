LANGUAGE_MAP = {
    "en": "en-US",
    "es": "es-ES",
    "de": "de-DE",
}


def to_textgears(lang: str) -> str:
    return LANGUAGE_MAP.get(lang, lang)


def to_trinka(lang: str) -> str:
    return lang.split("-")[0] if "-" in lang else lang
