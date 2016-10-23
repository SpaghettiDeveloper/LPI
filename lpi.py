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

# Librerie e moduli

import os

# Variabili globali

opzione = 0

# Pulisce lo schermo ad ogni iterazione

def Clearscreen():
      os.system('clear')



while opzione:
      
      print("""
      *---------------------------------*
      * LINUX POST INSTALLER - Ver. 1.0 *
      *---------------------------------*
      
      +------------------ ABOUT -------------------+
      + Autore: Stefano Peris <SpaghettiDeveloper> +
      + eMail: stefano.peris.dev@gmail.com         +
      +--------------------------------------------+
      
      +------------------------+
      +--------- MENU ---------+
      +------------------------+


      [1] Python 3.x - pip + Pygame
      [2] Midnight Commander
      [3] Vim
      [4] Git
      [5] Wget
      [6] Htop
      [7] Zim
      [8] Build Essential
      [9] Cmake
      [q] Esci
      """)

      opzione = input("Digita l'opzione desiderata > ")

      if opzione == "1":
            os.system("sudo apt-get install python3-pip")
            os.system("python3 -m pip install pygame")

      elif opzione == "2":
            os.system("sudo apt-get install -y mc")

      elif opzione == "3":
            os.system("sudo apt-get install -y vim")

      elif opzione == "4":
            os.system("sudo apt-get install -y git")

      elif opzione == "5":
            os.system("sudo apt-get install -y wget")

      elif opzione == "6":
            os.system("sudo apt-get install -y htop")

      elif opzione == "7":
            os.system("sudo apt-get install -y zim")

      elif opzione == "8":
            os.system("sudo apt-get install -y build-essential")

      elif opzione == "9":
            os.system("sudo apt-get install -y cmake")

      elif opzione == "10":
            os.system("sudo apt-get install -y gparted")
      
      elif opzione == "q":
            exit()

      else:
            null

