# Py-Pipe

## Synopsis
Usage: `python py-pipe.py -lport <port> -raddr <X.X.X.X> -rport <port> [-v] [-i <ip>]`

## Options
`-lport <port>`: Local Port to listen on (Required)
`-raddr <X.X.X.X>`: Remote IP Address to forward traffic to (Required)
`-rport <port>`: Remote Port to forward to (Required)
`-v, --verbose, --debug`: Enables verbose mode; Packets sent and received by the program will appear in the console window with an ASCII arrow indicating travel direction (Optional)
`-i, --ip`: Instructs the program to listen on a specific IP instead of `0.0.0.0`. Note: The IP address must be assigned to the local system on a running interface.

## Description
Py-Pipe is a TCP Port Forwarder inspired by Foundstone's fpipe program. Accepts a connection from a client (Computer-A) and proxy forwards connection traffic to a remote host (Computer-C) via Computer-B.

Py-Pipe is a free software program licensed under GNU General Public License v3.0.

![alt text](https://github.com/SparkWings/py-pipe/blob/main/py-pipe.PNG?raw=true)

## Examples
1. `python py-pipe.py -lport 4444 -raddr 172.18.31.1 -rport 23`: Forwards all traffic from port 4444 to 172.18.31.1:23 (telnet)
2. `python3 py-pipe.py -i 192.168.1.104 -lport 23 -raddr 192.168.1.2 -rport 23`: Forwards traffic from an interface with ip 192.168.1.104:23 to remote host 192.168.1.2:23

## Checksum
SHA-1: `5cb4f49ee4b92dd39b25292f81a1d8371fb9aaca`
MD5: `93c09b02d37f6466adaa408dc01ccedd`

## Author
This program was written by SparkWings <https://www.github.com/SparkWings> for Windows and Linux systems running Python version 2.7.18+. You may copy, distribute and modify the software as long as you track changes/dates in source files. Any modifications to or software including (via compiler) GPL-licensed code must also be made available under the GPL along with build & install instructions.
