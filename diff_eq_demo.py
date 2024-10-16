# Template for Diff Eq Solving
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the ODE function; custom ODE where y is dependent, t is independent
def ode(t, y):
    return -2 * y

# Define time points where we want the solution
t_span = (0, 5)  # Solve from t=0 to t=5
t_eval = np.linspace(0, 5, 100)  # 100 time points for evaluation

# Initial condition y(0) = 1
y0 = [1]

# Solve the ODE using solve_ivp
solution = solve_ivp(ode, t_span, y0, t_eval=t_eval)

# Plot the solution
plt.plot(solution.t, solution.y[0], label='Numerical solution y(t)')
plt.xlabel('Time t')
plt.ylabel('Solution y')
plt.title('ODE Demo')
plt.legend()
plt.grid(True)
plt.show()
