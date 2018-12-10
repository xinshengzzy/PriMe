import matplotlib.pyplot as plt
import matplotlib
import matplotlib
import np
from matplotlib.patches import Ellipse

font = {'size':18}
matplotlib.rc('font', **font)


def parse_file(filename):
    alpha = []
    cr_ofd = []
    cr_ofd_ci = []
    cr_hashpipe = []
    cr_normalhash = []
    with open(filename, "r") as f:
        for line in f:
            if "#" == line[0]:
                continue
            items = line.split("\t")
            alpha.append(float(items[0]))
            cr_ofd.append(float(items[1]))
            cr_ofd_ci.append(float(items[2]))
            cr_hashpipe.append(float(items[3]))
            cr_normalhash.append(float(items[4]))
    return alpha, cr_ofd, cr_ofd_ci, cr_hashpipe, cr_normalhash

if __name__ == "__main__":
    alpha, cr_ofd, cr_ofd_ci, cr_hashpipe, cr_normalhash = parse_file("./collision_rates.txt")

    plt.figure(1)
    plt.ylim(0, 1.0)
    plt.plot(alpha, cr_ofd, label = "OFD", marker = "x", markersize=10)
    plt.plot(alpha, cr_ofd_ci, label = "OFD-CI", marker = "^", markersize=10)
    plt.plot(alpha, cr_hashpipe, label = "HashPipe", marker = "<", markersize=10)
    plt.plot(alpha, cr_normalhash, label = "NormalHash", marker = "o", markersize=10)
    plt.legend(bbox_to_anchor=(0.0, 1.02, 1.0, 0.102), loc = 3, ncol = 2, mode = "expand", borderaxespad = 0.0)
    plt.xlabel("Skewing Factor")
    plt.ylabel("Collision Rate")
    plt.savefig("collision_rate.pdf", bbox_inches = "tight")
    plt.savefig("collision_rate.png", bbox_inches = "tight")
    plt.show()
