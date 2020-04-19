#! /usr/bin/python3


from nmap import nmap
nm = nmap.PortScanner()

nm.scan(hosts='192.168.56.10/15',arguments='-sX -PA21,22,9200')

nm.scan(hosts='192.168.56.10/15',arguments='sF -PA21,22,9200')

nm.scan(hosts='192.168.56.10/15',arguments='sS -PA21,22,9200')

hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
for host, status in hosts_list:
	print('{0}:{1}'.format(host, status))

f=open("t3.csv","w")
f.write(nm.csv())
