import time

from get_algorithm import get_algorithm
from generate_array import generate_array

def run_algorithm():
  func = get_algorithm()

  # Intialize runtime array
  runtime = []

  # Get current time for elapsed time.
  start_time = time.time()

  # Run function over 10,000 lists
  n = 10000
  for i in range(n):

    # print meta data
    print(f"Array number: {i + 1} out of 10,000, {round(((i + 1) / n) * 100, 2)}% Done\n")
    print(f"Time elapsed: {round(time.time() - start_time)}\n")

    # Generate arrays of length i + 1
    arr = generate_array(i + 1)

    # Start algorithm and its stopwatch
    runtime_start = time.process_time()
    _ = func(arr)
    runtime_end = time.process_time()

    # Append to runtime dump
    runtime.append(runtime_end - runtime_start)

  return runtime
