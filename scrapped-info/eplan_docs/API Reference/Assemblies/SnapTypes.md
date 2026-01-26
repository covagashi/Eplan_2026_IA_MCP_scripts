# SnapTypes

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.SnapTypes.html

---

Type of snap.

Syntax

**C#**



public enum SnapTypes : System.Enum

public enum class SnapTypes : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **Axis** | 64 | axis |
| **Center** | 8 | center of circle |
| **CustomSnap** | 16384 | custom snaps implemented by interaction |
| **End** | 1 | start or endpoint of line |
| **InsertionPos** | 32 | insertion point of text or symbol reference |
| **Intersection** | 16 | intersection point between placements |
| **Mid** | 2 | mid point of line |
| **NoSnapType** | 0 | no snap |
| **Perpendicular** | 4 | perpendicular to line from current position |
| **PointMate** | 4096 | point mates (only 3d) |
| **PriorInsertionPos** | 512 | exclusive for insertion point of text or symbol reference. |
| **ReserveSnap** | 256 | for future enhancements |
| **Tangent** | 1024 | tangent to a circle |
| **Text** | 128 | text |
| **Virtual** | 2048 | virtual intersection point |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.EServices.Ged.SnapTypes**
