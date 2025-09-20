from pypdf import PdfReader, PdfWriter
import argparse

def merge_pdf(input_pdf, replacement_pdf, page_to_replace, output_pdf):
    reader = PdfReader(input_pdf)
    print(f"Number of pages: {len(reader.pages)}")
    writer = PdfWriter()

    for i, page in enumerate(reader.pages):
        if i == page_to_replace - 1:  # Convert to 0-based index
            new_page = PdfReader(replacement_pdf).pages[0]
            writer.add_page(new_page)
        else:
            writer.add_page(page)

    with open(output_pdf, "wb") as output:
        writer.write(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Replace a page in a PDF file')
    parser.add_argument('input_pdf', help='Path to the input PDF file')
    parser.add_argument('replacement_pdf', help='Path to the PDF with replacement page')
    parser.add_argument('page_number', type=int, help='Page number to replace (1-based)')
    parser.add_argument('output_pdf', help='Path for the output PDF file')
    
    args = parser.parse_args()
    merge_pdf(args.input_pdf, args.replacement_pdf, args.page_number, args.output_pdf)
    #Example - python PDFMerge.py input.pdf replacement_page.pdf 13 output.pdf