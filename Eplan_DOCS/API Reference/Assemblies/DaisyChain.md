# DaisyChain

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DaisyChain.html

---

Represents daisy chain object of a net definition point.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)  
      **Eplan.EplApi.DataModel.DaisyChain**

Syntax

**C#**



public class DaisyChain : StorableObject

public ref class DaisyChain : public StorableObject


Example

The following example shows how to create, modify and remove daisy chains.

**C#**

```
//create new DaisyChain

DaisyChain newDaisyChain = netDefinitionPoint.AddDaisyChain(

    new[]{

        netDefinitionPoint.NetConnectionPoints[0],

        netDefinitionPoint.NetConnectionPoints[2],

        netDefinitionPoint.NetConnectionPoints[3]

    });

//list connection points of a DaisyChain

foreach (var connectionPoint in newDaisyChain.NetbasedWiringIds)

    Console.WriteLine(connectionPoint);    // will output IDs of netDefinitionPoint.NetConnectionPoints[0],

                                           // netDefinitionPoint.NetConnectionPoints[2],

                                           // netDefinitionPoint.NetConnectionPoints[3]

//list connections of a DaisyChain

foreach (var connection in newDaisyChain.Connections)

    Console.WriteLine(connection.Properties.CONNECTION_SOURCE + " <=> " + connection.Properties.CONNECTION_DESTINATION);

// will output 2 connections :

// netDefinitionPoint.NetConnectionPoints[0] <=> netDefinitionPoint.NetConnectionPoints[2]

// netDefinitionPoint.NetConnectionPoints[2] <=> netDefinitionPoint.NetConnectionPoints[3]

newDaisyChain.AddConnectionPoint(netDefinitionPoint.NetConnectionPoints[1], 1);

//list of net based wiring ids of a DaisyChain

foreach (var connectionPoint in newDaisyChain.NetbasedWiringIds)

    Console.WriteLine(connectionPoint);    // will output IDs of netDefinitionPoint.NetConnectionPoints[0],

                                           // netDefinitionPoint.NetConnectionPoints[1]

                                           // netDefinitionPoint.NetConnectionPoints[2]

                                           // , netDefinitionPoint.NetConnectionPoints[3]

                                           //list connection points of a DaisyChain

foreach (var connectionPoint in newDaisyChain.ConnectionPoints)

    Console.WriteLine(connectionPoint);    // will output connection points netDefinitionPoint.NetConnectionPoints[0],

                                           // netDefinitionPoint.NetConnectionPoints[1]

                                           // netDefinitionPoint.NetConnectionPoints[2]

                                           // , netDefinitionPoint.NetConnectionPoints[3]

//list connections of a DaisyChain

foreach (var connection in newDaisyChain.Connections)

    Console.WriteLine(connection.Properties.CONNECTION_SOURCE + " <=> " + connection.Properties.CONNECTION_DESTINATION);

// will output 3 connections :

// netDefinitionPoint.NetConnectionPoints[0] <=> netDefinitionPoint.NetConnectionPoints[1]

// netDefinitionPoint.NetConnectionPoints[1] <=> netDefinitionPoint.NetConnectionPoints[2]

// netDefinitionPoint.NetConnectionPoints[2] <=> netDefinitionPoint.NetConnectionPoints[3]

//remove DaisyChain

netDefinitionPoint.RemoveDaisyChain(newDaisyChain);

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [DaisyChain Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DaisyChain~_ctor().html) | Default constructor. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ConnectionPoints](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DaisyChain~ConnectionPoints.html) | Returns connection points belonging to the current daisy chain |
| Public Property | [Connections](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DaisyChain~Connections.html) | Returns connections |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [NetbasedWiringIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DaisyChain~NetbasedWiringIds.html) | Returns net-based Ids |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DaisyChain~Properties.html) | EPLAN properties of the DaisyChain object. |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddConnectionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DaisyChain~AddConnectionPoint.html) | Overloaded. Adds a new net connection point and creates connection |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of DaisyChain object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [RemoveConnectionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DaisyChain~RemoveConnectionPoint.html) | Removes a net connection point and connection |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |


