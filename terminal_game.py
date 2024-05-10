import random

# List of the locations in game
locations = ['Snow Mountains', 'Desert', 'Abandoned Sea', 'Haunted House']

# Player class / character
class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp = 150

    def attack(self, enemy):
        # Player attacks the enemy and deals random damage based on level
        damage = random.randint(10, 20) * self.level
        enemy.hp -= damage
        print(f"You attacked the {enemy.name} and dealt {damage} damage! ")

    def block(self):
        # Player blocks the enemy's and reduces the incoming damage
        blocked = random.randint(5, 50) * self.level
        print(f"You block the enemy's attack and reduced the incoming damage by {blocked}.")
        return blocked

    def heal(self):
        # Player heals themselves 
        heal_amount = random.randint(15, 35) * self.level
        self.hp += heal_amount
        print(f"You healed yourself for {heal_amount} HP")

    def flee(self):
        # Player attempts to flee from battle
        flee_chance = random.randint(0, 2)
        if flee_chance == 0:
            print("You are unable to flee the battle.")
        else:
            print("You escaped the battle")

    def display_health(self, enemy=None):
        # Display players HP and enemy's HP if provided
        print(f"Your HP: {self.hp}")
        if enemy:
            print(f"{enemy.name} HP: {enemy.hp}")

# Enemy class in game
class Enemy:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = 50 + (level * 10)

    def attack(self, player):
        # Enemy attacks the player and deals random damage
        if self.hp > 0:
            damage = random.randint(5, 25) * self.level
            player.hp -= damage
            print(f"The {self.name} attacked you and dealt {damage} damage!")
            
    def take_damage(self, damage):
        # Enemy takes damage
        self.hp -= damage

    def is_alive(self):
        # Checks if enemy is still alive
        return self.hp > 0
