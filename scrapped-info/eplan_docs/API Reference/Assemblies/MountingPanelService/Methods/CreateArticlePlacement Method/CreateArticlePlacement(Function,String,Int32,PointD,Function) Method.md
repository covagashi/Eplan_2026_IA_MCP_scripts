# CreateArticlePlacement(Function,String,Int32,PointD,Function) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1385.html

---

Produces an article placement on the mounting panel. The article must be in the project's database.

Syntax

**C#**



public void CreateArticlePlacement( 

   Function oMountingPanel,

   string strPartNumber,

   int macroVariant,

   PointD pLocation,

   ref Function oArticlePlacement

)

public:

void CreateArticlePlacement( 

   Function^ oMountingPanel,

   String^ strPartNumber,

   int macroVariant,

   PointD pLocation,

   Function^% oArticlePlacement

)


#### Parameters

*oMountingPanel*
:   mounting panel

*strPartNumber*
:   part number

*macroVariant*
:   variant of the article's macro to insert (0 - variant A, 1 - variant B, etc.)

*pLocation*
:   location

*oArticlePlacement*
:   created article placement

Remarks

In case the specified macro variant doesn't exist, a BaseException is thrown. Position of created placement is influenced by part placement handle string setting ("USER.PanelLayoutGui.Settings.Gripper"). If "USER.PanelLayoutGui.Settings.Gripper" is set to "UpperLeft" value then created placement will be positioned exactly at point passed in pLocation parameter.

Example

- [c#](#i-tab-content-712b3dd2-f734-4dc0-a63f-269eb6ca4785)

```
new Settings().SetStringSetting("USER.PanelLayoutGui.Settings.Gripper", "UpperLeft");

//Note: The article must have width and height specified (the values must be greater than zero).
```
