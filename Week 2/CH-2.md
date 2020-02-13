# Chapter 2

## 1
```bash
kali:~$ cd /usr/share/wordlists/metasploit
kali:~/usr/share/wordlists/metasploit$
```
## 2
```bash
kali:~/usr/share/wordlists/metasploit$ cat password.lst
!@$%
!@$%^
!@$%^&
!@$%^&*
!boerbul
!boerseun
!gatvol
!hotnot
            --- snip ---
zzz
z�rich
�gar
�ngstr�m
�clair
�clairs
�clat
�lan
�migr�
�migr�s
�p�e
�tude
vagrant
```
## 3
```bash
kali:~/usr/share/wordlists/metasploit$ more password.lst
!@$%
!@$%^
!@$%^&
!@$%^&*
!boerbul
!boerseun
!gatvol
!hotnot
!kak
!koedoe
!likable
!poes
!pomp
!soutpiel
.net
0
000000
00000000
0007
007
007007
0s
0th
# Pressed Q to exit
```
## 4
```bash
kali:~/usr/share/wordlists/metasploit$ less password.lst
!@$%
!@$%^
!@$%^&
!@$%^&*
!boerbul
!boerseun
!gatvol
!hotnot
!kak
!koedoe
!likable
!poes
!pomp
!soutpiel
.net
0
000000
00000000
0007
007
007007
0s
0th
# Pressed Q to exit
```
## 5
```bash
kali:~/usr/share/wordlists/metasploit$ nl password.lst
 1       !@$%
 2       !@$%^
 3       !@$%^&
 4       !@$%^&*
 5       !boerbul
            --- snip ---
 88392   �lan
 88393   �migr�
 88394   �migr�s
 88395   �p�e
 88396   �tude
 88397   vagrant
```
## 6
```bash
kali:~/usr/share/wordlists/metasploit$ tail password.lst
�ngstr�m
�clair
�clairs
�clat
�lan
�migr�
�migr�s
�p�e
�tude
vagrant
```
## 7
```bash
kali:~/usr/share/wordlists/metasploit$ cat password.lst | grep 123
123
123123
123321
1234
12345
123456
1234567
12345678
123456789
1234567890
1234qwer
123abc
123go
123qwe
a12345
abc123
abcd123
abcd1234
aki123
asdf1234
chris123
happy123
hello123
help123
jkl123
red123
test123
xxx123
xyz123
zxc123
```
