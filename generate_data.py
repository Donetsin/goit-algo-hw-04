import random

def generate_random_data(size):
    return [random.randint(0, 100000) for _ in range(size)]

def generate_sorted_data(size):
    return list(range(size))

def generate_reverse_sorted_data(size):
    return list(range(size, 0, -1))

def generate_partially_sorted_data(size):
    data = generate_sorted_data(size)
    for _ in range(size // 10):
        i, j = random.randint(0, size - 1), random.randint(0, size - 1)
        data[i], data[j] = data[j], data[i]
    return data