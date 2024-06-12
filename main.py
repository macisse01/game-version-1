from player import Player
from game_map import GameMap
from area import Area
from final_boss import FinalBoss

class Game:
    def __init__(self):
        self.game_map = GameMap()
        self.player = Player([0, 0])
        self.final_boss = FinalBoss("Dark Overlord", 50, 10, "The final challenge, a menacing figure of immense power.")

    def all_items_collected(self):
        for area in self.game_map.areas.values():
            if area.interactables:
                return False
        return True

    def all_enemies_defeated(self):
        for enemy in self.game_map.enemies.values():
            if enemy.health > 0:
                return False
        return True

    def final_boss_encounter(self):
        if self.player.encounter_enemy(self.final_boss):
            print("Dark Overlord: 'You have bested me... You are free now. Farewell.'")
            print("Congratulations! You have completed the game!")
            return True
        return False

    def main_menu(self):
        while True:
            self.player.print_area_description(self.game_map)
            print("\nChoose an action:")
            print("  u - Move up")
            print("  d - Move down")
            print("  l - Move left")
            print("  r - Move right")
            print("  s - Search")
            print("  i - Show inventory")
            print("  m - Show map")
            print("  h - Use heal item")
            print("  q - Quit")

            action = input("> ").lower().strip()

            if action == 'q':
                print("Exiting game.")
                break
            elif action in ['u', 'd', 'l', 'r']:
                self.player.move(action, self.game_map)
            elif action == 's':
                self.player.search(self.game_map)
            elif action == 'i':
                self.player.show_inventory()
            elif action == 'm':
                self.player.display_map(self.game_map)
            elif action == 'h':
                self.player.use_item()
            else:
                print("Invalid command. Please try again.")

            if self.all_items_collected() and self.all_enemies_defeated():
                if self.final_boss_encounter():
                    break

if __name__ == '__main__':
    print("Welcome to the Adventure Game!")
    game = Game()
    game.main_menu()