# FUNC_ARTICLE_ASSEMBLYVARIANT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1113.html

---

Cable entry into device # 26396.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_CABLE_ENTRY_INTO_THE_DEVICE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CABLE_ENTRY_INTO_THE_DEVICE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specifies the way in which a cable is inserted and fastened into the device, for example by means of a screw connection.
