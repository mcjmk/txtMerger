#! python3
# txtMerger.py - simple script to merge all txt files from source folder, and save it as a one txt
# in a destination folder

import os
from tkinter import Tk, filedialog, simpledialog, messagebox


def select_folder(title, root):
    folder_path = filedialog.askdirectory(title=title)
    if not folder_path:
        messagebox.showerror("Error. No folder selected, the program will exit")
        root.destroy()
        exit()
    return folder_path


def get_txt_files(folder_path):
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')]


def merge(file_list):
    all_lines = []
    for file_path in file_list:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    all_lines.append(line.strip())
        except IOError as e:
            messagebox.showerror("Error", f"Unable to read from file: {e}")
    return all_lines


def main():
    root = Tk()
    root.withdraw()

    source_folder = select_folder("Select source directory", root)
    output_folder = select_folder("Select destination directory", root)
    output_file_name = simpledialog.askstring("Input", "Enter the name of the output file: ", parent=root)

    files = get_txt_files(source_folder)
    lines = merge(files)

    output_path = os.path.join(output_folder, f"{output_file_name}.txt")

    try:
        with open(output_path, 'w', encoding='utf-8') as output_file:
            for line in lines:
                output_file.write(f"{line}\n")
        messagebox.showinfo("Success", f"The output file has been saved as {output_path}")
    except IOError as e:
        messagebox.showerror("Error", f"Failed to write to the file: {e}")

    root.destroy()


if __name__ == "__main__":
    main()
