from tkinter import *
import random
import os
import csv

if os.path.isdir("survey_results") is True:
    pass
else:
    os.mkdir("survey_results")

survey_template = {
    "Of the following fast-food restaurants, which one do you most prefer?": ["Mcdonald's", "Wendy's", "Burger King",
                                                                              "Sonic", "Chic-fil-a"],

    "Of the following cereal brands,  which one do you most prefer?": ["Cinnamon Toast Crunch", "Coco Puffs",
                                                                       "Lucky Charms", "Corn Flakes", "Trix",
                                                                       "Captain Crunch"],

    "How often do you wash your hands?": ["Never", "Not often", "Average", "Often", "Very often"],

    "How satisfied where you with your last nights sleep?": ["Very satisfied", "Satisfied",
                                                             "Neither satisfied nor dissatisfied", "Dissatisfied",
                                                             "Very dissatisfied"],

    "How many times did you listen to music in the last week?": ["Never", "Once", "A couple times", "Almost everyday",
                                                                 "Everyday"],

    "How likely are you to use curse words?": ["Very likely", "Likely", "Unlikely", "Very unlikely"],

    "On a scale of 1 to 10, 10 being the best, how would you rate your last date?": ["1", '2', '3', '4', '5', '6', '7',
                                                                                     '8', '9', '10']
}

user_data = []
total_data = []

questions = survey_template.keys()
questions = list(questions)
question_counter = 0

root = Tk()
root.title("Survey")
start = Frame(root)
questions_frame = Frame(root)
for frame in (start, questions_frame):
    frame.grid(row=0, column=0, sticky="nsew")


question = StringVar()
answer = StringVar()
answer.set("NONE")


def finish():
    global question_counter
    global user_data
    total_data.append(user_data)
    question_counter = 0
    user_data = []
    start.tkraise()


def start_survey():
    global question_counter
    user_data.append(f"user_{random.randint(1000, 9999)}")
    try:
        question.set(questions[0])
    except IndexError:
        pass

    for widget in questions_frame.winfo_children():
        widget.destroy()

    questions_label = Label(questions_frame, textvariable=question, font=("arial", 11))
    next_button = Button(questions_frame, text='Next Question', command=next_question, font=("arial", 11))
    white_space_q = Label(questions_frame, text="")
    questions_label.pack(side=TOP)
    for ans in survey_template[(questions[0])]:
        ans_radio_button = Radiobutton(questions_frame, text=ans, variable=answer, value=ans,font=("arial", 11),
                                       selectcolor='black')
        ans_radio_button.pack()

    no_answer = Radiobutton(questions_frame, text="Prefer not to answer", variable=answer, value='No response',
                            font=("arial", 11), selectcolor='black')
    no_answer.pack()
    next_button.pack(side=BOTTOM, pady=10)
    white_space_q.pack(side=BOTTOM)
    questions_frame.tkraise()


def next_question():
    global question_counter
    user_data.append(answer.get())
    try:
        question_counter += 1
        question.set(questions[question_counter])

        for widget in questions_frame.winfo_children():
            widget.destroy()

        questions_label = Label(questions_frame, textvariable=question, font=("arial", 11))
        next_button = Button(questions_frame, text='Next Question', command=next_question, font=("arial", 11))
        white_space_q = Label(questions_frame, text="")
        questions_label.pack(side=TOP)
        for ans in survey_template[(questions[question_counter])]:
            ans_radio_button = Radiobutton(questions_frame, text=ans, variable=answer, value=ans, font=("arial", 11),
                                           selectcolor='black')
            ans_radio_button.pack()
        no_answer = Radiobutton(questions_frame, text="Prefer not to answer", variable=answer,
                                value='No response', font=("arial", 11), selectcolor='black')
        no_answer.pack()
        next_button.pack(side=BOTTOM, pady=10)
        white_space_q.pack(side=BOTTOM)
    except IndexError:
        for widget in questions_frame.winfo_children():
            widget.destroy()
        question.set("Thank you for taking the survey")
        white_space6 = Label(questions_frame, text="  ")
        white_space7 = Label(questions_frame, text="  ")
        white_space10 = Label(questions_frame, text="  ")
        white_space11 = Label(questions_frame, text="  ")
        questions_label = Label(questions_frame, textvariable=question, font=("arial", 11))
        finish_button = Button(questions_frame, text="Finish", command=finish, font=("arial", 11))
        white_space6.pack(side=LEFT)
        white_space7.pack(side=LEFT)
        white_space10.pack(side=RIGHT)
        white_space11.pack(side=RIGHT)
        questions_label.pack(side=TOP)
        finish_button.pack(side=BOTTOM, pady=10)


start.tkraise()
start_label = Label(start, text="Please take a few moments\n to answer this brief survey", justify=CENTER,
                    font=("arial", 11))
white_space1 = Label(start, text="")
white_space2 = Label(start, text="")
white_space3 = Label(start, text="")
white_space4 = Label(start, text="         ")
white_space5 = Label(start, text="         ")
white_space8 = Label(start, text="         ")
white_space9 = Label(start, text="         ")
start_button = Button(start, text="Start Survey", command=start_survey, font=("arial", 11))

white_space3.grid(row=0, column=0)
white_space5.grid(row=1, column=0)
start_label.grid(row=1, column=1)
white_space1.grid(row=1, column=2)
white_space8.grid(row=3, column=2)
white_space9.grid(row=3, column=0)
white_space2.grid(row=2, column=0)
white_space4.grid(row=3, column=0)
start_button.grid(row=3, column=1, pady=10)
try:
    root.mainloop()
finally:
    if total_data:
        with open(f'survey_results/survey_data{random.randint(1000,9999)}.csv', 'w+', newline="", encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            questions.insert(0, "User")
            csv_writer.writerow(questions)
            for user in total_data:
                csv_writer.writerow(user)
    else:
        pass
