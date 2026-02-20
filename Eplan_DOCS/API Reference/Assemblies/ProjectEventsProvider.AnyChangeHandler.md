# ProjectEventsProvider.AnyChangeHandler

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectEventsProvider+AnyChangeHandler.html

---

Is called when something has changed in any project.

Syntax

**C#**



public delegate void ProjectEventsProvider.AnyChangeHandler( 

   StorableObject[] createdObjects,

   StorableObject[] changedObjects,

   string[] destroyedObjects

)

public delegate void ProjectEventsProvider.AnyChangeHandler( 

   array<StorableObject^>^ createdObjects,

   array<StorableObject^>^ changedObjects,

   array<String^>^ destroyedObjects

)


#### Parameters

*createdObjects*
:   List of created objects.

*changedObjects*
:   List of changed objects.

*destroyedObjects*
:   Database ids list of objects which were destroyed.
