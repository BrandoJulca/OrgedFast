import os
import shutil

current_path = os.getcwd()  # Obtener la ruta actual donde se ejecuta el script

file_types = {}

# Mapeo de extensiones a nombres descriptivos
extension_mapping = {
    #EJECUTABLES
    ".exe": "Archivos Ejecutables", #1
    ".msi": "Archivos Ejecutables", #2
    ".app": "Archivos Ejecutables", #3
    ".sh": "Archivos Ejecutables",  #4
    #EXCEL
    ".xlsx": "Archivos Excel",      #1
    ".xls": "Archivos Excel",       #2
    #WORD
    ".docx": "Archivos Word",       #1
    ".doc": "Archivos Word",        #2
    #POWER POINT
    ".pptx": "Archivos PowerPoint", #1
    ".ppt": "Archivos PowerPoint",  #2
    #TEXTO
    ".rtf": "Archivos de Texto",    #1
    ".txt": "Archivos de Texto",    #2
    #PDF
    ".pdf": "Archivos PDF",         #1
    #IMAGEN
    ".jpg": "Archivos de Imagen",   #1
    ".gif": "Archivos de Imagen",   #2
    ".jpeg": "Archivos de Imagen",  #3
    ".png": "Archivos de Imagen",   #4
    ".bmp": "Archivos de Imagen",   #5
    ".tiff": "Archivos de Imagen",  #6
    ".tif": "Archivos de Imagen",   #7
    ".svg": "Archivos de Imagen",   #8
    #COMPRIMIDOS
    ".zip": "Archivos Comprimidos", #1
    ".rar": "Archivos Comprimidos", #2
    ".7z": "Archivos Comprimidos",  #3
    #FILMORA
    ".wfp": "Archivos Filmora",     #1
    ".fsthumb": "Archivos Filmora", #2
    #STEAM
    ".url": "Archivos Steam",       #1
    #ACCESO_DIRECTO
    ".lnk": "Accesos Directos",     #1
    ".lnk": "Accesos Directos",     #2
    #C++
    ".cpp": "Archivos C++",         #1
    #AUDIO
    ".mp3": "Archivos de Audio",    #1
    ".wav": "Archivos de Video",    #2
    #VIDEO
    ".mp4": "Archivos de Video",    #1
    ".avi": "Archivos de Video",    #2
    ".mov": "Archivos de Video",    #3
    #HTML
    ".html": "Archivos Web",        #1
    ".htm": "Archivos Web",         #2
    ".css": "Archivos Web",         #3
    ".json": "Archivos Web",        #4
    #ROBLOX
    ".rbxl": "Archivos Roblox",     #1
    #ICONO
    ".ico": "Archivos de Iconos",   #1
    #APK
    ".apk": "Archivos Android",   #1
    # Agrega más extensiones y nombres descriptivos aquí
    
}

for entry in os.listdir(current_path):  # Usar la ruta actual en lugar del escritorio
    file_path = os.path.join(current_path, entry)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(entry)[1]
        if file_extension:
            if file_extension not in file_types:
                file_types[file_extension] = []
            file_types[file_extension].append(file_path)

for file_extension, files in file_types.items():
    if file_extension in extension_mapping:
        folder_name = current_path + "/" + extension_mapping[file_extension]
        os.makedirs(folder_name, exist_ok=True)
        for file_path in files:
            shutil.move(file_path, folder_name)


print("Archivos ordenados y organizados. ¡Gracias por usar esta app!")
input("Presione ENTER para terminar | </BranDev>")
#python -m PyInstaller --onefile --icon="icon.ico" OrgedFast.py


