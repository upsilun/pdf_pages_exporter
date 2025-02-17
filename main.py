import PyPDF2

def extract_pages(input_pdf):
    while True:
        try:
            start_page = int(input("Enter the start page (or 0 to exit): "))
            if start_page == 0:
                break
            end_page = int(input("Enter the end page: "))

            if start_page > end_page or start_page < 1:
                print("Invalid page range. Try again.")
                continue

            with open(input_pdf, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                writer = PyPDF2.PdfWriter()
                
                total_pages = len(reader.pages)
                if end_page > total_pages:
                    print(f"End page exceeds total pages ({total_pages}). Try again.")
                    continue

                for i in range(start_page - 1, end_page):
                    writer.add_page(reader.pages[i])

                output_pdf = f"extracted_{start_page}_to_{end_page}.pdf"
                with open(output_pdf, "wb") as output:
                    writer.write(output)
                
                print(f"Pages {start_page} to {end_page} saved as {output_pdf}.")
        except ValueError:
            print("Invalid input. Please enter numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    pdf_file = input("Enter the PDF filename: ")
    extract_pages(pdf_file)
