import time
from sort import sort


def run_benchmark():
    sizes = [100, 500, 700]
    algorithms = ["quick", "insert", "merge"]
    
    print("=" * 70)
    print(f"{'Алгоритм':<12} | {'n=100':<12} | {'n=500':<12} | {'n=700':<12}")
    print("=" * 70)
    
    for algo in algorithms:
        times = []
        for n in sizes:
            arr = [{"value": i} for i in range(n, 0, -1)]
            
            arr_copy = arr.copy()
            start = time.perf_counter()
            sort(arr_copy, by="value", reverse=False, algo=algo)
            end = time.perf_counter()
            
            times.append(f"{end - start:.6f}")
        
        print(f"{algo:<12} | {times[0]:<12} | {times[1]:<12} | {times[2]:<12}")
    
    print("=" * 70)


if __name__ == "__main__":
    run_benchmark()