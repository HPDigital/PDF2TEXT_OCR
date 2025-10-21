"""
PDF2TEXT_OCR
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

# Asegúrate de configurar el camino al ejecutable de tesseract si no está en PATH
# pytesseract.pytesseract.tesseract_cmd = r'<path_a_tu_tesseract.exe>'

def pdf_to_text_ocr(pdf_path):
    # Abre el documento PDF
    doc = fitz.open(pdf_path)
    text = ""

    for page_num in range(len(doc)):
        # Obtiene la página
        page = doc.load_page(page_num)

        # Extrae la imagen de la página
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes()))

        # Usa OCR para convertir la imagen a texto
        text += pytesseract.image_to_string(img)

    return text

# Ruta al archivo PDF
pdf_path = r"C:\Users\HP\Downloads\doc.pdf"
ruta_txt_destino =r"C:\Users\HP\Downloads\doc.txt"

# Convertir el PDF a texto con OCR
text = pdf_to_text_ocr(pdf_path)

# Opcional: guardar el texto en un archivo
with open(ruta_txt_destino, 'w') as f:
    f.write(text)

print("Conversión completada.")


# In[ ]:





# In[ ]:





# In[ ]:






if __name__ == "__main__":
    pass
