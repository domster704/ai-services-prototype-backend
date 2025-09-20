from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class TranslatedAndDetectedObject:
    detected: str
    translated: str
