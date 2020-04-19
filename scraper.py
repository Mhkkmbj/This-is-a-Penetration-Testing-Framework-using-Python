#grab banners from godaddy

nmap -sV --version-intensity 5 godaddy.com -p 80

#grab urls from page

python3 ./Photon/photon.py -u https://en.wikipedia.org/wiki/List_of_computer_security_certifications --dns

