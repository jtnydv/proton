if -d ~/proton; then
  sleep 0
else
  cd ~
  {
  git clone https://github.com/entynetproject/proton.git
  } &> /dev/null
  cd ~/proton
  chmod +x install.sh
  ./install.sh
fi

{
cd ~/proton/script/bin
cp pscript /usr/local/bin
chmod +x /usr/local/bin/pscript
cp pscript /bin
chmod +x /bin/proton
cp pscript /data/data/com.termux/files/usr/bin
chmod +x /data/data/com.termux/files/usr/bin/pscript
} &> /dev/null
  
