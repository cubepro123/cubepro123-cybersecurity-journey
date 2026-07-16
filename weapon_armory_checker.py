"""
Refactored Weapon Armory Checker
- provides functions that can be unit-tested
- supports non-interactive use via --choice
- includes basic input validation
"""
from typing import List
import argparse
import sys


ALLOWED_WEAPONS: List[str] = [
    "sword",
    "katana",
    "chainsaw",
    "pistol",
    "machinegun",
    "shotgun",
]


def is_valid_weapon(choice: str, weapons: List[str]) -> bool:
    """Return True if choice is one of the allowed weapons (case-insensitive)."""
    if not choice:
        return False
    return choice.lower() in (w.lower() for w in weapons)


def count_by_first_letter(choice: str, weapons: List[str]) -> int:
    """Count how many weapons start with the first letter of choice (case-insensitive)."""
    if not choice:
        return 0
    first = choice[0].lower()
    return sum(1 for w in weapons if w and w[0].lower() == first)


def list_weapons(weapons: List[str]) -> str:
    """Return a numbered string listing of weapons."""
    lines = [f"{i+1}. {w}" for i, w in enumerate(weapons)]
    return "\n".join(lines)


def parse_args(argv: List[str] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Weapon Armory Checker — small example for input validation and loops")
    parser.add_argument("--choice", "-c", help="Provide a weapon choice non-interactively")
    return parser.parse_args(argv)


def prompt_choice(weapons: List[str], max_attempts: int = 3) -> str:
    attempts = 0
    while attempts < max_attempts:
        print("\nType the name of a weapon to continue:")
        try:
            user_choice = input().strip()
        except EOFError:
            print("No input available. Exiting.")
            return ""
        if is_valid_weapon(user_choice, weapons):
            return user_choice
        print("That's not in the armory. Try again.")
        attempts += 1
    print("Too many invalid attempts. Exiting.")
    return ""


def main(argv: List[str] = None) -> int:
    args = parse_args(argv)

    print("=== Welcome to the Armory ===")
    print("Here are the weapons available:")
    print(list_weapons(ALLOWED_WEAPONS))

    if args.choice:
        choice = args.choice.strip()
        if not is_valid_weapon(choice, ALLOWED_WEAPONS):
            print(f"Provided choice '{choice}' is not valid.")
            return 2
    else:
        choice = prompt_choice(ALLOWED_WEAPONS)
        if not choice:
            return 1

    print(f"Nice choice! {choice} has been added to your loadout.")
    matching_count = count_by_first_letter(choice, ALLOWED_WEAPONS)
    print(f"\nFun fact: {matching_count} weapon(s) in the armory start with the letter '{choice[0]}'.")
    print("Armory session complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
