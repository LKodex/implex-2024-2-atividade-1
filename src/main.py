import sys
import time
import random
from functools import reduce
from implex.sort import bubble, insertion, merge, heap, quick, counting

helpFlags = [
    "h",
    "help",
    "?"
]

def run_experiments(algorithms, inc, fim, stp, rpt, vector_generator, label):
    print(f"[[{label}]]")
    
    print(f"{'n':<10}", end="")
    for alg_name in algorithms.keys():
        print(f"{alg_name:<15}", end="")
    print()
    
    for n in range(inc, fim + 1, stp):
        print(f"{n:<10}", end="")
        for alg_name, alg_func in algorithms.items():
            total_time = 0
            for _ in range(rpt):
                arr = vector_generator(n)
                start_time = time.time()
                alg_func.sort(arr)
                end_time = time.time()
                total_time += end_time - start_time
            avg_time = total_time / rpt
            print(f"{avg_time:<15.6f}", end="")
        print()

def generate_random_array(n):
    import random
    return [random.randint(0, n ** 2) for _ in range(n)]

def generate_reverse_array(n):
    return list(range(n, 0, -1))

def generate_sorted_array(n):
    return list(range(1, n + 1))

def generate_nearly_sorted_array(n):
    arr = list(range(1, n + 1))
    num_to_shuffle = max(1, n // 10)  # 10% do array
    indices = random.sample(range(n), num_to_shuffle)
    for i in indices:
        swap_with = random.randint(0, n - 1)
        arr[i], arr[swap_with] = arr[swap_with], arr[i]
    return arr

def cli():
    argsQuantity = len(sys.argv)
    # isHelpFlagTrue = False
    for arg in sys.argv:
        # isFlag = arg.startswith(("-", "--", "/"))
        isHelpRequest = reduce(lambda isHelp, helpFlag : isHelp or helpFlag in arg, helpFlags, False)
        if isHelpRequest:
            break
    if isHelpRequest:
        programName = sys.argv[0]
        print(f"Usage: {programName} <inc> <fim> <stp> <rpt>", file=sys.stderr)
        print("inc\t<-- é o tamanho inicial de um vetor de entrada")
        print("fim\t<-- é o tamanho final")
        print("stp\t<-- é o intervalo entre dois tamanhos")
        print("inc\t<-- é o número de repetições a serem realizadas")
        sys.exit(0)
    elif argsQuantity != 5:
        programName = sys.argv[0]
        print(f"Usage: {programName} <inc> <fim> <stp> <rpt>", file=sys.stderr)
        sys.exit(1)
    

if __name__ == "__main__":
    algorithms = {
        "BubbleSort": bubble,
        "InsertionSort": insertion,
        "MergeSort": merge,
        "HeapSort": heap,
        "QuickSort": quick,
        "CountingSort": counting
    }
    inc = int(sys.argv[1])
    fim = int(sys.argv[2])
    stp = int(sys.argv[3])
    rpt = int(sys.argv[4])

    run_experiments(algorithms, inc, fim, stp, rpt, generate_random_array, "RANDOM")
    run_experiments(algorithms, inc, fim, stp, rpt, generate_reverse_array, "REVERSE")
    run_experiments(algorithms, inc, fim, stp, rpt, generate_sorted_array, "SORTED")
    run_experiments(algorithms, inc, fim, stp, rpt, generate_nearly_sorted_array, "NEARLY SORTED")

