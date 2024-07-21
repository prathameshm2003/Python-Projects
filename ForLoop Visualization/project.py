import tkinter as tk

class LoopVisualizationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Loop Visualization")
        
        self.label1 = tk.Label(master, text="Enter the range for the loop:")
        self.label1.pack()

        self.start_entry = tk.Entry(master, width=5)
        self.start_entry.pack(side=tk.LEFT)
        self.end_entry = tk.Entry(master, width=5)
        self.end_entry.pack(side=tk.LEFT)

        self.visualize_button = tk.Button(master, text="Visualize Loop", command=self.visualize_loop)
        self.visualize_button.pack()

        self.canvas = tk.Canvas(master, width=400, height=200, bg='white')
        self.canvas.pack()

        self.current_iteration = tk.StringVar()
        self.current_iteration_label = tk.Label(master, textvariable=self.current_iteration)
        self.current_iteration_label.pack()

    def visualize_loop(self):
        try:
            start = int(self.start_entry.get())
            end = int(self.end_entry.get())
            self.canvas.delete("all")
            column = 50
            for i in range(start, end+1):
                self.canvas.create_text(column, 50, text=str(i))
                column += 50
            self.current_iteration.set("Loop completed!")
        except ValueError:
            pass

def main():
    root = tk.Tk()
    app = LoopVisualizationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
