def generate_hint(guess, actual_value):
    if guess < actual_value:
        return "Try a higher number...⬆️"
    else:
        return "Try a lower number...⬇️"