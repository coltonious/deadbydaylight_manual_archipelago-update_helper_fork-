"""Basic 'play as this killer' challenges for each killer"""

from dbd_types import Challenge, ChallengePack
import dbd_data


def generate_challenges() -> list[Challenge]:
    return [
        Challenge(f"Play as {killer}", ChallengePack.PLAY_AS_KILLER, killer_req=killer)
        for killer in dbd_data.killers()
    ]
