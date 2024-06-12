from enemy import Enemy

class FinalBoss(Enemy):
    def __init__(self, name, health, damage, description):
        super().__init__(name, health, damage, description)