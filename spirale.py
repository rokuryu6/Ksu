"""Выведите таблицу размером n \times nn×n, заполненную числами от 1 до n^2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5n=5):

5
Sample Output:

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""

k = int(input())
i = list(range(0, (k-1)+1))#Список строк
#print (i)
j = list(range(0, (k-1)+1)) #Список столбцов
mat = [[0 for z in range(k)]for n in range(k)]  # заполнение поля нулями
ch = 1 #счетчик заполняемого значения
I, J = 0,0

for c in range(k):
#Заполнение верх
  for J in j:
    mat[I][J] = ch
    ch += 1
  if I in i:
    i.remove(I) #удаление строки списка из перебора
  else: continue

#Заполнение право
  for I in i:
    mat[I][J] = ch
    ch += 1
  j.remove(J) #удаление строки списка из перебора
#print (mat[I][J])

#Заполнение низ
  for J in reversed(j):
    mat[I][J] = ch
    ch += 1
  if I in i:
    i.remove(I) #удаление строки списка из перебора
  else: continue
  
#Заполнение лево
  for I in reversed(i):
    mat[I][J] = ch
    ch += 1
  j.remove(J) #удаление строки списка из перебора

#print (i,j, 'списки i и j'))
for s in range(k): 
  for u in mat[s]:
    print (u, end = ' ')
  print ('')
