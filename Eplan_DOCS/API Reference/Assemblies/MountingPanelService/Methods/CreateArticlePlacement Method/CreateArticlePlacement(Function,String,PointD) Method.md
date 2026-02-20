# CreateArticlePlacement(Function,String,PointD) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.MountingPanelService~CreateArticlePlacement(Function,String,PointD).html

---

Produces an article placement on the mounting panel. The article must be in the project's database.

Syntax

**C#**



public void CreateArticlePlacement( 

   Function oMountingPanel,

   string strPartNumber,

   PointD pLocation

)

public:

void CreateArticlePlacement( 

   Function^ oMountingPanel,

   String^ strPartNumber,

   PointD pLocation

)


#### Parameters

*oMountingPanel*
:   mounting panel

*strPartNumber*
:   part number

*pLocation*
:   location

Remarks

By default, variant A of the macro specified for the article is inserted. In case the variant doesn't exist in the macro, a BaseException is thrown. Position of created placement is influenced by part placement handle string setting ("USER.PanelLayoutGui.Settings.Gripper"). If "USER.PanelLayoutGui.Settings.Gripper" is set to "UpperLeft" value then created placement will be positioned exactly at point passed in pLocation parameter.

Example

- [c#](#i-tab-content-713452ad-0526-4482-901a-ead0221901bf)

```
new Settings().SetStringSetting("USER.PanelLayoutGui.Settings.Gripper", "UpperLeft");

//Note: The article must have width and height specified (the values must be greater than zero).
```
