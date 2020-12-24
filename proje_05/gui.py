import tkinter as tk
from tkinter import filedialog
from components.database_viewer import Viewer
from components.all_comps import CustomButton as button



app = tk.Tk()
app.resizable(0, 0)

center_of_screen = {
    'x' : int(app.winfo_screenwidth() / 2),
    'y' : int(app.winfo_screenheight() / 2)
}

app.geometry(
    f'400x300+{center_of_screen["x"] - 200}+{center_of_screen["y"] - 150}')


app_icon = tk.PhotoImage(file='./assets/icon.png')


def open_database():
    source_path = filedialog.askopenfilename(
        initialdir="./", title="Bir veritabanı dosyası seç", filetypes=(("Veritabanı Dosyaları", "*.db *.db3 *.sqlite *.sqlite3"),))

    if not source_path == '':

        db_viewer = Viewer()
        db_viewer.load(app,source_path,center_of_screen)
        app.withdraw()
        db_viewer.mainloop()


database_open = button(app,text = 'Veritabanı Aç',relief = tk.FLAT, command = open_database)
database_open.load('./assets/open.png',{'x': int(125), 'y': int(100), 'w' : 150, 'h' : 40} )
database_open.colorize()

close_btn = button(app, text='Çıkış', relief=tk.FLAT, command = exit)
close_btn.load('./assets/close.png',
               {'x': int(125), 'y': int(160), 'w': 150, 'h': 40})
close_btn.colorize()

app.iconphoto(False,app_icon)
app.title("Veritabanı Uygulaması")

app.config(bg='#3F8F25')
app.mainloop()
