DESCRIPTION = "Ignore ProtonScript program exit."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    pass

def execute(shell, cmd):
    import os.path
        if (os.path.exists("/data/data/com.termux")):
            pspath = "/data/data/com.termux/files/usr/bin/pscript"
        else:
            pspath = "/usr/local/bin/pscript"
            
        if (os.path.exists(pspath)):
            import time
            time.sleep(0)
        else:
            REDL="\033[1;31m"
            WHSL="\033[0;97m"
            ENDL="\033[0m"
            print(REDL+"[-]"+ENDL+" "+WHSL+"ProtonScript is not installed!"+ENDL)
            ips = input('Install ProtonScript y/N: ')
            if ips == "y" or ips == "Y":
                os.system("cd script && chmod +x install.sh && ./install.sh")
                import sys
                sys.exit()
            else:
                import sys
                sys.exit()
