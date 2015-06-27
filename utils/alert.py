import smtplib
import sys
import config

def send_message(hostname):
	print 'setting up message'

	# Pull config from ini
	mail_config = config.get_config('email')

	sender = mail_config['sender']
	to = [mail_config['to']]

	subject = 'Server Outage!'

	message = "Your server hosted at %s is experiencing an outage!" % (hostname)

	try:
		smtp_srv = '{0}:{1}'.format(mail_config['hostname'], mail_config['port'])

		mail = smtplib.SMTP(smtp_srv)

		m = "From: %s\r\nTo: %s\r\nSubject: %s\r\nX-Mailer: My-Mail\r\n\r\n" % (sender, to, subject)

		mail.ehlo()
		mail.starttls()
		mail.login(mail_config['username'], mail_config['password'])
		mail.sendmail(sender, to, m + message)  

		print "Successfully sent email"
	except SMTPException:
		print "Error: unable to send email"

	sys.exit()