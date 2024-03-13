# File: Pdf_tools.py
# Purpose: pdf mini manger.
#          The application will allow the user to merge two pdf files together
#          and create a third file or extract individual pages from a pdf file.
# Authors: Marwan Hussein Galal \ Belal Alaa EL-Sabrawy
# version: 1.1
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#
import PyPDF2

def merge(): #Belal
    from PyPDF2 import PdfWriter
    # Get the number of PDFs to merge from the user and handle less than 2 input
    while True:
        x = int(input("How many PDFs would you like to merge: "))
        if x < 2:
            print("You must enter at least 2.")
        else:
            break
    pdfs = []
    # Collect names of PDF files from the user
    for i in range(0, x, 1):
        input_name = input(f"Enter the name of the #{i + 1} PDF: ")
        pdf = f"{input_name}.pdf"
        pdfs.append(pdf)
    # Display the list of PDFs to be merged
    print(pdfs)
    # Create a PdfWriter object for merging PDFs
    merger = PdfWriter()
    # Append each PDF to the merger
    for pdf in pdfs:
        merger.append(pdf)
    # Get the name for the merged file from the user
    name = input("What do you want to call the merged file?: ")
    # Write the merged PDF to a new file
    merger.write(f"{name}.pdf")
    # Close the merger
    merger.close()
    print ("operation has been done!")

def extract(): #Marwan
    from PyPDF2 import PdfWriter, PdfReader
    # Get the name of the PDF from the user
    input_name = input("Enter the name of the PDF: ")
    pdf = f"{input_name}.pdf"
    # Create a PdfReader object for reading the PDF
    read = PdfReader(pdf)
    # Get the page number to extract from the user
    page = int(input("Please input the page number you want to extract: "))
    # Find the specified page and create a PdfWriter object for writing the extracted page
    for find in range(0, len(read.pages)):
        if page == find + 1:
            break
        else:
            continue
    writer = PdfWriter()
    writer.add_page(read.pages[find])
    # Generate a name for the extracted page file
    name = f"{input_name}_page_{find + 1}.pdf"
    # Write the extracted page to a new file
    writer.write(f"{name}.pdf")
    # Close the writer
    writer.close()
    print ("operation has been done!")

def split(): #Marwan
    from PyPDF2 import PdfWriter, PdfReader
    # Get the name of the PDF from the user
    input_name = input("Enter the name of the PDF: ")
    pdf = f"{input_name}.pdf"
    # Create a PdfReader object for reading the PDF
    read = PdfReader(pdf)
    # Create a PdfWriter object for writing each individual page
    for i in range(len(read.pages)):
        writer = PdfWriter()
        writer.add_page(read.pages[i])
        # Generate a name for the individual page file
        name = f"{input_name}_page_{i + 1}.pdf"
        # Write the individual page to a new file
        writer.write(f"{name}.pdf")
    # Close the writer
    writer.close()
    print ("operation has been done!")

def main_menu(): #Marwan
    # the menu options
    main_menu ="""
                |**Main Menu**|
    ---------------------------------------
    A) Merge files
    B) Extract a page from file
    C) Split file into separate pages
    D) Exit
    """
    # Continuously display the menu and handle user choices
    while True:
        print(main_menu)
        choice = input("Enter your choice: ").upper()
        if choice == "A":
            try:
                merge()
            except FileNotFoundError:
                print ("files are not found in the current directory!")
        elif choice == "B":
            try:
                extract()
            except FileNotFoundError:
                print ("file not found in the current directory!")
        elif choice == "C":
            try:
                split()
            except FileNotFoundError:
                print ("file not found in the current directory!")
        elif choice == "D":
            print ("\n******** Good Bye ********\n")
            break
        else:
            print ("Please enter a valid choice")
#================================================================================================================#
main_menu()