DESCRIPTION = "Ignore ProtonScript program exit."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    pass

def execute(shell, cmd):
    REDL="\033[1;31m"
    WHSL="\033[0;97m"
    ENDL="\033[0m"
    print(REDL+"[-]"+ENDL+" "+WHSL+"You can only run this through ProtonScript!"+ENDL)
