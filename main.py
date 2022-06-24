from readmail import *
from parsemail import *

if __name__ == '__main__':
  POP3_SERVER = 'pop.gmail.com'
  PORT = '995'
  EMAIL = 'dark0666.emailboard@gmail.com'
  try:
    msgList = readMail(POP3_SERVER, PORT, EMAIL)
    postList = parseToPostList(msgList)
    for i in range(0, len(postList)):
      print(postList[i].subject)
      print(postList[i].message)
  except Exception as e:
    print(e)