# IsNotUsedAnymore Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition~IsNotUsedAnymore.html

---

Determines whether the segment definition in the project is write-protected.

Syntax

**C#**



public bool IsNotUsedAnymore {get; set;}

public:

property bool IsNotUsedAnymore {

   bool get();

   void set (    bool value);

}


Remarks

When compressing the project, such segment definitions can be deleted if they are not used in the project.
