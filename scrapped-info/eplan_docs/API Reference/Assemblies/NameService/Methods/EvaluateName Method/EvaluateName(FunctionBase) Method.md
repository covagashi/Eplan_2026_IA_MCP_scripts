# EvaluateName(FunctionBase) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~EvaluateName(FunctionBase).html

---

Method evaluates the full name for a FunctionBase (which is either a Function or a Location box or an Interruption-point) by using the visible device tag of that FunctionBase and building the full name by graphical search on the page where the FunctionBase is placed. For example if in the visible name of the FunctionBase some project structures (as (for example) the plant) are missing, but this project structure is necessary to build the full device tag, then the method does a search on the page for LocationBoxes that are surrounding the FunctionBase. If such a LocationBox has been found, then the project structures missing in the visible name of the FunctionBase will be taken over. If no LocationBox is found, the project structures missing in the visible name of the FunctionBase will be taken over from the Page-Object where the FunctionBase is placed. For an empty visible name the full name is taken from a function in search direction or from a surrounding device box. Nesting of device tags is made by using an surrounding device box, if nesting is enabled. The parameters used for evaluation are defined in the dialog with the project properties.

Syntax

**C#**



public UniversalPropertyList EvaluateName( 

   FunctionBase pFunctionBase

)

public:

UniversalPropertyList^ EvaluateName( 

   FunctionBase^ pFunctionBase

)


#### Parameters

*pFunctionBase*
:   Function for which is evaluated name.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | When page is not set. |
