import re

class Post:
  def __init__(self, subject, message):
    self.subject = subject
    self.message = message

def validateInputs(postList):
  for i in postList:
    test_list = ['CreateThread\s+\"[ -~]+\"', 'CreateThread', 'ReplyThread\s+[0-9]+']
    temp = '(?:% s)' % '|'.join(test_list) # match in test_list
    if re.match(temp, i.subject):
      if re.match('[\x00-\xFF]+', i.message): # match all ASCII characters
        pass
      else:
        postList.remove(i)
    else:
      postList.remove(i)
  return postList

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