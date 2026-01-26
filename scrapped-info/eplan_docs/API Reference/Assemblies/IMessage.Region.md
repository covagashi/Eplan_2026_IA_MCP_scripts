# IMessage.Region

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage+Region.html

---

Predefined regions for project messages; every project message must be assigned to one of these regions, other values will not be supported

Syntax

**C#**



public enum IMessage.Region : System.Enum

public enum class IMessage.Region : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **BlackBoxes** | 16 | 016 Black boxes |
| **Cables** | 3 | 003 Cables |
| **Connections** | 5 | 005 Connections |
| **CrossReferences** | 10 | 010 Cross-references |
| **Devices** | 7 | 007 Devices |
| **DeviceTags** | 17 | 017 DT |
| **DrillingPattern** | 32 | 032 Drilling pattern |
| **Eplan21Imports** | 19 | 018 Data transfer EPLAN 21 |
| **Eplan5Imports** | 18 | 018 Data transfer EPLAN 5 |
| **Externals** | 999 | 999 External |
| **Fluid** | 24 | 024 Fluid power |
| **ForeignLanguages** | 8 | 008 Foreign languages |
| **Harness** | 33 | 033 Harness |
| **InterruptionPoints** | 11 | 011 Interruption points |
| **Macro** | 14 | 014 Macro |
| **MountingLayout3D** | 26 | 026 3D mounting layout |
| **Others** | 22 | 022 Other |
| **PanelLayout2D** | 12 | 012 2D panel layout |
| **PartMasterData** | 502 | 502 Part master data |
| **PartsData** | 13 | 013 Parts data |
| **PlaceholderObject** | 21 | 021 Placeholder objects |
| **PLCBus** | 4 | 004 PLC / bus |
| **Plugs** | 2 | 002 Plugs |
| **PrePlanning** | 28 | 028 Pre-planning |
| **PrePlanningDepth** | 29 | 029 Pre-planning depth |
| **ProjectCompare** | 20 | 020 Project comparison |
| **ProjectSettings** | 25 | 025 Project settings |
| **Reports** | 15 | 015 Reports |
| **Subprojects** | 30 | 030 Subprojects |
| **Terminals** | 1 | 001 Terminals |
| **Topology** | 27 | 027 Topology |
| **Unknown** | 0 | Undefined |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.EServices.IMessage.Region**
