import public_ip as ip
import requests

request = requests.get("https://ident.me")
ip_publica = request.text
print(ip_publica)

ip_publica2 = ip.get()
print(ip_publica2)
