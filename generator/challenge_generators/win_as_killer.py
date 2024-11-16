"""Basic 'win as this killer' challenges for each killer"""

from dbd_types import Challenge, ChallengePack
import dbd_data


def generate_challenges() -> list[Challenge]:
    return [
        Challenge(f"Win as {killer}", ChallengePack.WIN_AS_KILLER, killer_req=killer)
        for killer in dbd_data.killers()
    ]
