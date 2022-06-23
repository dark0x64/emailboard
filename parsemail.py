import re

class Post:
  def __init__(self, subject, message):
    self.subject = subject
    self.message = message

def validateInputs(postList):
  for i in postList:
    subject = i.subject
    if re.match('CreateThread\s+\"[ -~]+\"', subject) or re.match('CreateThread', subject) or re.match('ReplyThread\+[0-9]+', subject):
      if not re.match('[ -~]+/g', i.message):
        postList.remove(i)
    else:
      postList.remove(i)

def parseToPostList(msgList):
  postList = []
  count = 1
  for i in msgList:
    msg = i.decode()
    subject = ''
    message = ''
    if 'Subject: ' in msg:
      subject = msg.split(':')[1].strip()
      for i in range(count, len(msgList)): # start from latter
        if "Subject: " not in msgList[i].decode():
          message = message + msgList[i].decode() + '\n'
          count += 1
        else:
          count += 1
          break
      postList.append(Post(subject, message.strip()))
  return validateInputs(postList)