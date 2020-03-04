try
 {
     var consentpath = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System";
     var consentval = proton.registry.read(proton.registry.HKLM, consentpath, "ConsentPromptBehaviorAdmin", proton.registry.DWORD).uValue;
     if (consentval == 2)
     {
         var e = Error('Consent value is too high!');
         throw e;
     }

     var path = "Software\\Classes\\AppX82a6gwre4fdg3bt635tn5ctqjf8msdd2\\Shell\\open\\command";
     var delegate = proton.registry.read(proton.registry.HKCU, path, 'DelegateExecute', proton.registry.STRING).SValue;
     proton.registry.write(proton.registry.HKCU, path, 'DelegateExecute', '', proton.registry.STRING);
     proton.registry.write(proton.registry.HKCU, path, '', '~PAYLOAD_DATA~', proton.registry.STRING);

     proton.shell.run("C:\\Windows\\System32\\wsreset.exe", false);

     proton.work.report("Completed");

     proton.registry.write(proton.registry.HKCU, path, 'DelegateExecute', delegate, proton.registry.STRING);
     proton.registry.write(proton.registry.HKCU, path, '', '', proton.registry.STRING);
 }
 catch (e)
 {
     proton.work.error(e);
 }

 proton.exit();
