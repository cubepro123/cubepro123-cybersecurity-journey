# 📔 My Python Progress Log

This file tracks my coding progress by topic. Each section is grouped by the main programming concept I learned, explaining how it works and listing the code examples we built.

---

## Topic 1: Variables and Data Types

### What it does:
Variables are like labeled boxes that store information so our programs can remember and use them later. We can store different types of data, such as words (strings) or yes/no values (booleans).

### 📁 Lesson 1: Storing text (Strings)

```python
# ==============================================================================
# LESSON: Creating and using string variables to store words
# ==============================================================================
# We use single or double quotes to tell Python this is text (a string)
user_name = "Bol"
print("Hi, my name is " + user_name)
```

### 📁 Lesson 2: Storing True/False values (Booleans)

```python
# ==============================================================================
# LESSON: Using True and False variables to control program states
# ==============================================================================
# Booleans must start with a capital letter (True or False)
# We use them as simple on/off switches
system_is_running = True
print(system_is_running)
```

### 📁 Lesson 3: Storing multiple values (Lists)

```python
# ==============================================================================
# LESSON: Storing multiple values inside a single list variable
# ==============================================================================
# Each item is separated by a comma and enclosed in square brackets []
allowed_weapons = ["sword", "katana", "chainsaw", "pistol", "machinegun", "shotgun"]
# We can print the entire list to the screen
print(allowed_weapons)
```

### 📁 Lesson 4: Searching a list with `in`

```python
# ==============================================================================
# LESSON: Searching a list using 'in' instead of comparing with '=='
# ==============================================================================
allowed_weapons = ["sword", "katana", "chainsaw", "pistol", "machinegun", "shotgun"]
user_choice = "katana"

# Using '==' fails because "katana" is not identical to the whole list object
# Using 'in' scans the entire list to check if our word is one of the items
if user_choice in allowed_weapons:
    print("Match found! This weapon is inside the list.")
```

### 📁 Lesson 5: Looping until valid input (`while` loop)

```python
# ==============================================================================
# LESSON: Repeating a weapon prompt until the user types a valid option
# ==============================================================================
allowed_weapons = ["sword", "katana", "chainsaw", "pistol", "machinegun", "shotgun"]

# We use this boolean flag as an on/off switch for our loop
loop_active = True

# This loop runs continuously as long as loop_active is True
while loop_active == True:
    print("Choose a weapon to continue:")
    user_choice = input()
    # Once a valid weapon is entered, we turn the loop switch off
    if user_choice in allowed_weapons:
        print("Nice choice!")
        loop_active = False  # The loop stops running once this changes to False
```
