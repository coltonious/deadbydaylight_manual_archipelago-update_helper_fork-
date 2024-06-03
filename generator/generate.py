import json

f = open("sourcedata.json")
killerDict = json.load(f)
f.close()

options = "#Generated option definitions\n"
options_adds = "#Generated option assignments\n"
items = []
locations = [
    {
        "name": "Entity Pleased",
        "category": "Master Enough Killers",
        "requires": "{hasEnoughWins()}",
        "victory": True,
    }
]
categories = {
    "Victory Tokens": {},
    "Perk": {"yaml_option": ["perk_roulette"]},
    "Base Perks": {"yaml_option": ["include_general_perks"]},
}
for perk in killerDict["base"]:
    items.append(
        {"name": perk, "category": ["Base Perks", "Perk"], "progression": True}
    )
    locations.append(
        {
            "name": f"{perk} Victory",
            "category": ["Perk", "Base Perks"],
            "requires": [perk],
        }
    )

print(
    f"Killer count: { len(killerDict['killers']) } - don't forget to set this in hooks/Options.py"
)

for killer, perks in killerDict["killers"].items():
    # cut out "The " in category name (AP doesn't like item and category name sharing)
    killer_category = killer[4:] + ", The"
    # name for yaml option (lowercase, underscored)
    yaml_option = killer.lower().replace(" ", "_")
    # name for option hook function (CamelCase, no spaces)
    func_name = killer.replace(" ", "")

    # add a category for the killer so it has a yaml option
    categories[killer_category] = {"yaml_option": [yaml_option]}
    # add an option stub for rich option description
    options += f'''class {func_name}(DefaultOnToggle):
    """Include {killer} and their perks ({", ".join(perks)}) as items and locations"""
    display_name = "Include {killer}"\n'''
    # generate add-to-options stubs too
    options_adds += f'options["{yaml_option}"] = {func_name}\n'

    victoryTokenName = f"{killer} Victory Token"
    # add item for killer
    items.append(
        {"name": killer, "category": ["Killer", killer_category], "progression": True}
    )
    # add item for killer win
    items.append(
        {
            "name": victoryTokenName,
            "category": ["Victory Tokens", killer_category],
            "progression": True,
        }
    )
    # add location for killer win (and killer win token)
    locations.append(
        {
            "name": victoryTokenName,
            "category": ["Killer", killer_category],
            "requires": [killer],
            "place_item": [victoryTokenName],
        }
    )
    locations.append(
        {
            "name": f"{killer} Victory",
            "category": ["Killer", killer_category],
            "requires": [killer],
        }
    )
    # add location & item for perks
    for killerPerk in perks:
        items.append(
            {
                "name": killerPerk,
                "category": ["Perk", killer_category],
                "progression": True,
            }
        )
        locations.append(
            {
                "name": f"{killerPerk} Victory",
                "category": ["Perk", killer_category],
                "requires": [killerPerk],
            }
        )


with open("locations.json", "w", encoding="utf-8") as locFile:
    json.dump(
        sorted(locations, key=lambda loc: loc["name"]),
        locFile,
        ensure_ascii=False,
        indent=4,
    )
with open("items.json", "w", encoding="utf-8") as itemsFile:
    json.dump(
        sorted(items, key=lambda item: item["name"]),
        itemsFile,
        ensure_ascii=False,
        indent=4,
    )
with open("categories.json", "w", encoding="utf-8") as categoriesFile:
    json.dump(categories, categoriesFile, ensure_ascii=False, indent=4)
with open("options.py.segment", "w", encoding="utf-8") as optionsFile:
    options += "#end generated"
    optionsFile.write(options)
with open("options_adds.py.segment", "w", encoding="utf-8") as optionsFile2:
    options_adds += "#end generated"
    optionsFile2.write(options_adds)
