# Outlook over firebird
the server-address of the email is outlook.office365.com and sends the data over TLS.
The address where the TLS data is sent is 143.204.55.45, which is a cloud-centre in oslo. Upon further
inspection we find that that the SMTP port to outlook.office365.com is 567, with the transfer having
the following frames: 
![wireshark_screenshot](./smtp.png)
after the initial smtp-setup, the transfer continues over TLS and is encrypted 
(under you see the initial handshake and first frames of the transfer):
![tls_encrypted](./tls.png)