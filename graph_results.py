import sys
import json
import matplotlib.pyplot as plt

def main():
    if (len(sys.argv) > 1):
        filename = sys.argv[1]
    else:
        raise Exception("Error. No file given.")

    graph_results(filename)

def graph_results(data, meta=""):

    # Open runtime dump
    with open (data, 'r') as f:
        runtime = json.load(f)

    # Initialize the graph
    fig, ax = plt.subplots()
    ax.scatter(range(len(runtime)), runtime)

    # Graph labels using metadata
    try:
        # Open runtime meta
        with open(meta, 'r') as f:
            meta = json.load(f)

        # Graph labels using meta
        plt.title(meta["title"])
        plt.xlabel(meta["x"])
        plt.ylabl(meta["y"])

    # If meta does not exist
    except:
        # Use these default labels
        plt.title("Time-Complexity")
        plt.xlabel("Array Size")
        plt.ylabel("Fractional Seconds")

    # Display graph
    plt.show()

if __name__ == "__main__":
    main()