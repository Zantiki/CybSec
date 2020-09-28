# Outlook over firebird
the server-address of the email is outlook.office365.com and sends the data over TLS.
The address where the TLS data is sent is 143.204.55.45, which is a cloud-centre in oslo. Upon further
inspection we find that that the SMTP port to outlook.office365.com is 567, with the transfer having
the following frames: 
![wireshark_screenshot](./smtp.png)
after the initial smtp-setup, the transfer continues over TLS and is encrypted 
(under you see the initial handshake and first frames of the transfer):
![tls_encrypted](./tls.png)

# Results from email_check

```console
---Scanning ibm.com---
ipv4s:  129.42.38.10
ipv6s: 

---reverse lookup---
Reverse lookup of 129.42.38.10:  None found

---mx servers---
mx0a-001b2d01.pphosted.com.
mx0b-001b2d01.pphosted.com.

---spf lookup---
ip4:148.163.158.5
ip4:148.163.156.1
ip4:67.231.145.127
ip4:67.231.153.87
ip4:168.245.101.145
_spf.google.com
_netblocks.google.com
ip4:35.190.247.0/24
ip4:64.233.160.0/19
ip4:66.102.0.0/20
ip4:66.249.80.0/20
ip4:72.14.192.0/18
ip4:74.125.0.0/16
ip4:108.177.8.0/21
ip4:173.194.0.0/16
ip4:209.85.128.0/17
ip4:216.58.192.0/19
ip4:216.239.32.0/19
_netblocks2.google.com
_netblocks3.google.com
ip4:172.217.0.0/19
ip4:172.217.32.0/20
ip4:172.217.128.0/19
ip4:172.217.160.0/20
ip4:172.217.192.0/19
ip4:172.253.56.0/21
ip4:172.253.112.0/20
ip4:108.177.96.0/19
ip4:35.191.0.0/16
ip4:130.211.0.0/22

##########################################
---Scanning statoil.no---
ipv4s:  140.86.60.34
ipv6s: 

---reverse lookup---
Reverse lookup of 140.86.60.34:  None found

---mx servers---
statoil-no.mail.protection.outlook.com.

---spf lookup---
spf.protection.outlook.com
ip4:40.92.0.0/15
ip4:40.107.0.0/16
ip4:52.100.0.0/14
ip4:104.47.0.0/17
spfd.protection.outlook.com
ip4:51.4.72.0/24
ip4:51.5.72.0/24
ip4:51.5.80.0/27
ip4:51.4.80.0/27

########################################
---Scanning google.com---
ipv4s:  172.217.21.142
ipv6s:  2a00:1450:400f:80d::200e

---reverse lookup---
Reverse lookup of 172.217.21.142:  arn11s02-in-f14.1e100.net. fra07s63-in-f142.1e100.net.
Reverse lookup of 2a00:1450:400f:80d::200e:  arn09s20-in-x0e.1e100.net.

---mx servers---
alt4.aspmx.l.google.com.
alt3.aspmx.l.google.com.
aspmx.l.google.com.
alt2.aspmx.l.google.com.
alt1.aspmx.l.google.com.

---spf lookup---
_spf.google.com
_netblocks.google.com
ip4:35.190.247.0/24
ip4:64.233.160.0/19
ip4:66.102.0.0/20
ip4:66.249.80.0/20
ip4:72.14.192.0/18
ip4:74.125.0.0/16
ip4:108.177.8.0/21
ip4:173.194.0.0/16
ip4:209.85.128.0/17
ip4:216.58.192.0/19
ip4:216.239.32.0/19
_netblocks2.google.com
_netblocks3.google.com
ip4:172.217.0.0/19
ip4:172.217.32.0/20
ip4:172.217.128.0/19
ip4:172.217.160.0/20
ip4:172.217.192.0/19
ip4:172.253.56.0/21
ip4:172.253.112.0/20
ip4:108.177.96.0/19
ip4:35.191.0.0/16
ip4:130.211.0.0/22
```