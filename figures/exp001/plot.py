import matplotlib.pyplot as plt
import matplotlib
import matplotlib
import np
from matplotlib.patches import Ellipse

font = {'size':22}
matplotlib.rc('font', **font)


def parse_file(filename):
    cr_prime = []
    cr_normalhash = []
    with open(filename, "r") as f:
        for line in f:
            if "#" == line[0]:
                continue
            items = line.split("\t")
            cr_prime.append(float(items[0]))
            cr_normalhash.append(float(items[1]))
    return cr_prime, cr_normalhash

if __name__ == "__main__":
    cr_prime, cr_normalhash = parse_file("./collision_rates.txt")

    plt.figure(1)
    plt.xticks(range(10), ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10"))
    plt.ylim(0, 0.5)
    plt.plot(range(10), cr_prime, label = "PriMe", marker = "x", markersize=10)
    plt.plot(range(10), cr_normalhash, label = "TurboFlow", marker = "o", markersize=10)
    plt.legend(bbox_to_anchor=(0.0, 1.02, 1.0, 0.102), loc = 3, ncol = 2, mode = "expand", borderaxespad = 0.0)
    plt.xlabel("Traces")
    plt.ylabel("Eviction Rate")
    plt.savefig("eviction_rate.eps", bbox_inches = "tight")
    plt.savefig("eviction_rate.png", bbox_inches = "tight")
