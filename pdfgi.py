import PyPDF2 as pp2
import re
def delete_page(addr, pages=[], dest= None, name="new"):
	'''
	addr is the address of the pdf file
	pages is a list storing the pages that should be deleted
	dest is the place the new pdf file will be stored in(the same as old by default)
	name is the name of the new_file
	'''
	try:
		with open(addr ,'rb') as pdf_file:
			pdf_reader = pp2.PdfFileReader(pdf_file)
			pdf_writer = pp2.PdfFileWriter()

			for page_num in range(pdf_reader.numPages):
				if page_num not in pages:
					print("page_num:",page_num)
					page_obj = pdf_reader.getPage(page_num)
					pdf_writer.addPage(page_obj)
			
			if not dest:
				matched = re.match(pattern=r"\w:\\([a-zA-Z_]+\\)*", string=addr).span()
				dest = addr[matched[0]:matched[1]]

			pdf_output_file = open(dest + name + '.pdf', 'wb')
			pdf_writer.write(pdf_output_file)
			pdf_output_file.close()

		print("delete pages sucess")

	except Exception as e:
		print(e)
		print("delete pages failed")

def combine_pdf(addrs, all_pages=[],dest= None, name="new"):
	#get destination
	if not dest:
		matched = re.match(pattern=r"\w:\\([a-zA-Z_]+\\)*", string=addrs[0]).span()
		dest = addrs[0][matched[0]:matched[1]]
	#writer and output stream
	pdf_writer = pp2.PdfFileWriter()
	with open(dest + name + '.pdf', 'wb') as pdf_output_file:
	#begin read and write
		i = 0
		for addr in addrs:
			pages = all_pages[i]
			with open(addr, 'rb') as pdf_file:
				pdf_reader = pp2.PdfFileReader(pdf_file)
				for page_num in pages:
					print("file {0}: page {1}".format(i, page_num))
					page_obj = pdf_reader.getPage(page_num)
					pdf_writer.addPage(page_obj)
				pdf_writer.write(pdf_output_file)
			i += 1
	print("combine pdf sucess")
'''
def test1():
	combine_pdf([r"E:\python\file\old1.pdf", r"E:\python\file\old2.pdf"], [[0], [0]])
	
def test2():
	combine_pdf([r"E:\python\file\old1.pdf"], [[i for i in range(100)]])
'''

			
