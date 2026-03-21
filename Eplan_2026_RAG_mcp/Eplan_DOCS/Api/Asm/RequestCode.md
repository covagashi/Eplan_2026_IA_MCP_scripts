# RequestCode

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.RequestCode.html

---

Available request which can be done by interaction event handler.

Syntax

**C#**



[Flags()]

public enum RequestCode : System.Enum

[Flags()]

public enum class RequestCode : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **Abort** | 512 | abort interaction |
| **AllowEmptySelection** | 65536 | in addition to fSelect this flag allows empty selection sets |
| **AllowProgress** | 262144 | allow progress bar in onSuccess |
| **Angle** | 256 | input of angle needed |
| **AutoConnection** | 16384 |  |
| **CallDefaultFunction** | 4096 | default event handler should be called |
| **Drag** | 32 | dragging is allowed |
| **Edge** | 1048576 | input or select edge |
| **Face** | 2097152 | input or select face |
| **Highlite** | 2048 | highlight of objects below mouse wanted |
| **IgnoreGroup** | 524288 |  |
| **InputFinish** | 16777216 | finish input (example: end polyline) |
| **Internal1** | 32768 | for internal use only |
| **Internal2** | 4194304 | for internal use |
| **Length** | 128 | input of Length needed |
| **NoCommandLine** | 67108864 |  |
| **NoCrossCursor** | 64 | suppress cross cursor |
| **NoMultiSelect** | 4 | may be combined with Selectonly one placement can be selected |
| **NoPreselect** | 8 |  |
| **Nothing** | 0 | event handler has no additional request |
| **Point** | 16 | coordinates of point are needed |
| **Reserved1** | 8388608 | for future use |
| **Reserved2** | 33554432 | for future use |
| **Restart** | 8192 |  |
| **Select** | 2 | selection of placements required |
| **Stop** | 1 | stop interaction |
| **Success** | 1024 | input of data was successful |
| **SystemDrag** | 131072 | dragging outside the window is allowed/requested |
| **Vertex** | 268435456 | selection of existing 3D vertex/point |
| **Wait** | 134217728 | should be used after start of sub interaction |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.EServices.Ged.RequestCode**
