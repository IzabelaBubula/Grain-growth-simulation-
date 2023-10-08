from tkinter import *
import Vizualization as Viz
from Import_Files import open_files

root = Tk()
t_1 = Text(root, wrap=WORD)  # Text box to show data from a .k file if needed


def click_action(points):
    Viz.show_whole_shape(points)


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            t_1.insert(END, f"File contents ({file_path}):\n")
            t_1.insert(END, content + "\n\n")
    except FileNotFoundError:
        t_1.insert(END, f"Error: File not found at '{file_path}'\n\n")
    except Exception as e:
        t_1.insert(END, f"An error occurred while reading '{file_path}': {e}\n\n")


def open_app(points):
    root.title('App')
    # root.geometry("600x600")

    b_1 = Button(root, text="Show", width=8, command=lambda: click_action(points))  # Show Visualization button
    b_2 = Button(root, text="Open K Files", width=8, command=open_files)  # Import button

    b_1.grid(row=0, column=0, sticky=W, pady=2)
    b_2.grid(row=0, column=1, sticky=W, pady=2)

    # Create a text widget to display file contents
    t_1.grid(row=1, column=0, pady=2)

    root.mainloop()

