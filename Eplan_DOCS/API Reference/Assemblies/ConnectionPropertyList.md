# ConnectionPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList.html

---

This class represents collection of properties of [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html) class. Please check also base classes for other properties which are available for [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html) objects: [StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         **Eplan.EplApi.DataModel.ConnectionPropertyList**  
            [Eplan.EplApi.DataModel.E3D.Connection3DPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Connection3DPropertyList.html)  
            [Eplan.EplApi.DataModel.Topology.RoutedConnectionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.RoutedConnectionPropertyList.html)

Syntax

**C#**



[DefaultMember("Property")]

public class ConnectionPropertyList : StorableObjectPropertyList

[DefaultMember("Property")]

public ref class ConnectionPropertyList : public StorableObjectPropertyList


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
| Public Constructor | [ConnectionPropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ARTICLE\_MATERIAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~ARTICLE_MATERIAL().html) | Material # 22081. |
| Public Property | [ARTICLE\_MATERIAL\_LIST](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~ARTICLE_MATERIAL_LIST().html) | Material selection list # 26656. |
| Public Property | [ARTICLE\_NORM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~ARTICLE_NORM().html) | Standard # 22227. |
| Public Property | [ARTICLE\_PIPECLASS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~ARTICLE_PIPECLASS().html) | Pipe class # 22224. |
| Public Property | [ARTICLE\_PRESSURELEVEL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~ARTICLE_PRESSURELEVEL().html) | Nominal pressure level # 22226. |
| Public Property | [ARTICLE\_WIDTHRATING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~ARTICLE_WIDTHRATING().html) | Nominal size # 22225. |
| Public Property | [AUTOMATIONML\_OBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~AUTOMATIONML_OBJECTID().html) | AutomationML GUID # 25030. |
| Public Property | [CABLING\_DUCT\_TYPES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CABLING_DUCT_TYPES().html) | Topology: Routing path types # 20344. |
| Public Property | [CABLING\_PATH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CABLING_PATH().html) | Topology: Routing track # 20237. |
| Public Property | [CABLING\_STRUCTURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CABLING_STRUCTURE().html) | Topology: Structure # 20245. |
| Public Property | [CDP\_SET\_AS\_MANUAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CDP_SET_AS_MANUAL().html) | Manually set # 31046. |
| Public Property | [CONNECTION\_ACL\_COLOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_ACL_COLOR().html) | Autoconnecting line: Color # 31005. |
| Public Property | [CONNECTION\_ACL\_FACTOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_ACL_FACTOR().html) | Autoconnecting line: Pattern length # 31018. |
| Public Property | [CONNECTION\_ACL\_LAYER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_ACL_LAYER().html) | Autoconnecting line: Layer # 31017. |
| Public Property | [CONNECTION\_ACL\_STYLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_ACL_STYLE().html) | Autoconnecting line: Line type # 31015. |
| Public Property | [CONNECTION\_ACL\_WIDTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_ACL_WIDTH().html) | Autoconnecting line: Line thickness # 31016. |
| Public Property | [CONNECTION\_ALTERNATE\_WIRECROSSSECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_ALTERNATE_WIRECROSSSECTION().html) | Alternative connection cross-section / diameter # 31025. |
| Public Property | [CONNECTION\_ALTERNATE\_WIRECROSSSECTION\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_ALTERNATE_WIRECROSSSECTION_UNIT().html) | Unit for alternative connection cross-section / diameter # 31065. |
| Public Property | [CONNECTION\_AUTO\_ALTERNATE\_WIRECROSSSECTION\_WITH\_UNIT](topic136.html) | Alternative connection cross-section / diameter with unit # 31064. |
| Public Property | [CONNECTION\_AUTO\_WIRECROSSSECTION\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_AUTO_WIRECROSSSECTION_UNIT().html) | Unit for connection cross-section / diameter (automatic) # 31060. |
| Public Property | [CONNECTION\_BUNDLE\_GROUP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_BUNDLE_GROUP().html) | Bundle group # 31093. |
| Public Property | [CONNECTION\_CABLEWIRE\_PAIRINDEX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_CABLEWIRE_PAIRINDEX().html) | Pair index # 31050. |
| Public Property | [CONNECTION\_CABLEWIRE\_SHIELDEDBY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_CABLEWIRE_SHIELDEDBY().html) | Shielded by # 31049. |
| Public Property | [CONNECTION\_CABLING\_DISTRIBUTOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_CABLING_DISTRIBUTOR(Int32).html) | Topology: Connection splicers passed through (sorted) # 31137. |
| Public Property | [CONNECTION\_CABLING\_DISTRIBUTOR\_DISTANCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_CABLING_DISTRIBUTOR_DISTANCE(Int32).html) | Topology: Distance between connection splicers and source # 31138. |
| Public Property | [CONNECTION\_CABLING\_PATH\_PRESETTING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_CABLING_PATH_PRESETTING().html) | Topology: Routing track specification # 31119. |
| Public Property | [CONNECTION\_CONNECTION\_INDEX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_CONNECTION_INDEX().html) | Connection index # 31078. |
| Public Property | [CONNECTION\_DAISYCHAIN\_INDEX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_DAISYCHAIN_INDEX().html) | Daisy chain index # 31077. |
| Public Property | [CONNECTION\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_DESCRIPTION().html) | Connection description # 31009. |
| Public Property | [CONNECTION\_DESIGNATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_DESIGNATION().html) | Connection designation # 31011. |
| Public Property | [CONNECTION\_DEST\_CP\_LENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_DEST_CP_LENGTH().html) | Connection: Connection point length target # 31083. |
| Public Property | [CONNECTION\_DESTINATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_DESTINATION().html) | Target # 31020. |
| Public Property | [CONNECTION\_DESTINATION\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_DESTINATION_DBOBJECTID().html) | Object identification: Target # 31161. |
| Public Property | [CONNECTION\_DISTRIBUTORS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_DISTRIBUTORS().html) | Connection splicers passed through # 31136. |
| Public Property | [CONNECTION\_DOUBLE\_SLEEVES\_DESTINATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_DOUBLE_SLEEVES_DESTINATION().html) | Dual sleeve prescribed at 2 targets at the target # 31099. |
| Public Property | [CONNECTION\_DOUBLE\_SLEEVES\_SOURCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_DOUBLE_SLEEVES_SOURCE().html) | Dual sleeve prescribed at 2 targets at the source # 31098. |
| Public Property | [CONNECTION\_FEEDTHROUGH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_FEEDTHROUGH().html) | Routed mechanical feedthroughs # 31164. |
| Public Property | [CONNECTION\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_FLOW().html) | Flow # 31085. |
| Public Property | [CONNECTION\_FULLFUNCTIONALASSIGNMENT\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_FULLFUNCTIONALASSIGNMENT_AUTOMATIC().html) | Functional assignment (automatic) # 31105. |
| Public Property | [CONNECTION\_FULLINSTALLATIONNUMBER\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_FULLINSTALLATIONNUMBER_AUTOMATIC().html) | Higher-level function number (automatic) # 31111. |
| Public Property | [CONNECTION\_FULLLOCATION\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_FULLLOCATION_AUTOMATIC().html) | Location designation (automatic) # 31103. |
| Public Property | [CONNECTION\_FULLPLACEOFINSTALLATION\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_FULLPLACEOFINSTALLATION_AUTOMATIC().html) | Installation site (automatic) # 31107. |
| Public Property | [CONNECTION\_FULLPLANT\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_FULLPLANT_AUTOMATIC().html) | Function designation (automatic) # 31101. |
| Public Property | [CONNECTION\_FULLPRODUCT\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_FULLPRODUCT_AUTOMATIC().html) | Product (automatic) # 31134. |
| Public Property | [CONNECTION\_FULLUSERDEFINED\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_FULLUSERDEFINED_AUTOMATIC().html) | User-defined structure (automatic) # 31109. |
| Public Property | [CONNECTION\_FUNCTIONALASSIGNMENT\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_FUNCTIONALASSIGNMENT_AUTOMATIC().html) | Functional assignment: Main identifier (automatic) # 31106. |
| Public Property | [CONNECTION\_GROUPING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_GROUPING().html) | Grouping # 31069. |
| Public Property | [CONNECTION\_HAS\_CDP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_HAS_CDP().html) | Connection definition point exists # 31089. |
| Public Property | [CONNECTION\_HAS\_DISTRIBUTOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_HAS_DISTRIBUTOR().html) | Connection splicers exist # 31139. |
| Public Property | [CONNECTION\_HAS\_FEEDTHROUGH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_HAS_FEEDTHROUGH().html) | Mechanical feedthroughs available # 31165. |
| Public Property | [CONNECTION\_INSTALLATIONNUMBER\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_INSTALLATIONNUMBER_AUTOMATIC().html) | Higher-level function number: Main identifier (automatic) # 31112. |
| Public Property | [CONNECTION\_IS\_CABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_IS_CABLE().html) | Cable connection # 31058. |
| Public Property | [CONNECTION\_IS\_PACKET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_IS_PACKET().html) | Conduit connection # 31086. |
| Public Property | [CONNECTION\_IS\_PHASEBAR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_IS_PHASEBAR().html) | Phase busbar connection # 31135. |
| Public Property | [CONNECTION\_IS\_PIPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_IS_PIPE().html) | Line # 31146. |
| Public Property | [CONNECTION\_KINDOFWIRE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_KINDOFWIRE().html) | Connection: Association # 31142. |
| Public Property | [CONNECTION\_LOCATION\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_LOCATION_AUTOMATIC().html) | Location designation: Main identifier (automatic) # 31104. |
| Public Property | [CONNECTION\_LOCATION\_DESTINATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_LOCATION_DESTINATION().html) | Target: Placement # 31022. |
| Public Property | [CONNECTION\_LOCATION\_SOURCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_LOCATION_SOURCE().html) | Source: Placement # 31021. |
| Public Property | [CONNECTION\_MEDIUM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_MEDIUM().html) | Substance # 31068. |
| Public Property | [CONNECTION\_MLWIRENUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_MLWIRENUMBER().html) | Connection: Color (multilingual) # 31061. |
| Public Property | [CONNECTION\_NET\_INDEX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_NET_INDEX().html) | Net index # 31076. |
| Public Property | [CONNECTION\_NR\_DESTINATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_NR_DESTINATION().html) | Target: Target number # 31024. |
| Public Property | [CONNECTION\_NR\_SOURCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_NR_SOURCE().html) | Source: Target number # 31023. |
| Public Property | [CONNECTION\_PAGENAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_PAGENAME().html) | Name of page containing connection # 31026. |
| Public Property | [CONNECTION\_PIPENAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_PIPENAME().html) | Piping name # 31157. |
| Public Property | [CONNECTION\_PLACEOFINSTALLATION\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_PLACEOFINSTALLATION_AUTOMATIC().html) | Installation site: Main identifier (automatic) # 31108. |
| Public Property | [CONNECTION\_PLANT\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_PLANT_AUTOMATIC().html) | Function designation: Main identifier (automatic) # 31102. |
| Public Property | [CONNECTION\_PRESSURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_PRESSURE().html) | Pressure # 31082. |
| Public Property | [CONNECTION\_PRODUCT\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_PRODUCT_AUTOMATIC().html) | Product: Main identifier (automatic) # 31133. |
| Public Property | [CONNECTION\_PROTECTED\_ROUTING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_PROTECTED_ROUTING().html) | Protected routing # 31113. |
| Public Property | [CONNECTION\_ROUTE\_DESTINATION\_XPOS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_ROUTE_DESTINATION_XPOS().html) | Routing track target: X coordinate # 31151. |
| Public Property | [CONNECTION\_ROUTE\_DESTINATION\_YPOS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_ROUTE_DESTINATION_YPOS().html) | Routing track target: Y coordinate # 31152. |
| Public Property | [CONNECTION\_ROUTE\_DESTINATION\_ZPOS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_ROUTE_DESTINATION_ZPOS().html) | Routing track target: Z coordinate # 31153. |
| Public Property | [CONNECTION\_ROUTE\_SOURCE\_XPOS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_ROUTE_SOURCE_XPOS().html) | Routing track source: X coordinate # 31148. |
| Public Property | [CONNECTION\_ROUTE\_SOURCE\_YPOS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_ROUTE_SOURCE_YPOS().html) | Routing track source: Y coordinate # 31149. |
| Public Property | [CONNECTION\_ROUTE\_SOURCE\_ZPOS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_ROUTE_SOURCE_ZPOS().html) | Routing track source: Z coordinate # 31150. |
| Public Property | [CONNECTION\_ROUTING\_DIRECTION\_DESTINATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_ROUTING_DIRECTION_DESTINATION().html) | Routing direction target # 31115. |
| Public Property | [CONNECTION\_ROUTING\_DIRECTION\_SOURCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_ROUTING_DIRECTION_SOURCE().html) | Routing direction source # 31114. |
| Public Property | [CONNECTION\_SADDLEJUMPER\_SLOT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_SADDLEJUMPER_SLOT().html) | Saddle jumper slot # 31163. |
| Public Property | [CONNECTION\_SLEEVECROSSSECTION\_DESTINATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_SLEEVECROSSSECTION_DESTINATION().html) | Target: Sleeve cross-section # 31054. |
| Public Property | [CONNECTION\_SLEEVECROSSSECTION\_SOURCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_SLEEVECROSSSECTION_SOURCE().html) | Source: Sleeve cross-section # 31053. |
| Public Property | [CONNECTION\_SOURCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_SOURCE().html) | Source # 31019. |
| Public Property | [CONNECTION\_SOURCE\_CP\_LENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_SOURCE_CP_LENGTH().html) | Connection: Connection point length source # 31080. |
| Public Property | [CONNECTION\_SOURCE\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_SOURCE_DBOBJECTID().html) | Object identification: Source # 31160. |
| Public Property | [CONNECTION\_STATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_STATE().html) | State (substance) # 31081. |
| Public Property | [CONNECTION\_STRIPPINGLENGTH\_DESIGNATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_STRIPPINGLENGTH_DESIGNATION().html) | Stripping length target # 31056. |
| Public Property | [CONNECTION\_STRIPPINGLENGTH\_SOURCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_STRIPPINGLENGTH_SOURCE().html) | Stripping length source # 31055. |
| Public Property | [CONNECTION\_SWAP\_SRC\_DEST](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_SWAP_SRC_DEST().html) | Exchange source and target # 31013. |
| Public Property | [CONNECTION\_TARGETINFO\_DESTINATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_TARGETINFO_DESTINATION().html) | Internal / External index: Target # 31141. |
| Public Property | [CONNECTION\_TARGETINFO\_SOURCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_TARGETINFO_SOURCE().html) | Internal / External index: Source # 31140. |
| Public Property | [CONNECTION\_TEMPERATURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_TEMPERATURE().html) | Temperature # 31084. |
| Public Property | [CONNECTION\_TERMINAL\_CONNECTIONDESIGNATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_TERMINAL_CONNECTIONDESIGNATION().html) | Connection: Associated terminal connection point (connection point designation) # 31118. |
| Public Property | [CONNECTION\_TERMINALSIZE\_DESTINATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_TERMINALSIZE_DESTINATION().html) | Connection dimension target # 31097. |
| Public Property | [CONNECTION\_TERMINALSIZE\_SOURCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_TERMINALSIZE_SOURCE().html) | Connection dimension source # 31096. |
| Public Property | [CONNECTION\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_TYPE().html) | Type of administration # 31075. |
| Public Property | [CONNECTION\_TYPEOFENDSTOP\_DESTINATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_TYPEOFENDSTOP_DESTINATION().html) | Wire termination processing target # 31052. |
| Public Property | [CONNECTION\_TYPEOFENDSTOP\_SOURCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_TYPEOFENDSTOP_SOURCE().html) | Wire termination processing source # 31051. |
| Public Property | [CONNECTION\_USERDEFINED\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_USERDEFINED_AUTOMATIC().html) | User-defined structure: Main identifier (automatic) # 31110. |
| Public Property | [CONNECTION\_WIRE\_BUNDLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_WIRE_BUNDLE().html) | Bundle # 31092. |
| Public Property | [CONNECTION\_WIRECROSSSECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_WIRECROSSSECTION().html) | Connection: Cross-section / diameter # 31002. |
| Public Property | [CONNECTION\_WIRECROSSSECTION\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_WIRECROSSSECTION_UNIT().html) | Unit for connection cross-section / diameter # 31059. |
| Public Property | [CONNECTION\_WIRECROSSSECTION\_WITH\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_WIRECROSSSECTION_WITH_UNIT().html) | Connection: Cross-section / diameter with unit # 31007. |
| Public Property | [CONNECTION\_WIRELENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_WIRELENGTH().html) | Connection: Length with unit # 31003. |
| Public Property | [CONNECTION\_WIRELENGTH\_FULL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_WIRELENGTH_FULL().html) | Connection: Length (full) # 31090. |
| Public Property | [CONNECTION\_WIRELENGTH\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_WIRELENGTH_UNIT().html) | Connection: Unit of length # 31001. |
| Public Property | [CONNECTION\_WIRELENGTH\_VALUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_WIRELENGTH_VALUE().html) | Connection: Length # 31000. |
| Public Property | [CONNECTION\_WIRENUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_WIRENUMBER().html) | Connection color / number # 31004. |
| Public Property | [CONNECTION\_WIRETYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_WIRETYPE().html) | Connection: Type designation # 31048. |
| Public Property | [CONNECTION\_WIRING\_PATH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_WIRING_PATH().html) | Layout space: Routing track # 31095. |
| Public Property | [CONNECTION\_WIRING\_PATH\_PRESETTING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_WIRING_PATH_PRESETTING().html) | Layout space: Routing track specification # 31094. |
| Public Property | [CONNECTION\_WIRING\_PATH\_PRESETTING\_AT\_DESTINATION](topic137.html) | Layout space: Specification for entry into routing path network (target) # 31116. |
| Public Property | [CONNECTION\_WIRING\_PATH\_PRESETTING\_AT\_SOURCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_WIRING_PATH_PRESETTING_AT_SOURCE().html) | Layout space: Specification for entry into routing path network (source) # 31100. |
| Public Property | [CONNECTION\_WORKING\_CONTROL\_LINE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_WORKING_CONTROL_LINE().html) | Pressure line / control line # 31057. |
| Public Property | [DESIGNATION\_FULLFUNCTIONALASSIGNMENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLFUNCTIONALASSIGNMENT().html) | Functional assignment # 1320. |
| Public Property | [DESIGNATION\_FULLFUNCTIONALASSIGNMENT\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLFUNCTIONALASSIGNMENT_DESCR().html) | Functional assignment: Description # 1350. |
| Public Property | [DESIGNATION\_FULLFUNCTIONALASSIGNMENT\_WITHPREFIX](topic138.html) | Functional assignment with preceding sign # 1340. |
| Public Property | [DESIGNATION\_FULLINSTALLATIONNUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLINSTALLATIONNUMBER().html) | Higher-level function number # 1720. |
| Public Property | [DESIGNATION\_FULLINSTALLATIONNUMBER\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLINSTALLATIONNUMBER_DESCR().html) | Higher-level function number: Description # 1750. |
| Public Property | [DESIGNATION\_FULLINSTALLATIONNUMBER\_WITHPREFIX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLINSTALLATIONNUMBER_WITHPREFIX().html) | Higher-level function number with preceding sign # 1740. |
| Public Property | [DESIGNATION\_FULLLOCATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLLOCATION().html) | Location designation # 1220. |
| Public Property | [DESIGNATION\_FULLLOCATION\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLLOCATION_DESCR().html) | Location designation: Description # 1250. |
| Public Property | [DESIGNATION\_FULLLOCATION\_WITHPREFIX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLLOCATION_WITHPREFIX().html) | Location designation with preceding sign # 1240. |
| Public Property | [DESIGNATION\_FULLPLACEOFINSTALLATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLPLACEOFINSTALLATION().html) | Installation site # 1420. |
| Public Property | [DESIGNATION\_FULLPLACEOFINSTALLATION\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLPLACEOFINSTALLATION_DESCR().html) | Installation site: Description # 1450. |
| Public Property | [DESIGNATION\_FULLPLACEOFINSTALLATION\_WITHPREFIX](topic139.html) | Installation site with preceding sign # 1440. |
| Public Property | [DESIGNATION\_FULLPLANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLPLANT().html) | Function designation # 1120. |
| Public Property | [DESIGNATION\_FULLPLANT\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLPLANT_DESCR().html) | Function designation: Description # 1150. |
| Public Property | [DESIGNATION\_FULLPLANT\_WITHPREFIX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLPLANT_WITHPREFIX().html) | Function designation with preceding sign # 1140. |
| Public Property | [DESIGNATION\_FULLPRODUCT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLPRODUCT().html) | Product # 1820. |
| Public Property | [DESIGNATION\_FULLPRODUCT\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLPRODUCT_DESCR().html) | Product: Description # 1850. |
| Public Property | [DESIGNATION\_FULLPRODUCT\_WITHPREFIX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLPRODUCT_WITHPREFIX().html) | Product with preceding sign # 1840. |
| Public Property | [DESIGNATION\_FULLSUBFUNCTIONALASSIGNMENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLSUBFUNCTIONALASSIGNMENT().html) | Functional assignment (sub-identifier, complete) # 1321. |
| Public Property | [DESIGNATION\_FULLSUBINSTALLATIONNUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLSUBINSTALLATIONNUMBER().html) | Higher-level function number (sub-identifier, complete) # 1721. |
| Public Property | [DESIGNATION\_FULLSUBLOCATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLSUBLOCATION().html) | Location designation (sub-identifier, complete) # 1221. |
| Public Property | [DESIGNATION\_FULLSUBPLACEOFINSTALLATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLSUBPLACEOFINSTALLATION().html) | Installation site (sub-identifier, complete) # 1421. |
| Public Property | [DESIGNATION\_FULLSUBPLANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLSUBPLANT().html) | Function designation (sub-identifier, complete) # 1121. |
| Public Property | [DESIGNATION\_FULLSUBPRODUCT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLSUBPRODUCT().html) | Product (sub-identifier, complete) # 1821. |
| Public Property | [DESIGNATION\_FULLSUBUSERDEFINED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLSUBUSERDEFINED().html) | User-defined structure (sub-identifier, complete) # 1621. |
| Public Property | [DESIGNATION\_FULLUSERDEFINED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLUSERDEFINED().html) | User-defined structure # 1620. |
| Public Property | [DESIGNATION\_FULLUSERDEFINED\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLUSERDEFINED_DESCR().html) | User-defined structure: Description # 1650. |
| Public Property | [DESIGNATION\_FULLUSERDEFINED\_WITHPREFIX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FULLUSERDEFINED_WITHPREFIX().html) | User-defined structure with preceding sign # 1640. |
| Public Property | [DESIGNATION\_FUNCTIONALASSIGNMENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FUNCTIONALASSIGNMENT().html) | Functional assignment (main identifier) # 1300. |
| Public Property | [DESIGNATION\_FUNCTIONALASSIGNMENT\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_FUNCTIONALASSIGNMENT_DESCR().html) | Functional assignment (main identifier): Description # 1330. |
| Public Property | [DESIGNATION\_FUNCTIONALASSIGNMENT\_LEADINGPARTS](topic140.html) | Functional assignment (leading identifiers) # 1322. |
| Public Property | [DESIGNATION\_INSTALLATIONNUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_INSTALLATIONNUMBER().html) | Higher-level function number (main identifier) # 1700. |
| Public Property | [DESIGNATION\_INSTALLATIONNUMBER\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_INSTALLATIONNUMBER_DESCR().html) | Higher-level function number (main identifier): Description # 1730. |
| Public Property | [DESIGNATION\_INSTALLATIONNUMBER\_LEADINGPARTS](topic141.html) | Higher-level function number (leading identifiers) # 1722. |
| Public Property | [DESIGNATION\_LOCATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_LOCATION().html) | Location designation (main identifier) # 1200. |
| Public Property | [DESIGNATION\_LOCATION\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_LOCATION_DESCR().html) | Location designation (main identifier): Description # 1230. |
| Public Property | [DESIGNATION\_LOCATION\_LEADINGPARTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_LOCATION_LEADINGPARTS(Int32).html) | Location designation (leading identifiers) # 1222. |
| Public Property | [DESIGNATION\_PLACEOFINSTALLATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_PLACEOFINSTALLATION().html) | Installation site (main identifier) # 1400. |
| Public Property | [DESIGNATION\_PLACEOFINSTALLATION\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_PLACEOFINSTALLATION_DESCR().html) | Installation site (main identifier): Description # 1430. |
| Public Property | [DESIGNATION\_PLACEOFINSTALLATION\_LEADINGPARTS](topic142.html) | Installation site (leading identifiers) # 1422. |
| Public Property | [DESIGNATION\_PLANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_PLANT().html) | Function designation (main identifier) # 1100. |
| Public Property | [DESIGNATION\_PLANT\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_PLANT_DESCR().html) | Function designation (main identifier): Description # 1130. |
| Public Property | [DESIGNATION\_PLANT\_LEADINGPARTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_PLANT_LEADINGPARTS(Int32).html) | Function designation (leading identifiers) # 1122. |
| Public Property | [DESIGNATION\_PRODUCT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_PRODUCT().html) | Product (main identifier) # 1800. |
| Public Property | [DESIGNATION\_PRODUCT\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_PRODUCT_DESCR().html) | Product (main identifier): Description # 1830. |
| Public Property | [DESIGNATION\_PRODUCT\_LEADINGPARTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_PRODUCT_LEADINGPARTS(Int32).html) | Product (leading identifiers) # 1822. |
| Public Property | [DESIGNATION\_SUBFUNCTIONALASSIGNMENT1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBFUNCTIONALASSIGNMENT1().html) | Functional assignment (sub-identifier 1) # 1301. |
| Public Property | [DESIGNATION\_SUBFUNCTIONALASSIGNMENT1\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBFUNCTIONALASSIGNMENT1_DESCR().html) | Functional assignment (sub-identifier 1): Description # 1331. |
| Public Property | [DESIGNATION\_SUBFUNCTIONALASSIGNMENT2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBFUNCTIONALASSIGNMENT2().html) | Functional assignment (sub-identifier 2) # 1302. |
| Public Property | [DESIGNATION\_SUBFUNCTIONALASSIGNMENT2\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBFUNCTIONALASSIGNMENT2_DESCR().html) | Functional assignment (sub-identifier 2): Description # 1332. |
| Public Property | [DESIGNATION\_SUBFUNCTIONALASSIGNMENT3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBFUNCTIONALASSIGNMENT3().html) | Functional assignment (sub-identifier 3) # 1303. |
| Public Property | [DESIGNATION\_SUBFUNCTIONALASSIGNMENT3\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBFUNCTIONALASSIGNMENT3_DESCR().html) | Functional assignment (sub-identifier 3): Description # 1333. |
| Public Property | [DESIGNATION\_SUBFUNCTIONALASSIGNMENT4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBFUNCTIONALASSIGNMENT4().html) | Functional assignment (sub-identifier 4) # 1304. |
| Public Property | [DESIGNATION\_SUBFUNCTIONALASSIGNMENT4\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBFUNCTIONALASSIGNMENT4_DESCR().html) | Functional assignment (sub-identifier 4): Description # 1334. |
| Public Property | [DESIGNATION\_SUBFUNCTIONALASSIGNMENT5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBFUNCTIONALASSIGNMENT5().html) | Functional assignment (sub-identifier 5) # 1305. |
| Public Property | [DESIGNATION\_SUBFUNCTIONALASSIGNMENT5\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBFUNCTIONALASSIGNMENT5_DESCR().html) | Functional assignment (sub-identifier 5): Description # 1335. |
| Public Property | [DESIGNATION\_SUBFUNCTIONALASSIGNMENT6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBFUNCTIONALASSIGNMENT6().html) | Functional assignment (sub-identifier 6) # 1306. |
| Public Property | [DESIGNATION\_SUBFUNCTIONALASSIGNMENT6\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBFUNCTIONALASSIGNMENT6_DESCR().html) | Functional assignment (sub-identifier 6): Description # 1336. |
| Public Property | [DESIGNATION\_SUBFUNCTIONALASSIGNMENT7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBFUNCTIONALASSIGNMENT7().html) | Functional assignment (sub-identifier 7) # 1307. |
| Public Property | [DESIGNATION\_SUBFUNCTIONALASSIGNMENT7\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBFUNCTIONALASSIGNMENT7_DESCR().html) | Functional assignment (sub-identifier 7): Description # 1337. |
| Public Property | [DESIGNATION\_SUBFUNCTIONALASSIGNMENT8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBFUNCTIONALASSIGNMENT8().html) | Functional assignment (sub-identifier 8) # 1308. |
| Public Property | [DESIGNATION\_SUBFUNCTIONALASSIGNMENT8\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBFUNCTIONALASSIGNMENT8_DESCR().html) | Functional assignment (sub-identifier 8): Description # 1338. |
| Public Property | [DESIGNATION\_SUBFUNCTIONALASSIGNMENT9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBFUNCTIONALASSIGNMENT9().html) | Functional assignment (sub-identifier 9) # 1309. |
| Public Property | [DESIGNATION\_SUBFUNCTIONALASSIGNMENT9\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBFUNCTIONALASSIGNMENT9_DESCR().html) | Functional assignment (sub-identifier 9): Description # 1339. |
| Public Property | [DESIGNATION\_SUBLOCATION1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION1().html) | Location designation (sub-identifier 1) # 1201. |
| Public Property | [DESIGNATION\_SUBLOCATION1\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION1_DESCR().html) | Location designation (sub-identifier 1): Description # 1231. |
| Public Property | [DESIGNATION\_SUBLOCATION2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION2().html) | Location designation (sub-identifier 2) # 1202. |
| Public Property | [DESIGNATION\_SUBLOCATION2\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION2_DESCR().html) | Location designation (sub-identifier 2): Description # 1232. |
| Public Property | [DESIGNATION\_SUBLOCATION3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION3().html) | Location designation (sub-identifier 3) # 1203. |
| Public Property | [DESIGNATION\_SUBLOCATION3\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION3_DESCR().html) | Location designation (sub-identifier 3): Description # 1233. |
| Public Property | [DESIGNATION\_SUBLOCATION4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION4().html) | Location designation (sub-identifier 4) # 1204. |
| Public Property | [DESIGNATION\_SUBLOCATION4\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION4_DESCR().html) | Location designation (sub-identifier 4): Description # 1234. |
| Public Property | [DESIGNATION\_SUBLOCATION5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION5().html) | Location designation (sub-identifier 5) # 1205. |
| Public Property | [DESIGNATION\_SUBLOCATION5\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION5_DESCR().html) | Location designation (sub-identifier 5): Description # 1235. |
| Public Property | [DESIGNATION\_SUBLOCATION6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION6().html) | Location designation (sub-identifier 6) # 1206. |
| Public Property | [DESIGNATION\_SUBLOCATION6\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION6_DESCR().html) | Location designation (sub-identifier 6): Description # 1236. |
| Public Property | [DESIGNATION\_SUBLOCATION7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION7().html) | Location designation (sub-identifier 7) # 1207. |
| Public Property | [DESIGNATION\_SUBLOCATION7\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION7_DESCR().html) | Location designation (sub-identifier 7): Description # 1237. |
| Public Property | [DESIGNATION\_SUBLOCATION8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION8().html) | Location designation (sub-identifier 8) # 1208. |
| Public Property | [DESIGNATION\_SUBLOCATION8\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION8_DESCR().html) | Location designation (sub-identifier 8): Description # 1238. |
| Public Property | [DESIGNATION\_SUBLOCATION9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION9().html) | Location designation (sub-identifier 9) # 1209. |
| Public Property | [DESIGNATION\_SUBLOCATION9\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION9_DESCR().html) | Location designation (sub-identifier 9): Description # 1239. |
| Public Property | [DESIGNATION\_SUBPLACEOFINSTALLATION1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLACEOFINSTALLATION1().html) | Installation site (sub-identifier 1) # 1401. |
| Public Property | [DESIGNATION\_SUBPLACEOFINSTALLATION1\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLACEOFINSTALLATION1_DESCR().html) | Installation site (sub-identifier 1): Description # 1431. |
| Public Property | [DESIGNATION\_SUBPLACEOFINSTALLATION2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLACEOFINSTALLATION2().html) | Installation site (sub-identifier 2) # 1402. |
| Public Property | [DESIGNATION\_SUBPLACEOFINSTALLATION2\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLACEOFINSTALLATION2_DESCR().html) | Installation site (sub-identifier 2): Description # 1432. |
| Public Property | [DESIGNATION\_SUBPLACEOFINSTALLATION3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLACEOFINSTALLATION3().html) | Installation site (sub-identifier 3) # 1403. |
| Public Property | [DESIGNATION\_SUBPLACEOFINSTALLATION3\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLACEOFINSTALLATION3_DESCR().html) | Installation site (sub-identifier 3): Description # 1433. |
| Public Property | [DESIGNATION\_SUBPLACEOFINSTALLATION4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLACEOFINSTALLATION4().html) | Installation site (sub-identifier 4) # 1404. |
| Public Property | [DESIGNATION\_SUBPLACEOFINSTALLATION4\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLACEOFINSTALLATION4_DESCR().html) | Installation site (sub-identifier 4): Description # 1434. |
| Public Property | [DESIGNATION\_SUBPLACEOFINSTALLATION5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLACEOFINSTALLATION5().html) | Installation site (sub-identifier 5) # 1405. |
| Public Property | [DESIGNATION\_SUBPLACEOFINSTALLATION5\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLACEOFINSTALLATION5_DESCR().html) | Installation site (sub-identifier 5): Description # 1435. |
| Public Property | [DESIGNATION\_SUBPLACEOFINSTALLATION6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLACEOFINSTALLATION6().html) | Installation site (sub-identifier 6) # 1406. |
| Public Property | [DESIGNATION\_SUBPLACEOFINSTALLATION6\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLACEOFINSTALLATION6_DESCR().html) | Installation site (sub-identifier 6): Description # 1436. |
| Public Property | [DESIGNATION\_SUBPLACEOFINSTALLATION7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLACEOFINSTALLATION7().html) | Installation site (sub-identifier 7) # 1407. |
| Public Property | [DESIGNATION\_SUBPLACEOFINSTALLATION7\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLACEOFINSTALLATION7_DESCR().html) | Installation site (sub-identifier 7): Description # 1437. |
| Public Property | [DESIGNATION\_SUBPLACEOFINSTALLATION8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLACEOFINSTALLATION8().html) | Installation site (sub-identifier 8) # 1408. |
| Public Property | [DESIGNATION\_SUBPLACEOFINSTALLATION8\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLACEOFINSTALLATION8_DESCR().html) | Installation site (sub-identifier 8): Description # 1438. |
| Public Property | [DESIGNATION\_SUBPLACEOFINSTALLATION9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLACEOFINSTALLATION9().html) | Installation site (sub-identifier 9) # 1409. |
| Public Property | [DESIGNATION\_SUBPLACEOFINSTALLATION9\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLACEOFINSTALLATION9_DESCR().html) | Installation site (sub-identifier 9): Description # 1439. |
| Public Property | [DESIGNATION\_SUBPLANT1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLANT1().html) | Function designation (sub-identifier 1) # 1101. |
| Public Property | [DESIGNATION\_SUBPLANT1\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLANT1_DESCR().html) | Function designation (sub-identifier 1): Description # 1131. |
| Public Property | [DESIGNATION\_SUBPLANT2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLANT2().html) | Function designation (sub-identifier 2) # 1102. |
| Public Property | [DESIGNATION\_SUBPLANT2\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLANT2_DESCR().html) | Function designation (sub-identifier 2): Description # 1132. |
| Public Property | [DESIGNATION\_SUBPLANT3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLANT3().html) | Function designation (sub-identifier 3) # 1103. |
| Public Property | [DESIGNATION\_SUBPLANT3\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLANT3_DESCR().html) | Function designation (sub-identifier 3): Description # 1133. |
| Public Property | [DESIGNATION\_SUBPLANT4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLANT4().html) | Function designation (sub-identifier 4) # 1104. |
| Public Property | [DESIGNATION\_SUBPLANT4\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLANT4_DESCR().html) | Function designation (sub-identifier 4): Description # 1134. |
| Public Property | [DESIGNATION\_SUBPLANT5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLANT5().html) | Function designation (sub-identifier 5) # 1105. |
| Public Property | [DESIGNATION\_SUBPLANT5\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLANT5_DESCR().html) | Function designation (sub-identifier 5): Description # 1135. |
| Public Property | [DESIGNATION\_SUBPLANT6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLANT6().html) | Function designation (sub-identifier 6) # 1106. |
| Public Property | [DESIGNATION\_SUBPLANT6\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLANT6_DESCR().html) | Function designation (sub-identifier 6): Description # 1136. |
| Public Property | [DESIGNATION\_SUBPLANT7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLANT7().html) | Function designation (sub-identifier 7) # 1107. |
| Public Property | [DESIGNATION\_SUBPLANT7\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLANT7_DESCR().html) | Function designation (sub-identifier 7): Description # 1137. |
| Public Property | [DESIGNATION\_SUBPLANT8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLANT8().html) | Function designation (sub-identifier 8) # 1108. |
| Public Property | [DESIGNATION\_SUBPLANT8\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLANT8_DESCR().html) | Function designation (sub-identifier 8): Description # 1138. |
| Public Property | [DESIGNATION\_SUBPLANT9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLANT9().html) | Function designation (sub-identifier 9) # 1109. |
| Public Property | [DESIGNATION\_SUBPLANT9\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPLANT9_DESCR().html) | Function designation (sub-identifier 9): Description # 1139. |
| Public Property | [DESIGNATION\_SUBPRODUCT1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPRODUCT1().html) | Product (sub-identifier 1) # 1801. |
| Public Property | [DESIGNATION\_SUBPRODUCT1\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPRODUCT1_DESCR().html) | Product (sub-identifier 1): Description # 1831. |
| Public Property | [DESIGNATION\_SUBPRODUCT2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPRODUCT2().html) | Product (sub-identifier 2) # 1802. |
| Public Property | [DESIGNATION\_SUBPRODUCT2\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPRODUCT2_DESCR().html) | Product (sub-identifier 2): Description # 1832. |
| Public Property | [DESIGNATION\_SUBPRODUCT3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPRODUCT3().html) | Product (sub-identifier 3) # 1803. |
| Public Property | [DESIGNATION\_SUBPRODUCT3\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPRODUCT3_DESCR().html) | Product (sub-identifier 3): Description # 1833. |
| Public Property | [DESIGNATION\_SUBPRODUCT4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPRODUCT4().html) | Product (sub-identifier 4) # 1804. |
| Public Property | [DESIGNATION\_SUBPRODUCT4\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPRODUCT4_DESCR().html) | Product (sub-identifier 4): Description # 1834. |
| Public Property | [DESIGNATION\_SUBPRODUCT5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPRODUCT5().html) | Product (sub-identifier 5) # 1805. |
| Public Property | [DESIGNATION\_SUBPRODUCT5\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPRODUCT5_DESCR().html) | Product (sub-identifier 5): Description # 1835. |
| Public Property | [DESIGNATION\_SUBPRODUCT6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPRODUCT6().html) | Product (sub-identifier 6) # 1806. |
| Public Property | [DESIGNATION\_SUBPRODUCT6\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPRODUCT6_DESCR().html) | Product (sub-identifier 6): Description # 1836. |
| Public Property | [DESIGNATION\_SUBPRODUCT7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPRODUCT7().html) | Product (sub-identifier 7) # 1807. |
| Public Property | [DESIGNATION\_SUBPRODUCT7\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPRODUCT7_DESCR().html) | Product (sub-identifier 7): Description # 1837. |
| Public Property | [DESIGNATION\_SUBPRODUCT8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPRODUCT8().html) | Product (sub-identifier 8) # 1808. |
| Public Property | [DESIGNATION\_SUBPRODUCT8\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPRODUCT8_DESCR().html) | Product (sub-identifier 8): Description # 1838. |
| Public Property | [DESIGNATION\_SUBPRODUCT9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPRODUCT9().html) | Product (sub-identifier 9) # 1809. |
| Public Property | [DESIGNATION\_SUBPRODUCT9\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBPRODUCT9_DESCR().html) | Product (sub-identifier 9): Description # 1839. |
| Public Property | [DESIGNATION\_USERDEFINED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED().html) | User-defined structure (main identifier) # 1600. |
| Public Property | [DESIGNATION\_USERDEFINED\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_DESCR().html) | User-defined structure (main identifier): Description # 1630. |
| Public Property | [DESIGNATION\_USERDEFINED\_LEADINGPARTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_LEADINGPARTS(Int32).html) | User-defined structure (leading identifiers) # 1622. |
| Public Property | [DESIGNATION\_USERDEFINED\_SUB1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB1().html) | User-defined structure (sub-identifier 1) # 1601. |
| Public Property | [DESIGNATION\_USERDEFINED\_SUB1\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB1_DESCR().html) | User-defined structure (sub-identifier 1): Description # 1631. |
| Public Property | [DESIGNATION\_USERDEFINED\_SUB2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB2().html) | User-defined structure (sub-identifier 2) # 1602. |
| Public Property | [DESIGNATION\_USERDEFINED\_SUB2\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB2_DESCR().html) | User-defined structure (sub-identifier 2): Description # 1632. |
| Public Property | [DESIGNATION\_USERDEFINED\_SUB3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB3().html) | User-defined structure (sub-identifier 3) # 1603. |
| Public Property | [DESIGNATION\_USERDEFINED\_SUB3\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB3_DESCR().html) | User-defined structure (sub-identifier 3): Description # 1633. |
| Public Property | [DESIGNATION\_USERDEFINED\_SUB4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB4().html) | User-defined structure (sub-identifier 4) # 1604. |
| Public Property | [DESIGNATION\_USERDEFINED\_SUB4\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB4_DESCR().html) | User-defined structure (sub-identifier 4): Description # 1634. |
| Public Property | [DESIGNATION\_USERDEFINED\_SUB5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB5().html) | User-defined structure (sub-identifier 5) # 1605. |
| Public Property | [DESIGNATION\_USERDEFINED\_SUB5\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB5_DESCR().html) | User-defined structure (sub-identifier 5): Description # 1635. |
| Public Property | [DESIGNATION\_USERDEFINED\_SUB6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB6().html) | User-defined structure (sub-identifier 6) # 1606. |
| Public Property | [DESIGNATION\_USERDEFINED\_SUB6\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB6_DESCR().html) | User-defined structure (sub-identifier 6): Description # 1636. |
| Public Property | [DESIGNATION\_USERDEFINED\_SUB7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB7().html) | User-defined structure (sub-identifier 7) # 1607. |
| Public Property | [DESIGNATION\_USERDEFINED\_SUB7\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB7_DESCR().html) | User-defined structure (sub-identifier 7): Description # 1637. |
| Public Property | [DESIGNATION\_USERDEFINED\_SUB8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB8().html) | User-defined structure (sub-identifier 8) # 1608. |
| Public Property | [DESIGNATION\_USERDEFINED\_SUB8\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB8_DESCR().html) | User-defined structure (sub-identifier 8): Description # 1638. |
| Public Property | [DESIGNATION\_USERDEFINED\_SUB9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB9().html) | User-defined structure (sub-identifier 9) # 1609. |
| Public Property | [DESIGNATION\_USERDEFINED\_SUB9\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB9_DESCR().html) | User-defined structure (sub-identifier 9): Description # 1639. |
| Public Property | [EDITINGAREA\_CRAFT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~EDITINGAREA_CRAFT().html) | Trade (Defined working sections) # 25000. |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [FUNC\_ADDITIONALIDENTIFYINGNAMEPART](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ADDITIONALIDENTIFYINGNAMEPART().html) | Additional identifying name element # 20032. |
| Public Property | [FUNC\_ARTICLE\_ABSORPTION\_VOLUME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ABSORPTION_VOLUME(Int32).html) | Reception volume # 26224. |
| Public Property | [FUNC\_ARTICLE\_ACCURACY\_FOR\_DYNAMIC\_VISCOSITY](topic143.html) | Dynamic viscosity: Accuracy # 26363. |
| Public Property | [FUNC\_ARTICLE\_ACCURACY\_FOR\_OPERATING\_VOLUME\_FLOW\_RATE](topic144.html) | Actual volume flow: Accuracy # 26361. |
| Public Property | [FUNC\_ARTICLE\_ACTIVE\_POWER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ACTIVE_POWER(Int32).html) | Active power # 26642. |
| Public Property | [FUNC\_ARTICLE\_ACTIVE\_POWER\_LOSS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ACTIVE_POWER_LOSS(Int32).html) | Active power loss # 26622. |
| Public Property | [FUNC\_ARTICLE\_ACTIVE\_POWER\_MAX\_ASV](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ACTIVE_POWER_MAX_ASV(Int32).html) | Active power (general power supply), max. # 26644. |
| Public Property | [FUNC\_ARTICLE\_ACTIVE\_POWER\_MAX\_NEA](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ACTIVE_POWER_MAX_NEA(Int32).html) | Active power (emergency power system), max. # 26646. |
| Public Property | [FUNC\_ARTICLE\_ACTIVE\_POWER\_MAX\_UPS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ACTIVE_POWER_MAX_UPS(Int32).html) | Active power (uninterruptible power supply), max. # 26648. |
| Public Property | [FUNC\_ARTICLE\_ACTUAL\_OUTPUT\_HYDRAULIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ACTUAL_OUTPUT_HYDRAULIC(Int32).html) | Actual power (hydraulic) # 26382. |
| Public Property | [FUNC\_ARTICLE\_ACTUAL\_OUTPUT\_HYDRAULIC\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ACTUAL_OUTPUT_HYDRAULIC_MAX(Int32).html) | Actual power (hydraulic), max. # 26384. |
| Public Property | [FUNC\_ARTICLE\_ACTUAL\_OUTPUT\_HYDRAULIC\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ACTUAL_OUTPUT_HYDRAULIC_MIN(Int32).html) | Actual power (hydraulic), min. # 26386. |
| Public Property | [FUNC\_ARTICLE\_ACTUAL\_OUTPUT\_PNEUMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ACTUAL_OUTPUT_PNEUMATIC(Int32).html) | Actual power (pneumatic) # 26388. |
| Public Property | [FUNC\_ARTICLE\_ACTUAL\_OUTPUT\_PNEUMATIC\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ACTUAL_OUTPUT_PNEUMATIC_MAX(Int32).html) | Actual power (pneumatic), max. # 26390. |
| Public Property | [FUNC\_ARTICLE\_ACTUAL\_POWER\_PNEUMATIC\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ACTUAL_POWER_PNEUMATIC_MIN(Int32).html) | Actual power (pneumatic), min. # 26392. |
| Public Property | [FUNC\_ARTICLE\_ADDITIONAL\_BOOLFIELD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ADDITIONAL_BOOLFIELD(Int32).html) | Supplementary field Yes / No # 20916. |
| Public Property | [FUNC\_ARTICLE\_ADDITIONAL\_TEXTFIELD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ADDITIONAL_TEXTFIELD(Int32).html) | Suppl. field: Text # 20915. |
| Public Property | [FUNC\_ARTICLE\_AML\_GUID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_AML_GUID(Int32).html) | AutomationML GUID (accessories) # 20399. |
| Public Property | [FUNC\_ARTICLE\_APPARENT\_POWER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_APPARENT_POWER(Int32).html) | Apparent power # 26550. |
| Public Property | [FUNC\_ARTICLE\_APPLICATION\_AREA\_OF\_THE\_CABLE](topic145.html) | Operating area: Cable # 26288. |
| Public Property | [FUNC\_ARTICLE\_APPLICATION\_RANGE\_OF\_THE\_CONNECTION\_CABLE](topic146.html) | Connecting cable: Application area # 26209. |
| Public Property | [FUNC\_ARTICLE\_ASSEMBLY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ASSEMBLY(Int32).html) | Assembly # 20905. |
| Public Property | [FUNC\_ARTICLE\_ASSEMBLY\_STRUCTURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ASSEMBLY_STRUCTURE(Int32).html) | Assembly structure # 20922. |
| Public Property | [FUNC\_ARTICLE\_ASSEMBLYVARIANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ASSEMBLYVARIANT(Int32).html) | Assembly variant # 20923. |
| Public Property | [FUNC\_ARTICLE\_ASSIGNMENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ASSIGNMENT(Int32).html) | Part allocation # 20904. |
| Public Property | [FUNC\_ARTICLE\_BACNET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_BACNET(Int32).html) | BACnet # 26228. |
| Public Property | [FUNC\_ARTICLE\_CABLE\_ENTRY\_INTO\_THE\_DEVICE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CABLE_ENTRY_INTO_THE_DEVICE(Int32).html) | Cable entry into device # 26396. |
| Public Property | [FUNC\_ARTICLE\_CABLE\_LENGTH\_LAID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CABLE_LENGTH_LAID(Int32).html) | Cable length, routed # 26398. |
| Public Property | [FUNC\_ARTICLE\_CABLE\_LENGTH\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CABLE_LENGTH_MAX(Int32).html) | Cable length, max. # 26399. |
| Public Property | [FUNC\_ARTICLE\_CABLE\_LEVEL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CABLE_LEVEL(Int32).html) | Cable: Voltage level # 26401. |
| Public Property | [FUNC\_ARTICLE\_CABLE\_PIPE\_TRANSMITTER\_CONNECTION](topic147.html) | Measuring transducer: Line connection (cable / pipe) # 26203. |
| Public Property | [FUNC\_ARTICLE\_CABLE\_WINDER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CABLE_WINDER(Int32).html) | Cable reel # 26394. |
| Public Property | [FUNC\_ARTICLE\_CAPACITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CAPACITY(Int32).html) | Volume capacity # 26323. |
| Public Property | [FUNC\_ARTICLE\_CHARACTER\_SET\_ACCORDING\_TO\_BACNET\_SPECIFICATION](topic148.html) | BACnet: Character set acc. to BACnet specification # 26652. |
| Public Property | [FUNC\_ARTICLE\_CHARACTERISTIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CHARACTERISTIC(Int32).html) | Characteristic curve # 26404. |
| Public Property | [FUNC\_ARTICLE\_CIRCUIT\_BREAKER\_TEST\_AVAILABLE](topic149.html) | Power circuit breaker - test available # 26434. |
| Public Property | [FUNC\_ARTICLE\_CLIMATE\_CLASS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CLIMATE_CLASS(Int32).html) | Climate class # 26408. |
| Public Property | [FUNC\_ARTICLE\_CLOSING\_PRESSURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CLOSING_PRESSURE(Int32).html) | Closing pressure # 26552. |
| Public Property | [FUNC\_ARTICLE\_CO2\_EMISSION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CO2_EMISSION(Int32).html) | CO2 emission # 26246. |
| Public Property | [FUNC\_ARTICLE\_COLLECTION\_VOLUME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_COLLECTION_VOLUME(Int32).html) | Retention volume # 26222. |
| Public Property | [FUNC\_ARTICLE\_CONNECTABLE\_CABLE\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CONNECTABLE_CABLE_TYPE(Int32).html) | Connectable cable type # 31179. |
| Public Property | [FUNC\_ARTICLE\_CONNECTION\_CABLE\_LENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CONNECTION_CABLE_LENGTH(Int32).html) | Connecting cable: Length # 26207. |
| Public Property | [FUNC\_ARTICLE\_CONNECTION\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CONNECTION_TYPE(Int32).html) | Connection point type # 26205. |
| Public Property | [FUNC\_ARTICLE\_CONNECTOR\_HOUSING\_OF\_CONNECTION\_1](topic150.html) | Plug-in connector housing (connection 1) # 26580. |
| Public Property | [FUNC\_ARTICLE\_CONNECTOR\_HOUSING\_OF\_THE\_CONNECTION\_2](topic151.html) | Plug-in connector housing (connection 2) # 26582. |
| Public Property | [FUNC\_ARTICLE\_CONSTRUCTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CONSTRUCTION(Int32).html) | Used drilling pattern # 20284. |
| Public Property | [FUNC\_ARTICLE\_COUNT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_COUNT(Int32).html) | Number of units / quantity # 20102. |
| Public Property | [FUNC\_ARTICLE\_CURRENT\_CONSUMPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CURRENT_CONSUMPTION(Int32).html) | Current consumption # 26596. |
| Public Property | [FUNC\_ARTICLE\_CURRENT\_CONSUMPTION\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CURRENT_CONSUMPTION_MAX(Int32).html) | Current consumption, max. # 26598. |
| Public Property | [FUNC\_ARTICLE\_DESCR1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_DESCR1(Int32).html) | Part: Designation 1 # 20193. |
| Public Property | [FUNC\_ARTICLE\_DESCR2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_DESCR2(Int32).html) | Part: Designation 2 # 20194. |
| Public Property | [FUNC\_ARTICLE\_DESCR3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_DESCR3(Int32).html) | Part: Designation 3 # 20203. |
| Public Property | [FUNC\_ARTICLE\_DEVICE\_PROFILE\_ACCORDING\_TO\_BACNET\_SPECIFICATION](topic152.html) | BACnet: Device profile according to BACnet specification # 26369. |
| Public Property | [FUNC\_ARTICLE\_DUTY\_CYCLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_DUTY_CYCLE(Int32).html) | Duty cycle # 26294. |
| Public Property | [FUNC\_ARTICLE\_EFFECTIVE\_DELIVERY\_RATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EFFECTIVE_DELIVERY_RATE(Int32).html) | Effective delivery amount # 26272. |
| Public Property | [FUNC\_ARTICLE\_EFFICIENCY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EFFICIENCY(Int32).html) | Efficiency # 26650. |
| Public Property | [FUNC\_ARTICLE\_END\_VALUE\_OF\_THE\_DYNAMIC\_VISCOSITY\_RANGE](topic153.html) | Dynamic viscosity range: End value # 26300. |
| Public Property | [FUNC\_ARTICLE\_ENERGY\_EFFICIENCY\_CLASS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS(Int32).html) | Energy efficiency class # 26302. |
| Public Property | [FUNC\_ARTICLE\_ENERGY\_EFFICIENCY\_CLASS\_CN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS_CN(Int32).html) | Energy efficiency class CN # 26306. |
| Public Property | [FUNC\_ARTICLE\_ENERGY\_EFFICIENCY\_CLASS\_MOTOR](topic154.html) | Energy efficiency class (motor) # 26304. |
| Public Property | [FUNC\_ARTICLE\_ENERGY\_EFFICIENCY\_CLASS\_US](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS_US(Int32).html) | Energy efficiency class US # 26308. |
| Public Property | [FUNC\_ARTICLE\_ERPNR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ERPNR(Int32).html) | ERP / PDM number 1 # 31117. |
| Public Property | [FUNC\_ARTICLE\_ERPNR\_10](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ERPNR_10(Int32).html) | ERP / PDM number 10 # 31175. |
| Public Property | [FUNC\_ARTICLE\_ERPNR\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ERPNR_2(Int32).html) | ERP / PDM number 2 # 31167. |
| Public Property | [FUNC\_ARTICLE\_ERPNR\_3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ERPNR_3(Int32).html) | ERP / PDM number 3 # 31168. |
| Public Property | [FUNC\_ARTICLE\_ERPNR\_4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ERPNR_4(Int32).html) | ERP / PDM number 4 # 31169. |
| Public Property | [FUNC\_ARTICLE\_ERPNR\_5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ERPNR_5(Int32).html) | ERP / PDM number 5 # 31170. |
| Public Property | [FUNC\_ARTICLE\_ERPNR\_6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ERPNR_6(Int32).html) | ERP / PDM number 6 # 31171. |
| Public Property | [FUNC\_ARTICLE\_ERPNR\_7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ERPNR_7(Int32).html) | ERP / PDM number 7 # 31172. |
| Public Property | [FUNC\_ARTICLE\_ERPNR\_8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ERPNR_8(Int32).html) | ERP / PDM number 8 # 31173. |
| Public Property | [FUNC\_ARTICLE\_ERPNR\_9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ERPNR_9(Int32).html) | ERP / PDM number 9 # 31174. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_1(Int32).html) | Part: External document 1 # 20190. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_10](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_10(Int32).html) | Part: External document 10 # 20269. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_11](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_11(Int32).html) | Part: External document 11 # 20270. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_12](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_12(Int32).html) | Part: External document 12 # 20271. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_13](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_13(Int32).html) | Part: External document 13 # 20272. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_14](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_14(Int32).html) | Part: External document 14 # 20273. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_15](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_15(Int32).html) | Part: External document 15 # 20274. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_16](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_16(Int32).html) | Part: External document 16 # 20275. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_17](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_17(Int32).html) | Part: External document 17 # 20276. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_18](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_18(Int32).html) | Part: External document 18 # 20277. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_19](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_19(Int32).html) | Part: External document 19 # 20278. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_2(Int32).html) | Part: External document 2 # 20191. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_20](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_20(Int32).html) | Part: External document 20 # 20279. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_3(Int32).html) | Part: External document 3 # 20192. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_4(Int32).html) | Part: External document 4 # 20263. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_5(Int32).html) | Part: External document 5 # 20264. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_6(Int32).html) | Part: External document 6 # 20265. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_7(Int32).html) | Part: External document 7 # 20266. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_8(Int32).html) | Part: External document 8 # 20267. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_9(Int32).html) | Part: External document 9 # 20268. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_PLACEMENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_PLACEMENT(Int32).html) | External placement # 20917. |
| Public Property | [FUNC\_ARTICLE\_FAN\_AIR\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_FAN_AIR_FLOW(Int32).html) | Blower air flow # 26354. |
| Public Property | [FUNC\_ARTICLE\_FILLING\_LEVEL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_FILLING_LEVEL(Int32).html) | Fill capacity # 26345. |
| Public Property | [FUNC\_ARTICLE\_FILLING\_VOLUME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_FILLING_VOLUME(Int32).html) | Fill volume # 26347. |
| Public Property | [FUNC\_ARTICLE\_FIRE\_PROTECTION\_PROPERTIES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_FIRE_PROTECTION_PROPERTIES(Int32).html) | Fire protection properties # 26244. |
| Public Property | [FUNC\_ARTICLE\_FITTING\_LENGTH\_OF\_THE\_PROTECTION\_TUBE](topic155.html) | Mounting length: Protective tube # 26278. |
| Public Property | [FUNC\_ARTICLE\_FLOW\_DIRECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_FLOW_DIRECTION(Int32).html) | Flow direction: Operating flow direction # 26268. |
| Public Property | [FUNC\_ARTICLE\_FLOW\_RATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_FLOW_RATE(Int32).html) | Flow rate # 26266. |
| Public Property | [FUNC\_ARTICLE\_FLOW\_RATE\_OPERATING\_NORMAL\_VOLUME\_FLOW](topic156.html) | Flow rate (operating / standard volume flow) # 26264. |
| Public Property | [FUNC\_ARTICLE\_FREQUENCY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_FREQUENCY(Int32).html) | Frequency # 26335. |
| Public Property | [FUNC\_ARTICLE\_FREQUENCY\_RANGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_FREQUENCY_RANGE(Int32).html) | Frequency range # 26343. |
| Public Property | [FUNC\_ARTICLE\_FREQUENCY\_RANGE\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_FREQUENCY_RANGE_MAX(Int32).html) | Frequency range, max. # 26331. |
| Public Property | [FUNC\_ARTICLE\_FREQUENCY\_RANGE\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_FREQUENCY_RANGE_MIN(Int32).html) | Frequency range, min. # 26333. |
| Public Property | [FUNC\_ARTICLE\_FREQUENCY\_SIGNAL\_PROCESSING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_FREQUENCY_SIGNAL_PROCESSING(Int32).html) | Frequency (signal processing) # 26337. |
| Public Property | [FUNC\_ARTICLE\_FREQUENCY\_SIGNAL\_PROCESSING\_SET](topic157.html) | Frequency (signal processing), set # 26339. |
| Public Property | [FUNC\_ARTICLE\_FUNCTIONGROUP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_FUNCTIONGROUP(Int32).html) | Function group # 20902. |
| Public Property | [FUNC\_ARTICLE\_FUNKTION\_IN\_RUHESTELLUNG](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_FUNKTION_IN_RUHESTELLUNG(Int32).html) | Function in rest position # 26349. |
| Public Property | [FUNC\_ARTICLE\_HARNESSPROD\_GUID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_HARNESSPROD_GUID(Int32).html) | Harness proD GUID # 20358. |
| Public Property | [FUNC\_ARTICLE\_INITIAL\_VALUE\_OF\_THE\_DYNAMIC\_VISCOSITY\_RANGE](topic158.html) | Dynamic viscosity range: Start value # 26189. |
| Public Property | [FUNC\_ARTICLE\_INPUT\_VOLTAGE\_FREQUENCY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_INPUT_VOLTAGE_FREQUENCY(Int32).html) | Frequency (input voltage) # 26341. |
| Public Property | [FUNC\_ARTICLE\_INPUT\_VOLUME\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_INPUT_VOLUME_FLOW(Int32).html) | Input flow rate # 26280. |
| Public Property | [FUNC\_ARTICLE\_INRUSH\_CURRENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_INRUSH_CURRENT(Int32).html) | Inrush current # 26296. |
| Public Property | [FUNC\_ARTICLE\_INSTALLATION\_LENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_INSTALLATION_LENGTH(Int32).html) | Mounting length # 26276. |
| Public Property | [FUNC\_ARTICLE\_INTAKE\_CAPACITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_INTAKE_CAPACITY(Int32).html) | Intake capacity # 26195. |
| Public Property | [FUNC\_ARTICLE\_INTAKE\_VOLUME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_INTAKE_VOLUME(Int32).html) | Intake volume # 26197. |
| Public Property | [FUNC\_ARTICLE\_INTAKE\_VOLUME\_FLOW\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_INTAKE_VOLUME_FLOW_MIN(Int32).html) | Intake flow rate, min. # 26201. |
| Public Property | [FUNC\_ARTICLE\_LABELLING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_LABELLING(Int32).html) | Identification # 26406. |
| Public Property | [FUNC\_ARTICLE\_LENGTH\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_LENGTH_MAX(Int32).html) | Length, max. # 26414. |
| Public Property | [FUNC\_ARTICLE\_LENGTH\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_LENGTH_MIN(Int32).html) | Length, min. # 26416. |
| Public Property | [FUNC\_ARTICLE\_LIFETIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_LIFETIME(Int32).html) | Service time # 20909. |
| Public Property | [FUNC\_ARTICLE\_LOCATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_LOCATION(Int32).html) | Operating location # 26292. |
| Public Property | [FUNC\_ARTICLE\_LV\_IDENTIFIER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_LV_IDENTIFIER(Int32).html) | Bill of quantities: Identifier # 26439. |
| Public Property | [FUNC\_ARTICLE\_MAINTENANCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_MAINTENANCE(Int32).html) | Lubrication / maintenance # 20912. |
| Public Property | [FUNC\_ARTICLE\_MAINTENANCE\_CYCLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_MAINTENANCE_CYCLE(Int32).html) | Maintenance cycle # 26638. |
| Public Property | [FUNC\_ARTICLE\_MAINTENANCE\_INTERVAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_MAINTENANCE_INTERVAL(Int32).html) | Maintenance interval # 26636. |
| Public Property | [FUNC\_ARTICLE\_MANUFACTURER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_MANUFACTURER(Int32).html) | Manufacturer # 20921. |
| Public Property | [FUNC\_ARTICLE\_MASS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_MASS(Int32).html) | Mass # 26441. |
| Public Property | [FUNC\_ARTICLE\_MASS\_MOMENT\_OF\_INERTIA\_OF\_THE\_LOAD](topic159.html) | Mass moment of inertia of the load # 26444. |
| Public Property | [FUNC\_ARTICLE\_MAX\_POWER\_CONSUMPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_MAX_POWER_CONSUMPTION(Int32).html) | Power consumption, max. # 26420. |
| Public Property | [FUNC\_ARTICLE\_MAX\_RATED\_CURRENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_MAX_RATED_CURRENT(Int32).html) | Nominal current, max. # 26501. |
| Public Property | [FUNC\_ARTICLE\_MAX\_RATED\_POWER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_MAX_RATED_POWER(Int32).html) | Nominal power (in kW), max. # 26479. |
| Public Property | [FUNC\_ARTICLE\_MEASURED\_VARIABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_MEASURED_VARIABLE(Int32).html) | Measurand # 26461. |
| Public Property | [FUNC\_ARTICLE\_MEASURING\_ACCURACY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_MEASURING_ACCURACY(Int32).html) | Measurement accuracy # 26459. |
| Public Property | [FUNC\_ARTICLE\_MOUNTING\_FORM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_MOUNTING_FORM(Int32).html) | Mounting configuration # 26274. |
| Public Property | [FUNC\_ARTICLE\_MOUNTINGSITE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_MOUNTINGSITE(Int32).html) | Part: Mounting surface # 20918. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_CURRENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_NOMINAL_CURRENT(Int32).html) | Nominal current # 26312. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_MOTOR\_POWER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_NOMINAL_MOTOR_POWER(Int32).html) | Motor nominal power # 26463. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_POWER\_CONSUMPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_NOMINAL_POWER_CONSUMPTION(Int32).html) | Nominal power consumption # 26483. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_POWER\_REQUIREMENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_NOMINAL_POWER_REQUIREMENT(Int32).html) | Nominal power requirement # 26485. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_PRESSURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_NOMINAL_PRESSURE(Int32).html) | Nominal pressure # 26471. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_PRESSURE\_RANGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_NOMINAL_PRESSURE_RANGE(Int32).html) | Pressure range # 26473. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_PRESSURE\_SERIES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_NOMINAL_PRESSURE_SERIES(Int32).html) | Nominal pressure series # 26310. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_VOLUME\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_NOMINAL_VOLUME_FLOW(Int32).html) | Nominal flow rate # 26507. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_VOLUME\_FLOW\_OF\_THE\_SUCTION\_SIDE](topic160.html) | Nominal flow rate (intake side) # 26509. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_VOLUMETRIC\_FLOW\_OF\_COMPRESSED\_AIR](topic161.html) | Nominal flow rate (compressed air) # 26511. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_WIDTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_NOMINAL_WIDTH(Int32).html) | Nominal size / diameter # 26513. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_WIDTH\_CONNECTION\_SIZE](topic162.html) | Nominal size / connection size # 26515. |
| Public Property | [FUNC\_ARTICLE\_NOTE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_NOTE(Int32).html) | Part description # 31014. |
| Public Property | [FUNC\_ARTICLE\_NUMBER\_OF\_BACNET\_I\_O\_OBJECTS](topic163.html) | BACnet: Number of I/O objects # 26213. |
| Public Property | [FUNC\_ARTICLE\_NUMBER\_OF\_HW\_INTERFACES\_BACNET](topic164.html) | BACnet: Number of hardware interfaces # 26215. |
| Public Property | [FUNC\_ARTICLE\_NUMBER\_OF\_INPUTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_NUMBER_OF_INPUTS(Int32).html) | Number of inputs # 26217. |
| Public Property | [FUNC\_ARTICLE\_NUMBER\_OF\_OUTPUTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_NUMBER_OF_OUTPUTS(Int32).html) | Number of outputs # 31177. |
| Public Property | [FUNC\_ARTICLE\_OPENING\_PRESSURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_OPENING_PRESSURE(Int32).html) | Opening pressure # 26523. |
| Public Property | [FUNC\_ARTICLE\_OPERATING\_TEMPERATURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_OPERATING_TEMPERATURE(Int32).html) | Operating temperature # 26238. |
| Public Property | [FUNC\_ARTICLE\_OPERATING\_TEMPERATURE\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_OPERATING_TEMPERATURE_MAX(Int32).html) | Operating temperature, max. # 26240. |
| Public Property | [FUNC\_ARTICLE\_OPERATING\_TEMPERATURE\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_OPERATING_TEMPERATURE_MIN(Int32).html) | Operating temperature, min. # 26242. |
| Public Property | [FUNC\_ARTICLE\_ORDERNR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ORDERNR(Int32).html) | Order number # 20919. |
| Public Property | [FUNC\_ARTICLE\_OUTPUT\_SPEED\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_OUTPUT_SPEED_MAX(Int32).html) | Output speed, max. # 26184. |
| Public Property | [FUNC\_ARTICLE\_OUTPUT\_SPEED\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_OUTPUT_SPEED_MIN(Int32).html) | Output speed, min. # 26186. |
| Public Property | [FUNC\_ARTICLE\_OVERLOAD\_CAPACITY\_OVERCURRENT](topic165.html) | Overload capability: Overcurrent # 26620. |
| Public Property | [FUNC\_ARTICLE\_PARTIAL\_LENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PARTIAL_LENGTH(Int32).html) | Subset / length # 31008. |
| Public Property | [FUNC\_ARTICLE\_PARTIAL\_LENGTH\_FULL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PARTIAL_LENGTH_FULL(Int32).html) | Subset / length (full) # 31091. |
| Public Property | [FUNC\_ARTICLE\_PARTIAL\_LENGTH\_IN\_PROJECT\_UNIT](topic166.html) | Subset / length in unit of project # 31040. |
| Public Property | [FUNC\_ARTICLE\_PARTIAL\_LENGTH\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PARTIAL_LENGTH_UNIT(Int32).html) | Unit for subset / length # 31012. |
| Public Property | [FUNC\_ARTICLE\_PARTIAL\_LENGTH\_VALUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PARTIAL_LENGTH_VALUE(Int32).html) | Subset / length: Value # 31010. |
| Public Property | [FUNC\_ARTICLE\_PARTIAL\_LENGTH\_WITH\_PROJECT\_UNIT](topic167.html) | Subset / length with unit of project # 31043. |
| Public Property | [FUNC\_ARTICLE\_PARTNR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PARTNR(Int32).html) | Part number # 20100. |
| Public Property | [FUNC\_ARTICLE\_PARTTYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PARTTYPE(Int32).html) | Record type # 20103. |
| Public Property | [FUNC\_ARTICLE\_PERFORMANCE\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PERFORMANCE_DESCRIPTION(Int32).html) | Performance description, standardized: Description (device, utility, service) # 26426. |
| Public Property | [FUNC\_ARTICLE\_PIECETYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PIECETYPE(Int32).html) | Part group # 20903. |
| Public Property | [FUNC\_ARTICLE\_PLUG\_CONNECTOR\_CONNECTION\_1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PLUG_CONNECTOR_CONNECTION_1(Int32).html) | Plug-in connector (connection 1) # 26576. |
| Public Property | [FUNC\_ARTICLE\_PLUG\_CONNECTOR\_CONNECTION\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PLUG_CONNECTOR_CONNECTION_2(Int32).html) | Plug-in connector (connection 2) # 26578. |
| Public Property | [FUNC\_ARTICLE\_POSITION\_KEYWORD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_POSITION_KEYWORD(Int32).html) | Performance description, standardized: Item keyword (device, utility, service) # 26537. |
| Public Property | [FUNC\_ARTICLE\_POSITION\_NUMBER\_MANUFACTURER](topic168.html) | Item number (manufacturer) # 26535. |
| Public Property | [FUNC\_ARTICLE\_POSITION\_NUMBER\_STLB](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_POSITION_NUMBER_STLB(Int32).html) | Performance description, standardized: Item number (device, utility, service) # 26533. |
| Public Property | [FUNC\_ARTICLE\_POSNR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_POSNR(Int32).html) | Item number # 20464. |
| Public Property | [FUNC\_ARTICLE\_POSSIBLE\_APPLICATIONS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_POSSIBLE_APPLICATIONS(Int32).html) | Possible uses # 26290. |
| Public Property | [FUNC\_ARTICLE\_POWER\_CONSUMPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_POWER_CONSUMPTION(Int32).html) | Power consumption # 26418. |
| Public Property | [FUNC\_ARTICLE\_POWER\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_POWER_DESCRIPTION(Int32).html) | Performance description (item, device) # 26428. |
| Public Property | [FUNC\_ARTICLE\_POWER\_GROUP\_ITEM\_NUMBER\_LGPOSNR](topic169.html) | Performance description, standardized: Performance group item number # 26432. |
| Public Property | [FUNC\_ARTICLE\_POWER\_REQUIREMENT\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_POWER_REQUIREMENT_MAX(Int32).html) | Power requirement, max. # 26422. |
| Public Property | [FUNC\_ARTICLE\_POWER\_REQUIREMENT\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_POWER_REQUIREMENT_MIN(Int32).html) | Power requirement, min. # 26424. |
| Public Property | [FUNC\_ARTICLE\_PRESSURE\_STAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PRESSURE_STAGE(Int32).html) | Pressure level # 26260. |
| Public Property | [FUNC\_ARTICLE\_PRODUCT\_FUNCTION\_WITH\_BACNET](topic170.html) | BACnet: Product function # 26539. |
| Public Property | [FUNC\_ARTICLE\_PROTECTION\_CLASS\_IP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PROTECTION_CLASS_IP(Int32).html) | Degree of protection (IP) # 26554. |
| Public Property | [FUNC\_ARTICLE\_PROTECTION\_CLASS\_IP\_FRONT\_SIDE](topic171.html) | Degree of protection (IP): Front side # 26560. |
| Public Property | [FUNC\_ARTICLE\_PROTECTION\_CLASS\_IP\_MOUNTED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PROTECTION_CLASS_IP_MOUNTED(Int32).html) | Degree of protection (IP): Mounted # 26562. |
| Public Property | [FUNC\_ARTICLE\_PROTECTION\_CLASS\_IP\_OF\_THE\_EVALUATION\_ELECTRONICS](topic172.html) | Degree of protection (IP): Evaluation electronics # 26556. |
| Public Property | [FUNC\_ARTICLE\_PROTECTION\_CLASS\_IP\_OF\_THE\_MEASURING\_HEAD](topic173.html) | Degree of protection (IP): Measuring head # 26558. |
| Public Property | [FUNC\_ARTICLE\_PROTECTION\_CLASS\_IP\_REAR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PROTECTION_CLASS_IP_REAR(Int32).html) | Degree of protection (IP): Rear side # 26564. |
| Public Property | [FUNC\_ARTICLE\_PROTECTION\_CLASS\_OF\_THE\_ELECTRIC\_MOTOR](topic174.html) | Protection type class (motor) # 26566. |
| Public Property | [FUNC\_ARTICLE\_PROTOCOL\_BACNET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PROTOCOL_BACNET(Int32).html) | BACnet: Protocol # 26541. |
| Public Property | [FUNC\_ARTICLE\_PROVISION\_OF\_THE\_CABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PROVISION_OF_THE_CABLE(Int32).html) | Provision of cable # 26233. |
| Public Property | [FUNC\_ARTICLE\_PROVISION\_OF\_THE\_CABLE\_GLAND](topic175.html) | Provision of cable gland # 26231. |
| Public Property | [FUNC\_ARTICLE\_PUMPING\_CAPACITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PUMPING_CAPACITY(Int32).html) | Transport capacity # 26325. |
| Public Property | [FUNC\_ARTICLE\_PUMPING\_CAPACITY\_OF\_THE\_OPERATING\_LIQUID](topic176.html) | Transport capacity of the operating fluid # 26327. |
| Public Property | [FUNC\_ARTICLE\_PUMPING\_VOLUME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PUMPING_VOLUME(Int32).html) | Transport volume # 26329. |
| Public Property | [FUNC\_ARTICLE\_QUANTITY\_IN\_PROJECT\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_QUANTITY_IN_PROJECT_UNIT(Int32).html) | Quantity / subset in unit of project # 31044. |
| Public Property | [FUNC\_ARTICLE\_RANGE\_OF\_APPLICATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RANGE_OF_APPLICATION(Int32).html) | Operating area # 26286. |
| Public Property | [FUNC\_ARTICLE\_RATED\_APPARENT\_POWER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RATED_APPARENT_POWER(Int32).html) | Rated apparent power # 26235. |
| Public Property | [FUNC\_ARTICLE\_RATED\_CURRENT\_CONSUMPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RATED_CURRENT_CONSUMPTION(Int32).html) | Nominal current consumption # 26505. |
| Public Property | [FUNC\_ARTICLE\_RATED\_CURRENT\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RATED_CURRENT_MIN(Int32).html) | Nominal current, min. # 26503. |
| Public Property | [FUNC\_ARTICLE\_RATED\_DRIVING\_TORQUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RATED_DRIVING_TORQUE(Int32).html) | Nominal drive torque # 26467. |
| Public Property | [FUNC\_ARTICLE\_RATED\_OUTPUT\_TORQUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RATED_OUTPUT_TORQUE(Int32).html) | Nominal output torque # 26465. |
| Public Property | [FUNC\_ARTICLE\_RATED\_POWER\_KW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RATED_POWER_KW(Int32).html) | Nominal power # 26475. |
| Public Property | [FUNC\_ARTICLE\_RATED\_POWER\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RATED_POWER_MIN(Int32).html) | Nominal power (in kW), min. # 26481. |
| Public Property | [FUNC\_ARTICLE\_RATED\_SPEED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RATED_SPEED(Int32).html) | Nominal rotation speed # 26469. |
| Public Property | [FUNC\_ARTICLE\_RATED\_VOLTAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RATED_VOLTAGE(Int32).html) | Nominal voltage # 26487. |
| Public Property | [FUNC\_ARTICLE\_RATED\_VOLTAGE\_FOR\_AC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RATED_VOLTAGE_FOR_AC(Int32).html) | Nominal voltage (AC) # 26491. |
| Public Property | [FUNC\_ARTICLE\_RATED\_VOLTAGE\_FOR\_AC\_50\_HZ](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RATED_VOLTAGE_FOR_AC_50_HZ(Int32).html) | Nominal voltage (AC 50 Hz) # 26489. |
| Public Property | [FUNC\_ARTICLE\_RATED\_VOLTAGE\_FOR\_DC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RATED_VOLTAGE_FOR_DC(Int32).html) | Nominal voltage (DC) # 26493. |
| Public Property | [FUNC\_ARTICLE\_RATED\_VOLTAGE\_OF\_THE\_CONTROL\_CIRCUIT](topic177.html) | Nominal voltage (control circuit) # 26497. |
| Public Property | [FUNC\_ARTICLE\_RATED\_VOLTAGE\_OF\_THE\_LOAD\_CIRCUIT](topic178.html) | Nominal voltage (load circuit) # 26495. |
| Public Property | [FUNC\_ARTICLE\_REPLACEMENT\_FOR\_PRODUCT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_REPLACEMENT_FOR_PRODUCT(Int32).html) | Replacement part: Original part # 26319. |
| Public Property | [FUNC\_ARTICLE\_RUN\_UP\_TIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RUN_UP_TIME(Int32).html) | Start-up time # 26314. |
| Public Property | [FUNC\_ARTICLE\_SECONDARY\_CASING\_PRESSURE\_STAGE](topic179.html) | Pressure level of secondary housing # 26262. |
| Public Property | [FUNC\_ARTICLE\_SERVICE\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_SERVICE_UNIT(Int32).html) | Performance unit (bill of quantities) # 26430. |
| Public Property | [FUNC\_ARTICLE\_SET\_POINT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_SET_POINT(Int32).html) | Setpoint # 26568. |
| Public Property | [FUNC\_ARTICLE\_SHOCK\_LOAD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_SHOCK_LOAD(Int32).html) | Shock load # 26585. |
| Public Property | [FUNC\_ARTICLE\_SPARE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_SPARE(Int32).html) | Spare part # 20907. |
| Public Property | [FUNC\_ARTICLE\_SPECIFIED\_MAXIMUM\_DRIVE\_TORQUE](topic180.html) | Drive torque (specified), max. # 26571. |
| Public Property | [FUNC\_ARTICLE\_SPECIFIED\_MINIMUM\_DRIVE\_TORQUE](topic181.html) | Drive torque (specified), min. # 26573. |
| Public Property | [FUNC\_ARTICLE\_SPEED\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_SPEED_MAX(Int32).html) | Rotation speed, max. # 26256. |
| Public Property | [FUNC\_ARTICLE\_SPEED\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_SPEED_MIN(Int32).html) | Rotation speed, min. # 26258. |
| Public Property | [FUNC\_ARTICLE\_STANDARD\_BACNET\_](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_STANDARD_BACNET_(Int32).html) | BACnet: Standard # 26517. |
| Public Property | [FUNC\_ARTICLE\_START\_UP\_TIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_START_UP_TIME(Int32).html) | Switch-on time # 26193. |
| Public Property | [FUNC\_ARTICLE\_STARTING\_CURRENT\_A](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_STARTING_CURRENT_A(Int32).html) | Starting current, max. # 26191. |
| Public Property | [FUNC\_ARTICLE\_STORAGE\_TRANSPORT\_AND\_PACKAGING\_REQUIREMENT](topic182.html) | Storage, transport and packaging (requirement) # 26410. |
| Public Property | [FUNC\_ARTICLE\_STRESS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_STRESS(Int32).html) | Stress # 20910. |
| Public Property | [FUNC\_ARTICLE\_STRIPPING\_LENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_STRIPPING_LENGTH(Int32).html) | Jacket (cable) stripping length # 31176. |
| Public Property | [FUNC\_ARTICLE\_SUCTION\_VOLUME\_FLOW\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_SUCTION_VOLUME_FLOW_MAX(Int32).html) | Intake flow rate, max. # 26199. |
| Public Property | [FUNC\_ARTICLE\_SUITABLE\_AS\_MONITOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_SUITABLE_AS_MONITOR(Int32).html) | Suitable as monitoring device # 26356. |
| Public Property | [FUNC\_ARTICLE\_SUITABLE\_FOR\_CABLE\_DIAMETERS](topic183.html) | Suitable for cable diameter # 26351. |
| Public Property | [FUNC\_ARTICLE\_SUITABLE\_FOR\_PROTECTION\_CLASS\_IP](topic184.html) | Suitable for degree of protection (IP) # 26359. |
| Public Property | [FUNC\_ARTICLE\_SUPPLIER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_SUPPLIER(Int32).html) | Supplier # 20920. |
| Public Property | [FUNC\_ARTICLE\_SUPPLIER\_BATCH\_NUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_SUPPLIER_BATCH_NUMBER(Int32).html) | Supplier batch number # 26436. |
| Public Property | [FUNC\_ARTICLE\_SUPPLY\_VOLTAGE\_RANGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_SUPPLY_VOLTAGE_RANGE(Int32).html) | Supply voltage range # 26624. |
| Public Property | [FUNC\_ARTICLE\_SUPPRESSINPARTSLIST](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_SUPPRESSINPARTSLIST(Int32).html) | Suppress in bill of materials (if filtered) # 20105. |
| Public Property | [FUNC\_ARTICLE\_SWITCHING\_CAPACITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_SWITCHING_CAPACITY(Int32).html) | Switching capacity # 26546. |
| Public Property | [FUNC\_ARTICLE\_TEMPERATUR\_MEDIUM\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_TEMPERATUR_MEDIUM_MAX(Int32).html) | Temperature (medium), max. # 26610. |
| Public Property | [FUNC\_ARTICLE\_TEMPERATUR\_MEDIUM\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_TEMPERATUR_MEDIUM_MIN(Int32).html) | Temperature (medium), min. # 26612. |
| Public Property | [FUNC\_ARTICLE\_TEMPERATURE\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_TEMPERATURE_MAX(Int32).html) | Temperature, max. # 26608. |
| Public Property | [FUNC\_ARTICLE\_TEMPERATURE\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_TEMPERATURE_MIN(Int32).html) | Temperature, min. # 26614. |
| Public Property | [FUNC\_ARTICLE\_TEMPERATURE\_RANGE\_MEDIUM\_MAX](topic185.html) | Temperature range (medium), max. # 26616. |
| Public Property | [FUNC\_ARTICLE\_TEMPERATURE\_RANGE\_MEDIUM\_MIN](topic186.html) | Temperature range (medium), min. # 26618. |
| Public Property | [FUNC\_ARTICLE\_THROUGHPUT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_THROUGHPUT(Int32).html) | Throughput # 26270. |
| Public Property | [FUNC\_ARTICLE\_TORQUE\_](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_TORQUE_(Int32).html) | Torque # 26248. |
| Public Property | [FUNC\_ARTICLE\_TORQUE\_AT\_MAX\_SPEED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_TORQUE_AT_MAX_SPEED(Int32).html) | Torque (at max. rotation speed) # 26250. |
| Public Property | [FUNC\_ARTICLE\_TORQUE\_AT\_MIN\_SPEED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_TORQUE_AT_MIN_SPEED(Int32).html) | Torque (at min. rotation speed) # 26252. |
| Public Property | [FUNC\_ARTICLE\_TORQUE\_MAX\_](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_TORQUE_MAX_(Int32).html) | Torque, max. # 26254. |
| Public Property | [FUNC\_ARTICLE\_TOTAL\_NUMBER\_OF\_BACNET\_OBJECTS](topic187.html) | BACnet: Total number of objects # 26211. |
| Public Property | [FUNC\_ARTICLE\_TYPE\_OF\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_TYPE_OF_FLOW(Int32).html) | Type of flow # 26220. |
| Public Property | [FUNC\_ARTICLE\_TYPE\_OF\_SWITCHING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_TYPE_OF_SWITCHING(Int32).html) | Circuit type # 26548. |
| Public Property | [FUNC\_ARTICLE\_TYPE\_OF\_USE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_TYPE_OF_USE(Int32).html) | Operating mode # 26284. |
| Public Property | [FUNC\_ARTICLE\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_UNIT(Int32).html) | Unit # 26282. |
| Public Property | [FUNC\_ARTICLE\_UNIT\_CLASS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_UNIT_CLASS(Int32).html) | Device class # 26367. |
| Public Property | [FUNC\_ARTICLE\_UNIT\_DESIGN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_UNIT_DESIGN(Int32).html) | Type of construction: Device # 26365. |
| Public Property | [FUNC\_ARTICLE\_UPPER\_PROCESS\_PRESSURE\_LIMIT\_ABSOLUTE\_PRESSURE](topic188.html) | Process pressure (absolute pressure), max. # 26519. |
| Public Property | [FUNC\_ARTICLE\_UPPER\_PROCESS\_PRESSURE\_LIMIT\_GAUGE\_PRESSURE](topic189.html) | Process pressure (overpressure), max. # 26521. |
| Public Property | [FUNC\_ARTICLE\_USAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_USAGE(Int32).html) | Procurement # 20911. |
| Public Property | [FUNC\_ARTICLE\_USE\_FOR\_MARKING\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_USE_FOR_MARKING_TYPE(Int32).html) | Usage for labeling type # 26626. |
| Public Property | [FUNC\_ARTICLE\_USED\_SAFETYRELATEDVALUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_USED_SAFETYRELATEDVALUE(Int32).html) | Safety-related values: Use case in use # 20307. |
| Public Property | [FUNC\_ARTICLE\_VARIANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_VARIANT(Int32).html) | Part variant # 20101. |
| Public Property | [FUNC\_ARTICLE\_VERSION\_AS\_MAINTENANCE\_REPAIR\_SWITCH](topic190.html) | Design as maintenance / repair switch # 31178. |
| Public Property | [FUNC\_ARTICLE\_VISCOSITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_VISCOSITY(Int32).html) | Viscosity # 26628. |
| Public Property | [FUNC\_ARTICLE\_VISCOSITY\_CLASS\_ACCORDING\_TO\_DIN\_51519](topic191.html) | Viscosity class (acc. to DIN 51519) # 26632. |
| Public Property | [FUNC\_ARTICLE\_VISCOSITY\_INDEX\_ACCORDING\_TO\_DIN\_ISO\_2909](topic192.html) | Viscosity index (acc. to DIN ISO 2909) # 26630. |
| Public Property | [FUNC\_ARTICLE\_VOLUME\_FLOW\_HEATING\_M3\_H](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_VOLUME_FLOW_HEATING_M3_H(Int32).html) | Flow rate # 26634. |
| Public Property | [FUNC\_ARTICLE\_WEAR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_WEAR(Int32).html) | Wearing part # 20908. |
| Public Property | [FUNC\_ARTICLE\_WEIGHT\_ITEM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_WEIGHT_ITEM(Int32).html) | Weight (part) # 26371. |
| Public Property | [FUNC\_ARTICLE\_WEIGHT\_KG\_1000\_M](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_WEIGHT_KG_1000_M(Int32).html) | Weight (in kg/1000 m) # 26375. |
| Public Property | [FUNC\_ARTICLE\_WEIGHT\_OF\_THE\_INDIVIDUAL\_ARTICLE\_PACKAGING](topic193.html) | Weight (individual packaging) # 26377. |
| Public Property | [FUNC\_ARTICLE\_WEIGHT\_OF\_THE\_PACKAGING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_WEIGHT_OF_THE_PACKAGING(Int32).html) | Weight (packaging) # 26379. |
| Public Property | [FUNC\_ARTICLE\_WEIGHT\_TOTAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_WEIGHT_TOTAL(Int32).html) | Total weight (part) # 26373. |
| Public Property | [FUNC\_ARTICLEREF\_PARTSLISTGROUP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLEREF_PARTSLISTGROUP(Int32).html) | Bill of materials group # 20924. |
| Public Property | [FUNC\_BLOCK\_VALUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_BLOCK_VALUE(Int32).html) | Block property # 20201. |
| Public Property | [FUNC\_CABLE\_DEVTAGINCLUDESSOURCEORDESTINATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_CABLE_DEVTAGINCLUDESSOURCEORDESTINATION().html) | Cable name includes source / target # 20069. |
| Public Property | [FUNC\_CANHAVEARTICLEDATA](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_CANHAVEARTICLEDATA().html) | Can have parts data # 20612. |
| Public Property | [FUNC\_CATEGORY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_CATEGORY().html) | Function definition: Category # 20115. |
| Public Property | [FUNC\_CATEGORY\_GROUP\_ID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_CATEGORY_GROUP_ID().html) | Function definition: Category / Group / Definition # 20188. |
| Public Property | [FUNC\_CATEGORY\_REGION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_CATEGORY_REGION().html) | Function definition: Area # 20088. |
| Public Property | [FUNC\_CIRCUITNUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_CIRCUITNUMBER().html) | Circuit number # 20317. |
| Public Property | [FUNC\_CODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_CODE().html) | DT: Identifier # 20013. |
| Public Property | [FUNC\_COMMENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_COMMENT().html) | Remark # 20045. |
| Public Property | [FUNC\_COMPONENTNUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_COMPONENTNUMBER().html) | Item number # 20318. |
| Public Property | [FUNC\_COMPONENTTYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_COMPONENTTYPE().html) | Function definition # 20026. |
| Public Property | [FUNC\_CONNECTIONDESTINATIONNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_CONNECTIONDESTINATIONNAME(Int32).html) | Name of target connection point # 20077. |
| Public Property | [FUNC\_COUNTER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_COUNTER().html) | DT: Counter # 20014. |
| Public Property | [FUNC\_CRAFT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_CRAFT().html) | Trade # 20466. |
| Public Property | [FUNC\_CRAFTCODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_CRAFTCODE().html) | Media code # 20316. |
| Public Property | [FUNC\_DESC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DESC().html) | Function definition: Description # 20117. |
| Public Property | [FUNC\_DEVICETAG\_FULL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DEVICETAG_FULL().html) | DT (full, without project structures) # 20009. |
| Public Property | [FUNC\_DEVICETAG\_FULL\_WITHSEPARATOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DEVICETAG_FULL_WITHSEPARATOR().html) | DT (full, without project structures, with preceding sign) # 20213. |
| Public Property | [FUNC\_DEVICETAG\_FULLNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DEVICETAG_FULLNAME().html) | Name (without project structures) # 20058. |
| Public Property | [FUNC\_DEVICETAG\_FULLNAME\_WITHSEPARATOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DEVICETAG_FULLNAME_WITHSEPARATOR().html) | Name (without project structures, with preceding sign) # 20214. |
| Public Property | [FUNC\_DEVICETAG\_MAIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DEVICETAG_MAIN().html) | DT (superior, without project structures) # 20003. |
| Public Property | [FUNC\_DEVICETAG\_MAIN\_WITHSEPARATOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DEVICETAG_MAIN_WITHSEPARATOR().html) | DT (superior, without project structures, with preceding sign) # 20211. |
| Public Property | [FUNC\_DEVICETAG\_MAINNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DEVICETAG_MAINNAME().html) | Superior product aspect incl. name supplement # 20335. |
| Public Property | [FUNC\_DEVICETAG\_NESTED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DEVICETAG_NESTED().html) | DT (subordinate, without project structures) # 20004. |
| Public Property | [FUNC\_DEVICETAG\_NESTED\_WITHSEPARATOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DEVICETAG_NESTED_WITHSEPARATOR().html) | DT (subordinate, without project structures, with preceding sign) # 20212. |
| Public Property | [FUNC\_DEVICETAG\_NESTEDNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DEVICETAG_NESTEDNAME().html) | Subordinate product aspect incl. name supplement # 20336. |
| Public Property | [FUNC\_DEVICETAG\_ONLYSTRUCTURES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DEVICETAG_ONLYSTRUCTURES().html) | DT (project structures only) # 20020. |
| Public Property | [FUNC\_DEVICETYPE\_MANUAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DEVICETYPE_MANUAL().html) | Device group # 20294. |
| Public Property | [FUNC\_DT\_COLUMN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT_COLUMN().html) | DT: Column # 20152. |
| Public Property | [FUNC\_DT\_FUNCTIONCODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT_FUNCTIONCODE().html) | DT: Application # 20155. |
| Public Property | [FUNC\_DT\_PAGECOUNTER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT_PAGECOUNTER().html) | DT: Page # 20150. |
| Public Property | [FUNC\_DT\_PAGESUBCOUNTER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT_PAGESUBCOUNTER().html) | DT: Subpage # 20151. |
| Public Property | [FUNC\_DT\_ROW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT_ROW().html) | DT: Row # 20153. |
| Public Property | [FUNC\_DT\_SECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT_SECTION().html) | DT: Section # 20154. |
| Public Property | [FUNC\_DT\_SUPPLEMENTARYFIELD01](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT_SUPPLEMENTARYFIELD01().html) | DT: Supplementary field 1 # 20156. |
| Public Property | [FUNC\_DT\_SUPPLEMENTARYFIELD02](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT_SUPPLEMENTARYFIELD02().html) | DT: Supplementary field 2 # 20157. |
| Public Property | [FUNC\_DT\_SUPPLEMENTARYFIELD03](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT_SUPPLEMENTARYFIELD03().html) | DT: Supplementary field 3 # 20158. |
| Public Property | [FUNC\_DT\_SUPPLEMENTARYFIELD04](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT_SUPPLEMENTARYFIELD04().html) | DT: Supplementary field 4 # 20159. |
| Public Property | [FUNC\_DT\_SUPPLEMENTARYFIELD05](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT_SUPPLEMENTARYFIELD05().html) | DT: Supplementary field 5 # 20160. |
| Public Property | [FUNC\_DT2\_COLUMN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT2_COLUMN().html) | DT (subordinate): Column # 20172. |
| Public Property | [FUNC\_DT2\_FUNCTIONCODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT2_FUNCTIONCODE().html) | DT (subordinate): Application # 20175. |
| Public Property | [FUNC\_DT2\_PAGECOUNTER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT2_PAGECOUNTER().html) | DT (subordinate): Page # 20170. |
| Public Property | [FUNC\_DT2\_PAGESUBCOUNTER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT2_PAGESUBCOUNTER().html) | DT (subordinate): Subpage # 20171. |
| Public Property | [FUNC\_DT2\_ROW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT2_ROW().html) | DT (subordinate): Row # 20173. |
| Public Property | [FUNC\_DT2\_SECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT2_SECTION().html) | DT (subordinate): Section # 20174. |
| Public Property | [FUNC\_DT2\_SUPPLEMENTARYFIELD01](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT2_SUPPLEMENTARYFIELD01().html) | DT (subordinate): Supplementary field 1 # 20176. |
| Public Property | [FUNC\_DT2\_SUPPLEMENTARYFIELD02](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT2_SUPPLEMENTARYFIELD02().html) | DT (subordinate): Supplementary field 2 # 20177. |
| Public Property | [FUNC\_DT2\_SUPPLEMENTARYFIELD03](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT2_SUPPLEMENTARYFIELD03().html) | DT (subordinate): Supplementary field 3 # 20178. |
| Public Property | [FUNC\_DT2\_SUPPLEMENTARYFIELD04](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT2_SUPPLEMENTARYFIELD04().html) | DT (subordinate): Supplementary field 4 # 20179. |
| Public Property | [FUNC\_DT2\_SUPPLEMENTARYFIELD05](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DT2_SUPPLEMENTARYFIELD05().html) | DT (subordinate): Supplementary field 5 # 20180. |
| Public Property | [FUNC\_FIXED\_DEVICE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_FIXED_DEVICE().html) | Device protection # 20475. |
| Public Property | [FUNC\_FULLCONNECTIONDESTINATIONNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_FULLCONNECTIONDESTINATIONNAME(Int32).html) | Name of target connection point (full) # 20048. |
| Public Property | [FUNC\_FULLDEVICETAG](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_FULLDEVICETAG().html) | DT (full) # 20006. |
| Public Property | [FUNC\_FULLNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_FULLNAME().html) | Name (full) # 20001. |
| Public Property | [FUNC\_GRAVINGTEXT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_GRAVINGTEXT().html) | Engraving text # 20025. |
| Public Property | [FUNC\_GROUP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_GROUP().html) | Function definition: Group # 20116. |
| Public Property | [FUNC\_IDENTDEVICETAG](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_IDENTDEVICETAG().html) | DT (identifying) # 20005. |
| Public Property | [FUNC\_IDENTDEVICETAGPARTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_IDENTDEVICETAGPARTS().html) | Identifying DT elements # 20096. |
| Public Property | [FUNC\_IDENTDEVICETAGWITHOUTSTRUCTURES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_IDENTDEVICETAGWITHOUTSTRUCTURES().html) | DT (identifying, without project structures) # 20008. |
| Public Property | [FUNC\_IDENTDEVICETAGWITHOUTSTRUCTURES\_WITHSEPARATOR](topic194.html) | DT (identifying, without project structures, with preceding sign) # 20215. |
| Public Property | [FUNC\_IDENTNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_IDENTNAME().html) | Name (identifying) # 20000. |
| Public Property | [FUNC\_IDENTNAMEPARTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_IDENTNAMEPARTS().html) | Identifying name elements # 20095. |
| Public Property | [FUNC\_ISPLACEDIN\_CIRCUIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ISPLACEDIN_CIRCUIT().html) | Function exists with 'Multi-line' representation type # 20470. |
| Public Property | [FUNC\_ISPLACEDIN\_OVERVIEW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ISPLACEDIN_OVERVIEW().html) | Function exists with 'Overview' representation type # 20473. |
| Public Property | [FUNC\_ISPLACEDIN\_PAIRCROSSREFERENCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ISPLACEDIN_PAIRCROSSREFERENCE().html) | Function exists with 'Pair cross-reference' representation type # 20472. |
| Public Property | [FUNC\_ISPLACEDIN\_PROCESSANDINSTDIAGRAM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ISPLACEDIN_PROCESSANDINSTDIAGRAM().html) | Function exists with 'P&I diagram' representation type # 20474. |
| Public Property | [FUNC\_ISPLACEDIN\_SINGLELINE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ISPLACEDIN_SINGLELINE().html) | Function exists with 'Single-line' representation type # 20471. |
| Public Property | [FUNC\_MACRO](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_MACRO().html) | Macro # 20468. |
| Public Property | [FUNC\_MODULE\_ID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_MODULE_ID().html) | DT ID # 20359. |
| Public Property | [FUNC\_NESTEDCODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_NESTEDCODE().html) | DT (subordinate): Identifier # 20017. |
| Public Property | [FUNC\_NESTEDCOUNTER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_NESTEDCOUNTER().html) | DT (subordinate):Counter # 20018. |
| Public Property | [FUNC\_NESTEDPREFIX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_NESTEDPREFIX().html) | DT (subordinate): Prefix # 20016. |
| Public Property | [FUNC\_NESTEDSUFFIX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_NESTEDSUFFIX().html) | DT (subordinate): Subcounter # 20019. |
| Public Property | [FUNC\_PREFIX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_PREFIX().html) | DT: Prefix # 20012. |
| Public Property | [FUNC\_SINGLE\_LINE\_FUNCTION\_COUNT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_SINGLE_LINE_FUNCTION_COUNT().html) | Number of functions # 20110. |
| Public Property | [FUNC\_SUBCRAFT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_SUBCRAFT().html) | Subtrade # 20467. |
| Public Property | [FUNC\_SUFFIX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_SUFFIX().html) | DT: Subcounter # 20015. |
| Public Property | [FUNC\_SUPPLEMENTARYFIELD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_SUPPLEMENTARYFIELD(Int32).html) | Supplementary field # 20901. |
| Public Property | [FUNC\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_TYPE().html) | Representation type # 20121. |
| Public Property | [FUNC\_TYPENOTATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_TYPENOTATION(Int32).html) | Type designation of part # 20200. |
| Public Property | [FUNCTION\_MESSAGETEXT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNCTION_MESSAGETEXT().html) | Message text # 20185. |
| Public Property | [FUNCTION\_PLCIMPORTCOMPARE\_MARKEDTOBEDELETED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNCTION_PLCIMPORTCOMPARE_MARKEDTOBEDELETED().html) | Marked for deletion # 20186. |
| Public Property | [FUNCTION\_TEMPLATE\_COMBINATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNCTION_TEMPLATE_COMBINATION().html) | Function template: Template group (multi-line) # 20429. |
| Public Property | [FUNCTION\_TEMPLATE\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNCTION_TEMPLATE_DESCRIPTION().html) | Function template: Description # 20389. |
| Public Property | [HARNESS\_CABLEUNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~HARNESS_CABLEUNIT().html) | Cable unit name # 31162. |
| Public Property | [HARNESS\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~HARNESS_NAME().html) | Wire harness name # 31143. |
| Public Property | [INSTANCE\_FULLPLACEMENTLOCATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~INSTANCE_FULLPLACEMENTLOCATION().html) | Placement # 19007. |
| Public Property | [INSTANCE\_REVISIONID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~INSTANCE_REVISIONID().html) | Revision change marker (from property comparison) # 10153. |
| Public Property | [INSTANCE\_REVISIONMARKER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~INSTANCE_REVISIONMARKER().html) | Revision marker (from property comparison) # 10152. |
| Public Property | [INSTANCE\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~INSTANCE_TYPE().html) | Representation type / report type # 19021. |
| Public Property | [INTRINSICSAFETY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~INTRINSICSAFETY().html) | Intrinsically safe # 31030. |
| Public Property | [MESSAGEMGMT\_MESSAGES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~MESSAGEMGMT_MESSAGES().html) | Check run messages available # 20930. |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [POTENTIAL\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~POTENTIAL_NAME().html) | Name of potential # 33000. |
| Public Property | [POTENTIAL\_NETNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~POTENTIAL_NETNAME().html) | Net name # 33007. |
| Public Property | [POTENTIAL\_PARENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~POTENTIAL_PARENT().html) | Superior potential # 33001. |
| Public Property | [POTENTIAL\_SIGNAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~POTENTIAL_SIGNAL().html) | Signal name # 33006. |
| Public Property | [POTENTIAL\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~POTENTIAL_TYPE().html) | Potential type # 31006. |
| Public Property | [POTENTIAL\_VALUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~POTENTIAL_VALUE().html) | Potential value # 33003. |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |
| Public Property | [STRANDCONNECTOR\_DESIGNATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~STRANDCONNECTOR_DESIGNATION().html) | Bundle: Connection point designation # 19070. |
| Public Property | [SUBPROJECT\_NUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~SUBPROJECT_NUMBER().html) | Subproject number # 25101. |
| Public Property | [WRITEPROTECTED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~WRITEPROTECTED().html) | Change protection # 3014. |
| Public Property | [WRITEPROTECTED\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~WRITEPROTECTED_AUTOMATIC().html) | Change protection (hierarchical) # 3015. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of ConnectionPropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |


