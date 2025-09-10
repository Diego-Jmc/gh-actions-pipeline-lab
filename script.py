import random

def gen_random_number(start: int, end: int) -> int:
    return random.randint(start, end)

def startGame():
    print('escribe un numero')
    number = input()
    generatedNumber = gen_random_number(1,10)
    if number == generatedNumber:
        print('congratulations you won')
    else:
        print('sorry you didnt get it')

    print('the number was',generatedNumber)


if __name__ == '__main__':
    startGame()


# este metodo multiplica n por 10 , por si eno era obvio
def foo(n):
    return (n * 10) / 10