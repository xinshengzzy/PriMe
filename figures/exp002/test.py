import re
from mytools import utility
line = "hello, [world] good [ok]."
print line
line = re.sub(r"\[([^\[\]])*\]", "", line)
print line
exit()
with open("/home/zongyi/network_trace/HGC/trace1.txt", "r") as f:
	for line in f:
#		print line
		line = line.decode("utf-8", errors = "ignore").strip()
		continue
		items = line.split(" ")
		items = utility.sift_list(items)
		print items
		print utility.locate_item_in_list(items, u"\u2192")
		print [str(items[2]), items[4], items[5], items[7], items[9]]
		exit()
		line = line.replace(u"\u2192", "to")
		items = line.split(" ")
		items = utility.sift_list(items)
		if False == utility.is_ip_add(items[2]) or False == utility.is_ip_add(items[4]):
			print line,
