import tkinter as tk
from tkinter import messagebox, ttk
import re


# === Функции ===
def click_button2():
    label.config(text="89292533281")


def click_button3():
    label.config(text="22446688")


def click_button4():
    label.config(text="снилс")


def click_button5():
    label.config(text="23100")


def click_button1():
    button2 = tk.Button(frame, text="Номер", font=("Arial", 20), command=click_button2)
    button2.place(x=1, y=250, width=100, height=50)
    button3 = tk.Button(frame, text="Паспорт", font=("Arial", 20), command=click_button3)
    button3.place(x=1, y=300, width=100, height=50)
    button4 = tk.Button(frame, text="Снилс", font=("Arial", 20), command=click_button4)
    button4.place(x=1, y=350, width=100, height=50)
    button5 = tk.Button(frame, text="Пароли", font=("Arial", 20), command=click_button5)
    button5.place(x=1, y=400, width=100, height=50)

def click_button6():
    user_input = entry_var.get()
    label.config(text=user_input)

def validate_input(text):
    """Проверяет ввод на соответствие формату."""
    if re.match(r'^\d{1,5}$', text):  # Разрешены только цифры (до 5 знаков)
        return True
    else:
        messagebox.showerror("Ошибка", "Неверный формат ввода. Введите число (до 5 знаков)")
        return False

def process_login():
    """Обрабатывает логин."""
    user_input = entry_var.get()
    if validate_input(user_input):
        if int(user_input) == 23100:
            messagebox.showinfo("Успех", "Вход от имени администратора")
        else:
           messagebox.showinfo("Успех", "Вход от имени пользователя")

# === Классы ===

class CustomButton(tk.Button):
    """Кастомная кнопка, которая увеличивает шрифт при наведении."""
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.original_font = kwargs.get('font', ('Arial', 20))
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
    def on_enter(self, event):
        font_name, font_size = self.original_font
        self.config(font=(font_name, font_size + 5))

    def on_leave(self, event):
        self.config(font=self.original_font)

class CustomLabel(tk.Label):
    """Кастомная метка, устанавливающая цвет фона при создании."""
    def __init__(self, master=None, background_color="white", **kwargs):
        super().__init__(master, bg=background_color, **kwargs)

class InputFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_var, font=("Arial", 20))
        self.entry.pack(side="left", padx=5)
        self.button = tk.Button(self, text="Ввод", font=("Arial", 20), command=self.submit_input)
        self.button.pack(side="left")

    def submit_input(self):
        user_input = self.entry_var.get()
        label.config(text=user_input)

    # === Операции ===


def show_message():
    messagebox.showinfo("Заголовок", "Приветствие")


def set_theme():
    """Устанавливает темную тему."""
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TLabel", background="gray", foreground="white", font=("Arial", 12))
    style.configure("TButton", background="darkgray", foreground="black", font=("Arial", 12), padding=5)
    style.configure("TFrame", background="black")


def show_combo_box():
    """Создает и выводит в окно ComboBox"""
    combo_values = ["Вариант 1", "Вариант 2", "Вариант 3"]
    combo = ttk.Combobox(window, values=combo_values)
    combo.pack()
    combo.current(0)


window = tk.Tk()
window.title('Окно с данными')
window.geometry("1200x720")
window.resizable(width=True, height=True)

set_theme()  # Устанавливаем тему

frame = ttk.Frame(window)
frame.place(relx=0.01, rely=0.01, relheight=0.98, relwidth=0.98)

# Создание кастомного Label и размещение
label = CustomLabel(frame, text="Данные", font=("Arial", 100), background_color="white")
label.place(x=1, y=1, width=1000, height=200)

# Создание кастомного Entry
entry_var = tk.StringVar()
entry = tk.Entry(frame, textvariable=entry_var, font=("Arial", 20))
entry.place(x=1, y=450, width=200, height=50)

# Создание кастомных кнопок
button1 = CustomButton(frame, text="Артём", font=("Arial", 20), command=click_button1)
button1.place(x=1, y=200, width=100, height=50)

button6 = tk.Button(frame, text="Ввод", font=("Arial", 20), command=click_button6)
button6.place(x=1, y=500, width=100, height=50)

login_button = CustomButton(frame, text="Логин", font=("Arial", 20), command=process_login)
login_button.place(x=1, y=550, width=100, height=50)

input_frame = InputFrame(master=frame, bg="lightyellow")
input_frame.place(x=1, y=600, width=200, height=50)

show_message_button = tk.Button(frame, text="Сообщение", font=("Arial", 20), command=show_message)
show_message_button.place(x=1, y=650, width=100, height=50)

show_combo_box()

window.mainloop()