DESCRIPTION = "String some text."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    shell.print_plain("")
    shell.print_plain('Use "string %s" to string some text.' % (shell.colors.colorize("TEXT", shell.colors.BOLD)))
    shell.print_plain("")

def execute(shell, cmd):
    splitted = cmd.split()
    
    if len(splitted) > 1:
        print(string)
    else:
help(shell)
