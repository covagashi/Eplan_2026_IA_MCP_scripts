# ARTICLE_ERPNR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLE_ERPNR().html

---

ERP / PDM number 1 # 22056.

Syntax

**C#**



public PropertyValue ARTICLE_ERPNR {get; set;}

public:

property PropertyValue^ ARTICLE_ERPNR {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Unique part number of an external ERP system or PDM system. The ERP / PDM numbers must be unique for different parts. Same values are also permitted for the properties "ERP / PDM number 1" to "ERP / PDM number 10" at a part. Any number of characters can be entered for the ERP / PDM number. However, only the first 64 characters in UTF-8 format are identifying. If you assign a value via the Application Programming Interface you have to specify the same value for all part variants.

EPLAN reads article reference properties from function or if corresponding propoerty does not exists on function or is empty, then it is taken directly from the article. User needs to remember that setting values which removes property value for article reference property causes that they are read from article. Here is list of such values for each type: LONG - 0, STRING - empty string, BOOL - false, DOUBLE - 0.0 and for MULTILANGSTRING - empty multi lang string.
