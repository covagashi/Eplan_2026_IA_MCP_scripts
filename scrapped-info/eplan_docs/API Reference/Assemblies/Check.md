# Check

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check.html

---

Class for checking projects or pages.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.Check**

Syntax

**C#**



public class Check

public ref class Check


Example

The following examples shows how to use class Check.

**C#**

```
Check oCheck = new Check();

oCheck.VerifyProject(m_oTestProject);

```

**C#**

```
Check oCheck = new Check();

oCheck.VerifyPages(new ArrayList(m_oTestProject.Pages));

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Check Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~_ctor.html) | Default constructor |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~Dispose().html) | Destructor |
| Public Method | [VerifyInstallationSpace](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyInstallationSpace.html) | Overloaded. Starts a check run for the given installation spaces. |
| Public Method | [VerifyMDPartsDatabaseItems](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyMDPartsDatabaseItems.html) | Overloaded. Starts a check run for the given MDPartsDatabaseItems (MDParts). |
| Public Method | [VerifyPages](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyPages.html) | Overloaded. Starts a check run for the given pages. |
| Public Method | [VerifyProject](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyProject.html) | Overloaded. Starts a check run for the given project. |


