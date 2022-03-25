import os
import shutil
from tkinter import messagebox

ruta_descargas = "C://Users/isael Diroche/Downloads//"
ruta_escritorio = "C://Users/isael Diroche/Desktop//"
ruta_documentos = "C://Users/isael Diroche/Documents//"
ruta_telegram = "C://Users/isael Diroche/Downloads/Telegram Desktop//"

ruta_imagenes = "C://Users/isael Diroche/Pictures//"
ruta_multimedia = "C://Users/isael Diroche/Videos//"

ext_texto = ['.txt', '.docx', '.doc', '.pdf', '.xlsx', '.pptx']
ext_texto_word = ['.docx', '.doc']
ext_texto_pdf = ['.pdf']
ext_texto_excel = ['.xlsx']
ext_texto_ppt = ['.pptx']

ext_foto = ['.jpeg', '.jpg', '.png', '.gif', '.pdn']
ext_multimedia = ['.mov', '.mp4', '.mp3']


# ================================================================================================== #
def ordenar_telegram(archivo, ext):
    for i in ext_texto_pdf:
        if ext == i:
            shutil.move(ruta_telegram + archivo, ruta_documentos + 'Archivos PDF')

    for i in ext_texto_word:
        if ext == i:
            shutil.move(ruta_telegram + archivo, ruta_documentos + 'Archivos word')

    for i in ext_texto_excel:
        if ext == i:
            shutil.move(ruta_telegram + archivo, ruta_documentos + 'Archivos excel')

    for i in ext_texto_ppt:
        if ext == i:
            shutil.move(ruta_telegram + archivo, ruta_documentos + 'Archivos ppt')

    for i in ext_foto:
        if ext == i:
            shutil.move(ruta_telegram + archivo, ruta_imagenes)

    for i in ext_multimedia:
        if ext == i:
            shutil.move(ruta_telegram + archivo, ruta_multimedia)


def telegram():
    for archivo in os.listdir(ruta_telegram):
        nombre_archivo, ext = os.path.splitext(archivo)
        ordenar_telegram(archivo, ext)
    messagebox.showinfo(message=f"Se han movido los archivos exitosamente!",
                        title="Directorio Telegram")


# ================================================================================================== #
def ordenar_escritorio(archivo, ext):
    for i in ext_texto_pdf:
        if ext == i:
            shutil.move(ruta_escritorio + archivo, ruta_documentos + 'Archivos PDF')

    for i in ext_texto_word:
        if ext == i:
            shutil.move(ruta_escritorio + archivo, ruta_documentos + 'Archivos word')

    for i in ext_texto_excel:
        if ext == i:
            shutil.move(ruta_escritorio + archivo, ruta_documentos + 'Archivos excel')

    for i in ext_texto_ppt:
        if ext == i:
            shutil.move(ruta_escritorio + archivo, ruta_documentos + 'Archivos ppt')

    for i in ext_foto:
        if ext == i:
            shutil.move(ruta_escritorio + archivo, ruta_imagenes)

    for i in ext_multimedia:
        if ext == i:
            shutil.move(ruta_escritorio + archivo, ruta_multimedia)


def escritorio():
    for archivo in os.listdir(ruta_escritorio):
        nombre_archivo, ext = os.path.splitext(archivo)
        ordenar_escritorio(archivo, ext)
    messagebox.showinfo(message=f"Se han movido los archivos exitosamente!",
                        title="Directorio Escritorio")


# ================================================================================================== #
def ordenar_descargas(archivo, ext):
    for i in ext_texto_pdf:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_documentos + 'Archivos PDF')

    for i in ext_texto_word:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_documentos + 'Archivos word')

    for i in ext_texto_excel:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_documentos + 'Archivos excel')

    for i in ext_texto_ppt:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_documentos + 'Archivos ppt')

    for i in ext_foto:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_imagenes)

    for i in ext_multimedia:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_multimedia)


def descargas():
    for archivo in os.listdir(ruta_descargas):
        nombre_archivo, ext = os.path.splitext(archivo)
        ordenar_descargas(archivo, ext)
    messagebox.showinfo(message=f"Se han movido los archivos exitosamente!",
                        title="Directorio Descargas")


# ================================================================================================== #
def ordenar_documentos(archivo, ext):
    for i in ext_texto_pdf:
        if ext == i:
            shutil.move(ruta_documentos + archivo, ruta_documentos + 'Archivos PDF')

    for i in ext_texto_word:
        if ext == i:
            shutil.move(ruta_documentos + archivo, ruta_documentos + 'Archivos word')

    for i in ext_texto_excel:
        if ext == i:
            shutil.move(ruta_documentos + archivo, ruta_documentos + 'Archivos excel')

    for i in ext_texto_ppt:
        if ext == i:
            shutil.move(ruta_documentos + archivo, ruta_documentos + 'Archivos ppt')

    for i in ext_foto:
        if ext == i:
            shutil.move(ruta_documentos + archivo, ruta_imagenes)

    for i in ext_multimedia:
        if ext == i:
            shutil.move(ruta_documentos + archivo, ruta_multimedia)


def documentos():
    for archivo in os.listdir(ruta_documentos):
        nombre_archivo, ext = os.path.splitext(archivo)
        ordenar_documentos(archivo, ext)
    messagebox.showinfo(message=f"Se han movido los archivos exitosamente!",
                        title="Directorio Documentos")
# ================================================================================================== #
