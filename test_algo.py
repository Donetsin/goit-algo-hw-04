import timeit
import generate_data as gen
import merge_sort as msrt
import insertion_sort as isrt
import tim_sort as tsrt

def test_sorting_algorithm(sort_func, data_generator, size, num_runs=10):
    data = data_generator(size)
    elapsed_time = timeit.timeit(lambda: sort_func(data[:]), number=num_runs) / num_runs
    return elapsed_time

sizes = [1000, 10000, 100000]
data_generators = [gen.generate_random_data, gen.generate_sorted_data, gen.generate_reverse_sorted_data, gen.generate_partially_sorted_data]
sort_functions = [msrt.merge_sort, isrt.insertion_sort, tsrt.tim_sort]

results = {}

for size in sizes:
    for data_gen in data_generators:
        for sort_func in sort_functions:
            key = (size, data_gen.__name__, sort_func.__name__)
            time = test_sorting_algorithm(sort_func, data_gen, size)
            results[key] = time
            print(f"Size: {size}, Data: {data_gen.__name__}, Sort: {sort_func.__name__}, Time: {time:.6f} seconds")