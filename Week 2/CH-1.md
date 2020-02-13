# Chapter 1

## 1
```bash
kali:~/Desktop$ cd      # Reach root directory
kali:~$

kali:~$ ls              # Explore root directory
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos

kali:~$ cd Music        # Go to Music Folder
kali:~/Music$

kali:~/Music$ pwd       # Get Current directory
/home/kali/Music
```

## 2
```bash
kali:~$ whoami          # Show current username
kali
```

## 3
```bash
kali:~$ locate wordlist   # Find anything with "wordlist" name
/usr/bin/wordlists
/usr/sbin/remove-default-wordlist
/usr/sbin/select-default-wordlist
/usr/sbin/update-default-wordlist
/usr/share/wordlists
/usr/share/amass/wordlists
/usr/share/amass/wordlists/all.txt
            --- snip ---
/var/lib/dpkg/info/wordlists.list
/var/lib/dpkg/info/wordlists.md5sums
/var/lib/dpkg/info/wordlists.postinst
/var/lib/dpkg/info/wordlists.prerm
/var/lib/dpkg/triggers/update-default-wordlist
```

## 4
```bash
kali:~$ cat >> sample.txt    # if sample.txt is created, >> appends
Hi I am banana
^C

kali:~$ cat sample.txt       # Reads from previously created file
Hi I am banana
kali:~$
```

## 5
```bash
kali:~$ mkdir hackerdirectory                # Creating a folder
kali:~$ cd hackerdirectory                   # Go to Folder
kali:~/hackerdirectory$

kali:~/hackerdirectory$ touch hackedfile     # Create hackedfile
kali:~/hackerdirectory$ sudo cp hackedfile /root/secretfile     # Copy to root and rename
```
