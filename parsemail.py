class Post:
  def __init__(self, subject, message):
    self.subject = subject
    self.message = message

def parseToPostList(msgList):
  postList = []
  for i in msgList:
    msg = i.decode()
    subject = ''
    message = ''
    if 'Subject: ' in msg:
      subject = msg.split(':')[1].strip()
      for i in range(1, len(msgList)): # start from latter
        if "Subject: " not in msgList[i].decode():
          message = message + msgList[i].decode() + '\n'
        else: break
      postList.append(Post(subject, message.strip()))
  return postList