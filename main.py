from readmail import *
from parsemail import *

if __name__ == '__main__':
  POP3_SERVER = 'pop.gmail.com'
  PORT = '995'
  EMAIL = 'dark0666.emailboard@gmail.com'
  DEBUG = True
  try:
    msgList = readMail(POP3_SERVER, PORT, EMAIL)
    postList = parseToPostList(msgList)
    if DEBUG == True:
      for i in range(0, len(postList)): # print incoming posts
        print(postList[i].subject)
        print(postList[i].message)
  except Exception as e:
    print(e)