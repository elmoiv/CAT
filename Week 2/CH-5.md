# Chapter 5

## 1
```bash
kali:~$ cd /
kali:/$ ls -l
total 580
lrwxrwxrwx  1 root root      7 Nov 28 01:31 bin -> usr/bin
drwxr-xr-x  1 root root   4096 Nov 19 11:18 boot
drwxr-xr-x  1 root root   4096 Feb 13 20:19 dev
drwxr-xr-x  1 root root   4096 Feb 13 20:47 etc
drwxr-xr-x  1 root root   4096 Feb 13 20:19 home
-rwxr-xr-x  1 root root 591344 Jan  1  1970 init
lrwxrwxrwx  1 root root      7 Nov 28 01:31 lib -> usr/lib
lrwxrwxrwx  1 root root      9 Nov 28 01:31 lib32 -> usr/lib32
lrwxrwxrwx  1 root root      9 Nov 28 01:31 lib64 -> usr/lib64
lrwxrwxrwx  1 root root     10 Nov 28 01:31 libx32 -> usr/libx32
drwxr-xr-x  1 root root   4096 Nov 28 01:31 media
drwxr-xr-x  1 root root   4096 Feb 13 20:19 mnt
drwxr-xr-x  1 root root   4096 Nov 28 01:31 opt
dr-xr-xr-x  9 root root      0 Feb 13 20:19 proc
drwx------  1 root root   4096 Feb 13 20:29 root
drwxr-xr-x  1 root root   4096 Feb 13 20:28 run
lrwxrwxrwx  1 root root      8 Nov 28 01:31 sbin -> usr/sbin
drwxr-xr-x  1 root root   4096 Nov 28 01:31 srv
dr-xr-xr-x 12 root root      0 Feb 13 20:19 sys
drwxrwxrwt  1 root root   4096 Feb 13 20:47 tmp
drwxr-xr-x  1 root root   4096 Nov 28 01:31 usr
drwxr-xr-x  1 root root   4096 Nov 28 01:31 var
```
## 2
```bash
kali:/$ chmod 777 init
# or
kali:/$ chmod u+x init
```
## 3
```bash
kali:/$ chown uuser2 init
```
## 4
```bash
kali:~$ find / -user root -perm -4000
```
