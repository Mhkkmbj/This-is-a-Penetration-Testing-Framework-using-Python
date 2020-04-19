import pyshark

capture = pyshark.RemoteCapture('192.168.56.10/15', 'eth0')

capture.sniff(timeout=50)

capture
