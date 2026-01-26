# FUNC_ARTICLE_VERSION_AS_MAINTENANCE_REPAIR_SWITCH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic456.html

---

Design as maintenance / repair switch # 31178.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_VERSION_AS_MAINTENANCE_REPAIR_SWITCH( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_VERSION_AS_MAINTENANCE_REPAIR_SWITCH {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Boolean.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specification whether the switch version is suitable for use as a maintenance / repair switch on the basis of the technical properties.
