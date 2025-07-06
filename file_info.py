import os

ruta = input("📂 Escribe la ruta de la carpeta a analizar:\n→ ")

#Si la ruta no es absoluta la asumimos dentro de la carpeta home
if not os.path.isabs(ruta):
    ruta = os.path.join(os.path.expanduser("~"), ruta)
else:
    ruta = os.path.expanduser (ruta)

ruta = os.path.abspath(ruta)

#validamos si la ruta existe
if not os.path.isdir(ruta):
    print("❌ La carpeta no existe o no es una carpeta valida. Verifica la ruta.")
    exit()

print(f"\n✅ Carpeta a analizar: {ruta}")

#Diccionario para contar por tipo de archivo
conteo_extensiones = {}
total_archivos = 0
tamaño_total = 0 #en bytes o MB

for carpeta_actual, subcarpetas, archivos in os.walk(ruta):
    for archivo in archivos:
        total_archivos += 1

        #Rutra completa del archivo
        ruta_archivo = os.path.join(carpeta_actual, archivo)

        #obtenemos el tamaño del archivo
        try:
            tamaño = os.path.getsize(ruta_archivo)
            tamaño_total += tamaño
            #muestra cada archivo y su tamaño
            print(f"📄 {archivo} → {round(tamaño / (1024 * 1024), 2)} MB → en: {carpeta_actual}")
        except:
            continue #esto si no puede leerse solo lo ignoramos

        #contamos por extension
        _, extension = os.path.splitext(archivo)
        if extension:
            conteo_extensiones[extension] = conteo_extensiones.get(extension, 0) + 1
        else:
            conteo_extensiones["(sin extension)"] = conteo_extensiones.get("sin extension", 0) + 1

print("\n📊 Resultados de analisis\n")

print(f"📁 Total de archivos encontrados: {total_archivos}")
print(f"💾 Tamaño total ocupado: {round(tamaño_total / (1024 * 1024), 2)} MB\n")

print("📌 Archivos por tipo de extensión:")
for extension, cantidad in conteo_extensiones.items():
    print(f"  - {extension}: {cantidad} archivo(s)")