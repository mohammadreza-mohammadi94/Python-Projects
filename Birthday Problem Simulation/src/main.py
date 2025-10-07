import random

def birthday_simulation(group_size=23, trials=1_000_000):
    same_birthday = 0
    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(group_size)]
        if len(birthdays) != len(set(birthdays)):
            same_birthday += 1
    return same_birthday / trials


if __name__ == "__main__":
    for n in [5, 10, 20, 23, 30, 50, 100]:
        p = birthday_simulation(group_size=n)
        print(f"Group of {n}: Probability of shared birthday: {p:.4f}")

