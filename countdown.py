import tkinter as tk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self):
        self.minutes = 0
        self.seconds = 0
        self.hundredths = 0

        self.root = tk.Tk()
        self.root.geometry("500x400")
        self.root.configure(bg=("light yellow"))
        self.root.title("Countdown Timer")
        self.label = tk.Label(self.root, text="", font=("Arial black", 20,), bg="light yellow", fg="blue")
        self.label.pack(padx=50, pady=20)

        self.entry = tk.Entry(self.root,font=("Arial black", 12))
        self.entry.pack(pady=10)

        self.set_button = tk.Button(self.root, text="Set Timer",bg="blue",fg="white", font=("Arial black", 12,), command=self.set_timer)
        self.set_button.pack(pady=5)

        self.start_button = tk.Button(self.root, text="Start",bg="green",fg="white", font=("Arial black", 12), command=self.start_timer, state=tk.DISABLED)
        self.start_button.pack(side=tk.LEFT,padx=10, pady=15 )
        self.stop_button = tk.Button(self.root, text="Stop",bg="red",fg="white", font=("Arial black", 12), command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=15)
        self.clear_button = tk.Button(self.root, text="Clear",bg="light blue",fg="white", font=("Arial black", 12), command=self.clear_timer, state=tk.DISABLED)
        self.clear_button.pack(side=tk.RIGHT, padx=10, pady=15)



        self.timer_running = False

    def set_timer(self):
        try:
            self.minutes = int(self.entry.get())
            self.seconds = self.minutes * 60
            self.hundredths = 0
            self.label.config(text=f"Countdown: {self.minutes:02d}:{self.seconds // 3600:02d}:{self.seconds % 60:02d}")

            self.set_button.config(state=tk.DISABLED, bg="blue",fg="white", font=("Arial black", 12))
            self.start_button.config(state=tk.NORMAL,bg="green",fg="white", font=("Arial black", 12))
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number of minutes.")

    def start_timer(self):
        if not self.timer_running:
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.clear_button.config(state=tk.DISABLED)
            self.timer_running = True
            self.update_timer()

    def stop_timer(self):
        if self.timer_running:
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.clear_button.config(state=tk.NORMAL)
            self.timer_running = False

    def clear_timer(self):
        self.minutes = 0
        self.seconds = 0
        self.hundredths = 0
        self.label.config(text="")
        self.set_button.config(state=tk.NORMAL)
        self.clear_button.config(state=tk.DISABLED)

    def update_timer(self):
        if self.timer_running:
            if self.seconds > 0 or self.hundredths > 0:
                self.hundredths -= 1
                if self.hundredths < 0:
                    self.seconds -= 1
                    self.hundredths = 59

                minutes = self.seconds // 60
                seconds = self.seconds % 60
                time_string = f"{minutes:02d}:{seconds:02d}.{self.hundredths:02d}"
                self.label.config(text=time_string)
                self.root.after(10, self.update_timer)
            else:
                messagebox.showinfo("Time's Up!", "The countdown timer has ended.")
                self.root.destroy()

if __name__ == "__main__":
    timer = CountdownTimer()
    timer.root.mainloop()













