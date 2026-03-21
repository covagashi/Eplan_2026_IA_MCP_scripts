# IEplActionEnable

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionEnable.html

---

Interface to enable or disable an Action. If this interface is not used, the Action is enabled by default. If you implement this interface in an action class, you can set the respective Action to disabled. If a ribbon item points to this Action, they will be also disabled (grayed out).

Syntax

**C#**



public interface IEplActionEnable

public interface class IEplActionEnable


Example

- [c#](#i-tab-content-9c6a1874-5c34-4f04-be8c-434dd664fc15)

```
public class TestAction : Eplan.EplApi.ApplicationFramework.IEplAction, Eplan.EplApi.ApplicationFramework.IEplActionEnable

    {

        //IEplAction Members

        #region IEplActionEnable Members

        public bool Enabled(string strActionName, Eplan.EplApi.ApplicationFramework.ActionCallingContext actionContext)

        {

            if (strActionName == "TESTACTION")

            {

                return false;

            }

            else

            {

                return true;

            }

        }

        #endregion

    }
```

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [Enabled](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionEnable~Enabled.html) | One action can be enabled or disabled. Return true when it is enabled. |


