def pick_cat(pick: int, cats: int) -> list:
    round = pick
    picked_cats = []
    for number in range(cats + 1)[1:]:
        if number == round:
            picked_cats.append(number)
            round += pick
    return picked_cats
        

# print(pick_cat(10, 100))


def cats_in_hats(cats: int, rounds: int) -> list:
    round = 1
    cats_with_hats = []
    while round <= rounds:
        checked_cats = pick_cat(round, cats)
        for cat in range(cats + 1)[1:]:
            if cat in checked_cats:
                if cat in cats_with_hats:
                    cats_with_hats.remove(cat)
                else:
                    cats_with_hats.append(cat)
        checked_cats.clear()
        round += 1
    return cats_with_hats

# Поки що не дуже певен, що вмію рахувати складність операцій,
# але якщо правильно розумію, то тут вона O(n)
