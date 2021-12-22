#!/usr/bin/env python

import sendgrid
import os
import sys
from sendgrid.helpers.mail import *


message = "SERVER: {0}, UUID: {1}, MESSAGE: {2}".format(sys.argv[1], sys.argv[2], sys.argv[3])

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("noreply.ezlink-app@thoughtworks.com")
to_email = Email("ezlink-app@thoughtworks.com")
subject = "Ezlink APP Alert"
content = Content("text/plain", message)
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
