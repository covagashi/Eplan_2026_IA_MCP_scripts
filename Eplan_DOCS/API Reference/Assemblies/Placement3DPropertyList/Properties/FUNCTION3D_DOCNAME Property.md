# FUNCTION3D_DOCNAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_DOCNAME().html

---

Name of the M-CAD file # 36042.

Syntax

**C#**



public PropertyValue FUNCTION3D_DOCNAME {get; set;}

public:

property PropertyValue^ FUNCTION3D_DOCNAME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is used during data exchange with external CAD systems. The full file name and the full file path of the imported STEP file is stored in this property and is entered at the created design space and at the imported 3D objects.
