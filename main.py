from tkinter import *
from Exersice import *
import Check

# window
window = Tk()
window.geometry("620x620")
window.title("Math simple exercise")
window.config(background="black")

quiz = ""
answer = ""
complete_quiz = ""
user_input = ""
fquiz = False  # checks if start_click() has did a quiz
quiz_number = 0


def start_click():
    global complete_quiz
    global quiz
    global answer
    global fquiz

    # assigns variables from the exercise function
    complete_quiz = str(exercise())
    quiz = complete_quiz.split(',')[0]
    answer = complete_quiz.split(',')[1]

    # Crops the strings from extras like parenthesis, apostrophes or comas
    quiz = quiz[2:-4]
    answer = answer[1:-1]
    complete_quiz = quiz + " = " + answer

    print(answer)

    ex.config(text=quiz)
    fquiz = True


def check_user_ans():
    # ans = user input answer & cans = Correct Answer
    inp = user_answer.get()
    global quiz_number

    if not fquiz:
        start_click()
    else:
        if Check.check_user_ans(inp, answer):
            start_click()
            quiz_number += 1
            ex_a.config(text="good job")
            user_answer.delete(0, 'end')
            ex_number.config(text="quiz answered "+str(quiz_number))

        else:
            ex_a.config(text="Try again")


# Text box
user_answer = Entry(window,
                    show=None,
                    font=('Arial', 14))

# photo

photo = PhotoImage(file='Math_logo.png')

# labels
title = Label(window,
              text="Simple Math ",
              font=('Arial', 20, 'bold'),
              fg="white",
              bg="black",
              image=photo,
              compound='right')

version = Label(window,
                text="version 1.2",
                font=('Arial', 8, 'bold'),
                fg="white",
                bg="black")

ex_number = Label(window,
                text=" ",
                font=('Arial', 10, 'bold'),
                fg="white",
                bg="black")

#   Exercise label
ex = Label(
           text=quiz,
           font=('Arial', 15, 'bold'),
           fg="white",
           bg="black")

ex_a = Label(window,
             text="",
             font=('Arial', 15, 'bold'),
             fg="white",
             bg="black")

# buttons
start_button = Button(window,
                      text='generate a random exercise',
                      command=start_click,
                      font=("Arial", 15),
                      fg="white",
                      bg="black",
                      activeforeground="white",
                      activebackground="black")

user_button = Button(window,
                     text='Check Answer',
                     command=check_user_ans,
                     font=("Arial", 15),
                     fg="white",
                     bg="black",
                     activeforeground="white",
                     activebackground="black")

# Packing, this show the elements on the window, don't change the order.
title.pack()
start_button.pack()
ex.pack()
user_answer.pack()
user_button.pack()
ex_a.pack()
ex_number.pack()
version.pack()

window.mainloop()
