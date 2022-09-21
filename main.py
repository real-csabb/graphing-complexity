from run_algorithm import run_algorithm
from write_dumps import write_dumps
from graph_results import graph_results

if __name__ == '__main__':

  results = run_algorithm()
  file = write_dumps(results)
  graph_results(file)