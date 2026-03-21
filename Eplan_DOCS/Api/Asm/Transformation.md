# Transformation

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Transformation.html

---

Class to determine displacement and scaling of objects (used for methods of the Import class). The following example shows how to use class Import.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.Transformation**

Syntax

**C#**



public class Transformation

public ref class Transformation


Example

The following example shows how to use class Import.

**C#**

```


Import oImport = new Import();

Transformation oTransformation = new Transformation();

oTransformation.XOffset = 80;

oTransformation.XScale = 0.1;

oTransformation.YOffset = 60;

oTransformation.YScale = 0.1;

oImport.DXFPage("$(MD_DXFDWG)\\test_6c.dxf", m_oProject.Pages[5], oTransformation, "");

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Transformation Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Transformation~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [DrawingLimit](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Transformation~DrawingLimit.html) | Get drawing limits |
| Public Property | [Height](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Transformation~Height.html) | Get height of imported element |
| Public Property | [Width](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Transformation~Width.html) | Get width of imported element |
| Public Property | [XOffset](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Transformation~XOffset.html) | Set offset in x-direction |
| Public Property | [XScale](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Transformation~XScale.html) | Set scaling in x-direction |
| Public Property | [XScaleRef](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Transformation~XScaleRef.html) | Set scaling reference in x-direction |
| Public Property | [YOffset](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Transformation~YOffset.html) | Set offset in y-direction |
| Public Property | [YScale](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Transformation~YScale.html) | Set scaling in y-direction |
| Public Property | [YScaleRef](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Transformation~YScaleRef.html) | Set scaling reference in y-direction |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Transformation~Dispose().html) | Destructor. |


