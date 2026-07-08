class Device:
    def __init__(self):
        self.hostname = ""
        self.interfaces=[]


class Interface:
    def __init__(self, name):
        self.name=name
        self.mode="" 
        self.access_vlan=""
        self.native_vlan=""
        self.allowed_vlans=""