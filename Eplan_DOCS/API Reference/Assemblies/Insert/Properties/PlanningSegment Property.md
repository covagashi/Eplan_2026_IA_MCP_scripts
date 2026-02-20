# PlanningSegment Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~PlanningSegment.html

---

Determines the planning segment to which all function inserted from window macro on page will be assign.

Syntax

**C#**



public PlanningSegment PlanningSegment {get; set;}

public:

property PlanningSegment^ PlanningSegment {

   PlanningSegment^ get();

   void set (    PlanningSegment^ value);

}


Example

**C#**

```
//create insert service

Insert oInsert = new Insert();

//set planning segment to which functions from macro will be assigned

oInsert.PlanningSegment = oPlanningSegment;

//insert a window macro

StorableObject [] arrInsertedSorableObjects = oInsert.WindowMacro(

    strPath,

    iVariant,

    oSchematicPage,

    oLocation,

    Insert.MoveKind.Absolute);

//get first inserted function 

Function oInsertedFunction = arrInsertedSorableObjects.OfType<Function>().FirstOrDefault();

```
