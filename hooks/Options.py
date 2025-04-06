# Object classes from AP that represent different types of options that you can create
from Options import Range, DefaultOnToggle


# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class TotalCharactersToWinWith(Range):
    """How many killers would you like to win with?
    If not enough killers are included, this setting will be reduced to "all included killers".
    """

    display_name = "Number of characters to beat the game with before victory"
    range_start = 3
    range_end = 39
    default = 20


class IncludeGeneralPerks(DefaultOnToggle):
    """Include general perks (perks which aren't associated with any killer) as items and locations.
    If Perk Roulette is disabled, this setting has no effect."""

    display_name = "Include General Perks"


class PerkRoulette(DefaultOnToggle):
    """Whether perks should be included as items and locations.
    If not included, only killers will be shuffled. No perks will be shuffled, regardless of other settings.
    """

    display_name = "Perk Roulette"


# Generated option definitions
class TheTrapper(DefaultOnToggle):
    """Include The Trapper and their perks (Unnerving Presence, Agitation, Brutal Strength) as items and locations"""

    display_name = "Include The Trapper"


class TheWraith(DefaultOnToggle):
    """Include The Wraith and their perks (Predator, Bloodhound, Shadowborn) as items and locations"""

    display_name = "Include The Wraith"


class TheHillbilly(DefaultOnToggle):
    """Include The Hillbilly and their perks (Enduring, Lightborn, Tinkerer) as items and locations"""

    display_name = "Include The Hillbilly"


class TheNurse(DefaultOnToggle):
    """Include The Nurse and their perks (Stridor, Thanatophobia, A Nurse's Calling) as items and locations"""

    display_name = "Include The Nurse"


class TheHuntress(DefaultOnToggle):
    """Include The Huntress and their perks (Beast of Prey, Territorial Imperative, Hex: Huntress Lullaby) as items
    and locations"""

    display_name = "Include The Huntress"


class TheShape(DefaultOnToggle):
    """Include The Shape and their perks (Save the Best for Last, Play With Your Food, Dying Light) as items and locations"""

    display_name = "Include The Shape"


class TheHag(DefaultOnToggle):
    """Include The Hag and their perks (Hex: The Third Seal, Hex: Ruin, Hex: Devour Hope) as items and locations"""

    display_name = "Include The Hag"


class TheDoctor(DefaultOnToggle):
    """Include The Doctor and their perks (Overwhelming Presence, Monitor & Abuse, Overcharge) as items and locations"""

    display_name = "Include The Doctor"


class TheCannibal(DefaultOnToggle):
    """Include The Cannibal and their perks (Knockout, Barbecue & Chilli, Franklin's Demise) as items and locations"""

    display_name = "Include The Cannibal"


class TheNightmare(DefaultOnToggle):
    """Include The Nightmare and their perks (Fire Up, Remember Me, Blood Warden) as items and locations"""

    display_name = "Include The Nightmare"


class ThePig(DefaultOnToggle):
    """Include The Pig and their perks (Scourge Hook: Hangman's Trick, Surveillance, Make Your Choice) as items and locations"""

    display_name = "Include The Pig"


class TheClown(DefaultOnToggle):
    """Include The Clown and their perks (Bamboozle, Coulrophobia, Pop Goes The Weasel) as items and locations"""

    display_name = "Include The Clown"


class TheSpirit(DefaultOnToggle):
    """Include The Spirit and their perks (Spirit Fury, Hex: Haunted Ground, Rancor) as items and locations"""

    display_name = "Include The Spirit"


class TheLegion(DefaultOnToggle):
    """Include The Legion and their perks (Discordance, Mad Grit, Iron Maiden) as items and locations"""

    display_name = "Include The Legion"


class ThePlague(DefaultOnToggle):
    """Include The Plague and their perks (Corrupt Intervention, Infectious Fright, Dark Devotion) as items and locations"""

    display_name = "Include The Plague"


class TheGhostFace(DefaultOnToggle):
    """Include The Ghost Face and their perks (I'm All Ears, Thrilling Tremors, Furitive Chase) as items and locations"""

    display_name = "Include The Ghost Face"


class TheDemogorgon(DefaultOnToggle):
    """Include The Demogorgon and their perks (Surge, Mindbreaker, Cruel Limits) as items and locations"""

    display_name = "Include The Demogorgon"


class TheOni(DefaultOnToggle):
    """Include The Oni and their perks (Zanshin Tactics, Blood Echo, Nemesis) as items and locations"""

    display_name = "Include The Oni"


class TheDeathslinger(DefaultOnToggle):
    """Include The Deathslinger and their perks (Gearhead, Dead Man's Switch, Hex: Retribution) as items and locations"""

    display_name = "Include The Deathslinger"


class TheExecutioner(DefaultOnToggle):
    """Include The Executioner and their perks (Forced Penance, Trail of Torment, Deathbound) as items and locations"""

    display_name = "Include The Executioner"


class TheBlight(DefaultOnToggle):
    """Include The Blight and their perks (Dragon's Grip, Hex: Blood Favor, Hex: Undying) as items and locations"""

    display_name = "Include The Blight"


class TheTwins(DefaultOnToggle):
    """Include The Twins and their perks (Hoarder, Oppression, Coup de Grace) as items and locations"""

    display_name = "Include The Twins"


class TheTrickster(DefaultOnToggle):
    """Include The Trickster and their perks (Starstruck, Hex: Crowd Control, No Way Out) as items and locations"""

    display_name = "Include The Trickster"


class TheNemesis(DefaultOnToggle):
    """Include The Nemesis and their perks (Lethal Pursuer, Hysteria, Eruption) as items and locations"""

    display_name = "Include The Nemesis"


class TheCenobite(DefaultOnToggle):
    """Include The Cenobite and their perks (Deadlock, Hex: Plaything, Scourge Hook: Gift of Pain) as items and locations"""

    display_name = "Include The Cenobite"


class TheArtist(DefaultOnToggle):
    """Include The Artist and their perks (Grim Embrace, Scourge Hook: Pain Resonance, Hex: Pentimento) as items and locations"""

    display_name = "Include The Artist"


class TheOnryo(DefaultOnToggle):
    """Include The Onryo and their perks (Call of Brine, Scourge Hook: Floods of Rage, Merciless Storm) as items and locations"""

    display_name = "Include The Onryo"


class TheDredge(DefaultOnToggle):
    """Include The Dredge and their perks (Dissolution, Darkness Revealed, Septic Touch) as items and locations"""

    display_name = "Include The Dredge"


class TheMastermind(DefaultOnToggle):
    """Include The Mastermind and their perks (Superior Anatomy, Awakened Awareness, Terminus) as items and locations"""

    display_name = "Include The Mastermind"


class TheKnight(DefaultOnToggle):
    """Include The Knight and their perks (Nowhere to Hide, Hex: Face the Darkness, Hubris) as items and locations"""

    display_name = "Include The Knight"


class TheSkullMerchant(DefaultOnToggle):
    """Include The Skull Merchant and their perks (THWACK!, Leverage, Game Afoot) as items and locations"""

    display_name = "Include The Skull Merchant"


class TheSingularity(DefaultOnToggle):
    """Include The Singularity and their perks (Genetic Limits, Forced Hesitation, Machine Learning) as items and locations"""

    display_name = "Include The Singularity"


class TheXenomorph(DefaultOnToggle):
    """Include The Xenomorph and their perks (Rapid Brutality, Alien Instinct, Ultimate Weapon) as items and locations"""

    display_name = "Include The Xenomorph"


class TheGoodGuy(DefaultOnToggle):
    """Include The Good Guy and their perks (Hex: Two Can Play, Friends 'til the End, Batteries Included) as items and locations"""

    display_name = "Include The Good Guy"


class TheUnknown(DefaultOnToggle):
    """Include The Unknown and their perks (Unbound, Undone, Unforeseen) as items and locations"""

    display_name = "Include The Unknown"


class TheLich(DefaultOnToggle):
    """Include The Lich and their perks (Dark Arrogance, Languid Touch, Weave Attunement) as items and locations"""

    display_name = "Include The Lich"


class TheDarkLord(DefaultOnToggle):
    """Include The Dark Lord and their perks (Dominance, Hex: Wretched Fate, Human Greed) as items and locations"""

    display_name = "Include The Dark Lord"


class TheHoundmaster(DefaultOnToggle):
    """Include The Houndmaster and their perks (All-Shaking Thunder, No Quarter, Scourge Hook: Jagged Compass) as items and locations"""

    display_name = "Include The Houndmaster"


class TheGhoul(DefaultOnToggle):
    """Include The Ghoul and their perks (Forever Entwined, Hex: Nothing But Misery, None Are Free) as items and locations"""
    display_name = "Include The Ghoul"

# end generated


# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["total_killers_to_win_with"] = TotalCharactersToWinWith
    options["perk_roulette"] = PerkRoulette
    options["include_general_perks"] = IncludeGeneralPerks
    # Generated option assignments
    options["the_trapper"] = TheTrapper
    options["the_wraith"] = TheWraith
    options["the_hillbilly"] = TheHillbilly
    options["the_nurse"] = TheNurse
    options["the_huntress"] = TheHuntress
    options["the_shape"] = TheShape
    options["the_hag"] = TheHag
    options["the_doctor"] = TheDoctor
    options["the_cannibal"] = TheCannibal
    options["the_nightmare"] = TheNightmare
    options["the_pig"] = ThePig
    options["the_clown"] = TheClown
    options["the_spirit"] = TheSpirit
    options["the_legion"] = TheLegion
    options["the_plague"] = ThePlague
    options["the_ghost_face"] = TheGhostFace
    options["the_demogorgon"] = TheDemogorgon
    options["the_oni"] = TheOni
    options["the_deathslinger"] = TheDeathslinger
    options["the_executioner"] = TheExecutioner
    options["the_blight"] = TheBlight
    options["the_twins"] = TheTwins
    options["the_trickster"] = TheTrickster
    options["the_nemesis"] = TheNemesis
    options["the_cenobite"] = TheCenobite
    options["the_artist"] = TheArtist
    options["the_onryo"] = TheOnryo
    options["the_dredge"] = TheDredge
    options["the_mastermind"] = TheMastermind
    options["the_knight"] = TheKnight
    options["the_skull_merchant"] = TheSkullMerchant
    options["the_singularity"] = TheSingularity
    options["the_xenomorph"] = TheXenomorph
    options["the_good_guy"] = TheGoodGuy
    options["the_unknown"] = TheUnknown
    options["the_lich"] = TheLich
    options["the_dark_lord"] = TheDarkLord
    options["the_houndmaster"] = TheHoundmaster
    # end generated

    return options


# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options
