from models import Device, Interface


def parse_config(filepath):
    device = Device()
    current_interface = None

    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("hostname"):
                parts = line.split()
                if len(parts) >= 2:
                    device.hostname = parts[1]

            elif line.startswith("interface"):
                parts = line.split()
                if len(parts) >= 2:
                    current_interface = Interface(parts[1])
                    device.interfaces.append(current_interface)
            elif current_interface:

                if line.startswith("switchport mode"):
                    current_interface.mode = line.split()[-1]
                elif line.startswith("switchport access vlan"):
                    current_interface.access_vlan = line.split()[-1]

                elif line.startswith("switchport trunk native vlan"):
                    current_interface.native_vlan = line.split()[-1]

                elif line.startswith("switchport trunk allowed vlan"):
                    current_interface.allowed_vlans = line.split()[-1]

    return device

def read(filepath):
    with open(filepath,"r") as file:
        content=file.read()

    return content