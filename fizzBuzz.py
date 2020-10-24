numbers = [3, 30, 9, 10, 45, 10, 55, 99, 100, 88, 34, 33, 111, 113, 6]

def fizzBuzz(number):
        if(number % 3 == 0 and number % 5 == 0):
            print('fizzBuzz')
        elif(number % 3 == 0):
            print('fizz')
        elif(number % 5 == 0):
            print('buzz')
        else:
            print("Not Divisible by 3 or 5")

for number in numbers:
    fizzBuzz(number)