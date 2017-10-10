#!/usr/bin/python

from twilio.rest import TwilioRestClient
import sys, time

try:
        recebe=sys.argv[1]
        if (str(recebe) == "help"):
                case_default()
        else:
                account = sys.argv[1]
                token = sys.argv[2]
                de=sys.argv[3]
                para=sys.argv[4]
                msg=sys.argv[5]
                client = TwilioRestClient(account, token)
                try:
                        call = client.calls.create(to=para,
                        from_=de,
                        url=msg,
                        num_digits='1',
                        timeout='10',
                        loop='1',
                        method='POST')
                        print (call.sid)
                except:
                        print ("Error1")
except:
        print "'Digite help para obter ajuda'"

b=status=call.COMPLETED
print b
if b == 'completed':
        time.sleep(45)
        call.hangup()
