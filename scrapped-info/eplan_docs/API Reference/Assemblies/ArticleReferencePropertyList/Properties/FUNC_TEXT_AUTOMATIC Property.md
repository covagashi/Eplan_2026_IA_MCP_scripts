# FUNC_TEXT_AUTOMATIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~FUNC_TEXT_AUTOMATIC().html

---

Function text (automatic) # 20031.

Syntax

**C#**



public PropertyValue FUNC_TEXT_AUTOMATIC {get; set;}

public:

property PropertyValue^ FUNC_TEXT_AUTOMATIC {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is read-only..

Displays the content of the manually entered function text or, if it is empty, the path function text. When this property is displayed on a project page, the line breaks are removed.
