from scipy.optimize import root

def solve_intersection(radius_squared, label):
    def equations(z):
        x, y = z
        return [
            x**2 + y**2 - radius_squared, 
            y - (x**2 - 1)                 
        ]

    print(f"--- {label} ---")
    for guess in ([1.0, 1.0], [-1.0, 1.0]):
        solution = root(equations, guess)
        print(f"Initial guess: {guess} -> Intersection [x, y]: {solution.x}")
        print(f"Residuals: {equations(solution.x)} | Converged: {solution.success}")
    print()

solve_intersection(4.0, "Original System (Radius^2 = 4)")

solve_intersection(9.0, "Parameter Changed (Radius^2 = 9)")

def market_equilibrium(z):
    Q, P = z
    return [
        P - (100.0 - Q**2),      
    
        P - (20.0 + 2.0 * Q**2) 
    ]

print("--- Real-World Case: Market Equilibrium ---")
eq_solution = root(market_equilibrium, [5.0, 50.0])
print(f"Equilibrium Quantity (Q): {eq_solution.x[0]:.4f} units")
print(f"Equilibrium Price (P):    ${eq_solution.x[1]:.2f}")
print(f"Residuals: {market_equilibrium(eq_solution.x)} | Converged: {eq_solution.success}")
