import httplib

def check_url_live(hostname):
	conn = httplib.HTTPConnection(hostname)
	conn.request("HEAD", "/")
	r1 = conn.getresponse()

	return r1.status
