# ARTICLE_PARTIAL_LENGTH_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLE_PARTIAL_LENGTH_UNIT().html

---

Unit for subset / length # 20498.

Syntax

**C#**



public PropertyValue ARTICLE_PARTIAL_LENGTH_UNIT {get; set;}

public:

property PropertyValue^ ARTICLE_PARTIAL_LENGTH_UNIT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Displayed measuring unit in which the subset or length of the part is specified. Possible values are:

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
