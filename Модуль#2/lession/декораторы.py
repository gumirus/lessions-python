#Декораторы

def summa(a, b): 
  print(a + b)

def mult(a, b):
  print(a * b)

summa(10, 10)
mult(5, 5)

def my_decorator (func) :
  def wrapper(a, b):
    print( 'Привет!')
    print(f'Ответ: {func(a, b)}') 
    print( 'Спасибо за использование нашего продукта')
    return wrapper

@my_decorator
def summa(a, b):
  return (a + b)

@my_decorator
def mult(a, b):
  return (a * b)

summa(10, 10) 
mult(5, 5)