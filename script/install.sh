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
} &> /dev/null
  
