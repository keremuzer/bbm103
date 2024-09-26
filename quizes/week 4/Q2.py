print("x² + bx + c = 0")
b = int(input("enter b: "))
c = int(input("enter c: "))
discriminant = b**2 - 4*c
if discriminant < 0:
    print("the equation has no real roots")
elif discriminant > 0:
    print(f"x = {(-1 * b + discriminant**(1 / 2)) / 2}\nx = {(-1 * b - discriminant**(1 / 2)) / 2}")
else:
    print(f"x = {(-1 * b + discriminant ** (1 / 2)) / 2}")
