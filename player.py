from inventory import Inventory
import random

class Player:
    def __init__(self, position):
        self.position = position
        self.health = 100
        self.damage = 5
        self.defense = 0
        self.inventory = Inventory()

    def encounter_enemy(self, enemy):
        print(f"You encounter a {enemy.name} - {enemy.description}")
        while enemy.health > 0 and self.health > 0:
            action = input("Do you want to fight (f) or run away (r)? ").lower()
            if action == "f":
                enemy.health -= random.randint(self.damage, self.damage + 10)
                print(f"You hit the {enemy.name}, reducing its health to {enemy.health}.")
                if enemy.health <= 0:
                    print(f"You defeated the {enemy.name}!")
                    return True
                damage_taken = max(0, enemy.damage - self.defense)
                self.health -= damage_taken
                print(f"The {enemy.name} hits you, reducing your health to {self.health}.")
                if self.health <= 0:
                    print("You have been defeated!")
                    break
            elif action == "r":
                print("You run away successfully.")
                break
            else:
                print("Invalid action. Choose 'f' to fight or 'r' to run away.")
        return False

    def search(self, game_map):
        area_index = game_map.get_area_index(self.position)
        interactables = game_map.areas[area_index].interactables
        if interactables:
            for item, details in interactables.items():
                print(f"You found something:\n{item}: {details['description']}")
                decision = input(f"Do you want to pick up the {item}? (y/n): ").strip().lower()
                if decision == 'y':
                    self.inventory.add_item(item, details)
                    del game_map.areas[area_index].interactables[item]
                    break
        else:
            print("There is nothing here to find.")

    def use_item(self):
        self.inventory.use_heal_item(self)

    def show_inventory(self):
        self.inventory.show(self)

    def display_map(self, game_map):
        map_display = game_map.create_map_display(self.position)
        print("\nMap:")
        print(map_display)

    def move(self, direction, game_map):
        x, y = self.position
        if direction == 'u' and x > 0:
            self.position = [x - 1, y]
        elif direction == 'd' and x < len(game_map.map) - 1:
            self.position = [x + 1, y]
        elif direction == 'r' and y < len(game_map.map[0]) - 1:
            self.position = [x, y + 1]
        elif direction == 'l' and y > 0:
            self.position = [x, y - 1]
        else:
            print("You can't move that way.")
            return
        self.print_area_description(game_map)

    def print_area_description(self, game_map):
        area_index = game_map.get_area_index(self.position)
        area_name = game_map.get_area_name(self.position)
        print("\nYou are in:", area_name)
        print(game_map.areas[area_index].description)
        if area_name in game_map.enemies and game_map.enemies[area_name].health > 0:
            self.encounter_enemy(game_map.enemies[area_name])