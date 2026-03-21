# DMG_COMMENT_RESPONSE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.CommentPropertyList~DMG_COMMENT_RESPONSE(Int32).html

---

Reply text # 19504.

Syntax

**C#**



public PropertyValue DMG_COMMENT_RESPONSE( 

   int index

) {get; set;}

public:

property PropertyValue^ DMG_COMMENT_RESPONSE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 100.
