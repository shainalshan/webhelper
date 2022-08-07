import time
from pytube import YouTube
#importing requests module
import requests
import sys
import pywhatkit
from docx2pdf import convert

def whatsapp():
    try:
        number = str(input("enter the destination number"))
        messege = str(input("enter your messege"))
        time = int(input("enter the hour(24)"))
        minute = int(input("enter the minute"))
        print(type("entered number is " + number))

        pywhatkit.sendwhatmsg('+91 number', 'messege', time, minute)
        print("succesfully send")
    except ValueError:
        print("you enterd a wrong value")

def ytd():
    print("welcome to Youtube video downloader\n")
    time.sleep(1)
    link = str(input("enter the video link\n"))
    try:
        # try > trying to get the link in to variable "a". if any error occur then jump into exception
        a = requests.get(link)
        # to access
        to_acces = YouTube(link)
        # to select reso
        to_select_reso = to_acces.streams.get_highest_resolution()
        # to download
        to_select_reso.download()
        print("dowloaded")
    except requests.exceptions.RequestException as w:
        print(w)

def doctopdf():

    try:
        # giving raw_input as r
        input_path = input(str(r"Enter the path and docs docx name "))
        output_path = input(str(r"enter the output path and pdf name"))
        convert(input_path,output_path)

        # to run without an input string
        # convert(r"C:\Users\shalu\Desktop\tech.docx ",r"C:\Users\shalu\Desktop\convetred2.pdf)
        print("conveted succes fully")
    except ValueError:
        print("you entered wrong path or fle name")
    except AssertionError:
        print("enterd wrong input \n=======================================\n")
        mainmenu = int(input("Enter     \n 8 for repeat  \n 0 for exit \n 1 for main menu"))
        try:
            if mainmenu == 8:
                doctopdf()
            elif mainmenu == 0:
                return exit()
            elif mainmenu == 1:
                engine()

            else:
                print("exiting...")
                return exit()
        except ValueError:
            print("wrong data")

def engine():
    try:
        print("INITIALIZING....")
        time.sleep(0.5)
        print("""               _       _          _                 
              | |     | |        | |                
 __      _____| |__   | |__   ___| |_ __   ___ _ __ 
 \ \ /\ / / _ \ '_ \  | '_ \ / _ \ | '_ \ / _ \ '__|
  \ V  V /  __/ |_) | | | | |  __/ | |_) |  __/ |   
   \_/\_/ \___|_.__/  |_| |_|\___|_| .__/ \___|_|   
                                   | |              
                                   |_|shainal badusha """)


        time.sleep(0.5)
        option=""
        while option != "exit":
            time.sleep(0.5)
            option = input(
                "Enter 1 for youtube downloader \nEnter 2 for Automatic whatsapp msg ""\nEnter 3 for Docs converter \nEnter 4 for future\n")
            if option == str(1):
                ytd()
            elif option == str(2):
                whatsapp()
            elif option == str(3):
                doctopdf()
            elif option == str(4):
                print("updation coming soon...")
            elif option == str("exit"):
                exit()
            else:
                print("you enterd a wrong choice\n --------------------------------------------")

    except ValueError:
        print("Returning to main menu")
        engine()


engine()