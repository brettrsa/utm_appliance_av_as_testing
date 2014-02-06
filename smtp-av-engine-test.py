#!/usr/bin/python
#
# A simple smtp AV engine test which uses the EICAR test string
#
# Start

import sys
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

if len(sys.argv) > 1:

	host= sys.argv[1]
	port = sys.argv[2]
	mail_from = sys.argv[3]
	mail_to = sys.argv[4]

	msg = MIMEMultipart()
	msg['From'] = mail_from
	msg['To'] = mail_to
	msg['Subject'] = 'Testing - AV Scanner'
	message = 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'

	msg.attach(MIMEText(message))

	mailserver = smtplib.SMTP(host,port)

	mailserver.set_debuglevel(1)

	mailserver.ehlo(name='joe')

	try:
   	   mailserver.sendmail(mail_from,mail_to,msg.as_string())
	except smtplib.SMTPDataError:
	   pass
 	except smtplib.SMTPRecipientsRefused:
	   pass
	finally:
   	   mailserver.quit()
else:
	print '----------------------------------------------------'
        print 'Usage: ./smtp.py <host> <port> <mail from> <mail to>'
        print '----------------------------------------------------'

# End
