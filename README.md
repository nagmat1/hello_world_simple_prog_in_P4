
Simple program in P4 to check if the hosts are communicating with each other. 

Compile p4 program : 
1. ``` ./tools/p4_build.sh ~/mysde/exercises/24_simple_l3/simple_l3.p4 ```
Load the program : 
2. ```  ./run_switchd.sh -p simple_l3 ```
Load bfrt_python scripts :  
3. ```  ./run_bfshell.sh -b ./exercises/24_simple_l3/setup.py   ``` 

```
Using SDE /home/nagumahu1/mysde
Using SDE_INSTALL /home/nagumahu1/mysde/install
Connecting to localhost port 7777 to check status on these devices: [0]
Waiting for device 0 to be ready
3.6 --host localhost --port 7777 --device 0
/home/nagumahu1/mysde/install/bin/bfshell ./exercises/24_simple_l3/setup.py
bfrt_python ./exercises/24_simple_l3/setup.py
e
        ********************************************
        *      WARNING: Authorised Access Only     *
        ********************************************
    
xi
bfshell> bfrt_python ./exercises/24_simple_l3/setup.py
cwd : /home/nagumahu1/mysde

We've found 1 p4 programs for device 0:
simple_l3
Creating tree for dev 0 and program simple_l3

Devices found :  [0]
Python 3.8.10 (default, Apr 28 2022, 22:27:25) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.18.1 -- An enhanced Interactive Python. Type '?' for help.

******************* PROGAMMING RESULTS *****************

Table ipv4_host:
----- ipv4_host Dump Start -----
Default Entry:
Entry data (action : NoAction):

pipe.Ingress.ipv4_host entries for action: Ingress.send
hdr.ipv4.dst_addr    port
-------------------  ------
0xC0A80101           0x11C
0xC0A80102           0x18
0xC0A80103           0x1C
0xC0A801FE           0x40


pipe.Ingress.ipv4_host entries for action: Ingress.drop
hdr.ipv4.dst_addr
-------------------
0xC0A80104


----- ipv4_host Dump End -----
Table ipv4_lpm:
----- ipv4_lpm Dump Start -----
Default Entry:
Entry data (action : Ingress.send):
    port                           : 0x40

pipe.Ingress.ipv4_lpm entries for action: Ingress.send
hdr.ipv4.dst_addr             port
----------------------------  ------
('0xC0A80100', '0x00000018')  0x01
('0x00000000', '0x00000000')  0x40


pipe.Ingress.ipv4_lpm entries for action: Ingress.drop
hdr.ipv4.dst_addr
----------------------------
('0xC0A80000', '0x00000010')


----- ipv4_lpm Dump End -----
bfshell> exit
/home/nagumahu1/mysde/install/bin/bfshell -b ./exercises/24_simple_l3/setup.py
```

On host 1 with IP address 192.168.1.1:

Send packets using send.py : ``` python3 send.py 192.168.1.3 "Salam" ```

```
IFACE= enp193s0
sending on interface enp193s0 to 192.168.1.3
###[ Ethernet ]### 
  dst       = ff:ff:ff:ff:ff:ff
  src       = b8:ce:f6:77:d7:6e
  type      = IPv4
###[ IP ]### 
     version   = 4
     ihl       = 5
     tos       = 0x0
     len       = 45
     id        = 1
     flags     = 
     frag      = 0
     ttl       = 64
     proto     = tcp
     chksum    = 0xf775
     src       = 192.168.1.1
     dst       = 192.168.1.3
     \options   \
###[ TCP ]### 
        sport     = 60735
        dport     = 5201
        seq       = 0
        ack       = 0
        dataofs   = 5
        reserved  = 0
        flags     = S
        window    = 8192
        chksum    = 0xde34
        urgptr    = 0
        options   = []
###[ Raw ]### 
           load      = 'Salam'

```






