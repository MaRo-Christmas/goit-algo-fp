
import random

def simulate_dice_rolls(num_rolls):
    results = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        results[roll1 + roll2] += 1
    
    probabilities = {k: v / num_rolls * 100 for k, v in results.items()}
    
    return probabilities

def main():
    num_rolls = 1000000
    monte_carlo_probabilities = simulate_dice_rolls(num_rolls)
    print("Monte Carlo Probabilities:")
    for total, probability in monte_carlo_probabilities.items():
        print(f"Total {total}: {probability:.2f}%")

    # Аналітичні значення
    var_pro = {
        '2': 2.78,
        '3': 5.56,
        '4': 8.33,
        '5': 11.11,
        '6': 13.89,
        '7': 16.67,
        '8': 13.89,
        '9': 11.11,
        '10': 8.33,
        '11': 5.56,
        '12': 2.78,
    }
    
    print("\nAnalytical Probabilities:")
    for total, probability in var_pro.items():
        print(f"Total {total}: {probability:.2f}%")

if __name__ == "__main__":
    main()
