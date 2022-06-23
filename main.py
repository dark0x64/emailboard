from readmail import *
from parsemail import *

if __name__ == '__main__':
  POP3_SERVER = 'pop.gmail.com'
  PORT = '995'
  EMAIL = 'dark0666.emailboard@gmail.com'
  msgList = readMail(POP3_SERVER, PORT, EMAIL)
  postList = parseToPostList(msgList)
  print(postList)

  print(postList[0].subject)
  print(postList[0].message)
  print(postList[1].subject)
  print(postList[1].message)