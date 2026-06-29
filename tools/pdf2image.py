import os
from pdf2image import convert_from_path

def pdf2image(path):
    images = convert_from_path(pdf_path=path)
    for idx, img in enumerate(images):
        basename = f"{idx + 1}.png"
        img_name = os.path.join(r"C:\Users\Lenovo\Desktop", basename)
        img.save(img_name)
        print("已保存图片")
pdf2image(r"C:\Users\Lenovo\Desktop\6拖带示意图.pdf")



