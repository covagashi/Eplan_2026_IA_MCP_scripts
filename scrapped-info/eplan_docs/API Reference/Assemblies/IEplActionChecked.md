# IEplActionChecked

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionChecked.html

---

Interface to switch the status on / off of an Action. If this interface is not used, the Action is off by default. If you implement this interface in an action class, you can set the state of the respective Action to on. If 0, unchecks; if 1, checks; and if 2, sets indeterminate.

Syntax

**C#**



public interface IEplActionChecked

public interface class IEplActionChecked


Example

- [c#](#i-tab-content-5e2ea7d3-f8d7-4514-9a1f-2e8f6bb9c13f)

```
public class TestAction : Eplan.EplApi.ApplicationFramework.IEplAction, Eplan.EplApi.ApplicationFramework.IEplActionChecked

    {

        //IEplAction Members

        \#region IEplActionChecked Members

        public int Checked(string strActionName, Eplan.EplApi.ApplicationFramework.ActionCallingContext actionContext)

        {

            if (strActionName == "TESTACTIONMIXED")

            {

                return 2;

            } 

			else if (strActionName == "TESTACTION")

            {

                return 1;

            }

            else 

            {

                return 0;

            }

        }

        \#endregion

    }
```

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [Checked](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionChecked~Checked.html) | One action can have the state on off or mixed. Return 0 for off, 1 for on, and 2 for mixed. |


