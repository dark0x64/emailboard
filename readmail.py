import poplib, getpass

def readMail(pop3_server, port, email):
  password = getpass.getpass()
  server = poplib.POP3_SSL(pop3_server, port)

  try:
    #print(server.set_debuglevel(1))
    server.user(email)
    server.pass_(password)
    print(email + ': successful')
    print('Messages: %s. Size: %s' % server.stat())

    numMessages = len(server.list()[1])
    msgList = []
    for i in range(numMessages):
      count = 0
      for msg in server.retr(i+1)[1]:
        if count == 6 or count > 10: # if subject or message
          msgList.append(msg)
        count += 1
    return msgList
  except poplib.error_proto as e:
    print(email + ": fail")
    print(e)
  finally:
    server.quit()