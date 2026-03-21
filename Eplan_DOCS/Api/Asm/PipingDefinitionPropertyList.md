# PipingDefinitionPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList.html

---

This class represents collection of properties of [PipingDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinition.html) class. Please check also base classes for other properties which are available for [PipingDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinition.html) objects: [PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html), [SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html), [PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html), [StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)  
            [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)  
               [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)  
                  **Eplan.EplApi.DataModel.PipingDefinitionPropertyList**

Syntax

**C#**



[DefaultMember("Property")]

public class PipingDefinitionPropertyList : PotentialDefinitionPropertyList

[DefaultMember("Property")]

public ref class PipingDefinitionPropertyList : public PotentialDefinitionPropertyList


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
| Public Constructor | [PipingDefinitionPropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ARTICLE\_MATERIAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~ARTICLE_MATERIAL().html) | Material # 22081. |
| Public Property | [ARTICLE\_MATERIAL\_LIST](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~ARTICLE_MATERIAL_LIST().html) | Material selection list # 26656. |
| Public Property | [ARTICLE\_NORM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~ARTICLE_NORM().html) | Standard # 22227. |
| Public Property | [ARTICLE\_PIPECLASS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~ARTICLE_PIPECLASS().html) | Pipe class # 22224. |
| Public Property | [ARTICLE\_PRESSURELEVEL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~ARTICLE_PRESSURELEVEL().html) | Nominal pressure level # 22226. |
| Public Property | [ARTICLE\_WIDTHRATING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~ARTICLE_WIDTHRATING().html) | Nominal size # 22225. |
| Public Property | [CONNECTION\_ACL\_COLOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_ACL_COLOR().html) | Overloaded. Autoconnecting line: Color # 31005. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_ACL\_FACTOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_ACL_FACTOR().html) | Overloaded. Autoconnecting line: Pattern length # 31018. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_ACL\_LAYER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_ACL_LAYER().html) | Overloaded. Autoconnecting line: Layer # 31017. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_ACL\_STYLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_ACL_STYLE().html) | Overloaded. Autoconnecting line: Line type # 31015. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_ACL\_WIDTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_ACL_WIDTH().html) | Overloaded. Autoconnecting line: Line thickness # 31016. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_ALTERNATE\_WIRECROSSSECTION](topic419.html) | Overloaded. Alternative connection cross-section / diameter # 31025. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_ALTERNATE\_WIRECROSSSECTION\_UNIT](topic420.html) | Overloaded. Unit for alternative connection cross-section / diameter # 31065. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_DESCRIPTION().html) | Overloaded. Connection description # 31009. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_DESIGNATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_DESIGNATION().html) | Overloaded. Connection designation # 31011. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~CONNECTION_FLOW().html) | Flow # 31085. |
| Public Property | [CONNECTION\_GROUPING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_GROUPING().html) | Overloaded. Grouping # 31069. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_MEDIUM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~CONNECTION_MEDIUM().html) | Substance # 31068. |
| Public Property | [CONNECTION\_MLWIRENUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_MLWIRENUMBER().html) | Overloaded. Connection: Color (multilingual) # 31061. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_PIPENAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~CONNECTION_PIPENAME().html) | Piping name # 31157. |
| Public Property | [CONNECTION\_PRESSURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~CONNECTION_PRESSURE().html) | Pressure # 31082. |
| Public Property | [CONNECTION\_SLEEVECROSSSECTION\_DESTINATION](topic421.html) | Overloaded. Target: Sleeve cross-section # 31054. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_SLEEVECROSSSECTION\_SOURCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_SLEEVECROSSSECTION_SOURCE().html) | Overloaded. Source: Sleeve cross-section # 31053. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_STATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~CONNECTION_STATE().html) | State (substance) # 31081. |
| Public Property | [CONNECTION\_STRIPPINGLENGTH\_DESIGNATION](topic422.html) | Overloaded. Stripping length target # 31056. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_STRIPPINGLENGTH\_SOURCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_STRIPPINGLENGTH_SOURCE().html) | Overloaded. Stripping length source # 31055. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_TEMPERATURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~CONNECTION_TEMPERATURE().html) | Temperature # 31084. |
| Public Property | [CONNECTION\_TYPEOFENDSTOP\_DESTINATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_TYPEOFENDSTOP_DESTINATION().html) | Overloaded. Wire termination processing target # 31052. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_TYPEOFENDSTOP\_SOURCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_TYPEOFENDSTOP_SOURCE().html) | Overloaded. Wire termination processing source # 31051. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_WIRECROSSSECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_WIRECROSSSECTION().html) | Overloaded. Connection: Cross-section / diameter # 31002. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_WIRECROSSSECTION\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_WIRECROSSSECTION_UNIT().html) | Overloaded. Unit for connection cross-section / diameter # 31059. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_WIRECROSSSECTION\_WITH\_UNIT](topic423.html) | Overloaded. Connection: Cross-section / diameter with unit # 31007. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_WIRELENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_WIRELENGTH().html) | Overloaded. Connection: Length with unit # 31003. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_WIRELENGTH\_FULL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_WIRELENGTH_FULL().html) | Overloaded. Connection: Length (full) # 31090. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_WIRELENGTH\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_WIRELENGTH_UNIT().html) | Overloaded. Connection: Unit of length # 31001. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_WIRELENGTH\_VALUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_WIRELENGTH_VALUE().html) | Overloaded. Connection: Length # 31000. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_WIRENUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_WIRENUMBER().html) | Overloaded. Connection color / number # 31004. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [CONNECTION\_WIRETYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_WIRETYPE().html) | Overloaded. Connection: Type designation # 31048. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [FUNC\_BLOCK\_FORMAT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~FUNC_BLOCK_FORMAT(Int32).html) | Overloaded. Block property: Format # 20202. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [FUNC\_BLOCK\_VALUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~FUNC_BLOCK_VALUE(Int32).html) | Overloaded. Block property # 20201. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [FUNC\_COMMENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~FUNC_COMMENT().html) | Overloaded. Remark # 20045. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [FUNC\_GRAVINGTEXT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~FUNC_GRAVINGTEXT().html) | Overloaded. Engraving text # 20025. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [FUNC\_SUPPLEMENTARYFIELD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~FUNC_SUPPLEMENTARYFIELD(Int32).html) | Overloaded. Supplementary field # 20901. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [FUNC\_SYMB\_DESC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~FUNC_SYMB_DESC().html) | Overloaded. Symbol description (function) # 20114. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [FUNC\_SYMB\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~FUNC_SYMB_NAME().html) | Overloaded. Symbol name # 20112. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [FUNC\_SYMB\_NUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~FUNC_SYMB_NUMBER().html) | Overloaded. Symbol number # 20168. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [FUNC\_SYMB\_VARIANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~FUNC_SYMB_VARIANT().html) | Overloaded. Symbol variant # 20113. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [FUNC\_SYMBLIB\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~FUNC_SYMBLIB_NAME().html) | Overloaded. Symbol library # 20111. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [FUNC\_SYMBOL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~FUNC_SYMBOL().html) | Overloaded. Symbol # 20575. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [FUNCTION\_NETBASEDWIRING\_ID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~FUNCTION_NETBASEDWIRING_ID(Int32).html) | Overloaded. ID for net-based connections # 20218. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [FUNCTION\_NETBASEDWIRING\_IDS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~FUNCTION_NETBASEDWIRING_IDS().html) | Overloaded. IDs for net-based connections # 20219. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [INSTANCE\_ACTIVE\_PROPERTYSET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_ACTIVE_PROPERTYSET().html) | Overloaded. Property arrangement # 19307. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_FULLPLACEMENTLOCATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_FULLPLACEMENTLOCATION().html) | Overloaded. Placement # 19007. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_PAGEFULLNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_PAGEFULLNAME().html) | Overloaded. Page name (full) # 19023. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_PAGENAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_PAGENAME().html) | Overloaded. Page name # 19022. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_PAGETYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_PAGETYPE().html) | Overloaded. Page type # 19020. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_PATHID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_PATHID().html) | Overloaded. Column number # 19005. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_POSID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_POSID().html) | Overloaded. Row number # 19006. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_DATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_DATE().html) | Overloaded. Modification date (change tracking) # 19032. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_MARKER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_MARKER().html) | Overloaded. Revision marker (change tracking) # 19030. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_MARKER\_FORMAT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_MARKER_FORMAT().html) | Overloaded. Revision marker format (change tracking) # 19031. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_TIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_TIME().html) | Overloaded. Modification time (change tracking) # 19034. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_USER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_USER().html) | Overloaded. Creator (change tracking) # 19033. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISIONID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISIONID().html) | Overloaded. Revision change marker (from property comparison) # 10153. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISIONMARKER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISIONMARKER().html) | Overloaded. Revision marker (from property comparison) # 10152. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_TYPE().html) | Overloaded. Representation type / report type # 19021. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_USER\_DEFINED\_PROPERTYSET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_USER_DEFINED_PROPERTYSET().html) | Overloaded. User-defined property arrangement: Name # 19008. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_XCOORD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_XCOORD().html) | Overloaded. X coordinate # 19002. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_YCOORD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_YCOORD().html) | Overloaded. Y coordinate # 19003. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [PIPELINE\_CHANGE\_SOURCE\_TARGET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~PIPELINE_CHANGE_SOURCE_TARGET().html) | Piping: Exchange source and target # 33301. |
| Public Property | [POTENTIAL\_FREQUENCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~POTENTIAL_FREQUENCE().html) | Overloaded. Frequency # 33004. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [POTENTIAL\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~POTENTIAL_NAME().html) | Overloaded. Name of potential # 33000. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [POTENTIAL\_NETNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~POTENTIAL_NETNAME().html) | Overloaded. Net name # 33007. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [POTENTIAL\_PARENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~POTENTIAL_PARENT().html) | Overloaded. Superior potential # 33001. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [POTENTIAL\_SIGNAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~POTENTIAL_SIGNAL().html) | Overloaded. Signal name # 33006. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [POTENTIAL\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~POTENTIAL_TYPE().html) | Overloaded. Potential type # 31006. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [POTENTIAL\_VALID\_POTENTIALS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~POTENTIAL_VALID_POTENTIALS().html) | Overloaded. Possible counter potentials # 33005. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [POTENTIAL\_VALUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~POTENTIAL_VALUE().html) | Overloaded. Potential value # 33003. (Inherited from [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)) |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |
| Public Property | [WRITEPROTECTED\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~WRITEPROTECTED_AUTOMATIC().html) | Overloaded. Change protection (hierarchical) # 3015. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of PipingDefinitionPropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |


