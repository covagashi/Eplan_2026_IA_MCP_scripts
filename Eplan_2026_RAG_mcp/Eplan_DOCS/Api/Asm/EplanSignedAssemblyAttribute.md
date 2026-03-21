# EplanSignedAssemblyAttribute

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Starteru~Eplan.EplApi.Starter.EplanSignedAssemblyAttribute.html

---

EplanAssemblyAttribute is the attribute to identify an assembly used for eplan. This Attribute is required when an assembly uses an own licence.

Inheritance Hierarchy

[System.Object](#)  
   [System.Attribute](#)  
      **Eplan.EplApi.Starter.EplanSignedAssemblyAttribute**

Syntax

**C#**



[AttributeUsage(AttributeTargets.Assembly)]

public class EplanSignedAssemblyAttribute : System.Attribute

[AttributeUsage(AttributeTargets.Assembly)]

public ref class EplanSignedAssemblyAttribute : public System.Attribute

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [EplanSignedAssemblyAttribute Constructor](Eplan.EplApi.Starteru~Eplan.EplApi.Starter.EplanSignedAssemblyAttribute~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [IsEplanAssembly](Eplan.EplApi.Starteru~Eplan.EplApi.Starter.EplanSignedAssemblyAttribute~IsEplanAssembly.html) | Tells this assembly is an eplan assembly. The licence of this assembly is checked. |
| Public Property | [TypeId](#) | (Inherited from [System.Attribute](#)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Equals](#) | (Inherited from [System.Attribute](#)) |
| Public Method | [GetHashCode](#) | (Inherited from [System.Attribute](#)) |
| Public Method | [IsDefaultAttribute](#) | (Inherited from [System.Attribute](#)) |
| Public Method | [Match](#) | (Inherited from [System.Attribute](#)) |


