# EvaluateName Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~EvaluateName.html

---

Method evaluates the full name for a Function3D by using the visible device tag of that Function3D and building the full name by graphical search on the installation space where the Function3D is placed.

Syntax

**C#**



public UniversalPropertyList EvaluateName( 

   IFunctionBase pFunctionBase

)

public:

UniversalPropertyList^ EvaluateName( 

   IFunctionBase^ pFunctionBase

)


#### Parameters

*pFunctionBase*
:   Function3D for which is evaluated name.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
