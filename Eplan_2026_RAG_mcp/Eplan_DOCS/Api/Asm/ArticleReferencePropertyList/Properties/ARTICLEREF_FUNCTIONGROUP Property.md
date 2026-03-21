# ARTICLEREF_FUNCTIONGROUP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLEREF_FUNCTIONGROUP().html

---

Function group # 20489.

Syntax

**C#**



public PropertyValue ARTICLEREF_FUNCTIONGROUP {get; set;}

public:

property PropertyValue^ ARTICLEREF_FUNCTIONGROUP {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This field is for informational purposes and can be used, for instance, for filtering during part selection.

EPLAN reads article reference properties from function or if corresponding propoerty does not exists on function or is empty, then it is taken directly from the article. User needs to remember that setting values which removes property value for article reference property causes that they are read from article. Here is list of such values for each type: LONG - 0, STRING - empty string, BOOL - false, DOUBLE - 0.0 and for MULTILANGSTRING - empty multi lang string.
