def prime_num(num):
  boo_lean = True
  if num > 1:
    for i in range(2, num):
      if (num % i) == 0:
        boo_lean = False
        return boo_lean
      else:
        boo_lean = True
        return boo_lean

print(prime_num(66))
print("\n")

def create_list(list):
  new_list = []
  for i in list:
    if i not in new_list:
      new_list.append(i)
  return(new_list)
  
old_list = [1, 3, 4, 5, 5, 5,5, 6, 2, 2, 2, 3, 3, 3, 3, 4, 4,4 ,4, 1, 1,1 ,1,1]
print(create_list(old_list))
print("\n")


from datetime import datetime, timedelta

def time_calc(age):
  current_date = datetime.now()
  current_age = current_date.year - age.year
  return current_age
  
birthday = datetime(1987, 11, 13)
print(time_calc(birthday))
print("\n")

def calc_factorial():
  user_num = int(input("Enter your number: "))
  fact = 1
  for i in range(1, user_num+1):
    fact = fact * i
  return print(fact)
calc_factorial()
print("\n")

import math

def perfect():
  hold_num = 1
  
  for num in range(2,1000):
    answer = 1
    div = 2
    holder = []
    while div * div < num:
      if (num % div) == 0:
        answer = answer + div + num//div
        holder.append(answer)
      div = div + 1
    if answer is num:
      retur
print(perfect())
      

def pascal(i):
  
  arr = [[0 for num in range(i)]
          for num2 in range(i)]
          
  for line in range(0, i):
    for x in range(0,line + 1):
      if (x is 0 or x is line):
        arr[line][x] = 1
        print(arr[line][x], end = " ")
        
      else:
        arr[line][x] = (arr[line - 1][x - 1] + arr[line - 1][i])
        print(arr[line][x], end=" ")
        
  print("\n", end=" ")
  
number_num = 10
pascal(number_num)