from pathlib import Path
from PyPDF2 import PdfReader,PdfWriter
PASTA_RAIZ =Path(__file__).parent
CAMINHO_PDF = PASTA_RAIZ / 'pdf1.pdf'
PDF_NOVO = PASTA_RAIZ / 'pdf2.pdf'

reader = PdfReader(CAMINHO_PDF)
page0 = reader.pages[0]
# print(page0.extract_text())
# print(page0.images)


# with open(page0.images[0], 'wb') as imagem: # type: ignore
#     imagem.write(page0.images[0].data)

writer = PdfWriter()
writer.add_page(page0)

with open(PDF_NOVO, 'wb') as fp:
    writer.write(fp)