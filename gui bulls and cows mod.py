from tkinter import *
import random
from tkinter import messagebox
import tkinter.font as font


root=Tk()
root.title('BULLS AND COWS')
root.geometry('1000x1000')

myFont = font.Font(family='algerian',size=30)
myfont1=font.Font(family='broadway',size=24)

can = Canvas(root, bg = 'gray25', height=1080, width=1920)
can.place(relx=0.5,rely=0.5, anchor=CENTER)



attempts=0
num=[]
a=0
guess=[]


def rand():
    for i in range(4):
        x=random.randrange(0,9)
        num.append(x)
    if len(num)!=len(set(num)):
        num.clear()
        rand()
    if num[0]==0:
        rand()
    return num

print(rand())


lab=Label(root,text='BULLS AND COWS',fg='blue',bg='black')
lab.pack()

lab['font']=myFont

e=Entry(root,width=25,borderwidth=5)
e.place(relx=0.4798,rely=0.3)



    
def game():
    global attempts
    global guess
    global a
    attempts+=1
    choice=e.get()
    e.delete(0, END)
    guess=[]
    for i in range(a):
        guess.append(int(choice[i]))
    g1()
    a=0

def g1():
    global attempts
    if guess[0]==0:
        attempts-=1
        messagebox.showwarning("Incorrect input","The first digit of number should not be 0")
    elif len(guess)!=4:
        attempts-=1
        messagebox.showwarning("Incorrect input","The number should be a 4-digit number")
    elif len(guess)!=len(set(guess)):
        attempts-=1
        messagebox.showwarning("Incorrect input","The number should not have repeated digits")
    else:
        cows=0
        bulls=0
        for i in range(4):
           if num[i]==guess[i]:
              cows+=1
        for i in range(4):
            if num[i] in guess and num[i]!=guess[i]:
               bulls+=1
        
        labb=Label(root,text=("bulls=",bulls))
        labc=Label(root,text=("cows=",cows))
        labb.place(relx=0.7,rely=0.2)
        labc.place(relx=0.7,rely=0.3)
        if cows==4:
            but_enter['state']=DISABLED
            but_1['state']=DISABLED
            but_2['state']=DISABLED
            but_3['state']=DISABLED
            but_4['state']=DISABLED
            but_5['state']=DISABLED
            but_6['state']=DISABLED
            
            but_7['state']=DISABLED
            but_8['state']=DISABLED
            but_9['state']=DISABLED
            but_0['state']=DISABLED
            e['state']=DISABLED

            messagebox.showinfo("CONGTRATULATIONS!","YOU WON")
            labd=Label(root,text="GAME OVER\n You did it in %g attempts"%attempts,bg='red',)
            labd.place(relx=0.7,rely=0.7)
            labd['font']=myfont1
            


def button_click(num):
    global a
    a+=1
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))
    

def button_enter():
    game()

def button_exit():
    root.destroy()

def button_inst():
    root1=Tk()
    root1.title('INSTRUCTIONS')
    Label(root1,text='Welcome to BULLS AND COWS').grid(row=1,column=1)
    Label(root1,text='Rules:').grid(row=3,column=1)
    Label(root1,text='1.The computer will guess a 4-digit number with no repetitions').grid(row=4,column=1)
    Label(root1,text='2.The user has to guess that particular number').grid(row=5,column=1)
    Label(root1,text='3.The input given by user should be a 4 digit number').grid(row=6,column=1)
    Label(root1,text='4.There should be no repetitions in the numbergiven as input').grid(row=7,column=1)
    Label(root1,text='5.The first digit should not be 0').grid(row=8,column=1)
    Label(root1,text='6.If the matching digits are in their right positions, they are "cows", if in different positions, they are "bulls"').grid(row=9,column=1)
    Label(root1,text='7.Everytime the player guesses,they will be shown the number of bulls and cows in the guessed number').grid(row=10,column=1)
    Label(root1,text='8.At the end when the player guesses the right number you will be shown the number of attempts in which the user has guessed').grid(row=11,column=1)

    def button_ex():
      root1.destroy()
    
    Button(root1,text='Exit',fg='red',command=button_ex).grid(row=12,column=1)

but_1=Button(root,text='1',command=lambda :button_click(1),width=10,height=2,fg='firebrick4',bg='lemon chiffon')
but_2=Button(root,text='2',command=lambda :button_click(2),width=10,height=2,fg='firebrick4',bg='lemon chiffon')
but_3=Button(root,text='3',command=lambda :button_click(3),width=10,height=2,fg='firebrick4',bg='lemon chiffon')
but_4=Button(root,text='4',command=lambda :button_click(4),width=10,height=2,fg='firebrick4',bg='lemon chiffon')
but_5=Button(root,text='5',command=lambda :button_click(5),width=10,height=2,fg='firebrick4',bg='lemon chiffon')
but_6=Button(root,text='6',command=lambda :button_click(6),width=10,height=2,fg='firebrick4',bg='lemon chiffon')
but_7=Button(root,text='7',command=lambda :button_click(7),width=10,height=2,fg='firebrick4',bg='lemon chiffon')
but_8=Button(root,text='8',command=lambda :button_click(8),width=10,height=2,fg='firebrick4',bg='lemon chiffon')
but_9=Button(root,text='9',command=lambda :button_click(9),width=10,height=2,fg='firebrick4',bg='lemon chiffon')
but_0=Button(root,text='0',command=lambda :button_click(0),width=10,height=2,fg='firebrick4',bg='lemon chiffon')

but_exit=Button(root,text='EXIT',command=button_exit,width=10)

but_enter=Button(root,text='ENTER',command=button_enter,width=10)

but_inst=Button(root,text='INSTRUCTIONS',command=button_inst)


but_1.place(relx=0.4,rely=0.4)
but_2.place(relx=0.5,rely=0.4)
but_3.place(relx=0.6,rely=0.4)

but_4.place(relx=0.4,rely=0.5)
but_5.place(relx=0.5,rely=0.5)
but_6.place(relx=0.6,rely=0.5)

but_7.place(relx=0.4,rely=0.6)
but_8.place(relx=0.5,rely=0.6)
but_9.place(relx=0.6,rely=0.6)

but_0.place(relx=0.5,rely=0.7)

but_enter.place(relx=0.5,rely=0.8)
but_exit.place(relx=0.5,rely=0.85)
but_inst.place(relx=0.5,rely=0.2)


root.mainloop()
