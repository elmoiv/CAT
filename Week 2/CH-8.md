# Chapter 8

## 1
```bash
kali:~$ cat > HelloHackersArise.sh
echo "Hell yeah :)"

kali:~$ chmod 755 HelloHackersArise.sh
kali:~$ ./HelloHackersArise.sh
Hell yeah :)
```
## 2
```bash
kali:~$ cat > MSSQLscanner.sh
#! /bin/bash

# Find Microsoft SQL open 1433 port

nmap -sT 192.168.1.0/24 -p 1433 >/dev/null -oG Result
cat Result | grep open > ResultOpen
cat ResultOpen

kali:~$ chmod 755 MSSQLscanner.sh
kali:~$ ./MSSQLscanner.sh
```
## 3
```bash
kali:~$ cat > MSSQLscanner.sh
#! /bin/bash

# Find Microsoft SQL open 1433 port
echo 'Enter starting IP: '
read ip1
echo 'Enter ending IP:'
read ip2
echo 'Enter port to scan: '
read port

nmap -sT $ip1-$ip2 -p $port >/dev/null -oG Result

cat Result | grep close > ResultOpen
cat ResultOpen

kali:~$ chmod 755 MSSQLscanner.sh
kali:~$ ./MSSQLscanner.sh
```
