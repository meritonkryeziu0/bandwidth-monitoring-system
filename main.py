from datetime import datetime
from psutil import net_io_counters
from tkinter import *
from PIL import ImageTk, Image
import humanize

def export_action():
    # TODO implement export_action() 
    pass


def visualize_action():
    # TODO implement visualize_action()
    pass

def close_action():
    # TODO implement close_action()
    pass

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

        global logo
        image = Image.open("photos/logo.jpg")
        img = image.resize((122, 78))
        logo = ImageTk.PhotoImage(img)
        self.photo = Label(image=logo)

        self.labels = {"download-header": Label(text="Download Speed", font="Arial 13 bold"),
                       "download": Label(text="Measuring...", font="Arial 11 bold", fg="#0e4373", pady=5),
                       "upload-header": Label(text="Upload Speed", font="Arial 13 bold"),
                       "upload": Label(text="Measuring...", font="Arial 11 bold", fg="#0e4373", pady=5), }

        self.exportBtn = Button(tk, text="Export", font="Arial 9 bold", padx=20, background="#145DA0",
                                foreground="white", activebackground="#0e4373", command=export_action)
        self.visualizeBtn = Button(tk, text="Visualize", font="Arial 9 bold", padx=12, background="#145DA0",
                                   foreground="white", activebackground="#0e4373", command=visualize_action)
        self.closeBtn = Button(tk, text="Close", font="Arial 9 bold", padx=21, background="#145DA0", foreground="white",
                               activebackground="#0e4373", command=close_action)
    
    def setup(self):
        self.photo.pack()
        self.labels["download-header"].pack()
        self.labels["download"].pack()
        self.labels["upload-header"].pack()
        self.labels["upload"].pack()
        self.exportBtn.pack()
        self.visualizeBtn.pack()
        self.closeBtn.pack()
        self.tk.update()

    def set_window_properties(self):
        self.window.title("Bandwidth monitoring system")
        self.window.geometry("400x500")
        self.window.resizable(False, False)

    def update_values(self):
        self.bytes_recv_old = self.bytes_recv
        self.bytes_sent_old = self.bytes_sent
        self.bytes_recv = net_io_counters().bytes_recv
        self.bytes_sent = net_io_counters().bytes_sent

        self.download_speed = humanize.naturalsize(self.bytes_recv - self.bytes_recv_old)
        self.upload_speed = humanize.naturalsize(self.bytes_sent - self.bytes_sent_old)

if __name__ == '__main__':
    print("Its working!")
    window = Tk()
    app = APP(window)
    app.set_window_properties()
    app.update_values()
    app.setup()
    window.mainloop()
