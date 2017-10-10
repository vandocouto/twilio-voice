#!/usr/bin/python

from twilio.rest import TwilioRestClient
import sys, time
def help_():
        print 'Por favor, informe os campos abaixo:\n\n\
"account" "token" "number-twilio" "number-you" "url-voice"\n\n\
exemplo: python telefone.py "AC0630f7a85ddb" "0fb97b000" "55XXXXXXXXXX" "55XXXXXXXX" "http://twimlets.com/holdmusic?Bucket=XXX"'

try:
        recebe=sys.argv[1]
        if (str(recebe) == 'help'):
                help_()
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
try:
        b=status=call.COMPLETED
        print b
        if b == 'completed':
                time.sleep(60)
                call.hangup()
except:
        print ""
