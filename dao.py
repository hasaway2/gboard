import datetime as d

board_list = []
bno=1

def save(title:str, content:str, writer:str)->bool:
  global bno
  writeday = d.datetime.now().date()
  board_list.append(dict(bno=bno, writeday=writeday, content=content, writer=writer, title=title))
  bno+=1
  return True

def findall()->list:
  return board_list

def findone(bno)->dict:
  for board in board_list:
    if board['bno']==bno:
      return board
  return None

def update(bno:int, title:str, content:str)->bool:
  for board in board_list:
    if board['bno']==bno:
      board['title']=title
      board['content']=content
      return True
  return False 

def delete(bno)->bool:
  for board in board_list:
    if board['bno']==bno:
      board_list.remove(board)
      return True
  return False 