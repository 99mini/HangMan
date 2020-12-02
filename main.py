def game(answer: str, count: int):
  length = len(answer)
  result = [' _ '] * length
  
  while True:
    if count == 0:
      print("H E  I S  D E A D . . . !")
      return
    count -=1
    print("Help Him...! : ", end='')
    alpa = input()
    
    for i in range(length):
      if answer[i] == alpa:
        result[i] = alpa
      
    print(' '.join(result))

    if ''.join(result) == answer:
      print("G O O D . . . !")
      return
    
game('apply', 5)
