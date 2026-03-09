# ----------------------------------------------
# Author: Amanda Brock
# Date: March 8, 2026
# Assignment: Module 10.2
# Purpose: UI interface practice with tkinter
# ----------------------------------------------

import tkinter as tk
import tkinter.messagebox as msg


class Todo(tk.Tk):

    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.tasks_canvas = tk.Canvas(self)

        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)

        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.title("Brock-ToDo")
        self.geometry("300x400")

        # Menu bar at the top of the program window
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        # Create the File dropdown menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Exit option lets the user close the program from the menu
        self.file_menu.add_command(label="Exit", command=self.destroy)

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.task_create.focus_set()

        instructions = tk.Label(
            self.tasks_frame,
            text="Double right-click a task to delete it",
            bg="white",
            fg="black",
            pady=5
        )

        instructions.pack(side=tk.TOP, fill=tk.X)

        self.colour_schemes = [
            {"bg": "purple", "fg": "white"},
            {"bg": "gold", "fg": "black"}
        ]

        self.placeholder_text = "--- Add Tasks Below ---"

        placeholder = tk.Label(self.tasks_frame, text=self.placeholder_text, pady=10)

        self.set_task_colour(len(self.tasks), placeholder)

        # Bind double right-click so a task can be deleted
        placeholder.bind("<Double-Button-3>", self.remove_task)

        placeholder.pack(side=tk.TOP, fill=tk.X)

        self.tasks.append(placeholder)

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

    def add_task(self, event=None):

        task_text = self.task_create.get(1.0, tk.END).strip()

        # Prevent empty tasks
        if len(task_text) == 0:
            return

        # Prevent using placeholder text
        if task_text == self.placeholder_text:
            msg.showwarning("Invalid Task", "That text is reserved by the program.")
            self.task_create.delete(1.0, tk.END)
            return

        # Remove placeholder if it exists
        if len(self.tasks) == 1 and self.tasks[0].cget("text") == self.placeholder_text:
            self.tasks[0].destroy()
            self.tasks.clear()

        new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

        self.set_task_colour(len(self.tasks), new_task)

        # Double right-click allows the user to delete a task
        new_task.bind("<Double-Button-3>", self.remove_task)

        new_task.pack(side=tk.TOP, fill=tk.X)

        self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):

        task = event.widget

        # Prevent the instruction label from being deleted
        # This ensures the user can always see how to remove tasks
        if task.cget("text") == "Right-click a task to delete it":
            return

        self.tasks.remove(task)
        task.destroy()

        # Restore placeholder if all tasks deleted
        if len(self.tasks) == 0:

            placeholder = tk.Label(self.tasks_frame, text=self.placeholder_text, pady=10)

            self.set_task_colour(0, placeholder)

            # Placeholder can also be removed using the same double right-click action
            placeholder.bind("<Double-Button-3>", self.remove_task)

            placeholder.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(placeholder)

        self.recolour_tasks()

    def recolour_tasks(self):

        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):

        task_style_choice = divmod(position, 2)

        my_scheme_choice = self.colour_schemes[task_style_choice[1]]

        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    def on_frame_configure(self, event=None):

        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):

        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def mouse_scroll(self, event):

        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:

            if event.num == 5:
                move = 1
            else:
                move = -1

            self.tasks_canvas.yview_scroll(move, "units")


if __name__ == "__main__":

    todo = Todo()
    todo.mainloop()