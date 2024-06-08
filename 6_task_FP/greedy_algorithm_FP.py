
def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            chosen_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']

    return chosen_items, total_cost, total_calories


def dynamic_programming(items, budget):
    dp_table = [[0] * (budget + 1) for _ in range(len(items) + 1)]

    for i, (item, info) in enumerate(items.items(), start=1):
        for j in range(1, budget + 1):
            if info['cost'] > j:
                dp_table[i][j] = dp_table[i - 1][j]
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i - 1][j - info['cost']] + info['calories'])

    chosen_items = []
    total_calories = dp_table[len(items)][budget]
    j = budget

    for i in range(len(items), 0, -1):
        if dp_table[i][j] != dp_table[i - 1][j]:
            item = list(items.keys())[i - 1]
            chosen_items.append(item)
            j -= items[item]['cost']

    chosen_items.reverse()
    total_cost = sum(items[item]['cost'] for item in chosen_items)

    return chosen_items, total_cost, total_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print("Greedy Algorithm:")
print("Chosen items:", greedy_result[0])
print("Total cost:", greedy_result[1])
print("Total calories:", greedy_result[2])

print("\nDynamic Programming:")
print("Chosen items:", dp_result[0])
print("Total cost:", dp_result[1])
print("Total calories:", dp_result[2])
