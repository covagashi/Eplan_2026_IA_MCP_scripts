# FUNC_DEVICETAGSEARCHDIRECTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_DEVICETAGSEARCHDIRECTION().html

---

DT adoption: Search direction # 20035.

Syntax

**C#**



public PropertyValue FUNC_DEVICETAGSEARCHDIRECTION {get; set;}

public:

property PropertyValue^ FUNC_DEVICETAGSEARCHDIRECTION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Shows the search direction for the DT adoption:

0 = According to orientation of plot frame

1 = As an alternative to orientation of plot frame

2 = Only from boxes.

Additional information can be obtained in the help system in the sections "DT adoption" and "Defining the Search Direction for DT Adoption".
