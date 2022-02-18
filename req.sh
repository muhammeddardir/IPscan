#!/bin/sh 

#install script languages 

sudo apt-get install golang;
sudo apt-get install python3;
sudo apt-get install python3-pip;
sudo apt-get install python-pip; 
sudo apt-get install git;
pip install subprocess; 
pip install termcolor; 


mkdir Tools
cd Tools

#metabigor
go install github.com/j3ssie/metabigor@latest

#mapcidr
go install  github.com/projectdiscovery/mapcidr/cmd/mapcidr@latest


#nrich
wget https://gitlab.com/api/v4/projects/33695681/packages/generic/nrich/latest/nrich_latest_amd64.deb
chmod +x nrich_latest_amd64.deb
sudo dpkg -i nrich_latest_amd64.deb

#httpx
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest