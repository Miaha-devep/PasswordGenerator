import secrets
from enum import IntEnum
from math import log2


def create_new(length: int, characters: str) -> str:
    return "".join(secrets.choice(characters) for _ in range(length))


def get_entropy(length: int, character_number: int) -> float:
    try:
        entropy = length * log2(character_number)
        return round(entropy, 2)
    except ValueError:
        return 0.0


class StrengthToEntropy(IntEnum):
    Pathetic = 0
    Weak = 30
    Good = 50
    Strong = 70
    Excellent = 120
