# FUNCTION3D_MOUNTINGLOCATION_AUTOMATIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~FUNCTION3D_MOUNTINGLOCATION_AUTOMATIC().html

---

Mounting site (describing, common) # 36003.

Syntax

**C#**



public PropertyValue FUNCTION3D_MOUNTINGLOCATION_AUTOMATIC {get; set;}

public:

property PropertyValue^ FUNCTION3D_MOUNTINGLOCATION_AUTOMATIC {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is read-only..

Shows the contents of the manually entered "Mounting site (describing)" property or if this is empty, the "Mounting site (describing)" property entered at the main function.
