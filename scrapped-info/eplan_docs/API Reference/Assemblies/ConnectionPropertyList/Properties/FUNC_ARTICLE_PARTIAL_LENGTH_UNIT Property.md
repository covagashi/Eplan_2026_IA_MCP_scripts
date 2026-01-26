# FUNC_ARTICLE_PARTIAL_LENGTH_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PARTIAL_LENGTH_UNIT(Int32).html

---

Unit for subset / length # 31012.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PARTIAL_LENGTH_UNIT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PARTIAL_LENGTH_UNIT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Displayed measuring unit in which the subset or length of the part is specified. Using the index, you can differentiate between 50 entries. Possible values are:

0 = As in project

1 = mm

2 = cm

3 = dm

4 = m

5 = Meter

6 = km

8 = Inch

9 = "

10 = In

11 = ft

12 = feet

13 = foot

14 = yd

15 = yard

29 = µm.
