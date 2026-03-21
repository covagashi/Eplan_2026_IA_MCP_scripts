# FUNC_LOGDEF_ISEXTERN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_LOGDEF_ISEXTERN(Int32).html

---

Connection point logic: External # 20321.

Syntax

**C#**



public PropertyValue FUNC_LOGDEF_ISEXTERN( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_LOGDEF_ISEXTERN {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Boolean.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Defines whether the connection point is to be interpreted as external. Using the index, you can differentiate between up to 100 settings.
