from project.classes.Surface import Surface

s = Surface(4, 5, 10)

for _ in range(10) :
    s.set_total_particle()

print(s.get_average_height())   # prints 5.0 -- working