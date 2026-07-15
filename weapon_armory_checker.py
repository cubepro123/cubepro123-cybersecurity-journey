# ==============================================================================
# PROJECT: Weapon Armory Checker
# Combines: strings, booleans, lists, 'in', while loops, and for loops
# ==============================================================================

allowed_weapons = ["sword", "katana", "chainsaw", "pistol", "machinegun", "shotgun"]

print("=== Welcome to the Armory ===")
print("Here are the weapons available:")

# FOR LOOP: go through the list and print each weapon with a number
for index in range(len(allowed_weapons)):
    weapon_number = index + 1
    print(str(weapon_number) + ". " + allowed_weapons[index])

# Boolean flag to control the while loop
loop_active = True

# WHILE LOOP: keep asking until the user types a valid weapon
while loop_active == True:
    print("\nType the name of a weapon to continue:")
    user_choice = input()

    if user_choice in allowed_weapons:
        print("Nice choice! " + user_choice + " has been added to your loadout.")
        loop_active = False
    else:
        print("That's not in the armory. Try again.")

# FOR LOOP (bonus): count how many weapons start with the same letter
first_letter = user_choice[0]
matching_count = 0

for weapon in allowed_weapons:
    if weapon[0] == first_letter:
        matching_count = matching_count + 1

print("\nFun fact: " + str(matching_count) + " weapon(s) in the armory start with the letter '" + first_letter + "'.")
print("Armory session complete.")
