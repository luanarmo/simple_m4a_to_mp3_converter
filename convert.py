import os
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment

def convert_m4a_to_mp3(input_path, output_path):
    try:
        sound = AudioSegment.from_file(input_path, format="m4a")
        output_path_with_extension = os.path.splitext(output_path)[0] + ".mp3"
        sound.export(output_path_with_extension, format="mp3")
        print(f"Conversion completed: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error converting: {input_path}\nError message: {e}")

def browse_files():
    input_files = filedialog.askopenfilenames(title="Select the files you want to convert", filetypes=[("M4A Files", "*.m4a")])
    
    if not input_files:
        return  # User canceled the selection

    output_folder = filedialog.askdirectory(title="Select the folder where you want to save the converted files")

    if not output_folder:
        return  # User canceled the folder selection
    
    for input_file in input_files:
        output_file = os.path.join(output_folder, os.path.basename(input_file))
        convert_m4a_to_mp3(input_file, output_file)

    print("Conversion completed for all selected files.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    browse_files()
