from utils import http_utils as http
from utils import alert

import sys
import threading

def start_scan():
	status = http.check_url_live(hostname)

	if status is not 200:
		print 'Alerting!'
		
		alert.send_message(hostname)

	threading.Timer(5, start_scan).start()

if __name__ == '__main__':
	print '''
		    __                    __  __               __ 
		   / /_  ___  ____ ______/ /_/ /_  ___  ____ _/ /_
		  / __ \/ _ \/ __ `/ ___/ __/ __ \/ _ \/ __ `/ __/
		 / / / /  __/ /_/ / /  / /_/ /_/ /  __/ /_/ / /_  
		/_/ /_/\___/\__,_/_/   \__/_.___/\___/\__,_/\__/  
		                                                  '''

	if len(sys.argv) < 2:
		print ''                                         
		print 'Usage: heartbeat.py <server_url/ip>'
	else:
		hostname = sys.argv[1]

		print 'Monitoring Server'
		start_scan()