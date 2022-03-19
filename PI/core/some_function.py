from termcolor import cprint
import os
import random


print_white = lambda x: cprint(x, 'white')  # Color text on white
print_green = lambda x: cprint(x, 'green')  # Color text on green
print_red = lambda x: cprint(x, "red")
print_green =  lambda x: cprint(x, "green")
#def print_green(skk): print("\033[92m {}\033[00m" .format(skk))
print_yellow = lambda x: cprint(x, "yellow")
print_yellow_bold = lambda x: cprint(x, "yellow", attrs=['bold'])
print_red_bold = lambda x: cprint(x, "red", attrs=['bold'])
clear = lambda: os.system('clear')  # clear terminal

def banner():
    info_bas = """
Name: ScanPlus
Version: v2.0
Author: {
            Consultant Cybersécurité & Developpeur: {
                Nom: KONE Sounan
                LinkdIn: https://www.linkedin.com/in/sounan-franck-aristide-kon%C3%A9-8b7174174/
            },
            Consultant Cybersécurité & Developpeur: {
                Nom: DIDIA Suzanne
                LinkdIn: https://www.linkedin.com/in/suzanne-didia-9a630417a/
            },
            Consultant Cybersécurité & Developpeur: {
                Nom: PONDO Alexis
                LinkdIn: https://www.linkedin.com/in/alexis-pondo/
            }
}
GitHub: https://github.com/Francky-3003/ScanPlus

ScanPLus est un programme de scan de vulnérabilités développé par les étudiants de l' Ecole Supérieure Africaine des TIC (ESATIC).
ScanPlus fait l'objet d'un projet interne, intégré dans le programme de Master 2 de l'ESATIC
Ce programme permet de scanner les vulnerabilités ou failles communes dans les différentes à applications web et qui sont régulièrement publiées par les communautés de Cyberdéfense telles OWASP ou WASC.
Sa différence vient du fait qu'il peut effectuer plusieurs types de scans distinct et de façon indépendante selon les besoins de l'utilisateur. Il est exécutable aussi sur les OS Linux et Windows et egalement compatible pour tout type de plateformes web.

    """
    ban1 = """
==============================================================================================================================================
======================================================= ScanPlus =============================================================================
==============================================================================================================================================

   SSSSSSSSSSSSSSS                                                        PPPPPPPPPPPPPPPPP   lllllll
 SS:::::::::::::::S                                                       P::::::::::::::::P  l:::::l
S:::::SSSSSS::::::S                                                       P::::::PPPPPP:::::P l:::::l
S:::::S     SSSSSSS                                                       PP:::::P     P:::::Pl:::::l
S:::::S                cccccccccccccccc  aaaaaaaaaaaaa  nnnn  nnnnnnnn      P::::P     P:::::P l::::l uuuuuu    uuuuuu      ssssssssss
S:::::S              cc:::::::::::::::c  a::::::::::::a n:::nn::::::::nn    P::::P     P:::::P l::::l u::::u    u::::u    ss::::::::::s
 S::::SSSS          c:::::::::::::::::c  aaaaaaaaa:::::an::::::::::::::nn   P::::PPPPPP:::::P  l::::l u::::u    u::::u  ss:::::::::::::s
  SS::::::SSSSS    c:::::::cccccc:::::c           a::::ann:::::::::::::::n  P:::::::::::::PP   l::::l u::::u    u::::u  s::::::ssss:::::s
    SSS::::::::SS  c::::::c     ccccccc    aaaaaaa:::::a  n:::::nnnn:::::n  P::::PPPPPPPPP     l::::l u::::u    u::::u   s:::::s  ssssss
       SSSSSS::::S c:::::c               aa::::::::::::a  n::::n    n::::n  P::::P             l::::l u::::u    u::::u     s::::::s
            S:::::Sc:::::c              a::::aaaa::::::a  n::::n    n::::n  P::::P             l::::l u::::u    u::::u        s::::::s
            S:::::Sc::::::c     ccccccca::::a    a:::::a  n::::n    n::::n  P::::P             l::::l u:::::uuuu:::::u  ssssss   s:::::s
SSSSSSS     S:::::Sc:::::::cccccc:::::ca::::a    a:::::a  n::::n    n::::nPP::::::PP          l::::::lu:::::::::::::::uus:::::ssss::::::s
S::::::SSSSSS:::::S c:::::::::::::::::ca:::::aaaa::::::a  n::::n    n::::nP::::::::P          l::::::l u:::::::::::::::us::::::::::::::s
S:::::::::::::::SS   cc:::::::::::::::c a::::::::::aa:::a n::::n    n::::nP::::::::P          l::::::l  uu::::::::uu:::u s:::::::::::ss
 SSSSSSSSSSSSSSS       cccccccccccccccc  aaaaaaaaaa  aaaa nnnnnn    nnnnnnPPPPPPPPPP          llllllll    uuuuuuuu  uuuu  sssssssssss

""" + info_bas + """
==============================================================================================================================================
==============================================================================================================================================
==============================================================================================================================================



"""
    ban2 = """


  _________                   __________.__
 /   _____/ ____ _____    ____\______   \  |  __ __  ______
 \_____  \_/ ___\\__  \  /    \|     ___/  | |  |  \/  ___/
 /        \  \___ / __ \|   |  \    |   |  |_|  |  /\___ \
/_______  /\___  >____  /___|  /____|   |____/____//____  >
        \/     \/     \/     \/                         \/

""" + info_bas + """

"""

    ban3 = """

 .----------------.  .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    _______   | || |     ______   | || |      __      | || | ____  _____  | || |   ______     | || |   _____      | || | _____  _____ | || |    _______   | |
| |   /  ___  |  | || |   .' ___  |  | || |     /  \     | || ||_   \|_   _| | || |  |_   __ \   | || |  |_   _|     | || ||_   _||_   _|| || |   /  ___  |  | |
| |  |  (__ \_|  | || |  / .'   \_|  | || |    / /\ \    | || |  |   \ | |   | || |    | |__) |  | || |    | |       | || |  | |    | |  | || |  |  (__ \_|  | |
| |   '.___`-.   | || |  | |         | || |   / ____ \   | || |  | |\ \| |   | || |    |  ___/   | || |    | |   _   | || |  | '    ' |  | || |   '.___`-.   | |
| |  |`\____) |  | || |  \ `.___.'\  | || | _/ /    \ \_ | || | _| |_\   |_  | || |   _| |_      | || |   _| |__/ |  | || |   \ `--' /   | || |  |`\____) |  | |
| |  |_______.'  | || |   `._____.'  | || ||____|  |____|| || ||_____|\____| | || |  |_____|     | || |  |________|  | || |    `.__.'    | || |  |_______.'  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'

""" + info_bas + """

"""

    ban4 = """

 $$$$$$\                               $$$$$$$\  $$\
$$  __$$\                              $$  __$$\ $$ |
$$ /  \__| $$$$$$$\ $$$$$$\  $$$$$$$\  $$ |  $$ |$$ |$$\   $$\  $$$$$$$\
\$$$$$$\  $$  _____|\____$$\ $$  __$$\ $$$$$$$  |$$ |$$ |  $$ |$$  _____|
 \____$$\ $$ /      $$$$$$$ |$$ |  $$ |$$  ____/ $$ |$$ |  $$ |\$$$$$$\
$$\   $$ |$$ |     $$  __$$ |$$ |  $$ |$$ |      $$ |$$ |  $$ | \____$$\
\$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |$$ |      $$ |\$$$$$$  |$$$$$$$  |
 \______/  \_______|\_______|\__|  \__|\__|      \__| \______/ \_______/

    """ + info_bas + """
    """
    ban = [ban1, ban2, ban3, ban4]
    #print_yellow_bold(random.choice(ban))
    print_yellow_bold(ban4)
