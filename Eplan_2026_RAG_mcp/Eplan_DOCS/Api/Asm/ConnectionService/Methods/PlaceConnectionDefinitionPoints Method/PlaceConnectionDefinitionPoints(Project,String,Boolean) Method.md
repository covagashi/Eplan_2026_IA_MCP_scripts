# PlaceConnectionDefinitionPoints(Project,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1325.html

---

Automatic optimization of nets and connections routed in them.

Syntax

**C#**



public bool OptimizeNetAutomatically( 

   IEnumerable<Connection3D> colConnections3D,

   int nMinSize,

   bool bPartiallySelected,

   bool bCloseDaisyChains

)

public:

bool OptimizeNetAutomatically( 

   IEnumerable<Connection3D^>^ colConnections3D,

   int nMinSize,

   bool bPartiallySelected,

   bool bCloseDaisyChains

)


#### Parameters

*colConnections3D*
:   Collection of 3d connections for which net optimalization will be done. Can't be null.

*nMinSize*
:   Specifies the number of connections per net that is to trigger an optimization. The minimum number is 2.

*bPartiallySelected*
:   If true then all nets included in collection completely or partially are optimized.

*bCloseDaisyChains*
:   If true then an additional connection from the first to the last connection point of the chain is generated.

#### Return Value

True if operation has been finished without problems. If false then check system messages for more information about problem.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Null was passed to as parameter or one of element in collection is `null`. |
| [System.ArgumentException](#) | One of element in collection is invalid. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when an error occurred during the optimization. Please refer to the exception message. |
