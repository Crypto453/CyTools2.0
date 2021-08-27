import os
import colorama
import time
import git
#lists
def lista_lista():
    lista_a = ["[1] Collection of information", "[2] Vulnerability analysis", "[3] Analysis of Web Applications", "[4] Database evaluation", "[5] Password attacks", "[6] Wireless Attacks", "[7] Exploitation tools", "[8] Sniffing & Spoofing", "[9] Forence Analysis", "[10] Exit"]
    for lista_a_lista in lista_a:
        print(chr(27)+"[1;33m"+lista_a_lista)
        time.sleep(0.1)
def collection_date_base():
    listv = ["Collection of information", "[1] nmap", "[2] dmitry", "[3] Dnsenum", "[4] p0f", "[5] Recon-ng", "[6] Maltego", "[7] EXIT "]
    for listv_a in listv:
        print(chr(27)+"[1;33m"+listv_a)
        time.sleep(0.1)
def analysis_data_base():
    list_ab = ["Vulnerability analysis", "[1] Legion", "[2] nikto", "[3] lynis", "[4] nmap scanner", "[5] EXIT"]
    for list_print in list_ab:
        print(list_print)
        time.sleep(0.1)        
def web_data_base():
    carga_carga = ["Analysis of Web Applications", "[1] sqlmap", "[2] Burpsuite", "[3] commix", "[4] paros", "[5] EXIT"]
    for carga_wait in carga_carga:
        print(carga_wait)
        time.sleep(0.1)     
def principal_data_base():
    data_base_prime = ["Database evaluation", "[1] Oscanner", "[2] Sqldict", "[3] sqlninja ", "[4] sqlmap", "[5] EXIT"]
    for data_base_one in data_base_prime:
        print(data_base_one)
        time.sleep(0.1)   
def passw_passw():
    passw_data_base = ["Password attacks", "[1] Cewl", "[2] Crunch", "[3] Hashcat", "[4] Hydra", "[5] Medusa", "[6] John", "[7] EXIT"]
    for passw_a in passw_data_base:
        print(passw_a)
        time.sleep(0.1)
def wireless_wireless():
    lista_wireless = ["Wireless Attacks", "[1] Aircrack-ng", "[2] Kismet", "[3] reaver", "[4] Wifite", "[5] Chirp", "[6] EXIT"]
    for lista_wireless_lista in lista_wireless:
        print(lista_wireless_lista)
        time.sleep(0.1)    
def explotation_explotation():
    ex_lista = ["Explotation Tools", "[1] Armitage", "[2] Metasploit Framework", "[3] SET", "[4] Termineter", "[5] EXIT "]
    for lista_ex in ex_lista:
        print(lista_ex)
        time.sleep(0.1)  
def sniff_sniff():
    sniff_lista = ["Sniffing & Spoofing", "[1] Bettercap", "[2] Wireshark", "[3] MaCchanger", "[4] hamster", "[5] EXIT"]
    for sniff_a in sniff_lista:
        print(sniff_a)
        time.sleep(0.1)
def forence_forence():
    forence_lista = ["Forence Analysis", "[1] Autopsy", "[2] binwalk", "[3] hashdeep", "[4] galleta", "[5] bulk_extractor", "[6] EXIT"]
    for forence_print in forence_lista:
        print(forence_print)
        time.sleep(0.1)
def small_lista_small():
    list_small = ["[1]Debian(ubuntu, etc)", "[2]Termux"]
    for list_big in list_small:
        print(list_big)
        time.sleep(0.3)        
#def times and prints
def time_funtion():
    time.sleep(0.3)
def time_funtion():
    time.sleep(4)
def time_funtion():
    time.sleep(0.3)
    os.system("clear")
def banner_banner_funtion():
    os.system("python3 banner_banner.py")
def clear_windows_clear():
    os.system("clear")
def welcome_welcome_date():
    print("\033[;36m"+"Welcome to CyTools\nThe author of this script is not responsible for the use of the tools")
def error_funtion_error():
    while True:
        print("ERROR Try Again--ERROR Try Again--ERROR Try Again")    
def what_funtion_what():
    print("What distribution or emulator do you use?")
def good_bye_funtion_end():
    bye_list = ["Closing the program...", "Closing the program.....", "Closing the program.......", "Closing the program........", "Closing the program............", "Closing the program..............."]
    for bye_bye in bye_list:
        print(bye_bye)
        time.sleep(0.4)
        os.system("clear")
#def the git and os, number one
def operative_system_funtion_a():
    os.system("sudo apt install nmap > nul") 
    os.system("python3 CyTools.py")
def operative_system_funtion_b():
    os.system("sudo apt install dmitry > nul") 
    os.system("python3 CyTools.py")
def operative_system_funtion_c():
    os.system("sudo apt install dnsenum > nul")
    os.system("python3 CyTools.py")
def operative_system_funtion_d():
    path_a = input("Write the path: ")
    git.Git(f"{path_a}").clone("https://github.com/p0f/p0f")
    os.system("python3 CyTools.py")
def operative_system_funtion_e():
    os.system("sudo apt install recon-ng")
    os.system("python3 CyTools.py")
def operative_system_funtion_f():
    path_b = input("Write the path: ")
    git.Git(f"{path_b}").clone("https://github.com/paterva/maltego-trx")

def analysis_system_funtion_a():
    path_c = input("Write the path: ")
    git.Git(f"{path_c}").clone("https://github.com/StanfordLegion/legion")    
    os.system("python3 CyTools.py")
def analysis_system_funtion_b():
    path_d = input("Write the path: ")
    git.Git(f"{path_d}").clone("https://github.com/topics/nikto")
    os.system("python3 CyTools.py")
def analysis_system_funtion_c():
    path_e = input("Write the path: ")
    git.Git(f"{path_e}").clone("https://github.com/CISOfy/Lynis")
def analysis_system_funtion_d():
    path_f = input("Write the path: ")
    os.system("sudo apt install nmap > nul")
    os.system("python3 CyTools.py")

def web_system_funtion_a():
    path_path_a = input("write the path: ")
    git.Git(f"{path_path_a}").clone("https://github.com/sqlmapproject/sqlmap")
    os.system("python3 CyTools.py")
def web_system_funtion_b():
    path_path_b = input("Write the path: ")
    git.Git(f"{path_path_b}").clone("https://github.com/thehackingsage/burpsuite")
    os.system("python3 CyTools.py")
def web_system_funtion_c():
    path_path_c = input("write the path: ")
    git.Git(f"{path_path_c}").clone("https://github.com/commixproject/commix")
    os.system("python3 CyTools.py")
def web_system_funtion_d():
    path_path_c = input("write the path: ")
    git.Git(f"{path_path_c}").clone("https://github.com/trol73/paros")
    os.system("python3 CyTools.py")

def database_web_funtion_a():
    time_funtion()
    print("https://gitlab.com/kalilinux/packages/oscanner/")
    os.system("python3 CyTools.py")
def database_web_funtion_b():
    path_path_d = input("write the path: ")
    git.Git(f"{path_path_d}").clone("https://github.com/skylergrammer/sqldict")
    os.system("python3 CyTools.py")
def database_web_funtion_c():
    path_path_e = input("write the path: ") 
    git.Git(f"{path_path_e}").clone("https://github.com/xxgrunge/sqlninja")
    os.system("python3 CyTools.py")

def passw_system_funtion_a():
    path_system = input("write the path: ")
    git.Git(f"{path_system}").clone("https://github.com/digininja/cewl")
    os.system("python3 CyTools.py")
def passw_system_funtion_b():
    os.system("sudo apt install crunch > nul")
    os.system("python3 CyTools.py")
def passw_system_funtion_c():
    path_system_a = input("write the path: ")    
    git.Git(f"{path_system_a}").clone("https://github.com/hashcat/hashcat")
    os.system("python3 CyTools.py")
def passw_system_funtion_d():
    os.system("sudo apt install hydra > nul")
    os.system("python3 CyTools.py")
def passw_system_funtion_e():
    os.system("sudo apt install medusa")    
    os.system("python3 CyTools.py")
def passw_system_funtion_f():
    path_system_b = input("write the path: ")
    git.Git(f"{path_system_b}").clone("https://github.com/openwall/john")
    os.system("python3 CyTools.py")

def wireless_system_funtion_a():
    os.system("sudo apt install aircrack-ng > nul")
    os.system("python3 CyTools.py")
def wireless_system_funtion_b():
    path_path_system_a = input("write the path: ")
    git.Git(f"{path_path_system_a}").clone("https://github.com/kismetwireless/kismet")
    os.system("python3 CyTools.py")
def wireless_system_funtion_c():
    path_path_system_b = input("write the path: ")
    git.Git(f"{path_path_system_b}").clone("https://github.com/t6x/reaver-wps-fork-t6x")
    os.system("python3 CyTools.py")
def wireless_system_funtion_d():
    path_path_system_c = input("write the path: ")
    git.Git(f"{path_path_system_c}").clone("https://github.com/derv82/wifite")
    os.system("python3 CyTools.py")
def wireless_system_funtion_e():
    path_path_system_d = input("write the path: ")
    git.Git(f"{wireless_system_funtion_e}").clone("https://shinmera.github.io/chirp/")
    os.system("python3 CyTools.py") 

def explotation_system_funtion_a():
    path_ex_a = input("write the path: ")
    git.Git(f"{path_ex}").clone("https://github.com/rsmudge/armitage")
    os.system("python3 CyTools.py")
def explotation_system_funtion_b():
    path_ex_b = input("write the path: ")
    git.Git(f"{path_ex_b}").clone("https://github.com/rapid7/metasploit-framework")
    os.system("python3 CyTools.py")
def explotation_system_funtion_c():
    path_ex_c = input("write the path: ")
    git.Git(f"{path_ex_c}").clone("https://github.com/trustedsec/social-engineer-toolkit")
    os.system("python3 CyTools.py")
def explotation_system_funtion_d():
    path_ex_d = input("write the path: ")
    git.Git(f"{path_ex_d}").clone("https://github.com/rsmusllp/termineter")
    os.system("python3 CyTools.py")
def sniff_system_funtion_a():
    path_sniff_a = input("write the path: ")
    git.Git(f"{path_sniff_a}").clone("https://github.com/bettercap/bettercap")
    os.system("python3 CyTools.py")
def sniff_system_funtion_b():
    os.system("sudo apt install wireshark > nul")
    os.system("python3 CyTools.py")
def sniff_system_funtion_c():
    os.system("sudo apt install macchanger > nul")
    os.system("python3 CyTools.py")
def sniff_system_funtion_d():
    path_sniff_b = input("write the path: ")
    git.Git(f"{path_sniff_b}").clone("https://github.com/projecthamster/hamster")

def forence_system_funtion_a():
    path_forence_a = input("write the path")
    git.Git(f"{path_forence_a}").clone("https://github.com/sleuthkit/autopsy")
    os.system("python3 CyTools.py")
def forence_system_funtion_b():
    path_forence_b = input("write the path: ")
    git.Git(f"{path_forence_b}").clone("https://github.com/ReFirmLabs/binwalk")
    os.system("python3 CyTools.py")
def forence_system_funtion_c():
    path_forence_c = input("write the path: ")
    git.Git(f"{path_forence_c}").clone("https://github.com/jessek/hashdeep")
    os.system("python3 CyTools.py")
def forence_system_funtion_d():
    print("https://tools.kali.org/forensics/galleta\nTe recomiento ir a la pagina de la herramienta") 
def forece_system_funtion_e():
    path_forence_d = input("write the path: ") 
    git.Git(f"{path_forence_d}").clone("https://github.com/4n6ist/bulk_extractor-rec")
    os.system("python3 CyTools.py")

#development
clear_windows_clear()
banner_banner_funtion()
welcome_welcome_date()
what_funtion_what()
small_lista_small()
user_date_big = int(input("===> "))
if user_date_big == 1:
    clear_windows_clear()
    banner_banner_funtion()
    welcome_welcome_date()
    lista_lista()
    user_date_user = int(input("===> "))
    if user_date_user == 1:
        clear_windows_clear()
        banner_banner_funtion()
        collection_date_base()
        user_date_a = int(input("===> "))
        if user_date_a == 1:
            operative_system_funtion_a()
        elif user_date_a == 2:
            operative_system_funtion_b()
        elif user_date_a == 3:
            operative_system_funtion_c()
        elif user_date_a == 4:
            operative_system_funtion_d()
        elif user_date_a == 5:
            operative_system_funtion_e()
        elif user_date_a == 6:
            operative_system_funtion_f()
        elif user_date_a == 7:
            good_bye_funtion_end()
        else:
            error_funtion_error()
    elif user_date_user == 2:
        clear_windows_clear()
        banner_banner_funtion()
        analysis_data_base()
        user_date_b = int(input("===> "))
        if user_date_b == 1:
            analysis_system_funtion_a()
        elif user_date_b == 2:
            analysis_system_funtion_b()
        elif user_date_b == 3:
            analysis_system_funtion_c()
        elif user_date_b == 4:
            analysis_system_funtion_d()
        elif user_date_b == 5:
            good_bye_funtion_end()
        else:
            error_funtion_error()
    elif user_date_user == 3:
        clear_windows_clear()
        banner_banner_funtion()
        web_data_base()
        user_date_c = int(input("===> "))
        if user_date_c == 1:
            web_system_funtion_a()
        elif user_date_c == 2:
            web_system_funtion_b()
        elif user_date_c == 3:
            web_system_funtion_c()
        elif user_date_c == 4:
            web_system_funtion_d()
        elif user_date_c == 5:
            good_bye_funtion_end()
        else:
            error_funtion_error()
    elif user_date_user == 4:
        clear_windows_clear()
        banner_banner_funtion()
        principal_data_base()
        user_date_d = int(input("===> "))
        if user_date_d == 1:
            database_web_funtion_a()
        elif user_date_d == 2:
            database_web_funtion_b()
        elif user_date_d == 3:
            database_web_funtion_c()
        elif user_date_d == 4:
            web_system_funtion_a()
        elif user_date_d == 5:
            good_bye_funtion_end()
        else:
            error_funtion_error()        
    elif user_date_user == 5:
        clear_windows_clear()
        banner_banner_funtion()
        passw_passw()
        user_date_e = int(input("===> "))
        if user_date_e == 1:
            passw_system_funtion_a()
        elif user_date_e == 2:
            passw_system_funtion_b()
        elif user_date_e == 3:
            passw_system_funtion_c()
        elif user_date_e == 4:
            passw_system_funtion_d()
        elif user_date_e == 5:
            passw_system_funtion_e()
        elif user_date_e == 6:
            passw_system_funtion_f()
        elif user_date_e == 7:
            good_bye_funtion_end()
        else:
            error_funtion_error()
    elif user_date_user == 6:
        clear_windows_clear()
        banner_banner_funtion_a()
        wireless_wireless()
        user_date_f = int(input("===> "))
        if user_date_f == 1:
            wireless_system_funtion_a()
        elif user_date_f == 2:
            wireless_system_funtion_b()
        elif user_date_f == 3:
            wireless_system_funtion_c()
        elif user_date_f == 4:
            wireless_system_funtion_d()
        elif user_date_f == 5:
            wireless_system_funtion_e()
        elif user_date_f == 6:
            good_bye_funtion_end()
        else:
            error_funtion_error()
    elif user_date_user == 7:
        clear_windows_clear()
        banner_banner_funtion()
        explotation_explotation()
        user_date_g = int(input("===> "))
        if user_date_g == 1:
            explotation_system_funtion_a()
        elif user_date_g == 2:
            explotation_system_funtion_b()
        elif user_date_g == 3:
            explotation_system_funtion_c()
        elif user_date_g == 4:
            explotation_system_funtion_d()  
        elif user_date_g == 5:
            good_bye_funtion_end()
        else:
            error_funtion_error()
    elif user_date_user == 8:
        clear_windows_clear()
        banner_banner_funtion()
        sniff_sniff()
        user_date_h = int(input("===> "))
        if user_date_h == 1:
            sniff_system_funtion_a()
        elif user_date_h == 2:
            sniff_system_funtion_b()
        elif user_date_h == 3:
            sniif_system_funtion_c()
        elif user_date_h == 4:
            sniff_system_funtion_d()
        elif user_date_h == 5:
            good_bye_funtion_end()
        else:
            error_funtion_error()
    elif user_date_user == 9:
        clear_windows_clear()
        banner_banner_funtion()
        forence_forence()
        user_date_i = int(input("===> "))
        if user_date_i == 1:
            forence_system_funtion_a()
        elif user_date_i == 2:
            forence_system_funtion_b()
        elif user_date_i == 3:
            forence_system_funtion_c()
        elif user_date_i == 4:
            forence_system_funtion_d()
        elif user_date_i == 5:
            forence_system_funtion_e()
        elif user_date_i == 6:
            good_bye_funtion_end()
        else:
            error_funtion_error()
    elif user_date_user == 10:
        clear_windows_clear()
        banner_banner_funtion()
        good_bye_funtion_end()
elif user_date_big == 2:
    os.system("python3 termux_termux")
else:
    error_funtion_error()



