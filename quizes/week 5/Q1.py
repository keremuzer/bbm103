N = int(input("Enter a number: "))
odd_numbers = 0
even_numbers = 0
count = 0
for i in range(1, N + 1):
    if i % 2 != 0:
        odd_numbers += i
    else:
        even_numbers += i
        count += 1

print(f"sum of odd numbers from 1 to {N} = {odd_numbers}")
if count != 0:
    print(f"average of even numbers from 1 to {N} = {even_numbers / count}")
else:
    print(f"average of even numbers from 1 to {N} = {even_numbers}")
