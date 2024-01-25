from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text = date)
    lab_month.config(text = month)
    lab_year.config(text=year)
    lab_Days.config(text=day)
    lab_hr.after(200,date_time)





clock = Tk()
clock.title ('         Digital clock and calender')
clock.geometry('2100x1600')
clock.config(bg='red')


lab_hr=Label(clock, text="00", font=('Times New Roman', 50, "bold"),bg="yellow",fg="white")
lab_hr.place(x=40, y=40, height=90, width=110)


lab_hr_txt=Label(clock, text="Hour", font=('Times New Roman', 20, "bold"),bg="yellow",fg="white")
lab_hr_txt.place(x=40, y=150, height=30, width=100)


lab_min=Label(clock, text="00", font=('Times New Roman', 50, "bold"),bg="yellow",fg="white")
lab_min.place(x=340, y=50, height=90, width=130)

lab_min_txt=Label(clock, text="min", font=('Times New Roman', 20, "bold"),bg="yellow",fg="white")
lab_min_txt.place(x=340, y=150, height=30, width=100)

lab_sec=Label(clock, text="00", font=('Times New Roman', 50, "bold"),bg="yellow",fg="white")
lab_sec.place(x=640, y=40, height=110, width=100)

lab_sec_txt=Label(clock, text="Sec", font=('Times New Roman', 20, "bold"),bg="yellow",fg="white")
lab_sec_txt.place(x=640, y=170, height=30, width=100)

lab_am=Label(clock, text="00", font=('Times New Roman', 50, "bold"),bg="yellow",fg="white")
lab_am.place(x=1040, y=40, height=110, width=100)

lab_am_txt=Label(clock, text="AM/PM", font=('Times New Roman', 20, "bold"),bg="yellow",fg="white")
lab_am_txt.place(x=1040, y=170, height=30, width=100)

#Date COde
lab_date=Label(clock, text="00", font=('Times New Roman', 50, "bold"),bg="yellow",fg="white")
lab_date.place(x=40, y=300, height=90, width=110)


lab_date_txt=Label(clock, text="Date", font=('Times New Roman', 20, "bold"),bg="yellow",fg="white")
lab_date_txt.place(x=40, y=400, height=30, width=100)

lab_month=Label(clock, text="00", font=('Times New Roman', 50, "bold"),bg="yellow",fg="white")
lab_month.place(x=340, y=300, height=90, width=110)


lab_month_txt=Label(clock, text="Month", font=('Times New Roman', 20, "bold"),bg="yellow",fg="white")
lab_month_txt.place(x=340, y=400, height=30, width=100)


lab_year=Label(clock, text="00", font=('Times New Roman', 50, "bold"),bg="yellow",fg="white")
lab_year.place(x=640, y=300, height=90, width=110)


lab_year_txt=Label(clock, text="Hour", font=('Times New Roman', 20, "bold"),bg="yellow",fg="white")
lab_year_txt.place(x=640, y=400, height=30, width=100)


lab_Days=Label(clock, text="00", font=('Times New Roman', 50, "bold"),bg="yellow",fg="white")
lab_Days.place(x=1040, y=300, height=90, width=110)


lab_Days_txt=Label(clock, text="Days", font=('Times New Roman', 20, "bold"),bg="yellow",fg="white")
lab_Days_txt.place(x=1040, y=400, height=30, width=100)

date_time()

clock.mainloop()