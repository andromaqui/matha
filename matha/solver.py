from scipy.optimize import minimize
import numpy as np

class Solver:
    def __init__(self, parsed_tokens: dict) -> None:
        self.parsed_tokens = parsed_tokens

    def solve(self):
        func_tokens = self.parsed_tokens["forward"]["expr"]
        func = ''.join(func_tokens)

        observed_tokens = self.parsed_tokens["data"]["observed"]
        observed = np.array(observed_tokens)

        x_values_tokens = self.parsed_tokens["data"]["x_values"]
        x_values = np.array(x_values_tokens)

        b_estimates = observed - x_values
        b = np.mean(b_estimates)
        print("Solved b:", b)

