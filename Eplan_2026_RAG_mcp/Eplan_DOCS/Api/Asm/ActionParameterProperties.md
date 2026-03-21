# ActionParameterProperties

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionParameterProperties.html

---

Description of a parameter that can be passed to an ActionCallingContext. This class only serves for documentation purposes.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.ApplicationFramework.ActionParameterProperties**

Syntax

**C#**



public class ActionParameterProperties

public ref class ActionParameterProperties


Example

Example of listing action parameters

**C#**

```
ActionManager actionManager = new ActionManager();

EplApi.ApplicationFramework.Action foundAction = actionManager.FindAction("ActionExample");

ArrayList listOfParameterProperties = foundAction.ActionProperties.GetParameterProperties();

if (listOfParameterProperties.Count > 0)

{

    foreach (ActionParameterProperties parameterProperty in listOfParameterProperties)

    {

        string strParamName = parameterProperty.Name;

        Debug.WriteLine(strParamName);

    }

}

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [ActionParameterProperties Constructor](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionParameterProperties~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Name](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionParameterProperties~Name.html) | Name of a parameter. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionParameterProperties~Dispose().html) | Destructor for deterministic finalization of ActionParameterProperties object. |
| Public Method | [GetAfActionParameter](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionParameterProperties~GetAfActionParameter.html) | For internal use only. |
| Public Method | [Set](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionParameterProperties~Set.html) | Description text of a parameter. Sets name and description text of a parameter. |


