➜  ~ docker run -it --rm --name rustscan rustscan/rustscan:latest -a 192.168.100.1 
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: http://discord.skerritt.blog           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan

[~] The config file is expected to be at "/home/rustscan/.rustscan.toml"
[~] File limit higher than batch size. Can increase speed by increasing batch size '-b 1048476'.
Open 192.168.100.1:23
Open 192.168.100.1:53
Open 192.168.100.1:80
Open 192.168.100.1:443
Open 192.168.100.1:37443
Open 192.168.100.1:37444
[~] Starting Script(s)
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2024-07-01 09:50 UTC
Initiating Ping Scan at 09:50
Scanning 192.168.100.1 [2 ports]
Completed Ping Scan at 09:50, 0.00s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 09:50
Completed Parallel DNS resolution of 1 host. at 09:50, 1.01s elapsed
DNS resolution of 1 IPs took 1.01s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 09:50
Scanning 192.168.100.1 [6 ports]
Discovered open port 80/tcp on 192.168.100.1
Discovered open port 23/tcp on 192.168.100.1
Discovered open port 443/tcp on 192.168.100.1
Discovered open port 53/tcp on 192.168.100.1
Discovered open port 37444/tcp on 192.168.100.1
Discovered open port 37443/tcp on 192.168.100.1
Completed Connect Scan at 09:50, 0.01s elapsed (6 total ports)
Nmap scan report for 192.168.100.1
Host is up, received syn-ack (0.0029s latency).
Scanned at 2024-07-01 09:50:42 UTC for 0s

PORT      STATE SERVICE REASON
23/tcp    open  telnet  syn-ack
53/tcp    open  domain  syn-ack
80/tcp    open  http    syn-ack
443/tcp   open  https   syn-ack
37443/tcp open  unknown syn-ack
37444/tcp open  unknown syn-ack

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 1.07 seconds
