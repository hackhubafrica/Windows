Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-01 13:02 EAT
NSE: Loaded 150 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 13:02
Completed NSE at 13:03, 10.01s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 13:03
Completed NSE at 13:03, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 13:03
Completed Parallel DNS resolution of 1 host. at 13:03, 1.03s elapsed
DNS resolution of 1 IPs took 1.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 13:03
Scanning 192.168.100.1 [6 ports]
Discovered open port 23/tcp on 192.168.100.1
Discovered open port 443/tcp on 192.168.100.1
Discovered open port 53/tcp on 192.168.100.1
Discovered open port 80/tcp on 192.168.100.1
Discovered open port 37444/tcp on 192.168.100.1
Discovered open port 37443/tcp on 192.168.100.1
Completed Connect Scan at 13:03, 0.00s elapsed (6 total ports)
Initiating Service scan at 13:03
Scanning 6 services on 192.168.100.1
Completed Service scan at 13:03, 20.34s elapsed (6 services on 1 host)
NSE: Script scanning 192.168.100.1.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 13:03
NSE: [firewall-bypass 192.168.100.1] lacks privileges.
NSE Timing: About 93.79% done; ETC: 13:03 (0:00:02 remaining)
NSE Timing: About 97.04% done; ETC: 13:04 (0:00:02 remaining)
NSE Timing: About 99.49% done; ETC: 13:04 (0:00:00 remaining)
NSE Timing: About 99.74% done; ETC: 13:05 (0:00:00 remaining)
Completed NSE at 13:05, 150.70s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 13:05
NSE: [tls-ticketbleed 192.168.100.1:443] Not running due to lack of privileges.
NSE: [ssl-ccs-injection 192.168.100.1:443] No response from server: EOF
Completed NSE at 13:05, 2.48s elapsed
Nmap scan report for 192.168.100.1
Host is up, received user-set (0.0019s latency).
Scanned at 2024-07-01 13:03:05 EAT for 174s

PORT      STATE SERVICE   REASON  VERSION
23/tcp    open  telnet    syn-ack Huawei Home Gateway telnetd
53/tcp    open  domain    syn-ack ISC BIND 9.16.15 (Ubuntu Linux)
| vulners: 
|   cpe:/a:isc:bind:9.16.15: 
|     	CVE-2023-50387	7.5	https://vulners.com/cve/CVE-2023-50387
|     	CVE-2023-3341	7.5	https://vulners.com/cve/CVE-2023-3341
|     	CVE-2023-2829	7.5	https://vulners.com/cve/CVE-2023-2829
|     	CVE-2023-2828	7.5	https://vulners.com/cve/CVE-2023-2828
|     	CVE-2022-3924	7.5	https://vulners.com/cve/CVE-2022-3924
|     	CVE-2022-38178	7.5	https://vulners.com/cve/CVE-2022-38178
|     	CVE-2022-38177	7.5	https://vulners.com/cve/CVE-2022-38177
|     	CVE-2022-3736	7.5	https://vulners.com/cve/CVE-2022-3736
|     	CVE-2022-3094	7.5	https://vulners.com/cve/CVE-2022-3094
|     	CVE-2022-3080	7.5	https://vulners.com/cve/CVE-2022-3080
|     	CVE-2019-6470	7.5	https://vulners.com/cve/CVE-2019-6470
|     	BB688FBF-CEE2-5DD1-8561-8F76501DE2D4	7.5	https://vulners.com/githubexploit/BB688FBF-CEE2-5DD1-8561-8F76501DE2D4	*EXPLOIT*
|     	CVE-2021-25220	6.8	https://vulners.com/cve/CVE-2021-25220
|     	CVE-2022-2795	5.3	https://vulners.com/cve/CVE-2022-2795
|     	CVE-2022-0396	5.3	https://vulners.com/cve/CVE-2022-0396
|_    	CVE-2021-25219	5.3	https://vulners.com/cve/CVE-2021-25219
80/tcp    open  http      syn-ack
|_http-vuln-cve2017-1001000: ERROR: Script execution failed (use -d to debug)
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
| fingerprint-strings: 
|   FourOhFourRequest, GetRequest: 
|     HTTP/1.1 400 Bad Request
|     Connection: Keep-Alive
|   GenericLines: 
|     HTTP/1.1 404 Not Found
|     Connection: Keep-Alive
|     requested URL was not found on this server.
|   HTTPOptions, RTSPRequest, SIPOptions: 
|     HTTP/1.1 404 Not Found
|     Content-Type:text/html
|     Pragma:no-cache
|     Cache-control:no-cache, no-store, max-age=0
|     Transfer-Encoding:chunked
|     X-Frame-Options:SAMEORIGIN
|     Connection:Keep-Alive
|_    requested URL was not found on this server.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
| http-litespeed-sourcecode-download: 
| Litespeed Web Server Source Code Disclosure (CVE-2010-2333)
| /index.php source code:
| <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\x0D
| <html xmlns="http://www.w3.org/1999/xhtml">\x0D
| <head>\x0D
| <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\x0D
| <meta http-equiv="X-UA-Compatible" content="IE=edge;chrome=1">\x0D
| <meta http-equiv="Pragma" content="no-cache" />\x0D
| <title></title>\x0D
| <script language="JavaScript" type="text/javascript">\x0D
| var SSLPort ='443';\x0D
| var SSLHostIp ='192\x2e168\x2e100\x2e1';\x0D
| var HostInfo = window.location.host;\x0D
| var IsMaintWan = '0';\x0D
| if (IsMaintWan == 1)\x0D
| {\x0D
| SSLPort = '7017';\x0D
| }\x0D
| \x0D
| function IsIPv6AddressUshortValid(Short)\x0D
| {\x0D
|     if (Short.length > 4)\x0D
|     {\x0D
|         return false;\x0D
|     }\x0D
|     \x0D
|     for (var i = 0; i < Short.length; i++)\x0D
|     {\x0D
|         var Char = Short.charAt(i);\x0D
|         if (!((Char >= '0' && Char <= '9') || (Char >= 'a' && Char <= 'f') || (Char >= 'A' && Char <= 'F')))\x0D
|         {\x0D
|             return false;\x0D
|         }\x0D
|     }\x0D
|     \x0D
|     return true;\x0D
| }\x0D
| \x0D
| function IsStandardIPv6AddressValid(Address)\x0D
| {\x0D
|     if ((Address.charAt(0) == ':') || (Address.charAt(Address.length-1) == ':'))\x0D
|     {\x0D
|         return false;\x0D
|     }    \x0D
|     \x0D
|     List = Address.split(":");\x0D
|     if (List.length > 8)\x0D
|     {\x0D
|         return false;\x0D
|     }\x0D
| \x0D
|     for (var i = 0; i < List.length; i++)\x0D
|     {\x0D
|         if (false == IsIPv6AddressUshortValid(List[i]))\x0D
|         {\x0D
|             return false;\x0D
|         }\x0D
|     }    \x0D
|     \x0D
|     return true;   \x0D
| }\x0D
| \x0D
| function IsIPv6AddressValid(Address)\x0D
| {\x0D
|     if (Address == "::")\x0D
|     {\x0D
|         return true;\x0D
|     }\x0D
| \x0D
|     if (Address.length < 3)\x0D
|     {\x0D
|         return false;\x0D
|     }\x0D
| \x0D
|     var List = Address.split("::");\x0D
|     if (List.length > 2)\x0D
|     {\x0D
|         return false;\x0D
|     }\x0D
|     \x0D
|     if (List.length == 1)\x0D
|     if (Address.split(":").length != 8)\x0D
|     {\x0D
|         return false;\x0D
|     }\x0D
|     \x0D
|     if (List.length > 1)\x0D
|     if (Address.split(":").length > 8)\x0D
|     {\x0D
|         return false;\x0D
|     }\x0D
| \x0D
|     List = Address.split("::");\x0D
|     for (var i = 0; i < List.length; i++)\x0D
|     {\x0D
|         if (false == IsStandardIPv6AddressValid(List[i]))\x0D
|         {\x0D
|             return false;\x0D
|         }\x0D
|     }\x0D
|     return true;\x0D
| }\x0D
| \x0D
| function LoadFrame()\x0D
| {\x0D
| var lastindex = HostInfo.lastIndexOf(":");\x0D
| if(-1 == lastindex)\x0D
| {\x0D
| /* host string not include ":", just ipv4 addr */\x0D
| window.location="https://" + HostInfo + ":" + SSLPort;\x0D
| }\x0D
| else\x0D
| {\x0D
| var List = HostInfo.split(":");\x0D
| if(List.length >= 3)\x0D
| {\x0D
| /* include two or more than two ":" */\x0D
| if(true == IsIPv6AddressValid(HostInfo))\x0D
| {\x0D
| /* host string not include port */\x0D
| window.location="https://[" + HostInfo + "]:" + SSLPort;\x0D
| }\x0D
| else\x0D
| {\x0D
| var newipv6addr = HostInfo.substr(0,lastindex);\x0D
| var newipv6port = HostInfo.substr(lastindex+1);\x0D
| if (IsMaintWan == 0)\x0D
| {\x0D
| window.location="https://[" + newipv6addr + "]:" + SSLPort;\x0D
| }\x0D
| else\x0D
| {\x0D
| window.location="https://[" + newipv6addr + "]:" + newipv6port;\x0D
| }\x0D
| }\x0D
| }\x0D
| else\x0D
| {\x0D
| /* just one ":" */\x0D
| var newipv4addr = HostInfo.substr(0,lastindex);\x0D
| if (IsMaintWan == 0)\x0D
| {\x0D
| window.location="https://" + newipv4addr + ":" + SSLPort;\x0D
| }\x0D
| else\x0D
| {\x0D
| window.location="https://" + HostInfo;\x0D
| }\x0D
| }\x0D
| }\x0D
| }\x0D
| </script>\x0D
| </head>\x0D
| <body class="mainbody" onLoad="LoadFrame();"> \x0D
| </body>\x0D
|_</html>\x0D
| http-phpmyadmin-dir-traversal: 
|   VULNERABLE:
|   phpMyAdmin grab_globals.lib.php subform Parameter Traversal Local File Inclusion
|     State: VULNERABLE (Exploitable)
|     IDs:  CVE:CVE-2005-3299
|       PHP file inclusion vulnerability in grab_globals.lib.php in phpMyAdmin 2.6.4 and 2.6.4-pl1 allows remote attackers to include local files via the $__redirect parameter, possibly involving the subform array.
|       
|     Disclosure date: 2005-10-nil
|     Extra information:
|       ../../../../../etc/passwd :
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|     References:
|       http://www.exploit-db.com/exploits/1244/
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2005-3299
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-majordomo2-dir-traversal: ERROR: Script execution failed (use -d to debug)
443/tcp   open  ssl/https syn-ack
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| ssl-poodle: 
|   VULNERABLE:
|   SSL POODLE information leak
|     State: VULNERABLE
|     IDs:  BID:70574  CVE:CVE-2014-3566
|           The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and other
|           products, uses nondeterministic CBC padding, which makes it easier
|           for man-in-the-middle attackers to obtain cleartext data via a
|           padding-oracle attack, aka the "POODLE" issue.
|     Disclosure date: 2014-10-14
|     Check results:
|       TLS_RSA_WITH_AES_128_CBC_SHA
|     References:
|       https://www.securityfocus.com/bid/70574
|       https://www.openssl.org/~bodo/ssl-poodle.pdf
|       https://www.imperialviolet.org/2014/10/14/poodle.html
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-3566
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
|_ssl-ccs-injection: No reply from server (TIMEOUT)
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
| http-slowloris-check: 
|   VULNERABLE:
|   Slowloris DOS attack
|     State: LIKELY VULNERABLE
|     IDs:  CVE:CVE-2007-6750
|       Slowloris tries to keep many connections to the target web server open and hold
|       them open as long as possible.  It accomplishes this by opening connections to
|       the target web server and sending a partial request. By doing so, it starves
|       the http server's resources causing Denial Of Service.
|       
|     Disclosure date: 2009-09-17
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-6750
|_      http://ha.ckers.org/slowloris/
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-majordomo2-dir-traversal: ERROR: Script execution failed (use -d to debug)
37443/tcp open  upnp      syn-ack Portable SDK for UPnP devices 1.6.18 (Linux 3.10.53-HULK2; UPnP 1.0)
37444/tcp open  upnp      syn-ack Portable SDK for UPnP devices 1.6.18 (Linux 3.10.53-HULK2; UPnP 1.0)
| vulners: 
|   cpe:/o:linux:linux_kernel:3.10.53-hulk2: 
|     	SSV:93207	10.0	https://vulners.com/seebug/SSV:93207	*EXPLOIT*
|     	SSV:92945	10.0	https://vulners.com/seebug/SSV:92945	*EXPLOIT*
|     	PACKETSTORM:167805	10.0	https://vulners.com/packetstorm/PACKETSTORM:167805	*EXPLOIT*
|     	PACKETSTORM:155267	10.0	https://vulners.com/packetstorm/PACKETSTORM:155267	*EXPLOIT*
|     	EXPLOITPACK:CDE6BEFB491AF8EAA191AB4CAF1FFA98	10.0	https://vulners.com/exploitpack/EXPLOITPACK:CDE6BEFB491AF8EAA191AB4CAF1FFA98	*EXPLOIT*
|     	CVE-2015-1421	10.0	https://vulners.com/cve/CVE-2015-1421
|     	1337DAY-ID-37859	10.0	https://vulners.com/zdt/1337DAY-ID-37859	*EXPLOIT*
|     	1337DAY-ID-33499	10.0	https://vulners.com/zdt/1337DAY-ID-33499	*EXPLOIT*
|     	EDB-ID:47625	9.8	https://vulners.com/exploitdb/EDB-ID:47625	*EXPLOIT*
|     	CVE-2021-3773	9.8	https://vulners.com/cve/CVE-2021-3773
|     	CVE-2019-18814	9.8	https://vulners.com/cve/CVE-2019-18814
|     	CVE-2019-17133	9.8	https://vulners.com/cve/CVE-2019-17133
|     	CVE-2019-16746	9.8	https://vulners.com/cve/CVE-2019-16746
|     	CVE-2019-15505	9.8	https://vulners.com/cve/CVE-2019-15505
|     	CVE-2019-14897	9.8	https://vulners.com/cve/CVE-2019-14897
|     	CVE-2019-14896	9.8	https://vulners.com/cve/CVE-2019-14896
|     	CVE-2019-14895	9.8	https://vulners.com/cve/CVE-2019-14895
|     	CVE-2017-7895	9.8	https://vulners.com/cve/CVE-2017-7895
|     	CVE-2017-5897	9.8	https://vulners.com/cve/CVE-2017-5897
|     	CVE-2017-18174	9.8	https://vulners.com/cve/CVE-2017-18174
|     	CVE-2017-18017	9.8	https://vulners.com/cve/CVE-2017-18017
|     	CVE-2016-9555	9.8	https://vulners.com/cve/CVE-2016-9555
|     	CVE-2016-7117	9.8	https://vulners.com/cve/CVE-2016-7117
|     	CVE-2016-5344	9.8	https://vulners.com/cve/CVE-2016-5344
|     	CVE-2016-5343	9.8	https://vulners.com/cve/CVE-2016-5343
|     	CVE-2016-3955	9.8	https://vulners.com/cve/CVE-2016-3955
|     	CVE-2016-10229	9.8	https://vulners.com/cve/CVE-2016-10229
|     	CVE-2015-8812	9.8	https://vulners.com/cve/CVE-2015-8812
|     	CVE-2015-0573	9.8	https://vulners.com/cve/CVE-2015-0573
|     	CVE-2014-9410	9.8	https://vulners.com/cve/CVE-2014-9410
|     	SSV:93143	9.3	https://vulners.com/seebug/SSV:93143	*EXPLOIT*
|     	SSV:93140	9.3	https://vulners.com/seebug/SSV:93140	*EXPLOIT*
|     	PACKETSTORM:141339	9.3	https://vulners.com/packetstorm/PACKETSTORM:141339	*EXPLOIT*
|     	PACKETSTORM:141331	9.3	https://vulners.com/packetstorm/PACKETSTORM:141331	*EXPLOIT*
|     	PACKETSTORM:135372	9.3	https://vulners.com/packetstorm/PACKETSTORM:135372	*EXPLOIT*
|     	EXPLOITPACK:439E4D3ACF94B8A9B5703C9D6BAD1C6C	9.3	https://vulners.com/exploitpack/EXPLOITPACK:439E4D3ACF94B8A9B5703C9D6BAD1C6C	*EXPLOIT*
|     	CVE-2015-3331	9.3	https://vulners.com/cve/CVE-2015-3331
|     	1BD47E86-3B10-5D96-B1C1-658AFD757407	9.3	https://vulners.com/githubexploit/1BD47E86-3B10-5D96-B1C1-658AFD757407	*EXPLOIT*
|     	1337DAY-ID-25771	9.3	https://vulners.com/zdt/1337DAY-ID-25771	*EXPLOIT*
|     	CVE-2022-0742	9.1	https://vulners.com/cve/CVE-2022-0742
|     	CVE-2019-15926	9.1	https://vulners.com/cve/CVE-2019-15926
|     	CVE-2014-3180	9.1	https://vulners.com/cve/CVE-2014-3180
|     	CVE-2015-4002	9.0	https://vulners.com/cve/CVE-2015-4002
|     	CVE-2015-4001	9.0	https://vulners.com/cve/CVE-2015-4001
|     	MSF:EXPLOIT-LINUX-LOCAL-CVE_2022_1043_IO_URING_PRIV_ESC-	8.8	https://vulners.com/metasploit/MSF:EXPLOIT-LINUX-LOCAL-CVE_2022_1043_IO_URING_PRIV_ESC-	*EXPLOIT*
|     	CVE-2023-44466	8.8	https://vulners.com/cve/CVE-2023-44466
|     	CVE-2022-42896	8.8	https://vulners.com/cve/CVE-2022-42896
|     	CVE-2022-2196	8.8	https://vulners.com/cve/CVE-2022-2196
|     	CVE-2022-1043	8.8	https://vulners.com/cve/CVE-2022-1043
|     	CVE-2022-0435	8.8	https://vulners.com/cve/CVE-2022-0435
|     	CVE-2021-4154	8.8	https://vulners.com/cve/CVE-2021-4154
|     	CVE-2021-4093	8.8	https://vulners.com/cve/CVE-2021-4093
|     	CVE-2021-3653	8.8	https://vulners.com/cve/CVE-2021-3653
|     	CVE-2020-36158	8.8	https://vulners.com/cve/CVE-2020-36158
|     	CVE-2019-3846	8.8	https://vulners.com/cve/CVE-2019-3846
|     	CVE-2019-17666	8.8	https://vulners.com/cve/CVE-2019-17666
|     	CVE-2019-14821	8.8	https://vulners.com/cve/CVE-2019-14821
|     	CVE-2019-10220	8.8	https://vulners.com/cve/CVE-2019-10220
|     	CVE-2018-16882	8.8	https://vulners.com/cve/CVE-2018-16882
|     	CE3B1D33-B4CA-596B-88B1-7DAA7FF99D30	8.8	https://vulners.com/githubexploit/CE3B1D33-B4CA-596B-88B1-7DAA7FF99D30	*EXPLOIT*
|     	BEF9C9DA-D16B-58C7-AD6A-7A645E871F56	8.8	https://vulners.com/githubexploit/BEF9C9DA-D16B-58C7-AD6A-7A645E871F56	*EXPLOIT*
|     	BDD6E431-5CC7-5183-A9D8-4870D7DF5670	8.8	https://vulners.com/githubexploit/BDD6E431-5CC7-5183-A9D8-4870D7DF5670	*EXPLOIT*
|     	B7E2B5CA-78B4-51D7-BE5F-DE5CA357E0F9	8.8	https://vulners.com/githubexploit/B7E2B5CA-78B4-51D7-BE5F-DE5CA357E0F9	*EXPLOIT*
|     	9080771D-5FCF-52BA-A72B-EC1BD7CF79B7	8.8	https://vulners.com/githubexploit/9080771D-5FCF-52BA-A72B-EC1BD7CF79B7	*EXPLOIT*
|     	4C3A6395-A40A-538E-BE67-F3B2B7B887C3	8.8	https://vulners.com/githubexploit/4C3A6395-A40A-538E-BE67-F3B2B7B887C3	*EXPLOIT*
|     	4B9FC39D-E20E-5C2B-9C2F-B18BF0FCFF81	8.8	https://vulners.com/githubexploit/4B9FC39D-E20E-5C2B-9C2F-B18BF0FCFF81	*EXPLOIT*
|     	48A6CF92-30C0-5ABD-894A-38DE0329DA11	8.8	https://vulners.com/githubexploit/48A6CF92-30C0-5ABD-894A-38DE0329DA11	*EXPLOIT*
|     	1337DAY-ID-38180	8.8	https://vulners.com/zdt/1337DAY-ID-38180	*EXPLOIT*
|     	CVE-2022-1055	8.6	https://vulners.com/cve/CVE-2022-1055
|     	CVE-2015-4004	8.5	https://vulners.com/cve/CVE-2015-4004
|     	CVE-2022-0185	8.4	https://vulners.com/cve/CVE-2022-0185
|     	CVE-2017-2583	8.4	https://vulners.com/cve/CVE-2017-2583
|     	CVE-2016-3134	8.4	https://vulners.com/cve/CVE-2016-3134
|     	C82EF4EF-DD99-59F6-8089-4CD646ADD47F	8.4	https://vulners.com/githubexploit/C82EF4EF-DD99-59F6-8089-4CD646ADD47F	*EXPLOIT*
|     	C3AC5E4B-16BD-51A0-9946-BD8044D50A25	8.4	https://vulners.com/githubexploit/C3AC5E4B-16BD-51A0-9946-BD8044D50A25	*EXPLOIT*
|     	5E126606-F632-53C1-B0AA-B3EF25F6DEF9	8.4	https://vulners.com/githubexploit/5E126606-F632-53C1-B0AA-B3EF25F6DEF9	*EXPLOIT*
|     	3866C22C-F32D-51B1-ABFA-8EBE645C9E48	8.4	https://vulners.com/githubexploit/3866C22C-F32D-51B1-ABFA-8EBE645C9E48	*EXPLOIT*
|     	23F688A6-E20D-50D4-8086-551284E49664	8.4	https://vulners.com/githubexploit/23F688A6-E20D-50D4-8086-551284E49664	*EXPLOIT*
|     	12D425DC-1CB6-54A7-990D-D8B140778D13	8.4	https://vulners.com/githubexploit/12D425DC-1CB6-54A7-990D-D8B140778D13	*EXPLOIT*
|     	SSV:96467	8.3	https://vulners.com/seebug/SSV:96467	*EXPLOIT*
|     	MSF:EXPLOIT-LINUX-LOCAL-NETFILTER_XTABLES_HEAP_OOB_WRITE_PRIV_ESC-	8.3	https://vulners.com/metasploit/MSF:EXPLOIT-LINUX-LOCAL-NETFILTER_XTABLES_HEAP_OOB_WRITE_PRIV_ESC-	*EXPLOIT*
|     	EXPLOITPACK:893F34D304318590019AD4800C97CC57	8.3	https://vulners.com/exploitpack/EXPLOITPACK:893F34D304318590019AD4800C97CC57	*EXPLOIT*
|     	EDB-ID:50135	8.3	https://vulners.com/exploitdb/EDB-ID:50135	*EXPLOIT*
|     	E7E00541-3777-5D3F-A33F-EAEE6520CEC1	8.3	https://vulners.com/githubexploit/E7E00541-3777-5D3F-A33F-EAEE6520CEC1	*EXPLOIT*
|     	CVE-2021-22555	8.3	https://vulners.com/cve/CVE-2021-22555
|     	BC48A99A-7FA7-5FC9-BABD-F53AF7D2C554	8.3	https://vulners.com/githubexploit/BC48A99A-7FA7-5FC9-BABD-F53AF7D2C554	*EXPLOIT*
|     	1337DAY-ID-36873	8.3	https://vulners.com/zdt/1337DAY-ID-36873	*EXPLOIT*
|     	1337DAY-ID-36562	8.3	https://vulners.com/zdt/1337DAY-ID-36562	*EXPLOIT*
|     	CVE-2023-39191	8.2	https://vulners.com/cve/CVE-2023-39191
|     	CVE-2022-1012	8.2	https://vulners.com/cve/CVE-2022-1012
|     	CVE-2019-19770	8.2	https://vulners.com/cve/CVE-2019-19770
|     	CVE-2023-1194	8.1	https://vulners.com/cve/CVE-2023-1194
|     	CVE-2020-28374	8.1	https://vulners.com/cve/CVE-2020-28374
|     	CVE-2020-14305	8.1	https://vulners.com/cve/CVE-2020-14305
|     	CVE-2019-6974	8.1	https://vulners.com/cve/CVE-2019-6974
|     	CVE-2018-20836	8.1	https://vulners.com/cve/CVE-2018-20836
|     	CVE-2017-15126	8.1	https://vulners.com/cve/CVE-2017-15126
|     	EDB-ID:42762	8.0	https://vulners.com/exploitdb/EDB-ID:42762	*EXPLOIT*
|     	CVE-2023-52434	8.0	https://vulners.com/cve/CVE-2023-52434
|     	CVE-2021-4157	8.0	https://vulners.com/cve/CVE-2021-4157
|     	CVE-2018-16884	8.0	https://vulners.com/cve/CVE-2018-16884
|     	CVE-2017-1000251	8.0	https://vulners.com/cve/CVE-2017-1000251
|     	ZSL-2019-5526	7.8	https://vulners.com/zeroscience/ZSL-2019-5526	*EXPLOIT*
|     	SAINT:ACA0D81E9F0D7499A5952D634DA1559F	7.8	https://vulners.com/saint/SAINT:ACA0D81E9F0D7499A5952D634DA1559F	*EXPLOIT*
|     	SAINT:489AB9509BA8D92A0D1AD0EDD028BB0F	7.8	https://vulners.com/saint/SAINT:489AB9509BA8D92A0D1AD0EDD028BB0F	*EXPLOIT*
|     	SAINT:24BDE9528F493A62492AC5847ED078BA	7.8	https://vulners.com/saint/SAINT:24BDE9528F493A62492AC5847ED078BA	*EXPLOIT*
|     	SAINT:23F7A7540E4D766FDCBF9B2C875D49EB	7.8	https://vulners.com/saint/SAINT:23F7A7540E4D766FDCBF9B2C875D49EB	*EXPLOIT*
|     	MSF:EXPLOIT-LINUX-LOCAL-NETFILTER_PRIV_ESC_IPV4-	7.8	https://vulners.com/metasploit/MSF:EXPLOIT-LINUX-LOCAL-NETFILTER_PRIV_ESC_IPV4-	*EXPLOIT*
|     	MSF:EXPLOIT-LINUX-LOCAL-DOCKER_CGROUP_ESCAPE-	7.8	https://vulners.com/metasploit/MSF:EXPLOIT-LINUX-LOCAL-DOCKER_CGROUP_ESCAPE-	*EXPLOIT*
|     	MSF:EXPLOIT-LINUX-LOCAL-CVE_2022_0995_WATCH_QUEUE-	7.8	https://vulners.com/metasploit/MSF:EXPLOIT-LINUX-LOCAL-CVE_2022_0995_WATCH_QUEUE-	*EXPLOIT*
|     	MSF:EXPLOIT-LINUX-LOCAL-CVE_2022_0847_DIRTYPIPE-	7.8	https://vulners.com/metasploit/MSF:EXPLOIT-LINUX-LOCAL-CVE_2022_0847_DIRTYPIPE-	*EXPLOIT*
|     	MSF:EXPLOIT-LINUX-LOCAL-AF_PACKET_PACKET_SET_RING_PRIV_ESC-	7.8	https://vulners.com/metasploit/MSF:EXPLOIT-LINUX-LOCAL-AF_PACKET_PACKET_SET_RING_PRIV_ESC-	*EXPLOIT*
|     	MSF:EXPLOIT-LINUX-LOCAL-AF_PACKET_CHOCOBO_ROOT_PRIV_ESC-	7.8	https://vulners.com/metasploit/MSF:EXPLOIT-LINUX-LOCAL-AF_PACKET_CHOCOBO_ROOT_PRIV_ESC-	*EXPLOIT*
|     	F96353A7-4B24-55A5-94FF-961F6C500826	7.8	https://vulners.com/githubexploit/F96353A7-4B24-55A5-94FF-961F6C500826	*EXPLOIT*
|     	F68A7C89-1ADB-5CF7-8EAC-4DEA137ED81A	7.8	https://vulners.com/githubexploit/F68A7C89-1ADB-5CF7-8EAC-4DEA137ED81A	*EXPLOIT*
|     	F67B1561-9F99-5BDE-8EDF-EA45E59D6039	7.8	https://vulners.com/githubexploit/F67B1561-9F99-5BDE-8EDF-EA45E59D6039	*EXPLOIT*
|     	F3F45FED-B716-5B56-9880-08CA523A08B7	7.8	https://vulners.com/githubexploit/F3F45FED-B716-5B56-9880-08CA523A08B7	*EXPLOIT*
|     	F122E89C-8C48-5222-B7BB-59C31560BC1B	7.8	https://vulners.com/githubexploit/F122E89C-8C48-5222-B7BB-59C31560BC1B	*EXPLOIT*
|     	EDB-ID:50808	7.8	https://vulners.com/exploitdb/EDB-ID:50808	*EXPLOIT*
|     	EDB-ID:47170	7.8	https://vulners.com/exploitdb/EDB-ID:47170	*EXPLOIT*
|     	EDB-ID:47168	7.8	https://vulners.com/exploitdb/EDB-ID:47168	*EXPLOIT*
|     	EDB-ID:47067	7.8	https://vulners.com/exploitdb/EDB-ID:47067	*EXPLOIT*
|     	EDB-ID:45553	7.8	https://vulners.com/exploitdb/EDB-ID:45553	*EXPLOIT*
|     	EDB-ID:45516	7.8	https://vulners.com/exploitdb/EDB-ID:45516	*EXPLOIT*
|     	EDB-ID:44806	7.8	https://vulners.com/exploitdb/EDB-ID:44806	*EXPLOIT*
|     	EDB-ID:44696	7.8	https://vulners.com/exploitdb/EDB-ID:44696	*EXPLOIT*
|     	EDB-ID:44654	7.8	https://vulners.com/exploitdb/EDB-ID:44654	*EXPLOIT*
|     	EDB-ID:44205	7.8	https://vulners.com/exploitdb/EDB-ID:44205	*EXPLOIT*
|     	EDB-ID:44053	7.8	https://vulners.com/exploitdb/EDB-ID:44053	*EXPLOIT*
|     	EDB-ID:44049	7.8	https://vulners.com/exploitdb/EDB-ID:44049	*EXPLOIT*
|     	EDB-ID:43234	7.8	https://vulners.com/exploitdb/EDB-ID:43234	*EXPLOIT*
|     	EDB-ID:42887	7.8	https://vulners.com/exploitdb/EDB-ID:42887	*EXPLOIT*
|     	EDB-ID:42275	7.8	https://vulners.com/exploitdb/EDB-ID:42275	*EXPLOIT*
|     	EDB-ID:41995	7.8	https://vulners.com/exploitdb/EDB-ID:41995	*EXPLOIT*
|     	EDB-ID:41994	7.8	https://vulners.com/exploitdb/EDB-ID:41994	*EXPLOIT*
|     	EDB-ID:41458	7.8	https://vulners.com/exploitdb/EDB-ID:41458	*EXPLOIT*
|     	EDB-ID:41457	7.8	https://vulners.com/exploitdb/EDB-ID:41457	*EXPLOIT*
|     	EDB-ID:40489	7.8	https://vulners.com/exploitdb/EDB-ID:40489	*EXPLOIT*
|     	EDB-ID:40435	7.8	https://vulners.com/exploitdb/EDB-ID:40435	*EXPLOIT*
|     	EDB-ID:40003	7.8	https://vulners.com/exploitdb/EDB-ID:40003	*EXPLOIT*
|     	EDB-ID:39669	7.8	https://vulners.com/exploitdb/EDB-ID:39669	*EXPLOIT*
|     	EDB-ID:39277	7.8	https://vulners.com/exploitdb/EDB-ID:39277	*EXPLOIT*
|     	EDB-ID:37293	7.8	https://vulners.com/exploitdb/EDB-ID:37293	*EXPLOIT*
|     	EDB-ID:37292	7.8	https://vulners.com/exploitdb/EDB-ID:37292	*EXPLOIT*
|     	EDB-ID:36266	7.8	https://vulners.com/exploitdb/EDB-ID:36266	*EXPLOIT*
|     	EB24215E-691D-5021-A9EA-DD51BE5B88A7	7.8	https://vulners.com/githubexploit/EB24215E-691D-5021-A9EA-DD51BE5B88A7	*EXPLOIT*
|     	EAE6E8A6-C842-512C-BBF8-905BB499529B	7.8	https://vulners.com/githubexploit/EAE6E8A6-C842-512C-BBF8-905BB499529B	*EXPLOIT*
|     	E512369B-4B70-5546-9049-78495817DFD3	7.8	https://vulners.com/githubexploit/E512369B-4B70-5546-9049-78495817DFD3	*EXPLOIT*
|     	E4C46A03-D265-51D4-AF1A-A576FA76B6B3	7.8	https://vulners.com/githubexploit/E4C46A03-D265-51D4-AF1A-A576FA76B6B3	*EXPLOIT*
|     	E486E79A-CFAD-56DE-B622-D64E700A822C	7.8	https://vulners.com/githubexploit/E486E79A-CFAD-56DE-B622-D64E700A822C	*EXPLOIT*
|     	E15E347F-A26F-5F55-AA97-650439269AD6	7.8	https://vulners.com/githubexploit/E15E347F-A26F-5F55-AA97-650439269AD6	*EXPLOIT*
|     	DFF99976-FE50-580B-8456-0C46E6F1AA69	7.8	https://vulners.com/githubexploit/DFF99976-FE50-580B-8456-0C46E6F1AA69	*EXPLOIT*
|     	DFCB8D82-860E-5D5D-ABA6-50C59B69936B	7.8	https://vulners.com/githubexploit/DFCB8D82-860E-5D5D-ABA6-50C59B69936B	*EXPLOIT*
|     	DE6CA7B3-18E2-5BFF-A971-D7B76F77EB65	7.8	https://vulners.com/githubexploit/DE6CA7B3-18E2-5BFF-A971-D7B76F77EB65	*EXPLOIT*
|     	DD445CDD-3049-55A7-BD3E-344AC2FD85BC	7.8	https://vulners.com/githubexploit/DD445CDD-3049-55A7-BD3E-344AC2FD85BC	*EXPLOIT*
|     	DC3905DC-182D-514C-A689-6B8E9D2771E0	7.8	https://vulners.com/githubexploit/DC3905DC-182D-514C-A689-6B8E9D2771E0	*EXPLOIT*
|     	D5DA0DC0-04A9-5A7E-9454-2F6D05E8FFE8	7.8	https://vulners.com/githubexploit/D5DA0DC0-04A9-5A7E-9454-2F6D05E8FFE8	*EXPLOIT*
|     	D31E1899-8B29-5739-AFF2-F7C0035CCFDF	7.8	https://vulners.com/githubexploit/D31E1899-8B29-5739-AFF2-F7C0035CCFDF	*EXPLOIT*
|     	D144D690-C331-5457-B5B3-92AE9A0109D6	7.8	https://vulners.com/githubexploit/D144D690-C331-5457-B5B3-92AE9A0109D6	*EXPLOIT*
|     	CVE-2024-39291	7.8	https://vulners.com/cve/CVE-2024-39291
|     	CVE-2024-39277	7.8	https://vulners.com/cve/CVE-2024-39277
|     	CVE-2024-38667	7.8	https://vulners.com/cve/CVE-2024-38667
|     	CVE-2024-38664	7.8	https://vulners.com/cve/CVE-2024-38664
|     	CVE-2024-36477	7.8	https://vulners.com/cve/CVE-2024-36477
|     	CVE-2024-27018	7.8	https://vulners.com/cve/CVE-2024-27018
|     	CVE-2024-26952	7.8	https://vulners.com/cve/CVE-2024-26952
|     	CVE-2024-26933	7.8	https://vulners.com/cve/CVE-2024-26933
|     	CVE-2024-26930	7.8	https://vulners.com/cve/CVE-2024-26930
|     	CVE-2024-26929	7.8	https://vulners.com/cve/CVE-2024-26929
|     	CVE-2024-26913	7.8	https://vulners.com/cve/CVE-2024-26913
|     	CVE-2024-26907	7.8	https://vulners.com/cve/CVE-2024-26907
|     	CVE-2024-26898	7.8	https://vulners.com/cve/CVE-2024-26898
|     	CVE-2024-26883	7.8	https://vulners.com/cve/CVE-2024-26883
|     	CVE-2024-26882	7.8	https://vulners.com/cve/CVE-2024-26882
|     	CVE-2024-26598	7.8	https://vulners.com/cve/CVE-2024-26598
|     	CVE-2024-26588	7.8	https://vulners.com/cve/CVE-2024-26588
|     	CVE-2024-26581	7.8	https://vulners.com/cve/CVE-2024-26581
|     	CVE-2024-22705	7.8	https://vulners.com/cve/CVE-2024-22705
|     	CVE-2024-21803	7.8	https://vulners.com/cve/CVE-2024-21803
|     	CVE-2024-0646	7.8	https://vulners.com/cve/CVE-2024-0646
|     	CVE-2024-0562	7.8	https://vulners.com/cve/CVE-2024-0562
|     	CVE-2023-6932	7.8	https://vulners.com/cve/CVE-2023-6932
|     	CVE-2023-6040	7.8	https://vulners.com/cve/CVE-2023-6040
|     	CVE-2023-5633	7.8	https://vulners.com/cve/CVE-2023-5633
|     	CVE-2023-5345	7.8	https://vulners.com/cve/CVE-2023-5345
|     	CVE-2023-52760	7.8	https://vulners.com/cve/CVE-2023-52760
|     	CVE-2023-52752	7.8	https://vulners.com/cve/CVE-2023-52752
|     	CVE-2023-52457	7.8	https://vulners.com/cve/CVE-2023-52457
|     	CVE-2023-52445	7.8	https://vulners.com/cve/CVE-2023-52445
|     	CVE-2023-52436	7.8	https://vulners.com/cve/CVE-2023-52436
|     	CVE-2023-51042	7.8	https://vulners.com/cve/CVE-2023-51042
|     	CVE-2023-4921	7.8	https://vulners.com/cve/CVE-2023-4921
|     	CVE-2023-4623	7.8	https://vulners.com/cve/CVE-2023-4623
|     	CVE-2023-45898	7.8	https://vulners.com/cve/CVE-2023-45898
|     	CVE-2023-42753	7.8	https://vulners.com/cve/CVE-2023-42753
|     	CVE-2023-4244	7.8	https://vulners.com/cve/CVE-2023-4244
|     	CVE-2023-4147	7.8	https://vulners.com/cve/CVE-2023-4147
|     	CVE-2023-40283	7.8	https://vulners.com/cve/CVE-2023-40283
|     	CVE-2023-3777	7.8	https://vulners.com/cve/CVE-2023-3777
|     	CVE-2023-3776	7.8	https://vulners.com/cve/CVE-2023-3776
|     	CVE-2023-3611	7.8	https://vulners.com/cve/CVE-2023-3611
|     	CVE-2023-31436	7.8	https://vulners.com/cve/CVE-2023-31436
|     	CVE-2023-3111	7.8	https://vulners.com/cve/CVE-2023-3111
|     	CVE-2023-26242	7.8	https://vulners.com/cve/CVE-2023-26242
|     	CVE-2023-2598	7.8	https://vulners.com/cve/CVE-2023-2598
|     	CVE-2023-23559	7.8	https://vulners.com/cve/CVE-2023-23559
|     	CVE-2023-22995	7.8	https://vulners.com/cve/CVE-2023-22995
|     	CVE-2023-2176	7.8	https://vulners.com/cve/CVE-2023-2176
|     	CVE-2023-2124	7.8	https://vulners.com/cve/CVE-2023-2124
|     	CVE-2023-2008	7.8	https://vulners.com/cve/CVE-2023-2008
|     	CVE-2023-2007	7.8	https://vulners.com/cve/CVE-2023-2007
|     	CVE-2023-1829	7.8	https://vulners.com/cve/CVE-2023-1829
|     	CVE-2023-1670	7.8	https://vulners.com/cve/CVE-2023-1670
|     	CVE-2023-1252	7.8	https://vulners.com/cve/CVE-2023-1252
|     	CVE-2023-1118	7.8	https://vulners.com/cve/CVE-2023-1118
|     	CVE-2023-0240	7.8	https://vulners.com/cve/CVE-2023-0240
|     	CVE-2023-0030	7.8	https://vulners.com/cve/CVE-2023-0030
|     	CVE-2022-48670	7.8	https://vulners.com/cve/CVE-2022-48670
|     	CVE-2022-48655	7.8	https://vulners.com/cve/CVE-2022-48655
|     	CVE-2022-48626	7.8	https://vulners.com/cve/CVE-2022-48626
|     	CVE-2022-48425	7.8	https://vulners.com/cve/CVE-2022-48425
|     	CVE-2022-48423	7.8	https://vulners.com/cve/CVE-2022-48423
|     	CVE-2022-4744	7.8	https://vulners.com/cve/CVE-2022-4744
|     	CVE-2022-45934	7.8	https://vulners.com/cve/CVE-2022-45934
|     	CVE-2022-4378	7.8	https://vulners.com/cve/CVE-2022-4378
|     	CVE-2022-4139	7.8	https://vulners.com/cve/CVE-2022-4139
|     	CVE-2022-4095	7.8	https://vulners.com/cve/CVE-2022-4095
|     	CVE-2022-3977	7.8	https://vulners.com/cve/CVE-2022-3977
|     	CVE-2022-36123	7.8	https://vulners.com/cve/CVE-2022-36123
|     	CVE-2022-3577	7.8	https://vulners.com/cve/CVE-2022-3577
|     	CVE-2022-3565	7.8	https://vulners.com/cve/CVE-2022-3565
|     	CVE-2022-3424	7.8	https://vulners.com/cve/CVE-2022-3424
|     	CVE-2022-32981	7.8	https://vulners.com/cve/CVE-2022-32981
|     	CVE-2022-3239	7.8	https://vulners.com/cve/CVE-2022-3239
|     	CVE-2022-3238	7.8	https://vulners.com/cve/CVE-2022-3238
|     	CVE-2022-3170	7.8	https://vulners.com/cve/CVE-2022-3170
|     	CVE-2022-30594	7.8	https://vulners.com/cve/CVE-2022-30594
|     	CVE-2022-29968	7.8	https://vulners.com/cve/CVE-2022-29968
|     	CVE-2022-2978	7.8	https://vulners.com/cve/CVE-2022-2978
|     	CVE-2022-2977	7.8	https://vulners.com/cve/CVE-2022-2977
|     	CVE-2022-2964	7.8	https://vulners.com/cve/CVE-2022-2964
|     	CVE-2022-29581	7.8	https://vulners.com/cve/CVE-2022-29581
|     	CVE-2022-2938	7.8	https://vulners.com/cve/CVE-2022-2938
|     	CVE-2022-28390	7.8	https://vulners.com/cve/CVE-2022-28390
|     	CVE-2022-27666	7.8	https://vulners.com/cve/CVE-2022-27666
|     	CVE-2022-26490	7.8	https://vulners.com/cve/CVE-2022-26490
|     	CVE-2022-2639	7.8	https://vulners.com/cve/CVE-2022-2639
|     	CVE-2022-2588	7.8	https://vulners.com/cve/CVE-2022-2588
|     	CVE-2022-2586	7.8	https://vulners.com/cve/CVE-2022-2586
|     	CVE-2022-25265	7.8	https://vulners.com/cve/CVE-2022-25265
|     	CVE-2022-24958	7.8	https://vulners.com/cve/CVE-2022-24958
|     	CVE-2022-1998	7.8	https://vulners.com/cve/CVE-2022-1998
|     	CVE-2022-1976	7.8	https://vulners.com/cve/CVE-2022-1976
|     	CVE-2022-1943	7.8	https://vulners.com/cve/CVE-2022-1943
|     	CVE-2022-1882	7.8	https://vulners.com/cve/CVE-2022-1882
|     	CVE-2022-1786	7.8	https://vulners.com/cve/CVE-2022-1786
|     	CVE-2022-1679	7.8	https://vulners.com/cve/CVE-2022-1679
|     	CVE-2022-1652	7.8	https://vulners.com/cve/CVE-2022-1652
|     	CVE-2022-1419	7.8	https://vulners.com/cve/CVE-2022-1419
|     	CVE-2022-1158	7.8	https://vulners.com/cve/CVE-2022-1158
|     	CVE-2022-1116	7.8	https://vulners.com/cve/CVE-2022-1116
|     	CVE-2022-1011	7.8	https://vulners.com/cve/CVE-2022-1011
|     	CVE-2022-0998	7.8	https://vulners.com/cve/CVE-2022-0998
|     	CVE-2022-0995	7.8	https://vulners.com/cve/CVE-2022-0995
|     	CVE-2022-0847	7.8	https://vulners.com/cve/CVE-2022-0847
|     	CVE-2022-0646	7.8	https://vulners.com/cve/CVE-2022-0646
|     	CVE-2022-0516	7.8	https://vulners.com/cve/CVE-2022-0516
|     	CVE-2022-0500	7.8	https://vulners.com/cve/CVE-2022-0500
|     	CVE-2022-0492	7.8	https://vulners.com/cve/CVE-2022-0492
|     	CVE-2022-0330	7.8	https://vulners.com/cve/CVE-2022-0330
|     	CVE-2021-47571	7.8	https://vulners.com/cve/CVE-2021-47571
|     	CVE-2021-47521	7.8	https://vulners.com/cve/CVE-2021-47521
|     	CVE-2021-47520	7.8	https://vulners.com/cve/CVE-2021-47520
|     	CVE-2021-47198	7.8	https://vulners.com/cve/CVE-2021-47198
|     	CVE-2021-47194	7.8	https://vulners.com/cve/CVE-2021-47194
|     	CVE-2021-46936	7.8	https://vulners.com/cve/CVE-2021-46936
|     	CVE-2021-45469	7.8	https://vulners.com/cve/CVE-2021-45469
|     	CVE-2021-42252	7.8	https://vulners.com/cve/CVE-2021-42252
|     	CVE-2021-42008	7.8	https://vulners.com/cve/CVE-2021-42008
|     	CVE-2021-4197	7.8	https://vulners.com/cve/CVE-2021-4197
|     	CVE-2021-41864	7.8	https://vulners.com/cve/CVE-2021-41864
|     	CVE-2021-4037	7.8	https://vulners.com/cve/CVE-2021-4037
|     	CVE-2021-4028	7.8	https://vulners.com/cve/CVE-2021-4028
|     	CVE-2021-3847	7.8	https://vulners.com/cve/CVE-2021-3847
|     	CVE-2021-38166	7.8	https://vulners.com/cve/CVE-2021-38166
|     	CVE-2021-38160	7.8	https://vulners.com/cve/CVE-2021-38160
|     	CVE-2021-3760	7.8	https://vulners.com/cve/CVE-2021-3760
|     	CVE-2021-37576	7.8	https://vulners.com/cve/CVE-2021-37576
|     	CVE-2021-3715	7.8	https://vulners.com/cve/CVE-2021-3715
|     	CVE-2021-3612	7.8	https://vulners.com/cve/CVE-2021-3612
|     	CVE-2021-34866	7.8	https://vulners.com/cve/CVE-2021-34866
|     	CVE-2021-3483	7.8	https://vulners.com/cve/CVE-2021-3483
|     	CVE-2021-3444	7.8	https://vulners.com/cve/CVE-2021-3444
|     	CVE-2021-3347	7.8	https://vulners.com/cve/CVE-2021-3347
|     	CVE-2021-33034	7.8	https://vulners.com/cve/CVE-2021-33034
|     	CVE-2021-33033	7.8	https://vulners.com/cve/CVE-2021-33033
|     	CVE-2021-29154	7.8	https://vulners.com/cve/CVE-2021-29154
|     	CVE-2021-28952	7.8	https://vulners.com/cve/CVE-2021-28952
|     	CVE-2021-27365	7.8	https://vulners.com/cve/CVE-2021-27365
|     	CVE-2021-23134	7.8	https://vulners.com/cve/CVE-2021-23134
|     	CVE-2021-20268	7.8	https://vulners.com/cve/CVE-2021-20268
|     	CVE-2021-20226	7.8	https://vulners.com/cve/CVE-2021-20226
|     	CVE-2021-20194	7.8	https://vulners.com/cve/CVE-2021-20194
|     	CVE-2020-36385	7.8	https://vulners.com/cve/CVE-2020-36385
|     	CVE-2020-36313	7.8	https://vulners.com/cve/CVE-2020-36313
|     	CVE-2020-35519	7.8	https://vulners.com/cve/CVE-2020-35519
|     	CVE-2020-29661	7.8	https://vulners.com/cve/CVE-2020-29661
|     	CVE-2020-27815	7.8	https://vulners.com/cve/CVE-2020-27815
|     	CVE-2020-27786	7.8	https://vulners.com/cve/CVE-2020-27786
|     	CVE-2020-25671	7.8	https://vulners.com/cve/CVE-2020-25671
|     	CVE-2020-25670	7.8	https://vulners.com/cve/CVE-2020-25670
|     	CVE-2020-25669	7.8	https://vulners.com/cve/CVE-2020-25669
|     	CVE-2020-14386	7.8	https://vulners.com/cve/CVE-2020-14386
|     	CVE-2020-14381	7.8	https://vulners.com/cve/CVE-2020-14381
|     	CVE-2020-14356	7.8	https://vulners.com/cve/CVE-2020-14356
|     	CVE-2020-14351	7.8	https://vulners.com/cve/CVE-2020-14351
|     	CVE-2020-13974	7.8	https://vulners.com/cve/CVE-2020-13974
|     	CVE-2020-12657	7.8	https://vulners.com/cve/CVE-2020-12657
|     	CVE-2020-12653	7.8	https://vulners.com/cve/CVE-2020-12653
|     	CVE-2020-11725	7.8	https://vulners.com/cve/CVE-2020-11725
|     	CVE-2020-10757	7.8	https://vulners.com/cve/CVE-2020-10757
|     	CVE-2019-7221	7.8	https://vulners.com/cve/CVE-2019-7221
|     	CVE-2019-25045	7.8	https://vulners.com/cve/CVE-2019-25045
|     	CVE-2019-19816	7.8	https://vulners.com/cve/CVE-2019-19816
|     	CVE-2019-19543	7.8	https://vulners.com/cve/CVE-2019-19543
|     	CVE-2019-19448	7.8	https://vulners.com/cve/CVE-2019-19448
|     	CVE-2019-19447	7.8	https://vulners.com/cve/CVE-2019-19447
|     	CVE-2019-19377	7.8	https://vulners.com/cve/CVE-2019-19377
|     	CVE-2019-19252	7.8	https://vulners.com/cve/CVE-2019-19252
|     	CVE-2019-19241	7.8	https://vulners.com/cve/CVE-2019-19241
|     	CVE-2019-18675	7.8	https://vulners.com/cve/CVE-2019-18675
|     	CVE-2019-15927	7.8	https://vulners.com/cve/CVE-2019-15927
|     	CVE-2019-15117	7.8	https://vulners.com/cve/CVE-2019-15117
|     	CVE-2019-14835	7.8	https://vulners.com/cve/CVE-2019-14835
|     	CVE-2019-14816	7.8	https://vulners.com/cve/CVE-2019-14816
|     	CVE-2019-14814	7.8	https://vulners.com/cve/CVE-2019-14814
|     	CVE-2019-12456	7.8	https://vulners.com/cve/CVE-2019-12456
|     	CVE-2019-12454	7.8	https://vulners.com/cve/CVE-2019-12454
|     	CVE-2019-11487	7.8	https://vulners.com/cve/CVE-2019-11487
|     	CVE-2018-9568	7.8	https://vulners.com/cve/CVE-2018-9568
|     	CVE-2018-8822	7.8	https://vulners.com/cve/CVE-2018-8822
|     	CVE-2018-8781	7.8	https://vulners.com/cve/CVE-2018-8781
|     	CVE-2018-6927	7.8	https://vulners.com/cve/CVE-2018-6927
|     	CVE-2018-6555	7.8	https://vulners.com/cve/CVE-2018-6555
|     	CVE-2018-5344	7.8	https://vulners.com/cve/CVE-2018-5344
|     	CVE-2018-5332	7.8	https://vulners.com/cve/CVE-2018-5332
|     	CVE-2018-25020	7.8	https://vulners.com/cve/CVE-2018-25020
|     	CVE-2018-25015	7.8	https://vulners.com/cve/CVE-2018-25015
|     	CVE-2018-20976	7.8	https://vulners.com/cve/CVE-2018-20976
|     	CVE-2018-20856	7.8	https://vulners.com/cve/CVE-2018-20856
|     	CVE-2018-20854	7.8	https://vulners.com/cve/CVE-2018-20854
|     	CVE-2018-19824	7.8	https://vulners.com/cve/CVE-2018-19824
|     	CVE-2018-18281	7.8	https://vulners.com/cve/CVE-2018-18281
|     	CVE-2018-16276	7.8	https://vulners.com/cve/CVE-2018-16276
|     	CVE-2018-14734	7.8	https://vulners.com/cve/CVE-2018-14734
|     	CVE-2018-14634	7.8	https://vulners.com/cve/CVE-2018-14634
|     	CVE-2018-13406	7.8	https://vulners.com/cve/CVE-2018-13406
|     	CVE-2018-13405	7.8	https://vulners.com/cve/CVE-2018-13405
|     	CVE-2018-12233	7.8	https://vulners.com/cve/CVE-2018-12233
|     	CVE-2018-10879	7.8	https://vulners.com/cve/CVE-2018-10879
|     	CVE-2018-10878	7.8	https://vulners.com/cve/CVE-2018-10878
|     	CVE-2018-10853	7.8	https://vulners.com/cve/CVE-2018-10853
|     	CVE-2018-10675	7.8	https://vulners.com/cve/CVE-2018-10675
|     	CVE-2017-9986	7.8	https://vulners.com/cve/CVE-2017-9986
|     	CVE-2017-9985	7.8	https://vulners.com/cve/CVE-2017-9985
|     	CVE-2017-9984	7.8	https://vulners.com/cve/CVE-2017-9984
|     	CVE-2017-9077	7.8	https://vulners.com/cve/CVE-2017-9077
|     	CVE-2017-9076	7.8	https://vulners.com/cve/CVE-2017-9076
|     	CVE-2017-9075	7.8	https://vulners.com/cve/CVE-2017-9075
|     	CVE-2017-9074	7.8	https://vulners.com/cve/CVE-2017-9074
|     	CVE-2017-8890	7.8	https://vulners.com/cve/CVE-2017-8890
|     	CVE-2017-8824	7.8	https://vulners.com/cve/CVE-2017-8824
|     	CVE-2017-7889	7.8	https://vulners.com/cve/CVE-2017-7889
|     	CVE-2017-7541	7.8	https://vulners.com/cve/CVE-2017-7541
|     	CVE-2017-7518	7.8	https://vulners.com/cve/CVE-2017-7518
|     	CVE-2017-7487	7.8	https://vulners.com/cve/CVE-2017-7487
|     	CVE-2017-7482	7.8	https://vulners.com/cve/CVE-2017-7482
|     	CVE-2017-7308	7.8	https://vulners.com/cve/CVE-2017-7308
|     	CVE-2017-7294	7.8	https://vulners.com/cve/CVE-2017-7294
|     	CVE-2017-7187	7.8	https://vulners.com/cve/CVE-2017-7187
|     	CVE-2017-7184	7.8	https://vulners.com/cve/CVE-2017-7184
|     	CVE-2017-6345	7.8	https://vulners.com/cve/CVE-2017-6345
|     	CVE-2017-6074	7.8	https://vulners.com/cve/CVE-2017-6074
|     	CVE-2017-5669	7.8	https://vulners.com/cve/CVE-2017-5669
|     	CVE-2017-2647	7.8	https://vulners.com/cve/CVE-2017-2647
|     	CVE-2017-18595	7.8	https://vulners.com/cve/CVE-2017-18595
|     	CVE-2017-18552	7.8	https://vulners.com/cve/CVE-2017-18552
|     	CVE-2017-18509	7.8	https://vulners.com/cve/CVE-2017-18509
|     	CVE-2017-18255	7.8	https://vulners.com/cve/CVE-2017-18255
|     	CVE-2017-18222	7.8	https://vulners.com/cve/CVE-2017-18222
|     	CVE-2017-18079	7.8	https://vulners.com/cve/CVE-2017-18079
|     	CVE-2017-17806	7.8	https://vulners.com/cve/CVE-2017-17806
|     	CVE-2017-17805	7.8	https://vulners.com/cve/CVE-2017-17805
|     	CVE-2017-17450	7.8	https://vulners.com/cve/CVE-2017-17450
|     	CVE-2017-17448	7.8	https://vulners.com/cve/CVE-2017-17448
|     	CVE-2017-16939	7.8	https://vulners.com/cve/CVE-2017-16939
|     	CVE-2017-16526	7.8	https://vulners.com/cve/CVE-2017-16526
|     	CVE-2017-15868	7.8	https://vulners.com/cve/CVE-2017-15868
|     	CVE-2017-15649	7.8	https://vulners.com/cve/CVE-2017-15649
|     	CVE-2017-15115	7.8	https://vulners.com/cve/CVE-2017-15115
|     	CVE-2017-11473	7.8	https://vulners.com/cve/CVE-2017-11473
|     	CVE-2017-11176	7.8	https://vulners.com/cve/CVE-2017-11176
|     	CVE-2017-10663	7.8	https://vulners.com/cve/CVE-2017-10663
|     	CVE-2017-10662	7.8	https://vulners.com/cve/CVE-2017-10662
|     	CVE-2017-1000379	7.8	https://vulners.com/cve/CVE-2017-1000379
|     	CVE-2017-1000365	7.8	https://vulners.com/cve/CVE-2017-1000365
|     	CVE-2017-1000363	7.8	https://vulners.com/cve/CVE-2017-1000363
|     	CVE-2017-1000253	7.8	https://vulners.com/cve/CVE-2017-1000253
|     	CVE-2017-1000111	7.8	https://vulners.com/cve/CVE-2017-1000111
|     	CVE-2016-9794	7.8	https://vulners.com/cve/CVE-2016-9794
|     	CVE-2016-9793	7.8	https://vulners.com/cve/CVE-2016-9793
|     	CVE-2016-9755	7.8	https://vulners.com/cve/CVE-2016-9755
|     	CVE-2016-9754	7.8	https://vulners.com/cve/CVE-2016-9754
|     	CVE-2016-9084	7.8	https://vulners.com/cve/CVE-2016-9084
|     	CVE-2016-9083	7.8	https://vulners.com/cve/CVE-2016-9083
|     	CVE-2016-8655	7.8	https://vulners.com/cve/CVE-2016-8655
|     	CVE-2016-8632	7.8	https://vulners.com/cve/CVE-2016-8632
|     	CVE-2016-7913	7.8	https://vulners.com/cve/CVE-2016-7913
|     	CVE-2016-7911	7.8	https://vulners.com/cve/CVE-2016-7911
|     	CVE-2016-7910	7.8	https://vulners.com/cve/CVE-2016-7910
|     	CVE-2016-7425	7.8	https://vulners.com/cve/CVE-2016-7425
|     	CVE-2016-5870	7.8	https://vulners.com/cve/CVE-2016-5870
|     	CVE-2016-5829	7.8	https://vulners.com/cve/CVE-2016-5829
|     	CVE-2016-5828	7.8	https://vulners.com/cve/CVE-2016-5828
|     	CVE-2016-5342	7.8	https://vulners.com/cve/CVE-2016-5342
|     	CVE-2016-5340	7.8	https://vulners.com/cve/CVE-2016-5340
|     	CVE-2016-5195	7.8	https://vulners.com/cve/CVE-2016-5195
|     	CVE-2016-4997	7.8	https://vulners.com/cve/CVE-2016-4997
|     	CVE-2016-4913	7.8	https://vulners.com/cve/CVE-2016-4913
|     	CVE-2016-4805	7.8	https://vulners.com/cve/CVE-2016-4805
|     	CVE-2016-4565	7.8	https://vulners.com/cve/CVE-2016-4565
|     	CVE-2016-3672	7.8	https://vulners.com/cve/CVE-2016-3672
|     	CVE-2016-3070	7.8	https://vulners.com/cve/CVE-2016-3070
|     	CVE-2016-2854	7.8	https://vulners.com/cve/CVE-2016-2854
|     	CVE-2016-2853	7.8	https://vulners.com/cve/CVE-2016-2853
|     	CVE-2016-2143	7.8	https://vulners.com/cve/CVE-2016-2143
|     	CVE-2016-2068	7.8	https://vulners.com/cve/CVE-2016-2068
|     	CVE-2016-2067	7.8	https://vulners.com/cve/CVE-2016-2067
|     	CVE-2016-2066	7.8	https://vulners.com/cve/CVE-2016-2066
|     	CVE-2016-2065	7.8	https://vulners.com/cve/CVE-2016-2065
|     	CVE-2016-2064	7.8	https://vulners.com/cve/CVE-2016-2064
|     	CVE-2016-2063	7.8	https://vulners.com/cve/CVE-2016-2063
|     	CVE-2016-2062	7.8	https://vulners.com/cve/CVE-2016-2062
|     	CVE-2016-2061	7.8	https://vulners.com/cve/CVE-2016-2061
|     	CVE-2016-1583	7.8	https://vulners.com/cve/CVE-2016-1583
|     	CVE-2016-1576	7.8	https://vulners.com/cve/CVE-2016-1576
|     	CVE-2016-1575	7.8	https://vulners.com/cve/CVE-2016-1575
|     	CVE-2016-10907	7.8	https://vulners.com/cve/CVE-2016-10907
|     	CVE-2016-10905	7.8	https://vulners.com/cve/CVE-2016-10905
|     	CVE-2016-10044	7.8	https://vulners.com/cve/CVE-2016-10044
|     	CVE-2016-0758	7.8	https://vulners.com/cve/CVE-2016-0758
|     	CVE-2016-0728	7.8	https://vulners.com/cve/CVE-2016-0728
|     	CVE-2015-8967	7.8	https://vulners.com/cve/CVE-2015-8967
|     	CVE-2015-8966	7.8	https://vulners.com/cve/CVE-2015-8966
|     	CVE-2015-8539	7.8	https://vulners.com/cve/CVE-2015-8539
|     	CVE-2015-5364	7.8	https://vulners.com/cve/CVE-2015-5364
|     	CVE-2015-4003	7.8	https://vulners.com/cve/CVE-2015-4003
|     	CVE-2015-3288	7.8	https://vulners.com/cve/CVE-2015-3288
|     	CVE-2015-1465	7.8	https://vulners.com/cve/CVE-2015-1465
|     	CVE-2015-1328	7.8	https://vulners.com/cve/CVE-2015-1328
|     	CVE-2015-0571	7.8	https://vulners.com/cve/CVE-2015-0571
|     	CVE-2015-0570	7.8	https://vulners.com/cve/CVE-2015-0570
|     	CVE-2015-0569	7.8	https://vulners.com/cve/CVE-2015-0569
|     	CVE-2015-0568	7.8	https://vulners.com/cve/CVE-2015-0568
|     	CVE-2014-9922	7.8	https://vulners.com/cve/CVE-2014-9922
|     	CVE-2014-9904	7.8	https://vulners.com/cve/CVE-2014-9904
|     	CVE-2014-9888	7.8	https://vulners.com/cve/CVE-2014-9888
|     	CVE-2014-9870	7.8	https://vulners.com/cve/CVE-2014-9870
|     	CVE-2014-9803	7.8	https://vulners.com/cve/CVE-2014-9803
|     	CVE-2014-9322	7.8	https://vulners.com/cve/CVE-2014-9322
|     	CVE-2014-8369	7.8	https://vulners.com/cve/CVE-2014-8369
|     	CVE-2014-7826	7.8	https://vulners.com/cve/CVE-2014-7826
|     	CVE-2014-7825	7.8	https://vulners.com/cve/CVE-2014-7825
|     	CVE-2014-7145	7.8	https://vulners.com/cve/CVE-2014-7145
|     	CVE-2014-6417	7.8	https://vulners.com/cve/CVE-2014-6417
|     	CVE-2014-6416	7.8	https://vulners.com/cve/CVE-2014-6416
|     	CVE-2013-7445	7.8	https://vulners.com/cve/CVE-2013-7445
|     	CEF1CF82-EB41-5011-81A4-38FBB4B05FCF	7.8	https://vulners.com/githubexploit/CEF1CF82-EB41-5011-81A4-38FBB4B05FCF	*EXPLOIT*
|     	CAF813CE-0A25-5EA7-93B7-BEA8325E0296	7.8	https://vulners.com/githubexploit/CAF813CE-0A25-5EA7-93B7-BEA8325E0296	*EXPLOIT*
|     	CA758B0E-756E-5AC0-B536-57A87282F901	7.8	https://vulners.com/githubexploit/CA758B0E-756E-5AC0-B536-57A87282F901	*EXPLOIT*
|     	C77E4DCD-6F02-5B59-A70C-5632A7207285	7.8	https://vulners.com/githubexploit/C77E4DCD-6F02-5B59-A70C-5632A7207285	*EXPLOIT*
|     	B5E6CCAE-6F85-50D3-A016-7CA8BDF4385C	7.8	https://vulners.com/githubexploit/B5E6CCAE-6F85-50D3-A016-7CA8BDF4385C	*EXPLOIT*
|     	B573163B-4BBC-5984-8941-EC17F24348B1	7.8	https://vulners.com/githubexploit/B573163B-4BBC-5984-8941-EC17F24348B1	*EXPLOIT*
|     	ABF4B7F4-3AAC-58C8-B546-FC4ED5C0827A	7.8	https://vulners.com/githubexploit/ABF4B7F4-3AAC-58C8-B546-FC4ED5C0827A	*EXPLOIT*
|     	A714BDDC-3F3E-5762-8D54-A97B7FAD41C4	7.8	https://vulners.com/githubexploit/A714BDDC-3F3E-5762-8D54-A97B7FAD41C4	*EXPLOIT*
|     	A404C02A-61C8-53DD-9BC0-EDE503C19C2C	7.8	https://vulners.com/githubexploit/A404C02A-61C8-53DD-9BC0-EDE503C19C2C	*EXPLOIT*
|     	A3B770BE-1A12-5CD4-A06F-EE317094975F	7.8	https://vulners.com/githubexploit/A3B770BE-1A12-5CD4-A06F-EE317094975F	*EXPLOIT*
|     	A249241C-8F8A-5640-BDDD-E66E8A9E48B8	7.8	https://vulners.com/githubexploit/A249241C-8F8A-5640-BDDD-E66E8A9E48B8	*EXPLOIT*
|     	9FDDDA87-06DB-51EC-ADC5-5009B1A6F124	7.8	https://vulners.com/githubexploit/9FDDDA87-06DB-51EC-ADC5-5009B1A6F124	*EXPLOIT*
|     	99591F54-921C-5A13-A3D1-598ADB33A910	7.8	https://vulners.com/githubexploit/99591F54-921C-5A13-A3D1-598ADB33A910	*EXPLOIT*
|     	9840D3EA-61BB-54B6-904A-09DAD15F24DC	7.8	https://vulners.com/githubexploit/9840D3EA-61BB-54B6-904A-09DAD15F24DC	*EXPLOIT*
|     	94F62977-858D-545B-8982-298E6008661F	7.8	https://vulners.com/githubexploit/94F62977-858D-545B-8982-298E6008661F	*EXPLOIT*
|     	926D289B-3E6E-5186-8511-1F7D832A8CAD	7.8	https://vulners.com/githubexploit/926D289B-3E6E-5186-8511-1F7D832A8CAD	*EXPLOIT*
|     	8F8D2F72-BC08-5672-91A1-523A5EF7D1AA	7.8	https://vulners.com/githubexploit/8F8D2F72-BC08-5672-91A1-523A5EF7D1AA	*EXPLOIT*
|     	8EA1B3FF-A26D-52F7-BC2E-6FCB3115088F	7.8	https://vulners.com/githubexploit/8EA1B3FF-A26D-52F7-BC2E-6FCB3115088F	*EXPLOIT*
|     	8B409CA3-4DAE-57CA-B491-B4590CB1E0FB	7.8	https://vulners.com/githubexploit/8B409CA3-4DAE-57CA-B491-B4590CB1E0FB	*EXPLOIT*
|     	7E61A61C-009B-5340-A95B-22EC79327D85	7.8	https://vulners.com/githubexploit/7E61A61C-009B-5340-A95B-22EC79327D85	*EXPLOIT*
|     	79F34E05-6833-5741-988E-66DCB1C4773B	7.8	https://vulners.com/githubexploit/79F34E05-6833-5741-988E-66DCB1C4773B	*EXPLOIT*
|     	756BB098-22EB-5E92-B463-48DFBD684FF4	7.8	https://vulners.com/githubexploit/756BB098-22EB-5E92-B463-48DFBD684FF4	*EXPLOIT*
|     	71F849A9-2312-5FE0-83E4-C6DE378661BA	7.8	https://vulners.com/githubexploit/71F849A9-2312-5FE0-83E4-C6DE378661BA	*EXPLOIT*
|     	713989C9-D7B5-52B3-8C25-409C7D21D49C	7.8	https://vulners.com/githubexploit/713989C9-D7B5-52B3-8C25-409C7D21D49C	*EXPLOIT*
|     	707C38FA-F0B2-55CC-8D02-98EDBDDA27DB	7.8	https://vulners.com/githubexploit/707C38FA-F0B2-55CC-8D02-98EDBDDA27DB	*EXPLOIT*
|     	6A4924B0-9084-5B06-800E-6CFC4CAD5ABD	7.8	https://vulners.com/githubexploit/6A4924B0-9084-5B06-800E-6CFC4CAD5ABD	*EXPLOIT*
|     	68FB3CCC-E98B-5AB8-BB16-9661E947858E	7.8	https://vulners.com/githubexploit/68FB3CCC-E98B-5AB8-BB16-9661E947858E	*EXPLOIT*
|     	689C5F8A-6D6F-57E5-9B20-4E85EB67AE29	7.8	https://vulners.com/githubexploit/689C5F8A-6D6F-57E5-9B20-4E85EB67AE29	*EXPLOIT*
|     	687DFFBC-B653-59B8-BEB3-091905C4B176	7.8	https://vulners.com/githubexploit/687DFFBC-B653-59B8-BEB3-091905C4B176	*EXPLOIT*
|     	62EB9BB0-69C5-5D00-BDC0-0A5A09048007	7.8	https://vulners.com/githubexploit/62EB9BB0-69C5-5D00-BDC0-0A5A09048007	*EXPLOIT*
|     	5A75201B-3448-5168-A938-2E71C7C5F2CE	7.8	https://vulners.com/githubexploit/5A75201B-3448-5168-A938-2E71C7C5F2CE	*EXPLOIT*
|     	573EA352-758D-5155-A64A-F73425ABFF66	7.8	https://vulners.com/githubexploit/573EA352-758D-5155-A64A-F73425ABFF66	*EXPLOIT*
|     	52F5C576-65D5-5536-996C-AF0A19F01F5B	7.8	https://vulners.com/githubexploit/52F5C576-65D5-5536-996C-AF0A19F01F5B	*EXPLOIT*
|     	4FBF7A3B-F996-53AD-8ED5-4C2ED0283698	7.8	https://vulners.com/githubexploit/4FBF7A3B-F996-53AD-8ED5-4C2ED0283698	*EXPLOIT*
|     	4DB16743-1B3F-505A-B93A-4202272E3C44	7.8	https://vulners.com/githubexploit/4DB16743-1B3F-505A-B93A-4202272E3C44	*EXPLOIT*
|     	4ABDA4BC-28F3-5905-A32E-0ACA0226EDFB	7.8	https://vulners.com/githubexploit/4ABDA4BC-28F3-5905-A32E-0ACA0226EDFB	*EXPLOIT*
|     	492EFDCD-23F3-59CE-A969-F39D7FDC6A26	7.8	https://vulners.com/githubexploit/492EFDCD-23F3-59CE-A969-F39D7FDC6A26	*EXPLOIT*
|     	483F1274-762B-571F-949F-1C5067A06733	7.8	https://vulners.com/githubexploit/483F1274-762B-571F-949F-1C5067A06733	*EXPLOIT*
|     	3BEECAD0-0163-5C18-AE71-9DA3E0C552E8	7.8	https://vulners.com/githubexploit/3BEECAD0-0163-5C18-AE71-9DA3E0C552E8	*EXPLOIT*
|     	37814312-0D08-57BF-AD5C-6A3A5942457B	7.8	https://vulners.com/githubexploit/37814312-0D08-57BF-AD5C-6A3A5942457B	*EXPLOIT*
|     	3508DC5C-AD5C-508A-B78C-09B6AAEB232C	7.8	https://vulners.com/githubexploit/3508DC5C-AD5C-508A-B78C-09B6AAEB232C	*EXPLOIT*
|     	33212288-81D4-514F-8070-F223DCDD9BE7	7.8	https://vulners.com/githubexploit/33212288-81D4-514F-8070-F223DCDD9BE7	*EXPLOIT*
|     	32070F43-C6B7-5C66-89ED-2AE2F8A1DD03	7.8	https://vulners.com/githubexploit/32070F43-C6B7-5C66-89ED-2AE2F8A1DD03	*EXPLOIT*
|     	2F7AEDB6-2F5A-5DA7-A85D-746DEA4C7B0B	7.8	https://vulners.com/githubexploit/2F7AEDB6-2F5A-5DA7-A85D-746DEA4C7B0B	*EXPLOIT*
|     	2C78124E-4C73-5C91-B8BF-5079AC3CDFA1	7.8	https://vulners.com/githubexploit/2C78124E-4C73-5C91-B8BF-5079AC3CDFA1	*EXPLOIT*
|     	2B0BB40A-DBC8-5FA2-A5A4-2CEC4E0370AE	7.8	https://vulners.com/githubexploit/2B0BB40A-DBC8-5FA2-A5A4-2CEC4E0370AE	*EXPLOIT*
|     	29EFE8F7-2C59-5276-A537-A2F113EB230A	7.8	https://vulners.com/githubexploit/29EFE8F7-2C59-5276-A537-A2F113EB230A	*EXPLOIT*
|     	269A4547-2CD1-5B12-B3D0-9D78BE5431EC	7.8	https://vulners.com/githubexploit/269A4547-2CD1-5B12-B3D0-9D78BE5431EC	*EXPLOIT*
|     	268A62CE-1F6E-52C6-91A8-A2FD15C5EDDF	7.8	https://vulners.com/githubexploit/268A62CE-1F6E-52C6-91A8-A2FD15C5EDDF	*EXPLOIT*
|     	220DCD7F-4030-5588-A210-0F3E9577A02D	7.8	https://vulners.com/githubexploit/220DCD7F-4030-5588-A210-0F3E9577A02D	*EXPLOIT*
|     	1EF67F84-0CA0-5928-AE63-14B72E0B13B0	7.8	https://vulners.com/githubexploit/1EF67F84-0CA0-5928-AE63-14B72E0B13B0	*EXPLOIT*
|     	1DED936B-C668-5163-BDB3-81F7AC0611B0	7.8	https://vulners.com/githubexploit/1DED936B-C668-5163-BDB3-81F7AC0611B0	*EXPLOIT*
|     	1B2BCEB8-3417-5A73-9A00-015DD899A63F	7.8	https://vulners.com/githubexploit/1B2BCEB8-3417-5A73-9A00-015DD899A63F	*EXPLOIT*
|     	194848D4-3D8D-57C9-B93F-94A7FB834CC7	7.8	https://vulners.com/githubexploit/194848D4-3D8D-57C9-B93F-94A7FB834CC7	*EXPLOIT*
|     	191EA2A2-A596-5DE6-9E3C-16764FD31DB4	7.8	https://vulners.com/githubexploit/191EA2A2-A596-5DE6-9E3C-16764FD31DB4	*EXPLOIT*
|     	18A0ECF1-D699-5318-9A70-6E1902FB2119	7.8	https://vulners.com/githubexploit/18A0ECF1-D699-5318-9A70-6E1902FB2119	*EXPLOIT*
|     	1712473E-5B8C-5296-AFBC-FCA3A1908918	7.8	https://vulners.com/githubexploit/1712473E-5B8C-5296-AFBC-FCA3A1908918	*EXPLOIT*
|     	1337DAY-ID-39184	7.8	https://vulners.com/zdt/1337DAY-ID-39184	*EXPLOIT*
|     	1337DAY-ID-37662	7.8	https://vulners.com/zdt/1337DAY-ID-37662	*EXPLOIT*
|     	1337DAY-ID-37474	7.8	https://vulners.com/zdt/1337DAY-ID-37474	*EXPLOIT*
|     	1337DAY-ID-37461	7.8	https://vulners.com/zdt/1337DAY-ID-37461	*EXPLOIT*
|     	1337DAY-ID-37460	7.8	https://vulners.com/zdt/1337DAY-ID-37460	*EXPLOIT*
|     	1337DAY-ID-37458	7.8	https://vulners.com/zdt/1337DAY-ID-37458	*EXPLOIT*
|     	1337DAY-ID-35569	7.8	https://vulners.com/zdt/1337DAY-ID-35569	*EXPLOIT*
|     	1337DAY-ID-27013	7.8	https://vulners.com/zdt/1337DAY-ID-27013	*EXPLOIT*
|     	0E8CF22B-25CE-5700-80BD-048D8CAC746E	7.8	https://vulners.com/githubexploit/0E8CF22B-25CE-5700-80BD-048D8CAC746E	*EXPLOIT*
|     	0CEB4629-9B78-506E-A0CF-6E62D3203564	7.8	https://vulners.com/githubexploit/0CEB4629-9B78-506E-A0CF-6E62D3203564	*EXPLOIT*
|     	0AADD19A-EDB0-57B1-90A5-96CF733B31D8	7.8	https://vulners.com/githubexploit/0AADD19A-EDB0-57B1-90A5-96CF733B31D8	*EXPLOIT*
|     	0A92F6C1-7482-5379-9255-395EE9F50C04	7.8	https://vulners.com/githubexploit/0A92F6C1-7482-5379-9255-395EE9F50C04	*EXPLOIT*
|     	086F5A44-8ECA-5D00-9C60-EC88FF0A6024	7.8	https://vulners.com/githubexploit/086F5A44-8ECA-5D00-9C60-EC88FF0A6024	*EXPLOIT*
|     	0661150D-5F5B-5091-9137-D0F74B0B773E	7.8	https://vulners.com/githubexploit/0661150D-5F5B-5091-9137-D0F74B0B773E	*EXPLOIT*
|     	05772ECE-A777-5C16-8AE4-25697DCA9E81	7.8	https://vulners.com/githubexploit/05772ECE-A777-5C16-8AE4-25697DCA9E81	*EXPLOIT*
|     	CVE-2019-3900	7.7	https://vulners.com/cve/CVE-2019-3900
|     	CVE-2018-1000026	7.7	https://vulners.com/cve/CVE-2018-1000026
|     	EXPLOITPACK:68588737FAF0ED161AC1D6A540E77231	7.6	https://vulners.com/exploitpack/EXPLOITPACK:68588737FAF0ED161AC1D6A540E77231	*EXPLOIT*
|     	1337DAY-ID-29249	7.6	https://vulners.com/zdt/1337DAY-ID-29249	*EXPLOIT*
|     	EXPLOITPACK:669B77DE42FC41B271BD53577DECE916	7.5	https://vulners.com/exploitpack/EXPLOITPACK:669B77DE42FC41B271BD53577DECE916	*EXPLOIT*
|     	CVE-2023-6200	7.5	https://vulners.com/cve/CVE-2023-6200
|     	CVE-2023-45871	7.5	https://vulners.com/cve/CVE-2023-45871
|     	CVE-2023-39198	7.5	https://vulners.com/cve/CVE-2023-39198
|     	CVE-2023-3312	7.5	https://vulners.com/cve/CVE-2023-3312
|     	CVE-2023-1390	7.5	https://vulners.com/cve/CVE-2023-1390
|     	CVE-2023-0210	7.5	https://vulners.com/cve/CVE-2023-0210
|     	CVE-2023-0122	7.5	https://vulners.com/cve/CVE-2023-0122
|     	CVE-2022-43945	7.5	https://vulners.com/cve/CVE-2022-43945
|     	CVE-2022-4379	7.5	https://vulners.com/cve/CVE-2022-4379
|     	CVE-2022-36946	7.5	https://vulners.com/cve/CVE-2022-36946
|     	CVE-2022-1199	7.5	https://vulners.com/cve/CVE-2022-1199
|     	CVE-2021-45485	7.5	https://vulners.com/cve/CVE-2021-45485
|     	CVE-2021-38207	7.5	https://vulners.com/cve/CVE-2021-38207
|     	CVE-2021-38202	7.5	https://vulners.com/cve/CVE-2021-38202
|     	CVE-2021-34981	7.5	https://vulners.com/cve/CVE-2021-34981
|     	CVE-2020-25645	7.5	https://vulners.com/cve/CVE-2020-25645
|     	CVE-2020-1749	7.5	https://vulners.com/cve/CVE-2020-1749
|     	CVE-2019-19074	7.5	https://vulners.com/cve/CVE-2019-19074
|     	CVE-2019-19064	7.5	https://vulners.com/cve/CVE-2019-19064
|     	CVE-2019-19061	7.5	https://vulners.com/cve/CVE-2019-19061
|     	CVE-2019-19060	7.5	https://vulners.com/cve/CVE-2019-19060
|     	CVE-2019-19049	7.5	https://vulners.com/cve/CVE-2019-19049
|     	CVE-2019-18807	7.5	https://vulners.com/cve/CVE-2019-18807
|     	CVE-2019-17075	7.5	https://vulners.com/cve/CVE-2019-17075
|     	CVE-2019-16921	7.5	https://vulners.com/cve/CVE-2019-16921
|     	CVE-2019-16714	7.5	https://vulners.com/cve/CVE-2019-16714
|     	CVE-2019-16413	7.5	https://vulners.com/cve/CVE-2019-16413
|     	CVE-2019-15916	7.5	https://vulners.com/cve/CVE-2019-15916
|     	CVE-2019-12818	7.5	https://vulners.com/cve/CVE-2019-12818
|     	CVE-2019-12615	7.5	https://vulners.com/cve/CVE-2019-12615
|     	CVE-2019-11810	7.5	https://vulners.com/cve/CVE-2019-11810
|     	CVE-2019-11478	7.5	https://vulners.com/cve/CVE-2019-11478
|     	CVE-2019-11477	7.5	https://vulners.com/cve/CVE-2019-11477
|     	CVE-2018-6412	7.5	https://vulners.com/cve/CVE-2018-6412
|     	CVE-2018-5391	7.5	https://vulners.com/cve/CVE-2018-5391
|     	CVE-2018-16871	7.5	https://vulners.com/cve/CVE-2018-16871
|     	CVE-2017-7645	7.5	https://vulners.com/cve/CVE-2017-7645
|     	CVE-2017-6214	7.5	https://vulners.com/cve/CVE-2017-6214
|     	CVE-2017-5972	7.5	https://vulners.com/cve/CVE-2017-5972
|     	CVE-2017-5970	7.5	https://vulners.com/cve/CVE-2017-5970
|     	CVE-2017-1000410	7.5	https://vulners.com/cve/CVE-2017-1000410
|     	CVE-2016-5244	7.5	https://vulners.com/cve/CVE-2016-5244
|     	CVE-2016-4580	7.5	https://vulners.com/cve/CVE-2016-4580
|     	CVE-2016-4485	7.5	https://vulners.com/cve/CVE-2016-4485
|     	CVE-2016-2117	7.5	https://vulners.com/cve/CVE-2016-2117
|     	CVE-2015-8746	7.5	https://vulners.com/cve/CVE-2015-8746
|     	CVE-2014-4608	7.5	https://vulners.com/cve/CVE-2014-4608
|     	CVE-2014-4323	7.5	https://vulners.com/cve/CVE-2014-4323
|     	CVE-2014-3687	7.5	https://vulners.com/cve/CVE-2014-3687
|     	CVE-2014-3673	7.5	https://vulners.com/cve/CVE-2014-3673
|     	B8B06A12-C7E0-50A2-8B97-C96DEC77EEB8	7.5	https://vulners.com/githubexploit/B8B06A12-C7E0-50A2-8B97-C96DEC77EEB8	*EXPLOIT*
|     	58D56E09-E266-52D1-8E6F-749551BEC175	7.5	https://vulners.com/githubexploit/58D56E09-E266-52D1-8E6F-749551BEC175	*EXPLOIT*
|     	4A3B5C53-2CB2-5006-B0EC-6228432CF4CF	7.5	https://vulners.com/githubexploit/4A3B5C53-2CB2-5006-B0EC-6228432CF4CF	*EXPLOIT*
|     	1337DAY-ID-32884	7.5	https://vulners.com/zdt/1337DAY-ID-32884	*EXPLOIT*
|     	1337DAY-ID-31841	7.5	https://vulners.com/zdt/1337DAY-ID-31841	*EXPLOIT*
|     	1337DAY-ID-31840	7.5	https://vulners.com/zdt/1337DAY-ID-31840	*EXPLOIT*
|     	SSV:61637	7.4	https://vulners.com/seebug/SSV:61637	*EXPLOIT*
|     	CVE-2021-20322	7.4	https://vulners.com/cve/CVE-2021-20322
|     	CVE-2020-25705	7.4	https://vulners.com/cve/CVE-2020-25705
|     	CVE-2017-1000407	7.4	https://vulners.com/cve/CVE-2017-1000407
|     	CVE-2017-1000364	7.4	https://vulners.com/cve/CVE-2017-1000364
|     	CVE-2016-6516	7.4	https://vulners.com/cve/CVE-2016-6516
|     	CVE-2016-2069	7.4	https://vulners.com/cve/CVE-2016-2069
|     	CVE-2014-0049	7.4	https://vulners.com/cve/CVE-2014-0049
|     	CVE-2016-3841	7.3	https://vulners.com/cve/CVE-2016-3841
|     	CVE-2015-8962	7.3	https://vulners.com/cve/CVE-2015-8962
|     	CVE-2015-8955	7.3	https://vulners.com/cve/CVE-2015-8955
|     	SSV:96908	7.2	https://vulners.com/seebug/SSV:96908	*EXPLOIT*
|     	SSV:93094	7.2	https://vulners.com/seebug/SSV:93094	*EXPLOIT*
|     	SSV:92861	7.2	https://vulners.com/seebug/SSV:92861	*EXPLOIT*
|     	SSV:92755	7.2	https://vulners.com/seebug/SSV:92755	*EXPLOIT*
|     	SSV:92700	7.2	https://vulners.com/seebug/SSV:92700	*EXPLOIT*
|     	SSV:92567	7.2	https://vulners.com/seebug/SSV:92567	*EXPLOIT*
|     	SSV:92488	7.2	https://vulners.com/seebug/SSV:92488	*EXPLOIT*
|     	SSV:91603	7.2	https://vulners.com/seebug/SSV:91603	*EXPLOIT*
|     	SSV:90673	7.2	https://vulners.com/seebug/SSV:90673	*EXPLOIT*
|     	SAINT:D99FE3AF85FA3F5D4D5C3CB8B43F5183	7.2	https://vulners.com/saint/SAINT:D99FE3AF85FA3F5D4D5C3CB8B43F5183	*EXPLOIT*
|     	SAINT:ABCD3AE5A28A14CD616BF070F6F8E939	7.2	https://vulners.com/saint/SAINT:ABCD3AE5A28A14CD616BF070F6F8E939	*EXPLOIT*
|     	SAINT:1E3BA1480EBC78481EFFC9BD1CFFBBE2	7.2	https://vulners.com/saint/SAINT:1E3BA1480EBC78481EFFC9BD1CFFBBE2	*EXPLOIT*
|     	PACKETSTORM:160681	7.2	https://vulners.com/packetstorm/PACKETSTORM:160681	*EXPLOIT*
|     	PACKETSTORM:149804	7.2	https://vulners.com/packetstorm/PACKETSTORM:149804	*EXPLOIT*
|     	PACKETSTORM:147727	7.2	https://vulners.com/packetstorm/PACKETSTORM:147727	*EXPLOIT*
|     	PACKETSTORM:147685	7.2	https://vulners.com/packetstorm/PACKETSTORM:147685	*EXPLOIT*
|     	PACKETSTORM:142487	7.2	https://vulners.com/packetstorm/PACKETSTORM:142487	*EXPLOIT*
|     	PACKETSTORM:139923	7.2	https://vulners.com/packetstorm/PACKETSTORM:139923	*EXPLOIT*
|     	PACKETSTORM:139922	7.2	https://vulners.com/packetstorm/PACKETSTORM:139922	*EXPLOIT*
|     	PACKETSTORM:139880	7.2	https://vulners.com/packetstorm/PACKETSTORM:139880	*EXPLOIT*
|     	PACKETSTORM:139474	7.2	https://vulners.com/packetstorm/PACKETSTORM:139474	*EXPLOIT*
|     	PACKETSTORM:138854	7.2	https://vulners.com/packetstorm/PACKETSTORM:138854	*EXPLOIT*
|     	PACKETSTORM:135330	7.2	https://vulners.com/packetstorm/PACKETSTORM:135330	*EXPLOIT*
|     	PACKETSTORM:132994	7.2	https://vulners.com/packetstorm/PACKETSTORM:132994	*EXPLOIT*
|     	OVERLAYFS	7.2	https://vulners.com/canvas/OVERLAYFS	*EXPLOIT*
|     	LINUX_FOLL_WRITE_COW	7.2	https://vulners.com/canvas/LINUX_FOLL_WRITE_COW	*EXPLOIT*
|     	F71E8A1A-6296-5CF7-A10B-4AB7F5749D07	7.2	https://vulners.com/githubexploit/F71E8A1A-6296-5CF7-A10B-4AB7F5749D07	*EXPLOIT*
|     	F235C897-C385-56AB-B58E-500B01C27538	7.2	https://vulners.com/githubexploit/F235C897-C385-56AB-B58E-500B01C27538	*EXPLOIT*
|     	EXPLOITPACK:F867C230BBE8FA4BCFE72E04CBAC881F	7.2	https://vulners.com/exploitpack/EXPLOITPACK:F867C230BBE8FA4BCFE72E04CBAC881F	*EXPLOIT*
|     	EXPLOITPACK:E39D353DDC7C21D9144CCF79357BB845	7.2	https://vulners.com/exploitpack/EXPLOITPACK:E39D353DDC7C21D9144CCF79357BB845	*EXPLOIT*
|     	EXPLOITPACK:E28EC01047BD87E7BBB9A8D9EBFFAF29	7.2	https://vulners.com/exploitpack/EXPLOITPACK:E28EC01047BD87E7BBB9A8D9EBFFAF29	*EXPLOIT*
|     	EXPLOITPACK:D5BBB161063632A8D15C357D43E97C75	7.2	https://vulners.com/exploitpack/EXPLOITPACK:D5BBB161063632A8D15C357D43E97C75	*EXPLOIT*
|     	EXPLOITPACK:CE3D88F8948DFAA1033D43E58712BE52	7.2	https://vulners.com/exploitpack/EXPLOITPACK:CE3D88F8948DFAA1033D43E58712BE52	*EXPLOIT*
|     	EXPLOITPACK:9F9EC3D4DD26B34F2A3BD7077A1EBB9E	7.2	https://vulners.com/exploitpack/EXPLOITPACK:9F9EC3D4DD26B34F2A3BD7077A1EBB9E	*EXPLOIT*
|     	EXPLOITPACK:9D752285F4A2795E32FB57E31FD31AB0	7.2	https://vulners.com/exploitpack/EXPLOITPACK:9D752285F4A2795E32FB57E31FD31AB0	*EXPLOIT*
|     	EXPLOITPACK:93D47AC26E5DA900EF305FD8DD1D8904	7.2	https://vulners.com/exploitpack/EXPLOITPACK:93D47AC26E5DA900EF305FD8DD1D8904	*EXPLOIT*
|     	EXPLOITPACK:84D4B1F42D5DCA9623080EFFD17E58E1	7.2	https://vulners.com/exploitpack/EXPLOITPACK:84D4B1F42D5DCA9623080EFFD17E58E1	*EXPLOIT*
|     	EXPLOITPACK:7AD8D8301E32D30D80BF379536ECB19B	7.2	https://vulners.com/exploitpack/EXPLOITPACK:7AD8D8301E32D30D80BF379536ECB19B	*EXPLOIT*
|     	EXPLOITPACK:66230DDA8228F7537211A7F78C05A763	7.2	https://vulners.com/exploitpack/EXPLOITPACK:66230DDA8228F7537211A7F78C05A763	*EXPLOIT*
|     	EXPLOITPACK:4F74638D00AC37320CD01F8B963CC200	7.2	https://vulners.com/exploitpack/EXPLOITPACK:4F74638D00AC37320CD01F8B963CC200	*EXPLOIT*
|     	EXPLOITPACK:4EEB4BE9E101A3B6E5FA4A3FC9B06CCD	7.2	https://vulners.com/exploitpack/EXPLOITPACK:4EEB4BE9E101A3B6E5FA4A3FC9B06CCD	*EXPLOIT*
|     	EXPLOITPACK:4CC02E891FC223E9BA1344151AC6958F	7.2	https://vulners.com/exploitpack/EXPLOITPACK:4CC02E891FC223E9BA1344151AC6958F	*EXPLOIT*
|     	EXPLOITPACK:4CB8F52029A7ED20CD5AD83DA63EF19E	7.2	https://vulners.com/exploitpack/EXPLOITPACK:4CB8F52029A7ED20CD5AD83DA63EF19E	*EXPLOIT*
|     	EXPLOITPACK:471477A64686FE6FF46F4A76389A0F11	7.2	https://vulners.com/exploitpack/EXPLOITPACK:471477A64686FE6FF46F4A76389A0F11	*EXPLOIT*
|     	EXPLOITPACK:3459535A8A480A3A2F164DB01F4CF994	7.2	https://vulners.com/exploitpack/EXPLOITPACK:3459535A8A480A3A2F164DB01F4CF994	*EXPLOIT*
|     	EXPLOITPACK:2E9704BB984395CF6BD1C5E00B34FE96	7.2	https://vulners.com/exploitpack/EXPLOITPACK:2E9704BB984395CF6BD1C5E00B34FE96	*EXPLOIT*
|     	EXPLOITPACK:28AB005E816C9849B89DE59958F58BF7	7.2	https://vulners.com/exploitpack/EXPLOITPACK:28AB005E816C9849B89DE59958F58BF7	*EXPLOIT*
|     	EXPLOITPACK:21E02FD686B4E07E01D154BAF895DE82	7.2	https://vulners.com/exploitpack/EXPLOITPACK:21E02FD686B4E07E01D154BAF895DE82	*EXPLOIT*
|     	EXPLOITPACK:16C6631EA58A39D16E0BC600D7FA1BAB	7.2	https://vulners.com/exploitpack/EXPLOITPACK:16C6631EA58A39D16E0BC600D7FA1BAB	*EXPLOIT*
|     	EXPLOITPACK:088CF7ADCAFEF383490420614A9EEA47	7.2	https://vulners.com/exploitpack/EXPLOITPACK:088CF7ADCAFEF383490420614A9EEA47	*EXPLOIT*
|     	EDB-ID:45554	7.2	https://vulners.com/exploitdb/EDB-ID:45554	*EXPLOIT*
|     	EDB-ID:37722	7.2	https://vulners.com/exploitdb/EDB-ID:37722	*EXPLOIT*
|     	EDB-ID:36743	7.2	https://vulners.com/exploitdb/EDB-ID:36743	*EXPLOIT*
|     	EDB-ID:35711	7.2	https://vulners.com/exploitdb/EDB-ID:35711	*EXPLOIT*
|     	EBDBA910-86AB-51E0-AF47-697C7E5C334C	7.2	https://vulners.com/githubexploit/EBDBA910-86AB-51E0-AF47-697C7E5C334C	*EXPLOIT*
|     	D86EDC54-781B-5FC3-95F4-35B9EB4DFF0B	7.2	https://vulners.com/githubexploit/D86EDC54-781B-5FC3-95F4-35B9EB4DFF0B	*EXPLOIT*
|     	D632E896-5824-5634-95FB-A564581718DA	7.2	https://vulners.com/githubexploit/D632E896-5824-5634-95FB-A564581718DA	*EXPLOIT*
|     	D2F07A56-EAB9-5BC0-915B-E0D6E88AC81C	7.2	https://vulners.com/githubexploit/D2F07A56-EAB9-5BC0-915B-E0D6E88AC81C	*EXPLOIT*
|     	CVE-2020-25643	7.2	https://vulners.com/cve/CVE-2020-25643
|     	CVE-2015-5157	7.2	https://vulners.com/cve/CVE-2015-5157
|     	CVE-2015-4036	7.2	https://vulners.com/cve/CVE-2015-4036
|     	CVE-2015-3290	7.2	https://vulners.com/cve/CVE-2015-3290
|     	CVE-2015-1805	7.2	https://vulners.com/cve/CVE-2015-1805
|     	CVE-2014-8173	7.2	https://vulners.com/cve/CVE-2014-8173
|     	CVE-2014-7822	7.2	https://vulners.com/cve/CVE-2014-7822
|     	CVE-2014-5206	7.2	https://vulners.com/cve/CVE-2014-5206
|     	CVE-2014-4322	7.2	https://vulners.com/cve/CVE-2014-4322
|     	C56D37BC-0825-5F31-B1DE-FDCAB22ECBED	7.2	https://vulners.com/githubexploit/C56D37BC-0825-5F31-B1DE-FDCAB22ECBED	*EXPLOIT*
|     	BC274E1C-826C-5417-953C-082B3ECA17BD	7.2	https://vulners.com/githubexploit/BC274E1C-826C-5417-953C-082B3ECA17BD	*EXPLOIT*
|     	BB30BDE6-E8F6-5ECC-9BF0-0D35F0A1FA7A	7.2	https://vulners.com/githubexploit/BB30BDE6-E8F6-5ECC-9BF0-0D35F0A1FA7A	*EXPLOIT*
|     	B534183D-00E6-58F7-BD0F-372BEC91370C	7.2	https://vulners.com/githubexploit/B534183D-00E6-58F7-BD0F-372BEC91370C	*EXPLOIT*
|     	A5816523-972A-580C-A7BC-0292D1132D1E	7.2	https://vulners.com/githubexploit/A5816523-972A-580C-A7BC-0292D1132D1E	*EXPLOIT*
|     	A10132DA-F650-5163-A3F9-DBE973D0187D	7.2	https://vulners.com/githubexploit/A10132DA-F650-5163-A3F9-DBE973D0187D	*EXPLOIT*
|     	939FF0B7-EA0B-569E-A54E-38A68F563E58	7.2	https://vulners.com/githubexploit/939FF0B7-EA0B-569E-A54E-38A68F563E58	*EXPLOIT*
|     	91ACFD93-47E2-56B0-A34A-8DC0F7D97A8E	7.2	https://vulners.com/githubexploit/91ACFD93-47E2-56B0-A34A-8DC0F7D97A8E	*EXPLOIT*
|     	85567B66-33FE-5200-8371-D8BB5B44F74D	7.2	https://vulners.com/githubexploit/85567B66-33FE-5200-8371-D8BB5B44F74D	*EXPLOIT*
|     	504EFC7A-78B6-5F21-AD8D-7249C4FBC727	7.2	https://vulners.com/githubexploit/504EFC7A-78B6-5F21-AD8D-7249C4FBC727	*EXPLOIT*
|     	3773C013-3749-58FC-826E-D8D781A68DF0	7.2	https://vulners.com/githubexploit/3773C013-3749-58FC-826E-D8D781A68DF0	*EXPLOIT*
|     	2F990B46-0F97-57C0-9C4B-7012BBDBA610	7.2	https://vulners.com/githubexploit/2F990B46-0F97-57C0-9C4B-7012BBDBA610	*EXPLOIT*
|     	1F2532B3-0167-53EA-ACD1-3EC546ACA052	7.2	https://vulners.com/githubexploit/1F2532B3-0167-53EA-ACD1-3EC546ACA052	*EXPLOIT*
|     	18307056-6D88-5195-8CFA-56E31359A0D0	7.2	https://vulners.com/githubexploit/18307056-6D88-5195-8CFA-56E31359A0D0	*EXPLOIT*
|     	1337DAY-ID-33037	7.2	https://vulners.com/zdt/1337DAY-ID-33037	*EXPLOIT*
|     	1337DAY-ID-33035	7.2	https://vulners.com/zdt/1337DAY-ID-33035	*EXPLOIT*
|     	1337DAY-ID-31273	7.2	https://vulners.com/zdt/1337DAY-ID-31273	*EXPLOIT*
|     	1337DAY-ID-30429	7.2	https://vulners.com/zdt/1337DAY-ID-30429	*EXPLOIT*
|     	1337DAY-ID-30376	7.2	https://vulners.com/zdt/1337DAY-ID-30376	*EXPLOIT*
|     	1337DAY-ID-29916	7.2	https://vulners.com/zdt/1337DAY-ID-29916	*EXPLOIT*
|     	1337DAY-ID-29141	7.2	https://vulners.com/zdt/1337DAY-ID-29141	*EXPLOIT*
|     	1337DAY-ID-27764	7.2	https://vulners.com/zdt/1337DAY-ID-27764	*EXPLOIT*
|     	1337DAY-ID-27761	7.2	https://vulners.com/zdt/1337DAY-ID-27761	*EXPLOIT*
|     	1337DAY-ID-27471	7.2	https://vulners.com/zdt/1337DAY-ID-27471	*EXPLOIT*
|     	1337DAY-ID-27467	7.2	https://vulners.com/zdt/1337DAY-ID-27467	*EXPLOIT*
|     	1337DAY-ID-27134	7.2	https://vulners.com/zdt/1337DAY-ID-27134	*EXPLOIT*
|     	1337DAY-ID-27133	7.2	https://vulners.com/zdt/1337DAY-ID-27133	*EXPLOIT*
|     	1337DAY-ID-26493	7.2	https://vulners.com/zdt/1337DAY-ID-26493	*EXPLOIT*
|     	1337DAY-ID-26446	7.2	https://vulners.com/zdt/1337DAY-ID-26446	*EXPLOIT*
|     	1337DAY-ID-26431	7.2	https://vulners.com/zdt/1337DAY-ID-26431	*EXPLOIT*
|     	1337DAY-ID-26430	7.2	https://vulners.com/zdt/1337DAY-ID-26430	*EXPLOIT*
|     	1337DAY-ID-26429	7.2	https://vulners.com/zdt/1337DAY-ID-26429	*EXPLOIT*
|     	1337DAY-ID-26412	7.2	https://vulners.com/zdt/1337DAY-ID-26412	*EXPLOIT*
|     	1337DAY-ID-26220	7.2	https://vulners.com/zdt/1337DAY-ID-26220	*EXPLOIT*
|     	1337DAY-ID-26201	7.2	https://vulners.com/zdt/1337DAY-ID-26201	*EXPLOIT*
|     	1337DAY-ID-25952	7.2	https://vulners.com/zdt/1337DAY-ID-25952	*EXPLOIT*
|     	1337DAY-ID-25944	7.2	https://vulners.com/zdt/1337DAY-ID-25944	*EXPLOIT*
|     	1337DAY-ID-25943	7.2	https://vulners.com/zdt/1337DAY-ID-25943	*EXPLOIT*
|     	1337DAY-ID-25862	7.2	https://vulners.com/zdt/1337DAY-ID-25862	*EXPLOIT*
|     	1337DAY-ID-25603	7.2	https://vulners.com/zdt/1337DAY-ID-25603	*EXPLOIT*
|     	1337DAY-ID-25517	7.2	https://vulners.com/zdt/1337DAY-ID-25517	*EXPLOIT*
|     	1337DAY-ID-25516	7.2	https://vulners.com/zdt/1337DAY-ID-25516	*EXPLOIT*
|     	1337DAY-ID-24860	7.2	https://vulners.com/zdt/1337DAY-ID-24860	*EXPLOIT*
|     	1337DAY-ID-23971	7.2	https://vulners.com/zdt/1337DAY-ID-23971	*EXPLOIT*
|     	1337DAY-ID-23763	7.2	https://vulners.com/zdt/1337DAY-ID-23763	*EXPLOIT*
|     	1337DAY-ID-23357	7.2	https://vulners.com/zdt/1337DAY-ID-23357	*EXPLOIT*
|     	12586F18-65D0-56EC-ABDC-A2C75034CF09	7.2	https://vulners.com/githubexploit/12586F18-65D0-56EC-ABDC-A2C75034CF09	*EXPLOIT*
|     	12570BB6-9BCA-5792-9E08-32A83CFD8209	7.2	https://vulners.com/githubexploit/12570BB6-9BCA-5792-9E08-32A83CFD8209	*EXPLOIT*
|     	0AB0DD16-3EF1-5D1D-BE61-96FDD1D699D1	7.2	https://vulners.com/githubexploit/0AB0DD16-3EF1-5D1D-BE61-96FDD1D699D1	*EXPLOIT*
|     	01EF49BE-F69D-52BF-B4C3-3DC0FAAD5CD8	7.2	https://vulners.com/githubexploit/01EF49BE-F69D-52BF-B4C3-3DC0FAAD5CD8	*EXPLOIT*
|     	CVE-2024-26594	7.1	https://vulners.com/cve/CVE-2024-26594
|     	CVE-2024-0775	7.1	https://vulners.com/cve/CVE-2024-0775
|     	CVE-2023-52827	7.1	https://vulners.com/cve/CVE-2023-52827
|     	CVE-2023-3567	7.1	https://vulners.com/cve/CVE-2023-3567
|     	CVE-2023-3317	7.1	https://vulners.com/cve/CVE-2023-3317
|     	CVE-2023-3268	7.1	https://vulners.com/cve/CVE-2023-3268
|     	CVE-2023-3141	7.1	https://vulners.com/cve/CVE-2023-3141
|     	CVE-2023-26607	7.1	https://vulners.com/cve/CVE-2023-26607
|     	CVE-2023-1838	7.1	https://vulners.com/cve/CVE-2023-1838
|     	CVE-2023-1652	7.1	https://vulners.com/cve/CVE-2023-1652
|     	CVE-2023-1380	7.1	https://vulners.com/cve/CVE-2023-1380
|     	CVE-2022-41858	7.1	https://vulners.com/cve/CVE-2022-41858
|     	CVE-2022-3564	7.1	https://vulners.com/cve/CVE-2022-3564
|     	CVE-2022-33742	7.1	https://vulners.com/cve/CVE-2022-33742
|     	CVE-2022-33741	7.1	https://vulners.com/cve/CVE-2022-33741
|     	CVE-2022-33740	7.1	https://vulners.com/cve/CVE-2022-33740
|     	CVE-2022-3202	7.1	https://vulners.com/cve/CVE-2022-3202
|     	CVE-2022-26365	7.1	https://vulners.com/cve/CVE-2022-26365
|     	CVE-2022-1973	7.1	https://vulners.com/cve/CVE-2022-1973
|     	CVE-2022-1671	7.1	https://vulners.com/cve/CVE-2022-1671
|     	CVE-2022-1651	7.1	https://vulners.com/cve/CVE-2022-1651
|     	CVE-2022-1353	7.1	https://vulners.com/cve/CVE-2022-1353
|     	CVE-2022-0850	7.1	https://vulners.com/cve/CVE-2022-0850
|     	CVE-2021-4204	7.1	https://vulners.com/cve/CVE-2021-4204
|     	CVE-2021-4090	7.1	https://vulners.com/cve/CVE-2021-4090
|     	CVE-2021-3752	7.1	https://vulners.com/cve/CVE-2021-3752
|     	CVE-2021-3743	7.1	https://vulners.com/cve/CVE-2021-3743
|     	CVE-2021-3739	7.1	https://vulners.com/cve/CVE-2021-3739
|     	CVE-2021-3506	7.1	https://vulners.com/cve/CVE-2021-3506
|     	CVE-2021-3501	7.1	https://vulners.com/cve/CVE-2021-3501
|     	CVE-2021-32078	7.1	https://vulners.com/cve/CVE-2021-32078
|     	CVE-2021-27364	7.1	https://vulners.com/cve/CVE-2021-27364
|     	CVE-2020-8648	7.1	https://vulners.com/cve/CVE-2020-8648
|     	CVE-2020-36386	7.1	https://vulners.com/cve/CVE-2020-36386
|     	CVE-2020-24394	7.1	https://vulners.com/cve/CVE-2020-24394
|     	CVE-2020-12654	7.1	https://vulners.com/cve/CVE-2020-12654
|     	CVE-2020-11668	7.1	https://vulners.com/cve/CVE-2020-11668
|     	CVE-2019-25160	7.1	https://vulners.com/cve/CVE-2019-25160
|     	CVE-2018-18021	7.1	https://vulners.com/cve/CVE-2018-18021
|     	CVE-2017-7277	7.1	https://vulners.com/cve/CVE-2017-7277
|     	CVE-2017-2584	7.1	https://vulners.com/cve/CVE-2017-2584
|     	CVE-2017-18270	7.1	https://vulners.com/cve/CVE-2017-18270
|     	CVE-2017-12154	7.1	https://vulners.com/cve/CVE-2017-12154
|     	CVE-2017-11472	7.1	https://vulners.com/cve/CVE-2017-11472
|     	CVE-2016-4998	7.1	https://vulners.com/cve/CVE-2016-4998
|     	CVE-2016-3713	7.1	https://vulners.com/cve/CVE-2016-3713
|     	CVE-2014-6418	7.1	https://vulners.com/cve/CVE-2014-6418
|     	2B3EC3DA-4EE0-518F-8706-77CCA2D66F96	7.1	https://vulners.com/githubexploit/2B3EC3DA-4EE0-518F-8706-77CCA2D66F96	*EXPLOIT*
|     	096E2723-7D96-5370-B173-04C907D454A3	7.1	https://vulners.com/githubexploit/096E2723-7D96-5370-B173-04C907D454A3	*EXPLOIT*
|     	MSF:EXPLOIT-LINUX-LOCAL-UFO_PRIVILEGE_ESCALATION-	7.0	https://vulners.com/metasploit/MSF:EXPLOIT-LINUX-LOCAL-UFO_PRIVILEGE_ESCALATION-	*EXPLOIT*
|     	EDB-ID:47169	7.0	https://vulners.com/exploitdb/EDB-ID:47169	*EXPLOIT*
|     	EDB-ID:45147	7.0	https://vulners.com/exploitdb/EDB-ID:45147	*EXPLOIT*
|     	EDB-ID:44302	7.0	https://vulners.com/exploitdb/EDB-ID:44302	*EXPLOIT*
|     	EDB-ID:43418	7.0	https://vulners.com/exploitdb/EDB-ID:43418	*EXPLOIT*
|     	EDB-ID:43345	7.0	https://vulners.com/exploitdb/EDB-ID:43345	*EXPLOIT*
|     	ED4486DF-C3F3-577E-A1AF-2DF89300C736	7.0	https://vulners.com/githubexploit/ED4486DF-C3F3-577E-A1AF-2DF89300C736	*EXPLOIT*
|     	DD595957-D3F4-572A-9F7E-58901ABA7499	7.0	https://vulners.com/githubexploit/DD595957-D3F4-572A-9F7E-58901ABA7499	*EXPLOIT*
|     	CVE-2023-6546	7.0	https://vulners.com/cve/CVE-2023-6546
|     	CVE-2023-6531	7.0	https://vulners.com/cve/CVE-2023-6531
|     	CVE-2023-51782	7.0	https://vulners.com/cve/CVE-2023-51782
|     	CVE-2023-51781	7.0	https://vulners.com/cve/CVE-2023-51781
|     	CVE-2023-51780	7.0	https://vulners.com/cve/CVE-2023-51780
|     	CVE-2023-51043	7.0	https://vulners.com/cve/CVE-2023-51043
|     	CVE-2023-46813	7.0	https://vulners.com/cve/CVE-2023-46813
|     	CVE-2023-4611	7.0	https://vulners.com/cve/CVE-2023-4611
|     	CVE-2023-35827	7.0	https://vulners.com/cve/CVE-2023-35827
|     	CVE-2023-35824	7.0	https://vulners.com/cve/CVE-2023-35824
|     	CVE-2023-35823	7.0	https://vulners.com/cve/CVE-2023-35823
|     	CVE-2023-1989	7.0	https://vulners.com/cve/CVE-2023-1989
|     	CVE-2023-1476	7.0	https://vulners.com/cve/CVE-2023-1476
|     	CVE-2023-1077	7.0	https://vulners.com/cve/CVE-2023-1077
|     	CVE-2022-45919	7.0	https://vulners.com/cve/CVE-2022-45919
|     	CVE-2022-45886	7.0	https://vulners.com/cve/CVE-2022-45886
|     	CVE-2022-45885	7.0	https://vulners.com/cve/CVE-2022-45885
|     	CVE-2022-45884	7.0	https://vulners.com/cve/CVE-2022-45884
|     	CVE-2022-3649	7.0	https://vulners.com/cve/CVE-2022-3649
|     	CVE-2022-3635	7.0	https://vulners.com/cve/CVE-2022-3635
|     	CVE-2022-3028	7.0	https://vulners.com/cve/CVE-2022-3028
|     	CVE-2022-2961	7.0	https://vulners.com/cve/CVE-2022-2961
|     	CVE-2022-2959	7.0	https://vulners.com/cve/CVE-2022-2959
|     	CVE-2022-29582	7.0	https://vulners.com/cve/CVE-2022-29582
|     	CVE-2022-2602	7.0	https://vulners.com/cve/CVE-2022-2602
|     	CVE-2022-2590	7.0	https://vulners.com/cve/CVE-2022-2590
|     	CVE-2022-1734	7.0	https://vulners.com/cve/CVE-2022-1734
|     	CVE-2022-1729	7.0	https://vulners.com/cve/CVE-2022-1729
|     	CVE-2022-1048	7.0	https://vulners.com/cve/CVE-2022-1048
|     	CVE-2021-44733	7.0	https://vulners.com/cve/CVE-2021-44733
|     	CVE-2021-4202	7.0	https://vulners.com/cve/CVE-2021-4202
|     	CVE-2021-4083	7.0	https://vulners.com/cve/CVE-2021-4083
|     	CVE-2021-40490	7.0	https://vulners.com/cve/CVE-2021-40490
|     	CVE-2021-3640	7.0	https://vulners.com/cve/CVE-2021-3640
|     	CVE-2021-3609	7.0	https://vulners.com/cve/CVE-2021-3609
|     	CVE-2021-3348	7.0	https://vulners.com/cve/CVE-2021-3348
|     	CVE-2021-32399	7.0	https://vulners.com/cve/CVE-2021-32399
|     	CVE-2021-31440	7.0	https://vulners.com/cve/CVE-2021-31440
|     	CVE-2021-22600	7.0	https://vulners.com/cve/CVE-2021-22600
|     	CVE-2020-29370	7.0	https://vulners.com/cve/CVE-2020-29370
|     	CVE-2020-25668	7.0	https://vulners.com/cve/CVE-2020-25668
|     	CVE-2020-25212	7.0	https://vulners.com/cve/CVE-2020-25212
|     	CVE-2019-13233	7.0	https://vulners.com/cve/CVE-2019-13233
|     	CVE-2019-12817	7.0	https://vulners.com/cve/CVE-2019-12817
|     	CVE-2019-11599	7.0	https://vulners.com/cve/CVE-2019-11599
|     	CVE-2019-11486	7.0	https://vulners.com/cve/CVE-2019-11486
|     	CVE-2018-5814	7.0	https://vulners.com/cve/CVE-2018-5814
|     	CVE-2018-14656	7.0	https://vulners.com/cve/CVE-2018-14656
|     	CVE-2018-14633	7.0	https://vulners.com/cve/CVE-2018-14633
|     	CVE-2017-7533	7.0	https://vulners.com/cve/CVE-2017-7533
|     	CVE-2017-6346	7.0	https://vulners.com/cve/CVE-2017-6346
|     	CVE-2017-2636	7.0	https://vulners.com/cve/CVE-2017-2636
|     	CVE-2017-18249	7.0	https://vulners.com/cve/CVE-2017-18249
|     	CVE-2017-15265	7.0	https://vulners.com/cve/CVE-2017-15265
|     	CVE-2017-11600	7.0	https://vulners.com/cve/CVE-2017-11600
|     	CVE-2017-10661	7.0	https://vulners.com/cve/CVE-2017-10661
|     	CVE-2017-1000112	7.0	https://vulners.com/cve/CVE-2017-1000112
|     	CVE-2017-0523	7.0	https://vulners.com/cve/CVE-2017-0523
|     	CVE-2016-6787	7.0	https://vulners.com/cve/CVE-2016-6787
|     	CVE-2016-6786	7.0	https://vulners.com/cve/CVE-2016-6786
|     	CVE-2016-2059	7.0	https://vulners.com/cve/CVE-2016-2059
|     	CVE-2016-10906	7.0	https://vulners.com/cve/CVE-2016-10906
|     	CVE-2016-10200	7.0	https://vulners.com/cve/CVE-2016-10200
|     	CVE-2016-10088	7.0	https://vulners.com/cve/CVE-2016-10088
|     	CVE-2015-8963	7.0	https://vulners.com/cve/CVE-2015-8963
|     	CVE-2015-8709	7.0	https://vulners.com/cve/CVE-2015-8709
|     	CVE-2015-8543	7.0	https://vulners.com/cve/CVE-2015-8543
|     	CVE-2015-0572	7.0	https://vulners.com/cve/CVE-2015-0572
|     	CVE-2014-9940	7.0	https://vulners.com/cve/CVE-2014-9940
|     	BF419F70-A6F6-572C-8DB0-55498291C16C	7.0	https://vulners.com/githubexploit/BF419F70-A6F6-572C-8DB0-55498291C16C	*EXPLOIT*
|     	88B2258B-A28E-5C00-85F0-542DB0BD2275	7.0	https://vulners.com/githubexploit/88B2258B-A28E-5C00-85F0-542DB0BD2275	*EXPLOIT*
|     	65A5287D-DE34-5736-ABA3-A5465299C813	7.0	https://vulners.com/githubexploit/65A5287D-DE34-5736-ABA3-A5465299C813	*EXPLOIT*
|     	1337DAY-ID-32619	7.0	https://vulners.com/zdt/1337DAY-ID-32619	*EXPLOIT*
|     	08611DC9-A473-548B-8CE6-8D8F95C6B293	7.0	https://vulners.com/githubexploit/08611DC9-A473-548B-8CE6-8D8F95C6B293	*EXPLOIT*
|     	SSV:96343	6.9	https://vulners.com/seebug/SSV:96343	*EXPLOIT*
|     	SSV:61013	6.9	https://vulners.com/seebug/SSV:61013	*EXPLOIT*
|     	PACKETSTORM:176099	6.9	https://vulners.com/packetstorm/PACKETSTORM:176099	*EXPLOIT*
|     	PACKETSTORM:148795	6.9	https://vulners.com/packetstorm/PACKETSTORM:148795	*EXPLOIT*
|     	EXPLOITPACK:A5820DF756E60078D7D5399A134D0CEE	6.9	https://vulners.com/exploitpack/EXPLOITPACK:A5820DF756E60078D7D5399A134D0CEE	*EXPLOIT*
|     	EXPLOITPACK:7E4B21925D392950552D213FE7157C98	6.9	https://vulners.com/exploitpack/EXPLOITPACK:7E4B21925D392950552D213FE7157C98	*EXPLOIT*
|     	EXPLOITPACK:7C26DD271630EDB66FB520C30E13D873	6.9	https://vulners.com/exploitpack/EXPLOITPACK:7C26DD271630EDB66FB520C30E13D873	*EXPLOIT*
|     	CVE-2022-2503	6.9	https://vulners.com/cve/CVE-2022-2503
|     	CVE-2015-7613	6.9	https://vulners.com/cve/CVE-2015-7613
|     	CVE-2015-2925	6.9	https://vulners.com/cve/CVE-2015-2925
|     	CVE-2015-2666	6.9	https://vulners.com/cve/CVE-2015-2666
|     	CVE-2014-9710	6.9	https://vulners.com/cve/CVE-2014-9710
|     	CVE-2014-9529	6.9	https://vulners.com/cve/CVE-2014-9529
|     	CVE-2014-8159	6.9	https://vulners.com/cve/CVE-2014-8159
|     	CVE-2014-3186	6.9	https://vulners.com/cve/CVE-2014-3186
|     	CVE-2014-3185	6.9	https://vulners.com/cve/CVE-2014-3185
|     	CVE-2014-3182	6.9	https://vulners.com/cve/CVE-2014-3182
|     	CVE-2014-3181	6.9	https://vulners.com/cve/CVE-2014-3181
|     	CVE-2013-4470	6.9	https://vulners.com/cve/CVE-2013-4470
|     	1337DAY-ID-30013	6.9	https://vulners.com/zdt/1337DAY-ID-30013	*EXPLOIT*
|     	CVE-2024-24857	6.8	https://vulners.com/cve/CVE-2024-24857
|     	CVE-2023-2002	6.8	https://vulners.com/cve/CVE-2023-2002
|     	CVE-2023-1079	6.8	https://vulners.com/cve/CVE-2023-1079
|     	CVE-2022-1789	6.8	https://vulners.com/cve/CVE-2022-1789
|     	CVE-2021-4203	6.8	https://vulners.com/cve/CVE-2021-4203
|     	CVE-2021-38204	6.8	https://vulners.com/cve/CVE-2021-38204
|     	CVE-2021-33656	6.8	https://vulners.com/cve/CVE-2021-33656
|     	CVE-2019-19532	6.8	https://vulners.com/cve/CVE-2019-19532
|     	CVE-2019-19531	6.8	https://vulners.com/cve/CVE-2019-19531
|     	CVE-2019-19527	6.8	https://vulners.com/cve/CVE-2019-19527
|     	CVE-2019-14283	6.8	https://vulners.com/cve/CVE-2019-14283
|     	CVE-2019-13631	6.8	https://vulners.com/cve/CVE-2019-13631
|     	CVE-2018-20169	6.8	https://vulners.com/cve/CVE-2018-20169
|     	CVE-2016-8633	6.8	https://vulners.com/cve/CVE-2016-8633
|     	CVE-2016-0723	6.8	https://vulners.com/cve/CVE-2016-0723
|     	CVE-2015-8816	6.8	https://vulners.com/cve/CVE-2015-8816
|     	8B51C62F-B44C-5061-9647-E58DEFF955C1	6.8	https://vulners.com/githubexploit/8B51C62F-B44C-5061-9647-E58DEFF955C1	*EXPLOIT*
|     	1337DAY-ID-32199	6.8	https://vulners.com/zdt/1337DAY-ID-32199	*EXPLOIT*
|     	MSF:EXPLOIT-LINUX-LOCAL-OVERLAYFS_PRIV_ESC-	6.7	https://vulners.com/metasploit/MSF:EXPLOIT-LINUX-LOCAL-OVERLAYFS_PRIV_ESC-	*EXPLOIT*
|     	EDB-ID:40688	6.7	https://vulners.com/exploitdb/EDB-ID:40688	*EXPLOIT*
|     	CVE-2023-4394	6.7	https://vulners.com/cve/CVE-2023-4394
|     	CVE-2023-4273	6.7	https://vulners.com/cve/CVE-2023-4273
|     	CVE-2023-39192	6.7	https://vulners.com/cve/CVE-2023-39192
|     	CVE-2023-33952	6.7	https://vulners.com/cve/CVE-2023-33952
|     	CVE-2023-33951	6.7	https://vulners.com/cve/CVE-2023-33951
|     	CVE-2023-32269	6.7	https://vulners.com/cve/CVE-2023-32269
|     	CVE-2023-3159	6.7	https://vulners.com/cve/CVE-2023-3159
|     	CVE-2023-28772	6.7	https://vulners.com/cve/CVE-2023-28772
|     	CVE-2023-2513	6.7	https://vulners.com/cve/CVE-2023-2513
|     	CVE-2023-2194	6.7	https://vulners.com/cve/CVE-2023-2194
|     	CVE-2022-43750	6.7	https://vulners.com/cve/CVE-2022-43750
|     	CVE-2022-2991	6.7	https://vulners.com/cve/CVE-2022-2991
|     	CVE-2022-2785	6.7	https://vulners.com/cve/CVE-2022-2785
|     	CVE-2021-43975	6.7	https://vulners.com/cve/CVE-2021-43975
|     	CVE-2021-42739	6.7	https://vulners.com/cve/CVE-2021-42739
|     	CVE-2021-42327	6.7	https://vulners.com/cve/CVE-2021-42327
|     	CVE-2021-3543	6.7	https://vulners.com/cve/CVE-2021-3543
|     	CVE-2021-3411	6.7	https://vulners.com/cve/CVE-2021-3411
|     	CVE-2021-33655	6.7	https://vulners.com/cve/CVE-2021-33655
|     	CVE-2021-31916	6.7	https://vulners.com/cve/CVE-2021-31916
|     	CVE-2021-28972	6.7	https://vulners.com/cve/CVE-2021-28972
|     	CVE-2021-20292	6.7	https://vulners.com/cve/CVE-2021-20292
|     	CVE-2020-36694	6.7	https://vulners.com/cve/CVE-2020-36694
|     	CVE-2020-35499	6.7	https://vulners.com/cve/CVE-2020-35499
|     	CVE-2020-27777	6.7	https://vulners.com/cve/CVE-2020-27777
|     	CVE-2020-15780	6.7	https://vulners.com/cve/CVE-2020-15780
|     	CVE-2020-15436	6.7	https://vulners.com/cve/CVE-2020-15436
|     	CVE-2020-12770	6.7	https://vulners.com/cve/CVE-2020-12770
|     	CVE-2020-12464	6.7	https://vulners.com/cve/CVE-2020-12464
|     	CVE-2019-20908	6.7	https://vulners.com/cve/CVE-2019-20908
|     	CVE-2019-20636	6.7	https://vulners.com/cve/CVE-2019-20636
|     	CVE-2019-19769	6.7	https://vulners.com/cve/CVE-2019-19769
|     	CVE-2019-15090	6.7	https://vulners.com/cve/CVE-2019-15090
|     	CVE-2018-1068	6.7	https://vulners.com/cve/CVE-2018-1068
|     	CVE-2017-18551	6.7	https://vulners.com/cve/CVE-2017-18551
|     	CDC86280-5BEC-53D5-B6FA-130CF99602EE	6.7	https://vulners.com/githubexploit/CDC86280-5BEC-53D5-B6FA-130CF99602EE	*EXPLOIT*
|     	C88EC5D2-2767-5E5E-AE6E-479AF57F1FFC	6.7	https://vulners.com/githubexploit/C88EC5D2-2767-5E5E-AE6E-479AF57F1FFC	*EXPLOIT*
|     	7DC0D441-2198-52E7-A813-4D310A89E3AF	6.7	https://vulners.com/githubexploit/7DC0D441-2198-52E7-A813-4D310A89E3AF	*EXPLOIT*
|     	2E310E77-C8C1-54BC-B75A-D409AD2532AA	6.7	https://vulners.com/githubexploit/2E310E77-C8C1-54BC-B75A-D409AD2532AA	*EXPLOIT*
|     	PACKETSTORM:166815	6.6	https://vulners.com/packetstorm/PACKETSTORM:166815	*EXPLOIT*
|     	PACKETSTORM:166770	6.6	https://vulners.com/packetstorm/PACKETSTORM:166770	*EXPLOIT*
|     	CVE-2024-0607	6.6	https://vulners.com/cve/CVE-2024-0607
|     	CVE-2022-3628	6.6	https://vulners.com/cve/CVE-2022-3628
|     	CVE-2022-1015	6.6	https://vulners.com/cve/CVE-2022-1015
|     	CVE-2020-14331	6.6	https://vulners.com/cve/CVE-2020-14331
|     	CVE-2017-17558	6.6	https://vulners.com/cve/CVE-2017-17558
|     	CVE-2017-16650	6.6	https://vulners.com/cve/CVE-2017-16650
|     	CVE-2017-16649	6.6	https://vulners.com/cve/CVE-2017-16649
|     	CVE-2017-16648	6.6	https://vulners.com/cve/CVE-2017-16648
|     	CVE-2017-16647	6.6	https://vulners.com/cve/CVE-2017-16647
|     	CVE-2017-16646	6.6	https://vulners.com/cve/CVE-2017-16646
|     	CVE-2017-16645	6.6	https://vulners.com/cve/CVE-2017-16645
|     	CVE-2017-16644	6.6	https://vulners.com/cve/CVE-2017-16644
|     	CVE-2017-16643	6.6	https://vulners.com/cve/CVE-2017-16643
|     	CVE-2017-16538	6.6	https://vulners.com/cve/CVE-2017-16538
|     	CVE-2017-16537	6.6	https://vulners.com/cve/CVE-2017-16537
|     	CVE-2017-16536	6.6	https://vulners.com/cve/CVE-2017-16536
|     	CVE-2017-16535	6.6	https://vulners.com/cve/CVE-2017-16535
|     	CVE-2017-16533	6.6	https://vulners.com/cve/CVE-2017-16533
|     	CVE-2017-16532	6.6	https://vulners.com/cve/CVE-2017-16532
|     	CVE-2017-16531	6.6	https://vulners.com/cve/CVE-2017-16531
|     	CVE-2017-16530	6.6	https://vulners.com/cve/CVE-2017-16530
|     	CVE-2017-16529	6.6	https://vulners.com/cve/CVE-2017-16529
|     	CVE-2017-16527	6.6	https://vulners.com/cve/CVE-2017-16527
|     	CVE-2017-16525	6.6	https://vulners.com/cve/CVE-2017-16525
|     	9D903AC3-081F-5485-A855-58D63FAF01A2	6.6	https://vulners.com/githubexploit/9D903AC3-081F-5485-A855-58D63FAF01A2	*EXPLOIT*
|     	8FD8C8EC-6004-5390-80EE-DA046C796FC4	6.6	https://vulners.com/githubexploit/8FD8C8EC-6004-5390-80EE-DA046C796FC4	*EXPLOIT*
|     	5F6F4F04-E530-5303-96A4-654898983096	6.6	https://vulners.com/githubexploit/5F6F4F04-E530-5303-96A4-654898983096	*EXPLOIT*
|     	50953417-D37E-5232-988A-515C87054353	6.6	https://vulners.com/githubexploit/50953417-D37E-5232-988A-515C87054353	*EXPLOIT*
|     	3E6ECE0B-2F76-54DA-8A9F-0AB7F69F96FA	6.6	https://vulners.com/githubexploit/3E6ECE0B-2F76-54DA-8A9F-0AB7F69F96FA	*EXPLOIT*
|     	19C06A56-2589-525D-AA16-1436A60FCA7E	6.6	https://vulners.com/githubexploit/19C06A56-2589-525D-AA16-1436A60FCA7E	*EXPLOIT*
|     	CVE-2023-5158	6.5	https://vulners.com/cve/CVE-2023-5158
|     	CVE-2023-42755	6.5	https://vulners.com/cve/CVE-2023-42755
|     	CVE-2023-3338	6.5	https://vulners.com/cve/CVE-2023-3338
|     	CVE-2023-30456	6.5	https://vulners.com/cve/CVE-2023-30456
|     	CVE-2023-1193	6.5	https://vulners.com/cve/CVE-2023-1193
|     	CVE-2023-1192	6.5	https://vulners.com/cve/CVE-2023-1192
|     	CVE-2023-0459	6.5	https://vulners.com/cve/CVE-2023-0459
|     	CVE-2021-38199	6.5	https://vulners.com/cve/CVE-2021-38199
|     	CVE-2021-3772	6.5	https://vulners.com/cve/CVE-2021-3772
|     	CVE-2021-3178	6.5	https://vulners.com/cve/CVE-2021-3178
|     	CVE-2021-28715	6.5	https://vulners.com/cve/CVE-2021-28715
|     	CVE-2021-28714	6.5	https://vulners.com/cve/CVE-2021-28714
|     	CVE-2021-28038	6.5	https://vulners.com/cve/CVE-2021-28038
|     	CVE-2020-29373	6.5	https://vulners.com/cve/CVE-2020-29373
|     	CVE-2020-26541	6.5	https://vulners.com/cve/CVE-2020-26541
|     	CVE-2020-10690	6.5	https://vulners.com/cve/CVE-2020-10690
|     	CVE-2019-5108	6.5	https://vulners.com/cve/CVE-2019-5108
|     	CVE-2019-3874	6.5	https://vulners.com/cve/CVE-2019-3874
|     	CVE-2019-3460	6.5	https://vulners.com/cve/CVE-2019-3460
|     	CVE-2019-3459	6.5	https://vulners.com/cve/CVE-2019-3459
|     	CVE-2019-19046	6.5	https://vulners.com/cve/CVE-2019-19046
|     	CVE-2019-17351	6.5	https://vulners.com/cve/CVE-2019-17351
|     	CVE-2019-10638	6.5	https://vulners.com/cve/CVE-2019-10638
|     	CVE-2018-15572	6.5	https://vulners.com/cve/CVE-2018-15572
|     	CVE-2018-1066	6.5	https://vulners.com/cve/CVE-2018-1066
|     	CVE-2017-2596	6.5	https://vulners.com/cve/CVE-2017-2596
|     	CVE-2017-17741	6.5	https://vulners.com/cve/CVE-2017-17741
|     	CVE-2017-12190	6.5	https://vulners.com/cve/CVE-2017-12190
|     	CVE-2017-10911	6.5	https://vulners.com/cve/CVE-2017-10911
|     	CVE-2016-5412	6.5	https://vulners.com/cve/CVE-2016-5412
|     	CVE-2016-10318	6.5	https://vulners.com/cve/CVE-2016-10318
|     	CVE-2015-7513	6.5	https://vulners.com/cve/CVE-2015-7513
|     	CAF53201-1371-591C-BFC7-4BA2A958F08A	6.5	https://vulners.com/githubexploit/CAF53201-1371-591C-BFC7-4BA2A958F08A	*EXPLOIT*
|     	294A2C02-1F46-5A48-915D-92DDD89915A1	6.5	https://vulners.com/githubexploit/294A2C02-1F46-5A48-915D-92DDD89915A1	*EXPLOIT*
|     	CVE-2023-45863	6.4	https://vulners.com/cve/CVE-2023-45863
|     	CVE-2023-3863	6.4	https://vulners.com/cve/CVE-2023-3863
|     	CVE-2023-33203	6.4	https://vulners.com/cve/CVE-2023-33203
|     	CVE-2023-30772	6.4	https://vulners.com/cve/CVE-2023-30772
|     	CVE-2022-45888	6.4	https://vulners.com/cve/CVE-2022-45888
|     	CVE-2022-44034	6.4	https://vulners.com/cve/CVE-2022-44034
|     	CVE-2022-44033	6.4	https://vulners.com/cve/CVE-2022-44033
|     	CVE-2022-44032	6.4	https://vulners.com/cve/CVE-2022-44032
|     	CVE-2021-37159	6.4	https://vulners.com/cve/CVE-2021-37159
|     	CVE-2021-3573	6.4	https://vulners.com/cve/CVE-2021-3573
|     	CVE-2021-20261	6.4	https://vulners.com/cve/CVE-2021-20261
|     	CVE-2020-25285	6.4	https://vulners.com/cve/CVE-2020-25285
|     	CVE-2019-15214	6.4	https://vulners.com/cve/CVE-2019-15214
|     	CVE-2017-8831	6.4	https://vulners.com/cve/CVE-2017-8831
|     	CVE-2023-40791	6.3	https://vulners.com/cve/CVE-2023-40791
|     	CVE-2023-1855	6.3	https://vulners.com/cve/CVE-2023-1855
|     	CVE-2023-1611	6.3	https://vulners.com/cve/CVE-2023-1611
|     	CVE-2022-36280	6.3	https://vulners.com/cve/CVE-2022-36280
|     	CVE-2022-1280	6.3	https://vulners.com/cve/CVE-2022-1280
|     	CVE-2019-19529	6.3	https://vulners.com/cve/CVE-2019-19529
|     	CVE-2018-12633	6.3	https://vulners.com/cve/CVE-2018-12633
|     	CVE-2017-15102	6.3	https://vulners.com/cve/CVE-2017-15102
|     	CVE-2016-5728	6.3	https://vulners.com/cve/CVE-2016-5728
|     	SSV:87007	6.2	https://vulners.com/seebug/SSV:87007	*EXPLOIT*
|     	SSV:61159	6.2	https://vulners.com/seebug/SSV:61159	*EXPLOIT*
|     	EXPLOITPACK:BF6D2794135FA3148CDCFB0D89F0F202	6.2	https://vulners.com/exploitpack/EXPLOITPACK:BF6D2794135FA3148CDCFB0D89F0F202	*EXPLOIT*
|     	EDB-ID:34923	6.2	https://vulners.com/exploitdb/EDB-ID:34923	*EXPLOIT*
|     	EDB-ID:33824	6.2	https://vulners.com/exploitdb/EDB-ID:33824	*EXPLOIT*
|     	CVE-2023-6915	6.2	https://vulners.com/cve/CVE-2023-6915
|     	CVE-2023-3108	6.2	https://vulners.com/cve/CVE-2023-3108
|     	CVE-2021-30002	6.2	https://vulners.com/cve/CVE-2021-30002
|     	CVE-2019-3016	6.2	https://vulners.com/cve/CVE-2019-3016
|     	CVE-2019-14284	6.2	https://vulners.com/cve/CVE-2019-14284
|     	CVE-2016-7042	6.2	https://vulners.com/cve/CVE-2016-7042
|     	CVE-2016-4482	6.2	https://vulners.com/cve/CVE-2016-4482
|     	CVE-2016-2847	6.2	https://vulners.com/cve/CVE-2016-2847
|     	CVE-2016-2549	6.2	https://vulners.com/cve/CVE-2016-2549
|     	CVE-2016-2548	6.2	https://vulners.com/cve/CVE-2016-2548
|     	CVE-2016-2543	6.2	https://vulners.com/cve/CVE-2016-2543
|     	CVE-2015-8785	6.2	https://vulners.com/cve/CVE-2015-8785
|     	CVE-2015-8767	6.2	https://vulners.com/cve/CVE-2015-8767
|     	CVE-2015-3339	6.2	https://vulners.com/cve/CVE-2015-3339
|     	CVE-2015-1339	6.2	https://vulners.com/cve/CVE-2015-1339
|     	CVE-2014-5207	6.2	https://vulners.com/cve/CVE-2014-5207
|     	CVE-2014-5045	6.2	https://vulners.com/cve/CVE-2014-5045
|     	CVE-2014-4014	6.2	https://vulners.com/cve/CVE-2014-4014
|     	CVE-2013-6368	6.2	https://vulners.com/cve/CVE-2013-6368
|     	CVE-2013-4312	6.2	https://vulners.com/cve/CVE-2013-4312
|     	CVE-2013-2888	6.2	https://vulners.com/cve/CVE-2013-2888
|     	1337DAY-ID-22363	6.2	https://vulners.com/zdt/1337DAY-ID-22363	*EXPLOIT*
|     	SSV:61742	6.1	https://vulners.com/seebug/SSV:61742	*EXPLOIT*
|     	CVE-2023-39193	6.1	https://vulners.com/cve/CVE-2023-39193
|     	CVE-2022-39842	6.1	https://vulners.com/cve/CVE-2022-39842
|     	CVE-2022-1508	6.1	https://vulners.com/cve/CVE-2022-1508
|     	CVE-2020-8647	6.1	https://vulners.com/cve/CVE-2020-8647
|     	CVE-2020-10751	6.1	https://vulners.com/cve/CVE-2020-10751
|     	CVE-2019-19602	6.1	https://vulners.com/cve/CVE-2019-19602
|     	CVE-2019-19528	6.1	https://vulners.com/cve/CVE-2019-19528
|     	CVE-2018-16658	6.1	https://vulners.com/cve/CVE-2018-16658
|     	CVE-2016-8658	6.1	https://vulners.com/cve/CVE-2016-8658
|     	CVE-2015-8956	6.1	https://vulners.com/cve/CVE-2015-8956
|     	CVE-2015-5156	6.1	https://vulners.com/cve/CVE-2015-5156
|     	CVE-2014-9717	6.1	https://vulners.com/cve/CVE-2014-9717
|     	CVE-2014-8884	6.1	https://vulners.com/cve/CVE-2014-8884
|     	CVE-2014-2309	6.1	https://vulners.com/cve/CVE-2014-2309
|     	CVE-2013-7027	6.1	https://vulners.com/cve/CVE-2013-7027
|     	CVE-2013-4387	6.1	https://vulners.com/cve/CVE-2013-4387
|     	SSV:87322	6.0	https://vulners.com/seebug/SSV:87322	*EXPLOIT*
|     	PACKETSTORM:128595	6.0	https://vulners.com/packetstorm/PACKETSTORM:128595	*EXPLOIT*
|     	EXPLOITPACK:F8053CF56EBE8E6A9E4404FBAF8824B6	6.0	https://vulners.com/exploitpack/EXPLOITPACK:F8053CF56EBE8E6A9E4404FBAF8824B6	*EXPLOIT*
|     	CVE-2023-5090	6.0	https://vulners.com/cve/CVE-2023-5090
|     	CVE-2023-39189	6.0	https://vulners.com/cve/CVE-2023-39189
|     	CVE-2020-27171	6.0	https://vulners.com/cve/CVE-2020-27171
|     	CVE-2020-25211	6.0	https://vulners.com/cve/CVE-2020-25211
|     	CVE-2020-11565	6.0	https://vulners.com/cve/CVE-2020-11565
|     	CVE-2017-12168	6.0	https://vulners.com/cve/CVE-2017-12168
|     	CVE-2013-4299	6.0	https://vulners.com/cve/CVE-2013-4299
|     	1337DAY-ID-22736	6.0	https://vulners.com/zdt/1337DAY-ID-22736	*EXPLOIT*
|     	CVE-2020-8649	5.9	https://vulners.com/cve/CVE-2020-8649
|     	CVE-2020-36516	5.9	https://vulners.com/cve/CVE-2020-36516
|     	CVE-2020-28097	5.9	https://vulners.com/cve/CVE-2020-28097
|     	CVE-2020-10711	5.9	https://vulners.com/cve/CVE-2020-10711
|     	CVE-2019-19081	5.9	https://vulners.com/cve/CVE-2019-19081
|     	CVE-2019-19080	5.9	https://vulners.com/cve/CVE-2019-19080
|     	CVE-2019-19076	5.9	https://vulners.com/cve/CVE-2019-19076
|     	CVE-2018-12232	5.9	https://vulners.com/cve/CVE-2018-12232
|     	CVE-2018-1108	5.9	https://vulners.com/cve/CVE-2018-1108
|     	CVE-2013-7470	5.9	https://vulners.com/cve/CVE-2013-7470
|     	CVE-2020-28915	5.8	https://vulners.com/cve/CVE-2020-28915
|     	CVE-2015-7990	5.8	https://vulners.com/cve/CVE-2015-7990
|     	CVE-2013-4345	5.8	https://vulners.com/cve/CVE-2013-4345
|     	75991DB8-5059-57ED-BB85-3A5F3309F92C	5.8	https://vulners.com/githubexploit/75991DB8-5059-57ED-BB85-3A5F3309F92C	*EXPLOIT*
|     	5ACF6B43-1E0E-55AE-A3C6-2FFCB8E95A05	5.8	https://vulners.com/githubexploit/5ACF6B43-1E0E-55AE-A3C6-2FFCB8E95A05	*EXPLOIT*
|     	SSV:61158	5.7	https://vulners.com/seebug/SSV:61158	*EXPLOIT*
|     	CVE-2023-23039	5.7	https://vulners.com/cve/CVE-2023-23039
|     	CVE-2023-1206	5.7	https://vulners.com/cve/CVE-2023-1206
|     	CVE-2022-3533	5.7	https://vulners.com/cve/CVE-2022-3533
|     	CVE-2020-27825	5.7	https://vulners.com/cve/CVE-2020-27825
|     	CVE-2013-6367	5.7	https://vulners.com/cve/CVE-2013-6367
|     	SAINT:C4918A16B528F26790825558E8BF5A72	5.6	https://vulners.com/saint/SAINT:C4918A16B528F26790825558E8BF5A72	*EXPLOIT*
|     	PACKETSTORM:132334	5.6	https://vulners.com/packetstorm/PACKETSTORM:132334	*EXPLOIT*
|     	EDB-ID:51384	5.6	https://vulners.com/exploitdb/EDB-ID:51384	*EXPLOIT*
|     	CVE-2023-1998	5.6	https://vulners.com/cve/CVE-2023-1998
|     	CVE-2020-14390	5.6	https://vulners.com/cve/CVE-2020-14390
|     	CVE-2019-7308	5.6	https://vulners.com/cve/CVE-2019-7308
|     	CVE-2019-3887	5.6	https://vulners.com/cve/CVE-2019-3887
|     	1337DAY-ID-38613	5.6	https://vulners.com/zdt/1337DAY-ID-38613	*EXPLOIT*
|     	SSV:62125	5.5	https://vulners.com/seebug/SSV:62125	*EXPLOIT*
|     	SSV:62091	5.5	https://vulners.com/seebug/SSV:62091	*EXPLOIT*
|     	MSF:EXPLOIT-LINUX-LOCAL-RDS_ATOMIC_FREE_OP_NULL_POINTER_DEREF_PRIV_ESC-	5.5	https://vulners.com/metasploit/MSF:EXPLOIT-LINUX-LOCAL-RDS_ATOMIC_FREE_OP_NULL_POINTER_DEREF_PRIV_ESC-	*EXPLOIT*
|     	MSF:EXPLOIT-LINUX-HTTP-ROXY_WI_EXEC-	5.5	https://vulners.com/metasploit/MSF:EXPLOIT-LINUX-HTTP-ROXY_WI_EXEC-	*EXPLOIT*
|     	EDB-ID:47957	5.5	https://vulners.com/exploitdb/EDB-ID:47957	*EXPLOIT*
|     	EDB-ID:46529	5.5	https://vulners.com/exploitdb/EDB-ID:46529	*EXPLOIT*
|     	EDB-ID:45983	5.5	https://vulners.com/exploitdb/EDB-ID:45983	*EXPLOIT*
|     	EDB-ID:45175	5.5	https://vulners.com/exploitdb/EDB-ID:45175	*EXPLOIT*
|     	EDB-ID:42932	5.5	https://vulners.com/exploitdb/EDB-ID:42932	*EXPLOIT*
|     	EDB-ID:42136	5.5	https://vulners.com/exploitdb/EDB-ID:42136	*EXPLOIT*
|     	EDB-ID:40731	5.5	https://vulners.com/exploitdb/EDB-ID:40731	*EXPLOIT*
|     	CVE-2024-39292	5.5	https://vulners.com/cve/CVE-2024-39292
|     	CVE-2024-38780	5.5	https://vulners.com/cve/CVE-2024-38780
|     	CVE-2024-36902	5.5	https://vulners.com/cve/CVE-2024-36902
|     	CVE-2024-36901	5.5	https://vulners.com/cve/CVE-2024-36901
|     	CVE-2024-36897	5.5	https://vulners.com/cve/CVE-2024-36897
|     	CVE-2024-36893	5.5	https://vulners.com/cve/CVE-2024-36893
|     	CVE-2024-36481	5.5	https://vulners.com/cve/CVE-2024-36481
|     	CVE-2024-36288	5.5	https://vulners.com/cve/CVE-2024-36288
|     	CVE-2024-36023	5.5	https://vulners.com/cve/CVE-2024-36023
|     	CVE-2024-35997	5.5	https://vulners.com/cve/CVE-2024-35997
|     	CVE-2024-27013	5.5	https://vulners.com/cve/CVE-2024-27013
|     	CVE-2024-26978	5.5	https://vulners.com/cve/CVE-2024-26978
|     	CVE-2024-26949	5.5	https://vulners.com/cve/CVE-2024-26949
|     	CVE-2024-26903	5.5	https://vulners.com/cve/CVE-2024-26903
|     	CVE-2024-26902	5.5	https://vulners.com/cve/CVE-2024-26902
|     	CVE-2024-26901	5.5	https://vulners.com/cve/CVE-2024-26901
|     	CVE-2024-26606	5.5	https://vulners.com/cve/CVE-2024-26606
|     	CVE-2024-26601	5.5	https://vulners.com/cve/CVE-2024-26601
|     	CVE-2024-26600	5.5	https://vulners.com/cve/CVE-2024-26600
|     	CVE-2024-26591	5.5	https://vulners.com/cve/CVE-2024-26591
|     	CVE-2024-26587	5.5	https://vulners.com/cve/CVE-2024-26587
|     	CVE-2024-25740	5.5	https://vulners.com/cve/CVE-2024-25740
|     	CVE-2024-25739	5.5	https://vulners.com/cve/CVE-2024-25739
|     	CVE-2024-23851	5.5	https://vulners.com/cve/CVE-2024-23851
|     	CVE-2024-23850	5.5	https://vulners.com/cve/CVE-2024-23850
|     	CVE-2024-23849	5.5	https://vulners.com/cve/CVE-2024-23849
|     	CVE-2024-23848	5.5	https://vulners.com/cve/CVE-2024-23848
|     	CVE-2024-0641	5.5	https://vulners.com/cve/CVE-2024-0641
|     	CVE-2024-0639	5.5	https://vulners.com/cve/CVE-2024-0639
|     	CVE-2024-0340	5.5	https://vulners.com/cve/CVE-2024-0340
|     	CVE-2023-7192	5.5	https://vulners.com/cve/CVE-2023-7192
|     	CVE-2023-6622	5.5	https://vulners.com/cve/CVE-2023-6622
|     	CVE-2023-6560	5.5	https://vulners.com/cve/CVE-2023-6560
|     	CVE-2023-6039	5.5	https://vulners.com/cve/CVE-2023-6039
|     	CVE-2023-52821	5.5	https://vulners.com/cve/CVE-2023-52821
|     	CVE-2023-52817	5.5	https://vulners.com/cve/CVE-2023-52817
|     	CVE-2023-52815	5.5	https://vulners.com/cve/CVE-2023-52815
|     	CVE-2023-52814	5.5	https://vulners.com/cve/CVE-2023-52814
|     	CVE-2023-52809	5.5	https://vulners.com/cve/CVE-2023-52809
|     	CVE-2023-52806	5.5	https://vulners.com/cve/CVE-2023-52806
|     	CVE-2023-52753	5.5	https://vulners.com/cve/CVE-2023-52753
|     	CVE-2023-52462	5.5	https://vulners.com/cve/CVE-2023-52462
|     	CVE-2023-52458	5.5	https://vulners.com/cve/CVE-2023-52458
|     	CVE-2023-52449	5.5	https://vulners.com/cve/CVE-2023-52449
|     	CVE-2023-52443	5.5	https://vulners.com/cve/CVE-2023-52443
|     	CVE-2023-52435	5.5	https://vulners.com/cve/CVE-2023-52435
|     	CVE-2023-52429	5.5	https://vulners.com/cve/CVE-2023-52429
|     	CVE-2023-50431	5.5	https://vulners.com/cve/CVE-2023-50431
|     	CVE-2023-46343	5.5	https://vulners.com/cve/CVE-2023-46343
|     	CVE-2023-45862	5.5	https://vulners.com/cve/CVE-2023-45862
|     	CVE-2023-4569	5.5	https://vulners.com/cve/CVE-2023-4569
|     	CVE-2023-4459	5.5	https://vulners.com/cve/CVE-2023-4459
|     	CVE-2023-4385	5.5	https://vulners.com/cve/CVE-2023-4385
|     	CVE-2023-42754	5.5	https://vulners.com/cve/CVE-2023-42754
|     	CVE-2023-42752	5.5	https://vulners.com/cve/CVE-2023-42752
|     	CVE-2023-4194	5.5	https://vulners.com/cve/CVE-2023-4194
|     	CVE-2023-4133	5.5	https://vulners.com/cve/CVE-2023-4133
|     	CVE-2023-4132	5.5	https://vulners.com/cve/CVE-2023-4132
|     	CVE-2023-38409	5.5	https://vulners.com/cve/CVE-2023-38409
|     	CVE-2023-37454	5.5	https://vulners.com/cve/CVE-2023-37454
|     	CVE-2023-34256	5.5	https://vulners.com/cve/CVE-2023-34256
|     	CVE-2023-3359	5.5	https://vulners.com/cve/CVE-2023-3359
|     	CVE-2023-3358	5.5	https://vulners.com/cve/CVE-2023-3358
|     	CVE-2023-3357	5.5	https://vulners.com/cve/CVE-2023-3357
|     	CVE-2023-3355	5.5	https://vulners.com/cve/CVE-2023-3355
|     	CVE-2023-3220	5.5	https://vulners.com/cve/CVE-2023-3220
|     	CVE-2023-3161	5.5	https://vulners.com/cve/CVE-2023-3161
|     	CVE-2023-3022	5.5	https://vulners.com/cve/CVE-2023-3022
|     	CVE-2023-3006	5.5	https://vulners.com/cve/CVE-2023-3006
|     	CVE-2023-2985	5.5	https://vulners.com/cve/CVE-2023-2985
|     	CVE-2023-28328	5.5	https://vulners.com/cve/CVE-2023-28328
|     	CVE-2023-28327	5.5	https://vulners.com/cve/CVE-2023-28327
|     	CVE-2023-2430	5.5	https://vulners.com/cve/CVE-2023-2430
|     	CVE-2023-23455	5.5	https://vulners.com/cve/CVE-2023-23455
|     	CVE-2023-23454	5.5	https://vulners.com/cve/CVE-2023-23454
|     	CVE-2023-23006	5.5	https://vulners.com/cve/CVE-2023-23006
|     	CVE-2023-23005	5.5	https://vulners.com/cve/CVE-2023-23005
|     	CVE-2023-23004	5.5	https://vulners.com/cve/CVE-2023-23004
|     	CVE-2023-23002	5.5	https://vulners.com/cve/CVE-2023-23002
|     	CVE-2023-23001	5.5	https://vulners.com/cve/CVE-2023-23001
|     	CVE-2023-23000	5.5	https://vulners.com/cve/CVE-2023-23000
|     	CVE-2023-22999	5.5	https://vulners.com/cve/CVE-2023-22999
|     	CVE-2023-22998	5.5	https://vulners.com/cve/CVE-2023-22998
|     	CVE-2023-22997	5.5	https://vulners.com/cve/CVE-2023-22997
|     	CVE-2023-22996	5.5	https://vulners.com/cve/CVE-2023-22996
|     	CVE-2023-2177	5.5	https://vulners.com/cve/CVE-2023-2177
|     	CVE-2023-2166	5.5	https://vulners.com/cve/CVE-2023-2166
|     	CVE-2023-2162	5.5	https://vulners.com/cve/CVE-2023-2162
|     	CVE-2023-1637	5.5	https://vulners.com/cve/CVE-2023-1637
|     	CVE-2023-1583	5.5	https://vulners.com/cve/CVE-2023-1583
|     	CVE-2023-1249	5.5	https://vulners.com/cve/CVE-2023-1249
|     	CVE-2023-1195	5.5	https://vulners.com/cve/CVE-2023-1195
|     	CVE-2023-1095	5.5	https://vulners.com/cve/CVE-2023-1095
|     	CVE-2023-0615	5.5	https://vulners.com/cve/CVE-2023-0615
|     	CVE-2023-0597	5.5	https://vulners.com/cve/CVE-2023-0597
|     	CVE-2023-0469	5.5	https://vulners.com/cve/CVE-2023-0469
|     	CVE-2023-0394	5.5	https://vulners.com/cve/CVE-2023-0394
|     	CVE-2023-0160	5.5	https://vulners.com/cve/CVE-2023-0160
|     	CVE-2022-48659	5.5	https://vulners.com/cve/CVE-2022-48659
|     	CVE-2022-48619	5.5	https://vulners.com/cve/CVE-2022-48619
|     	CVE-2022-4842	5.5	https://vulners.com/cve/CVE-2022-4842
|     	CVE-2022-47929	5.5	https://vulners.com/cve/CVE-2022-47929
|     	CVE-2022-4662	5.5	https://vulners.com/cve/CVE-2022-4662
|     	CVE-2022-45869	5.5	https://vulners.com/cve/CVE-2022-45869
|     	CVE-2022-42703	5.5	https://vulners.com/cve/CVE-2022-42703
|     	CVE-2022-4269	5.5	https://vulners.com/cve/CVE-2022-4269
|     	CVE-2022-42329	5.5	https://vulners.com/cve/CVE-2022-42329
|     	CVE-2022-42328	5.5	https://vulners.com/cve/CVE-2022-42328
|     	CVE-2022-4129	5.5	https://vulners.com/cve/CVE-2022-4129
|     	CVE-2022-4128	5.5	https://vulners.com/cve/CVE-2022-4128
|     	CVE-2022-4127	5.5	https://vulners.com/cve/CVE-2022-4127
|     	CVE-2022-41218	5.5	https://vulners.com/cve/CVE-2022-41218
|     	CVE-2022-40768	5.5	https://vulners.com/cve/CVE-2022-40768
|     	CVE-2022-40476	5.5	https://vulners.com/cve/CVE-2022-40476
|     	CVE-2022-39190	5.5	https://vulners.com/cve/CVE-2022-39190
|     	CVE-2022-3707	5.5	https://vulners.com/cve/CVE-2022-3707
|     	CVE-2022-36879	5.5	https://vulners.com/cve/CVE-2022-36879
|     	CVE-2022-3606	5.5	https://vulners.com/cve/CVE-2022-3606
|     	CVE-2022-3595	5.5	https://vulners.com/cve/CVE-2022-3595
|     	CVE-2022-3586	5.5	https://vulners.com/cve/CVE-2022-3586
|     	CVE-2022-3544	5.5	https://vulners.com/cve/CVE-2022-3544
|     	CVE-2022-3543	5.5	https://vulners.com/cve/CVE-2022-3543
|     	CVE-2022-34495	5.5	https://vulners.com/cve/CVE-2022-34495
|     	CVE-2022-34494	5.5	https://vulners.com/cve/CVE-2022-34494
|     	CVE-2022-3344	5.5	https://vulners.com/cve/CVE-2022-3344
|     	CVE-2022-3169	5.5	https://vulners.com/cve/CVE-2022-3169
|     	CVE-2022-3115	5.5	https://vulners.com/cve/CVE-2022-3115
|     	CVE-2022-3114	5.5	https://vulners.com/cve/CVE-2022-3114
|     	CVE-2022-3113	5.5	https://vulners.com/cve/CVE-2022-3113
|     	CVE-2022-3112	5.5	https://vulners.com/cve/CVE-2022-3112
|     	CVE-2022-3111	5.5	https://vulners.com/cve/CVE-2022-3111
|     	CVE-2022-3110	5.5	https://vulners.com/cve/CVE-2022-3110
|     	CVE-2022-3108	5.5	https://vulners.com/cve/CVE-2022-3108
|     	CVE-2022-3107	5.5	https://vulners.com/cve/CVE-2022-3107
|     	CVE-2022-3106	5.5	https://vulners.com/cve/CVE-2022-3106
|     	CVE-2022-3105	5.5	https://vulners.com/cve/CVE-2022-3105
|     	CVE-2022-3104	5.5	https://vulners.com/cve/CVE-2022-3104
|     	CVE-2022-3078	5.5	https://vulners.com/cve/CVE-2022-3078
|     	CVE-2022-3077	5.5	https://vulners.com/cve/CVE-2022-3077
|     	CVE-2022-3061	5.5	https://vulners.com/cve/CVE-2022-3061
|     	CVE-2022-2905	5.5	https://vulners.com/cve/CVE-2022-2905
|     	CVE-2022-2873	5.5	https://vulners.com/cve/CVE-2022-2873
|     	CVE-2022-28389	5.5	https://vulners.com/cve/CVE-2022-28389
|     	CVE-2022-28388	5.5	https://vulners.com/cve/CVE-2022-28388
|     	CVE-2022-28356	5.5	https://vulners.com/cve/CVE-2022-28356
|     	CVE-2022-27950	5.5	https://vulners.com/cve/CVE-2022-27950
|     	CVE-2022-26966	5.5	https://vulners.com/cve/CVE-2022-26966
|     	CVE-2022-26878	5.5	https://vulners.com/cve/CVE-2022-26878
|     	CVE-2022-25375	5.5	https://vulners.com/cve/CVE-2022-25375
|     	CVE-2022-24959	5.5	https://vulners.com/cve/CVE-2022-24959
|     	CVE-2022-2380	5.5	https://vulners.com/cve/CVE-2022-2380
|     	CVE-2022-2318	5.5	https://vulners.com/cve/CVE-2022-2318
|     	CVE-2022-2153	5.5	https://vulners.com/cve/CVE-2022-2153
|     	CVE-2022-2078	5.5	https://vulners.com/cve/CVE-2022-2078
|     	CVE-2022-1975	5.5	https://vulners.com/cve/CVE-2022-1975
|     	CVE-2022-1852	5.5	https://vulners.com/cve/CVE-2022-1852
|     	CVE-2022-1516	5.5	https://vulners.com/cve/CVE-2022-1516
|     	CVE-2022-1263	5.5	https://vulners.com/cve/CVE-2022-1263
|     	CVE-2022-1204	5.5	https://vulners.com/cve/CVE-2022-1204
|     	CVE-2022-1198	5.5	https://vulners.com/cve/CVE-2022-1198
|     	CVE-2022-1195	5.5	https://vulners.com/cve/CVE-2022-1195
|     	CVE-2022-1184	5.5	https://vulners.com/cve/CVE-2022-1184
|     	CVE-2022-1016	5.5	https://vulners.com/cve/CVE-2022-1016
|     	CVE-2022-0854	5.5	https://vulners.com/cve/CVE-2022-0854
|     	CVE-2022-0617	5.5	https://vulners.com/cve/CVE-2022-0617
|     	CVE-2022-0487	5.5	https://vulners.com/cve/CVE-2022-0487
|     	CVE-2022-0480	5.5	https://vulners.com/cve/CVE-2022-0480
|     	CVE-2022-0433	5.5	https://vulners.com/cve/CVE-2022-0433
|     	CVE-2022-0382	5.5	https://vulners.com/cve/CVE-2022-0382
|     	CVE-2022-0322	5.5	https://vulners.com/cve/CVE-2022-0322
|     	CVE-2022-0264	5.5	https://vulners.com/cve/CVE-2022-0264
|     	CVE-2022-0171	5.5	https://vulners.com/cve/CVE-2022-0171
|     	CVE-2021-47550	5.5	https://vulners.com/cve/CVE-2021-47550
|     	CVE-2021-47542	5.5	https://vulners.com/cve/CVE-2021-47542
|     	CVE-2021-47522	5.5	https://vulners.com/cve/CVE-2021-47522
|     	CVE-2021-47193	5.5	https://vulners.com/cve/CVE-2021-47193
|     	CVE-2021-47173	5.5	https://vulners.com/cve/CVE-2021-47173
|     	CVE-2021-47171	5.5	https://vulners.com/cve/CVE-2021-47171
|     	CVE-2021-46939	5.5	https://vulners.com/cve/CVE-2021-46939
|     	CVE-2021-46932	5.5	https://vulners.com/cve/CVE-2021-46932
|     	CVE-2021-46928	5.5	https://vulners.com/cve/CVE-2021-46928
|     	CVE-2021-46926	5.5	https://vulners.com/cve/CVE-2021-46926
|     	CVE-2021-46906	5.5	https://vulners.com/cve/CVE-2021-46906
|     	CVE-2021-46905	5.5	https://vulners.com/cve/CVE-2021-46905
|     	CVE-2021-46904	5.5	https://vulners.com/cve/CVE-2021-46904
|     	CVE-2021-46283	5.5	https://vulners.com/cve/CVE-2021-46283
|     	CVE-2021-45868	5.5	https://vulners.com/cve/CVE-2021-45868
|     	CVE-2021-45480	5.5	https://vulners.com/cve/CVE-2021-45480
|     	CVE-2021-45402	5.5	https://vulners.com/cve/CVE-2021-45402
|     	CVE-2021-45095	5.5	https://vulners.com/cve/CVE-2021-45095
|     	CVE-2021-44879	5.5	https://vulners.com/cve/CVE-2021-44879
|     	CVE-2021-43389	5.5	https://vulners.com/cve/CVE-2021-43389
|     	CVE-2021-4155	5.5	https://vulners.com/cve/CVE-2021-4155
|     	CVE-2021-4150	5.5	https://vulners.com/cve/CVE-2021-4150
|     	CVE-2021-4149	5.5	https://vulners.com/cve/CVE-2021-4149
|     	CVE-2021-4148	5.5	https://vulners.com/cve/CVE-2021-4148
|     	CVE-2021-4135	5.5	https://vulners.com/cve/CVE-2021-4135
|     	CVE-2021-4095	5.5	https://vulners.com/cve/CVE-2021-4095
|     	CVE-2021-4023	5.5	https://vulners.com/cve/CVE-2021-4023
|     	CVE-2021-38208	5.5	https://vulners.com/cve/CVE-2021-38208
|     	CVE-2021-38206	5.5	https://vulners.com/cve/CVE-2021-38206
|     	CVE-2021-38203	5.5	https://vulners.com/cve/CVE-2021-38203
|     	CVE-2021-38200	5.5	https://vulners.com/cve/CVE-2021-38200
|     	CVE-2021-38198	5.5	https://vulners.com/cve/CVE-2021-38198
|     	CVE-2021-3764	5.5	https://vulners.com/cve/CVE-2021-3764
|     	CVE-2021-3759	5.5	https://vulners.com/cve/CVE-2021-3759
|     	CVE-2021-3744	5.5	https://vulners.com/cve/CVE-2021-3744
|     	CVE-2021-3736	5.5	https://vulners.com/cve/CVE-2021-3736
|     	CVE-2021-3732	5.5	https://vulners.com/cve/CVE-2021-3732
|     	CVE-2021-3679	5.5	https://vulners.com/cve/CVE-2021-3679
|     	CVE-2021-3659	5.5	https://vulners.com/cve/CVE-2021-3659
|     	CVE-2021-3564	5.5	https://vulners.com/cve/CVE-2021-3564
|     	CVE-2021-35477	5.5	https://vulners.com/cve/CVE-2021-35477
|     	CVE-2021-34693	5.5	https://vulners.com/cve/CVE-2021-34693
|     	CVE-2021-34556	5.5	https://vulners.com/cve/CVE-2021-34556
|     	CVE-2021-3428	5.5	https://vulners.com/cve/CVE-2021-3428
|     	CVE-2021-31829	5.5	https://vulners.com/cve/CVE-2021-31829
|     	CVE-2021-30178	5.5	https://vulners.com/cve/CVE-2021-30178
|     	CVE-2021-29650	5.5	https://vulners.com/cve/CVE-2021-29650
|     	CVE-2021-29649	5.5	https://vulners.com/cve/CVE-2021-29649
|     	CVE-2021-29648	5.5	https://vulners.com/cve/CVE-2021-29648
|     	CVE-2021-29647	5.5	https://vulners.com/cve/CVE-2021-29647
|     	CVE-2021-29646	5.5	https://vulners.com/cve/CVE-2021-29646
|     	CVE-2021-29264	5.5	https://vulners.com/cve/CVE-2021-29264
|     	CVE-2021-29155	5.5	https://vulners.com/cve/CVE-2021-29155
|     	CVE-2021-28971	5.5	https://vulners.com/cve/CVE-2021-28971
|     	CVE-2021-28951	5.5	https://vulners.com/cve/CVE-2021-28951
|     	CVE-2021-28950	5.5	https://vulners.com/cve/CVE-2021-28950
|     	CVE-2021-26932	5.5	https://vulners.com/cve/CVE-2021-26932
|     	CVE-2021-26931	5.5	https://vulners.com/cve/CVE-2021-26931
|     	CVE-2021-20320	5.5	https://vulners.com/cve/CVE-2021-20320
|     	CVE-2021-20265	5.5	https://vulners.com/cve/CVE-2021-20265
|     	CVE-2021-20219	5.5	https://vulners.com/cve/CVE-2021-20219
|     	CVE-2020-8992	5.5	https://vulners.com/cve/CVE-2020-8992
|     	CVE-2020-36775	5.5	https://vulners.com/cve/CVE-2020-36775
|     	CVE-2020-36691	5.5	https://vulners.com/cve/CVE-2020-36691
|     	CVE-2020-36322	5.5	https://vulners.com/cve/CVE-2020-36322
|     	CVE-2020-36312	5.5	https://vulners.com/cve/CVE-2020-36312
|     	CVE-2020-36311	5.5	https://vulners.com/cve/CVE-2020-36311
|     	CVE-2020-36310	5.5	https://vulners.com/cve/CVE-2020-36310
|     	CVE-2020-28941	5.5	https://vulners.com/cve/CVE-2020-28941
|     	CVE-2020-28588	5.5	https://vulners.com/cve/CVE-2020-28588
|     	CVE-2020-27830	5.5	https://vulners.com/cve/CVE-2020-27830
|     	CVE-2020-27673	5.5	https://vulners.com/cve/CVE-2020-27673
|     	CVE-2020-27194	5.5	https://vulners.com/cve/CVE-2020-27194
|     	CVE-2020-27152	5.5	https://vulners.com/cve/CVE-2020-27152
|     	CVE-2020-26088	5.5	https://vulners.com/cve/CVE-2020-26088
|     	CVE-2020-25704	5.5	https://vulners.com/cve/CVE-2020-25704
|     	CVE-2020-25673	5.5	https://vulners.com/cve/CVE-2020-25673
|     	CVE-2020-25641	5.5	https://vulners.com/cve/CVE-2020-25641
|     	CVE-2020-14385	5.5	https://vulners.com/cve/CVE-2020-14385
|     	CVE-2020-14314	5.5	https://vulners.com/cve/CVE-2020-14314
|     	CVE-2020-12771	5.5	https://vulners.com/cve/CVE-2020-12771
|     	CVE-2020-12769	5.5	https://vulners.com/cve/CVE-2020-12769
|     	CVE-2020-12768	5.5	https://vulners.com/cve/CVE-2020-12768
|     	CVE-2020-12656	5.5	https://vulners.com/cve/CVE-2020-12656
|     	CVE-2020-12655	5.5	https://vulners.com/cve/CVE-2020-12655
|     	CVE-2020-11669	5.5	https://vulners.com/cve/CVE-2020-11669
|     	CVE-2020-10781	5.5	https://vulners.com/cve/CVE-2020-10781
|     	CVE-2020-10774	5.5	https://vulners.com/cve/CVE-2020-10774
|     	CVE-2020-10769	5.5	https://vulners.com/cve/CVE-2020-10769
|     	CVE-2020-10768	5.5	https://vulners.com/cve/CVE-2020-10768
|     	CVE-2020-10767	5.5	https://vulners.com/cve/CVE-2020-10767
|     	CVE-2020-10766	5.5	https://vulners.com/cve/CVE-2020-10766
|     	CVE-2020-10720	5.5	https://vulners.com/cve/CVE-2020-10720
|     	CVE-2019-9857	5.5	https://vulners.com/cve/CVE-2019-9857
|     	CVE-2019-7222	5.5	https://vulners.com/cve/CVE-2019-7222
|     	CVE-2019-5489	5.5	https://vulners.com/cve/CVE-2019-5489
|     	CVE-2019-3882	5.5	https://vulners.com/cve/CVE-2019-3882
|     	CVE-2019-20812	5.5	https://vulners.com/cve/CVE-2019-20812
|     	CVE-2019-20811	5.5	https://vulners.com/cve/CVE-2019-20811
|     	CVE-2019-20810	5.5	https://vulners.com/cve/CVE-2019-20810
|     	CVE-2019-20422	5.5	https://vulners.com/cve/CVE-2019-20422
|     	CVE-2019-20096	5.5	https://vulners.com/cve/CVE-2019-20096
|     	CVE-2019-20095	5.5	https://vulners.com/cve/CVE-2019-20095
|     	CVE-2019-20054	5.5	https://vulners.com/cve/CVE-2019-20054
|     	CVE-2019-19922	5.5	https://vulners.com/cve/CVE-2019-19922
|     	CVE-2019-19767	5.5	https://vulners.com/cve/CVE-2019-19767
|     	CVE-2019-19462	5.5	https://vulners.com/cve/CVE-2019-19462
|     	CVE-2019-19338	5.5	https://vulners.com/cve/CVE-2019-19338
|     	CVE-2019-19227	5.5	https://vulners.com/cve/CVE-2019-19227
|     	CVE-2019-19077	5.5	https://vulners.com/cve/CVE-2019-19077
|     	CVE-2019-19055	5.5	https://vulners.com/cve/CVE-2019-19055
|     	CVE-2019-19051	5.5	https://vulners.com/cve/CVE-2019-19051
|     	CVE-2019-19047	5.5	https://vulners.com/cve/CVE-2019-19047
|     	CVE-2019-19043	5.5	https://vulners.com/cve/CVE-2019-19043
|     	CVE-2019-19039	5.5	https://vulners.com/cve/CVE-2019-19039
|     	CVE-2019-19037	5.5	https://vulners.com/cve/CVE-2019-19037
|     	CVE-2019-19036	5.5	https://vulners.com/cve/CVE-2019-19036
|     	CVE-2019-18885	5.5	https://vulners.com/cve/CVE-2019-18885
|     	CVE-2019-18811	5.5	https://vulners.com/cve/CVE-2019-18811
|     	CVE-2019-18808	5.5	https://vulners.com/cve/CVE-2019-18808
|     	CVE-2019-18806	5.5	https://vulners.com/cve/CVE-2019-18806
|     	CVE-2019-18786	5.5	https://vulners.com/cve/CVE-2019-18786
|     	CVE-2019-15924	5.5	https://vulners.com/cve/CVE-2019-15924
|     	CVE-2019-15923	5.5	https://vulners.com/cve/CVE-2019-15923
|     	CVE-2019-15922	5.5	https://vulners.com/cve/CVE-2019-15922
|     	CVE-2019-15118	5.5	https://vulners.com/cve/CVE-2019-15118
|     	CVE-2019-14763	5.5	https://vulners.com/cve/CVE-2019-14763
|     	CVE-2019-13648	5.5	https://vulners.com/cve/CVE-2019-13648
|     	CVE-2019-12984	5.5	https://vulners.com/cve/CVE-2019-12984
|     	CVE-2019-12819	5.5	https://vulners.com/cve/CVE-2019-12819
|     	CVE-2019-12455	5.5	https://vulners.com/cve/CVE-2019-12455
|     	CVE-2019-12382	5.5	https://vulners.com/cve/CVE-2019-12382
|     	CVE-2019-12381	5.5	https://vulners.com/cve/CVE-2019-12381
|     	CVE-2019-12380	5.5	https://vulners.com/cve/CVE-2019-12380
|     	CVE-2019-12379	5.5	https://vulners.com/cve/CVE-2019-12379
|     	CVE-2019-12378	5.5	https://vulners.com/cve/CVE-2019-12378
|     	CVE-2019-11833	5.5	https://vulners.com/cve/CVE-2019-11833
|     	CVE-2019-10207	5.5	https://vulners.com/cve/CVE-2019-10207
|     	CVE-2018-8087	5.5	https://vulners.com/cve/CVE-2018-8087
|     	CVE-2018-8043	5.5	https://vulners.com/cve/CVE-2018-8043
|     	CVE-2018-7757	5.5	https://vulners.com/cve/CVE-2018-7757
|     	CVE-2018-7755	5.5	https://vulners.com/cve/CVE-2018-7755
|     	CVE-2018-7754	5.5	https://vulners.com/cve/CVE-2018-7754
|     	CVE-2018-7740	5.5	https://vulners.com/cve/CVE-2018-7740
|     	CVE-2018-7492	5.5	https://vulners.com/cve/CVE-2018-7492
|     	CVE-2018-7273	5.5	https://vulners.com/cve/CVE-2018-7273
|     	CVE-2018-7191	5.5	https://vulners.com/cve/CVE-2018-7191
|     	CVE-2018-6554	5.5	https://vulners.com/cve/CVE-2018-6554
|     	CVE-2018-5995	5.5	https://vulners.com/cve/CVE-2018-5995
|     	CVE-2018-5953	5.5	https://vulners.com/cve/CVE-2018-5953
|     	CVE-2018-5803	5.5	https://vulners.com/cve/CVE-2018-5803
|     	CVE-2018-5750	5.5	https://vulners.com/cve/CVE-2018-5750
|     	CVE-2018-5333	5.5	https://vulners.com/cve/CVE-2018-5333
|     	CVE-2018-21008	5.5	https://vulners.com/cve/CVE-2018-21008
|     	CVE-2018-20511	5.5	https://vulners.com/cve/CVE-2018-20511
|     	CVE-2018-19407	5.5	https://vulners.com/cve/CVE-2018-19407
|     	CVE-2018-19406	5.5	https://vulners.com/cve/CVE-2018-19406
|     	CVE-2018-18710	5.5	https://vulners.com/cve/CVE-2018-18710
|     	CVE-2018-18690	5.5	https://vulners.com/cve/CVE-2018-18690
|     	CVE-2018-18397	5.5	https://vulners.com/cve/CVE-2018-18397
|     	CVE-2018-17972	5.5	https://vulners.com/cve/CVE-2018-17972
|     	CVE-2018-16885	5.5	https://vulners.com/cve/CVE-2018-16885
|     	CVE-2018-16862	5.5	https://vulners.com/cve/CVE-2018-16862
|     	CVE-2018-16597	5.5	https://vulners.com/cve/CVE-2018-16597
|     	CVE-2018-15594	5.5	https://vulners.com/cve/CVE-2018-15594
|     	CVE-2018-14646	5.5	https://vulners.com/cve/CVE-2018-14646
|     	CVE-2018-14617	5.5	https://vulners.com/cve/CVE-2018-14617
|     	CVE-2018-14616	5.5	https://vulners.com/cve/CVE-2018-14616
|     	CVE-2018-14615	5.5	https://vulners.com/cve/CVE-2018-14615
|     	CVE-2018-14614	5.5	https://vulners.com/cve/CVE-2018-14614
|     	CVE-2018-14613	5.5	https://vulners.com/cve/CVE-2018-14613
|     	CVE-2018-14612	5.5	https://vulners.com/cve/CVE-2018-14612
|     	CVE-2018-14611	5.5	https://vulners.com/cve/CVE-2018-14611
|     	CVE-2018-14610	5.5	https://vulners.com/cve/CVE-2018-14610
|     	CVE-2018-14609	5.5	https://vulners.com/cve/CVE-2018-14609
|     	CVE-2018-13100	5.5	https://vulners.com/cve/CVE-2018-13100
|     	CVE-2018-13099	5.5	https://vulners.com/cve/CVE-2018-13099
|     	CVE-2018-13098	5.5	https://vulners.com/cve/CVE-2018-13098
|     	CVE-2018-13097	5.5	https://vulners.com/cve/CVE-2018-13097
|     	CVE-2018-13096	5.5	https://vulners.com/cve/CVE-2018-13096
|     	CVE-2018-13095	5.5	https://vulners.com/cve/CVE-2018-13095
|     	CVE-2018-13094	5.5	https://vulners.com/cve/CVE-2018-13094
|     	CVE-2018-13093	5.5	https://vulners.com/cve/CVE-2018-13093
|     	CVE-2018-12896	5.5	https://vulners.com/cve/CVE-2018-12896
|     	CVE-2018-11508	5.5	https://vulners.com/cve/CVE-2018-11508
|     	CVE-2018-1130	5.5	https://vulners.com/cve/CVE-2018-1130
|     	CVE-2018-11232	5.5	https://vulners.com/cve/CVE-2018-11232
|     	CVE-2018-1095	5.5	https://vulners.com/cve/CVE-2018-1095
|     	CVE-2018-10940	5.5	https://vulners.com/cve/CVE-2018-10940
|     	CVE-2018-1094	5.5	https://vulners.com/cve/CVE-2018-1094
|     	CVE-2018-1093	5.5	https://vulners.com/cve/CVE-2018-1093
|     	CVE-2018-1092	5.5	https://vulners.com/cve/CVE-2018-1092
|     	CVE-2018-1091	5.5	https://vulners.com/cve/CVE-2018-1091
|     	CVE-2018-10883	5.5	https://vulners.com/cve/CVE-2018-10883
|     	CVE-2018-10881	5.5	https://vulners.com/cve/CVE-2018-10881
|     	CVE-2018-10880	5.5	https://vulners.com/cve/CVE-2018-10880
|     	CVE-2018-10323	5.5	https://vulners.com/cve/CVE-2018-10323
|     	CVE-2018-10322	5.5	https://vulners.com/cve/CVE-2018-10322
|     	CVE-2018-10124	5.5	https://vulners.com/cve/CVE-2018-10124
|     	CVE-2018-10087	5.5	https://vulners.com/cve/CVE-2018-10087
|     	CVE-2018-10074	5.5	https://vulners.com/cve/CVE-2018-10074
|     	CVE-2018-10021	5.5	https://vulners.com/cve/CVE-2018-10021
|     	CVE-2017-9605	5.5	https://vulners.com/cve/CVE-2017-9605
|     	CVE-2017-9242	5.5	https://vulners.com/cve/CVE-2017-9242
|     	CVE-2017-9211	5.5	https://vulners.com/cve/CVE-2017-9211
|     	CVE-2017-9150	5.5	https://vulners.com/cve/CVE-2017-9150
|     	CVE-2017-9059	5.5	https://vulners.com/cve/CVE-2017-9059
|     	CVE-2017-8925	5.5	https://vulners.com/cve/CVE-2017-8925
|     	CVE-2017-7616	5.5	https://vulners.com/cve/CVE-2017-7616
|     	CVE-2017-7542	5.5	https://vulners.com/cve/CVE-2017-7542
|     	CVE-2017-7495	5.5	https://vulners.com/cve/CVE-2017-7495
|     	CVE-2017-7472	5.5	https://vulners.com/cve/CVE-2017-7472
|     	CVE-2017-7346	5.5	https://vulners.com/cve/CVE-2017-7346
|     	CVE-2017-7261	5.5	https://vulners.com/cve/CVE-2017-7261
|     	CVE-2017-6951	5.5	https://vulners.com/cve/CVE-2017-6951
|     	CVE-2017-6353	5.5	https://vulners.com/cve/CVE-2017-6353
|     	CVE-2017-6348	5.5	https://vulners.com/cve/CVE-2017-6348
|     	CVE-2017-5986	5.5	https://vulners.com/cve/CVE-2017-5986
|     	CVE-2017-5577	5.5	https://vulners.com/cve/CVE-2017-5577
|     	CVE-2017-5550	5.5	https://vulners.com/cve/CVE-2017-5550
|     	CVE-2017-5549	5.5	https://vulners.com/cve/CVE-2017-5549
|     	CVE-2017-2671	5.5	https://vulners.com/cve/CVE-2017-2671
|     	CVE-2017-2618	5.5	https://vulners.com/cve/CVE-2017-2618
|     	CVE-2017-18550	5.5	https://vulners.com/cve/CVE-2017-18550
|     	CVE-2017-18549	5.5	https://vulners.com/cve/CVE-2017-18549
|     	CVE-2017-18360	5.5	https://vulners.com/cve/CVE-2017-18360
|     	CVE-2017-18344	5.5	https://vulners.com/cve/CVE-2017-18344
|     	CVE-2017-18261	5.5	https://vulners.com/cve/CVE-2017-18261
|     	CVE-2017-18257	5.5	https://vulners.com/cve/CVE-2017-18257
|     	CVE-2017-18241	5.5	https://vulners.com/cve/CVE-2017-18241
|     	CVE-2017-18232	5.5	https://vulners.com/cve/CVE-2017-18232
|     	CVE-2017-18221	5.5	https://vulners.com/cve/CVE-2017-18221
|     	CVE-2017-18216	5.5	https://vulners.com/cve/CVE-2017-18216
|     	CVE-2017-18208	5.5	https://vulners.com/cve/CVE-2017-18208
|     	CVE-2017-18204	5.5	https://vulners.com/cve/CVE-2017-18204
|     	CVE-2017-18200	5.5	https://vulners.com/cve/CVE-2017-18200
|     	CVE-2017-18193	5.5	https://vulners.com/cve/CVE-2017-18193
|     	CVE-2017-17975	5.5	https://vulners.com/cve/CVE-2017-17975
|     	CVE-2017-17862	5.5	https://vulners.com/cve/CVE-2017-17862
|     	CVE-2017-16994	5.5	https://vulners.com/cve/CVE-2017-16994
|     	CVE-2017-15537	5.5	https://vulners.com/cve/CVE-2017-15537
|     	CVE-2017-15306	5.5	https://vulners.com/cve/CVE-2017-15306
|     	CVE-2017-15299	5.5	https://vulners.com/cve/CVE-2017-15299
|     	CVE-2017-15274	5.5	https://vulners.com/cve/CVE-2017-15274
|     	CVE-2017-15128	5.5	https://vulners.com/cve/CVE-2017-15128
|     	CVE-2017-15127	5.5	https://vulners.com/cve/CVE-2017-15127
|     	CVE-2017-15116	5.5	https://vulners.com/cve/CVE-2017-15116
|     	CVE-2017-14991	5.5	https://vulners.com/cve/CVE-2017-14991
|     	CVE-2017-14954	5.5	https://vulners.com/cve/CVE-2017-14954
|     	CVE-2017-14489	5.5	https://vulners.com/cve/CVE-2017-14489
|     	CVE-2017-14340	5.5	https://vulners.com/cve/CVE-2017-14340
|     	CVE-2017-14156	5.5	https://vulners.com/cve/CVE-2017-14156
|     	CVE-2017-14140	5.5	https://vulners.com/cve/CVE-2017-14140
|     	CVE-2017-14106	5.5	https://vulners.com/cve/CVE-2017-14106
|     	CVE-2017-13695	5.5	https://vulners.com/cve/CVE-2017-13695
|     	CVE-2017-13694	5.5	https://vulners.com/cve/CVE-2017-13694
|     	CVE-2017-13693	5.5	https://vulners.com/cve/CVE-2017-13693
|     	CVE-2017-12193	5.5	https://vulners.com/cve/CVE-2017-12193
|     	CVE-2017-12192	5.5	https://vulners.com/cve/CVE-2017-12192
|     	CVE-2017-1000380	5.5	https://vulners.com/cve/CVE-2017-1000380
|     	CVE-2017-1000252	5.5	https://vulners.com/cve/CVE-2017-1000252
|     	CVE-2016-9756	5.5	https://vulners.com/cve/CVE-2016-9756
|     	CVE-2016-9685	5.5	https://vulners.com/cve/CVE-2016-9685
|     	CVE-2016-9588	5.5	https://vulners.com/cve/CVE-2016-9588
|     	CVE-2016-9191	5.5	https://vulners.com/cve/CVE-2016-9191
|     	CVE-2016-9178	5.5	https://vulners.com/cve/CVE-2016-9178
|     	CVE-2016-8660	5.5	https://vulners.com/cve/CVE-2016-8660
|     	CVE-2016-8650	5.5	https://vulners.com/cve/CVE-2016-8650
|     	CVE-2016-8646	5.5	https://vulners.com/cve/CVE-2016-8646
|     	CVE-2016-8645	5.5	https://vulners.com/cve/CVE-2016-8645
|     	CVE-2016-8630	5.5	https://vulners.com/cve/CVE-2016-8630
|     	CVE-2016-7916	5.5	https://vulners.com/cve/CVE-2016-7916
|     	CVE-2016-7915	5.5	https://vulners.com/cve/CVE-2016-7915
|     	CVE-2016-7914	5.5	https://vulners.com/cve/CVE-2016-7914
|     	CVE-2016-6828	5.5	https://vulners.com/cve/CVE-2016-6828
|     	CVE-2016-6327	5.5	https://vulners.com/cve/CVE-2016-6327
|     	CVE-2016-6198	5.5	https://vulners.com/cve/CVE-2016-6198
|     	CVE-2016-6197	5.5	https://vulners.com/cve/CVE-2016-6197
|     	CVE-2016-5243	5.5	https://vulners.com/cve/CVE-2016-5243
|     	CVE-2016-4581	5.5	https://vulners.com/cve/CVE-2016-4581
|     	CVE-2016-4578	5.5	https://vulners.com/cve/CVE-2016-4578
|     	CVE-2016-4569	5.5	https://vulners.com/cve/CVE-2016-4569
|     	CVE-2016-4470	5.5	https://vulners.com/cve/CVE-2016-4470
|     	CVE-2016-3156	5.5	https://vulners.com/cve/CVE-2016-3156
|     	CVE-2016-2550	5.5	https://vulners.com/cve/CVE-2016-2550
|     	CVE-2016-2383	5.5	https://vulners.com/cve/CVE-2016-2383
|     	CVE-2016-2085	5.5	https://vulners.com/cve/CVE-2016-2085
|     	CVE-2016-1237	5.5	https://vulners.com/cve/CVE-2016-1237
|     	CVE-2016-10723	5.5	https://vulners.com/cve/CVE-2016-10723
|     	CVE-2016-10147	5.5	https://vulners.com/cve/CVE-2016-10147
|     	CVE-2016-0821	5.5	https://vulners.com/cve/CVE-2016-0821
|     	CVE-2015-9289	5.5	https://vulners.com/cve/CVE-2015-9289
|     	CVE-2015-8970	5.5	https://vulners.com/cve/CVE-2015-8970
|     	CVE-2015-8964	5.5	https://vulners.com/cve/CVE-2015-8964
|     	CVE-2015-8953	5.5	https://vulners.com/cve/CVE-2015-8953
|     	CVE-2015-8952	5.5	https://vulners.com/cve/CVE-2015-8952
|     	CVE-2015-8950	5.5	https://vulners.com/cve/CVE-2015-8950
|     	CVE-2015-8944	5.5	https://vulners.com/cve/CVE-2015-8944
|     	CVE-2015-8845	5.5	https://vulners.com/cve/CVE-2015-8845
|     	CVE-2015-8844	5.5	https://vulners.com/cve/CVE-2015-8844
|     	CVE-2015-7550	5.5	https://vulners.com/cve/CVE-2015-7550
|     	CVE-2015-4178	5.5	https://vulners.com/cve/CVE-2015-4178
|     	CVE-2015-4177	5.5	https://vulners.com/cve/CVE-2015-4177
|     	CVE-2015-4176	5.5	https://vulners.com/cve/CVE-2015-4176
|     	CVE-2015-2672	5.5	https://vulners.com/cve/CVE-2015-2672
|     	CVE-2015-1573	5.5	https://vulners.com/cve/CVE-2015-1573
|     	CVE-2015-1350	5.5	https://vulners.com/cve/CVE-2015-1350
|     	CVE-2014-9900	5.5	https://vulners.com/cve/CVE-2014-9900
|     	CVE-2014-9895	5.5	https://vulners.com/cve/CVE-2014-9895
|     	CVE-2014-9892	5.5	https://vulners.com/cve/CVE-2014-9892
|     	CVE-2014-8559	5.5	https://vulners.com/cve/CVE-2014-8559
|     	CVE-2014-7975	5.5	https://vulners.com/cve/CVE-2014-7975
|     	CVE-2014-7970	5.5	https://vulners.com/cve/CVE-2014-7970
|     	CVE-2014-3690	5.5	https://vulners.com/cve/CVE-2014-3690
|     	CVE-2014-3647	5.5	https://vulners.com/cve/CVE-2014-3647
|     	CVE-2014-3646	5.5	https://vulners.com/cve/CVE-2014-3646
|     	CVE-2014-3610	5.5	https://vulners.com/cve/CVE-2014-3610
|     	CVE-2014-0155	5.5	https://vulners.com/cve/CVE-2014-0155
|     	CVE-2014-0077	5.5	https://vulners.com/cve/CVE-2014-0077
|     	564795E6-048F-581C-B600-4CA7B45E1319	5.5	https://vulners.com/githubexploit/564795E6-048F-581C-B600-4CA7B45E1319	*EXPLOIT*
|     	3DE02833-DEE3-5151-AEF7-3A0B9BAC1C28	5.5	https://vulners.com/githubexploit/3DE02833-DEE3-5151-AEF7-3A0B9BAC1C28	*EXPLOIT*
|     	1AC912AC-B7DA-5F88-B22A-12B17E5D1D5C	5.5	https://vulners.com/githubexploit/1AC912AC-B7DA-5F88-B22A-12B17E5D1D5C	*EXPLOIT*
|     	1337DAY-ID-39223	5.5	https://vulners.com/zdt/1337DAY-ID-39223	*EXPLOIT*
|     	1337DAY-ID-32339	5.5	https://vulners.com/zdt/1337DAY-ID-32339	*EXPLOIT*
|     	CVE-2013-2895	5.4	https://vulners.com/cve/CVE-2013-2895
|     	CVE-2024-24860	5.3	https://vulners.com/cve/CVE-2024-24860
|     	CVE-2024-24858	5.3	https://vulners.com/cve/CVE-2024-24858
|     	CVE-2024-23196	5.3	https://vulners.com/cve/CVE-2024-23196
|     	CVE-2024-22386	5.3	https://vulners.com/cve/CVE-2024-22386
|     	CVE-2023-28866	5.3	https://vulners.com/cve/CVE-2023-28866
|     	CVE-2023-0458	5.3	https://vulners.com/cve/CVE-2023-0458
|     	CVE-2022-3594	5.3	https://vulners.com/cve/CVE-2022-3594
|     	CVE-2020-12888	5.3	https://vulners.com/cve/CVE-2020-12888
|     	CVE-2020-12826	5.3	https://vulners.com/cve/CVE-2020-12826
|     	CVE-2020-10942	5.3	https://vulners.com/cve/CVE-2020-10942
|     	CVE-2018-1120	5.3	https://vulners.com/cve/CVE-2018-1120
|     	CVE-2013-7446	5.3	https://vulners.com/cve/CVE-2013-7446
|     	SSV:61684	5.2	https://vulners.com/seebug/SSV:61684	*EXPLOIT*
|     	CVE-2014-0102	5.2	https://vulners.com/cve/CVE-2014-0102
|     	CVE-2013-6376	5.2	https://vulners.com/cve/CVE-2013-6376
|     	CVE-2024-1312	5.1	https://vulners.com/cve/CVE-2024-1312
|     	CVE-2020-36558	5.1	https://vulners.com/cve/CVE-2020-36558
|     	CVE-2020-36557	5.1	https://vulners.com/cve/CVE-2020-36557
|     	CVE-2020-16120	5.1	https://vulners.com/cve/CVE-2020-16120
|     	CVE-2016-6480	5.1	https://vulners.com/cve/CVE-2016-6480
|     	CVE-2016-6156	5.1	https://vulners.com/cve/CVE-2016-6156
|     	CVE-2016-2547	5.1	https://vulners.com/cve/CVE-2016-2547
|     	CVE-2016-2546	5.1	https://vulners.com/cve/CVE-2016-2546
|     	CVE-2016-2545	5.1	https://vulners.com/cve/CVE-2016-2545
|     	CVE-2016-2544	5.1	https://vulners.com/cve/CVE-2016-2544
|     	CVE-2015-8839	5.1	https://vulners.com/cve/CVE-2015-8839
|     	SSV:61030	5.0	https://vulners.com/seebug/SSV:61030	*EXPLOIT*
|     	CVE-2020-28974	5.0	https://vulners.com/cve/CVE-2020-28974
|     	CVE-2016-7917	5.0	https://vulners.com/cve/CVE-2016-7917
|     	CVE-2015-8215	5.0	https://vulners.com/cve/CVE-2015-8215
|     	CVE-2015-5366	5.0	https://vulners.com/cve/CVE-2015-5366
|     	CVE-2015-1593	5.0	https://vulners.com/cve/CVE-2015-1593
|     	CVE-2014-8709	5.0	https://vulners.com/cve/CVE-2014-8709
|     	CVE-2014-8160	5.0	https://vulners.com/cve/CVE-2014-8160
|     	CVE-2014-7841	5.0	https://vulners.com/cve/CVE-2014-7841
|     	CVE-2014-4667	5.0	https://vulners.com/cve/CVE-2014-4667
|     	CVE-2014-4611	5.0	https://vulners.com/cve/CVE-2014-4611
|     	CVE-2014-3688	5.0	https://vulners.com/cve/CVE-2014-3688
|     	CVE-2013-4350	5.0	https://vulners.com/cve/CVE-2013-4350
|     	PACKETSTORM:156053	4.9	https://vulners.com/packetstorm/PACKETSTORM:156053	*EXPLOIT*
|     	PACKETSTORM:146863	4.9	https://vulners.com/packetstorm/PACKETSTORM:146863	*EXPLOIT*
|     	PACKETSTORM:144476	4.9	https://vulners.com/packetstorm/PACKETSTORM:144476	*EXPLOIT*
|     	PACKETSTORM:142872	4.9	https://vulners.com/packetstorm/PACKETSTORM:142872	*EXPLOIT*
|     	PACKETSTORM:142871	4.9	https://vulners.com/packetstorm/PACKETSTORM:142871	*EXPLOIT*
|     	PACKETSTORM:142488	4.9	https://vulners.com/packetstorm/PACKETSTORM:142488	*EXPLOIT*
|     	PACKETSTORM:139642	4.9	https://vulners.com/packetstorm/PACKETSTORM:139642	*EXPLOIT*
|     	PACKETSTORM:136222	4.9	https://vulners.com/packetstorm/PACKETSTORM:136222	*EXPLOIT*
|     	PACKETSTORM:136221	4.9	https://vulners.com/packetstorm/PACKETSTORM:136221	*EXPLOIT*
|     	PACKETSTORM:136219	4.9	https://vulners.com/packetstorm/PACKETSTORM:136219	*EXPLOIT*
|     	PACKETSTORM:136218	4.9	https://vulners.com/packetstorm/PACKETSTORM:136218	*EXPLOIT*
|     	PACKETSTORM:136217	4.9	https://vulners.com/packetstorm/PACKETSTORM:136217	*EXPLOIT*
|     	PACKETSTORM:136144	4.9	https://vulners.com/packetstorm/PACKETSTORM:136144	*EXPLOIT*
|     	PACKETSTORM:136143	4.9	https://vulners.com/packetstorm/PACKETSTORM:136143	*EXPLOIT*
|     	PACKETSTORM:136142	4.9	https://vulners.com/packetstorm/PACKETSTORM:136142	*EXPLOIT*
|     	PACKETSTORM:136141	4.9	https://vulners.com/packetstorm/PACKETSTORM:136141	*EXPLOIT*
|     	PACKETSTORM:136140	4.9	https://vulners.com/packetstorm/PACKETSTORM:136140	*EXPLOIT*
|     	PACKETSTORM:136139	4.9	https://vulners.com/packetstorm/PACKETSTORM:136139	*EXPLOIT*
|     	PACKETSTORM:136138	4.9	https://vulners.com/packetstorm/PACKETSTORM:136138	*EXPLOIT*
|     	PACKETSTORM:136137	4.9	https://vulners.com/packetstorm/PACKETSTORM:136137	*EXPLOIT*
|     	EXPLOITPACK:C617424ADAF7B063C6D9C6F505360E69	4.9	https://vulners.com/exploitpack/EXPLOITPACK:C617424ADAF7B063C6D9C6F505360E69	*EXPLOIT*
|     	EXPLOITPACK:AA6ABBE8E5BE3C243DF38A29FC076191	4.9	https://vulners.com/exploitpack/EXPLOITPACK:AA6ABBE8E5BE3C243DF38A29FC076191	*EXPLOIT*
|     	EXPLOITPACK:8A56E1C4D18EC6E5D9443B5BD5864C74	4.9	https://vulners.com/exploitpack/EXPLOITPACK:8A56E1C4D18EC6E5D9443B5BD5864C74	*EXPLOIT*
|     	EXPLOITPACK:1FBD31E3DB245782B704F7FD19F38A9F	4.9	https://vulners.com/exploitpack/EXPLOITPACK:1FBD31E3DB245782B704F7FD19F38A9F	*EXPLOIT*
|     	EXPLOITPACK:1EC12227A84F918BB0C8C659BE0F2284	4.9	https://vulners.com/exploitpack/EXPLOITPACK:1EC12227A84F918BB0C8C659BE0F2284	*EXPLOIT*
|     	EXPLOITPACK:07DF51A414A141989EF9F5989CC324A1	4.9	https://vulners.com/exploitpack/EXPLOITPACK:07DF51A414A141989EF9F5989CC324A1	*EXPLOIT*
|     	EXPLOITPACK:015934939F5336F3396A9248CEA51EB4	4.9	https://vulners.com/exploitpack/EXPLOITPACK:015934939F5336F3396A9248CEA51EB4	*EXPLOIT*
|     	CVE-2023-34324	4.9	https://vulners.com/cve/CVE-2023-34324
|     	CVE-2020-35513	4.9	https://vulners.com/cve/CVE-2020-35513
|     	CVE-2018-12904	4.9	https://vulners.com/cve/CVE-2018-12904
|     	CVE-2015-7799	4.9	https://vulners.com/cve/CVE-2015-7799
|     	CVE-2015-6937	4.9	https://vulners.com/cve/CVE-2015-6937
|     	CVE-2015-6526	4.9	https://vulners.com/cve/CVE-2015-6526
|     	CVE-2015-5307	4.9	https://vulners.com/cve/CVE-2015-5307
|     	CVE-2015-5257	4.9	https://vulners.com/cve/CVE-2015-5257
|     	CVE-2015-4700	4.9	https://vulners.com/cve/CVE-2015-4700
|     	CVE-2015-4692	4.9	https://vulners.com/cve/CVE-2015-4692
|     	CVE-2015-3636	4.9	https://vulners.com/cve/CVE-2015-3636
|     	CVE-2015-3332	4.9	https://vulners.com/cve/CVE-2015-3332
|     	CVE-2015-3212	4.9	https://vulners.com/cve/CVE-2015-3212
|     	CVE-2015-2150	4.9	https://vulners.com/cve/CVE-2015-2150
|     	CVE-2015-1333	4.9	https://vulners.com/cve/CVE-2015-1333
|     	CVE-2015-0275	4.9	https://vulners.com/cve/CVE-2015-0275
|     	CVE-2014-9730	4.9	https://vulners.com/cve/CVE-2014-9730
|     	CVE-2014-9729	4.9	https://vulners.com/cve/CVE-2014-9729
|     	CVE-2014-9728	4.9	https://vulners.com/cve/CVE-2014-9728
|     	CVE-2014-9715	4.9	https://vulners.com/cve/CVE-2014-9715
|     	CVE-2014-9420	4.9	https://vulners.com/cve/CVE-2014-9420
|     	CVE-2014-9090	4.9	https://vulners.com/cve/CVE-2014-9090
|     	CVE-2014-8481	4.9	https://vulners.com/cve/CVE-2014-8481
|     	CVE-2014-8480	4.9	https://vulners.com/cve/CVE-2014-8480
|     	CVE-2014-8172	4.9	https://vulners.com/cve/CVE-2014-8172
|     	CVE-2014-7843	4.9	https://vulners.com/cve/CVE-2014-7843
|     	CVE-2014-7842	4.9	https://vulners.com/cve/CVE-2014-7842
|     	CVE-2014-7283	4.9	https://vulners.com/cve/CVE-2014-7283
|     	CVE-2014-4655	4.9	https://vulners.com/cve/CVE-2014-4655
|     	CVE-2014-3145	4.9	https://vulners.com/cve/CVE-2014-3145
|     	CVE-2014-3144	4.9	https://vulners.com/cve/CVE-2014-3144
|     	CVE-2014-3122	4.9	https://vulners.com/cve/CVE-2014-3122
|     	CVE-2014-2039	4.9	https://vulners.com/cve/CVE-2014-2039
|     	CVE-2014-1874	4.9	https://vulners.com/cve/CVE-2014-1874
|     	CVE-2013-7281	4.9	https://vulners.com/cve/CVE-2013-7281
|     	CVE-2013-7271	4.9	https://vulners.com/cve/CVE-2013-7271
|     	CVE-2013-7270	4.9	https://vulners.com/cve/CVE-2013-7270
|     	CVE-2013-7269	4.9	https://vulners.com/cve/CVE-2013-7269
|     	CVE-2013-7268	4.9	https://vulners.com/cve/CVE-2013-7268
|     	CVE-2013-7267	4.9	https://vulners.com/cve/CVE-2013-7267
|     	CVE-2013-7266	4.9	https://vulners.com/cve/CVE-2013-7266
|     	CVE-2013-7265	4.9	https://vulners.com/cve/CVE-2013-7265
|     	CVE-2013-7264	4.9	https://vulners.com/cve/CVE-2013-7264
|     	CVE-2013-7263	4.9	https://vulners.com/cve/CVE-2013-7263
|     	CVE-2013-4516	4.9	https://vulners.com/cve/CVE-2013-4516
|     	CVE-2013-4515	4.9	https://vulners.com/cve/CVE-2013-4515
|     	CVE-2013-4513	4.9	https://vulners.com/cve/CVE-2013-4513
|     	1337DAY-ID-33849	4.9	https://vulners.com/zdt/1337DAY-ID-33849	*EXPLOIT*
|     	1337DAY-ID-30032	4.9	https://vulners.com/zdt/1337DAY-ID-30032	*EXPLOIT*
|     	1337DAY-ID-28714	4.9	https://vulners.com/zdt/1337DAY-ID-28714	*EXPLOIT*
|     	1337DAY-ID-27914	4.9	https://vulners.com/zdt/1337DAY-ID-27914	*EXPLOIT*
|     	1337DAY-ID-27913	4.9	https://vulners.com/zdt/1337DAY-ID-27913	*EXPLOIT*
|     	1337DAY-ID-27765	4.9	https://vulners.com/zdt/1337DAY-ID-27765	*EXPLOIT*
|     	1337DAY-ID-26265	4.9	https://vulners.com/zdt/1337DAY-ID-26265	*EXPLOIT*
|     	1337DAY-ID-25881	4.9	https://vulners.com/zdt/1337DAY-ID-25881	*EXPLOIT*
|     	1337DAY-ID-25880	4.9	https://vulners.com/zdt/1337DAY-ID-25880	*EXPLOIT*
|     	1337DAY-ID-25872	4.9	https://vulners.com/zdt/1337DAY-ID-25872	*EXPLOIT*
|     	1337DAY-ID-25871	4.9	https://vulners.com/zdt/1337DAY-ID-25871	*EXPLOIT*
|     	1337DAY-ID-25870	4.9	https://vulners.com/zdt/1337DAY-ID-25870	*EXPLOIT*
|     	1337DAY-ID-25869	4.9	https://vulners.com/zdt/1337DAY-ID-25869	*EXPLOIT*
|     	1337DAY-ID-25867	4.9	https://vulners.com/zdt/1337DAY-ID-25867	*EXPLOIT*
|     	1337DAY-ID-25865	4.9	https://vulners.com/zdt/1337DAY-ID-25865	*EXPLOIT*
|     	CVE-2024-24859	4.8	https://vulners.com/cve/CVE-2024-24859
|     	CVE-2016-5696	4.8	https://vulners.com/cve/CVE-2016-5696
|     	SSV:62043	4.7	https://vulners.com/seebug/SSV:62043	*EXPLOIT*
|     	SSV:61914	4.7	https://vulners.com/seebug/SSV:61914	*EXPLOIT*
|     	EAE6763D-4067-54F1-9005-22CCA4072D1B	4.7	https://vulners.com/githubexploit/EAE6763D-4067-54F1-9005-22CCA4072D1B	*EXPLOIT*
|     	CVE-2024-26910	4.7	https://vulners.com/cve/CVE-2024-26910
|     	CVE-2023-4732	4.7	https://vulners.com/cve/CVE-2023-4732
|     	CVE-2023-46862	4.7	https://vulners.com/cve/CVE-2023-46862
|     	CVE-2023-42756	4.7	https://vulners.com/cve/CVE-2023-42756
|     	CVE-2023-3439	4.7	https://vulners.com/cve/CVE-2023-3439
|     	CVE-2023-33288	4.7	https://vulners.com/cve/CVE-2023-33288
|     	CVE-2023-26545	4.7	https://vulners.com/cve/CVE-2023-26545
|     	CVE-2023-1990	4.7	https://vulners.com/cve/CVE-2023-1990
|     	CVE-2023-1859	4.7	https://vulners.com/cve/CVE-2023-1859
|     	CVE-2023-1582	4.7	https://vulners.com/cve/CVE-2023-1582
|     	CVE-2023-1382	4.7	https://vulners.com/cve/CVE-2023-1382
|     	CVE-2023-0590	4.7	https://vulners.com/cve/CVE-2023-0590
|     	CVE-2023-0468	4.7	https://vulners.com/cve/CVE-2023-0468
|     	CVE-2022-45887	4.7	https://vulners.com/cve/CVE-2022-45887
|     	CVE-2022-41850	4.7	https://vulners.com/cve/CVE-2022-41850
|     	CVE-2022-40307	4.7	https://vulners.com/cve/CVE-2022-40307
|     	CVE-2022-39188	4.7	https://vulners.com/cve/CVE-2022-39188
|     	CVE-2022-3303	4.7	https://vulners.com/cve/CVE-2022-3303
|     	CVE-2022-1205	4.7	https://vulners.com/cve/CVE-2022-1205
|     	CVE-2021-3753	4.7	https://vulners.com/cve/CVE-2021-3753
|     	CVE-2021-33624	4.7	https://vulners.com/cve/CVE-2021-33624
|     	CVE-2021-29265	4.7	https://vulners.com/cve/CVE-2021-29265
|     	CVE-2021-28964	4.7	https://vulners.com/cve/CVE-2021-28964
|     	CVE-2021-20321	4.7	https://vulners.com/cve/CVE-2021-20321
|     	CVE-2020-29372	4.7	https://vulners.com/cve/CVE-2020-29372
|     	CVE-2020-27820	4.7	https://vulners.com/cve/CVE-2020-27820
|     	CVE-2020-27675	4.7	https://vulners.com/cve/CVE-2020-27675
|     	CVE-2020-27170	4.7	https://vulners.com/cve/CVE-2020-27170
|     	CVE-2019-3901	4.7	https://vulners.com/cve/CVE-2019-3901
|     	CVE-2019-19965	4.7	https://vulners.com/cve/CVE-2019-19965
|     	CVE-2019-19083	4.7	https://vulners.com/cve/CVE-2019-19083
|     	CVE-2019-19082	4.7	https://vulners.com/cve/CVE-2019-19082
|     	CVE-2019-19066	4.7	https://vulners.com/cve/CVE-2019-19066
|     	CVE-2019-19065	4.7	https://vulners.com/cve/CVE-2019-19065
|     	CVE-2019-19062	4.7	https://vulners.com/cve/CVE-2019-19062
|     	CVE-2019-19059	4.7	https://vulners.com/cve/CVE-2019-19059
|     	CVE-2019-19058	4.7	https://vulners.com/cve/CVE-2019-19058
|     	CVE-2019-19056	4.7	https://vulners.com/cve/CVE-2019-19056
|     	CVE-2019-19054	4.7	https://vulners.com/cve/CVE-2019-19054
|     	CVE-2019-18660	4.7	https://vulners.com/cve/CVE-2019-18660
|     	CVE-2019-16994	4.7	https://vulners.com/cve/CVE-2019-16994
|     	CVE-2019-15921	4.7	https://vulners.com/cve/CVE-2019-15921
|     	CVE-2019-15807	4.7	https://vulners.com/cve/CVE-2019-15807
|     	CVE-2019-15292	4.7	https://vulners.com/cve/CVE-2019-15292
|     	CVE-2019-11190	4.7	https://vulners.com/cve/CVE-2019-11190
|     	CVE-2018-7995	4.7	https://vulners.com/cve/CVE-2018-7995
|     	CVE-2018-19854	4.7	https://vulners.com/cve/CVE-2018-19854
|     	CVE-2018-1065	4.7	https://vulners.com/cve/CVE-2018-1065
|     	CVE-2017-18224	4.7	https://vulners.com/cve/CVE-2017-18224
|     	CVE-2017-18203	4.7	https://vulners.com/cve/CVE-2017-18203
|     	CVE-2017-17449	4.7	https://vulners.com/cve/CVE-2017-17449
|     	CVE-2016-6213	4.7	https://vulners.com/cve/CVE-2016-6213
|     	CVE-2016-6136	4.7	https://vulners.com/cve/CVE-2016-6136
|     	CVE-2016-6130	4.7	https://vulners.com/cve/CVE-2016-6130
|     	CVE-2016-2053	4.7	https://vulners.com/cve/CVE-2016-2053
|     	CVE-2016-10741	4.7	https://vulners.com/cve/CVE-2016-10741
|     	CVE-2015-8104	4.7	https://vulners.com/cve/CVE-2015-8104
|     	CVE-2015-5283	4.7	https://vulners.com/cve/CVE-2015-5283
|     	CVE-2015-4170	4.7	https://vulners.com/cve/CVE-2015-4170
|     	CVE-2015-4167	4.7	https://vulners.com/cve/CVE-2015-4167
|     	CVE-2014-8086	4.7	https://vulners.com/cve/CVE-2014-8086
|     	CVE-2014-6410	4.7	https://vulners.com/cve/CVE-2014-6410
|     	CVE-2014-4508	4.7	https://vulners.com/cve/CVE-2014-4508
|     	CVE-2014-4171	4.7	https://vulners.com/cve/CVE-2014-4171
|     	CVE-2014-3611	4.7	https://vulners.com/cve/CVE-2014-3611
|     	CVE-2014-3184	4.7	https://vulners.com/cve/CVE-2014-3184
|     	CVE-2014-2678	4.7	https://vulners.com/cve/CVE-2014-2678
|     	CVE-2014-2673	4.7	https://vulners.com/cve/CVE-2014-2673
|     	CVE-2014-1438	4.7	https://vulners.com/cve/CVE-2014-1438
|     	CVE-2013-7339	4.7	https://vulners.com/cve/CVE-2013-7339
|     	CVE-2013-7026	4.7	https://vulners.com/cve/CVE-2013-7026
|     	CVE-2013-6431	4.7	https://vulners.com/cve/CVE-2013-6431
|     	CVE-2013-6380	4.7	https://vulners.com/cve/CVE-2013-6380
|     	CVE-2013-4514	4.7	https://vulners.com/cve/CVE-2013-4514
|     	CVE-2013-4512	4.7	https://vulners.com/cve/CVE-2013-4512
|     	CVE-2013-2899	4.7	https://vulners.com/cve/CVE-2013-2899
|     	CVE-2013-2897	4.7	https://vulners.com/cve/CVE-2013-2897
|     	CVE-2013-2896	4.7	https://vulners.com/cve/CVE-2013-2896
|     	CVE-2013-2894	4.7	https://vulners.com/cve/CVE-2013-2894
|     	CVE-2013-2893	4.7	https://vulners.com/cve/CVE-2013-2893
|     	CVE-2013-2892	4.7	https://vulners.com/cve/CVE-2013-2892
|     	CVE-2013-2891	4.7	https://vulners.com/cve/CVE-2013-2891
|     	CVE-2013-2890	4.7	https://vulners.com/cve/CVE-2013-2890
|     	CVE-2013-2889	4.7	https://vulners.com/cve/CVE-2013-2889
|     	SSV:96778	4.6	https://vulners.com/seebug/SSV:96778	*EXPLOIT*
|     	PACKETSTORM:164437	4.6	https://vulners.com/packetstorm/PACKETSTORM:164437	*EXPLOIT*
|     	PACKETSTORM:163528	4.6	https://vulners.com/packetstorm/PACKETSTORM:163528	*EXPLOIT*
|     	PACKETSTORM:153493	4.6	https://vulners.com/packetstorm/PACKETSTORM:153493	*EXPLOIT*
|     	PACKETSTORM:141914	4.6	https://vulners.com/packetstorm/PACKETSTORM:141914	*EXPLOIT*
|     	EXPLOITPACK:A80EC992E1B2F9D76F9013820F33CF10	4.6	https://vulners.com/exploitpack/EXPLOITPACK:A80EC992E1B2F9D76F9013820F33CF10	*EXPLOIT*
|     	EXPLOITPACK:A031F8D10EB08B211770A02799B5FBA0	4.6	https://vulners.com/exploitpack/EXPLOITPACK:A031F8D10EB08B211770A02799B5FBA0	*EXPLOIT*
|     	EXPLOITPACK:6AD5ACC620F0F4EF82BC0FA4AB29F652	4.6	https://vulners.com/exploitpack/EXPLOITPACK:6AD5ACC620F0F4EF82BC0FA4AB29F652	*EXPLOIT*
|     	EDB-ID:41999	4.6	https://vulners.com/exploitdb/EDB-ID:41999	*EXPLOIT*
|     	EDB-ID:39544	4.6	https://vulners.com/exploitdb/EDB-ID:39544	*EXPLOIT*
|     	EDB-ID:39540	4.6	https://vulners.com/exploitdb/EDB-ID:39540	*EXPLOIT*
|     	EDB-ID:39539	4.6	https://vulners.com/exploitdb/EDB-ID:39539	*EXPLOIT*
|     	CVE-2023-37453	4.6	https://vulners.com/cve/CVE-2023-37453
|     	CVE-2023-25012	4.6	https://vulners.com/cve/CVE-2023-25012
|     	CVE-2022-3903	4.6	https://vulners.com/cve/CVE-2022-3903
|     	CVE-2022-25258	4.6	https://vulners.com/cve/CVE-2022-25258
|     	CVE-2021-43976	4.6	https://vulners.com/cve/CVE-2021-43976
|     	CVE-2019-19966	4.6	https://vulners.com/cve/CVE-2019-19966
|     	CVE-2019-19947	4.6	https://vulners.com/cve/CVE-2019-19947
|     	CVE-2019-19536	4.6	https://vulners.com/cve/CVE-2019-19536
|     	CVE-2019-19535	4.6	https://vulners.com/cve/CVE-2019-19535
|     	CVE-2019-19530	4.6	https://vulners.com/cve/CVE-2019-19530
|     	CVE-2019-19526	4.6	https://vulners.com/cve/CVE-2019-19526
|     	CVE-2019-19525	4.6	https://vulners.com/cve/CVE-2019-19525
|     	CVE-2019-19524	4.6	https://vulners.com/cve/CVE-2019-19524
|     	CVE-2019-19523	4.6	https://vulners.com/cve/CVE-2019-19523
|     	CVE-2019-19068	4.6	https://vulners.com/cve/CVE-2019-19068
|     	CVE-2019-19063	4.6	https://vulners.com/cve/CVE-2019-19063
|     	CVE-2019-18809	4.6	https://vulners.com/cve/CVE-2019-18809
|     	CVE-2019-15291	4.6	https://vulners.com/cve/CVE-2019-15291
|     	CVE-2019-15223	4.6	https://vulners.com/cve/CVE-2019-15223
|     	CVE-2019-15222	4.6	https://vulners.com/cve/CVE-2019-15222
|     	CVE-2019-15221	4.6	https://vulners.com/cve/CVE-2019-15221
|     	CVE-2019-15220	4.6	https://vulners.com/cve/CVE-2019-15220
|     	CVE-2019-15219	4.6	https://vulners.com/cve/CVE-2019-15219
|     	CVE-2019-15218	4.6	https://vulners.com/cve/CVE-2019-15218
|     	CVE-2019-15217	4.6	https://vulners.com/cve/CVE-2019-15217
|     	CVE-2019-15216	4.6	https://vulners.com/cve/CVE-2019-15216
|     	CVE-2019-15215	4.6	https://vulners.com/cve/CVE-2019-15215
|     	CVE-2019-15213	4.6	https://vulners.com/cve/CVE-2019-15213
|     	CVE-2019-15212	4.6	https://vulners.com/cve/CVE-2019-15212
|     	CVE-2019-15211	4.6	https://vulners.com/cve/CVE-2019-15211
|     	CVE-2019-15098	4.6	https://vulners.com/cve/CVE-2019-15098
|     	CVE-2018-19985	4.6	https://vulners.com/cve/CVE-2018-19985
|     	CVE-2017-8924	4.6	https://vulners.com/cve/CVE-2017-8924
|     	CVE-2016-3689	4.6	https://vulners.com/cve/CVE-2016-3689
|     	CVE-2016-3140	4.6	https://vulners.com/cve/CVE-2016-3140
|     	CVE-2016-3139	4.6	https://vulners.com/cve/CVE-2016-3139
|     	CVE-2016-3138	4.6	https://vulners.com/cve/CVE-2016-3138
|     	CVE-2016-3137	4.6	https://vulners.com/cve/CVE-2016-3137
|     	CVE-2016-3136	4.6	https://vulners.com/cve/CVE-2016-3136
|     	CVE-2016-2782	4.6	https://vulners.com/cve/CVE-2016-2782
|     	CVE-2016-2384	4.6	https://vulners.com/cve/CVE-2016-2384
|     	CVE-2016-2188	4.6	https://vulners.com/cve/CVE-2016-2188
|     	CVE-2016-2187	4.6	https://vulners.com/cve/CVE-2016-2187
|     	CVE-2016-2186	4.6	https://vulners.com/cve/CVE-2016-2186
|     	CVE-2016-2185	4.6	https://vulners.com/cve/CVE-2016-2185
|     	CVE-2016-2184	4.6	https://vulners.com/cve/CVE-2016-2184
|     	CVE-2015-7566	4.6	https://vulners.com/cve/CVE-2015-7566
|     	CVE-2015-7515	4.6	https://vulners.com/cve/CVE-2015-7515
|     	CVE-2015-5707	4.6	https://vulners.com/cve/CVE-2015-5707
|     	CVE-2015-5706	4.6	https://vulners.com/cve/CVE-2015-5706
|     	CVE-2015-2042	4.6	https://vulners.com/cve/CVE-2015-2042
|     	CVE-2015-2041	4.6	https://vulners.com/cve/CVE-2015-2041
|     	CVE-2014-8989	4.6	https://vulners.com/cve/CVE-2014-8989
|     	CVE-2014-4656	4.6	https://vulners.com/cve/CVE-2014-4656
|     	CVE-2014-4654	4.6	https://vulners.com/cve/CVE-2014-4654
|     	CVE-2014-4653	4.6	https://vulners.com/cve/CVE-2014-4653
|     	CVE-2014-4157	4.6	https://vulners.com/cve/CVE-2014-4157
|     	CVE-2013-7348	4.6	https://vulners.com/cve/CVE-2013-7348
|     	CVE-2013-6432	4.6	https://vulners.com/cve/CVE-2013-6432
|     	490EABEE-259A-5EC7-92F2-4B9159861857	4.6	https://vulners.com/githubexploit/490EABEE-259A-5EC7-92F2-4B9159861857	*EXPLOIT*
|     	40BC579C-001A-55C8-BA87-003B6E41F5BA	4.6	https://vulners.com/githubexploit/40BC579C-001A-55C8-BA87-003B6E41F5BA	*EXPLOIT*
|     	3E320B36-9DFC-53EF-8079-9B652019A21A	4.6	https://vulners.com/githubexploit/3E320B36-9DFC-53EF-8079-9B652019A21A	*EXPLOIT*
|     	1337DAY-ID-33662	4.6	https://vulners.com/zdt/1337DAY-ID-33662	*EXPLOIT*
|     	1337DAY-ID-27469	4.6	https://vulners.com/zdt/1337DAY-ID-27469	*EXPLOIT*
|     	1337DAY-ID-25969	4.6	https://vulners.com/zdt/1337DAY-ID-25969	*EXPLOIT*
|     	CVE-2020-35508	4.5	https://vulners.com/cve/CVE-2020-35508
|     	E51F4AE5-FB27-586A-ACDE-5A70AD48E096	4.4	https://vulners.com/githubexploit/E51F4AE5-FB27-586A-ACDE-5A70AD48E096	*EXPLOIT*
|     	CVE-2023-39194	4.4	https://vulners.com/cve/CVE-2023-39194
|     	CVE-2023-3212	4.4	https://vulners.com/cve/CVE-2023-3212
|     	CVE-2023-2860	4.4	https://vulners.com/cve/CVE-2023-2860
|     	CVE-2023-2269	4.4	https://vulners.com/cve/CVE-2023-2269
|     	CVE-2023-2019	4.4	https://vulners.com/cve/CVE-2023-2019
|     	CVE-2022-42432	4.4	https://vulners.com/cve/CVE-2022-42432
|     	CVE-2022-0494	4.4	https://vulners.com/cve/CVE-2022-0494
|     	CVE-2022-0168	4.4	https://vulners.com/cve/CVE-2022-0168
|     	CVE-2021-4159	4.4	https://vulners.com/cve/CVE-2021-4159
|     	CVE-2021-4032	4.4	https://vulners.com/cve/CVE-2021-4032
|     	CVE-2021-4002	4.4	https://vulners.com/cve/CVE-2021-4002
|     	CVE-2021-3635	4.4	https://vulners.com/cve/CVE-2021-3635
|     	CVE-2021-27363	4.4	https://vulners.com/cve/CVE-2021-27363
|     	CVE-2021-20317	4.4	https://vulners.com/cve/CVE-2021-20317
|     	CVE-2021-20177	4.4	https://vulners.com/cve/CVE-2021-20177
|     	CVE-2020-29660	4.4	https://vulners.com/cve/CVE-2020-29660
|     	CVE-2020-27835	4.4	https://vulners.com/cve/CVE-2020-27835
|     	CVE-2020-25639	4.4	https://vulners.com/cve/CVE-2020-25639
|     	CVE-2020-15437	4.4	https://vulners.com/cve/CVE-2020-15437
|     	CVE-2020-14304	4.4	https://vulners.com/cve/CVE-2020-14304
|     	CVE-2020-10732	4.4	https://vulners.com/cve/CVE-2020-10732
|     	CVE-2019-3701	4.4	https://vulners.com/cve/CVE-2019-3701
|     	CVE-2019-20806	4.4	https://vulners.com/cve/CVE-2019-20806
|     	CVE-2019-19072	4.4	https://vulners.com/cve/CVE-2019-19072
|     	CVE-2019-19067	4.4	https://vulners.com/cve/CVE-2019-19067
|     	CVE-2019-19045	4.4	https://vulners.com/cve/CVE-2019-19045
|     	CVE-2019-15666	4.4	https://vulners.com/cve/CVE-2019-15666
|     	CVE-2019-15031	4.4	https://vulners.com/cve/CVE-2019-15031
|     	CVE-2019-15030	4.4	https://vulners.com/cve/CVE-2019-15030
|     	CVE-2017-5551	4.4	https://vulners.com/cve/CVE-2017-5551
|     	CVE-2017-14051	4.4	https://vulners.com/cve/CVE-2017-14051
|     	CVE-2017-12153	4.4	https://vulners.com/cve/CVE-2017-12153
|     	CVE-2016-9604	4.4	https://vulners.com/cve/CVE-2016-9604
|     	CVE-2016-7097	4.4	https://vulners.com/cve/CVE-2016-7097
|     	CVE-2015-7312	4.4	https://vulners.com/cve/CVE-2015-7312
|     	CVE-2015-0239	4.4	https://vulners.com/cve/CVE-2015-0239
|     	CVE-2013-6378	4.4	https://vulners.com/cve/CVE-2013-6378
|     	A7634AF1-97BC-5FDE-AB55-C342F7AA7545	4.4	https://vulners.com/githubexploit/A7634AF1-97BC-5FDE-AB55-C342F7AA7545	*EXPLOIT*
|     	2F93A054-50AD-529C-A586-5BE5E04A859E	4.4	https://vulners.com/githubexploit/2F93A054-50AD-529C-A586-5BE5E04A859E	*EXPLOIT*
|     	CVE-2023-47233	4.3	https://vulners.com/cve/CVE-2023-47233
|     	CVE-2022-0812	4.3	https://vulners.com/cve/CVE-2022-0812
|     	CVE-2020-11609	4.3	https://vulners.com/cve/CVE-2020-11609
|     	CVE-2020-11608	4.3	https://vulners.com/cve/CVE-2020-11608
|     	CVE-2019-15920	4.3	https://vulners.com/cve/CVE-2019-15920
|     	CVE-2016-5400	4.3	https://vulners.com/cve/CVE-2016-5400
|     	CVE-2016-10208	4.3	https://vulners.com/cve/CVE-2016-10208
|     	CVE-2014-3601	4.3	https://vulners.com/cve/CVE-2014-3601
|     	CVE-2013-4579	4.3	https://vulners.com/cve/CVE-2013-4579
|     	CVE-2010-5321	4.3	https://vulners.com/cve/CVE-2010-5321
|     	947C195E-C204-5E09-82FA-6C302D81AD05	4.3	https://vulners.com/githubexploit/947C195E-C204-5E09-82FA-6C302D81AD05	*EXPLOIT*
|     	768F8F97-383F-5D15-BBA5-81FFC7138CD5	4.3	https://vulners.com/githubexploit/768F8F97-383F-5D15-BBA5-81FFC7138CD5	*EXPLOIT*
|     	CVE-2022-41849	4.2	https://vulners.com/cve/CVE-2022-41849
|     	CVE-2022-41848	4.2	https://vulners.com/cve/CVE-2022-41848
|     	CVE-2020-26558	4.2	https://vulners.com/cve/CVE-2020-26558
|     	CVE-2020-14416	4.2	https://vulners.com/cve/CVE-2020-14416
|     	CVE-2019-19537	4.2	https://vulners.com/cve/CVE-2019-19537
|     	CVE-2022-1974	4.1	https://vulners.com/cve/CVE-2022-1974
|     	CVE-2021-4001	4.1	https://vulners.com/cve/CVE-2021-4001
|     	CVE-2020-25656	4.1	https://vulners.com/cve/CVE-2020-25656
|     	CVE-2020-25284	4.1	https://vulners.com/cve/CVE-2020-25284
|     	CVE-2020-12652	4.1	https://vulners.com/cve/CVE-2020-12652
|     	CVE-2019-16089	4.1	https://vulners.com/cve/CVE-2019-16089
|     	CVE-2019-12614	4.1	https://vulners.com/cve/CVE-2019-12614
|     	CVE-2023-23003	4.0	https://vulners.com/cve/CVE-2023-23003
|     	CVE-2019-19073	4.0	https://vulners.com/cve/CVE-2019-19073
|     	CVE-2017-5967	4.0	https://vulners.com/cve/CVE-2017-5967
|     	CVE-2016-0823	4.0	https://vulners.com/cve/CVE-2016-0823
|     	CVE-2015-8575	4.0	https://vulners.com/cve/CVE-2015-8575
|     	CVE-2015-8374	4.0	https://vulners.com/cve/CVE-2015-8374
|     	CVE-2014-5472	4.0	https://vulners.com/cve/CVE-2014-5472
|     	CVE-2014-5471	4.0	https://vulners.com/cve/CVE-2014-5471
|     	CVE-2014-3940	4.0	https://vulners.com/cve/CVE-2014-3940
|     	CVE-2013-6382	4.0	https://vulners.com/cve/CVE-2013-6382
|     	60DBFB07-2D29-569A-8384-705F4FE2E081	4.0	https://vulners.com/githubexploit/60DBFB07-2D29-569A-8384-705F4FE2E081	*EXPLOIT*
|     	57A0415B-1028-561B-9CAC-CE0A5197780D	4.0	https://vulners.com/githubexploit/57A0415B-1028-561B-9CAC-CE0A5197780D	*EXPLOIT*
|     	50927148-58D3-562D-AF6A-5BB14568110B	4.0	https://vulners.com/githubexploit/50927148-58D3-562D-AF6A-5BB14568110B	*EXPLOIT*
|     	CVE-2020-16166	3.7	https://vulners.com/cve/CVE-2020-16166
|     	CVE-2020-29374	3.6	https://vulners.com/cve/CVE-2020-29374
|     	CVE-2014-9683	3.6	https://vulners.com/cve/CVE-2014-9683
|     	CVE-2013-4270	3.6	https://vulners.com/cve/CVE-2013-4270
|     	CVE-2013-2930	3.6	https://vulners.com/cve/CVE-2013-2930
|     	CVE-2021-45486	3.5	https://vulners.com/cve/CVE-2021-45486
|     	CVE-2020-35501	3.4	https://vulners.com/cve/CVE-2020-35501
|     	EDB-ID:46006	3.3	https://vulners.com/exploitdb/EDB-ID:46006	*EXPLOIT*
|     	CVE-2023-1513	3.3	https://vulners.com/cve/CVE-2023-1513
|     	CVE-2022-33981	3.3	https://vulners.com/cve/CVE-2022-33981
|     	CVE-2022-32296	3.3	https://vulners.com/cve/CVE-2022-32296
|     	CVE-2022-24448	3.3	https://vulners.com/cve/CVE-2022-24448
|     	CVE-2021-38209	3.3	https://vulners.com/cve/CVE-2021-38209
|     	CVE-2021-38205	3.3	https://vulners.com/cve/CVE-2021-38205
|     	CVE-2021-3655	3.3	https://vulners.com/cve/CVE-2021-3655
|     	CVE-2021-21781	3.3	https://vulners.com/cve/CVE-2021-21781
|     	CVE-2021-20239	3.3	https://vulners.com/cve/CVE-2021-20239
|     	CVE-2020-36766	3.3	https://vulners.com/cve/CVE-2020-36766
|     	CVE-2020-29371	3.3	https://vulners.com/cve/CVE-2020-29371
|     	CVE-2019-19057	3.3	https://vulners.com/cve/CVE-2019-19057
|     	CVE-2019-17056	3.3	https://vulners.com/cve/CVE-2019-17056
|     	CVE-2019-17055	3.3	https://vulners.com/cve/CVE-2019-17055
|     	CVE-2019-17054	3.3	https://vulners.com/cve/CVE-2019-17054
|     	CVE-2019-17053	3.3	https://vulners.com/cve/CVE-2019-17053
|     	CVE-2019-15919	3.3	https://vulners.com/cve/CVE-2019-15919
|     	CVE-2019-11884	3.3	https://vulners.com/cve/CVE-2019-11884
|     	CVE-2018-20855	3.3	https://vulners.com/cve/CVE-2018-20855
|     	CVE-2018-18386	3.3	https://vulners.com/cve/CVE-2018-18386
|     	CVE-2018-13053	3.3	https://vulners.com/cve/CVE-2018-13053
|     	CVE-2017-17864	3.3	https://vulners.com/cve/CVE-2017-17864
|     	CVE-2017-17807	3.3	https://vulners.com/cve/CVE-2017-17807
|     	CVE-2016-4486	3.3	https://vulners.com/cve/CVE-2016-4486
|     	CVE-2015-2922	3.3	https://vulners.com/cve/CVE-2015-2922
|     	CVE-2015-2877	3.3	https://vulners.com/cve/CVE-2015-2877
|     	CVE-2014-8134	3.3	https://vulners.com/cve/CVE-2014-8134
|     	CVE-2014-3917	3.3	https://vulners.com/cve/CVE-2014-3917
|     	CVE-2013-2929	3.3	https://vulners.com/cve/CVE-2013-2929
|     	9F694BF4-A8B2-54FA-A630-95D42A475B72	3.2	https://vulners.com/githubexploit/9F694BF4-A8B2-54FA-A630-95D42A475B72	*EXPLOIT*
|     	87995656-FD30-5D61-AF78-F049F09B92A2	3.2	https://vulners.com/githubexploit/87995656-FD30-5D61-AF78-F049F09B92A2	*EXPLOIT*
|     	SSV:62031	2.9	https://vulners.com/seebug/SSV:62031	*EXPLOIT*
|     	SSV:61934	2.9	https://vulners.com/seebug/SSV:61934	*EXPLOIT*
|     	SSV:61913	2.9	https://vulners.com/seebug/SSV:61913	*EXPLOIT*
|     	CVE-2014-2568	2.9	https://vulners.com/cve/CVE-2014-2568
|     	CVE-2014-0131	2.9	https://vulners.com/cve/CVE-2014-0131
|     	CVE-2022-3521	2.6	https://vulners.com/cve/CVE-2022-3521
|     	CVE-2014-1690	2.6	https://vulners.com/cve/CVE-2014-1690
|     	CVE-2019-11191	2.5	https://vulners.com/cve/CVE-2019-11191
|     	CVE-2019-19534	2.4	https://vulners.com/cve/CVE-2019-19534
|     	CVE-2019-19533	2.4	https://vulners.com/cve/CVE-2019-19533
|     	CVE-2021-3923	2.3	https://vulners.com/cve/CVE-2021-3923
|     	CVE-2015-8569	2.3	https://vulners.com/cve/CVE-2015-8569
|     	CVE-2015-7885	2.3	https://vulners.com/cve/CVE-2015-7885
|     	CVE-2015-7884	2.3	https://vulners.com/cve/CVE-2015-7884
|     	CVE-2014-4027	2.3	https://vulners.com/cve/CVE-2014-4027
|     	SSV:96915	2.1	https://vulners.com/seebug/SSV:96915	*EXPLOIT*
|     	SSV:61344	2.1	https://vulners.com/seebug/SSV:61344	*EXPLOIT*
|     	SHOW_TIMER_LEAK	2.1	https://vulners.com/canvas/SHOW_TIMER_LEAK	*EXPLOIT*
|     	PACKETSTORM:152031	2.1	https://vulners.com/packetstorm/PACKETSTORM:152031	*EXPLOIT*
|     	PACKETSTORM:151241	2.1	https://vulners.com/packetstorm/PACKETSTORM:151241	*EXPLOIT*
|     	PACKETSTORM:150840	2.1	https://vulners.com/packetstorm/PACKETSTORM:150840	*EXPLOIT*
|     	EXPLOITPACK:CC3E0CE0239066A83BA64B22929DBCEC	2.1	https://vulners.com/exploitpack/EXPLOITPACK:CC3E0CE0239066A83BA64B22929DBCEC	*EXPLOIT*
|     	EXPLOITPACK:A7D1F1EE22D287BA7C370716B05F2B20	2.1	https://vulners.com/exploitpack/EXPLOITPACK:A7D1F1EE22D287BA7C370716B05F2B20	*EXPLOIT*
|     	EXPLOITPACK:5A579BB0C6565F601142E5641AED86AB	2.1	https://vulners.com/exploitpack/EXPLOITPACK:5A579BB0C6565F601142E5641AED86AB	*EXPLOIT*
|     	EXPLOITPACK:4C655D3CA17B7B7E6BE5BEFF9024D311	2.1	https://vulners.com/exploitpack/EXPLOITPACK:4C655D3CA17B7B7E6BE5BEFF9024D311	*EXPLOIT*
|     	EDB-ID:39214	2.1	https://vulners.com/exploitdb/EDB-ID:39214	*EXPLOIT*
|     	E5D4E7F8-5D9A-5970-907B-1583C529EB4C	2.1	https://vulners.com/githubexploit/E5D4E7F8-5D9A-5970-907B-1583C529EB4C	*EXPLOIT*
|     	DMESG_LEAK	2.1	https://vulners.com/canvas/DMESG_LEAK	*EXPLOIT*
|     	CVE-2015-7872	2.1	https://vulners.com/cve/CVE-2015-7872
|     	CVE-2015-6252	2.1	https://vulners.com/cve/CVE-2015-6252
|     	CVE-2015-5697	2.1	https://vulners.com/cve/CVE-2015-5697
|     	CVE-2015-3291	2.1	https://vulners.com/cve/CVE-2015-3291
|     	CVE-2014-9731	2.1	https://vulners.com/cve/CVE-2014-9731
|     	CVE-2014-9644	2.1	https://vulners.com/cve/CVE-2014-9644
|     	CVE-2014-9585	2.1	https://vulners.com/cve/CVE-2014-9585
|     	CVE-2014-9584	2.1	https://vulners.com/cve/CVE-2014-9584
|     	CVE-2014-9419	2.1	https://vulners.com/cve/CVE-2014-9419
|     	CVE-2014-8133	2.1	https://vulners.com/cve/CVE-2014-8133
|     	CVE-2014-3645	2.1	https://vulners.com/cve/CVE-2014-3645
|     	CVE-2014-2038	2.1	https://vulners.com/cve/CVE-2014-2038
|     	CVE-2014-1739	2.1	https://vulners.com/cve/CVE-2014-1739
|     	CVE-2014-1738	2.1	https://vulners.com/cve/CVE-2014-1738
|     	CVE-2014-1445	2.1	https://vulners.com/cve/CVE-2014-1445
|     	CVE-2014-0206	2.1	https://vulners.com/cve/CVE-2014-0206
|     	CVE-2014-0181	2.1	https://vulners.com/cve/CVE-2014-0181
|     	CVE-2013-7421	2.1	https://vulners.com/cve/CVE-2013-7421
|     	C0ADE54F-990F-5E04-8AD2-C7DD772426F3	2.1	https://vulners.com/githubexploit/C0ADE54F-990F-5E04-8AD2-C7DD772426F3	*EXPLOIT*
|     	A9F0245C-3F9D-5922-A64E-F7627478A24A	2.1	https://vulners.com/githubexploit/A9F0245C-3F9D-5922-A64E-F7627478A24A	*EXPLOIT*
|     	A435389F-9C9F-5CEA-8255-C23422F533AB	2.1	https://vulners.com/githubexploit/A435389F-9C9F-5CEA-8255-C23422F533AB	*EXPLOIT*
|     	6E89126D-8B63-5397-9CCC-12A4A00199EF	2.1	https://vulners.com/githubexploit/6E89126D-8B63-5397-9CCC-12A4A00199EF	*EXPLOIT*
|     	3F37E677-DA72-5006-A200-8C99B713FBAE	2.1	https://vulners.com/githubexploit/3F37E677-DA72-5006-A200-8C99B713FBAE	*EXPLOIT*
|     	1337DAY-ID-32013	2.1	https://vulners.com/zdt/1337DAY-ID-32013	*EXPLOIT*
|     	1337DAY-ID-31822	2.1	https://vulners.com/zdt/1337DAY-ID-31822	*EXPLOIT*
|     	1337DAY-ID-31779	2.1	https://vulners.com/zdt/1337DAY-ID-31779	*EXPLOIT*
|     	1337DAY-ID-30016	2.1	https://vulners.com/zdt/1337DAY-ID-30016	*EXPLOIT*
|     	1337DAY-ID-30015	2.1	https://vulners.com/zdt/1337DAY-ID-30015	*EXPLOIT*
|     	SSV:61343	1.9	https://vulners.com/seebug/SSV:61343	*EXPLOIT*
|     	CVE-2015-2830	1.9	https://vulners.com/cve/CVE-2015-2830
|     	CVE-2015-1420	1.9	https://vulners.com/cve/CVE-2015-1420
|     	CVE-2014-4652	1.9	https://vulners.com/cve/CVE-2014-4652
|     	CVE-2014-1446	1.9	https://vulners.com/cve/CVE-2014-1446
|     	CVE-2013-2898	1.9	https://vulners.com/cve/CVE-2013-2898
|     	SSV:61345	1.7	https://vulners.com/seebug/SSV:61345	*EXPLOIT*
|     	PACKETSTORM:176405	1.7	https://vulners.com/packetstorm/PACKETSTORM:176405	*EXPLOIT*
|     	EXPLOITPACK:448F0B0D44522EA4F8F2133CF21B41E4	1.7	https://vulners.com/exploitpack/EXPLOITPACK:448F0B0D44522EA4F8F2133CF21B41E4	*EXPLOIT*
|     	CVE-2014-1444	1.7	https://vulners.com/cve/CVE-2014-1444
|     	5226B4B5-D53F-503C-8DD3-C3A316CA43FC	1.7	https://vulners.com/githubexploit/5226B4B5-D53F-503C-8DD3-C3A316CA43FC	*EXPLOIT*
|     	PACKETSTORM:170834	0.0	https://vulners.com/packetstorm/PACKETSTORM:170834	*EXPLOIT*
|     	PACKETSTORM:166258	0.0	https://vulners.com/packetstorm/PACKETSTORM:166258	*EXPLOIT*
|     	PACKETSTORM:155669	0.0	https://vulners.com/packetstorm/PACKETSTORM:155669	*EXPLOIT*
|     	PACKETSTORM:152663	0.0	https://vulners.com/packetstorm/PACKETSTORM:152663	*EXPLOIT*
|     	PACKETSTORM:150748	0.0	https://vulners.com/packetstorm/PACKETSTORM:150748	*EXPLOIT*
|     	PACKETSTORM:150001	0.0	https://vulners.com/packetstorm/PACKETSTORM:150001	*EXPLOIT*
|     	PACKETSTORM:148867	0.0	https://vulners.com/packetstorm/PACKETSTORM:148867	*EXPLOIT*
|     	PACKETSTORM:147806	0.0	https://vulners.com/packetstorm/PACKETSTORM:147806	*EXPLOIT*
|     	PACKETSTORM:147423	0.0	https://vulners.com/packetstorm/PACKETSTORM:147423	*EXPLOIT*
|     	PACKETSTORM:145235	0.0	https://vulners.com/packetstorm/PACKETSTORM:145235	*EXPLOIT*
|     	PACKETSTORM:141083	0.0	https://vulners.com/packetstorm/PACKETSTORM:141083	*EXPLOIT*
|     	D789A432-2137-57A8-BD99-560ABE0F7D40	0.0	https://vulners.com/githubexploit/D789A432-2137-57A8-BD99-560ABE0F7D40	*EXPLOIT*
|     	D5706C20-994B-524A-8C43-838B970CD47C	0.0	https://vulners.com/githubexploit/D5706C20-994B-524A-8C43-838B970CD47C	*EXPLOIT*
|     	CVE-2024-39469	0.0	https://vulners.com/cve/CVE-2024-39469
|     	CVE-2024-39301	0.0	https://vulners.com/cve/CVE-2024-39301
|     	CVE-2024-38659	0.0	https://vulners.com/cve/CVE-2024-38659
|     	CVE-2024-38634	0.0	https://vulners.com/cve/CVE-2024-38634
|     	CVE-2024-38633	0.0	https://vulners.com/cve/CVE-2024-38633
|     	CVE-2024-38630	0.0	https://vulners.com/cve/CVE-2024-38630
|     	CVE-2024-38621	0.0	https://vulners.com/cve/CVE-2024-38621
|     	CVE-2024-38619	0.0	https://vulners.com/cve/CVE-2024-38619
|     	CVE-2024-38613	0.0	https://vulners.com/cve/CVE-2024-38613
|     	CVE-2024-38607	0.0	https://vulners.com/cve/CVE-2024-38607
|     	CVE-2024-38601	0.0	https://vulners.com/cve/CVE-2024-38601
|     	CVE-2024-38599	0.0	https://vulners.com/cve/CVE-2024-38599
|     	CVE-2024-38597	0.0	https://vulners.com/cve/CVE-2024-38597
|     	CVE-2024-38596	0.0	https://vulners.com/cve/CVE-2024-38596
|     	CVE-2024-38589	0.0	https://vulners.com/cve/CVE-2024-38589
|     	CVE-2024-38588	0.0	https://vulners.com/cve/CVE-2024-38588
|     	CVE-2024-38583	0.0	https://vulners.com/cve/CVE-2024-38583
|     	CVE-2024-38578	0.0	https://vulners.com/cve/CVE-2024-38578
|     	CVE-2024-38570	0.0	https://vulners.com/cve/CVE-2024-38570
|     	CVE-2024-38567	0.0	https://vulners.com/cve/CVE-2024-38567
|     	CVE-2024-38565	0.0	https://vulners.com/cve/CVE-2024-38565
|     	CVE-2024-38553	0.0	https://vulners.com/cve/CVE-2024-38553
|     	CVE-2024-38538	0.0	https://vulners.com/cve/CVE-2024-38538
|     	CVE-2024-37078	0.0	https://vulners.com/cve/CVE-2024-37078
|     	CVE-2024-36968	0.0	https://vulners.com/cve/CVE-2024-36968
|     	CVE-2024-36960	0.0	https://vulners.com/cve/CVE-2024-36960
|     	CVE-2024-36946	0.0	https://vulners.com/cve/CVE-2024-36946
|     	CVE-2024-36939	0.0	https://vulners.com/cve/CVE-2024-36939
|     	CVE-2024-36934	0.0	https://vulners.com/cve/CVE-2024-36934
|     	CVE-2024-36905	0.0	https://vulners.com/cve/CVE-2024-36905
|     	CVE-2024-36883	0.0	https://vulners.com/cve/CVE-2024-36883
|     	CVE-2024-36286	0.0	https://vulners.com/cve/CVE-2024-36286
|     	CVE-2024-36270	0.0	https://vulners.com/cve/CVE-2024-36270
|     	CVE-2024-36016	0.0	https://vulners.com/cve/CVE-2024-36016
|     	CVE-2024-36013	0.0	https://vulners.com/cve/CVE-2024-36013
|     	CVE-2024-35969	0.0	https://vulners.com/cve/CVE-2024-35969
|     	CVE-2024-35967	0.0	https://vulners.com/cve/CVE-2024-35967
|     	CVE-2024-35966	0.0	https://vulners.com/cve/CVE-2024-35966
|     	CVE-2024-35965	0.0	https://vulners.com/cve/CVE-2024-35965
|     	CVE-2024-35915	0.0	https://vulners.com/cve/CVE-2024-35915
|     	CVE-2024-35896	0.0	https://vulners.com/cve/CVE-2024-35896
|     	CVE-2024-35887	0.0	https://vulners.com/cve/CVE-2024-35887
|     	CVE-2024-35886	0.0	https://vulners.com/cve/CVE-2024-35886
|     	CVE-2024-35877	0.0	https://vulners.com/cve/CVE-2024-35877
|     	CVE-2024-35828	0.0	https://vulners.com/cve/CVE-2024-35828
|     	CVE-2024-35823	0.0	https://vulners.com/cve/CVE-2024-35823
|     	CVE-2024-35821	0.0	https://vulners.com/cve/CVE-2024-35821
|     	CVE-2024-35811	0.0	https://vulners.com/cve/CVE-2024-35811
|     	CVE-2024-35808	0.0	https://vulners.com/cve/CVE-2024-35808
|     	CVE-2024-35807	0.0	https://vulners.com/cve/CVE-2024-35807
|     	CVE-2024-27437	0.0	https://vulners.com/cve/CVE-2024-27437
|     	CVE-2024-27436	0.0	https://vulners.com/cve/CVE-2024-27436
|     	CVE-2024-27419	0.0	https://vulners.com/cve/CVE-2024-27419
|     	CVE-2024-27415	0.0	https://vulners.com/cve/CVE-2024-27415
|     	CVE-2024-27405	0.0	https://vulners.com/cve/CVE-2024-27405
|     	CVE-2024-27402	0.0	https://vulners.com/cve/CVE-2024-27402
|     	CVE-2024-27399	0.0	https://vulners.com/cve/CVE-2024-27399
|     	CVE-2024-27388	0.0	https://vulners.com/cve/CVE-2024-27388
|     	CVE-2024-27074	0.0	https://vulners.com/cve/CVE-2024-27074
|     	CVE-2024-27073	0.0	https://vulners.com/cve/CVE-2024-27073
|     	CVE-2024-27059	0.0	https://vulners.com/cve/CVE-2024-27059
|     	CVE-2024-27043	0.0	https://vulners.com/cve/CVE-2024-27043
|     	CVE-2024-27008	0.0	https://vulners.com/cve/CVE-2024-27008
|     	CVE-2024-27001	0.0	https://vulners.com/cve/CVE-2024-27001
|     	CVE-2024-26999	0.0	https://vulners.com/cve/CVE-2024-26999
|     	CVE-2024-26994	0.0	https://vulners.com/cve/CVE-2024-26994
|     	CVE-2024-26981	0.0	https://vulners.com/cve/CVE-2024-26981
|     	CVE-2024-26976	0.0	https://vulners.com/cve/CVE-2024-26976
|     	CVE-2024-26973	0.0	https://vulners.com/cve/CVE-2024-26973
|     	CVE-2024-26956	0.0	https://vulners.com/cve/CVE-2024-26956
|     	CVE-2024-26955	0.0	https://vulners.com/cve/CVE-2024-26955
|     	CVE-2024-26923	0.0	https://vulners.com/cve/CVE-2024-26923
|     	CVE-2024-26894	0.0	https://vulners.com/cve/CVE-2024-26894
|     	CVE-2024-26875	0.0	https://vulners.com/cve/CVE-2024-26875
|     	CVE-2024-26872	0.0	https://vulners.com/cve/CVE-2024-26872
|     	CVE-2024-26851	0.0	https://vulners.com/cve/CVE-2024-26851
|     	CVE-2024-26840	0.0	https://vulners.com/cve/CVE-2024-26840
|     	CVE-2024-26825	0.0	https://vulners.com/cve/CVE-2024-26825
|     	CVE-2024-26816	0.0	https://vulners.com/cve/CVE-2024-26816
|     	CVE-2024-26812	0.0	https://vulners.com/cve/CVE-2024-26812
|     	CVE-2024-26810	0.0	https://vulners.com/cve/CVE-2024-26810
|     	CVE-2024-26804	0.0	https://vulners.com/cve/CVE-2024-26804
|     	CVE-2024-26758	0.0	https://vulners.com/cve/CVE-2024-26758
|     	CVE-2024-26756	0.0	https://vulners.com/cve/CVE-2024-26756
|     	CVE-2024-26744	0.0	https://vulners.com/cve/CVE-2024-26744
|     	CVE-2024-26733	0.0	https://vulners.com/cve/CVE-2024-26733
|     	CVE-2024-26696	0.0	https://vulners.com/cve/CVE-2024-26696
|     	CVE-2024-26687	0.0	https://vulners.com/cve/CVE-2024-26687
|     	CVE-2024-26677	0.0	https://vulners.com/cve/CVE-2024-26677
|     	CVE-2024-26675	0.0	https://vulners.com/cve/CVE-2024-26675
|     	CVE-2024-26654	0.0	https://vulners.com/cve/CVE-2024-26654
|     	CVE-2024-26636	0.0	https://vulners.com/cve/CVE-2024-26636
|     	CVE-2024-26635	0.0	https://vulners.com/cve/CVE-2024-26635
|     	CVE-2024-26625	0.0	https://vulners.com/cve/CVE-2024-26625
|     	CVE-2024-26622	0.0	https://vulners.com/cve/CVE-2024-26622
|     	CVE-2024-26614	0.0	https://vulners.com/cve/CVE-2024-26614
|     	CVE-2023-52881	0.0	https://vulners.com/cve/CVE-2023-52881
|     	CVE-2023-52878	0.0	https://vulners.com/cve/CVE-2023-52878
|     	CVE-2023-52868	0.0	https://vulners.com/cve/CVE-2023-52868
|     	CVE-2023-52843	0.0	https://vulners.com/cve/CVE-2023-52843
|     	CVE-2023-52803	0.0	https://vulners.com/cve/CVE-2023-52803
|     	CVE-2023-52784	0.0	https://vulners.com/cve/CVE-2023-52784
|     	CVE-2023-52774	0.0	https://vulners.com/cve/CVE-2023-52774
|     	CVE-2023-52742	0.0	https://vulners.com/cve/CVE-2023-52742
|     	CVE-2023-52730	0.0	https://vulners.com/cve/CVE-2023-52730
|     	CVE-2023-52708	0.0	https://vulners.com/cve/CVE-2023-52708
|     	CVE-2023-52703	0.0	https://vulners.com/cve/CVE-2023-52703
|     	CVE-2023-52693	0.0	https://vulners.com/cve/CVE-2023-52693
|     	CVE-2023-52669	0.0	https://vulners.com/cve/CVE-2023-52669
|     	CVE-2023-52653	0.0	https://vulners.com/cve/CVE-2023-52653
|     	CVE-2023-52644	0.0	https://vulners.com/cve/CVE-2023-52644
|     	CVE-2023-52629	0.0	https://vulners.com/cve/CVE-2023-52629
|     	CVE-2023-52615	0.0	https://vulners.com/cve/CVE-2023-52615
|     	CVE-2023-52614	0.0	https://vulners.com/cve/CVE-2023-52614
|     	CVE-2023-52609	0.0	https://vulners.com/cve/CVE-2023-52609
|     	CVE-2023-52578	0.0	https://vulners.com/cve/CVE-2023-52578
|     	CVE-2023-52574	0.0	https://vulners.com/cve/CVE-2023-52574
|     	CVE-2023-52572	0.0	https://vulners.com/cve/CVE-2023-52572
|     	CVE-2023-52566	0.0	https://vulners.com/cve/CVE-2023-52566
|     	CVE-2023-52531	0.0	https://vulners.com/cve/CVE-2023-52531
|     	CVE-2023-52528	0.0	https://vulners.com/cve/CVE-2023-52528
|     	CVE-2023-52527	0.0	https://vulners.com/cve/CVE-2023-52527
|     	CVE-2023-52522	0.0	https://vulners.com/cve/CVE-2023-52522
|     	CVE-2023-52515	0.0	https://vulners.com/cve/CVE-2023-52515
|     	CVE-2023-52507	0.0	https://vulners.com/cve/CVE-2023-52507
|     	CVE-2023-52502	0.0	https://vulners.com/cve/CVE-2023-52502
|     	CVE-2022-48758	0.0	https://vulners.com/cve/CVE-2022-48758
|     	CVE-2022-48757	0.0	https://vulners.com/cve/CVE-2022-48757
|     	CVE-2022-48636	0.0	https://vulners.com/cve/CVE-2022-48636
|     	CVE-2022-48627	0.0	https://vulners.com/cve/CVE-2022-48627
|     	CVE-2021-47618	0.0	https://vulners.com/cve/CVE-2021-47618
|     	CVE-2021-47597	0.0	https://vulners.com/cve/CVE-2021-47597
|     	CVE-2021-47589	0.0	https://vulners.com/cve/CVE-2021-47589
|     	CVE-2021-47583	0.0	https://vulners.com/cve/CVE-2021-47583
|     	CVE-2021-47566	0.0	https://vulners.com/cve/CVE-2021-47566
|     	CVE-2021-47565	0.0	https://vulners.com/cve/CVE-2021-47565
|     	CVE-2021-47549	0.0	https://vulners.com/cve/CVE-2021-47549
|     	CVE-2021-47544	0.0	https://vulners.com/cve/CVE-2021-47544
|     	CVE-2021-47485	0.0	https://vulners.com/cve/CVE-2021-47485
|     	CVE-2021-47482	0.0	https://vulners.com/cve/CVE-2021-47482
|     	CVE-2021-47479	0.0	https://vulners.com/cve/CVE-2021-47479
|     	CVE-2021-47477	0.0	https://vulners.com/cve/CVE-2021-47477
|     	CVE-2021-47475	0.0	https://vulners.com/cve/CVE-2021-47475
|     	CVE-2021-47474	0.0	https://vulners.com/cve/CVE-2021-47474
|     	CVE-2021-47456	0.0	https://vulners.com/cve/CVE-2021-47456
|     	CVE-2021-47418	0.0	https://vulners.com/cve/CVE-2021-47418
|     	CVE-2021-47416	0.0	https://vulners.com/cve/CVE-2021-47416
|     	CVE-2021-47401	0.0	https://vulners.com/cve/CVE-2021-47401
|     	CVE-2021-47396	0.0	https://vulners.com/cve/CVE-2021-47396
|     	CVE-2021-47391	0.0	https://vulners.com/cve/CVE-2021-47391
|     	CVE-2021-47375	0.0	https://vulners.com/cve/CVE-2021-47375
|     	CVE-2021-47366	0.0	https://vulners.com/cve/CVE-2021-47366
|     	CVE-2021-47351	0.0	https://vulners.com/cve/CVE-2021-47351
|     	CVE-2021-47344	0.0	https://vulners.com/cve/CVE-2021-47344
|     	CVE-2021-47315	0.0	https://vulners.com/cve/CVE-2021-47315
|     	CVE-2021-47314	0.0	https://vulners.com/cve/CVE-2021-47314
|     	CVE-2021-47310	0.0	https://vulners.com/cve/CVE-2021-47310
|     	CVE-2021-47297	0.0	https://vulners.com/cve/CVE-2021-47297
|     	CVE-2021-47288	0.0	https://vulners.com/cve/CVE-2021-47288
|     	CVE-2021-47276	0.0	https://vulners.com/cve/CVE-2021-47276
|     	CVE-2021-47250	0.0	https://vulners.com/cve/CVE-2021-47250
|     	CVE-2021-47249	0.0	https://vulners.com/cve/CVE-2021-47249
|     	CVE-2021-47237	0.0	https://vulners.com/cve/CVE-2021-47237
|     	CVE-2021-47236	0.0	https://vulners.com/cve/CVE-2021-47236
|     	CVE-2021-47188	0.0	https://vulners.com/cve/CVE-2021-47188
|     	CVE-2021-47168	0.0	https://vulners.com/cve/CVE-2021-47168
|     	CVE-2021-47153	0.0	https://vulners.com/cve/CVE-2021-47153
|     	CVE-2021-47146	0.0	https://vulners.com/cve/CVE-2021-47146
|     	CVE-2021-47122	0.0	https://vulners.com/cve/CVE-2021-47122
|     	CVE-2021-47121	0.0	https://vulners.com/cve/CVE-2021-47121
|     	CVE-2021-47119	0.0	https://vulners.com/cve/CVE-2021-47119
|     	CVE-2021-47118	0.0	https://vulners.com/cve/CVE-2021-47118
|     	CVE-2021-47103	0.0	https://vulners.com/cve/CVE-2021-47103
|     	C38E0645-3DE1-5134-94E3-00DFE9B99A88	0.0	https://vulners.com/githubexploit/C38E0645-3DE1-5134-94E3-00DFE9B99A88	*EXPLOIT*
|     	AC8391C6-9C7C-562A-A523-E925BC4005C3	0.0	https://vulners.com/githubexploit/AC8391C6-9C7C-562A-A523-E925BC4005C3	*EXPLOIT*
|     	9E1C498D-25A3-57B2-A391-764CDA0E674F	0.0	https://vulners.com/githubexploit/9E1C498D-25A3-57B2-A391-764CDA0E674F	*EXPLOIT*
|     	59D4903F-B387-50CB-AC2C-B34EB1920BF5	0.0	https://vulners.com/githubexploit/59D4903F-B387-50CB-AC2C-B34EB1920BF5	*EXPLOIT*
|     	1337DAY-ID-31237	0.0	https://vulners.com/zdt/1337DAY-ID-31237	*EXPLOIT*
|     	1337DAY-ID-30863	0.0	https://vulners.com/zdt/1337DAY-ID-30863	*EXPLOIT*
|     	1337DAY-ID-30727	0.0	https://vulners.com/zdt/1337DAY-ID-30727	*EXPLOIT*
|     	1337DAY-ID-30505	0.0	https://vulners.com/zdt/1337DAY-ID-30505	*EXPLOIT*
|     	1337DAY-ID-30284	0.0	https://vulners.com/zdt/1337DAY-ID-30284	*EXPLOIT*
|_    	1337DAY-ID-29921	0.0	https://vulners.com/zdt/1337DAY-ID-29921	*EXPLOIT*
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port80-TCP:V=7.94SVN%I=7%D=7/1%Time=66827EDF%P=x86_64-pc-linux-gnu%r(Ge
SF:tRequest,39,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x20Keep-
SF:Alive\r\n\r\n0\r\n\r\n")%r(HTTPOptions,F8,"HTTP/1\.1\x20404\x20Not\x20F
SF:ound\r\nContent-Type:text/html\r\nPragma:no-cache\r\nCache-control:no-c
SF:ache,\x20no-store,\x20max-age=0\r\nTransfer-Encoding:chunked\r\nX-Frame
SF:-Options:SAMEORIGIN\r\nConnection:Keep-Alive\r\n\r\n2f\r\nThe\x20reques
SF:ted\x20URL\x20was\x20not\x20found\x20on\x20this\x20server\.\r\n0\r\n\r\
SF:n")%r(RTSPRequest,F8,"HTTP/1\.1\x20404\x20Not\x20Found\r\nContent-Type:
SF:text/html\r\nPragma:no-cache\r\nCache-control:no-cache,\x20no-store,\x2
SF:0max-age=0\r\nTransfer-Encoding:chunked\r\nX-Frame-Options:SAMEORIGIN\r
SF:\nConnection:Keep-Alive\r\n\r\n2f\r\nThe\x20requested\x20URL\x20was\x20
SF:not\x20found\x20on\x20this\x20server\.\r\n0\r\n\r\n")%r(FourOhFourReque
SF:st,39,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x20Keep-Alive\
SF:r\n\r\n0\r\n\r\n")%r(GenericLines,67,"HTTP/1\.1\x20404\x20Not\x20Found\
SF:r\nConnection:\x20Keep-Alive\r\n\r\n2f\r\nThe\x20requested\x20URL\x20wa
SF:s\x20not\x20found\x20on\x20this\x20server\.\r\n")%r(SIPOptions,F8,"HTTP
SF:/1\.1\x20404\x20Not\x20Found\r\nContent-Type:text/html\r\nPragma:no-cac
SF:he\r\nCache-control:no-cache,\x20no-store,\x20max-age=0\r\nTransfer-Enc
SF:oding:chunked\r\nX-Frame-Options:SAMEORIGIN\r\nConnection:Keep-Alive\r\
SF:n\r\n2f\r\nThe\x20requested\x20URL\x20was\x20not\x20found\x20on\x20this
SF:\x20server\.\r\n0\r\n\r\n");
Service Info: OS: Linux; Device: broadband router; CPE: cpe:/o:linux:linux_kernel, cpe:/o:linux:linux_kernel:3.10.53-hulk2

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 13:05
Completed NSE at 13:05, 0.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 13:05
Completed NSE at 13:05, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 184.97 seconds
