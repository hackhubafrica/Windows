Configuring DNS settings in Windows can be done through the Control Panel, Settings app, or using Command Prompt/PowerShell. Below are the methods for each approach:
Method 1: Using the Control Panel

    Open Control Panel:
        Press Win + R, type control, and press Enter.

    Network and Sharing Center:
        Go to Network and Internet > Network and Sharing Center.

    Change Adapter Settings:
        In the left pane, click on Change adapter settings.

    Select Network Adapter:
        Right-click on the network adapter you want to configure (e.g., Ethernet, Wi-Fi) and select Properties.

    Internet Protocol Version 4 (TCP/IPv4):
        Select Internet Protocol Version 4 (TCP/IPv4) and click Properties.

    Configure DNS Servers:
        Select Use the following DNS server addresses.
        Enter the preferred and alternate DNS server addresses. For example:
            Preferred DNS server: 8.8.8.8 (Google Public DNS)
            Alternate DNS server: 8.8.4.4 (Google Public DNS)
        Click OK.

    Internet Protocol Version 6 (TCP/IPv6) (Optional):
        If you are using IPv6, select Internet Protocol Version 6 (TCP/IPv6) and click Properties.
        Enter the IPv6 DNS server addresses if needed.

    Close and Apply:
        Click OK to close the properties window.
        Close the Network Connection Properties window.

Method 2: Using the Settings App (Windows 10 and Windows 11)

    Open Settings:
        Press Win + I to open the Settings app.

    Network & Internet:
        Go to Network & Internet.

    Select Network Adapter:
        Click on Status in the left pane.
        Click on Change adapter options.

    Select Network Adapter:
        Right-click on the network adapter you want to configure (e.g., Ethernet, Wi-Fi) and select Properties.

    Internet Protocol Version 4 (TCP/IPv4):
        Select Internet Protocol Version 4 (TCP/IPv4) and click Properties.

    Configure DNS Servers:
        Select Use the following DNS server addresses.
        Enter the preferred and alternate DNS server addresses. For example:
            Preferred DNS server: 8.8.8.8 (Google Public DNS)
            Alternate DNS server: 8.8.4.4 (Google Public DNS)
        Click OK.

    Internet Protocol Version 6 (TCP/IPv6) (Optional):
        If you are using IPv6, select Internet Protocol Version 6 (TCP/IPv6) and click Properties.
        Enter the IPv6 DNS server addresses if needed.

    Close and Apply:
        Click OK to close the properties window.
        Close the Network Connection Properties window.

Method 3: Using Command Prompt

    Open Command Prompt as Administrator:
        Press Win + X and select Command Prompt (Admin) or Windows PowerShell (Admin).

    Set DNS Server:
        Use the following command to set the DNS server. Replace Wi-Fi with the name of your network adapter and the IP addresses with your preferred DNS servers:

        cmd

        netsh interface ip set dns name="Wi-Fi" source=static addr=8.8.8.8
        netsh interface ip add dns name="Wi-Fi" addr=8.8.4.4 index=2

Method 4: Using PowerShell

    Open PowerShell as Administrator:
        Press Win + X and select Windows PowerShell (Admin).

    Set DNS Server:
        Use the following command to set the DNS server. Replace Wi-Fi with the name of your network adapter and the IP addresses with your preferred DNS servers:

        powershell

        Set-DnsClientServerAddress -InterfaceAlias "Wi-Fi" -ServerAddresses 8.8.8.8,8.8.4.4

These methods should allow you to configure DNS settings on your Windows machine effectively.