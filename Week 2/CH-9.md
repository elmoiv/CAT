# Chapter 9

## 1
```bash
kali:~$ cat > S1.sh
abcdefghijklmnopqrstuvwxyz

kali:~$ cp S1.sh S2.sh
kali:~$ cp S1.sh S3.sh
```
## 2
```bash
kali:~$ tar -cf L4H.tar S1.sh S2.sh S3.sh
```
## 3
```bash
kali:~$ gzip L4H.tar
```
## 4
```bash
kali:~$ bzip2 L4H.tar
```
## 5
```bash
kali:~$ compress L4H.tar
```
## 6
```bash
kali:~$ dd if=/dev/media of=/root/flashcopy bs=4096 conv:noerror
```
