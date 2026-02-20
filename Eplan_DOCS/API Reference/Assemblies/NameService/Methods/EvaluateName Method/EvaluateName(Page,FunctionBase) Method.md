# EvaluateName(Page,FunctionBase) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~EvaluateName(Page,FunctionBase).html

---

Sets the page and evaluates the full name for a FunctionBase (which is either a Function or a Location box or an Interruption-point) by using the visible device tag of that FunctionBase and building the full name by graphical search on the page where the FunctionBase is placed. In the visible name missing project structures, which for example are supplemented from surrounding LocationBoxes or from the Page-Object itself. For an empty visible name the full name is taken from a function in search direction or from a surrounding device box. Nesting of device tags is made by using an surrounding device box, if nesting is enabled. The parameters used for evaluation are defined in the dialog with the project properties.

Syntax

**C#**



public UniversalPropertyList EvaluateName( 

   Page pPage,

   FunctionBase pFunctionBase

)

public:

UniversalPropertyList^ EvaluateName( 

   Page^ pPage,

   FunctionBase^ pFunctionBase

)


#### Parameters

*pPage*
:   Page to set.

*pFunctionBase*
:   Function for which is evaluated name.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
