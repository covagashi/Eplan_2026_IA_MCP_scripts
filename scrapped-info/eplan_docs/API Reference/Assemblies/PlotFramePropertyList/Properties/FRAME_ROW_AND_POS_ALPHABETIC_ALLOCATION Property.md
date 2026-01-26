# FRAME_ROW_AND_POS_ALPHABETIC_ALLOCATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic738.html

---

Alphabetical column / row distribution # 12010.

Syntax

**C#**



public PropertyValue FRAME_ROW_AND_POS_ALPHABETIC_ALLOCATION {get; set;}

public:

property PropertyValue^ FRAME_ROW_AND_POS_ALPHABETIC_ALLOCATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Sequence of characters used for implementation of column and row numbers in strings. The entry '0123456789ABCDEF', for instance, results in hexadecimal column designations.
