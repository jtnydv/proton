DESCRIPTION = "Eval some python code."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    shell.print_plain("")
    shell.print_plain("Usage: pyexec <code>")
    shell.print_plain("")

def execute(shell, cmd):
    code = " ".join(cmd.split(" ")[1:])
    exec(code)
