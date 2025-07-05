import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# Аналітичні ймовірності
PROBS = {
    "2": 1/36,
    "3": 2/36,
    "4": 3/36,
    "5": 4/36,
    "6": 5/36,
    "7": 6/36,
    "8": 5/36,
    "9": 4/36,
    "10": 3/36,
    "11": 2/36,
    "12": 1/36
}


def simulate_dice_rolls(num_rolls):
    '''
    Розрахунок статистичних ймовірностей
    '''
    results = [random.randint(1, 6) + random.randint(1, 6) for _ in range(num_rolls)]
    results = Counter(results)    
    probabilities = {}
    for i in range(2, 13):
        probabilities[i] = results[i] / num_rolls    
    return probabilities


def plot_probabilities(probabilities):
    '''
    Побудова зведеної гістограми
    '''
    sums = list(PROBS.keys()) # суми чисел на кубиках
    x = np.arange(len(sums)) 
    width = 0.15 
    multiplier = -1

    fig, ax = plt.subplots(figsize=(15, 8), layout='constrained')

    for exp, results in probabilities.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, results.values(), width, label = exp)
        ax.bar_label(
            rects,
            labels=[f'{v * 100:.2f}%' for v in results.values()],
            padding = 3,
            rotation = 90
        )
        multiplier += 1

    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми чисел на двох кубиках')
    ax.set_xticks(x + width, sums)
    ax.legend(loc='upper left', ncols=5)    
    max_bar_height = max(max(value.values()) for value in probabilities.values())
    ax.set_ylim(0, max_bar_height * 1.2)
    plt.show()


def main():
    data = {}
    data["analitical"] = PROBS.copy()
    for accuracy in [100, 1000, 10000, 100000]:
        # Симуляція кидків і обчислення ймовірностей
        probabilities = simulate_dice_rolls(accuracy)
        data[f"{str(accuracy)} exp"] = probabilities

    # Відображення ймовірностей на графіку    
    plot_probabilities(data)


if __name__ == "__main__":
    main()