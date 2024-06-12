class Inventory:
  def __init__(self):
      self.items = {
          "weapon": None,
          "defense": None,
          "heal": [],
          "general": []
      }
      self.weapon_stats = {
          "Sword": 10,
          "Scale": 15
      }
      self.defense_stats = {
          "Shield": 5,
          "Mask": 8
      }

  def add_item(self, item, details):
      if details['type'] in ["weapon", "defense"]:
          self.items[details['type']] = item
          if details['type'] == "weapon":
              self.player_damage = self.weapon_stats[item]
          elif details['type'] == "defense":
              self.player_defense = self.defense_stats[item]
      else:
          self.items[details['type']].append(item)
      print(f"{item} added to your inventory.")

  def use_heal_item(self, player):
      print("Heal items in your inventory:")
      for item in self.items['heal']:
          print(f" - {item}")
      item = input("Which item do you want to use? ")
      if item in self.items['heal']:
          player.health += 20  # Arbitrary healing value
          self.items['heal'].remove(item)
          print(f"Used {item}. Health increased to {player.health}.")
      else:
          print("Invalid item or not a heal item.")

  def show(self, player):
      print("Your inventory contains:")
      for category, items in self.items.items():
          if isinstance(items, list) and items:
              for item in items:
                  print(f"{category.capitalize()}: {item}")
          elif items:
              print(f"{category.capitalize()}: {items}")
      print(f"Health: {player.health}, Damage: {player.damage}, Defense: {player.defense}")