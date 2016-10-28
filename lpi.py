#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Schermata delle informazioni.
def About():
    print("""
          _  (`-')  _
   <-.    \-.(OO ) (_)
 ,--. )   _.'    \ ,-(`-')
 |  (`-')(_...--'' | ( OO)
 |  |OO )|  |_.' | |  |  )
(|  '__ ||  .___.'(|  |_/
 |     |'|  |      |  |'->
 `-----' `--'      `--'

*-------------------------------------*
* LINUX POST INSTALLER - Ver. 0.6 dev *
*-------------------------------------*

#===============================================================================
#title           :lpi.py
#description     :This will create a header for a python script.
#author          :Stefano Peris
#email           :stefano.peris.dev@gmail.com
#date            :28/10/2016
#version         :0.6
#usage           :python lpi.py
#notes           :
#python_version  :3.5
#===============================================================================
    """)

## IMPORTANTE:

## Se necessario, dare i permessi di esecuzione al fine con: chmod +x lpi.py
## Per generare il bytecode "*.pyc", da terminale scrivere il seguente comando: python -c "import lpi.py"

#===============================================================================

# Librerie e moduli
import os

# Variabili globali
opzione = 0

# Pulisce lo schermo ad ogni iterazione
def Clearscreen():
    os.system('clear')

#===============================================================================

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
    [9] Geany
    [i] Info
    [x] Esci
    """)

    opzione = input("Digita l'opzione desiderata > ")

    if opzione == "1":
        os.system("sudo apt-get install python3-pip")

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
            os.system("sudo apt-get install -y build-essential cmake libsdl1.2-dev libboost-dev")

        elif opzione == "9":
            os.system("sudo apt-get install -y geany")

        elif opzione == "10":
            os.system("sudo apt-get install -y gparted")

        elif opzione == "i":
            About()

        elif opzione == "x":
            exit()

        else:
            null
