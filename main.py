from datetime import datetime
from tkinter import *


class APP:
    # globals
    window = None
    bytes_recv, bytes_sent, download_speed, upload_speed = 0, 0, 0, 0

    def __init__(self, tk):
        self.tk = tk
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.startTime = datetime.now()
        self.window = tk

        self.labels = {"download-header": Label(text="Download Speed", font="Monospace 12 bold"),
                       "download": Label(text="Measuring...", font="Monospace 12 bold"),
                       "upload-header": Label(text="Upload Speed", font="Monospace 12 bold"),
                       "upload": Label(text="Measuring...", font="Monospace 11 bold")
                       }

    def setup(self):
        self.labels["download-header"].pack()
        self.labels["download"].pack()
        self.labels["upload-header"].pack()
        self.labels["upload"].pack()
        self.tk.update()

    def set_window_properties(self):
        self.window.title("Bandwidth monitoring system")
        self.window.geometry("400x500")
        self.window.resizable(False, False)

    def update_values(self):
        print("called!")
        self.frame.after(1000, self.update_values)


if __name__ == '__main__':
    print("Its working!")
    window = Tk()
    app = APP(window)
    app.set_window_properties()
    app.update_values()
    app.setup()
    window.mainloop()
