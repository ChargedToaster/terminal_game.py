import random
import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print("\n")

class Player:
    def __init__(self):
        self.hp = 50
    
    def is_alive(self):
        return self.hp > 0
    
class Enemy:
    def __init__(self, name):
        self.name = name
        self.hp = random.randint(20, 30)

    def is_alive(self):
        return self.hp > 0


def combat(player, enemy):
    slow_print(f"An enemy {enemy.name} appears! Prepare for battle!")
    while player.is_alive() and enemy.is_alive():
        print("\nYour HP:", player.hp)
        print(f"{enemy.name}'s HP:", enemy.hp)
        print("1. Attack\n2. Block\n3. Heal")
        choice = input("> ")
        if choice == "1":
            dmg = random.randint(4, 8)
            enemy.hp -= dmg
            slow_print(f"You attack {enemy.name} for {dmg} damage!")
        elif choice == "2":
            block = True
            slow_print("You prepare to block the next attack.")
        elif choice == "3":
            heal = random.randint(5, 10)
            player.hp += heal
            slow_print(f"You heal for {heal} HP")
        else:
            slow_print("Invalid Choice.")
            continue

        if enemy.is_alive():
            enemy_attack = random.randint(6, 12)
            if "block" in locals() and block:
                enemy_attack = enemy_attack // 2
                slow_print(f"You block and reudce the damage to {enemy_attack}!")
                block = False
            player.hp -= enemy_attack
            slow_print(f"{enemy.name} attacks you for {enemy_attack} damage!")

    if player.is_alive:
        slow_print(f"You deafeated the {enemy.name}!")
    else:
        slow_print("You were defeated in battle. . . Game over.")
        exit()
    

def intro():
    slow_print("Welcome aboard the Starship Odyssey!")
    slow_print("You are part of a brave exploration crew journeying to uncharted galaxies.")
    slow_print("Your mission: explore Planet Xyz and return with intel.")
    input("Press Enter to begin your adventure...")

def explore_path():
    while True:
        slow_print("You exit your ship and see two paths ahead on Planet Xyz: ")
        slow_print("1. A shining cave\n2. A dark gloomy forest")
        choice = input("> ")
        if choice == "1":
            slow_print("You step into the shiny cave... there is a weird glow around you.")
            combat(player, Enemy("Cave Beast"))
            break
        elif choice == "2":
            slow_print("You enter the dark gloomy forest... Creatures stir in the dark.")
            combat(player, Enemy("Treant"))
            break
        else:
            slow_print("Invalid Choice")
        
def final_choice():
    slow_print("You reach the ancient ruins of a Xyz Temple.")
    slow_print("Inside, a terminal glows with alien code. You have two options:")
    slow_print("1. Attempt to decode the terminal\n2. Take a sample and leave")
    choice = input("> ")
    if choice == "1":
        success = random.choice([True, False])
        if success:
            slow_print("You decode the terminal and gain ancient knowledge. Victory!")
        else:
            slow_print("The terminal triggers a defense mechanism!")
            combat(player, Enemy("Guardian"))
            slow_print("You escape with valuable data. Mission success!")
    elif choice == "2":
        slow_print("You take a sample and return to your ship safely.")
        slow_print("Mission accomplished... but what secrets remain hidden?")
    else:
        slow_print("Hesitation causes the temple to collapse! You barely escape.")
        slow_print("Mission failed... sort of.")

player = Player()
intro()
explore_path()
final_choice()
slow_print("Thanks for playing my scuffed Terminal game!")
            
