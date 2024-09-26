import sys


# create a list from a file
def read_file(file):
    with open(file, 'r') as file:
        return [int(x) for x in file.read().split()]


# write a line to given file
def write_file(file_name, line):
    with open(file_name, 'w') as f:
        f.write("")  # clear the file
    with open(file_name, 'a') as file:
        file.write(line)


# control if given list is sorted
def is_sorted(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True


# apply insertion sort algorithm to a list
def insertion_sort(numbers):
    output = ""
    for i in range(1, len(numbers)):
        j = i
        while j > 0 and numbers[j - 1] > numbers[j]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            j -= 1
        new_numbers = " ".join([str(i) for i in numbers])
        output += f"Pass {i}: {new_numbers}\n"
        if is_sorted(numbers):
            return output.strip()


# apply bubble sort algorithm to a list
def bubble_sort(numbers):
    output = ""
    counter = 1
    while not is_sorted(numbers):
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        new_numbers = " ".join([str(i) for i in numbers])
        output += f"Pass {counter}: {new_numbers}\n"
        counter += 1
    return output.strip()


def main():
    if len(sys.argv) != 4:
        print("Usage: python sort.py <input_file> <output_bubble> <output_insertion>")
        return

    input_file = sys.argv[1]
    output_bubble = sys.argv[2]
    output_insertion = sys.argv[3]

    numbers = read_file(input_file)
    bubble_sorted = bubble_sort(read_file(input_file))
    insertion_sorted = insertion_sort(read_file(input_file))

    if is_sorted(numbers):
        write_file(output_bubble, "Already sorted!")
        write_file(output_insertion, "Already sorted!")
    else:
        write_file(output_bubble, bubble_sorted)
        write_file(output_insertion, insertion_sorted)


main()
