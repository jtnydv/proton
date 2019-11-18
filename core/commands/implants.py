DESCRIPTION = "Display info about implants."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    shell.print_plain("")
    shell.print_plain('Use "implants -l" to print all available implants.')
    shell.print_plain("")

def execute(shell, cmd):
bypassuac_compdefaults	Bypass UAC via registry hijack for ComputerDefaults.exe.
bypassuac_compmgmtlauncher	Bypass UAC via registry hijack for CompMgmtLauncher.exe.
bypassuac_eventvwr	Uses enigma0x3's eventvwr.exe exploit to bypass UAC on Windows 7, 8, and 10.
bypassuac_fodhelper	Bypass UAC via registry hijack for fodhelper.exe.
bypassuac_sdclt	Uses enigma0x3's sdclt.exe exploit to bypass UAC on Windows 10.
bypassuac_slui	Bypass UAC via registry hijack for slui.exe.
system_createservice	Elevate from administrative session to SYSTEM via SC.exe.
youtube	Maxes volume and opens the specified YouTube video in a hidden window.
voice	Plays a message over text-to-speech.
clipboard	Retrieves the current content of the user clipboard.
comsvcs_lsass	Utilizes comsvcs.dll to create a MiniDump of LSASS, parses with pypykatz.
enum_domain_info	Retrieve information about the Windows domain.
hashdump_dc	Domain controller hashes from the NTDS.dit file.
hashdump_sam	Retrieves hashed passwords from the SAM hive.
loot_finder	Finds loot on the target box.
user_hunter	Locate users logged on to domain computers (using Dynamic Wrapper X).
mimikatz_dotnet2js	Injects a reflective-loaded DLL to run powerkatz.dll.
mimikatz_dynwrapx	Injects a reflective-loaded DLL to run powerkatz.dll (using Dynamic Wrapper X).
implant/inject/mimikatz_tashlib	Executes arbitrary shellcode using the TashLib COM object. (Work in Progress!)
shellcode_dotnet2js	Executes arbitrary shellcode using the DotNet2JS technique. Inject shellcode into a host process via createremotethread as a new thread (thanks psmitty7373!).
shellcode_dynwrapx	Executes arbitrary shellcode using the Dynamic Wrapper X COM object.
shellcode_excel	Runs arbitrary shellcode payload (if Excel is installed).
enable_rdesktop	Enables remote desktop on the target.
exec_cmd	Run an arbitrary command on the target, and optionally receive the output.
add_user	Adds a either a local or domain user.
registry	Adds a Proton stager payload in the registry.
schtasks	Establishes persistence via a scheduled task.
wmi	Creates persistence using a WMI subscription.
password_box	Prompt a user to enter their password.
exec_psexec	Run a command on another machine using psexec from sysinternals.
exec_wmi	Executes a command on another system.
stage_wmi	Hook a zombie on another machine using WMI.
tcp	Uses HTTP to scan open TCP ports on the target zombie LAN.
download_file	Downloads a file from the target zombie.
multi_module	Run a number of implants in succession.
upload_file
