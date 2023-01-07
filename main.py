from tkinter import *
from app import app as source_app 

if __name__ == '__main__':
    print("Its working!")
    window = Tk()
    app = source_app.APP(window)
    app.set_window_properties()
    app.update_window()
    app.setup()
    window.mainloop()
