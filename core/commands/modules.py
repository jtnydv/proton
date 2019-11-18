DESCRIPTION = "Display all stagers and implants."

def autocomplete(shell, line, text, state):
    pass

def help(shell):
    shell.print_plain("")
    shell.print_plain('Use "modules -s" to print all available stagers.')
    shell.print_plain('Use "modules -i" to print all available implants.')
    shell.print_plain("")

def execute(shell, cmd):

    splitted = cmd.split()

    if len(splitted) > 1:
        flag = splitted[1]
        if flag == "-s":
            print("")
            print("         NAME         DESCRIPTION")                
            print("         -----        -------------")                
            print("         mshta	       Serves payloads using MSHTA.exe HTML Applications (default).")
            print("         regsvr	     Serves payloads using regsvr32.exe COM+ scriptlets.")
            print("         wmic 	       Serves payloads using WMIC XSL.")
            print("         rundll32_js	 Serves payloads using rundll32.exe.")
            print("         disk	       Serves payloads using files on disk.")
            print("         bitsadmin	   Transfers a .wsf payload containing JScript over a Bitsadmin job and executes it.")
            print("")
            import sys
            sys.exit(0)
                
        elif flag == "-i":
            return
    else:
        help(shell)
