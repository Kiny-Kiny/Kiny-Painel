#!/bin/bash
rm -rf *.py
git clone https://github.com/Kiny-Kiny/Kiny-Painel.git
mv ./Kiny-painel/* ./
rm -rf Kiny-painel 
chmod +x *
