from scipy.optimize import root_scalar, newton

original_cash_flows = [-10000, 3000, 3500, 4000, 2500]

modified_cash_flows = [-10000, 3000, 3500, 4000, 4500]


def calculate_irr(cash_flows, label):

    def npv(rate):
        return sum(
            cf / (1 + rate)**t
            for t, cf in enumerate(cash_flows)
        )

    def d_npv(rate):
        return sum(
            -t * cf / (1 + rate)**(t + 1)
            for t, cf in enumerate(cash_flows)
            if t > 0
        )


    newton_result = newton(
        npv,
        x0=0.10,
        fprime=d_npv,
        tol=1e-12
    )


    secant_result = root_scalar(
        npv,
        x0=0.05,
        x1=0.20,
        method="secant",
        xtol=1e-12
    )

    print(f"--- {label} ---")
    print(f"IRR using Newton-Raphson: {newton_result:.6%}")
    print(f"IRR using Secant method:  {secant_result.root:.6%}")
    print(f"NPV at Newton solution:   {npv(newton_result):.6f}\n")


calculate_irr(original_cash_flows, "Original Cash Flows")

calculate_irr(modified_cash_flows, "Parameter Changed (Final Inflow = 4500)")

loan_flows = [-20000, 4500, 4500, 4500, 4500, 4500, 4500]

calculate_irr(loan_flows, "Real-World Case: Loan Effective Interest Rate")
