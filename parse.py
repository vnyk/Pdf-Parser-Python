from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import re
import MySQLdb

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

s=convert('U16571275.pdf', pages=[0,1])
#print(s)


srn=re.findall(r'[A-Z]\d+\d+\d+\d+\d+\d+\d', str(s))
sr_date=re.findall(r'(.\d\W.\d\W.\d..)', str(s))
#k=re.findall(r't=(.*)\s+a:.*\s+(\d+)\s+.*=(.*)',str(s))
serv_desc=re.findall(r'([A-Z]\d.*\d)+\s+\W', str(s))
tof=re.findall(r'\W.*\W+\n+(.*?)+\n\w', str(s))
amt=re.findiall(r'(\d+\.\d*)', str(s))



db = MySQLdb.connect("localhost","usermm","root","zauba" )
cursor = db.cursor()
# Create table as per requirement
sql = " insert into zauba values("+ .join(srn) +","+.join(sr_date)+","+serv_desc+","+ .join(tof)+","+.join(amt)+");"

cursor.execute(sql)


db.close()


