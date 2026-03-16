import numpy as np

def rosenbrock(x):
    return (1-x[0])**2 + 100*(x[1]-x[0]**2)**2

def grad(x):
    dfdx = -2*(1-x[0]) - 400*x[0]*(x[1]-x[0]**2)
    dfdy = 200*(x[1]-x[0]**2)
    return np.array([dfdx,dfdy])

def hessian(x):
    h11 = 2 - 400*(x[1]-3*x[0]**2)
    h12 = -400*x[0]
    h21 = -400*x[0]
    h22 = 200
    return np.array([[h11,h12],[h21,h22]])

def steepest_descent(start, lr=0.001, iterations=5000):
    x = np.array(start,dtype=float)
    
    for i in range(iterations):
        x = x - lr*grad(x)
    
    return x, rosenbrock(x), iterations

def newton_method(start, iterations=20):
    x = np.array(start,dtype=float)
    
    for i in range(iterations):
        x = x - np.linalg.inv(hessian(x)).dot(grad(x))
    
    return x, rosenbrock(x), iterations

start = [-1.2,1]

sd = steepest_descent(start)
nm = newton_method(start)

print("Steepest Descent:", sd)
print("Newton Method:", nm)
