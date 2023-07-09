import os
import fitz
import pytesseract
from PIL import Image
from dotenv import load_dotenv

load_dotenv()


def convert_pdf_to_txt(path):
    """
    This function converts a PDF to an editable text file.
    It checks whether a PDF contains images. If it does, OCR is applied;
    otherwise, the text is extracted directly.
    """
    try:
        # Open the PDF
        doc = fitz.open(path)

        # Check if the PDF is encrypted
        if doc.is_encrypted:
            print(f"The file {path} is encrypted and cannot be processed.")
            return

        text = ""

        # Iterate over PDF pages
        for page in doc:
            # Try to extract text
            extracted_text = page.get_text()
            if extracted_text:  # Text-based PDF
                text += extracted_text.strip()
            else:  # Image-based PDF, use OCR
                pix = page.get_pixmap()
                img = Image.frombytes(
                    "RGB",
                    [pix.width, pix.height],
                    pix.samples,
                )
                text += str(pytesseract.image_to_string(img)).strip()

        return text.strip()

    except Exception as e:
        print(f"There was an error processing the file {path}. Error: {e}")
        return


def write_to_txt(text, output_path):
    """
    This function writes the extracted text to a .txt file.
    """
    # Ensure the directory exists; if not, create it
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    root_folder = os.getenv("PDF_FOLDER_PATH")
    output_folder = "./output/"

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
                    print("Writting", txt_path, "successfully\n\n")

                # Optionally remove the processed PDF
                # os.remove(pdf_path)


if __name__ == "__main__":
    main()
