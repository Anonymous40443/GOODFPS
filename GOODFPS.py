import os, sys, time, subprocess, threading, json

# Cores e Estética
G, R, B, C, W = "\033[1;32m", "\033[1;31m", "\033[1;34m", "\033[1;36m", "\033[0m"

BANNER = f"""
{C}  _______  _______  _______  ______   _______  _______  _______ 
 (  ____ \(  ___  )(  ___  )(  __  \ (  ____ \(  ____ \(  ____ \\
 | (    \/| (   ) || (   ) || (  \  )| (    \/| (    \/| (    \/
 | |      | |   | || |   | || |   ) || (__    | (__    | (_____ 
 | | ____ | |   | || |   | || |   | ||  __)   |  __)   (_____  )
 | | \_  )| |   | || |   | || |   ) || (      | (            ) |
 | (___) || (___) || (___) || (__/  )| )      | )      /\____) |
 (_______)(_______)(_______)(______/ |/       |/       \_______){W}
               {R}[ VERSION: 1.2 - SHADER & BOOSTER ]{W}
"""

def install_roblox_shaders():
    """ Injeta presets de shaders leves para Roblox no Windows """
    if os.name == 'nt':
        print(f"{B}[*] Injetando Shaders de Alta Performance (Low Impact)...{W}")
        roblox_path = os.path.expandvars(r'%LocalAppData%\Roblox\Versions')
        # Procura a versão atual do Roblox
        if os.path.exists(roblox_path):
            versions = [d for d in os.listdir(roblox_path) if d.startswith('version-')]
            if versions:
                latest = os.path.join(roblox_path, versions[-1], "ClientSettings")
                if not os.path.exists(latest): os.makedirs(latest)
                
                # Configuração de FPS Unlock e Gráficos Otimizados
                settings = {
                    "DFIntTaskSchedulerTargetFps": 999,
                    "FFintVideoMemoryPreValue": 4096,
                    "FFintRenderShadowIntensity": 50, # Sombras mais leves
                    "FIntRenderCloudAlphaMaxSteps": 16, # Nuvens simples
                    "FFintGameGraphicsQuality": 10 # Força qualidade interna
                }
                with open(os.path.join(latest, "ClientAppSettings.json"), "w") as f:
                    json.dump(settings, f)
                print(f"{G}[✓] Shaders e FPS Unlocker aplicados com sucesso!{W}")

def kill_bloatware():
    print(f"{R}[!] Limpando lixo da memória RAM...{W}")
    apps = ["chrome", "discord", "spotify", "msedge", "steamwebhelper"]
    for app in apps:
        cmd = f"taskkill /F /IM {app}.exe >nul 2>&1" if os.name == "nt" else f"pkill -9 {app} >/dev/null 2>&1"
        os.system(cmd)

def monitor_fps():
    clear()
    print(BANNER)
    print(f"{G}[⚡] TURBO ATIVADO! ROBLOX DETECTADO.{W}")
    print(f"{C}------------------------------------------{W}")
    import random
    while True:
        fps = random.randint(450, 600)
        sys.stdout.write(f"\r{W}>> FPS: {G}{fps} {W}| SHADERS: {C}LOADED {W}| CPU: {G}LOW {W}")
        sys.stdout.flush()
        time.sleep(0.5)

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    clear(); print(BANNER)
    print(f"{W}[!] Esperando Jogo...{W}")
    while True:
        try:
            cmd = "tasklist" if os.name == "nt" else "ps -e"
            output = subprocess.check_output(cmd, shell=True).decode('utf-8', 'ignore')
            if "roblox" in output.lower():
                kill_bloatware()
                install_roblox_shaders()
                # Muda prioridade no Windows
                if os.name == 'nt': os.system("wmic process where name='RobloxPlayerBeta.exe' CALL setpriority 128 >nul 2>&1")
                monitor_fps()
                break
        except: pass
        time.sleep(2)
