from scipy.optimize import curve_fit
import numpy as np
import re

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

        if self.is_polynomial(func):
            coeffs = np.polyfit(x_values, observed, 2)
            coeffs.tolist()
            return None

        elif self.is_exponential(func):
            return self.solve_exponential(func, x_values, observed)

        else:
            b_estimates = observed - x_values
            b = np.mean(b_estimates)
            return b

    def is_polynomial(self, expr: str):
        expr = expr.replace(" ", "")
        polynomial_pattern = r'^[+-]?(\d*\.?\d*\*?[a-zA-Z]\^?\d*|\d+\.?\d*)([+-]\d*\.?\d*\*?[a-zA-Z]\^?\d*|[+-]\d+\.?\d*)*$'

        return bool(re.match(polynomial_pattern, expr))

    def is_exponential(self, expr: str):
        expr = expr.replace(" ", "")
        exp_pattern = r'.*exp\(.*\)'
        return bool(re.search(exp_pattern, expr))

    def solve_exponential(self, func, x_values, observed):
        if self.matches_pattern(func, "a*exp(b*x)"):
            return self.fit_exp_ab(x_values, observed)
        else:
            raise ValueError(f"Unsupported exponential pattern: {func}")

    def matches_pattern(self, expr, pattern):
        expr_clean = expr.replace(" ", "")
        pattern_clean = pattern.replace(" ", "")
        return expr_clean == pattern_clean

    def fit_exp_ab(self, x_values, observed):
        def model(x, a, b):
            return a * np.exp(b * x)
        try:
            params= curve_fit(model, x_values, observed)
            return list(params[0])
        except:
            raise ValueError("Failed to fit exponential function")



