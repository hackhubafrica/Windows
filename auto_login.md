# Method 1: Using Command Prompt

Open Command Prompt as Administrator:
        
Press Windows + X, then select Command Prompt (Admin) or Windows Terminal (Admin).

  Type the following command and press Enter:

    control userpasswords2

Uncheck "Users must enter a user name and password to use this computer":
In the User Accounts window that appears, make sure the box is unchecked.

Click OK.

Restart your computer to apply the changes.

# Method 2: Using the Registry Editor

  Open the Registry Editor:
        Press Windows + R, type regedit, and press Enter.

  Navigate to the following key:

    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon

  Double-click the "AutoAdminLogon" entry on the right-hand side.

  Change the value from "1" to "0" and click OK.

  Check for and delete any "DefaultUserName", "DefaultPassword", and "DefaultDomainName" entries if they exist. This ensures Windows won't automatically log in with specific credentials.

  Restart your computer to apply the changes.

# Method 3: Using Group Policy Editor (Windows Pro and Enterprise editions)

  Open Group Policy Editor:
        Press Windows + R, type gpedit.msc, and press Enter.

  Navigate to the following path:

        Computer Configuration -> Windows Settings -> Security Settings -> Local Policies -> Security Options

  Find and double-click on "Interactive logon: Do not display last user name".

    Select "Enabled" and click OK.

  Restart your computer to apply the changes.

Note:

If you're using a Windows edition that doesn't have Group Policy Editor (like Windows Home), you might not be able to use Method 3.

Always be cautious when modifying the Windows Registry (Method 2), as incorrect changes can cause system instability.
