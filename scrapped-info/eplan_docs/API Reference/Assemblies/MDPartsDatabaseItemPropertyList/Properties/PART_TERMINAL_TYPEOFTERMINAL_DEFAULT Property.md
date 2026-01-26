# PART_TERMINAL_TYPEOFTERMINAL_DEFAULT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1724.html

---

Connection category (default) # 22968.

Syntax

**C#**



public MDPropertyValue PART_TERMINAL_TYPEOFTERMINAL_DEFAULT {get; set;}

public:

property MDPropertyValue^ PART_TERMINAL_TYPEOFTERMINAL_DEFAULT {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is used if no connection category has been entered for the individual connection point in the connection point pattern. Specifies the connection point type of a connection more exactly:

0 = Undefined

1 = Screw clamp connection single (do not use anymore)

2 = Screw clamp connection double (do not use anymore)

3 = Cage clamp connection (do not use anymore)

4 = Insulation-displacement connection

5 = Screw-type connection (Ring or U cable lug), (do not use anymore)

6 = Ferrule connection (cable lug), (do not use anymore)

7 = Plug connection (do not use anymore)

8 = Conductor plate connection (do not use anymore)

9 = Plug-in connection (Fluid), (do not use anymore)

10 = Nipple (do not use anymore)

11 = Internal thread

12 = External thread

13 = Compression nut (do not use anymore)

14 = Compression fitting (do not use anymore)

15 = User-defined

1015 = Screw connection

1016 = Spring pulley connection

1017 = Push-in connection

1018 = Penetration connection

1019 = Push-in fitting

1020 = Push-wire connection

1021 = Bolt connection

1022 = Flat plug-in connector

1023 = Crimp connection

1024 = Band connection

1025 = Rail connection

1026 = Soldering lug connection

1027 = Wrap post.
