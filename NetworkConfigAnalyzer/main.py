from parser import parse_config
from parser import read
device=parse_config("configs/SW8-CORE.txt")
configs=read("configs\SW8-CORE.txt")
print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
print("Interface Counter and Parser")
print("for Cybernet Certification & Training Center Network")
print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n")

print(f"Hostname: {device.hostname}\n")


while True:
    choice=int(input("What would you like to do?\n [(1)Show Interfaces] or [(2)Show Configurations] or [(0)Exit]?: "))

    if choice==1:
        intlen= len(device.interfaces)
        print("\n\n+++ NETWORK INTERFACES: " , intlen,"Interfaces +++\n")

        physical_interfaces=[
            interface for interface in device.interfaces
            if interface.name.startswith("FastEthernet")
            or interface.name.startswith("GigabitEthernet")
        ]
        print("Physical Interfaces: ", len(physical_interfaces))

        vlan_interfaces=[
            interface for interface in device.interfaces
            if interface.name.startswith("Vlan")
        ]
        print("VLAN Interfaces: ", len(vlan_interfaces), "\n")



        for interface in device.interfaces:
            print(interface.name)
            print(" Mode:", interface.mode)
            print(" Access VLAN:", interface.access_vlan)
            print(" Native VLAN:", interface.native_vlan)
            print(" Allowed VLANs:", interface.allowed_vlans)



    elif choice==2:
        print(configs)
    
    elif choice==0:
        break
    else:
        print("Invalid Choice.")