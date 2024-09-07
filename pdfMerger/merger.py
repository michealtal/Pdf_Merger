# import PyPDF2
# import os

# merger = PyPDF2.PdfMerger()
# for file in os.listdir(os.curdir):
#     if file.endswith('.pdf'):
#         print(file)
#         merger.append(file)
# merger.write('merged.pdf')

# To merge specific PDFs:

# import PyPDF2
# import os

# def merge_pdfs(pdf_files, output_filename):
#     merger = PyPDF2.PdfMerger()
#     for pdf in pdf_files:
#         if os.path.exists(pdf):
#             merger.append(pdf)
#         else:
#             print(f"File not found: {pdf}")
#     merger.write(output_filename)
#     print(f"Merged PDF saved as: {output_filename}")

# # List of PDFs you want to merge
# pdfs_to_merge = ['file1.pdf', 'file2.pdf', 'file3.pdf']
# merge_pdfs(pdfs_to_merge, 'merged_output.pdf')

#To merge PDFs from a specific folder:
import PyPDF2
import os

def merge_pdfs_in_folder(folder_path, output_filename):
    merger = PyPDF2.PdfMerger()
    for file in os.listdir(folder_path):
        if file.endswith('.pdf'):
            file_path = os.path.join(folder_path, file)
            merger.append(file_path)
            print(f"Adding: {file}")
    merger.write(output_filename)
    print(f"Merged PDF saved as: {output_filename}")

# Specify the folder path containing PDFs
folder_path = r'C:\Users\Micheal\Desktop\testpdf'
merge_pdfs_in_folder(folder_path, 'merged_output.pdf')