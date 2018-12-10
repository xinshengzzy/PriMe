import matplotlib.pyplot as plt
import matplotlib
import matplotlib
import np
from matplotlib.patches import Ellipse

font = {'size':22}
matplotlib.rc('font', **font)


def parse_file(filename):
    memory = []
    n_exports = []
    n_aggre = []
    n_fr = []
    with open(filename, "r") as f:
        for line in f:
            if "#" == line[0]:
                continue
            items = line.split("\t")
            memory.append(float(items[0]))
            n_exports.append(int(items[1]))
            n_aggre.append(int(items[2]))
            n_fr.append(int(items[3]))
    return memory, n_exports, n_aggre, n_fr

if __name__ == "__main__":
    n_pkts = 5000000
    n_real_fr_hgc = 526153
    n_real_fr_caida = 302675

    memory, n_exports, n_aggre, n_fr = parse_file("./caida_results.txt")
    caida_aggre_rate = []
    caida_redundancy = []
    for i in range(len(n_aggre)):
        caida_aggre_rate.append(n_aggre[i]/float(n_pkts))
        caida_redundancy.append(1.0 - float(n_real_fr_caida)/n_fr[i])
    memory, n_exports, n_aggre, n_fr = parse_file("./hgc_results.txt")
    hgc_aggre_rate = []
    hgc_redundancy = []
    for i in range(len(n_aggre)):
        hgc_aggre_rate.append(n_aggre[i]/float(n_pkts))
        hgc_redundancy.append(1.0 - float(n_real_fr_hgc)/n_fr[i])

    print("hgc_redundancy:")
    print(hgc_redundancy)
    print("caida_redundancy:")
    print(caida_redundancy)

    print("hgc_aggre_rate:")
    print(hgc_aggre_rate)
    print("caida_aggre_rate:")
    print(caida_aggre_rate)

    plt.figure(1)
#    plt.xticks(range(10), ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10"))
    plt.ylim(0, 0.5)
    plt.plot(memory, caida_aggre_rate, label="CAIDA", marker = "x", markersize=10)
    plt.plot(memory, hgc_aggre_rate, label="HGC", marker = "o", markersize=10)
    plt.legend(bbox_to_anchor=(0.0, 1.02, 1.0, 0.102), loc = 3, ncol = 2, mode = "expand", borderaxespad = 0.0)
    plt.xlabel("Memory")
    plt.ylabel("Aggregation Rate")
    plt.savefig("aggregation_rate.eps", bbox_inches = "tight")
    plt.savefig("aggregation_rate.png", bbox_inches = "tight")

    plt.figure(2)
    plt.ylim(0, 1.0)
    plt.plot(memory, caida_redundancy, label="CAIDA", marker='x', markersize=10)
    plt.plot(memory, hgc_redundancy, label="HGC", marker='o', markersize=10)
    plt.legend(bbox_to_anchor=(0.0, 1.02, 1.0, 0.102), loc = 3, ncol = 2, mode = "expand", borderaxespad = 0.0)
    plt.xlabel("Memory")
    plt.ylabel("Redundancy")
    plt.savefig("redundancy.eps", bbox_inches = "tight")
    plt.savefig("redundancy.png", bbox_inches = "tight")
