# TextBase.FontInfo Constructor(Int32,Boolean,Boolean,Boolean,Boolean)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic713.html

---

Constructor which creates new Font object.

Syntax

**C#**



public TextBase.FontInfo( 

   int font_index,

   bool bold,

   bool italic,

   bool underline,

   bool strikeout

)

public:

TextBase.FontInfo( 

   int font_index,

   bool bold,

   bool italic,

   bool underline,

   bool strikeout

)


#### Parameters

*font\_index*
:   Index of the font in font table. Please see Index member.

*bold*


*italic*


*underline*


*strikeout*

Remarks

Font family is represented by font index. P8 has font table with 10 predefined fonts. These fonts names can be changed in string settings: COMPANY.GedViewer.Fonts.Val with index 0 to 9.
