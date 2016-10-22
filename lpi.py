#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

          _  (`-')  _      
   <-.    \-.(OO ) (_)     
 ,--. )   _.'    \ ,-(`-') 
 |  (`-')(_...--'' | ( OO) 
 |  |OO )|  |_.' | |  |  ) 
(|  '__ ||  .___.'(|  |_/  
 |     |'|  |      |  |'-> 
 `-----' `--'      `--'    

*---------------------------------*
* LINUX POST INSTALLER - Ver. 1.0 *
*---------------------------------*

- Autore: Stefano Peris <SpaghettiDeveloper>
- eMail: stefano.peris.dev@gmail.com

"""

## IMPORTANTE:

## Se necessario, dare i permessi di esecuzione al fine con: chmod +x lpi.py
## Per generare il bytecode "*.pyc", da terminale scrivere il seguente comando: python -c "import lpi.py"

import os


def Clearscreen():
      os.system('clear')

def Menu():
      Clearscreen()

      print("*---------------------------------*")
      print("* LINUX POST INSTALLER - Ver. 1.0 *")
      print("*---------------------------------*")
      print("")
      print("- Autore: Stefano Peris <SpaghettiDeveloper>")
      print("- eMail: stefano.peris.dev@gmail.com")
      print("")
      print("---------- MENU ----------")
      print("")
      print("")
      print("")
      print("[1] Python 3.x - pip + Pygame")
      print("[2] Midnight Commander")
      print("[3] Vim")
      print("[4] Git")
      print("[5] Wget")
      print("[6] Htop")
      print("[7] Zim")
      print("[8] Build Essential")
      print("[9] Cmake")
      print("[q] Esci")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# Python 3.x - Gestore moduli pip + Pygame.

os.system("sudo apt-get install python3-pip")

os.system("python3 -m pip install pygame")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# MIDNIGHT COMMANDER - File manager per sistemi Unix e Unix-like.

os.system("sudo apt-get install -y mc")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# VIM - Editor di testo modale.

os.system("sudo apt-get install -y vim")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# GIT - software di controllo versione distribuito utilizzabile da interfaccia a riga di comando.

os.system("sudo apt-get install -y git")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# WGET - Gestore di download libero, multipiattaforma. Supporta i protocolli HTTP, HTTPS e FTP.

os.system("sudo apt-get install -y wget")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# HTOP - visualizzatore di processi basato su ncurses, simile a top,
# ma permette di scorrere l'elenco verticalmente ed orizzontalmente
# per vedere tutti i processi e la loro intera riga di comando.

os.system("sudo apt-get install -y htop")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# ZIM - Editor di wiki che consente di scrivere in modo visuale ipertesti con un minimo di formattazione,
# di inserire immagini e di esportare il tutto in html direttamente sul browser di sistema,
# non richiede installazioni di alcun software aggiuntivo, è molto leggero e stabile. 

os.system("sudo apt-get install -y zim")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# BUILD ESSENTIAL - Collezione di compilatori e librerie.

os.system("sudo apt-get install -y build-essential")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# CMAKE - Software libero multipiattaforma per l'automazione dello sviluppo.

os.system("sudo apt-get install -y cmake")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

