# FUNC_PLC_BUSSYSTEM Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLC_BUSSYSTEM().html

---

Bus system # 20308.

Syntax

**C#**



public PropertyValue FUNC_PLC_BUSSYSTEM {get; set;}

public:

property PropertyValue^ FUNC_PLC_BUSSYSTEM {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Type of bus system to which a bus port is assigned as a bus node. The following values are possible:

0 = Other bus systems

1 = CANbus

2 = DeviceNet

3 = EtherCAT

4 = Ethernet

5 = Foundation Fieldbus

6 = Interbus

7 = Lightbus

8 =Local bus: Rack /PLC card

9 = ModBus

10 = MPI bus

11 = PROFIBUS

12 = PROFINET

13 = ASI

14 = Local-Bus: Extension

15 = X2X

16 = Powerlink

17 = CC-Link

18 = ControlNet

19 = DALI

20 = EIB

21 = EtherNet/IP

22 = FIPIO

23 = LON

24 = RS232/RS485

25 = SERCOS interface

26 = USB

27 = IPLink

28 = Axioline

29 = DIOBus

30 = RIOBus

31 = ERIOBus

32 = RIO/DIO bus

33 = MDI I/O bus

34 = VARAN

35 = CC-Link IE

36 = Modbus TCP

37 = SERCOS III

38 = DRIVE-CLiQ

39 = SSCNET III

40 = CC-Link IE Control

41 = CC-Link IE Field

42 = IO-Link

43 = SSI

44 = ET-Connection

45 = CC-Link IE Field Basic

46 = PortToPort

47 = MELSECNET/H

48 = EtherCAT P

49 = EtherCAT G

50 = BACnet

51 = KNX
