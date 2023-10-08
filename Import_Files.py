from tkinter import filedialog
import App.App as App


def open_files():
    file_paths = filedialog.askopenfilenames(
        title="Select K Files",
        filetypes=[("K files", "*.k"), ("All files", "*.*")]
    )

    if file_paths:
        for file_path in file_paths:
            App.read_file(file_path)