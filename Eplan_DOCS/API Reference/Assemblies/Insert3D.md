# Insert3D

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert3D.html

---

Inserts 3-d macros into layout space.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.Insert3D**

Syntax

**C#**



public class Insert3D

public ref class Insert3D


Remarks

Please mind that in case of 3d macros, the root object(s) could be transformed. So if you insert a macro on position 0,0,0 of a layout space, the transformation of root object will be not 0,0,0 but the one copied from window macro. If you want to reset root object(s) in a macro to 0,0,0 position, please use WindowMacro::ResetPositions3D method.

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Insert3D Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert3D~_ctor.html) | Default constructor |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert3D~Dispose().html) | Destructor |
| Public Method | [SymbolMacro](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert3D~SymbolMacro.html) | Places objects from symbol macro into layout space. |
| Public Method | [WindowMacro](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert3D~WindowMacro.html) | Overloaded. Places a window macro with snapping source mate to a target mate from another object. |


