from weapon_armory_checker import is_valid_weapon, count_by_first_letter


def test_is_valid_weapon_true():
    assert is_valid_weapon("katana", ["sword", "katana"]) is True


def test_is_valid_weapon_false():
    assert is_valid_weapon("laser", ["sword", "katana"]) is False


def test_count_by_first_letter():
    weapons = ["sword", "shotgun", "katana", "chainsaw"]
    assert count_by_first_letter("sword", weapons) == 2  # sword & shotgun
    assert count_by_first_letter("k", weapons) == 1
