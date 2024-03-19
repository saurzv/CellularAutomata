from project.classes.Surface import Surface

row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
theta_dep = float(input("Enter the value of theta_dep: "))
theta_max = int(input("Enter the theta_max: "))     # Max height
Z = int(input("Enter the value of Z: "))
tau = float(input("Enter the value of tau: "))
freq = int(input("Enter the value of saving freq: "))

surface = Surface(row, col, theta_dep, theta_max, Z, tau, freq)

roughness_array = []
