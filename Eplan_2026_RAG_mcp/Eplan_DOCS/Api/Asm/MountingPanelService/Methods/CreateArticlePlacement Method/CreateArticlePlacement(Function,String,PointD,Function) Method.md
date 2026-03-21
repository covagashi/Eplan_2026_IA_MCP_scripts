# CreateArticlePlacement(Function,String,PointD,Function) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1386.html

---

Produces an article placement on the mounting panel. The article must be in the project's database.

Syntax

**C#**



public void CreateArticlePlacement( 

   Function oMountingPanel,

   string strPartNumber,

   PointD pLocation,

   ref Function oArticlePlacement

)

public:

void CreateArticlePlacement( 

   Function^ oMountingPanel,

   String^ strPartNumber,

   PointD pLocation,

   Function^% oArticlePlacement

)


#### Parameters

*oMountingPanel*
:   mounting panel

*strPartNumber*
:   part number

*pLocation*
:   location

*oArticlePlacement*
:   created article placement

Remarks

By default, variant A of the macro specified for the article is inserted. In case the variant doesn't exist in the macro, a BaseException is thrown. Position of created placement is influenced by part placement handle string setting ("USER.PanelLayoutGui.Settings.Gripper"). If "USER.PanelLayoutGui.Settings.Gripper" is set to "UpperLeft" value then created placement will be positioned exactly at point passed in pLocation parameter.

Example

- [c#](#i-tab-content-52c2a05f-4e40-4ab9-abc7-45d6b5d213f0)

```
new Settings().SetStringSetting("USER.PanelLayoutGui.Settings.Gripper", "UpperLeft");

//Note: The article must have width and height specified (the values must be greater than zero).
```
