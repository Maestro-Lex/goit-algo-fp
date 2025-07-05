# Adjusting the code to use a dictionary for items instead of a list of tuples.

# Define the items with their cost and calorie value.
ITEMS = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


# Greedy approach
def greedy_algorithm(items: dict, budget: int) -> dict:
    items = items.copy()
    total_calories = 0
    remaining_budget = budget
    chosen_items = []
    while True:
        max_ = max(items.items(), key = lambda x: x[1]["calories"] / x[1]["cost"])
        if remaining_budget - max_[1]["cost"] < 0:
            break
        chosen_items.append(max_[0])
        del items[max_[0]]
        remaining_budget -= max_[1]["cost"]
        total_calories += max_[1]["calories"]

    return {
        "total_calories": total_calories,
        "spended": budget - remaining_budget,
        "result": chosen_items
    }


# Dynamic Programming approach
def dynamic_programming(items, budget):
    item_names = list(items.keys())

    # Create a DP table where rows represent up to the i-th item and columns represent budget
    dp_table = [[0 for x in range(budget + 1)] for y in range(len(items) + 1)]

    for i in range(1, len(item_names) + 1):
        name = item_names[i - 1]
        cost = items[name]['cost']
        calories = items[name]['calories']
        for b in range(budget + 1):
            if cost > b:
                dp_table[i][b] = dp_table[i - 1][b]
            else:
                dp_table[i][b] = max(dp_table[i - 1][b], dp_table[i - 1][b - cost] + calories)

    chosen_items = []
    temp_budget = budget

    for i in range(len(item_names), 0, -1):
        if dp_table[i][b] != dp_table[i - 1][b]:
            name = item_names[i - 1]
            chosen_items.append(name)
            b -= items[name]['cost']
            temp_budget -= items[name]['cost']

    return {
        "total_calories": dp_table[len(items)][budget],
        "spended": budget - temp_budget,
        "result": chosen_items
    }


if __name__ == '__main__':
    # Execute both algorithms
    budget = 100

    greedy_result = greedy_algorithm(ITEMS, budget)
    dp_result = dynamic_programming(ITEMS, budget)
    
    print("Результат роботи жадібного алгоритму:")
    print(greedy_result)
    print("Результат роботи динамічного програмування:")
    print(dp_result)