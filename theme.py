import os, sys, time, io
class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'

os.system("pkg install openssh")
os.system("pkg install ruby")
os.system("gem install lolcat")

def banner():
 os.system("clear")
 print(f"""{color.cyan}


 __  __ _ _            _____                 _ 
|  \/  (_|_)          |  __ \               (_)
| \  / |_ _   ______  | |__) |__ _ _ __ ___  _ 
| |\/| | | | |______| |  _  // _` | '_ ` _ \| |
| |  | | | |          | | \ \ (_| | | | | | | |
|_|  |_| |_|          |_|  \_\__,_|_| |_| |_|_|
      _/ |                                     
     |__/                                      
     Cassifer    -     Exploit

 """)
 print(f"{color.fin}")

#barra de carga
def carga():
    print(f"{color.verde}")
    print("""Loading…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    banner()

#menu principal

def menu():
    os.system("clear")
    banner()
    carga()
    print(f"{color.verde}    QUE BANER TE GUSTARIA PONER")
    print("")
    print(f"{color.verde}[1]LOBO")
    print(f"{color.verde}[2]OSO")
    print(f"{color.verde}[3]MARIO")
    print(f"{color.verde}[4]BATMAN")
    print(f"{color.verde}[5]MIKI")
    print(f"{color.verde}[6]FUCK")
    print(f"{color.verde}[7]MEGAMAN")
    print(f"{color.verde}[8]TANKE")
    print(f"{color.verde}[9]HELICOPTERO")
    print(f"{color.verde}[10]THECROSS")
    print(f"{color.verde}[11]SEXIGIRL")
    print(f"{color.rojo}[0]SALIR{color.fin}")
    eleccion =input(f"{color.cyan}ELIJE UN NUMERO >>{color.fin} ")
    if eleccion == "1" :
        banner()
        lobo()
        print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")

    elif eleccion == "2" :
        banner()
        oso()
        print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")
    elif eleccion == "3" :
     banner()
     mario()
     print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")
    elif eleccion == "4" :
     banner()
     batman()
     print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")
    elif eleccion == "5" :
     banner()
     miki()
     print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")
    elif eleccion == "6" :
     banner()
     dedo()
     print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")   
    elif eleccion == "7" :
     banner()
     megaman()
     print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")
    elif eleccion == "8" :
     banner()
     tanke()
     print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")
    elif eleccion == "9" :
     banner()
     helicoptero()
     print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")
    elif eleccion == "10" :
     banner()
     THECROSS()
     print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")
    elif eleccion == "11" :
     banner()
     SEXIGIRL()
     print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")
    elif eleccion == "0" :
     banner()
     salir() 
 
    else:
        incorrecto()
        
def incorrecto():
    os.system("clear")
    print(f"""{color.rojo}
░█████╗░██████╗░░█████╗░██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
██║░░██║██████╔╝██║░░╚═╝██║██║░░██║██╔██╗██║
██║░░██║██╔═══╝░██║░░██╗██║██║░░██║██║╚████║
╚█████╔╝██║░░░░░╚█████╔╝██║╚█████╔╝██║░╚███║
░╚════╝░╚═╝░░░░░░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝


██╗███╗░░██╗░█████╗░░█████╗░██████╗░██████╗░
██║████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║██╔██╗██║██║░░╚═╝██║░░██║██████╔╝██████╔╝
██║██║╚████║██║░░██╗██║░░██║██╔══██╗██╔══██╗
██║██║░╚███║╚█████╔╝╚█████╔╝██║░░██║██║░░██║
╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝

███████╗░█████╗░████████╗░█████╗░
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗
█████╗░░██║░░╚═╝░░░██║░░░███████║
██╔══╝░░██║░░██╗░░░██║░░░██╔══██║
███████╗╚█████╔╝░░░██║░░░██║░░██║
╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝{color.fin}""")
    time.sleep(4)
    menu()

def salir():
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    print(f"{color.fin}")
    sys.exit()
def lobo():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒
▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░▒▒▒▒▒
▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▌░░▒▒▒▒
▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄███▀░░░░▒▒▒
▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░█████░▄█░░░░▒▒
▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄████████▀░░░░▒▒
▒▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄███████▌░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░▄███████████▌░░░░░░░░▒
▒░░░░░░░░░░░░░░░▄▄▄▄██████████████▌░░░░░░░░▒
▒░░░░░░░░░░░▄▄███████████████████▌░░░░░░░░░▒
▒░░░░░░░░░▄██████████████████████▌░░░░░░░░░▒
▒░░░░░░░░████████████████████████░░░░░░░░░░▒
▒█░░░░░▐██████████▌░▀▀███████████░░░░░░░░░░▒
▐██░░░▄██████████▌░░░░░░░░░▀██▐█▌░░░░░░░░░▒▒
▒██████░█████████░░░░░░░░░░░▐█▐█▌░░░░░░░░░▒▒
▒▒▀▀▀▀░░░██████▀░░░░░░░░░░░░▐█▐█▌░░░░░░░░▒▒▒
▒▒▒▒▒░░░░▐█████▌░░░░░░░░░░░░▐█▐█▌░░░░░░░▒▒▒▒
▒▒▒▒▒▒░░░░███▀██░░░░░░░░░░░░░█░█▌░░░░░░▒▒▒▒▒
▒▒▒▒▒▒▒▒░▐██░░░██░░░░░░░░▄▄████████▄▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒██▌░░░░█▄░░░░░░▄███████████████████
▒▒▒▒▒▒▒▒▒▐██▒▒░░░██▄▄███████████████████████
▒▒▒▒▒▒▒▒▒▒▐██▒▒▄████████████████████████████
▒▒▒▒▒▒▒▒▒▒▄▄████████████████████████████████
████████████████████████████████████████████''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close()
def helicopter():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''  ''' |lolcat""")
 fd.write(f"{salto}PS1='$'")
 fd.close()


def oso():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█  ''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close()


def mario():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''░░░░█████░░░░░░░░
░░░█▓▓▒▓▓██░░░░░░
░░░█▓▒▒▒▓▓▓█░░░░░
░░███████▓▓▓█░░░░
░██████████▓▓█░░░
░███████████▓▓█░░
░░██░░▒░░▒██▓██░░
░░░█░█▒█░▒▒██▒▒█░
░░█▒░█▒█░▒▒██▒▒█░
░░█▒▒▒▒▒▒▒██▒▒▒█░
░░█▒▒▒▒██▒▒█▒▒▒█░
░░███████▒▒▒██░░░
░░██████▒▒▒▒██░░░
░░░░█▒▒▒▒▒▒██░░░░
░░░░░██████░░░░░░ ''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close()

def batman():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░▄█░░░░░░░░░░░░██░░░
░░░░░▄██░░░░░░░░░░░███░░░
░░░░░███░░░░░░░░░░████░░░
░░░░████░░▄▄▄▄░░░█████░░░
░░░███████████████████░░░
░░░███████████████████░░░
░▄█████████████████████░░
░██████████████████████░░
░██████████████████████░░
░█░▀████████▀░▄████████░░
▄██▄▄█████▄▄▄██████████▄░
██▀███████▀▀█▀▀░░███████░
░█░░░▀▀▀░░░░▀▀░░░███████░
░█░░░████▄░░░░░░░████████
░█░░░░░░░░░░░░░░░████████
░██░░░░░░░░░░░░░░████████
░░█░░░░░░░░░░░░▄█████████  ''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close()

def miki():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓█████▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓
▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓█████████▓▓▓▓▓▓▓▓
████▓▓█████▓░▓██▓▓▓▓▓▓
█████▒▓███▒░░░▓█▓▓▓▓▓▓
██████████░░░░█▒██▓▓▓▓
██████▒░░█░░░░█▒█▓▓▓▓▓
█████▓░░░░░░░░█▒███▓██
█████░░▒▒░░░░░█░▓▒░███
▓▓▓▓█▒░░▒░░░░░░░░░░░█▓
▓▓▓▓█▓░░░▓░░░░░░░░░▒█▓
▓▓▓▓▓█▒░░██░░░░░░░▒█▓▓
▓▓▓▓▓▓█▓▒▓███▓▒▒▒▓█▓▓▓
▓▓▓▓▓▓▓██▒███░████▓▓▓▓
▓▓▓▓▓▓▓██▓░▒░▓█████▓▓▓  ''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close()

def tanke():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''-----██████████ ]▄▄▄▄▄▄▄▄▄▄▄▄▃
▂▄▅█████████▅▄▃▂
I███████████████████].
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...  ''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close()

def dedo():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e ''' ───────────────────██
──────────────────█─██
──────────────────█───█
──────────────────█───█
──────────────────█───█
──────────────────█───█
──────────────────█───█▓
──────────────────█───▓█
──────────────────█───░█
──────────────────█───░█
──────────────────█░░░─█
───────────▓███──██▓▓███
───────────██──▓██▓────██
───────────█▓────█▓─────▓█
───────────█▓─────█──────░█
██████─────█▓─────█────────█
████████▓███░──────█──█▓────█
█░░░░░░█───────────█░███────█▓
▓██████─────────────█▓██────██
███████░────────────────────▓█
▓██████░────────────────────░█
▓██████░────────────────────▓█
▓██████░────────────────────█▓
▓██████░────────────────────█
▓██████░───────────────────██
▓███░██░──────────────────█
▓███──████████████████████
██████
 ''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close()

def megaman():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''░░░░░░░░░░▄▄█▀▀▄░░░░
░░░░░░░░▄█████▄▄█▄░░░░
░░░░░▄▄▄▀██████▄▄██░░░░
░░▄██░░█░█▀░░▄▄▀█░█░░░▄▄▄▄
▄█████░░██░░░▀▀░▀░█▀▀██▀▀▀█▀▄
█████░█░░▀█░▀▀▀▀▄▀░░░███████▀
░▀▀█▄░██▄▄░▀▀▀▀█▀▀▀▀▀░▀▀▀▀
░▄████████▀▀▀▄▀░░░░
██████░▀▀█▄░░░█▄░░░░
░▀▀▀▀█▄▄▀░██████▄░░░░
░░░░░░░░░█████████░░░░  ''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close() 


def helicoptero():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''──▀▀▀▀▀▀▀▀▀▀▀▄▄▀▀▀▀▀▀▀▀▀▀▀
────────────█▀▀█
───────────█▓▓▓▓█
───────══▄▀█▓▓▓▓█▀▄══
──▄▄▄▄▄▄▄█▒█▓▓▓▓█▒█▄▄▄▄▄▄▄
──█▀▀▀▀█▀███▄▓▓▄███▀█▀▀▀▀█
─▄█▄──▄█▄───▀██▀───▄█▄──▄█▄
─█▒█──█▒█──────────█▒█──█▒█
─▀▀▀──▀▀▀──────────▀▀▀──▀▀▀  ''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close() 


def THECROSS():
	salto = "\n"
	fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
	fd.write(f"clear{salto}")
	fd.write("""echo -e
	
     ""____________6____________
__________66666__________
_________6666666_________
_________6666666_________
__________66666__________
___6_______666_______6___
__666______666______666__
_66666666666666666666666_
_66666666666666666666666_
_66666666666666666666666_
__666______666______666__
___6_______666_______6___
___________666___________
___________666___________
___________666___________
___________666___________
___________666___________
___________666___________
__________66666__________
_________6666666_________
__________66666__________
___________666___________
""
         
|lolcat""")
 

def SEXIGIRL():
	salto = "\n"
	fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
	fd.write(f"clear{salto}")
	fd.write("""echo -e
______ MMMMMoooooooooooM8888888,
_____M6ooooMMMmoooooooM888888888,
_____Mmooo8oooooooooooooM888888888,
____MmmmooooooooooooooM888888888888,
___Moooooooooo8888888M8888888888888888,
__Mooooooooooooo88888M88888888888888888,
___MmooooooooooooooommM8888888888888888,
_______M88ooooo888mooMM88888888888888888,
________M88888888oommooM8888888888888888,
_________M888888ooooMM8888888888888888888,
_________MooooooooooM888888888888888888888,
______888MoooooooooM8888888888888888888888,
___888888MooooooooM88888888888888888888888,
__88888888MoooooooM8888888888mmmm88888888,
_888888888Mo8oooooM8888888MooooooooM888888,
8888888888Moo8oooM8888MM8ooooooooooooM88888,
8888888888Mooo88ooooM888MoooooooooooooM8888,
_M8o8888ooo8oo88ooo0ooMMoo888oooooooooooM88,
Mooo88888ooo8o88o8oooooooooo8888oooooooooM8,
Moo8888o8ooooo8ooooooooooooooo8888ooooooooM8,
Mooo88oooooooooooooooooooooooo888888oooooooM8,
Mooooooooooooooooooooooooooooo88888888ooooooM8,
_MooMooooooooooooooooooooooooooM888ooo88oooooM,
__Mmoooooooooooooooooooooooooo888Moooo8oooooooM,
___Moooooooooo8oooooooooooooo8888MMooooooooooooM,
____Moooooooo88ooooooooooooo88888MMM8oooooooooooM,
____Moooooooo88oooooooooooooo88888MMMMoooooooooooM,
____Moooooooo88Moooooooooooooooo88888MMMMoooooooooM,
___Mooooooooo88Moooooooooooooooo8MooooMMMMoooooooooM,
__Mooooooooo8MMooooooooooooooo88MoooooMMMMooooooooooM,
_Mooooooooo88MMoom888mooooooo88MooooooMM_MMoooooooooo,
_M8moooooo888MMoom@@8moooo8888M8oooooooMM__MMooooooo,
M@88moooo888MooMom8@8mooo8888MooooooooMM___Mmoooooo0,
_*M8mooo8888MooooMm8mooo888M888ooooooooMM___Moooooo00,
____MMMMMM8888oooooMMmmmmM88888oooooooMM_Moooooooo0,
__________M88Moooooo8888888888oooooooooooMMoooooooooo,
__________M88Mooooo8o888888888ooooooooooooMoooooooo88,
___________M88Mooooo8ooo888888oooooooooooMooooooo8888,
____________M888Mooo888ooooo888ooooooooooMoooooo8888M,
____________M88888Moo888oooooo8888ooooooMooooooo888M8,
_____________M888888Mo8888oooooo8888oooMooooooo888M88,
______________M8888888Mo8888ooooooooooMoooooooo88M888,
________________M888888M88888oooooooooMoooooooo8M8888,
_________________M8oo888M888888ooooooMoooooooo8M88888,
__________________M8ooooMM88888888ooMooooooooM8888ooo,
___________________MooooM_M88888888MooooooooM888ooooo,
____________________MooooM_M888888Mooooooo8M88**ooooo,
_____________________MooooM_mmmmmmMoooooo8Mmoooooo,
______________________MoooQooommmmMoooMMooooooooooo,
_____________________MM88ooo8ooooMMMooooooooooooooooo,
__________________mM8888M88o88mMmoooooooooooooooooooo,
____________mMMMoooooooooM888Mmoooooooooooooooooooooo,
_______MMMMoooooooooooooooMMooooooooooooooooooooooooo,
___MMMoooooooooooooooooMMoooooooooooooooooooooooooooo,
MMMooooooooooooooooooMMooooooooooooooooooooooooooooo8,
oooooooooooooooooooMMooooooooooooooooooooooooooooo888,
oooooooooooooooooMMooooooooooooooooooooooooooo8888888,
oooooooooooooooMMoooooooooooooooooooooooooo8888888888,
oooooooooooooMooooooooooooooooooooooooooo88888888888M,
ooooooooooooMooooooooooooooooooooooooo8888888888M____,
oooooooo88Mooooooooooooooooooooooo88888888888M_______,
oo8888888Mooooooooooooooooooooo888888MMMMMMMMMMMM8,
8888MMMMMooooooooooooooooooooo8888M888888888888888888,
8MMM888Moooooooooooooooooooo88M8ooooooooooo8888888888,
88oooooMoooooooooooooooooooMMoooooo888888888888888888,
8888888M8888oooooo88ooooooMoo888888888888888888888MM,
MMMMMMMM888888ooo88888oo8Mo8888888888888888888888888


 
|lolcat""")



menu()
