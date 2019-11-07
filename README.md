# Proton Framework (Windows Post Exploitation Framework)

<h4 align="center"><img src="https://user-images.githubusercontent.com/54115104/68429726-b4af7380-01bf-11ea-96d2-8e19b3945380.png"> 
<h4 align="center"><img src="https://user-images.githubusercontent.com/54115104/68430856-f3462d80-01c1-11ea-8dbf-3d5fdf45af33.jpeg"> 


<p align="center">
  <a href="http://entynetproject.simplesite.com/">
    <img src="https://img.shields.io/badge/entynetproject-Ivan%20Nikolsky-blue.svg">
  </a> 
  <a href="https://github.com/entynetproject/proton/releases">
    <img src="https://img.shields.io/github/release/entynetproject/proton.svg">
  </a>
  <a href="https://wikipedia.org/wiki/Python_(programming_language)">
    <img src="https://img.shields.io/badge/language-python-blue.svg">
 </a>
  <a href="https://github.com/entynetproject/proton">
    <img src="https://img.shields.io/badge/implants-44-red.svg">
 </a>
  <a href="https://github.com/entynetproject/proton/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues/entynetproject/proton.svg">
  </a>
  <a href="https://github.com/entynetproject/proton/wiki">
      <img src="https://img.shields.io/badge/wiki%20-proton-lightgrey.svg">
 </a>
  <a href="https://twitter.com/entynetproject">
    <img src="https://img.shields.io/badge/twitter-entynetproject-blue.svg">
 </a>
</p>

***

# About proton framework

    INFO: Proton Framework is a Windows post exploitation framework similar to other penetration 
    testing tools such as Meterpreter and Powershell Invader Framework. The major difference is that 
    the Proton Framework does most of its operations using Windows Script Host (a.k.a. JScript/VBScript), 
    with compatibility in the core to support a default installation of Windows 2000 with no service 
    packs (and potentially even versions of NT4) all the way through Windows 10.
   
***

# Getting started

## Proton installation

> cd proton

> chmod +x install.sh

> ./install.sh

## Proton uninstallation

> cd proton

> chmod +x uninstall.sh

> ./uninstall.sh

***

# How to execute proton

> proton -h

    usage: proton [-h] [--autorun AUTORUN] [--restore RESTORE] [-u]
                    
    optional arguments:
      -h, --help         show this help message and exit
      --autorun AUTORUN  A file containing Proton commands.
      --restore RESTORE  A Proton restore json file.
      -u, --update       Update Proton Framework.
      
***

# Proton framework modules

    INFO: There are to kinds of Proton Framework 
    modules - stagers and implants. Proton stagers hook 
    target zombies and allow you to use implants. Proton 
    implants starts jobs on remote target zombie.
    
## Proton stagers

    INFO: Proton stagers hook target 
    zombie and allow you to use implants.

Module | Description
--------|------------
stager/js/mshta | Serves payloads using MSHTA.exe HTML Applications (default).
stager/js/regsvr | Serves payloads using regsvr32.exe COM+ scriptlets.
stager/js/wmic | Serves payloads using WMIC XSL.
stager/js/rundll32_js | Serves payloads using rundll32.exe.
stager/js/disk | Serves payloads using files on disk.
stager/js/bitsadmin | Transfers a .wsf payload containing JScript over a Bitsadmin job and executes it.

## Proton implants

    INFO: Proton implants starts 
    jobs on a remote zombie target.

Module | Description
--------|------------
implant/elevate/bypassuac_compdefaults | Bypass UAC via registry hijack for ComputerDefaults.exe.
implant/elevate/bypassuac_compmgmtlauncher | Bypass UAC via registry hijack for CompMgmtLauncher.exe.
implant/elevate/bypassuac_eventvwr | Uses enigma0x3's eventvwr.exe exploit to bypass UAC on Windows 7, 8, and 10.
implant/elevate/bypassuac_fodhelper | Bypass UAC via registry hijack for fodhelper.exe.
implant/elevate/bypassuac_sdclt | Uses enigma0x3's sdclt.exe exploit to bypass UAC on Windows 10.
implant/elevate/bypassuac_slui | Bypass UAC via registry hijack for slui.exe.
implant/elevate/system_createservice | Elevate from administrative session to SYSTEM via SC.exe.
implant/fun/youtube | Maxes volume and opens the specified YouTube video in a hidden window.
implant/fun/voice | Plays a message over text-to-speech.
implant/gather/clipboard | Retrieves the current content of the user clipboard.
implant/gather/comsvcs_lsass | Utilizes comsvcs.dll to create a MiniDump of LSASS, parses with pypykatz.
implant/gather/enum_domain_info | Retrieve information about the Windows domain.
implant/gather/hashdump_dc | Domain controller hashes from the NTDS.dit file.
implant/gather/hashdump_sam | Retrieves hashed passwords from the SAM hive.
implant/gather/loot_finder | Finds loot on the target box.
implant/gather/user_hunter | Locate users logged on to domain computers (using Dynamic Wrapper X).
implant/inject/mimikatz_dotnet2js | Injects a reflective-loaded DLL to run powerkatz.dll.
implant/inject/mimikatz_dynwrapx | Injects a reflective-loaded DLL to run powerkatz.dll (using Dynamic Wrapper X).
implant/inject/mimikatz_tashlib | Executes arbitrary shellcode using the TashLib COM object. (Work in Progress!)
implant/inject/shellcode_dotnet2js | Executes arbitrary shellcode using the DotNet2JS technique. Inject shellcode into a host process via createremotethread as a new thread (thanks psmitty7373!).
implant/inject/shellcode_dynwrapx | Executes arbitrary shellcode using the Dynamic Wrapper X COM object.
implant/inject/shellcode_excel | Runs arbitrary shellcode payload (if Excel is installed).
implant/manage/enable_rdesktop | Enables remote desktop on the target.
implant/manage/exec_cmd | Run an arbitrary command on the target, and optionally receive the output.
implant/persist/add_user | Adds a either a local or domain user.
implant/persist/registry | Adds a Proton stager payload in the registry.
implant/persist/schtasks | Establishes persistence via a scheduled task.
implant/persist/wmi | Creates persistence using a WMI subscription.
implant/phishing/password_box | Prompt a user to enter their password.
implant/pivot/exec_psexec | Run a command on another machine using psexec from sysinternals.
implant/pivot/exec_wmi | Executes a command on another system.
implant/pivot/stage_wmi | Hook a zombie on another machine using WMI.
implant/scan/tcp | Uses HTTP to scan open TCP ports on the target zombie LAN.
implant/utils/download_file | Downloads a file from the target zombie.
implant/utils/multi_module | Run a number of implants in succession.
implant/utils/upload_file | Uploads a file from the listening server to the target zombies.

***

# TLS Communications

    INFO: To enable TLS communications, you will need 
    to host your Proton stager on a valid domain 
    (i.e. malicious.com) with a known Root CA signed 
    certificate. Windows will check its certificate 
    store and will NOT allow a self-signed certificate.
    
***
    
# Disclaimer

Usage of Proton for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, federal, and international laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.
    
***

# Proton apache license

    Copyright (C) 2016 - 2018 Entynetproject

    Licensed under the Apache License, Version 2.0 (the "License"); you may not
    use the software except in compliance with the License.

    You may obtain a copy of the License at:

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
    License for the specific language governing permissions and limitations under
    the License.

    Disclaimer:
    Usage of Proton for attacking targets without prior mutual consent is illegal.
    It is the end user's responsibility to obey all applicable local, state,
    federal, and international laws. Developers assume no liability and are not
    responsible for any misuse or damage caused by this program.
    
***

# Thats all!
