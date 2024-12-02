import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


def create_empty_file():
    """Создание пустого файла по заданному пути."""
    path = file_path_entry.get()
    if not path:
        messagebox.showwarning("Ошибка", "Введите путь для создания файла.")
        return
    try:
        with open(path, 'w'):
            pass
        messagebox.showinfo("Успех", f"Файл создан: {path}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось создать файл: {e}")


def copy_file_shutil():
    """Копирование файла из одного места в другое."""
    src = file_path_entry.get()
    if not src or not os.path.isfile(src):
        messagebox.showwarning("Ошибка", "Укажите корректный путь исходного файла.")
        return

    dest = filedialog.asksaveasfilename(title="Сохранить файл как")
    if not dest:
        return

    try:
        shutil.copy(src, dest)
        messagebox.showinfo("Успех", f"Файл скопирован в: {dest}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось скопировать файл: {e}")

def copy_file_manual():
    """Копирование файла вручную без использования shutil."""
    src = file_path_entry.get()
    if not src or not os.path.isfile(src):
        messagebox.showwarning("Ошибка", "Укажите корректный путь исходного файла.")
        return

    dest = filedialog.asksaveasfilename(title="Сохранить файл как")
    if not dest:
        return

    try:
        # Открываем исходный файл для чтения
        with open(src, 'rb') as src_file:
            # Создаём файл назначения для записи
            with open(dest, 'wb') as dest_file:
                # Копируем данные порциями (например, по 64 КБ)
                while chunk := src_file.read(64 * 1024):  # Читаем блоки по 64 КБ
                    dest_file.write(chunk)

        messagebox.showinfo("Успех", f"Файл скопирован в: {dest}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось скопировать файл: {e}")

def delete_file():
    """Удаление файла по заданному пути."""
    path = file_path_entry.get()
    if not path or not os.path.isfile(path):
        messagebox.showwarning("Ошибка", "Укажите корректный путь файла для удаления.")
        return

    try:
        os.remove(path)
        messagebox.showinfo("Успех", f"Файл удален: {path}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось удалить файл: {e}")


def select_file():
    """Открытие окна проводника для выбора файла."""
    path = filedialog.askopenfilename(title="Выберите файл")
    if path:
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, path)


# Создание основного окна
root = tk.Tk()
root.title("Файловый менеджер")

# Поле для ввода пути к файлу
file_path_entry = tk.Entry(root, width=40)
file_path_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

# Кнопка для выбора пути через проводник
browse_button = tk.Button(root, text="Путь к файлу", command=select_file)
browse_button.grid(row=0, column=3, padx=5, pady=5)

# Кнопки управления
create_button = tk.Button(root, text="Создать", command=create_empty_file)
create_button.grid(row=1, column=0, padx=5, pady=5)

copy_button = tk.Button(root, text="Скопировать", command=copy_file_shutil)
copy_button.grid(row=1, column=1, padx=5, pady=5)

delete_button = tk.Button(root, text="Удалить", command=delete_file)
delete_button.grid(row=1, column=2, padx=5, pady=5)

# Запуск главного цикла приложения
root.mainloop()
