from dbd_types import Challenge, ChallengePack
import dbd_data


def generate_challenges() -> list[Challenge]:
    return [
        Challenge(
            f"Play a game using {perk}", ChallengePack.PLAY_WITH_PERK, perk_reqs=[perk]
        )
        for perk in dbd_data.all_perks()
    ]
