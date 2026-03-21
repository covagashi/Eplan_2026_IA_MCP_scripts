# FUNC_SOURCE_CP_LENGTH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_SOURCE_CP_LENGTH().html

---

Cables: Connection point length source # 20243.

Syntax

**C#**



public PropertyValue FUNC_SOURCE_CP_LENGTH {get; set;}

public:

property PropertyValue^ FUNC_SOURCE_CP_LENGTH {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Indicates the item length of the connection that is required to connect the source item. It is by this value that the cable must project at the last routing point.
