import sys
import importlib as imp

def get_algorithm():
    if (len(sys.argv) > 2): 
        # File path of the algorithm
        module = imp.import_module(sys.argv[1])

        # Function name of the algorithm
        func = getattr(module, sys.argv[2])
    else:
        raise Exception("Error. Not enough arguments.")

    return func