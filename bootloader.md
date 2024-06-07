To fix bootloader issues in Windows using a live image disk, you can follow these general steps:

Boot from the Windows Installation Media: Insert your Windows installation disk or USB drive into your computer and boot from it. 
You may need to change the boot order in your BIOS or UEFI settings to prioritize booting from the installation media.

Access Repair Options: Once the Windows installation screen appears, select your language preferences and click "Next."
Then, instead of clicking "Install now," look for the option to "Repair your computer" or "Troubleshoot." Click on it to access repair options.

Launch Command Prompt: In the repair options menu, you should find an option to open a Command Prompt. T
his will allow you to access the command line interface for performing repair tasks.

Run Bootrec Commands: Use the bootrec command-line tool to repair the bootloader. Here are the common commands you can use:
    
    bootrec /fixmbr  #: Repairs the Master Boot Record (MBR).
    bootrec /fixboot   #: Writes a new boot sector onto the system partition.
    bootrec /rebuildbcd    #: Scans all disks for installations compatible with Windows and allows you to add them to the BCD (Boot Configuration Data).

Run these commands one by one, pressing Enter after each command, and follow any on-screen prompts.
Restart Your Computer: After running the necessary bootrec commands, type exit to close the Command Prompt window, and then restart your computer.
check Boot: After restarting, your computer should boot into Windows normally. 
If you're still experiencing issues, you may need to repeat the steps or consider other troubleshooting options.
