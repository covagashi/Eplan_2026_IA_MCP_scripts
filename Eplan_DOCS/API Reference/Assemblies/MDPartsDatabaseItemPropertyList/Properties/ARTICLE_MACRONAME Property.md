# ARTICLE_MACRONAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_MACRONAME().html

---

Graphical macro (without macro directory name) # 22018.

Syntax

**C#**



public MDPropertyValue ARTICLE_MACRONAME {get; set;}

public:

property MDPropertyValue^ ARTICLE_MACRONAME {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Name of the graphics macro (CAD number) for the 2D panel layout, without the directory.
