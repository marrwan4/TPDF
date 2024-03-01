# File: CS112_A1_T2_3_20230381.py
# Purpose: pdf mini manger.
#          The application will allow the user to merge two pdf files together
#          and create a third file or extract individual pages from a pdf file.
# Authors: Marwan Hussein Galal \ Belal Alaa EL-Sabrawy 
# version: 1.0
# ID: 20230381
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#
import PyPDF2

def merge():
    from PyPDF2 import PdfWriter
    x = int(input("how many pdfs would you like to merge: "))
    pdfs = []
    for i in range(0, x, 1):
        input_name = input(f"Enter the name of the # {i+1} pdf: ")
        pdf = f"{input_name}.pdf"
        pdfs.append(pdf)
    print(pdfs)
    merger = PdfWriter()
    for pdf in pdfs:
        merger.append(pdf)
    name = input("what do you want to call the merged file?: ")
    merger.write(f"{name}.pdf")
    merger.close()

def extract():
    from PyPDF2 import PdfWriter , PdfReader
    input_name = input("Enter the name of the pdf: ")
    pdf = f"{input_name}.pdf"
    read = PdfReader(pdf)
    page = int(input("please input the page number you want to extract: "))
    for find in range (0, len(read.pages)):
        if page == find +1:
            break
        else:
            continue
    writer = PdfWriter()
    writer.add_page(read.pages[find])
    name = f"{input_name}_page_{find+1}.pdf"
    writer.write(f"{name}.pdf")
    writer.close()

def split():
    from PyPDF2 import PdfWriter , PdfReader
    input_name = input("Enter the name of the pdf: ")
    pdf = f"{input_name}.pdf"
    read = PdfReader(pdf)
    for i in range(len(read.pages)):
        writer = PdfWriter()
        writer.add_page(read.pages[i])
        name = f"{input_name}_page_{i+1}.pdf"
        writer.write(f"{name}.pdf")
    writer.close()

def main_menu():
    main_menu ="""
                |**Main Menu**|
    ---------------------------------------
    A) Merge two files
    B) Extract a page from file
    C) Split file into separate pages
    D) Exit
    """
    while True:
        print(main_menu)
        choice = input("Enter your choice: ").upper()
        if choice == "A":
            merge()
        elif choice == "B":
            extract()
        elif choice == "C":
            split()
        elif choice == "D":
            print ("\n******** Good Bye ********\n")
            break
        else:
            print ("Please enter a valid choice")
#================================================================================================================#
main_menu()