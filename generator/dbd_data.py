"""Data for DBD, and helper methods for using it"""

_base_perks = [
    "Bitter Murmur",
    "Deerstalker",
    "Distressing",
    "Hex: No One Escapes Death",
    "Hex: Thrill of the Hunt",
    "Insidious",
    "Iron Grasp",
    "Scourge Hook: Monstrous Shrine",
    "Shattered Hope",
    "Sloppy Butcher",
    "Spies from the Shadows",
    "Unrelenting",
    "Whispers",
]

_killers = {
    "The Trapper": ["Unnerving Presence", "Agitation", "Brutal Strength"],
    "The Wraith": ["Predator", "Bloodhound", "Shadowborn"],
    "The Hillbilly": ["Enduring", "Lightborn", "Tinkerer"],
    "The Nurse": ["Stridor", "Thanatophobia", "A Nurse's Calling"],
    "The Huntress": [
        "Beast of Prey",
        "Territorial Imperative",
        "Hex: Huntress Lullaby",
    ],
    "The Shape": [
        "Save the Best for Last",
        "Play With Your Food",
        "Dying Light",
    ],
    "The Hag": ["Hex: The Third Seal", "Hex: Ruin", "Hex: Devour Hope"],
    "The Doctor": ["Overwhelming Presence", "Monitor & Abuse", "Overcharge"],
    "The Cannibal": ["Knockout", "Barbecue & Chilli", "Franklin's Demise"],
    "The Nightmare": ["Fire Up", "Remember Me", "Blood Warden"],
    "The Pig": [
        "Scourge Hook: Hangman's Trick",
        "Surveillance",
        "Make Your Choice",
    ],
    "The Clown": ["Bamboozle", "Coulrophobia", "Pop Goes The Weasel"],
    "The Spirit": ["Spirit Fury", "Hex: Haunted Ground", "Rancor"],
    "The Legion": ["Discordance", "Mad Grit", "Iron Maiden"],
    "The Plague": [
        "Corrupt Intervention",
        "Infectious Fright",
        "Dark Devotion",
    ],
    "The Ghost Face": ["I'm All Ears", "Thrilling Tremors", "furtive Chase"],
    "The Demogorgon": ["Surge", "Mindbreaker", "Cruel Limits"],
    "The Oni": ["Zanshin Tactics", "Blood Echo", "Nemesis"],
    "The Deathslinger": ["Gearhead", "Dead Man's Switch", "Hex: Retribution"],
    "The Executioner": ["Forced Penance", "Trail of Torment", "Deathbound"],
    "The Blight": ["Dragon's Grip", "Hex: Blood Favor", "Hex: Undying"],
    "The Twins": ["Hoarder", "Oppression", "Coup de Grace"],
    "The Trickster": ["Starstruck", "Hex: Crowd Control", "No Way Out"],
    "The Nemesis": ["Lethal Pursuer", "Hysteria", "Eruption"],
    "The Cenobite": [
        "Deadlock",
        "Hex: Plaything",
        "Scourge Hook: Gift of Pain",
    ],
    "The Artist": [
        "Grim Embrace",
        "Scourge Hook: Pain Resonance",
        "Hex: Pentimento",
    ],
    "The Onryo": [
        "Call of Brine",
        "Scourge Hook: Floods of Rage",
        "Merciless Storm",
    ],
    "The Dredge": ["Dissolution", "Darkness Revealed", "Septic Touch"],
    "The Mastermind": ["Superior Anatomy", "Awakened Awareness", "Terminus"],
    "The Knight": ["Nowhere to Hide", "Hex: Face the Darkness", "Hubris"],
    "The Skull Merchant": ["THWACK!", "Leverage", "Game Afoot"],
    "The Singularity": [
        "Genetic Limits",
        "Forced Hesitation",
        "Machine Learning",
    ],
    "The Xenomorph": ["Rapid Brutality", "Alien Instinct", "Ultimate Weapon"],
    "The Good Guy": [
        "Hex: Two Can Play",
        "Friends 'til the End",
        "Batteries Included",
    ],
    "The Unknown": ["Unbound", "Undone", "Unforeseen"],
    "The Lich": ["Dark Arrogance", "Languid Touch", "Weave Attunement"],
    "The Dark Lord": ["Dominance", "Hex: Wretched Fate", "Human Greed"],
    "The Houndmaster": [
        "All-Shaking Thunder",
        "No Quarter",
        "Scourge Hook: Jagged Compass",
    ],
    "The Ghoul": [
        "Forever Entwined",
        "Hex: Nothing But Misery",
        "None Are Free"
    ],
    "The Animatronic": [
        "Phantom Fear",
        "Help Wanted",
        "Haywire"
    ],
    "The Krasue": [
        "Hex: Overture of Doom",
        "Ravenous",
        "Wandering Eye"
    ]
}


def killers() -> list[str]:
    """Get a list of killers (as strings)"""
    return _killers.keys()


def base_perks() -> list[str]:
    """Get a list of base perks (as strings)"""
    return _base_perks


def killer_perks_by_killer() -> dict[str, list[str]]:
    """Get a dict with killer names as keys and lists of their perks' names as values"""
    return _killers


def all_perks() -> list[str]:
    """Get a list of all perks (as strings)"""
    return base_perks + [perk for killer in _killers for perk in killer]
