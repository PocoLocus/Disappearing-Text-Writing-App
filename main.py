import tkinter

class App:
    def __init__(self):
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.TOTAL_TIME = 3
        self.timer_object = None

    def setup_ui(self):
        self.window = tkinter.Tk()
        # self.window.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.window.title("Disappearing Text Writing App")

        self.timer_label = tkinter.Label(self.window, text=self.TOTAL_TIME, font=("Arial", 16), width=4, height=1, bg="white", borderwidth=2, relief="groove")
        self.timer_label.grid(row=0, column=0, padx=10, pady=10)
        self.text_entry = tkinter.Text(self.window, font=("Arial", 12), width=80, height=30)
        self.text_entry.focus()
        self.text_entry.grid(row=1, column=0, padx=10, pady=10)

        self.window.bind("<Any-KeyPress>", self.key_press)

        self.window.mainloop()

    def key_press(self, event):
        time_left = self.TOTAL_TIME
        if self.timer_object is not None:
            self.window.after_cancel(self.timer_object)
        self.countdown(time_left)

    def countdown(self, time_left):
        self.timer_label.config(text=time_left)
        if time_left > 0:
            self.timer_object = self.window.after(1000, self.countdown, time_left-1)
        else:
            self.out_of_time()

    def out_of_time(self):
        self.text_entry.delete(1.0, "end")


app = App()
app.setup_ui()
