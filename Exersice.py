import random

choice = ["+", "-", "*", "/"]


# this function give us the exercise and the answer
def exercise():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.choice(choice)

    if c == "+":
        d = a + b
    elif c == "-":
        d = a - b
    elif c == "*":
        d = a * b
    elif c == "/":
        d = a / b
        d = round(d, 1)


    e = (str(a) + "" + c + "" + str(b) + " = ")

    return e, d

