# ARTICLE_CUSTOM_DATA_VALUE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~ARTICLE_CUSTOM_DATA_VALUE(Int32).html

---

API Parts Management Extension: Value from add-in # 22213.

Syntax

**C#**



public PropertyValue ARTICLE_CUSTOM_DATA_VALUE( 

   int index

) {get; set;}

public:

property PropertyValue^ ARTICLE_CUSTOM_DATA_VALUE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 100.

This property is used by the "API Parts Management Extension" module. Using this module, you can add user-defined data from a database of your own to the parts that are stored in the Eplan parts database. It is intended for information that you do not want to save to existing part properties. You can assign this information to a part and display it in parts management. If such a part is exported or stored in the project, this information will be stored in the properties "API Parts Management Extension: Name of add-in" (ID 22212) and "API Parts Management Extension: Value from add-in" (ID 22213). In the property ID 22212, the name of the add-in is stored via the index; up to 100 are possible. In the property ID 22213, the value from the add-in with the same index is stored via the index.
