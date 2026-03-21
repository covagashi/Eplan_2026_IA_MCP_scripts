# Connection

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html

---

This class represents a connection between two [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s (two devices in the project). The following example shows how to use class Connection.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)  
      **Eplan.EplApi.DataModel.Connection**  
         [Eplan.EplApi.DataModel.E3D.Connection3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Connection3D.html)  
         [Eplan.EplApi.DataModel.Topology.RoutedConnection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.RoutedConnection.html)

Syntax

**C#**



public class Connection : StorableObject, IArticleUser, IWriteProtection

public ref class Connection : public StorableObject, IArticleUser, IWriteProtection


Remarks

Some properties of Data model classes are not linked with their owners even if from the syntax it may seem otherwise. Like in this line: oRectangle.Pen.ColorId = 5, the ColorId of the Pen is changed but oRectangle object doesn't know about it since the Pen property is a stand alone value not aware of oRectangle object existence. This remark applies to the following Connection properties: Articles, Shieldings, SubConnections, SymbolReferences, Pins.

Example

The following example shows how to use class Connection.

**C#**

```


Function oFunction = null;

foreach (Page oP in m_oTestProject.Pages)

{

    if (oP.PageType == DocumentTypeManager.DocumentType.Circuit)

    {

        foreach (Function oF in oP.Functions)

        {

            if (oF.Connections.Length > 0)

            {

                oFunction = oF;

                break;

            }

        }

    }

}

Function oStartFunc = null;

Function oEndFunc = null;

foreach (Connection oC in oFunction.Connections)

{

    oStartFunc = ((Function)oC.StartSymbolReference);

    oEndFunc = ((Function)oC.EndSymbolReference);

    Console.Out.WriteLine("StartSymbolReference: " + oStartFunc.Name);

    Console.Out.WriteLine("EndSymbolReference: " + oEndFunc.Name);

}

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Connection Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ArticleReferences](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~ArticleReferences.html) | Returns [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s that are referenced by Connection. |
| Public Property | [Articles](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~Articles.html) | Returns [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s that are referenced by Connection, and only those that are stored in project database. |
| Public Property | [CableDefinitionLine](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~CableDefinitionLine.html) | Returns [Eplan.EplApi.DataModel.EObjects.Cable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Cable.html) from a [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html) assigned to this Connection. If there are more then one [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html) assigned to this Connection, an exception is thrown. Such situation has to be handled by calling [ConnectionDefPoints](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~ConnectionDefPoints.html) and analyze of the result. |
| Public Property | [CableNameParts](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~CableNameParts.html) | Gets/Sets a cable's name to the connection. |
| Public Property | [CanHaveArticleData](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~CanHaveArticleData.html) | Check if the Connection can have [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s. |
| Public Property | [Connection3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~Connection3D.html) | Returns the [Eplan.EplApi.DataModel.E3D.Connection3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Connection3D.html) which is a 3d representation of this connection. |
| Public Property | [ConnectionDefPointProperties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~ConnectionDefPointProperties.html) | Allows to access properties of a [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html) assigned to this Connection. If there are more then one [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html) assigned to this Connection, an exception is thrown. Such situation has to be handled by calling [ConnectionDefPoints](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~ConnectionDefPoints.html) and analyze of the result. |
| Public Property | [ConnectionDefPoints](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~ConnectionDefPoints.html) | Returns the [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html) related to this connection. |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [EndIndex](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~EndIndex.html) | Index of the end function's connection point (0,1,2,...) that the connection is connected to. |
| Public Property | [EndPin](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~EndPin.html) | Returns the end [Pin](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin.html) of this connection, if such exists (i.e. if the connection is connected on the target side). Otherwise, NULL is returned. |
| Public Property | [EndSymbolConnPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~EndSymbolConnPoint.html) | Returns the [PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html) which this connection is connected to on the target side. If this connection is not connected on the target side, NULL is returned. |
| Public Property | [EndSymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~EndSymbolReference.html) | Returns the second of two [SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)s connected by this connection. |
| Public Property | [EndTargetNumber](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~EndTargetNumber.html) | Target number of end function (1,2,3...) |
| Public Property | [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~FunctionDefinition.html) | Returns the [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) of the Connection. |
| Public Property | [IsCoveredTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~IsCoveredTemplate.html) | Returns true if this is a Connection object that covers a wire's template in the cable where it belongs. |
| Public Property | [IsFixedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~IsFixedDevice.html) | Checks if device to which connection is assign is fixed or not. |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsPlaced](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~IsPlaced.html) | Returns true if the placement is placed |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsRemovable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~IsRemovable.html) | Returns true if the Connection can be removed |
| Public Property | [IsTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~IsTemplate.html) | Returns true if this is a transient Connection object representing a cable wire's template. |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [KindOfWire](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~KindOfWire.html) | Returns kind of wire. |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~Page.html) | Returns the [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) where the connection is placed on. |
| Public Property | [PotentialDefinitions](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~PotentialDefinitions.html) | Returns the [PotentialDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinition.html) related to this connection. |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~Properties.html) | .NET Property enabling access to P8 properties of the Connection object. |
| Public Property | [RepresentationType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~RepresentationType.html) | Gets/Sets connection's representation type. |
| Public Property | [Shieldings](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~Shieldings.html) | Returns the Shielding objects the connection is composed of. It does not return Shielding objects the connection is shielded by. |
| Public Property | [StartIndex](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~StartIndex.html) | Index of the start function's connection point (0,1,2,...) that the connection is connected to. |
| Public Property | [StartPin](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~StartPin.html) | Returns the start [Pin](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin.html) of this connection, if such exists (i.e. if the connection is connected on the source side). Otherwise, NULL is returned. |
| Public Property | [StartSymbolConnPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~StartSymbolConnPoint.html) | Returns the [PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html) which this connection is connected to on the source side. If this connection is not connected on the source side, NULL is returned. |
| Public Property | [StartSymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~StartSymbolReference.html) | Returns the first of two [SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)s connected by this connection. |
| Public Property | [StartTargetNumber](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~StartTargetNumber.html) | Target number of start function (1,2,3...) |
| Public Property | [SubConnections](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~SubConnections.html) | If connection contains interruption points, this method returns an array of partial connections which current connection consists of For a "net connection" this method will return an empty array. |
| Public Property | [SymbolReferences](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~SymbolReferences.html) | This method returns an array of SymbolReferences objects that belong to a connection . This may for example be T-pieces or corners. Also beginning and end are returned. |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [WriteProtected](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~WriteProtected.html) | Check if object is currently write protected or sets Manual write protection |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~AddArticleReference.html) | Overloaded. Adds a new [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) to the Connection. Returns the added [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html). |
| Public Method | [Assign](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~Assign.html) | Assigns this connection to another, which means that values of this connection's properties are copied to the target connection and the source connection itself is removed from the project. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of Connection object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetWriteProtectionFlagSet](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~GetWriteProtectionFlagSet.html) | Checks if a specific write protection kind was set. |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [MakePersistent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~MakePersistent.html) | Allows to create non-placed connection from a connection template. In effect connection template becomes covered template. |
| Public Method | [PauseWriteProtection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~PauseWriteProtection.html) | Temporarily disables write protection. Note that current write protection flags are not cleared. |
| Public Method | [PlaceAsConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~PlaceAsConnectionDefinitionPoint.html) | Places this connection as a connection def. point on the given schematic page and in the given location. If this is an uncovered connection template and the location points to a connection line on schematic page, the template automatically becomes covered (i.e. connection is created in the project) Note: When uncovered connection template becomes covered, connections on the page are updated which may affect performance. If this method needs to be called repeatedly, use the [DisableConnectionUpdateStep](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DisableConnectionUpdateStep.html) object to make the performance better. |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~Remove.html) | Removes the connection from the [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html). |
| Public Method | [RemoveArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~RemoveArticleReference.html) | Removes the ArticleReference from the Connecttion |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |


