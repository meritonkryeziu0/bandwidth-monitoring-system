from datetime import datetime
from psutil import net_io_counters
from tkinter import *
from PIL import ImageTk, Image
import shutil, os, humanize
from to_csv import ExportingToCSV
import visualize.VisualizeLoggedData as visualize


def export_action():
    shutil.copy(".tmp.csv", "log.csv")


def visualize_action():
    visualize.plot_graph()


def close_action():
    os.remove(".tmp.csv")
    exit(0)


class APP:
    # globals
    window = None
    bytes_recv_old, bytes_sent_old = net_io_counters().bytes_recv, net_io_counters().bytes_sent
    bytes_recv, bytes_sent = bytes_recv_old, bytes_sent_old
    download_speed, upload_speed = 0, 0

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
        self.photo.pack(expand=1)
        self.labels["download-header"].pack(expand=1)
        self.labels["download"].pack()
        self.labels["upload-header"].pack(expand=1)
        self.labels["upload"].pack()
        self.exportBtn.pack(expand=1)
        self.visualizeBtn.pack(expand=1)
        self.closeBtn.pack(expand=1)
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

        diff_recv = self.bytes_recv - self.bytes_recv_old
        diff_sent = self.bytes_sent - self.bytes_sent_old

        self.download_speed = humanize.naturalsize(diff_recv)
        self.upload_speed = humanize.naturalsize(diff_sent)

        dt = datetime.now()
        ExportingToCSV.write(dt.strftime('%Y/%m/%d %X'), diff_recv / (1024 ** 2), diff_sent / (1024 ** 2))

    def update_window(self):
        self.update_values()
        self.labels["download"].config(text=self.download_speed)
        self.labels["upload"].config(text=self.upload_speed)
        self.tk.after(1000, self.update_window)
