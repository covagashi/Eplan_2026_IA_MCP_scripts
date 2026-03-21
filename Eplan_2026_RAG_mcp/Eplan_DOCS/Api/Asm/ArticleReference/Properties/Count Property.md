# Count Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~Count.html

---

Sets and gets count

Syntax

**C#**



public int Count {get; set;}

public:

property int Count {

   int get();

   void set (    int value);

}


Remarks

For 2D Functions of category ArticlePlacement value higher than "1" will be ignored and adjusted to "1".
