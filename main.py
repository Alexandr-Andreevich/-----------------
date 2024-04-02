
from tkinter import*
import PIL.ImageTk as ImageTk


class Alexandr:

    def __init__(self):
        self.count = 1
        self.age = 26
        self.window = Tk()
        self.window.title('Угадай!')
        self.window.geometry('400x350+350+140')
        self.window.resizable(width=False, height=False)

        self.bg = 'bg.jpg'
        self.bg_image = ImageTk.PhotoImage(file=self.bg)

        self.bg_1 = Label(self.window, image=self.bg_image)
        self.bg_1.pack()

        self.l = Label(self.window, text='Привет! \n Угадай, как меня зовут?', font='Arial 10 bold')
        self.l.place(rely=0.07, relx=0.25)

        self.user_answer_name = Entry(self.window, font='Arial 16 bold')
        self.user_answer_name.place(rely=0.2, relx=0.20)

        self.btn1 = Button(self.window, text='Ответить', font='Arial 11 bold', command=self.result)
        self.btn1.place(rely=0.3, relx=0.25)

        self.btn2 = Button(self.window, text='Сбросить', font='Arial 11 bold', command=self.clear)
        self.btn2.place(rely=0.3, relx=0.55)

        self.true_answer_name = Label(self.window, text='', font='Arial 10 bold')
        self.true_answer_name.place(rely=0.7, relx=0.20)


    def result(self):

        self.answer_name = str(self.user_answer_name.get())
        self.name = str('Саша')

        if self.answer_name == self.name:
            self.true_answer_name['text'] = f'Угадал! Мое имя {self.name}. Мой возраст {self.age}. \n ' \
                                            f'Ты справился с {self.count} попытки!'
            self.count = 1


        elif self.answer_name != self.name:
            self.true_answer_name['text'] = f'Нет. Это не мое имя! \n Попробуй еще раз'
            self.count += 1
            self.user_answer_name.delete(0, END)


    def clear(self):
        self.user_answer_name.delete(0, END)
        self.true_answer_name['text'] = f''
        self.count = 1


    def run(self):
        self.window.mainloop()

app = Alexandr()
app.run()