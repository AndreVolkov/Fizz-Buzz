# Fizz Buzz

def FizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print('Fizz Buzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
    return FizzBuzz
        
n = int(input('Введите n:'))

for i in range(1, n+1):
    FizzBuzz(i)
