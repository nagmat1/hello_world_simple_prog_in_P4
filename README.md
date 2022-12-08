
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

I have inserted cables on Lanes 4,13 and 20. The Development ports are as follows: 

1. 192.168.1.1 - DEV PORT 284

2. 192.168.1.2 - DEV PORT 24

3.192.168.1.3 - DEV PORT 28

```
bfshell> ucli
Cannot read termcap database;
using dumb terminal settings.
bf-sde> pm
bf-sde.pm> show
-----+----+---+----+-------+----+--+--+---+---+---+--------+----------------+----------------+-
PORT |MAC |D_P|P/PT|SPEED  |FEC |AN|KR|RDY|ADM|OPR|LPBK    |FRAMES RX       |FRAMES TX       |E
-----+----+---+----+-------+----+--+--+---+---+---+--------+----------------+----------------+-
4/0  |40/0|284|2/28|10G    |NONE|Ds|Au|YES|ENB|UP |  NONE  |              36|               0| 
13/0 |22/0| 24|0/24|40G    |NONE|Ds|Au|YES|ENB|UP |  NONE  |              17|               0| 
20/0 | 8/0| 28|0/28|40G    |NONE|Ds|Au|YES|ENB|UP |  NONE  |              17|               2| 
33/0 |64/0| 64|0/64|10G    |NONE|En|Au|YES|ENB|UP |  NONE  |               1|               8| 
33/1 |64/1| 65|0/65|10G    |NONE|En|Au|YES|ENB|DWN|  NONE  |               0|               0| 
33/2 |64/2| 66|0/66|10G    |NONE|En|Au|YES|ENB|UP |  NONE  |               3|               0| 
33/3 |64/3| 67|0/67|10G    |NONE|En|Au|YES|ENB|DWN|  NONE  |               0|               0| 
601/0| 1/0|184|1/56|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
603/0| 3/0|176|1/48|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
605/0| 5/0|168|1/40|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
607/0| 7/0|160|1/32|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
609/0| 9/0|152|1/24|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
611/0|11/0|144|1/16|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
613/0|13/0|136|1/ 8|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
615/0|15/0|128|1/ 0|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
617/0|17/0|132|1/ 4|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
619/0|19/0|140|1/12|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
621/0|21/0|148|1/20|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
623/0|23/0|156|1/28|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
625/0|25/0|164|1/36|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
627/0|27/0|172|1/44|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
629/0|29/0|180|1/52|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
631/0|31/0|188|1/60|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
633/0|33/0|440|3/56|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
635/0|35/0|432|3/48|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
637/0|37/0|424|3/40|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
639/0|39/0|416|3/32|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
641/0|41/0|408|3/24|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
643/0|43/0|400|3/16|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
645/0|45/0|392|3/ 8|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
647/0|47/0|384|3/ 0|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
649/0|49/0|388|3/ 4|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
651/0|51/0|396|3/12|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
653/0|53/0|404|3/20|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
655/0|55/0|412|3/28|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
657/0|57/0|420|3/36|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
659/0|59/0|428|3/44|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
661/0|61/0|436|3/52|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
663/0|63/0|444|3/60|100G   |NONE|Au|Au|NO |ENB|UP |Mac-near|               0|               0| 
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

On host 2 and host 3 Run receive.py : 
``` python3 receive.py  ```

```
I= enp2s0
sniffing on enp2s0
got a packet
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
        sport     = 49848
        dport     = 5201
        seq       = 0
        ack       = 0
        dataofs   = 5
        reserved  = 0
        flags     = S
        window    = 8192
        chksum    = 0x8bc
        urgptr    = 0
        options   = []
###[ Raw ]### 
           load      = 'Salam'
###[ Padding ]### 
              load      = '\x00'
```





