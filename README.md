forward y = x + b 
data observed = [2.1, 3.2, 4.0, 5.1]  # corresponding to x = [1,2,3,4]

inverse estimate_b(observed) -> b
    using y = x + b
    regularize l2(0.01)
    noise gaussian(0.1)