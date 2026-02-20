# Edit

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit.html

---

Class to open pages in the graphics editor for editing.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.Edit**

Syntax

**C#**



public class Edit

public ref class Edit

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Edit Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~_ctor.html) | Default constructor |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [BringToFront](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~BringToFront.html) | Opens the page, selects the Placement passed as oPlacementToMove and move the Placement front. |
| Public Method | [ClearSelection](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~ClearSelection.html) | Removes selection from all objects in the GED. |
| Public Method | [ClosePage](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~ClosePage.html) | closes a page and the associated GEDs |
| Public Method | [CutOff](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~CutOff.html) | Overloaded. Cut off given object at a given position. Page with object needs to be the currently opened page in graphical editor. |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~Dispose().html) | Destructor |
| Public Method | [FitTextsInAlignmentBoxes](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~FitTextsInAlignmentBoxes.html) | Fit the text in Alignement Boxes |
| Public Method | [Mirror](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~Mirror.html) | Overloaded. Mirrors placements |
| Public Method | [OpenPageWithDeviceName](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~OpenPageWithDeviceName.html) | Opens the page which contains a given function. The function is selected in the graphic editor. |
| Public Method | [OpenPageWithName](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~OpenPageWithName.html) | Opens the page with the name passed to strPageName. |
| Public Method | [OpenPageWithNameAndDeviceName](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~OpenPageWithNameAndDeviceName.html) | Opens the page with the name passed to strPageName and select the function whose name passed to strDeviceName. The function is selected in the graphic editor. If no function with name strDeviceName was found on the page, so no element will be selected. But the page will be still opened. |
| Public Method | [OpenPageWithNameAndFunctionName](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~OpenPageWithNameAndFunctionName.html) | Opens the page which contains a given function. The function is selected in the graphic editor. |
| Public Method | [OpenPageWithNameAndXYCoords](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~OpenPageWithNameAndXYCoords.html) | Opens the page with the name passed to strPageName and sets the cursor to the position defined by the X and Y coordinates. |
| Public Method | [OpenPageWithPlacement](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~OpenPageWithPlacement.html) | Opens the page and selects the Placement passed as oPlacementToSelect. The Placement is selected in the graphic editor. |
| Public Method | [RedrawGed](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~RedrawGed.html) | Redraws GED surface. |
| Public Method | [Rotate](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~Rotate.html) | Rotates objects. |
| Public Method | [SelectObjects](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~SelectObjects.html) | Selects objects in GED |
| Public Method | [SelectProjectInPagesNavigator](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~SelectProjectInPagesNavigator.html) | Selects the project in pages navigator |
| Public Method | [SendToBack](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~SendToBack.html) | Opens the page, selects the Placement passed as oPlacementToMove and move the Placement back. |
| Public Method | [SetFocusToGED](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~SetFocusToGED.html) | Sets focus to GED frame. |
| Public Method | [SynchronizeObjectsToNavigators](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~SynchronizeObjectsToNavigators.html) | Synchronize objects selected in GUI navigators. Groups will not be resolved, each object of a group must be given in parameter. |


