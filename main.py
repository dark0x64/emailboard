from readmail import *

if __name__ == '__main__':
  POP3_SERVER = 'pop.gmail.com'
  PORT = '995'
  EMAIL = 'dark0666.emailboard@gmail.com'
  print(readMail(POP3_SERVER, PORT, EMAIL))