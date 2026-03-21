# MacroRepresentationType Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~MacroRepresentationType.html

---

Page's property describing type of macro. This type is used to find a suitable variant of macro, which can be insert on this page. While inserting macro on page, inserting variant of macro is get from page's MacroRepresentationType and variant of macro defined by user. This property depends on property PageType.

Syntax

**C#**



public WindowMacro.Enums.RepresentationType MacroRepresentationType {get;}

public:

property WindowMacro.Enums.RepresentationType MacroRepresentationType {

   WindowMacro.Enums.RepresentationType get();

}


#### Property Value

RepresentationType : enum type with available types of macro
