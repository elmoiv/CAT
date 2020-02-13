# Chapter 6

## 1
```bash
kali:~$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   8892   312 ?        Ssl  20:19   0:00 /init
root        65  0.0  0.0   8896   216 tty1     Ss   20:30   0:00 /init
elmoiv      66  0.0  0.0  14972  2332 tty1     S    20:30   0:00 -bash
root      1760  0.0  0.0  15904  2220 tty1     S    21:08   0:00 sudo -i
root      1761  0.0  0.0  14976  2280 tty1     S    21:08   0:00 -bash
root      1765  0.0  0.0  16620  1820 tty1     R    21:12   0:00 ps aux
```
## 2
```bash
kali:/$ top

top - 21:22:34 up  1:02,  0 users,  load average: 0.52, 0.58, 0.59
Tasks:   4 total,   1 running,   3 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :  16263.2 total,   9736.4 free,   6302.9 used,    224.0 buff/cache
MiB Swap:  30365.1 total,  30365.1 free,      0.0 used.   9829.8 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
    1 root      20   0    8892    312    276 S   0.0   0.0   0:00.03 init
   65 root      20   0    8896    216    172 S   0.0   0.0   0:00.00 init
   66 elmoiv    20   0   14972   2348   2268 S   0.0   0.0   0:00.20 bash
 3369 elmoiv    20   0   16976   1956   1388 R   0.0   0.0   0:00.01 top
```
## 3
```bash
kali:/$ sudo kill -9 3369        # This kills "top"
```
## 4
```bash
kali:~$ renice 19 66             # Change priority of "bash" to +19
```
## 5
```bash
kali:~$ cat > scanscript.sh
echo "ScanScript by Khaled El-Morshedy"
echo "Scanning in progress..."
find / -user root -perm -4000
echo "Scanning Completed :)"
                                        # Pressed Ctrl+C to exit editor
kali:~$ chmod u+x scanscript.sh         # Give myself permission to execute
kali:~$ ./scanscript.sh
ScanScript by Khaled El-Morshedy
Scanning in progress...
find: ‘/etc/ssl/private’: Permission denied
find: ‘/mnt/c/hiberfil.sys’: Permission denied
find: ‘/mnt/c/pagefile.sys’: Permission denied
            --- snip ---
Scanning Completed :)

kali:~$ at tomorrow
at> scanscript.sh

# my script will run tomorrow
```
