from tabulate import tabulate
from area import Area
from enemy import Enemy

class GameMap:
    def __init__(self):
        self.map = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
        self.area_names = [
            ["Limgrave", "Stormveil Castle", "Mistwood"],
            ["Caelid", "Raya Lucaria Academy", "Siofra River"],
            ["Mountains of Giants", "Eternal City", "Faraum Azula"]
        ]

        self.enemies = {
            "Stormveil Castle": Enemy("Guardian Knight", 30, 5, "A towering knight clad in heavy armor."),
            "Eternal City": Enemy("Spectral Shade", 20, 8, "A ghostly apparition wielding a spectral blade.")
        }

        self.areas = {
            0: Area("Rolling hills and the occasional crumbling ruin. A gentle introduction to a harsh world", {"Sword": {"description": "A rusty old sword stuck in the ground", "type": "weapon"}}),
            1: Area("A massive fortress guarded by formidable foes. The sound of clanking armor fills the air", {"Shield": {"description": "A sturdy shield abandoned by a fallen knight", "type": "defense"}}),
            2: Area("Dense fog and eerie silence, home to unseen creatures lurking in the shadows.", {"Amulet": {"description": "An ancient amulet, glowing softly in the fog.", "type": "heal"}}),
            3: Area("A desolate landscape, tainted by a scarlet rot that consumes all life.", {"Herbs": {"description": "A rare medical herb resistant to the rot.", "type": "heal"}}),
            4: Area("A center of learning and magic, surrounded by water and mystery.", {"Book": {"description": "A tome of forgotten spells left on a dusty shelf", "type": "general"}}),
            5: Area("An underground cavern with a river that glows with an eternal light.", {"Crystal": {"description": "A luminous crystal by the river's edge.", "type": "general"}}),
            6: Area("Snow-covered peaks and the remnants of ancient giants.", {"Horns": {"description": "A giant's horn, carved into a wild instrument", "type": "general"}}),
            7: Area("Ruins filled with the secrets of lost civilizations and guarded by spectral figures.", {"Mask": {"description": "A mysterious mask, floating above an altar.", "type": "defense"}}),
            8: Area("Floating islands above a sea of clouds, the domain of dragons and lightning.", {"Scale": {"description": "A dragon scale, shimmering with energy.", "type": "weapon"}})
        }

    def get_area_index(self, position):
        return self.map[position[0]][position[1]]

    def get_area_name(self, position):
        return self.area_names[position[0]][position[1]]

    def create_map_display(self, player_position):
        map_display = [[self.area_names[x][y] for y in range(len(self.map[0]))] for x in range(len(self.map))]
        x, y = player_position
        map_display[x][y] = map_display[x][y] + " (P)"
        return tabulate(map_display, tablefmt='grid')