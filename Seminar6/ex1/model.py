
from sqlite3 import OperationalError
import control as con


# a = int(input('Введите число '))
# b = int(input('Введите число '))


# result_delen = con.delen(a, b), '/'
# result_mult = con.mult(a, b), '*'
# result_sum = con.sum(a, b), '+'
# result_minus = con.minus(a, b), '-'

def calculate(a, b, operation):
   
   if operation == '+':
       result = con.sum(a, b)
   elif operation == '-':
       result = con.subtract(a, b)
   elif operation == '/':
       result = con.dividedivide(a, b)
   elif operation == '*':
       result = con.multiply(a, b)
   else:
       print('Неизвестная операция')  
    
   return result



def ops():
   # Запрашиваем у пользователя желаемое действие
   operation = input('Выбери операцию ') 
 
   return operation


def total():
   # Запрашиваем данные
   a = int(input('Введите первое число: '))
   b = int(input('Введите второе число: '))

   # Запрашиваем тип операции
   operation = ops()
  
   # Производим вычисления
   result = calculate(a, b, operation)
 
   # Выводим результат в консоль
   print(f'Результат вычислений: {result}')