"""Types for various DBD manual things."""

from enum import StrEnum
from collections.abc import Iterable


class Effect(StrEnum):
    """Effects that might get mentioned in challenges.
    Killers and perks have these."""

    BLINDNESS = "Blindness"
    BROKEN = "Broken"
    DEEP_WOUND = "Deep Wound"
    EXPOSED = "Exposed"
    AURA_READ = "Aura Reading"
    UNDETECTABLE = "Undetectable"
    SCOURGE_HOOK = "Scourge Hook"
    KILLER_INSTINCT = "Killer Instinct"
    HEX = "Hex"


class ChallengePack(StrEnum):
    WIN_AS_KILLER = "Win as Killer"
    PLAY_AS_KILLER = "Play as Killer"
    WIN_WITH_PERK = "Win with Perk"
    PLAY_WITH_PERK = "Play with Perk"
    BASIC = "Basic challenges with no requirements"


class Perk:
    """A DBD Perk"""

    name: str
    effects: list[Effect]


class Challenge:
    """A DBD Challenge"""

    pack: ChallengePack
    killer_req: str | None
    perk_reqs: Iterable[str]
    effect_reqs: Iterable[Effect]
    text: str

    def __init__(
        self,
        challenge_text: str,
        pack: ChallengePack,
        killer_req: str = None,
        perk_reqs: Iterable[str] = None,
        effect_reqs: Iterable[Effect] = None,
    ):
        self.pack = pack
        if effect_reqs is None:
            effect_reqs = []
        if perk_reqs is None:
            perk_reqs = []
        self.text = challenge_text
        self.killer_reqs = killer_req
        self.perk_reqs = perk_reqs
        self.effect_reqs = effect_reqs
