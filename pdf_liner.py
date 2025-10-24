import io

from reportlab.pdfgen.canvas import Canvas
from PyPDF2 import PdfReader, PdfWriter

from arg_parser import parse_args

def add_lines_to_pdf(
    input_pdf_path: str,
    output_pdf_path: str,
    line_spacing: float,
    line_opacity: float
):
    """
    Add equally spaced horizontal lines to all pages of a PDF.
    
    Args:
        input_pdf_path: Path to the input PDF file
        output_pdf_path: Path to save the output PDF file
        line_spacing: Space between lines in points (default: 30)
        line_opacity: Opacity of lines from 0.0 to 1.0 (default: 0.3)
    """
    
    print(f"[pdf](input): {input_pdf_path}")
    
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    
    total_pages = len(reader.pages)
    print(f"[pdf](pages): {total_pages}")
    
    for page_num, page in enumerate(reader.pages, 1):
        # print(f"[pdf]({page_num}/{total_pages}): completed")
        
        page_width = float(page.mediabox.width)
        page_height = float(page.mediabox.height)
        
        packet = io.BytesIO()
        canvas = Canvas(packet, pagesize=(page_width, page_height))
        
        canvas.setStrokeColorRGB(0, 0, 0)
        canvas.setStrokeAlpha(line_opacity)
        canvas.setLineWidth(0.5)
        
        y_position = line_spacing
        while y_position < page_height:
            canvas.line(0, y_position, page_width, y_position)
            y_position += line_spacing
        
        canvas.save()
        
        packet.seek(0)
        
        lines_pdf = PdfReader(packet)
        lines_page = lines_pdf.pages[0]
        
        page.merge_page(lines_page)
        
        writer.add_page(page)
    
    print(f"[pdf](output): {output_pdf_path}")
    with open(output_pdf_path, 'wb') as output_file:
        writer.write(output_file)
    
    print("[pdf]: completed")

def main():
    args = parse_args()
    
    add_lines_to_pdf(
        args.input_pdf,
        args.output_pdf,
        args.line_spacing,
        args.opacity
    )

if __name__ == "__main__":
    main()
