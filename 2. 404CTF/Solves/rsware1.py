from binascii import hexlify, unhexlify
import os

with open("hope.pdf", "wb") as fd_out:
    cmd = os.popen('tshark -r ransomware1.pcapng -T fields -Y "ip.src==172.17.0.1" -e tcp.flags')
    fd_in = cmd.read()
    for line in fd_in.split("\n"):
        try:
            line = line.split("00")[1]
            if line == '':
                line = '00'
            fd_out.write(unhexlify(line))
        except:
            print('error', line)
