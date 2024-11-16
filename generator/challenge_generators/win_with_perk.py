"""Basic 'win with this perk' challenges for each perk"""

from dbd_types import Challenge, ChallengePack
import dbd_data


def generate_challenges() -> list[Challenge]:
    return [
        Challenge(f"Win with {perk}", ChallengePack.WIN_WITH_PERK, perk_reqs=[perk])
        for perk in dbd_data.all_perks()
    ]
