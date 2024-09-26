n = 8
my_dict = {i: ['*'] * i for i in range(1, n + 1)}
for i in range(0, n):
    print("".join(my_dict[i + 1]))
