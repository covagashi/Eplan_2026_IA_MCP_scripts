# GraphicalPlacementPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacementPropertyList.html

---

This class represents collection of properties of [GraphicalPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement.html) class. Please check also base classes for other properties which are available for [GraphicalPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement.html) objects: [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html), [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)  
            **Eplan.EplApi.DataModel.Graphics.GraphicalPlacementPropertyList**  
               [Eplan.EplApi.DataModel.Graphics.ArcPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ArcPropertyList.html)  
               [Eplan.EplApi.DataModel.Graphics.DimensionCirclePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionCirclePropertyList.html)  
               [Eplan.EplApi.DataModel.Graphics.DimensionItemPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItemPropertyList.html)  
               [Eplan.EplApi.DataModel.Graphics.LinePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.LinePropertyList.html)  
               [Eplan.EplApi.DataModel.Graphics.PlaceHolderPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolderPropertyList.html)  
               [Eplan.EplApi.DataModel.Graphics.PolyLinePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PolyLinePropertyList.html)  
               [Eplan.EplApi.DataModel.Graphics.RectanglePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.RectanglePropertyList.html)  
               [Eplan.EplApi.DataModel.Graphics.ShieldingPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ShieldingPropertyList.html)  
               [Eplan.EplApi.DataModel.Graphics.TextBasePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.TextBasePropertyList.html)

Syntax

**C#**



[DefaultMember("Property")]

public class GraphicalPlacementPropertyList : Eplan.EplApi.DataModel.PlacementPropertyList

[DefaultMember("Property")]

public ref class GraphicalPlacementPropertyList : public Eplan.EplApi.DataModel.PlacementPropertyList


Remarks

It uses operator[] in order to access its elements (stored properties).

Property list is a container for property values and just like them can be `online` or `offline`. If property list is `online` it means that is associated with properties of some StorableObject or other property list. In this case if any property is added, changed or removed from property list the result is also visible in related objects. Whether property list is online or offline is being determine in time of it's creation and can not be changed.

Example

Example shows usage of online an offline property list:

**C#**

```
// creation of persistent property list

FunctionPropertyList oPersistentPropertyList1 = oFunction.Properties;

oPersistentPropertyList1.FUNC_COMMENT = "Comment";

// now oFunction.Properties.FUNC_COMMENT is equal "Comment"

FunctionPropertyList oPersistentPropertyList2 = new FunctionPropertyList(oFunction);

oPersistentPropertyList2.FUNC_COMMENT = "Test";

// now oFunction.Properties.FUNC_COMMENT is equal "Test"

// creation of transient property list

FunctionPropertyList oTransientPropertyList = new FunctionPropertyList();

oTransientPropertyList.FUNC_COMMENT = "Test comment";

oFunction.Properties.FUNC_COMMENT = oTransientPropertyList.FUNC_COMMENT;

oTransientPropertyList.FUNC_COMMENT = "Transient comment";

// now oTransientPropertyList.FUNC_COMMENT is equal "Test comment"

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [GraphicalPlacementPropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacementPropertyList~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [INSTANCE\_COLOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacementPropertyList~INSTANCE_COLOR().html) | Color # 19010. |
| Public Property | [INSTANCE\_FULLPLACEMENTLOCATION](topic709.html) | Placement # 19007. |
| Public Property | [INSTANCE\_GEDLOCATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacementPropertyList~INSTANCE_GEDLOCATION().html) | Graphical placement # 19103. |
| Public Property | [INSTANCE\_INVISIBLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacementPropertyList~INSTANCE_INVISIBLE().html) | Invisible # 19101. |
| Public Property | [INSTANCE\_LAYER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacementPropertyList~INSTANCE_LAYER().html) | Layer # 19019. |
| Public Property | [INSTANCE\_PAGEFULLNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacementPropertyList~INSTANCE_PAGEFULLNAME().html) | Page name (full) # 19023. |
| Public Property | [INSTANCE\_PAGENAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacementPropertyList~INSTANCE_PAGENAME().html) | Page name # 19022. |
| Public Property | [INSTANCE\_PAGENOMINATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacementPropertyList~INSTANCE_PAGENOMINATION().html) | Page description # 19024. |
| Public Property | [INSTANCE\_PAGETYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacementPropertyList~INSTANCE_PAGETYPE().html) | Page type # 19020. |
| Public Property | [INSTANCE\_PARAMETRICRULE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacementPropertyList~INSTANCE_PARAMETRICRULE().html) | Parametric rules # 19100. |
| Public Property | [INSTANCE\_PATHID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacementPropertyList~INSTANCE_PATHID().html) | Column number # 19005. |
| Public Property | [INSTANCE\_POSID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacementPropertyList~INSTANCE_POSID().html) | Row number # 19006. |
| Public Property | [INSTANCE\_REVISION\_LOG\_DATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_DATE().html) | Overloaded. Modification date (change tracking) # 19032. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_MARKER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_MARKER().html) | Overloaded. Revision marker (change tracking) # 19030. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_MARKER\_FORMAT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_MARKER_FORMAT().html) | Overloaded. Revision marker format (change tracking) # 19031. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_TIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_TIME().html) | Overloaded. Modification time (change tracking) # 19034. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_USER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_USER().html) | Overloaded. Creator (change tracking) # 19033. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISIONID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISIONID().html) | Overloaded. Revision change marker (from property comparison) # 10153. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISIONMARKER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISIONMARKER().html) | Overloaded. Revision marker (from property comparison) # 10152. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_XCOORD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacementPropertyList~INSTANCE_XCOORD().html) | X coordinate # 19002. |
| Public Property | [INSTANCE\_YCOORD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacementPropertyList~INSTANCE_YCOORD().html) | Y coordinate # 19003. |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacementPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |
| Public Property | [WRITEPROTECTED\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~WRITEPROTECTED_AUTOMATIC().html) | Overloaded. Change protection (hierarchical) # 3015. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of GraphicalPlacementPropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacementPropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |


