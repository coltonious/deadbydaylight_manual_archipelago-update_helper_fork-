"""What if we did tome challenges??? TBD, WIP, ETC"""

import json

import challenge_generators.basic
import challenge_generators.play_as_killer
import challenge_generators.play_with_perk
import challenge_generators.win_as_killer
import challenge_generators.win_with_perk
from dbd_types import Challenge

f = open("sourcedata.json", encoding="utf8")
killerDict = json.load(f)


def get_all_challenges():
    """Get all the possible challenges.
    Archipelago wants you to expose all possible locations, right?"""
    challenge_list: list[Challenge] = []
    challenge_list.extend(challenge_generators.win_as_killer.generate_challenges())
    challenge_list.extend(challenge_generators.win_with_perk.generate_challenges())
    challenge_list.extend(challenge_generators.play_with_perk.generate_challenges())
    challenge_list.extend(challenge_generators.play_as_killer.generate_challenges())
    challenge_list.extend(challenge_generators.basic.generate_challenges())
    return challenge_list
