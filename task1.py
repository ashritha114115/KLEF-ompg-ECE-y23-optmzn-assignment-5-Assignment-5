import sympy as sp

# define variables
x1, x2, x3, x4, x5 = sp.symbols('x1 x2 x3 x4 x5')

# define function
f = x1**2 + x2**2 + x3**2 + x4**2 + (1/4)*x5**4 - 2*x5**2

# gradient
grad = [sp.diff(f, var) for var in (x1, x2, x3, x4, x5)]

print("Gradient:")
print(grad)

# solve critical points
critical = sp.solve(grad, (x1, x2, x3, x4, x5))

print("\nCritical Points:")
print(critical)

# evaluate function at critical points
for point in critical:
    val = f.subs({x1:point[0], x2:point[1], x3:point[2], x4:point[3], x5:point[4]})
    print("Point:", point, "Function Value:", val)
