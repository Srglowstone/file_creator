#imports
import os
os.system("pip install termcolor")
from termcolor import colored

#Banner
print(colored("""
 #######   ####    ####     #######             ####   ######   #######    ##     ######    #####   ######
  ##   #    ##      ##       ##   #            ##  ##   ##  ##   ##   #   ####    # ## #   ##   ##   ##  ##
  ## #      ##      ##       ## #             ##        ##  ##   ## #    ##  ##     ##     ##   ##   ##  ##             ####      ##      ##       ####             ##        #####    ####    ##  ##     ##     ##   ##   #####
  ## #      ##      ##   #   ## #             ##        ## ##    ## #    ######     ##     ##   ##   ## ##
  ##        ##      ##  ##   ##   #            ##  ##   ##  ##   ##   #  ##  ##     ##     ##   ##   ##  ##
 ####      ####    #######  #######             ####   #### ##  #######  ##  ##    ####     #####   #### ##
""", "red"))

#Preguntamos al user el nombre del archivo y su extensión                                                             file_name = input("[*]Introduce el nombre del archivo: ")
file_ext = input("[*]Introduce la extensión del archivo.\n\ntxt (A)\npy (B)\njs (C)\njava (D)\nhtml (E)\nSi desea una>

#Condicionales + crear el archivo
if file_ext == "A":                                                                                                       file = open(f"{file_name}.txt", "w")

elif file_ext == "B":
    file = open(f"{file_name}.py", "w")

elif file_ext == "C":
    file = open(f"{file_name}.js", "w")

elif file_ext == "D":
    file = open(f"{file_name}.java", "w")

elif file_ext == "E":
    file = open(f"{file_name}.html", "w")

else:
    file = open(f"{file_name}.{file_ext}", "w")


#Preguntamos si desea iterar el archivo creado
iterar = input("[*]¿Desea iterar el archivo creado?\nSi (A)\nNo (B)\nRespuesta:  ")

#Creamos las condiciones
if iterar == "A":
    texto = input("[*]Introduzca el texto que desea incluir en el archivo creado: ")
    file.write(f"{texto}")

elif iterar == "B":
    print("[*]Gracias por usar este script.")

else:
    print("[Error]")