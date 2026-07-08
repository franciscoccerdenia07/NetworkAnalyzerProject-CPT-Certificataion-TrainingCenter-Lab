# NetworkAnalyzerProject-CPT-Certificataion-TrainingCenter-Lab
- This is continuation and more projects related to my CPT-Certification/TrainingCenter-Lab Network Project. I plan to add more projects that can  be tools and my original network lab will serve as the foundation to use tools and projects I plan to create in the future.
- This project was created to improve my Python programming skills while applying networking concepts learned through Cisco Packet Tracer and Cisco IOS configuration.
- As someone interested in networking and cybersecurity, I wanted to build a project that combines Python programming with Cisco networking concepts.
- Rather than creating another beginner Python project, I wanted something that solves networking problems, even if it means starting from the simplest and easiest tasks.
- This project also serves as a practical way to strengthen my understanding of | Python | OOP | Configuration parsing | Network automation | Cisco IOS | Auditing (hopefully) |
- 
---

## V1.1 -> Interface Counter and Parser Only

- For this project, I started studying and learning essential tools I can use in relation to my original Network Project. The console asks for 2 options, starting with Interface Counter by simply being able to read txt files containing copy-pasted manual configurations on each device. For instance, the running-configuration of SW1-LAB1 contents are read using file.read and return and displays line by line. 
-On the other hand, the parsing.

---

### Current Features (V1.1)

- Read Cisco IOS configuration files (.txt)
- Parse device hostname
- Detect physical interfaces
  - FastEthernet
  - GigabitEthernet
- Parse interface switchport mode
  - Access
  - Trunk
- Parse access VLAN assignments
- Parse native VLAN configuration
- Parse allowed VLAN lists
- Display interface summaries
- View original device configuration

---


## Project Structure

```
NetworkAnalyzerProject/
-> configs/
  --> SW1-LAB1.txt, SW8-CORE, etc.
-
-> main.py          # Console
-> parser.py        # Cisco config parser
-> models.py        # Data models
-
-> README.md

```

---

## Sample Output

```
*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
Interface Counter and Parser
for Cybernet Certification & Training Center Network
*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*

Hostname: SW8-CORE

What would you like to do?
 [(1)Show Interfaces] or [(2)Show Configurations] or [(0)Exit]?: 1


+++ NETWORK INTERFACES:  37 Interfaces +++

Physical Interfaces:  26
VLAN Interfaces:  11 

FastEthernet0/1
 Mode: trunk
 Access VLAN: 
 Native VLAN: 100
 Allowed VLANs: 90,100
FastEthernet0/2
 Mode: trunk
 Access VLAN: 
 Native VLAN: 100
 Allowed VLANs: 10,100
FastEthernet0/3
 Mode: trunk
 Access VLAN: 
 Native VLAN: 100
 Allowed VLANs: 20,100
FastEthernet0/4
 Mode: trunk
 Access VLAN: 
 Native VLAN: 100
 Allowed VLANs: 30,100
FastEthernet0/5
 Mode: trunk
 Access VLAN: 
 Native VLAN: 100
 Allowed VLANs: 40,100
FastEthernet0/6
 Mode: trunk
 Access VLAN: 
 Native VLAN: 100
 Allowed VLANs: 50,100
FastEthernet0/7
 Mode: trunk
 Access VLAN: 
 Native VLAN: 100
 Allowed VLANs: 60,70,80,100
FastEthernet0/8
 Mode: trunk
 Access VLAN: 
 Native VLAN: 100
 Allowed VLANs: 10,100
FastEthernet0/9
 Mode: 
 Access VLAN: 
 Native VLAN: 100
 Allowed VLANs: 20,100
FastEthernet0/10
 Mode: trunk
 Access VLAN: 
 Native VLAN: 100
 Allowed VLANs: 30,100
FastEthernet0/11
 Mode: trunk
 Access VLAN: 
 Native VLAN: 100
 Allowed VLANs: 40,100
FastEthernet0/12
 Mode: trunk
 Access VLAN: 
 Native VLAN: 100
 Allowed VLANs: 50,100
FastEthernet0/13
 Mode: trunk
 Access VLAN: 
 Native VLAN: 100
 Allowed VLANs: 60,70,80,100
FastEthernet0/14
 Mode: trunk
 Access VLAN: 
 Native VLAN: 100
 Allowed VLANs: 90,100
FastEthernet0/15
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
FastEthernet0/16
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
FastEthernet0/17
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
FastEthernet0/18
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
FastEthernet0/19
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
FastEthernet0/20
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
FastEthernet0/21
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
FastEthernet0/22
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
FastEthernet0/23
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
FastEthernet0/24
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
GigabitEthernet0/1
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
GigabitEthernet0/2
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
Vlan1
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
Vlan10
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
Vlan20
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
Vlan30
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
Vlan40
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
Vlan50
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
Vlan60
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
Vlan70
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
Vlan80
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
Vlan90
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
Vlan99
 Mode: 
 Access VLAN: 
 Native VLAN: 
 Allowed VLANs: 
What would you like to do?
 [(1)Show Interfaces] or [(2)Show Configurations] or [(0)Exit]?: 
```

---

## How It Works

1. Read any Configuration file copy-pasted from device IOS.
2. Parse the configuration line-by-line.
3. Converts configuration sections into Python objects.
4. Store parsed info in structured models.
5. Displays list and number of Interfaces or the Configurations themselves.


---


## Future Planned Features/Projects

- [x] Parse hostname
- [x] Parse interfaces
- [x] Parse switchport mode
- [x] Parse VLAN information
- [ ] IP/Subnet
- [ ] VLAN parser
- [ ] Routing parser
- [ ] ACL parser
- [ ] HSRP parser
- [ ] Cisco ASA parser
- [ ] Firewall audit


---

## Sample Configuration

The project currently uses any Cisco IOS configuration files exported from Cisco Packet Tracer laboratory exercises.

---

