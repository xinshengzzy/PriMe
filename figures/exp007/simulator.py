from mytools import utility
from mytools import OFD
import random

if __name__ == "__main__":
	n_buckets = 1000
	n_flows = 10000
	n_pkts = 1000000
	outfile = open("collision_rates.txt", "w")
	outfile.write("#alpha	OFD	OFD_CI	HashPipe	NormalHash\n")
	for i in range(1, 21):
		alpha = 0.1*i
		collision_rates = [str(alpha)]
		
		n_collision = 0
		for k in range(5):
			pktGenerator = utility.ZipfPktGenerator(n_flows, n_pkts, alpha)
			alg = OFD.sim_OFD(n_buckets)
			for i in range(n_pkts):
				pkt = pktGenerator.get_pkt()
				alg.insert_pkt(pkt)
			n_collision = n_collision + alg.n_collision
		n_collision = n_collision/5
		collision_rates.append(str(n_collision/float(n_pkts)))

		n_collision = 0
		for k in range(5):
			pktGenerator = utility.ZipfPktGenerator(n_flows, n_pkts, alpha)
			alg = OFD.sim_OFD_CI(n_buckets)
			for i in range(n_pkts):
				pkt = pktGenerator.get_pkt()
				alg.insert_pkt(pkt)
			n_collision = n_collision + alg.n_collision
		n_collision = n_collision/5
		collision_rates.append(str(n_collision/float(n_pkts)))

		n_collision = 0
		for k in range(5):
			pktGenerator = utility.ZipfPktGenerator(n_flows, n_pkts, alpha)
			alg = OFD.sim_HashPipe(n_buckets)
			for i in range(n_pkts):
				pkt = pktGenerator.get_pkt()
				alg.insert_pkt(pkt)
			n_collision = n_collision + alg.n_collision
		n_collision = n_collision/5
		collision_rates.append(str(n_collision/float(n_pkts)))

		n_collision = 0
		for k in range(5):
			pktGenerator = utility.ZipfPktGenerator(n_flows, n_pkts, alpha)
			alg = OFD.sim_NormalHash(n_buckets)
			for i in range(n_pkts):
				pkt = pktGenerator.get_pkt()
				alg.insert_pkt(pkt)
			n_collision = n_collision + alg.n_collision
		n_collision = n_collision/5
		collision_rates.append(str(n_collision/float(n_pkts)))

		print collision_rates
		outfile.write("\t".join(collision_rates) + "\n")
	outfile.close()
