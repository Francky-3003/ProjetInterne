#!/usr/bin/python3

# à executer dabord
# export PYTHONPATH="${PYTHONPATH}:/home/alexispondo/projet_pi/"
# import os
# os.system("source pi_env/bin/activate")

from core.some_function import *
from core.global_scan import *
from core.is_bruteforce_scan import *
from core.commonuserpass_scan import *
from core.sqli_scan import *
from core.xssi_scan import *
from core.cmd_i_scan import *

def first_display():
    clear()
    print_orange("Demarrage ScanPlus...")
    banner()
    print_orange("Quel type de scan voulez-vous effectuer? \n")
    print_orange("Tapez juste le numéro de scan que vous desirez effectuer, puis tapez la touche entrée du clavier\n")
    print_white("1) Scan Global\n")
    print_white("2) Scan Is_BruteForce\n")
    print_white("3) Scan CommonUserPass\n")
    print_white("4) Scan Injection SQL\n")
    print_white("5) Scan Injection XSS\n")
    print_white("6) Scan Injection de commandes\n")
    print_white("q) Quitter")
    print("")
    answer = input("scanplus> ")
    return answer


def main():
    answer = first_display()
    while answer != "q":
        if answer == "1":
            global_scan()
        elif answer == "2":
            is_bruteforce()
        elif answer == "3":
            CommonAuth()
        elif answer == "4":
            SQL_i()
        elif answer == "5":
            XSS_i()
        elif answer == "6":
            CMD_i()
        elif answer == "q":
            print("Ce fût un grand plaisir de vous voir sur ScanPlus. Au Revoir et à très bientôt!!!")
            break
        else:
            answer = first_display()


main()
