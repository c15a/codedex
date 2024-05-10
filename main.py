from terminal_game import Player, Enemy
import random

# Main function to run the game
def main():
    player_name = input("Enter your Adventurer's name: ")
    player = Player(player_name)
    print(f"Welcome {player_name} to the Terminal Adventure Game!\n")
    print("'\nYour adventure begins now...Are you ready?...'\n'")

    # Main loop
    while player.hp > 0:
        # Generates a random enemy from a pool(list)
        enemies = [Enemy("Goblin", player.level), Enemy("Skeleton", player.level), Enemy("Orc", player.level), Enemy("Demon", player.level), Enemy("Wolf", player.level)]
        enemy = random.choice(enemies)
        print(f"'\nYou encounter a {enemy.name}!")
        player.display_health(enemy)

        # Battle loop when enemy is still alive
        while enemy.is_alive():
            # Choose actions during the Battle - Attack/Block/Heal or Flee
            action = input("What will you do? (1) Attack, (2) Block, (3) Heal, (4) Flee: ")

            if action == '1':
                player.attack(enemy)
                if enemy.is_alive():
                    enemy.attack(player)
                    player.display_health(enemy)
            elif action == '2':
                player.block()
                enemy.attack(player)
                player.display_health(enemy)
            elif action == '3':
                player.heal()
                enemy.attack(player)
                player.display_health(enemy)
            elif action == '4':
                player.flee()
                break
            else:
                print("Invalid choice. Try again.'\n'")

            # Game is Over when Player's HP reaches 0 and below
            if player.hp <= 0:
                print("Game Over. You have been defeated")
                return
        # Player defeats the enemy and player is still alive
        if player.hp > 0 and not enemy.is_alive():
            # Gain 1 player Level for each enemy the player defeats
            player.level += 1
            print(f"\n{enemy.name} has been defeated and you leveled up to level {player.level}!")

            # prompt player to choose their next location
            print("Available locations: Snow Mountains, Desert, Abandoned Sea, Haunted House")
            # enumerate() function adds a counter to an iterable
            for il, loc in enumerate(locations):
                # prints index of the location in order to start from 1 instead of 0
                print(f"{il+1}. {loc}")
            choice = int(input("Please choose your next path from (1, 2, 3, 4): "))
            chosen_location = locations[choice - 1]
            print(f"You chose to go to {chosen_location}.")

main()
