# DeclareAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.Scripting.DeclareAction.html

---

Attribute used to mark a method of a class in a [script](Scripts.html) so that this method will be registered as an **Action:Eplan::EplApi::ApplicationFramework:** in the system.  
If a method marked by the DeclareAction attribute has string parameters, these parameters will be recognized as parameters of the Action.

Inheritance Hierarchy

[System.Object](#)  
   [System.Attribute](#)  
      **Eplan.EplApi.Scripting.DeclareAction**

Syntax

**C#**



[AttributeUsage(AttributeTargets.Method)]

public class DeclareAction : System.Attribute

[AttributeUsage(AttributeTargets.Method)]

public ref class DeclareAction : public System.Attribute

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [DeclareAction Constructor](Eplan.EplApi.AFu~Eplan.EplApi.Scripting.DeclareAction~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Name](Eplan.EplApi.AFu~Eplan.EplApi.Scripting.DeclareAction~Name.html) | Name of the action. |
| Public Property | [Ordinal](Eplan.EplApi.AFu~Eplan.EplApi.Scripting.DeclareAction~Ordinal.html) | Overload level of the action. |
| Public Property | [TypeId](#) | (Inherited from [System.Attribute](#)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Equals](#) | (Inherited from [System.Attribute](#)) |
| Public Method | [GetHashCode](#) | (Inherited from [System.Attribute](#)) |
| Public Method | [IsDefaultAttribute](#) | (Inherited from [System.Attribute](#)) |
| Public Method | [Match](#) | (Inherited from [System.Attribute](#)) |


