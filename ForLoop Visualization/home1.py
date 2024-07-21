import tkinter as tk
from tkinter import ttk
import time
from PIL import Image, ImageTk
import os
from tkinter import ttk, messagebox


class HomeWindow:
    def __init__(self, master, loop_type):
        self.master = master
        self.loop_type = loop_type
        self.table_rows = []

        if self.loop_type == "for":
            self.master.title("For Loop Window")
        elif self.loop_type == "nested":
            self.master.title("Nested For Loop Window")

        self.label1 = tk.Label(master, text="Enter the first loop value:",font=("MS Sans Serif", 15,"bold") )
        self.label1.pack(pady=10)

        self.loop_value_entry = tk.Entry(master,width=30)
        self.loop_value_entry.pack(pady=30)

        if self.loop_type == "nested":
            self.label2 = tk.Label(master, text="Enter the second loop value:",font=("MS Sans Serif", 15,"bold"))
            self.label2.pack(pady=10)

            self.second_loop_value_entry = tk.Entry(master,width=50)
            self.second_loop_value_entry.pack(pady=30)

        self.run_button = tk.Button(master, text="Run Loop",font=("MS Sans Serif", 15,"bold"), command=self.run_loop, bg="yellow",width=10, height=2)
        self.run_button.pack(pady=20)

        self.table = ttk.Treeview(master, height=50, columns=("Initialization", "Condition", "Increment/Decrement"))
        self.table.heading("Initialization", text="Initialization", anchor=tk.CENTER)
        self.table.heading("Condition", text="Condition", anchor=tk.CENTER)
        self.table.heading("Increment/Decrement", text="Increment/Decrement", anchor=tk.CENTER)
        self.table.column("#0", width=0, stretch=tk.NO) 
        self.table.column("Initialization", width=500, anchor=tk.CENTER)
        self.table.column("Condition", width=500, anchor=tk.CENTER)
        self.table.column("Increment/Decrement", width=500, anchor=tk.CENTER)
        self.table.pack(pady=10)
        ##self.table.pack(pady=10)

    def run_loop(self):
        self.clear_table()
        try:
            loop_value = int(self.loop_value_entry.get())
            if self.loop_type == "nested":
                second_loop_value = int(self.second_loop_value_entry.get())
                self.display_nested_loop(loop_value, second_loop_value)
            else:
                self.display_for_loop(loop_value)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid integer values.")

    def clear_table(self):
        for row in self.table_rows:
            self.table.delete(row)
        self.table_rows = []

    def display_for_loop(self, loop_value):
        self.display_for_loop_recursive(loop_value, 1)

    def display_for_loop_recursive(self, loop_value, i):
        if i <= loop_value:
            self.table_rows.append(self.table.insert("", "end", values=(f"i = {i}", f"i <= {loop_value}", "i++")))
            time.sleep(2.0)
            self.master.after(500, self.display_for_loop_recursive, loop_value, i + 1)

    def display_nested_loop(self, loop_value, second_loop_value):
        self.display_nested_loop_recursive(loop_value, second_loop_value, 1, 1)

    def display_nested_loop_recursive(self, loop_value, second_loop_value, i, j):
        if i <= loop_value:
            if j <= second_loop_value:
                self.table_rows.append(self.table.insert("", "end", values=(f"i = {i}, j = {j}",
                                                                             f"i <= {loop_value} && j <= {second_loop_value}",
                                                                             "j++")))
                time.sleep(2.0)
                self.master.after(500, self.display_nested_loop_recursive, loop_value, second_loop_value, i, j + 1)
            else:
                self.display_nested_loop_recursive(loop_value, second_loop_value, i + 1, 1)


def main():
    root = tk.Tk()
    app = HomeWindow(root, loop_type="for")
    root.mainloop()


if __name__ == "__main__":
    main()

