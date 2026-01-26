# CollectConnections Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.TopologyService~CollectConnections.html

---

Finds or creates topology connections for given elements.

Syntax

**C#**



public RoutedConnection[] CollectConnections( 

   Project pProject,

   ICollection<StorableObject> colObjects

)

public:

array<RoutedConnection^>^ CollectConnections( 

   Project^ pProject,

   ICollection<StorableObject^>^ colObjects

)


#### Parameters

*pProject*
:   [Eplan.EplApi.DataModel.Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) for which connections will be found and create.

*colObjects*
:   Collection of regular connections and functions for which topology connections will be found. Can't be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | If any parameter is `null`. |
| [System.ArgumentException](#) | If any parameter is invalid. |
| [System.ApplicationException](#) | Failed to find connections. Please refer to the error message. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An internal error occurred during finding or creating the connections. Please refer to the error message. |
