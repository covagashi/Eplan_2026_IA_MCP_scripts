# ARTICLEREF_ARTICLEDEFINITION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLEREF_ARTICLEDEFINITION().html

---

Part of a part definition # 20508.

Syntax

**C#**



public PropertyValue ARTICLEREF_ARTICLEDEFINITION {get; set;}

public:

property PropertyValue^ ARTICLEREF_ARTICLEDEFINITION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

Parts which are assigned to a part definition do not belong to any specific device. They might belong to parts included in the delivery, general installation materials, etc. In contrast to project parts, parts that are assigned to a part definition are assigned to specific project structures.
