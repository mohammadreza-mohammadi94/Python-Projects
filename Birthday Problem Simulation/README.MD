# Birthday Problem Simulation

This project is a Python simulation of the famous Birthday Problem. It demonstrates the surprisingly high probability of two people sharing a birthday in a relatively small group.

## The Birthday Problem

The birthday problem asks for the probability that, in a set of `n` randomly chosen people, at least two will share a birthday. The birthday paradox is that, counter-intuitively, the probability of a shared birthday exceeds 50% in a group of only 23 people.

The simulation demonstrates this by running a large number of trials for different group sizes and calculating the proportion of trials where a shared birthday is found.

## How to Run the Simulation

To run the simulation, navigate to the `src` directory and execute the `main.py` script from your terminal:

```bash
python main.py
```

## The Code

The simulation is implemented in the `main.py` file. It consists of one main function:

- `birthday_simulation(group_size, trials)`: Simulates the birthday problem for a given group size and number of trials.

The script runs the simulation for several group sizes (5, 10, 20, 23, 30, 50, 100) and prints the probability of a shared birthday for each group size.

## Expected Output

When you run the script, you will see an output similar to the following:

```
Group of 5: Probability of shared birthday: 0.0271
Group of 10: Probability of shared birthday: 0.1170
Group of 20: Probability of shared birthday: 0.4114
Group of 23: Probability of shared birthday: 0.5073
Group of 30: Probability of shared birthday: 0.7063
Group of 50: Probability of shared birthday: 0.9704
Group of 100: Probability of shared birthday: 1.0000
```

This output demonstrates that with a group of just 23 people, the probability of a shared birthday is over 50%.
