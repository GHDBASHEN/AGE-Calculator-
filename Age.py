from tkinter import *
from PIL import ImageTk, Image
import datetime


root = Tk()
root.title("Age Calculator")
root.geometry("400x350")
root.resizable(0, 0)
root.configure(bg="#f3f4f6")  # Light background color


header_frame = Frame(root, bg="#4a90e2", width=400, height=60)
header_frame.pack(fill=X)
header_label = Label(header_frame, text="Age Calculator", bg="#4a90e2", fg="white", font=("Helvetica", 18, "bold"))
header_label.pack(pady=10)


input_frame = Frame(root, bg="#ffffff", width=360, height=180)
input_frame.place(x=20, y=80)
Label(input_frame, text="Enter Your Date of Birth", bg="white", font=("Helvetica", 12)).place(x=85, y=10)

Label(input_frame, text='Day', bg='white', font=("Helvetica", 10)).place(x=50, y=50)
birth_day_entry = Entry(input_frame, border=0, bg='#e8e8e8', width=5, justify='center', font=("Helvetica", 12))
birth_day_entry.place(x=50, y=70)

Label(input_frame, text='Month', bg='white', font=("Helvetica", 10)).place(x=160, y=50)
birth_month_entry = Entry(input_frame, border=0, bg='#e8e8e8', width=5, justify='center', font=("Helvetica", 12))
birth_month_entry.place(x=160, y=70)

Label(input_frame, text='Year', bg='white', font=("Helvetica", 10)).place(x=270, y=50)
birth_year_entry = Entry(input_frame, border=0, bg='#e8e8e8', width=5, justify='center', font=("Helvetica", 12))
birth_year_entry.place(x=270, y=70)


def calculate_age():
    b_day = int(birth_day_entry.get())
    b_month = int(birth_month_entry.get())
    b_year = int(birth_year_entry.get())

    b_date = datetime.date(b_year, b_month, b_day)
    today = datetime.date.today()

    age = today.year - b_year - ((today.month, today.day) < (b_month, b_day))
    age_months = (today.year - b_year) * 12 + today.month - b_month

    result_label.config(text=f"Age: {age} years, {age_months % 12} months")
    months_label.config(text=f"In Months: {age_months} months")


calculate_button = Button(root, text="Calculate Age", bg="#4a90e2", fg="white", font=("Helvetica", 12),
                          command=calculate_age, border=0)
calculate_button.place(x=140, y=270)


result_label = Label(root, text="", bg="#f3f4f6", font=("Helvetica", 12))
result_label.place(x=20, y=310)

months_label = Label(root, text="", bg="#f3f4f6", font=("Helvetica", 12))
months_label.place(x=20, y=330)

root.mainloop()
