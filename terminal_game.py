import random
import time
def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print('\n')

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def is_alive(self):
        return self.hp > 0
    def __str__(self):
        return f"{self.name} (HP: {self.hp})"

class Player(Character):
    def __init__(self):
        super().__init__('Master-Chief', 50)
class Enemy(Character):
    def __init__(self, name):
        super().__init__(name, random.randint(20, 30))
def perform_action(player, enemy):
    actions = {
        '1': 'Attack',
        '2': 'Block',
        '3': 'Restore HP'
    }
    block = False
    print(f"\nStatus: {player}")
    print(f"Enemy: {enemy}")
    for key, action in actions.items():
        print(f"{key}. {action}")

    choice = input("What do you want to do: ")
    if choice == '1':
        damage = random.randint(4, 8)
        enemy.hp -= damage
        entry = f"Hit {enemy.name} for {damage} damage"
        slow_print(entry)
    elif choice == '2':
        block = True
        entry = "You are blocking the next attack"
        slow_print(entry)
    elif choice == '3':
        heal = random.randint(5, 10)
        player.hp += heal
        entry = f"Restored {heal} HP"
        slow_print(entry)
    else:
        entry = "Inavlid input"
        slow_print(entry)
    return block
def combat(player, enemy):
    slow_print(f"Enemy {enemy.name} approaching")
    block_next = False

    while player.is_alive() and enemy.is_alive():
        block = perform_action(player, enemy)

        if enemy.is_alive():
            damage = random.randint(6, 12)
            if block_next:
                damage //= 2
                slow_print(f"Blocked. Damage reduced to {damage}")
                block_next = False
            else:
                block_next = block
            player.hp -= damage
            slow_print(f"{enemy.name} hits you for {damage} damage")

    outcome = f"{enemy.name} defeated" if player.is_alive() else "You Died"
    slow_print(outcome)
    if not player.is_alive():
        exit()

def introduction():
    log_entries = [
        "Welcome on the Forward Unto Dawn",
        "Objective: Observation on the Halo",
    ]
    for entry in log_entries:
        slow_print(entry)
    input("Starting Misison (press Enter)...")
def choose_path(player):
    paths = {
        '1': ("a cave with weird sounds coming out of it", "Brute"),
        '2': ("a narrow street with alot of uncleared buildings", "Hunter")
    }

    while True:
        slow_print("Mission Journal: Divergence detected on planetary surface")
        for key, (desc, _) in paths.items():
            slow_print(f"{key}. Navigate towards {desc}")

        choice = input("Select your route: ")
        if choice in paths:
            description, enemy_name = paths[choice]
            slow_print(f"Navigating towards {description}. Readying for potential threats...")
            combat(player, Enemy(enemy_name))
            break
        else:
            slow_print("Route selection invalid. Try again")
def final_decision(player):
    slow_print("Arrival at Covenant Temple ruins")
    slow_print("Objective node detected. Options:")
    slow_print("1. Interface with alien terminal\n2. Extract artifact and withdraw")

    choice = input("Your decision: ")
    if choice == '1':
        if random.random() < 0.5:
            entry = "Terminal deciphered. Ancient tech assimilated. Mission Done"
            slow_print(entry)
        else:
            entry = "Security breach! Defense mechanism activated"
            slow_print(entry)
            combat(player, Enemy("Prophet"))
            slow_print("Evaded with encrypted data. Success")
    elif choice == '2':
        entry = "Artifact secured. Extracted"
        slow_print(entry)
    else:
        entry = "Inavlid Imput"
        slow_print(entry)
if __name__ == '__main__':
    player = Player()
    introduction()
    choose_path(player)
    final_decision(player)
    slow_print("Mission Complete")
