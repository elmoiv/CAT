# Chapter 3

## 1
```bash
kali:~$ ip a        # "ifconfig" is now "ip a"
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether **:**:**:**:**:** brd ff:ff:ff:ff:ff:ff
```
## 2
```bash
kali:~$ sudo ip addr add 192.168.1.1 dev eth0
```
## 3
```bash
kali:~$ sudo ip link set dev eth0 down
kali:~$ sudo ip link set dev eth0 address ef:ca:4b:fc:1d:f9
kali:~$ sudo ip link set dev eth0 up
```
## 4
```bash
kali:~$ iwconfig
```
## 5
```bash
kali:~$ dhclient eth0
```
## 6
```bash
kali:~$ dig www.google.com ns

; <<>> DiG 9.11.5-P4-5.1+b1-Debian <<>> www.google.com ns
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 41576
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;www.google.com.                        IN      NS

;; AUTHORITY SECTION:
google.com.             60      IN      SOA     ns1.google.com. dns-admin.google.com. 294627250 900 900 1800 60

;; Query time: 95 msec
;; SERVER: 163.121.128.134#53(163.121.128.134)
;; WHEN: Thu Feb 13 20:30:35 EET 2020
;; MSG SIZE  rcvd: 93
```
```bash
kali:~$ dig www.google.com mx

; <<>> DiG 9.11.5-P4-5.1+b1-Debian <<>> www.google.com ns
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 41576
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;www.google.com.                        IN      NS

;; AUTHORITY SECTION:
google.com.             60      IN      SOA     ns1.google.com. dns-admin.google.com. 294627250 900 900 1800 60

;; Query time: 95 msec
;; SERVER: 163.121.128.134#53(163.121.128.134)
;; WHEN: Thu Feb 13 20:30:35 EET 2020
;; MSG SIZE  rcvd: 93

```
## 7
```bash
kali:~$ echo "nameserver 8.8.8.8" /etc/resolv.conf
nameserver 8.8.8.8 /etc/resolv.conf
```
