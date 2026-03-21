# DMG_COMMENT_RESPONSE_DATETIME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.CommentPropertyList~DMG_COMMENT_RESPONSE_DATETIME(Int32).html

---

Date and time # 19505.

Syntax

**C#**



public PropertyValue DMG_COMMENT_RESPONSE_DATETIME( 

   int index

) {get; set;}

public:

property PropertyValue^ DMG_COMMENT_RESPONSE_DATETIME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.DateTime.

Remarks

Property is indexed. Possible indexes are from 1 to 100.

Date and time of the reply. The time is output in the local time of the user in accordance with the set time zone.
