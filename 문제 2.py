def game():
  a = input('캐릭터의 이름을 입력하세요: ')
  import random
  print('캐릭터 이름: ', a)
  b = random.randint(6, 8)
  c = random.randint(6, 8)
  print('캐릭터 정보: ', '힘(%d), 지력(%d)' %(b, c))
  if b > c:
    print('캐릭터 직업: ', '전사' )
  elif b == c:
    print('캐릭터 직업: ', '궁수')
  else:
    print('캐릭터 직업: ', '법사')
