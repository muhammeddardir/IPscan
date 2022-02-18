#!/bin/sh 

#install script languages 

tput setaf 1; echo "install Programming langs and libraries"
sleep 1;
sudo apt-get install golang;
sudo apt-get install python3;
sudo apt-get install pipx;
sudo apt-get install pip; 
sudo apt-get install git;
sudo pip install subprocess; 
sudo pip install termcolor; 

tput setaf 1; echo "Create Directory Tools"
sleep 1;
mkdir Tools
cd Tools

tput setaf 1; echo "install metabigor"
sleep 1;
#metabigor
go install github.com/j3ssie/metabigor@latest

tput setaf 1; echo "install mapcidr"
sleep 1;
#mapcidr
go install  github.com/projectdiscovery/mapcidr/cmd/mapcidr@latest

tput setaf 1; echo "install nrich"
sleep 1;
#nrich
wget https://gitlab.com/api/v4/projects/33695681/packages/generic/nrich/latest/nrich_latest_amd64.deb
chmod +x nrich_latest_amd64.deb
sudo dpkg -i nrich_latest_amd64.deb

tput setaf 1; echo "install httpx"
sleep 1;
#httpx
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
