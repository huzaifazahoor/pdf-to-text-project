# PDF to Text Converter

This Python script recursively converts all PDF files in a specified directory to plain text files. If the PDF contains images, OCR is used to extract the text.

## Requirements

- Python 3
- PyPDF2
- pdf2image
- pytesseract
- PIL (Pillow)
- python-dotenv

You can install the required Python libraries using pip:

```pip install --upgrade -r requirements.txt```

You will also need to install Tesseract OCR on your system. On macOS, this can be done using the provided script.sh.

## Usage

- Update the root_folder and output_folder variables in the Python script to match your input and output directories.
- Run the Python script with:
```python3 pdf_to_txt.py```
- If you're using macOS, you can use the provided script.sh to automate the process.
- First, give it execution permissions:
```chmod +x ./script.sh```
- Then run it:
```./script.sh```

## Notes

- The Python script can be used on any OS, but the shell script is designed for macOS only.
- The script does not support password-protected PDFs.
- The script is resource-intensive and may take a long time to process large or complex PDFs.