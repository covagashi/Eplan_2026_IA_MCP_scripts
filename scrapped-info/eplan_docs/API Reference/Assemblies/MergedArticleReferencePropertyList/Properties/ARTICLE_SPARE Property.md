# ARTICLE_SPARE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLE_SPARE().html

---

Spare part # 22140.

Syntax

**C#**



public PropertyValue ARTICLE_SPARE {get; set;}

public:

property PropertyValue^ ARTICLE_SPARE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Identifies a spare part, e.g. the name of the item that can replace the defective or worn part.

EPLAN reads article reference properties from function or if corresponding propoerty does not exists on function or is empty, then it is taken directly from the article. User needs to remember that setting values which removes property value for article reference property causes that they are read from article. Here is list of such values for each type: LONG - 0, STRING - empty string, BOOL - false, DOUBLE - 0.0 and for MULTILANGSTRING - empty multi lang string.
