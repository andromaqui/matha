# Matha: A Language for Inverse Problems

Matha is a domain-specific programming language designed to make inverse problems accessible through natural, mathematical syntax. Instead of writing complex optimization code, scientists and researchers can express inverse problems in intuitive mathematical notation.

## Overview

Inverse problems involve determining unknown parameters from observed data given a forward model. Matha allows you to:

1. **Define forward models** using natural mathematical syntax
2. **Specify observational data** with simple array notation  
3. **Solve inverse problems** automatically with built-in parameter estimation

## Quick Example

```matha
forward y = x + b
data observed = [2.1, 3.2, 4.0, 5.1] 
data x_values = [1, 2, 3, 4] 
inverse estimate(observed, x_values) -> b 
    using y
```

**Result:** `b = 1.1` (automatically estimated from noisy data)

## Language Syntax

### Forward Models
Define the mathematical relationship between variables:
```matha
forward y = x + b
```

### Data Specification
Provide observational data and input values:
```matha
data observed = [2.1, 3.2, 4.0, 5.1]
data x_values = [1, 2, 3, 4]
```

### Inverse Problems
Specify which parameters to estimate:
```matha
inverse estimate(observed, x_values) -> b
    using y
```

## Installation & Usage

### Prerequisites
- Python 3.11+
- NumPy
- SciPy

### Setup
```bash
git clone https://github.com/andromaqui/matha
cd matha
pip install numpy scipy
```

### Interactive Mode
```bash
python reply.py
```

## Architecture

Matha follows a traditional interpreter architecture:

1. **Lexer** (`lexer.py`) - Tokenizes Matha source code
2. **Parser** (`parser.py`) - Builds abstract syntax trees from tokens
3. **Solver** (`solver.py`) - Executes inverse problem solving using numerical methods

## Current Features

- ✅ Linear forward models (`y = x + b`)
- ✅ Array data specification
- ✅ Automatic parameter estimation
- ✅ Interactive REPL
- ✅ Basic error handling

## Planned Features

- [ ] Nonlinear forward models (`y = a*x^2 + b*x + c`)
- [ ] Multiple parameter estimation
- [ ] Regularization support (`l2`, `l1`)
- [ ] Noise modeling (`gaussian`, `uniform`)
- [ ] Uncertainty quantification
- [ ] Advanced optimization methods

## Research Goals

Matha aims to bridge the gap between mathematical formulation and computational implementation of inverse problems. By providing domain-specific syntax, we enable:

- **Faster prototyping** of inverse problem solutions
- **Improved readability** of scientific computing code
- **Reduced cognitive load** for domain experts
- **Better reproducibility** through clear problem specification
