# Audio File Converter

## Description
This is a Python script that allows you to convert M4A audio files to MP3 format. It uses the `pydub` library to perform the conversions and provides a simple graphical interface to select input files, output folder, and perform the conversions.

## Dependencies

### FFmpeg
To perform the conversions, you need to have FFmpeg installed on your system. FFmpeg is a command-line tool used for processing multimedia files. You can download it from its official website: [FFmpeg Official Website](https://ffmpeg.org/download.html).

After installation, make sure to add the location of the FFmpeg executable folder to your system's PATH.

### Tkinter
The `tkinter` library is used to create the graphical interface in this script. In most cases, `tkinter` is already included in standard Python installations. However, if you need to install it, you can do so using the following command:

```bash
pip install tk
# for linux users
sudo apt-get install python3-tk
```
## Usage

1. Run the `convert.py` script.
2. Select the M4A files you want to convert using the file dialog.
3. Choose the output folder where you want to save the converted MP3 files.
4. The script will perform the conversions and display error messages if something goes wrong during the conversion of a specific file.
5. Upon completion, you will see a message indicating the successful conversion of all selected files.

## Notes

- If you encounter any issues with conversions, ensure that you have FFmpeg installed and configured correctly on your system.
- Make sure you have write permissions to the selected output folder.
- Keep in mind that the quality of the output file depends on the quality of the original file and the configuration options used in the conversion.

## Contributions

If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request in this repository.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
