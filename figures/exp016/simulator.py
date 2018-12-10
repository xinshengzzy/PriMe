from mytools import utility
from mytools import ofd
import random

filename = "/home/zongyi/network_trace/CAIDA/trace1.txt"
prefix = "/home/zongyi/network_trace/CAIDA/trace"

def PriMe(memory, n_pkts):
	global filename
	flowCounter = utility.FlowCounter(filename, n_pkts)
	n_real_flow_records = str(flowCounter.get_flow_count())
	pktGenerator = utility.PcapFileObj(filename)
	n_buckets = int(memory*1024*1024/71)
	n_bits = 2*n_buckets
	alg = ofd.sim_PriMe(n_buckets)
	for i in range(n_pkts):
		pkt = pktGenerator.get_pkt()
		alg.insert_pkt(pkt)
	n_exports = str(alg.n_exports)
	n_checks = str(alg.n_checks)
	n_flow_records = str(alg.get_flow_record_count())
	return "\t".join([n_real_flow_records, n_exports, n_checks, n_flow_records])

if __name__ == "__main__":
	n_pkts = 5000000
	memory = 1.0
	with open("results.txt", "w") as f:
		print "#n_real_flow_records	n_exports	n_checks	n_flow_records"
		f.write("#n_real_flow_records	n_exports	n_checks	n_flow_records\n")
		for index in range(1, 11):
			filename = prefix + str(index) + ".txt"
			res = PriMe(memory, n_pkts)
			print res
			f.write(res + "\n")
