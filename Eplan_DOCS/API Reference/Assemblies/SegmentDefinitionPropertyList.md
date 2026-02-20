# SegmentDefinitionPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinitionPropertyList.html

---

This class represents a collection of properties of [SegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html) class. Please also check the base classes for other properties that are available for [SegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html) objects: [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         **Eplan.EplApi.DataModel.Planning.SegmentDefinitionPropertyList**

Syntax

**C#**



[DefaultMember("Property")]

public class SegmentDefinitionPropertyList : Eplan.EplApi.DataModel.StorableObjectPropertyList

[DefaultMember("Property")]

public ref class SegmentDefinitionPropertyList : public Eplan.EplApi.DataModel.StorableObjectPropertyList


Remarks

It uses the [] operator in order to access its elements (stored properties).

Property list is a container for property values and just like them can be `persistent` (also called `online`) or `transient` (also called `offline`). If a property list is `persistent`, this means that it is associated with the properties of some StorableObject or other property list. If any property is added, changed or removed from the property list in this case, the result is also visible in the related objects. Whether a property list is `persistent` or `transient` is determined at the time of its creation and cannot be changed.

Example

This example shows the different usage of persistent property lists and transient property lists:

**C#**

```
// Creation of a persistent property list

FunctionPropertyList oPersistentPropertyList1 = oFunction.Properties;

oPersistentPropertyList1.FUNC_COMMENT = "Comment";

// Now, oFunction.Properties.FUNC_COMMENT is equals "Comment"

FunctionPropertyList oPersistentPropertyList2 = new FunctionPropertyList(oFunction);

oPersistentPropertyList2.FUNC_COMMENT = "Test";

// Now, oFunction.Properties.FUNC_COMMENT equals "Test"

// Creation of a transient property list

FunctionPropertyList oTransientPropertyList = new FunctionPropertyList();

oTransientPropertyList.FUNC_COMMENT = "Test comment";

oFunction.Properties.FUNC_COMMENT = oTransientPropertyList.FUNC_COMMENT;

oTransientPropertyList.FUNC_COMMENT = "Transient comment";

// Now, oTransientPropertyList.FUNC_COMMENT equals "Test comment"

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [SegmentDefinitionPropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinitionPropertyList~_ctor().html) | Constructor |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [DMPLAOBJECTDEFINITION\_BEGINWITHPREFIX](topic1065.html) | Segment definition: Preceding sign also at the beginning # 44046. |
| Public Property | [DMPLAOBJECTDEFINITION\_DISPLAYNAME\_FORMAT](topic1066.html) | Display format: Segment name # 44002. |
| Public Property | [DMPLAOBJECTDEFINITION\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinitionPropertyList~DMPLAOBJECTDEFINITION_NAME().html) | Segment definition: Displayed name # 44003. |
| Public Property | [DMPLAOBJECTDEFINITION\_NO\_STRUCTUREDELIMITER](topic1067.html) | Structure identifiers without separators # 44033. |
| Public Property | [DMPLAOBJECTDEFINITION\_NUMBER\_NO\_SPACE](topic1068.html) | Segment definition: No blank space before the number # 44091. |
| Public Property | [DMPLAOBJECTDEFINITION\_PREFIX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinitionPropertyList~DMPLAOBJECTDEFINITION_PREFIX().html) | Segment definition: Preceding sign # 44045. |
| Public Property | [DMPLAOBJECTDEFINITION\_PREFIX\_SA](topic1069.html) | Segment definition: Separator symbolic address # 44090. |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [FUNC\_BLOCK\_FORMAT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinitionPropertyList~FUNC_BLOCK_FORMAT(Int32).html) | Block property: Format # 20202. |
| Public Property | [FUNC\_CRAFT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinitionPropertyList~FUNC_CRAFT().html) | Trade # 20466. |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinitionPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |
| Public Property | [WRITEPROTECTED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinitionPropertyList~WRITEPROTECTED().html) | Change protection # 3014. |
| Public Property | [WRITEPROTECTED\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinitionPropertyList~WRITEPROTECTED_AUTOMATIC().html) | Change protection (hierarchical) # 3015. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of SegmentDefinitionPropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinitionPropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |


