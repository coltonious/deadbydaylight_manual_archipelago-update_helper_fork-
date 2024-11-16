"""Basic, zero-requirement challenges. Not easy to come up with."""

from dbd_types import Challenge, ChallengePack

_base_challenges = [
    "Sacrifice 3 survivors to The Entity",
    "Damage generators 6 times",
    "Knock down survivors 8 times",
    "Hook survivors in the basement 2 times",
    "Hit 4 survivors near a pallet",
]


def generate_challenges() -> list[Challenge]:
    return [Challenge(text, ChallengePack.BASIC) for text in _base_challenges]
