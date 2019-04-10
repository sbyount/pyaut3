from netmiko import ConnectHandler

def ssh_command(device, command):
    """Establish an SSH connection. Execute command, return results."""
    device = ConnectHandler(**device)
    output = device.send_command(command)
    device.disconnect()
    print(output)
    return

def ssh_command2(device, command):
    """Establish an SSH connection. Execute command, return results."""
    device = ConnectHandler(**device)
    output = device.send_command(command)
    device.disconnect()
    return output
