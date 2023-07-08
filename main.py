import os
import PyPDF2
from pdf2image import convert_from_path
import pytesseract
from dotenv import load_dotenv

load_dotenv()


def convert_pdf_to_txt(path):
    """
    This function converts a PDF to an editable text file.
    It checks whether a PDF contains images. If it does, OCR is applied;
    otherwise, the text is extracted directly.
    """
    try:
        pdf_file = PyPDF2.PdfFileReader(path)
        text = ""

        # Check if PDF is Encrypted
        if pdf_file.isEncrypted:
            print(f"The file {path} is encrypted and cannot be processed.")
            return

        # PDF is image-based
        elif pdf_file.getPage(0).extractText() == "":
            pages = convert_from_path(path, 500)

            for page in pages:
                text += str(pytesseract.image_to_string(page))

        # PDF is text-based
        else:
            for page_num in range(pdf_file.numPages):
                page = pdf_file.getPage(page_num)
                text += page.extractText()

        return text
    except Exception as e:
        print(f"There was an error processing the file {path}.", e)
        return


def write_to_txt(text, output_path):
    """
    This function writes the extracted text to a .txt file.
    """
    with open(output_path, "w") as f:
        f.write(text)


def main():
    root_folder = os.getenv("PDF_FOLDER_PATH")
    output_folder = "output/"

    # Walk through the directory
    for subdir, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".pdf"):
                print(f"Processing {file}...")
                pdf_path = os.path.join(subdir, file)
                txt_path = os.path.join(
                    output_folder,
                    file.replace(
                        ".pdf",
                        ".txt",
                    ),
                )

                # Process the PDF and write to text file
                text = convert_pdf_to_txt(pdf_path)
                if text:
                    write_to_txt(text, txt_path)

                # Optionally remove the processed PDF
                # os.remove(pdf_path)


if __name__ == "__main__":
    main()
