import winreg

def enable_remote_connections():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Control\Terminal Server', 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, 'fDenyTSConnections', 0, winreg.REG_DWORD, 0)
        print("Remote connections enabled successfully.")
    except Exception as e:
        print(f"Failed to enable remote connections: {str(e)}")
    finally:
        if key:
            winreg.CloseKey(key)

def disable_remote_connections():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Control\Terminal Server', 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, 'fDenyTSConnections', 0, winreg.REG_DWORD, 1)
        print("Remote connections disabled successfully.")
    except Exception as e:
        print(f"Failed to disable remote connections: {str(e)}")
    finally:
        if key:
            winreg.CloseKey(key)

# Example usage:
#enable_remote_connections()
disable_remote_connections()
