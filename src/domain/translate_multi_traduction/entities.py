from __future__ import annotations

from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class TranslatedObject:
    translated: str

    @classmethod
    def from_list(cls, items: list[str]) -> TranslatedObject:
        return cls(translated=items[0])
