# from PyPDF2 import PdfFileReader
#
# def extract_information(pdf_path):
#     with open(pdf_path, 'rb') as f:
#         pdf = PdfFileReader(f)
#         information = pdf.getDocumentInfo()
#         number_of_pages = pdf.getNumPages()
#
#     txt = f"""
#     Information about {pdf_path}:
#     Author:{information.author}
#     Creator:{information.creator}
#     Producer:{information.producer}
#     Subject:{information.subject}
#     Title:{information.title}
#     Number of pages:{number_of_pages}
#     """
#
#     print(txt)
#     return information
#
# if __name__ == '__main__':
#     path = r'自产AES-2017001A-工程基本知识试题库20190829B.pdf'
#     # 这是我个人PDF的路径
#     extract_information(path)


import importlib
import sys
import time

importlib.reload(sys)
time1 = time.time()

import os.path
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


def parse(pdf_path, txt_path):
    '''解析PDF文本，并保存到TXT文件中'''
    fp = open(pdf_path, 'rb')
    # pdf1 = urlopen('http://www.tencent.com/20160321.pdf')
    # 用文件对象创建一个PDF文档分析器
    parser = PDFParser(fp)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器，与文档对象
    parser.set_document(doc)
    doc.set_parser(parser)

    # 提供初始化密码，如果没有密码，就创建一个空的字符串
    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDF，资源管理器，来共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释其对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # 循环遍历列表，每次处理一个page内容
        # doc.get_pages() 获取page列表
        for page in doc.get_pages():
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
            # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
            # 想要获取文本就获得对象的text属性，
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(txt_path, 'a') as f:
                        results = x.get_text()
                        print(results)
                        f.write(results + "\n")


if __name__ == '__main__':
    pdf_path = '自产AES-2017001A-工程基本知识试题库20190829B.pdf'
    txt_path = 'test.txt'
    parse(pdf_path, txt_path)
    time2 = time.time()
    print("总共消耗时间为:", time2 - time1)