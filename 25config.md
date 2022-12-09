
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

