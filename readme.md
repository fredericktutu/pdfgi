# pdfgi
## A tool for combining several PDFs or deleting specific pages in a PDF using Python3

now it only support command-line execution

---
For combining, the combining function is defined as follow. 
```
def combine_pdf(addrs, all_pages=[],dest= None, name="new"):
``` 
+ The `addrs` is a list for all the addresses of the PDFs.

+ The `all_pages` is a list of lists, the ith element of it, is the corresponding pages we want of `addrs[i]`. It is set to an empty list as default.

+ The `dest` is the output folder path, and the `name` is the file name.

---
for deleting, the function:
```
def delete_page(addr, pages=[], dest= None, name="new"):
``` 
+ the `addr` is the PDF path
+ `pages` is a list, containing the page nums you wants to delete(start from 0).
+ other settings are similar.
