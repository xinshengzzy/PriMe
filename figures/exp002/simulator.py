from mytools import utility
from mytools import OFD
import random

if __name__ == "__main__":
	memory = 2.0
	path = "/home/zongyi/network_trace/HGC/"
	filenames = []
	for i in range(1, 11):
		filename = path + "trace" + str(i) + ".txt"
		filenames.append(filename)
	n_lines = [10314013, 10349753, 10308838, 10284767, 10326758, 10349150, 10288650, 10304861, 10274171, 10255910]
	outfile = open("collision_rates.txt", "a")
	outfile.write("#OFD	OFD_CI	HashPipe	NormalHash\n")
	for i in range(4, 10):
		filename = filenames[i]
		n_pkts = n_lines[i]
		collision_rates = []

		n_buckets = int(memory*1024*1024/18)
		fileObj = utility.PcapFileObj(filename)
		alg = OFD.sim_OFD(n_buckets)
		for i in range(n_pkts):
			pkt = fileObj.get_pkt()
			alg.insert_pkt(pkt)
		n_collision_ofd = alg.n_collision
		collision_rates.append(str(n_collision_ofd/float(n_pkts)))

		n_buckets = int(memory*1024*1024/18)
		fileObj = utility.PcapFileObj(filename)
		alg = OFD.sim_OFD_CI(n_buckets)
		for i in range(n_pkts):
			pkt = fileObj.get_pkt()
			alg.insert_pkt(pkt)
		n_collision_ofd_ci = alg.n_collision
		collision_rates.append(str(n_collision_ofd_ci/float(n_pkts)))

		n_buckets = int(memory*1024*1024/17)
		fileObj = utility.PcapFileObj(filename)
		alg = OFD.sim_HashPipe(n_buckets)
		for i in range(n_pkts):
			pkt = fileObj.get_pkt()
			alg.insert_pkt(pkt)
		n_collision_hashpipe = alg.n_collision
		collision_rates.append(str(n_collision_hashpipe/float(n_pkts)))

		n_buckets = int(memory*1024*1024/17)
		fileObj = utility.PcapFileObj(filename)
		alg = OFD.sim_NormalHash(n_buckets)
		for i in range(n_pkts):
			pkt = fileObj.get_pkt()
			alg.insert_pkt(pkt)
		n_collision_normalhash = alg.n_collision
		collision_rates.append(str(n_collision_normalhash/float(n_pkts)))

		print collision_rates
		outfile.write("\t".join(collision_rates) + "\n")
	outfile.close()
