
Ethernet switch on programmable switch : 

```
enp4s0f0 --> 192.168.1.6
enp4s0f1 --> 192.168.1.4 
```

Assign IPs as shown : 
```
sudo ip addr add 192.168.1.6/24 dev enp4s0f0 
sudo ip addr add 192.168.1.4/24 dev enp4s0f1
```


host 2 : enp2s0 --> 192.168.1.2 
host 3 : enp1s0f1 --> 192.168.1.3

Assign IPs as shown : 
```
sudo ip addr add 192.168.1.2/24 dev enp2s0
sudo ip addr add 192.168.1.3/24 dev enp1s0f1
```
