# API DataModel

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/API_DataModel.html

---

The electrotechnical data model (Eplan.EplApi.DataModel  namespace) contains all the classes / objects belonging to an Eplan project, such as the project itself, pages, functions, placements, etc. Each class is derived from the  StorableObject  base class and has its specific properties. In contrast to the Eplan 21 data model, Eplan does not strictly differentiate between the graphical and the logical information. For example, a page keeps record of both the functions (logical) and the placements (graphical). There is **no** device object that stores the functions with the same device tag.

**Note**

The class  Function  is named like a keyword of Visual Basic. In order to get no compilation errors in VB, you need to always refer to a  Function  object by its complete name space:  Eplan.EplApi.DataModel.Function  or in square brackets:  [Function].

We recommend you to explicitly release data model objects when they are no longer needed. This is especially true for loops that set a large number of properties. Make sure that the garbage collector has the opportunity to clean up these objects by frequently calling  System.GC.WaitForPendingFinalizers().

Please take into account that generally data model objects store length values in millimeters and dimensions are according to graphical coordinate system.
