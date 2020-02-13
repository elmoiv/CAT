# Chapter 7

## 1
```bash
kali:~$ set | more

BASH=/bin/bash
BASHOPTS=checkwinsize:cmdhist:complete_fullquote:expand_aliases:extquote:force_fignore:globasciiranges:hostcomplete:inte
ractive_comments:login_shell:progcomp:promptvars:sourcepath
BASH_ALIASES=()
BASH_ARGC=([0]="0")
BASH_ARGV=()
BASH_CMDS=()
BASH_LINENO=()
BASH_SOURCE=()
BASH_VERSINFO=([0]="5" [1]="0" [2]="11" [3]="1" [4]="release" [5]="x86_64-pc-linux-gnu")
BASH_VERSION='5.0.11(1)-release'
COLUMNS=120
DIRSTACK=()
EUID=0
GROUPS=()
HISTFILE=/root/.bash_history
HISTFILESIZE=500
HISTSIZE=1000
HOME=/root
HOSTNAME=PIKACHU
HOSTTYPE=x86_64
IFS=$' \t\n'
IS_WSL='Linux version 4.4.0-18362-Microsoft (Microsoft@Microsoft.com) (gcc version 5.4.0 (GCC) ) #476-Microsoft Fri Nov
01 16:53:00 PST 2019'
LANG=en_US.UTF-8
LINES=30
LOGNAME=root
LS_COLORS='rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg
=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01
--More--
```
## 2
```bash
kali:/$ echo $HOSTNAME
PIKACHU
```
## 3
```bash
kali:/$ sed 's|\\|/|g'
```
## 4
```bash
kali:~$ MYVAR='Khaled'
```
## 5
```bash
kali:~$ echo $MYVAR
Khaled
```
## 6
```bash
kali:~$ export MYVAR
```
## 7
```bash
kali:~$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```
## 8
```bash
kali:~$ PATH=$PATH:/home
```

## 9
```bash
kali:~$ PS1='World’s Greatest Hacker:'
```
