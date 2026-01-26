# ProjectEventsProvider

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectEventsProvider.html

---

This class provides notifications about project changes.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.ProjectEventsProvider**

Syntax

**C#**



public sealed class ProjectEventsProvider

public ref class ProjectEventsProvider sealed


Remarks

`ProjectEventsProvider` tracks changes made only by current instance of P8. When making changes, please use Eplan.EplApi.HEServices.ChangeInfoService in order to disable notification and avoid infinite recursion.

Example

The following example shows how to use class `ProjectEventsProvider`.

**C#**

```
public class EventListener : IDisposable

{

    public EventListener()

    {

        oProjectEventsProvider.AddAnyChangeHandler(

            AnyChangeEvent_Handler);

    }

    public void Dispose()

    {

        oProjectEventsProvider.RemoveAnyChangeHandler(

            AnyChangeEvent_Handler);

    }

    public void AnyChangeEvent_Handler(StorableObject[] createdObjects, StorableObject[] changedObjects, String[] destroyedObjects)

    {

        foreach (StorableObject oStorableObject in createdObjects)

        {

            if (oStorableObject is Function)

            {

                Function oFunction = oStorableObject as Function;

                System.Console.WriteLine("Function created : " + oFunction.Name);

            }

        }

    }

    private ProjectEventsProvider oProjectEventsProvider = new ProjectEventsProvider();

}

EventListener oEventListener = new EventListener();

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [ProjectEventsProvider Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectEventsProvider~_ctor.html) | Constructor |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddAnyChangeHandler](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectEventsProvider~AddAnyChangeHandler.html) | Adds project events handler. |
| Public Method | [AddPreRemoveHandler](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectEventsProvider~AddPreRemoveHandler.html) | Adds pre remove events handler. |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectEventsProvider~Dispose().html) | Destructor for deterministic finalization of ProjectEventsProvider object. |
| Public Method | [RemoveAnyChangeHandler](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectEventsProvider~RemoveAnyChangeHandler.html) | Removes project events handler. |
| Public Method | [RemovePreRemoveHandler](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectEventsProvider~RemovePreRemoveHandler.html) | Removes pre remove events handler. |


