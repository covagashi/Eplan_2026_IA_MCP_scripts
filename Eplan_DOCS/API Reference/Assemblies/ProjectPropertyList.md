# ProjectPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList.html

---

This class represents collection of properties of [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) class. Please check also base classes for other properties which are available for [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) objects: [StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         **Eplan.EplApi.DataModel.ProjectPropertyList**

Syntax

**C#**



[DefaultMember("Property")]

public class ProjectPropertyList : StorableObjectPropertyList

[DefaultMember("Property")]

public ref class ProjectPropertyList : public StorableObjectPropertyList


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
| Public Constructor | [ProjectPropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AUTOMATIONML\_OBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~AUTOMATIONML_OBJECTID().html) | AutomationML GUID # 25030. |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [FUNC\_ARTICLE\_ABSORPTION\_VOLUME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ABSORPTION_VOLUME(Int32).html) | Reception volume # 26224. |
| Public Property | [FUNC\_ARTICLE\_ACCURACY\_FOR\_DYNAMIC\_VISCOSITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ACCURACY_FOR_DYNAMIC_VISCOSITY(Int32).html) | Dynamic viscosity: Accuracy # 26363. |
| Public Property | [FUNC\_ARTICLE\_ACCURACY\_FOR\_OPERATING\_VOLUME\_FLOW\_RATE](topic428.html) | Actual volume flow: Accuracy # 26361. |
| Public Property | [FUNC\_ARTICLE\_ACTIVE\_POWER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ACTIVE_POWER(Int32).html) | Active power # 26642. |
| Public Property | [FUNC\_ARTICLE\_ACTIVE\_POWER\_LOSS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ACTIVE_POWER_LOSS(Int32).html) | Active power loss # 26622. |
| Public Property | [FUNC\_ARTICLE\_ACTIVE\_POWER\_MAX\_ASV](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ACTIVE_POWER_MAX_ASV(Int32).html) | Active power (general power supply), max. # 26644. |
| Public Property | [FUNC\_ARTICLE\_ACTIVE\_POWER\_MAX\_NEA](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ACTIVE_POWER_MAX_NEA(Int32).html) | Active power (emergency power system), max. # 26646. |
| Public Property | [FUNC\_ARTICLE\_ACTIVE\_POWER\_MAX\_UPS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ACTIVE_POWER_MAX_UPS(Int32).html) | Active power (uninterruptible power supply), max. # 26648. |
| Public Property | [FUNC\_ARTICLE\_ACTUAL\_OUTPUT\_HYDRAULIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ACTUAL_OUTPUT_HYDRAULIC(Int32).html) | Actual power (hydraulic) # 26382. |
| Public Property | [FUNC\_ARTICLE\_ACTUAL\_OUTPUT\_HYDRAULIC\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ACTUAL_OUTPUT_HYDRAULIC_MAX(Int32).html) | Actual power (hydraulic), max. # 26384. |
| Public Property | [FUNC\_ARTICLE\_ACTUAL\_OUTPUT\_HYDRAULIC\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ACTUAL_OUTPUT_HYDRAULIC_MIN(Int32).html) | Actual power (hydraulic), min. # 26386. |
| Public Property | [FUNC\_ARTICLE\_ACTUAL\_OUTPUT\_PNEUMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ACTUAL_OUTPUT_PNEUMATIC(Int32).html) | Actual power (pneumatic) # 26388. |
| Public Property | [FUNC\_ARTICLE\_ACTUAL\_OUTPUT\_PNEUMATIC\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ACTUAL_OUTPUT_PNEUMATIC_MAX(Int32).html) | Actual power (pneumatic), max. # 26390. |
| Public Property | [FUNC\_ARTICLE\_ACTUAL\_POWER\_PNEUMATIC\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ACTUAL_POWER_PNEUMATIC_MIN(Int32).html) | Actual power (pneumatic), min. # 26392. |
| Public Property | [FUNC\_ARTICLE\_ADDITIONAL\_BOOLFIELD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ADDITIONAL_BOOLFIELD(Int32).html) | Supplementary field Yes / No # 20916. |
| Public Property | [FUNC\_ARTICLE\_ADDITIONAL\_TEXTFIELD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ADDITIONAL_TEXTFIELD(Int32).html) | Suppl. field: Text # 20915. |
| Public Property | [FUNC\_ARTICLE\_APPARENT\_POWER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_APPARENT_POWER(Int32).html) | Apparent power # 26550. |
| Public Property | [FUNC\_ARTICLE\_APPLICATION\_AREA\_OF\_THE\_CABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_APPLICATION_AREA_OF_THE_CABLE(Int32).html) | Operating area: Cable # 26288. |
| Public Property | [FUNC\_ARTICLE\_APPLICATION\_RANGE\_OF\_THE\_CONNECTION\_CABLE](topic429.html) | Connecting cable: Application area # 26209. |
| Public Property | [FUNC\_ARTICLE\_ASSEMBLY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ASSEMBLY(Int32).html) | Assembly # 20905. |
| Public Property | [FUNC\_ARTICLE\_ASSEMBLY\_STRUCTURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ASSEMBLY_STRUCTURE(Int32).html) | Assembly structure # 20922. |
| Public Property | [FUNC\_ARTICLE\_ASSEMBLYVARIANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ASSEMBLYVARIANT(Int32).html) | Assembly variant # 20923. |
| Public Property | [FUNC\_ARTICLE\_ASSIGNMENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ASSIGNMENT(Int32).html) | Part allocation # 20904. |
| Public Property | [FUNC\_ARTICLE\_BACNET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_BACNET(Int32).html) | BACnet # 26228. |
| Public Property | [FUNC\_ARTICLE\_CABLE\_ENTRY\_INTO\_THE\_DEVICE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CABLE_ENTRY_INTO_THE_DEVICE(Int32).html) | Cable entry into device # 26396. |
| Public Property | [FUNC\_ARTICLE\_CABLE\_LENGTH\_LAID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CABLE_LENGTH_LAID(Int32).html) | Cable length, routed # 26398. |
| Public Property | [FUNC\_ARTICLE\_CABLE\_LENGTH\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CABLE_LENGTH_MAX(Int32).html) | Cable length, max. # 26399. |
| Public Property | [FUNC\_ARTICLE\_CABLE\_LEVEL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CABLE_LEVEL(Int32).html) | Cable: Voltage level # 26401. |
| Public Property | [FUNC\_ARTICLE\_CABLE\_PIPE\_TRANSMITTER\_CONNECTION](topic430.html) | Measuring transducer: Line connection (cable / pipe) # 26203. |
| Public Property | [FUNC\_ARTICLE\_CABLE\_WINDER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CABLE_WINDER(Int32).html) | Cable reel # 26394. |
| Public Property | [FUNC\_ARTICLE\_CAPACITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CAPACITY(Int32).html) | Volume capacity # 26323. |
| Public Property | [FUNC\_ARTICLE\_CHARACTER\_SET\_ACCORDING\_TO\_BACNET\_SPECIFICATION](topic431.html) | BACnet: Character set acc. to BACnet specification # 26652. |
| Public Property | [FUNC\_ARTICLE\_CHARACTERISTIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CHARACTERISTIC(Int32).html) | Characteristic curve # 26404. |
| Public Property | [FUNC\_ARTICLE\_CIRCUIT\_BREAKER\_TEST\_AVAILABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CIRCUIT_BREAKER_TEST_AVAILABLE(Int32).html) | Power circuit breaker - test available # 26434. |
| Public Property | [FUNC\_ARTICLE\_CLIMATE\_CLASS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CLIMATE_CLASS(Int32).html) | Climate class # 26408. |
| Public Property | [FUNC\_ARTICLE\_CLOSING\_PRESSURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CLOSING_PRESSURE(Int32).html) | Closing pressure # 26552. |
| Public Property | [FUNC\_ARTICLE\_CO2\_EMISSION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CO2_EMISSION(Int32).html) | CO2 emission # 26246. |
| Public Property | [FUNC\_ARTICLE\_COLLECTION\_VOLUME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_COLLECTION_VOLUME(Int32).html) | Retention volume # 26222. |
| Public Property | [FUNC\_ARTICLE\_CONNECTABLE\_CABLE\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CONNECTABLE_CABLE_TYPE(Int32).html) | Connectable cable type # 31179. |
| Public Property | [FUNC\_ARTICLE\_CONNECTION\_CABLE\_LENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CONNECTION_CABLE_LENGTH(Int32).html) | Connecting cable: Length # 26207. |
| Public Property | [FUNC\_ARTICLE\_CONNECTION\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CONNECTION_TYPE(Int32).html) | Connection point type # 26205. |
| Public Property | [FUNC\_ARTICLE\_CONNECTOR\_HOUSING\_OF\_CONNECTION\_1](topic432.html) | Plug-in connector housing (connection 1) # 26580. |
| Public Property | [FUNC\_ARTICLE\_CONNECTOR\_HOUSING\_OF\_THE\_CONNECTION\_2](topic433.html) | Plug-in connector housing (connection 2) # 26582. |
| Public Property | [FUNC\_ARTICLE\_CONSTRUCTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CONSTRUCTION(Int32).html) | Used drilling pattern # 20284. |
| Public Property | [FUNC\_ARTICLE\_COUNT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_COUNT(Int32).html) | Number of units / quantity # 20102. |
| Public Property | [FUNC\_ARTICLE\_CURRENT\_CONSUMPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CURRENT_CONSUMPTION(Int32).html) | Current consumption # 26596. |
| Public Property | [FUNC\_ARTICLE\_CURRENT\_CONSUMPTION\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CURRENT_CONSUMPTION_MAX(Int32).html) | Current consumption, max. # 26598. |
| Public Property | [FUNC\_ARTICLE\_DESCR1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_DESCR1(Int32).html) | Part: Designation 1 # 20193. |
| Public Property | [FUNC\_ARTICLE\_DESCR2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_DESCR2(Int32).html) | Part: Designation 2 # 20194. |
| Public Property | [FUNC\_ARTICLE\_DESCR3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_DESCR3(Int32).html) | Part: Designation 3 # 20203. |
| Public Property | [FUNC\_ARTICLE\_DEVICE\_PROFILE\_ACCORDING\_TO\_BACNET\_SPECIFICATION](topic434.html) | BACnet: Device profile according to BACnet specification # 26369. |
| Public Property | [FUNC\_ARTICLE\_DUTY\_CYCLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_DUTY_CYCLE(Int32).html) | Duty cycle # 26294. |
| Public Property | [FUNC\_ARTICLE\_EFFECTIVE\_DELIVERY\_RATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EFFECTIVE_DELIVERY_RATE(Int32).html) | Effective delivery amount # 26272. |
| Public Property | [FUNC\_ARTICLE\_EFFICIENCY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EFFICIENCY(Int32).html) | Efficiency # 26650. |
| Public Property | [FUNC\_ARTICLE\_END\_VALUE\_OF\_THE\_DYNAMIC\_VISCOSITY\_RANGE](topic435.html) | Dynamic viscosity range: End value # 26300. |
| Public Property | [FUNC\_ARTICLE\_ENERGY\_EFFICIENCY\_CLASS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS(Int32).html) | Energy efficiency class # 26302. |
| Public Property | [FUNC\_ARTICLE\_ENERGY\_EFFICIENCY\_CLASS\_CN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS_CN(Int32).html) | Energy efficiency class CN # 26306. |
| Public Property | [FUNC\_ARTICLE\_ENERGY\_EFFICIENCY\_CLASS\_MOTOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS_MOTOR(Int32).html) | Energy efficiency class (motor) # 26304. |
| Public Property | [FUNC\_ARTICLE\_ENERGY\_EFFICIENCY\_CLASS\_US](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS_US(Int32).html) | Energy efficiency class US # 26308. |
| Public Property | [FUNC\_ARTICLE\_ERPNR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ERPNR(Int32).html) | ERP / PDM number 1 # 31117. |
| Public Property | [FUNC\_ARTICLE\_ERPNR\_10](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ERPNR_10(Int32).html) | ERP / PDM number 10 # 31175. |
| Public Property | [FUNC\_ARTICLE\_ERPNR\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ERPNR_2(Int32).html) | ERP / PDM number 2 # 31167. |
| Public Property | [FUNC\_ARTICLE\_ERPNR\_3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ERPNR_3(Int32).html) | ERP / PDM number 3 # 31168. |
| Public Property | [FUNC\_ARTICLE\_ERPNR\_4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ERPNR_4(Int32).html) | ERP / PDM number 4 # 31169. |
| Public Property | [FUNC\_ARTICLE\_ERPNR\_5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ERPNR_5(Int32).html) | ERP / PDM number 5 # 31170. |
| Public Property | [FUNC\_ARTICLE\_ERPNR\_6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ERPNR_6(Int32).html) | ERP / PDM number 6 # 31171. |
| Public Property | [FUNC\_ARTICLE\_ERPNR\_7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ERPNR_7(Int32).html) | ERP / PDM number 7 # 31172. |
| Public Property | [FUNC\_ARTICLE\_ERPNR\_8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ERPNR_8(Int32).html) | ERP / PDM number 8 # 31173. |
| Public Property | [FUNC\_ARTICLE\_ERPNR\_9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ERPNR_9(Int32).html) | ERP / PDM number 9 # 31174. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_1(Int32).html) | Part: External document 1 # 20190. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_10](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_10(Int32).html) | Part: External document 10 # 20269. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_11](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_11(Int32).html) | Part: External document 11 # 20270. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_12](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_12(Int32).html) | Part: External document 12 # 20271. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_13](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_13(Int32).html) | Part: External document 13 # 20272. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_14](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_14(Int32).html) | Part: External document 14 # 20273. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_15](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_15(Int32).html) | Part: External document 15 # 20274. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_16](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_16(Int32).html) | Part: External document 16 # 20275. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_17](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_17(Int32).html) | Part: External document 17 # 20276. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_18](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_18(Int32).html) | Part: External document 18 # 20277. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_19](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_19(Int32).html) | Part: External document 19 # 20278. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_2(Int32).html) | Part: External document 2 # 20191. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_20](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_20(Int32).html) | Part: External document 20 # 20279. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_3(Int32).html) | Part: External document 3 # 20192. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_4(Int32).html) | Part: External document 4 # 20263. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_5(Int32).html) | Part: External document 5 # 20264. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_6(Int32).html) | Part: External document 6 # 20265. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_7(Int32).html) | Part: External document 7 # 20266. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_8(Int32).html) | Part: External document 8 # 20267. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_DOCUMENT\_9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_DOCUMENT_9(Int32).html) | Part: External document 9 # 20268. |
| Public Property | [FUNC\_ARTICLE\_EXTERNAL\_PLACEMENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_EXTERNAL_PLACEMENT(Int32).html) | External placement # 20917. |
| Public Property | [FUNC\_ARTICLE\_FAN\_AIR\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_FAN_AIR_FLOW(Int32).html) | Blower air flow # 26354. |
| Public Property | [FUNC\_ARTICLE\_FILLING\_LEVEL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_FILLING_LEVEL(Int32).html) | Fill capacity # 26345. |
| Public Property | [FUNC\_ARTICLE\_FILLING\_VOLUME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_FILLING_VOLUME(Int32).html) | Fill volume # 26347. |
| Public Property | [FUNC\_ARTICLE\_FIRE\_PROTECTION\_PROPERTIES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_FIRE_PROTECTION_PROPERTIES(Int32).html) | Fire protection properties # 26244. |
| Public Property | [FUNC\_ARTICLE\_FITTING\_LENGTH\_OF\_THE\_PROTECTION\_TUBE](topic436.html) | Mounting length: Protective tube # 26278. |
| Public Property | [FUNC\_ARTICLE\_FLOW\_DIRECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_FLOW_DIRECTION(Int32).html) | Flow direction: Operating flow direction # 26268. |
| Public Property | [FUNC\_ARTICLE\_FLOW\_RATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_FLOW_RATE(Int32).html) | Flow rate # 26266. |
| Public Property | [FUNC\_ARTICLE\_FLOW\_RATE\_OPERATING\_NORMAL\_VOLUME\_FLOW](topic437.html) | Flow rate (operating / standard volume flow) # 26264. |
| Public Property | [FUNC\_ARTICLE\_FREQUENCY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_FREQUENCY(Int32).html) | Frequency # 26335. |
| Public Property | [FUNC\_ARTICLE\_FREQUENCY\_RANGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_FREQUENCY_RANGE(Int32).html) | Frequency range # 26343. |
| Public Property | [FUNC\_ARTICLE\_FREQUENCY\_RANGE\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_FREQUENCY_RANGE_MAX(Int32).html) | Frequency range, max. # 26331. |
| Public Property | [FUNC\_ARTICLE\_FREQUENCY\_RANGE\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_FREQUENCY_RANGE_MIN(Int32).html) | Frequency range, min. # 26333. |
| Public Property | [FUNC\_ARTICLE\_FREQUENCY\_SIGNAL\_PROCESSING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_FREQUENCY_SIGNAL_PROCESSING(Int32).html) | Frequency (signal processing) # 26337. |
| Public Property | [FUNC\_ARTICLE\_FREQUENCY\_SIGNAL\_PROCESSING\_SET](topic438.html) | Frequency (signal processing), set # 26339. |
| Public Property | [FUNC\_ARTICLE\_FUNCTIONGROUP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_FUNCTIONGROUP(Int32).html) | Function group # 20902. |
| Public Property | [FUNC\_ARTICLE\_FUNKTION\_IN\_RUHESTELLUNG](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_FUNKTION_IN_RUHESTELLUNG(Int32).html) | Function in rest position # 26349. |
| Public Property | [FUNC\_ARTICLE\_INITIAL\_VALUE\_OF\_THE\_DYNAMIC\_VISCOSITY\_RANGE](topic439.html) | Dynamic viscosity range: Start value # 26189. |
| Public Property | [FUNC\_ARTICLE\_INPUT\_VOLTAGE\_FREQUENCY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_INPUT_VOLTAGE_FREQUENCY(Int32).html) | Frequency (input voltage) # 26341. |
| Public Property | [FUNC\_ARTICLE\_INPUT\_VOLUME\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_INPUT_VOLUME_FLOW(Int32).html) | Input flow rate # 26280. |
| Public Property | [FUNC\_ARTICLE\_INRUSH\_CURRENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_INRUSH_CURRENT(Int32).html) | Inrush current # 26296. |
| Public Property | [FUNC\_ARTICLE\_INSTALLATION\_LENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_INSTALLATION_LENGTH(Int32).html) | Mounting length # 26276. |
| Public Property | [FUNC\_ARTICLE\_INTAKE\_CAPACITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_INTAKE_CAPACITY(Int32).html) | Intake capacity # 26195. |
| Public Property | [FUNC\_ARTICLE\_INTAKE\_VOLUME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_INTAKE_VOLUME(Int32).html) | Intake volume # 26197. |
| Public Property | [FUNC\_ARTICLE\_INTAKE\_VOLUME\_FLOW\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_INTAKE_VOLUME_FLOW_MIN(Int32).html) | Intake flow rate, min. # 26201. |
| Public Property | [FUNC\_ARTICLE\_LABELLING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_LABELLING(Int32).html) | Identification # 26406. |
| Public Property | [FUNC\_ARTICLE\_LENGTH\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_LENGTH_MAX(Int32).html) | Length, max. # 26414. |
| Public Property | [FUNC\_ARTICLE\_LENGTH\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_LENGTH_MIN(Int32).html) | Length, min. # 26416. |
| Public Property | [FUNC\_ARTICLE\_LIFETIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_LIFETIME(Int32).html) | Service time # 20909. |
| Public Property | [FUNC\_ARTICLE\_LOCATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_LOCATION(Int32).html) | Operating location # 26292. |
| Public Property | [FUNC\_ARTICLE\_LV\_IDENTIFIER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_LV_IDENTIFIER(Int32).html) | Bill of quantities: Identifier # 26439. |
| Public Property | [FUNC\_ARTICLE\_MAINTENANCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_MAINTENANCE(Int32).html) | Lubrication / maintenance # 20912. |
| Public Property | [FUNC\_ARTICLE\_MAINTENANCE\_CYCLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_MAINTENANCE_CYCLE(Int32).html) | Maintenance cycle # 26638. |
| Public Property | [FUNC\_ARTICLE\_MAINTENANCE\_INTERVAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_MAINTENANCE_INTERVAL(Int32).html) | Maintenance interval # 26636. |
| Public Property | [FUNC\_ARTICLE\_MANUFACTURER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_MANUFACTURER(Int32).html) | Manufacturer # 20921. |
| Public Property | [FUNC\_ARTICLE\_MASS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_MASS(Int32).html) | Mass # 26441. |
| Public Property | [FUNC\_ARTICLE\_MASS\_MOMENT\_OF\_INERTIA\_OF\_THE\_LOAD](topic440.html) | Mass moment of inertia of the load # 26444. |
| Public Property | [FUNC\_ARTICLE\_MAX\_POWER\_CONSUMPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_MAX_POWER_CONSUMPTION(Int32).html) | Power consumption, max. # 26420. |
| Public Property | [FUNC\_ARTICLE\_MAX\_RATED\_CURRENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_MAX_RATED_CURRENT(Int32).html) | Nominal current, max. # 26501. |
| Public Property | [FUNC\_ARTICLE\_MAX\_RATED\_POWER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_MAX_RATED_POWER(Int32).html) | Nominal power (in kW), max. # 26479. |
| Public Property | [FUNC\_ARTICLE\_MEASURED\_VARIABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_MEASURED_VARIABLE(Int32).html) | Measurand # 26461. |
| Public Property | [FUNC\_ARTICLE\_MEASURING\_ACCURACY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_MEASURING_ACCURACY(Int32).html) | Measurement accuracy # 26459. |
| Public Property | [FUNC\_ARTICLE\_MOUNTING\_FORM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_MOUNTING_FORM(Int32).html) | Mounting configuration # 26274. |
| Public Property | [FUNC\_ARTICLE\_MOUNTINGSITE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_MOUNTINGSITE(Int32).html) | Part: Mounting surface # 20918. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_CURRENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_NOMINAL_CURRENT(Int32).html) | Nominal current # 26312. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_MOTOR\_POWER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_NOMINAL_MOTOR_POWER(Int32).html) | Motor nominal power # 26463. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_POWER\_CONSUMPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_NOMINAL_POWER_CONSUMPTION(Int32).html) | Nominal power consumption # 26483. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_POWER\_REQUIREMENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_NOMINAL_POWER_REQUIREMENT(Int32).html) | Nominal power requirement # 26485. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_PRESSURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_NOMINAL_PRESSURE(Int32).html) | Nominal pressure # 26471. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_PRESSURE\_RANGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_NOMINAL_PRESSURE_RANGE(Int32).html) | Pressure range # 26473. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_PRESSURE\_SERIES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_NOMINAL_PRESSURE_SERIES(Int32).html) | Nominal pressure series # 26310. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_VOLUME\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_NOMINAL_VOLUME_FLOW(Int32).html) | Nominal flow rate # 26507. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_VOLUME\_FLOW\_OF\_THE\_SUCTION\_SIDE](topic441.html) | Nominal flow rate (intake side) # 26509. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_VOLUMETRIC\_FLOW\_OF\_COMPRESSED\_AIR](topic442.html) | Nominal flow rate (compressed air) # 26511. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_WIDTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_NOMINAL_WIDTH(Int32).html) | Nominal size / diameter # 26513. |
| Public Property | [FUNC\_ARTICLE\_NOMINAL\_WIDTH\_CONNECTION\_SIZE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_NOMINAL_WIDTH_CONNECTION_SIZE(Int32).html) | Nominal size / connection size # 26515. |
| Public Property | [FUNC\_ARTICLE\_NOTE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_NOTE(Int32).html) | Part description # 31014. |
| Public Property | [FUNC\_ARTICLE\_NUMBER\_OF\_BACNET\_I\_O\_OBJECTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_NUMBER_OF_BACNET_I_O_OBJECTS(Int32).html) | BACnet: Number of I/O objects # 26213. |
| Public Property | [FUNC\_ARTICLE\_NUMBER\_OF\_HW\_INTERFACES\_BACNET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_NUMBER_OF_HW_INTERFACES_BACNET(Int32).html) | BACnet: Number of hardware interfaces # 26215. |
| Public Property | [FUNC\_ARTICLE\_NUMBER\_OF\_INPUTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_NUMBER_OF_INPUTS(Int32).html) | Number of inputs # 26217. |
| Public Property | [FUNC\_ARTICLE\_NUMBER\_OF\_OUTPUTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_NUMBER_OF_OUTPUTS(Int32).html) | Number of outputs # 31177. |
| Public Property | [FUNC\_ARTICLE\_OPENING\_PRESSURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_OPENING_PRESSURE(Int32).html) | Opening pressure # 26523. |
| Public Property | [FUNC\_ARTICLE\_OPERATING\_TEMPERATURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_OPERATING_TEMPERATURE(Int32).html) | Operating temperature # 26238. |
| Public Property | [FUNC\_ARTICLE\_OPERATING\_TEMPERATURE\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_OPERATING_TEMPERATURE_MAX(Int32).html) | Operating temperature, max. # 26240. |
| Public Property | [FUNC\_ARTICLE\_OPERATING\_TEMPERATURE\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_OPERATING_TEMPERATURE_MIN(Int32).html) | Operating temperature, min. # 26242. |
| Public Property | [FUNC\_ARTICLE\_ORDERNR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ORDERNR(Int32).html) | Order number # 20919. |
| Public Property | [FUNC\_ARTICLE\_OUTPUT\_SPEED\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_OUTPUT_SPEED_MAX(Int32).html) | Output speed, max. # 26184. |
| Public Property | [FUNC\_ARTICLE\_OUTPUT\_SPEED\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_OUTPUT_SPEED_MIN(Int32).html) | Output speed, min. # 26186. |
| Public Property | [FUNC\_ARTICLE\_OVERLOAD\_CAPACITY\_OVERCURRENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_OVERLOAD_CAPACITY_OVERCURRENT(Int32).html) | Overload capability: Overcurrent # 26620. |
| Public Property | [FUNC\_ARTICLE\_PARTIAL\_LENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PARTIAL_LENGTH(Int32).html) | Subset / length # 31008. |
| Public Property | [FUNC\_ARTICLE\_PARTIAL\_LENGTH\_FULL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PARTIAL_LENGTH_FULL(Int32).html) | Subset / length (full) # 31091. |
| Public Property | [FUNC\_ARTICLE\_PARTIAL\_LENGTH\_IN\_PROJECT\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PARTIAL_LENGTH_IN_PROJECT_UNIT(Int32).html) | Subset / length in unit of project # 31040. |
| Public Property | [FUNC\_ARTICLE\_PARTIAL\_LENGTH\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PARTIAL_LENGTH_UNIT(Int32).html) | Unit for subset / length # 31012. |
| Public Property | [FUNC\_ARTICLE\_PARTIAL\_LENGTH\_VALUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PARTIAL_LENGTH_VALUE(Int32).html) | Subset / length: Value # 31010. |
| Public Property | [FUNC\_ARTICLE\_PARTIAL\_LENGTH\_WITH\_PROJECT\_UNIT](topic443.html) | Subset / length with unit of project # 31043. |
| Public Property | [FUNC\_ARTICLE\_PARTNR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PARTNR(Int32).html) | Part number # 20100. |
| Public Property | [FUNC\_ARTICLE\_PARTTYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PARTTYPE(Int32).html) | Record type # 20103. |
| Public Property | [FUNC\_ARTICLE\_PERFORMANCE\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PERFORMANCE_DESCRIPTION(Int32).html) | Performance description, standardized: Description (device, utility, service) # 26426. |
| Public Property | [FUNC\_ARTICLE\_PIECETYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PIECETYPE(Int32).html) | Part group # 20903. |
| Public Property | [FUNC\_ARTICLE\_PLUG\_CONNECTOR\_CONNECTION\_1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PLUG_CONNECTOR_CONNECTION_1(Int32).html) | Plug-in connector (connection 1) # 26576. |
| Public Property | [FUNC\_ARTICLE\_PLUG\_CONNECTOR\_CONNECTION\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PLUG_CONNECTOR_CONNECTION_2(Int32).html) | Plug-in connector (connection 2) # 26578. |
| Public Property | [FUNC\_ARTICLE\_POSITION\_KEYWORD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_POSITION_KEYWORD(Int32).html) | Performance description, standardized: Item keyword (device, utility, service) # 26537. |
| Public Property | [FUNC\_ARTICLE\_POSITION\_NUMBER\_MANUFACTURER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_POSITION_NUMBER_MANUFACTURER(Int32).html) | Item number (manufacturer) # 26535. |
| Public Property | [FUNC\_ARTICLE\_POSITION\_NUMBER\_STLB](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_POSITION_NUMBER_STLB(Int32).html) | Performance description, standardized: Item number (device, utility, service) # 26533. |
| Public Property | [FUNC\_ARTICLE\_POSNR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_POSNR(Int32).html) | Item number # 20464. |
| Public Property | [FUNC\_ARTICLE\_POSSIBLE\_APPLICATIONS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_POSSIBLE_APPLICATIONS(Int32).html) | Possible uses # 26290. |
| Public Property | [FUNC\_ARTICLE\_POWER\_CONSUMPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_POWER_CONSUMPTION(Int32).html) | Power consumption # 26418. |
| Public Property | [FUNC\_ARTICLE\_POWER\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_POWER_DESCRIPTION(Int32).html) | Performance description (item, device) # 26428. |
| Public Property | [FUNC\_ARTICLE\_POWER\_GROUP\_ITEM\_NUMBER\_LGPOSNR](topic444.html) | Performance description, standardized: Performance group item number # 26432. |
| Public Property | [FUNC\_ARTICLE\_POWER\_REQUIREMENT\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_POWER_REQUIREMENT_MAX(Int32).html) | Power requirement, max. # 26422. |
| Public Property | [FUNC\_ARTICLE\_POWER\_REQUIREMENT\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_POWER_REQUIREMENT_MIN(Int32).html) | Power requirement, min. # 26424. |
| Public Property | [FUNC\_ARTICLE\_PRESSURE\_STAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PRESSURE_STAGE(Int32).html) | Pressure level # 26260. |
| Public Property | [FUNC\_ARTICLE\_PRODUCT\_FUNCTION\_WITH\_BACNET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PRODUCT_FUNCTION_WITH_BACNET(Int32).html) | BACnet: Product function # 26539. |
| Public Property | [FUNC\_ARTICLE\_PROTECTION\_CLASS\_IP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PROTECTION_CLASS_IP(Int32).html) | Degree of protection (IP) # 26554. |
| Public Property | [FUNC\_ARTICLE\_PROTECTION\_CLASS\_IP\_FRONT\_SIDE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PROTECTION_CLASS_IP_FRONT_SIDE(Int32).html) | Degree of protection (IP): Front side # 26560. |
| Public Property | [FUNC\_ARTICLE\_PROTECTION\_CLASS\_IP\_MOUNTED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PROTECTION_CLASS_IP_MOUNTED(Int32).html) | Degree of protection (IP): Mounted # 26562. |
| Public Property | [FUNC\_ARTICLE\_PROTECTION\_CLASS\_IP\_OF\_THE\_EVALUATION\_ELECTRONICS](topic445.html) | Degree of protection (IP): Evaluation electronics # 26556. |
| Public Property | [FUNC\_ARTICLE\_PROTECTION\_CLASS\_IP\_OF\_THE\_MEASURING\_HEAD](topic446.html) | Degree of protection (IP): Measuring head # 26558. |
| Public Property | [FUNC\_ARTICLE\_PROTECTION\_CLASS\_IP\_REAR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PROTECTION_CLASS_IP_REAR(Int32).html) | Degree of protection (IP): Rear side # 26564. |
| Public Property | [FUNC\_ARTICLE\_PROTECTION\_CLASS\_OF\_THE\_ELECTRIC\_MOTOR](topic447.html) | Protection type class (motor) # 26566. |
| Public Property | [FUNC\_ARTICLE\_PROTOCOL\_BACNET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PROTOCOL_BACNET(Int32).html) | BACnet: Protocol # 26541. |
| Public Property | [FUNC\_ARTICLE\_PROVISION\_OF\_THE\_CABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PROVISION_OF_THE_CABLE(Int32).html) | Provision of cable # 26233. |
| Public Property | [FUNC\_ARTICLE\_PROVISION\_OF\_THE\_CABLE\_GLAND](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PROVISION_OF_THE_CABLE_GLAND(Int32).html) | Provision of cable gland # 26231. |
| Public Property | [FUNC\_ARTICLE\_PUMPING\_CAPACITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PUMPING_CAPACITY(Int32).html) | Transport capacity # 26325. |
| Public Property | [FUNC\_ARTICLE\_PUMPING\_CAPACITY\_OF\_THE\_OPERATING\_LIQUID](topic448.html) | Transport capacity of the operating fluid # 26327. |
| Public Property | [FUNC\_ARTICLE\_PUMPING\_VOLUME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PUMPING_VOLUME(Int32).html) | Transport volume # 26329. |
| Public Property | [FUNC\_ARTICLE\_QUANTITY\_IN\_PROJECT\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_QUANTITY_IN_PROJECT_UNIT(Int32).html) | Quantity / subset in unit of project # 31044. |
| Public Property | [FUNC\_ARTICLE\_RANGE\_OF\_APPLICATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_RANGE_OF_APPLICATION(Int32).html) | Operating area # 26286. |
| Public Property | [FUNC\_ARTICLE\_RATED\_APPARENT\_POWER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_RATED_APPARENT_POWER(Int32).html) | Rated apparent power # 26235. |
| Public Property | [FUNC\_ARTICLE\_RATED\_CURRENT\_CONSUMPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_RATED_CURRENT_CONSUMPTION(Int32).html) | Nominal current consumption # 26505. |
| Public Property | [FUNC\_ARTICLE\_RATED\_CURRENT\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_RATED_CURRENT_MIN(Int32).html) | Nominal current, min. # 26503. |
| Public Property | [FUNC\_ARTICLE\_RATED\_DRIVING\_TORQUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_RATED_DRIVING_TORQUE(Int32).html) | Nominal drive torque # 26467. |
| Public Property | [FUNC\_ARTICLE\_RATED\_OUTPUT\_TORQUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_RATED_OUTPUT_TORQUE(Int32).html) | Nominal output torque # 26465. |
| Public Property | [FUNC\_ARTICLE\_RATED\_POWER\_KW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_RATED_POWER_KW(Int32).html) | Nominal power # 26475. |
| Public Property | [FUNC\_ARTICLE\_RATED\_POWER\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_RATED_POWER_MIN(Int32).html) | Nominal power (in kW), min. # 26481. |
| Public Property | [FUNC\_ARTICLE\_RATED\_SPEED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_RATED_SPEED(Int32).html) | Nominal rotation speed # 26469. |
| Public Property | [FUNC\_ARTICLE\_RATED\_VOLTAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_RATED_VOLTAGE(Int32).html) | Nominal voltage # 26487. |
| Public Property | [FUNC\_ARTICLE\_RATED\_VOLTAGE\_FOR\_AC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_RATED_VOLTAGE_FOR_AC(Int32).html) | Nominal voltage (AC) # 26491. |
| Public Property | [FUNC\_ARTICLE\_RATED\_VOLTAGE\_FOR\_AC\_50\_HZ](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_RATED_VOLTAGE_FOR_AC_50_HZ(Int32).html) | Nominal voltage (AC 50 Hz) # 26489. |
| Public Property | [FUNC\_ARTICLE\_RATED\_VOLTAGE\_FOR\_DC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_RATED_VOLTAGE_FOR_DC(Int32).html) | Nominal voltage (DC) # 26493. |
| Public Property | [FUNC\_ARTICLE\_RATED\_VOLTAGE\_OF\_THE\_CONTROL\_CIRCUIT](topic449.html) | Nominal voltage (control circuit) # 26497. |
| Public Property | [FUNC\_ARTICLE\_RATED\_VOLTAGE\_OF\_THE\_LOAD\_CIRCUIT](topic450.html) | Nominal voltage (load circuit) # 26495. |
| Public Property | [FUNC\_ARTICLE\_REPLACEMENT\_FOR\_PRODUCT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_REPLACEMENT_FOR_PRODUCT(Int32).html) | Replacement part: Original part # 26319. |
| Public Property | [FUNC\_ARTICLE\_RUN\_UP\_TIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_RUN_UP_TIME(Int32).html) | Start-up time # 26314. |
| Public Property | [FUNC\_ARTICLE\_SECONDARY\_CASING\_PRESSURE\_STAGE](topic451.html) | Pressure level of secondary housing # 26262. |
| Public Property | [FUNC\_ARTICLE\_SERVICE\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_SERVICE_UNIT(Int32).html) | Performance unit (bill of quantities) # 26430. |
| Public Property | [FUNC\_ARTICLE\_SET\_POINT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_SET_POINT(Int32).html) | Setpoint # 26568. |
| Public Property | [FUNC\_ARTICLE\_SHOCK\_LOAD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_SHOCK_LOAD(Int32).html) | Shock load # 26585. |
| Public Property | [FUNC\_ARTICLE\_SPARE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_SPARE(Int32).html) | Spare part # 20907. |
| Public Property | [FUNC\_ARTICLE\_SPECIFIED\_MAXIMUM\_DRIVE\_TORQUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_SPECIFIED_MAXIMUM_DRIVE_TORQUE(Int32).html) | Drive torque (specified), max. # 26571. |
| Public Property | [FUNC\_ARTICLE\_SPECIFIED\_MINIMUM\_DRIVE\_TORQUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_SPECIFIED_MINIMUM_DRIVE_TORQUE(Int32).html) | Drive torque (specified), min. # 26573. |
| Public Property | [FUNC\_ARTICLE\_SPEED\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_SPEED_MAX(Int32).html) | Rotation speed, max. # 26256. |
| Public Property | [FUNC\_ARTICLE\_SPEED\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_SPEED_MIN(Int32).html) | Rotation speed, min. # 26258. |
| Public Property | [FUNC\_ARTICLE\_STANDARD\_BACNET\_](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_STANDARD_BACNET_(Int32).html) | BACnet: Standard # 26517. |
| Public Property | [FUNC\_ARTICLE\_START\_UP\_TIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_START_UP_TIME(Int32).html) | Switch-on time # 26193. |
| Public Property | [FUNC\_ARTICLE\_STARTING\_CURRENT\_A](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_STARTING_CURRENT_A(Int32).html) | Starting current, max. # 26191. |
| Public Property | [FUNC\_ARTICLE\_STORAGE\_TRANSPORT\_AND\_PACKAGING\_REQUIREMENT](topic452.html) | Storage, transport and packaging (requirement) # 26410. |
| Public Property | [FUNC\_ARTICLE\_STRESS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_STRESS(Int32).html) | Stress # 20910. |
| Public Property | [FUNC\_ARTICLE\_STRIPPING\_LENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_STRIPPING_LENGTH(Int32).html) | Jacket (cable) stripping length # 31176. |
| Public Property | [FUNC\_ARTICLE\_SUCTION\_VOLUME\_FLOW\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_SUCTION_VOLUME_FLOW_MAX(Int32).html) | Intake flow rate, max. # 26199. |
| Public Property | [FUNC\_ARTICLE\_SUITABLE\_AS\_MONITOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_SUITABLE_AS_MONITOR(Int32).html) | Suitable as monitoring device # 26356. |
| Public Property | [FUNC\_ARTICLE\_SUITABLE\_FOR\_CABLE\_DIAMETERS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_SUITABLE_FOR_CABLE_DIAMETERS(Int32).html) | Suitable for cable diameter # 26351. |
| Public Property | [FUNC\_ARTICLE\_SUITABLE\_FOR\_PROTECTION\_CLASS\_IP](topic453.html) | Suitable for degree of protection (IP) # 26359. |
| Public Property | [FUNC\_ARTICLE\_SUPPLIER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_SUPPLIER(Int32).html) | Supplier # 20920. |
| Public Property | [FUNC\_ARTICLE\_SUPPLIER\_BATCH\_NUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_SUPPLIER_BATCH_NUMBER(Int32).html) | Supplier batch number # 26436. |
| Public Property | [FUNC\_ARTICLE\_SUPPLY\_VOLTAGE\_RANGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_SUPPLY_VOLTAGE_RANGE(Int32).html) | Supply voltage range # 26624. |
| Public Property | [FUNC\_ARTICLE\_SUPPRESSINPARTSLIST](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_SUPPRESSINPARTSLIST(Int32).html) | Suppress in bill of materials (if filtered) # 20105. |
| Public Property | [FUNC\_ARTICLE\_SWITCHING\_CAPACITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_SWITCHING_CAPACITY(Int32).html) | Switching capacity # 26546. |
| Public Property | [FUNC\_ARTICLE\_TEMPERATUR\_MEDIUM\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_TEMPERATUR_MEDIUM_MAX(Int32).html) | Temperature (medium), max. # 26610. |
| Public Property | [FUNC\_ARTICLE\_TEMPERATUR\_MEDIUM\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_TEMPERATUR_MEDIUM_MIN(Int32).html) | Temperature (medium), min. # 26612. |
| Public Property | [FUNC\_ARTICLE\_TEMPERATURE\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_TEMPERATURE_MAX(Int32).html) | Temperature, max. # 26608. |
| Public Property | [FUNC\_ARTICLE\_TEMPERATURE\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_TEMPERATURE_MIN(Int32).html) | Temperature, min. # 26614. |
| Public Property | [FUNC\_ARTICLE\_TEMPERATURE\_RANGE\_MEDIUM\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_TEMPERATURE_RANGE_MEDIUM_MAX(Int32).html) | Temperature range (medium), max. # 26616. |
| Public Property | [FUNC\_ARTICLE\_TEMPERATURE\_RANGE\_MEDIUM\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_TEMPERATURE_RANGE_MEDIUM_MIN(Int32).html) | Temperature range (medium), min. # 26618. |
| Public Property | [FUNC\_ARTICLE\_THROUGHPUT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_THROUGHPUT(Int32).html) | Throughput # 26270. |
| Public Property | [FUNC\_ARTICLE\_TORQUE\_](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_TORQUE_(Int32).html) | Torque # 26248. |
| Public Property | [FUNC\_ARTICLE\_TORQUE\_AT\_MAX\_SPEED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_TORQUE_AT_MAX_SPEED(Int32).html) | Torque (at max. rotation speed) # 26250. |
| Public Property | [FUNC\_ARTICLE\_TORQUE\_AT\_MIN\_SPEED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_TORQUE_AT_MIN_SPEED(Int32).html) | Torque (at min. rotation speed) # 26252. |
| Public Property | [FUNC\_ARTICLE\_TORQUE\_MAX\_](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_TORQUE_MAX_(Int32).html) | Torque, max. # 26254. |
| Public Property | [FUNC\_ARTICLE\_TOTAL\_NUMBER\_OF\_BACNET\_OBJECTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_TOTAL_NUMBER_OF_BACNET_OBJECTS(Int32).html) | BACnet: Total number of objects # 26211. |
| Public Property | [FUNC\_ARTICLE\_TYPE\_OF\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_TYPE_OF_FLOW(Int32).html) | Type of flow # 26220. |
| Public Property | [FUNC\_ARTICLE\_TYPE\_OF\_SWITCHING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_TYPE_OF_SWITCHING(Int32).html) | Circuit type # 26548. |
| Public Property | [FUNC\_ARTICLE\_TYPE\_OF\_USE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_TYPE_OF_USE(Int32).html) | Operating mode # 26284. |
| Public Property | [FUNC\_ARTICLE\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_UNIT(Int32).html) | Unit # 26282. |
| Public Property | [FUNC\_ARTICLE\_UNIT\_CLASS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_UNIT_CLASS(Int32).html) | Device class # 26367. |
| Public Property | [FUNC\_ARTICLE\_UNIT\_DESIGN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_UNIT_DESIGN(Int32).html) | Type of construction: Device # 26365. |
| Public Property | [FUNC\_ARTICLE\_UPPER\_PROCESS\_PRESSURE\_LIMIT\_ABSOLUTE\_PRESSURE](topic454.html) | Process pressure (absolute pressure), max. # 26519. |
| Public Property | [FUNC\_ARTICLE\_UPPER\_PROCESS\_PRESSURE\_LIMIT\_GAUGE\_PRESSURE](topic455.html) | Process pressure (overpressure), max. # 26521. |
| Public Property | [FUNC\_ARTICLE\_USAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_USAGE(Int32).html) | Procurement # 20911. |
| Public Property | [FUNC\_ARTICLE\_USE\_FOR\_MARKING\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_USE_FOR_MARKING_TYPE(Int32).html) | Usage for labeling type # 26626. |
| Public Property | [FUNC\_ARTICLE\_USED\_SAFETYRELATEDVALUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_USED_SAFETYRELATEDVALUE(Int32).html) | Safety-related values: Use case in use # 20307. |
| Public Property | [FUNC\_ARTICLE\_VARIANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_VARIANT(Int32).html) | Part variant # 20101. |
| Public Property | [FUNC\_ARTICLE\_VERSION\_AS\_MAINTENANCE\_REPAIR\_SWITCH](topic456.html) | Design as maintenance / repair switch # 31178. |
| Public Property | [FUNC\_ARTICLE\_VISCOSITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_VISCOSITY(Int32).html) | Viscosity # 26628. |
| Public Property | [FUNC\_ARTICLE\_VISCOSITY\_CLASS\_ACCORDING\_TO\_DIN\_51519](topic457.html) | Viscosity class (acc. to DIN 51519) # 26632. |
| Public Property | [FUNC\_ARTICLE\_VISCOSITY\_INDEX\_ACCORDING\_TO\_DIN\_ISO\_2909](topic458.html) | Viscosity index (acc. to DIN ISO 2909) # 26630. |
| Public Property | [FUNC\_ARTICLE\_VOLUME\_FLOW\_HEATING\_M3\_H](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_VOLUME_FLOW_HEATING_M3_H(Int32).html) | Flow rate # 26634. |
| Public Property | [FUNC\_ARTICLE\_WEAR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_WEAR(Int32).html) | Wearing part # 20908. |
| Public Property | [FUNC\_ARTICLE\_WEIGHT\_ITEM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_WEIGHT_ITEM(Int32).html) | Weight (part) # 26371. |
| Public Property | [FUNC\_ARTICLE\_WEIGHT\_KG\_1000\_M](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_WEIGHT_KG_1000_M(Int32).html) | Weight (in kg/1000 m) # 26375. |
| Public Property | [FUNC\_ARTICLE\_WEIGHT\_OF\_THE\_INDIVIDUAL\_ARTICLE\_PACKAGING](topic459.html) | Weight (individual packaging) # 26377. |
| Public Property | [FUNC\_ARTICLE\_WEIGHT\_OF\_THE\_PACKAGING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_WEIGHT_OF_THE_PACKAGING(Int32).html) | Weight (packaging) # 26379. |
| Public Property | [FUNC\_ARTICLE\_WEIGHT\_TOTAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_WEIGHT_TOTAL(Int32).html) | Total weight (part) # 26373. |
| Public Property | [FUNC\_ARTICLEREF\_PARTSLISTGROUP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLEREF_PARTSLISTGROUP(Int32).html) | Bill of materials group # 20924. |
| Public Property | [FUNC\_DEVICETAG\_FULL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_DEVICETAG_FULL().html) | DT (full, without project structures) # 20009. |
| Public Property | [FUNC\_DEVICETAG\_FULL\_WITHSEPARATOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_DEVICETAG_FULL_WITHSEPARATOR().html) | DT (full, without project structures, with preceding sign) # 20213. |
| Public Property | [INSTANCE\_REVISION\_LOG\_MARKER\_FORMAT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~INSTANCE_REVISION_LOG_MARKER_FORMAT().html) | Revision marker format (change tracking) # 19031. |
| Public Property | [INSTANCE\_REVISIONID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~INSTANCE_REVISIONID().html) | Revision change marker (from property comparison) # 10153. |
| Public Property | [INSTANCE\_REVISIONMARKER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~INSTANCE_REVISIONMARKER().html) | Revision marker (from property comparison) # 10152. |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [PROJ\_ACTUALDATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ACTUALDATE().html) | Date # 10027. |
| Public Property | [PROJ\_ACTUALTIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ACTUALTIME().html) | Time of the day # 10058. |
| Public Property | [PROJ\_ADDITIONALINFO\_DOCUMENTSTRUCTUREINFRONT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ADDITIONALINFO_DOCUMENTSTRUCTUREINFRONT().html) | Start page name with document type # 10450. |
| Public Property | [PROJ\_ARTICLEREF\_CRAFT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ARTICLEREF_CRAFT(Int32).html) | Trade of part reference # 20913. |
| Public Property | [PROJ\_ARTICLEREF\_SUBCRAFT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ARTICLEREF_SUBCRAFT(Int32).html) | Subtrade of part reference # 20914. |
| Public Property | [PROJ\_BACKUP\_BACKUPPATH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BACKUP_BACKUPPATH().html) | Data backup: Backup directory # 10517. |
| Public Property | [PROJ\_BACKUP\_COMPRESS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BACKUP_COMPRESS().html) | Data backup: Reorganize project # 10513. |
| Public Property | [PROJ\_BACKUP\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BACKUP_DESCRIPTION().html) | Data backup: Description # 10518. |
| Public Property | [PROJ\_BACKUP\_EXTDOCS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BACKUP_EXTDOCS().html) | Data backup: Back up external documents # 10511. |
| Public Property | [PROJ\_BACKUP\_FULL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BACKUP_FULL().html) | Data backup: Complete backup # 10510. |
| Public Property | [PROJ\_BACKUP\_IMAGES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BACKUP_IMAGES().html) | Data backup: Back up image files # 10512. |
| Public Property | [PROJ\_BACKUP\_MEDIUM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BACKUP_MEDIUM().html) | Data backup: Backup medium # 10515. |
| Public Property | [PROJ\_BACKUP\_METHOD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BACKUP_METHOD().html) | Data backup: Method # 10514. |
| Public Property | [PROJ\_BACKUP\_SPLITSIZE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BACKUP_SPLITSIZE().html) | Data backup: E-mail message split size in MB # 10516. |
| Public Property | [PROJ\_BLOCKFORMAT\_BLACKBOX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_BLACKBOX(Int32).html) | Block property: Format (black box) # 10610. |
| Public Property | [PROJ\_BLOCKFORMAT\_BUSBAR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_BUSBAR(Int32).html) | Block property: Format (busbar) # 10612. |
| Public Property | [PROJ\_BLOCKFORMAT\_CABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_CABLE(Int32).html) | Block property: Format (cable / shield) # 10607. |
| Public Property | [PROJ\_BLOCKFORMAT\_CONNECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_CONNECTION(Int32).html) | Block property: Format (connection) # 10608. |
| Public Property | [PROJ\_BLOCKFORMAT\_CONNECTOR\_DEF\_TEXT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_CONNECTOR_DEF_TEXT(Int32).html) | Block property: Format (plug definition) # 10603. |
| Public Property | [PROJ\_BLOCKFORMAT\_DEVICE\_END\_TERMINAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_DEVICE_END_TERMINAL(Int32).html) | Block property: Format (device connection point) # 10611. |
| Public Property | [PROJ\_BLOCKFORMAT\_DISTRIBUTOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_DISTRIBUTOR(Int32).html) | Block property: Format (fluid connection splicer / line connector) # 10614. |
| Public Property | [PROJ\_BLOCKFORMAT\_FLUIDDEVICE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_FLUIDDEVICE(Int32).html) | Block property: Format (fluid device) # 10613. |
| Public Property | [PROJ\_BLOCKFORMAT\_FUNCTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_FUNCTION(Int32).html) | Block property: Format (general devices) # 10600. |
| Public Property | [PROJ\_BLOCKFORMAT\_INTERRUPTION\_POINT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_INTERRUPTION_POINT(Int32).html) | Block property: Format (interruption point) # 10609. |
| Public Property | [PROJ\_BLOCKFORMAT\_LOCATIONBOX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_LOCATIONBOX(Int32).html) | Block property: Format (structure box) # 10662. |
| Public Property | [PROJ\_BLOCKFORMAT\_MECHANIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_MECHANIC(Int32).html) | Block property: Format (mechanical) # 10619. |
| Public Property | [PROJ\_BLOCKFORMAT\_PAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_PAGE(Int32).html) | Block property: Format (page) # 10618. |
| Public Property | [PROJ\_BLOCKFORMAT\_PLAOBJECT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_PLAOBJECT(Int32).html) | Block property: Format (pre-planning) # 10661. |
| Public Property | [PROJ\_BLOCKFORMAT\_PLC\_TERMINAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_PLC_TERMINAL(Int32).html) | Block property: Format (PLC connection point) # 10606. |
| Public Property | [PROJ\_BLOCKFORMAT\_PLCBOX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_PLCBOX(Int32).html) | Block property: Format (PLC box) # 10605. |
| Public Property | [PROJ\_BLOCKFORMAT\_PLT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_PLT(Int32).html) | Block property: Format (PCT loop) # 10615. |
| Public Property | [PROJ\_BLOCKFORMAT\_PLTFUNCTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_PLTFUNCTION(Int32).html) | Block property: Format (PCT loop function) # 10616. |
| Public Property | [PROJ\_BLOCKFORMAT\_PLUG](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_PLUG(Int32).html) | Block property: Format (pin) # 10604. |
| Public Property | [PROJ\_BLOCKFORMAT\_POTENTIALDEFINITION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_POTENTIALDEFINITION(Int32).html) | Block property: Format (potential definition) # 10096. |
| Public Property | [PROJ\_BLOCKFORMAT\_PROCESS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_PROCESS(Int32).html) | Block property: Format (process engineering) # 10617. |
| Public Property | [PROJ\_BLOCKFORMAT\_PROCESSDEFINITION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_PROCESSDEFINITION(Int32).html) | Block property: Format (piping definition) # 10097. |
| Public Property | [PROJ\_BLOCKFORMAT\_TERMINAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_TERMINAL(Int32).html) | Block property: Format (terminal) # 10602. |
| Public Property | [PROJ\_BLOCKFORMAT\_TERMINAL\_DEF\_TEXT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_TERMINAL_DEF_TEXT(Int32).html) | Block property: Format (terminal strip definition) # 10601. |
| Public Property | [PROJ\_BLOCKPROPERTY\_REPLACETEXT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKPROPERTY_REPLACETEXT(Int32).html) | Block property: Replacement text # 10660. |
| Public Property | [PROJ\_CLOUD\_EDITMODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CLOUD_EDITMODE().html) | Processing mode for the cloud # 10122. |
| Public Property | [PROJ\_CLOUD\_PROJECT\_ID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CLOUD_PROJECT_ID().html) | Unique project ID for the Cloud # 10120. |
| Public Property | [PROJ\_COMMISSION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_COMMISSION().html) | Commission # 10014. |
| Public Property | [PROJ\_COMPANYADDRESS1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_COMPANYADDRESS1().html) | Company address 1 # 10016. |
| Public Property | [PROJ\_COMPANYADDRESS2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_COMPANYADDRESS2().html) | Company address 2 # 10017. |
| Public Property | [PROJ\_COMPANYNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_COMPANYNAME().html) | Company name # 10015. |
| Public Property | [PROJ\_CONTROLVOLTAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CONTROLVOLTAGE().html) | Control voltage # 10041. |
| Public Property | [PROJ\_COUNTPERPAGETYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_COUNTPERPAGETYPE(Int32).html) | Number of pages per page type # 10200. |
| Public Property | [PROJ\_CREATIONDATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATIONDATE().html) | Creation date # 10021. |
| Public Property | [PROJ\_CREATIONTIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATIONTIME().html) | Creation time # 10046. |
| Public Property | [PROJ\_CREATOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATOR().html) | Creator # 10020. |
| Public Property | [PROJ\_CREATORCITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATORCITY().html) | Creator: City # 10238. |
| Public Property | [PROJ\_CREATORCOUNTRY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATORCOUNTRY().html) | Creator: Country # 10239. |
| Public Property | [PROJ\_CREATOREMAIL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATOREMAIL().html) | Creator: E-mail # 10242. |
| Public Property | [PROJ\_CREATORFAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATORFAX().html) | Creator: Fax # 10241. |
| Public Property | [PROJ\_CREATORID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATORID().html) | Creator: Short name # 10230. |
| Public Property | [PROJ\_CREATORLONGNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATORLONGNAME().html) | Creator: Full name # 10245. |
| Public Property | [PROJ\_CREATORNAME1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATORNAME1().html) | Creator: Name 1 # 10232. |
| Public Property | [PROJ\_CREATORNAME2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATORNAME2().html) | Creator: Name 2 # 10233. |
| Public Property | [PROJ\_CREATORNAME3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATORNAME3().html) | Creator: Name 3 # 10234. |
| Public Property | [PROJ\_CREATORNOTE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATORNOTE().html) | Creator: Description # 10247. |
| Public Property | [PROJ\_CREATORNUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATORNUMBER().html) | Creator: Customer number # 10246. |
| Public Property | [PROJ\_CREATORPOBOX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATORPOBOX().html) | Creator: P.O. box # 10236. |
| Public Property | [PROJ\_CREATORREGION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATORREGION().html) | Creator: State / Region # 10244. |
| Public Property | [PROJ\_CREATORSTREET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATORSTREET().html) | Creator: Street # 10235. |
| Public Property | [PROJ\_CREATORTELEPHONE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATORTELEPHONE().html) | Creator: Phone # 10240. |
| Public Property | [PROJ\_CREATORTITLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATORTITLE().html) | Creator: Title # 10231. |
| Public Property | [PROJ\_CREATORZIPCODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATORZIPCODE().html) | Creator: Zip code (City) # 10237. |
| Public Property | [PROJ\_CREATORZIPCODEPOBOX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATORZIPCODEPOBOX().html) | Creator: Zip code (P.O. box) # 10243. |
| Public Property | [PROJ\_CUSTOMER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMER().html) | Customer # 10370. |
| Public Property | [PROJ\_CUSTOMERCITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMERCITY().html) | Customer: City # 10108. |
| Public Property | [PROJ\_CUSTOMERCOUNTRY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMERCOUNTRY().html) | Customer: Country # 10109. |
| Public Property | [PROJ\_CUSTOMEREMAIL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMEREMAIL().html) | Customer: E-mail # 10112. |
| Public Property | [PROJ\_CUSTOMERFAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMERFAX().html) | Customer: Fax # 10111. |
| Public Property | [PROJ\_CUSTOMERID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMERID().html) | Customer: Short name # 10100. |
| Public Property | [PROJ\_CUSTOMERLONGNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMERLONGNAME().html) | Customer: Full name # 10115. |
| Public Property | [PROJ\_CUSTOMERNAME1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMERNAME1().html) | Customer: Name 1 # 10102. |
| Public Property | [PROJ\_CUSTOMERNAME2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMERNAME2().html) | Customer: Name 2 # 10103. |
| Public Property | [PROJ\_CUSTOMERNAME3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMERNAME3().html) | Customer: Name 3 # 10104. |
| Public Property | [PROJ\_CUSTOMERNOTE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMERNOTE().html) | Customer: Description # 10117. |
| Public Property | [PROJ\_CUSTOMERNUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMERNUMBER().html) | Customer: Customer number # 10116. |
| Public Property | [PROJ\_CUSTOMERPOBOX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMERPOBOX().html) | Customer: P.O. box # 10106. |
| Public Property | [PROJ\_CUSTOMERREGION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMERREGION().html) | Customer: State / Region # 10114. |
| Public Property | [PROJ\_CUSTOMERSTREET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMERSTREET().html) | Customer: Street # 10105. |
| Public Property | [PROJ\_CUSTOMERTELEPHONE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMERTELEPHONE().html) | Customer: Phone # 10110. |
| Public Property | [PROJ\_CUSTOMERTITLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMERTITLE().html) | Customer: Title # 10101. |
| Public Property | [PROJ\_CUSTOMERZIPCODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMERZIPCODE().html) | Customer: Zip code (City) # 10107. |
| Public Property | [PROJ\_CUSTOMERZIPCODEPOBOX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMERZIPCODEPOBOX().html) | Customer: Zip code (P.O. box) # 10113. |
| Public Property | [PROJ\_CUSTOMIDENTIFICATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMIDENTIFICATION().html) | Customer code # 10180. |
| Public Property | [PROJ\_DATEPERPAGETYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DATEPERPAGETYPE(Int32).html) | Last modification date per page type # 10250. |
| Public Property | [PROJ\_DEGOFPROTECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DEGOFPROTECTION().html) | Degree of protection # 10037. |
| Public Property | [PROJ\_DEVTAGFORMAT\_CUSTOMFORMAT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DEVTAGFORMAT_CUSTOMFORMAT().html) | Sequence of individual DT properties # 10091. |
| Public Property | [PROJ\_DEVTAGFORMAT\_ENABLECUSTOMFORMAT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DEVTAGFORMAT_ENABLECUSTOMFORMAT().html) | Edit DT in individual fields # 10090. |
| Public Property | [PROJ\_DRAWINGNUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DRAWINGNUMBER().html) | Job number # 10013. |
| Public Property | [PROJ\_DTFORMAT\_BLACKBOX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DTFORMAT_BLACKBOX().html) | Format of displayed DT: Black box # 10630. |
| Public Property | [PROJ\_DTFORMAT\_BUSBAR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DTFORMAT_BUSBAR().html) | Format of displayed DT: Busbar # 10632. |
| Public Property | [PROJ\_DTFORMAT\_CABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DTFORMAT_CABLE().html) | Format of displayed DT: Cable / shield # 10627. |
| Public Property | [PROJ\_DTFORMAT\_CABLE\_CONNECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DTFORMAT_CABLE_CONNECTION().html) | Format of displayed DT: Cable connection # 10635. |
| Public Property | [PROJ\_DTFORMAT\_CONNECTOR\_DEF\_TEXT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DTFORMAT_CONNECTOR_DEF_TEXT().html) | Format of displayed DT: Plug definition # 10623. |
| Public Property | [PROJ\_DTFORMAT\_DEVICE\_END\_TERMINAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DTFORMAT_DEVICE_END_TERMINAL().html) | Format of displayed DT: Device connection point # 10631. |
| Public Property | [PROJ\_DTFORMAT\_DISTRIBUTOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DTFORMAT_DISTRIBUTOR().html) | Format of displayed DT: Fluid connection splicer / line connector # 10634. |
| Public Property | [PROJ\_DTFORMAT\_FLUIDDEVICE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DTFORMAT_FLUIDDEVICE().html) | Format of displayed DT: Fluid device # 10633. |
| Public Property | [PROJ\_DTFORMAT\_FUNCTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DTFORMAT_FUNCTION().html) | Format of displayed DT: General devices # 10620. |
| Public Property | [PROJ\_DTFORMAT\_INTERRUPTION\_POINT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DTFORMAT_INTERRUPTION_POINT().html) | Format of displayed DT: Interruption point # 10629. |
| Public Property | [PROJ\_DTFORMAT\_PLC\_TERMINAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DTFORMAT_PLC_TERMINAL().html) | Format of displayed DT: PLC connection point # 10626. |
| Public Property | [PROJ\_DTFORMAT\_PLCBOX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DTFORMAT_PLCBOX().html) | Format of displayed DT: PLC box # 10625. |
| Public Property | [PROJ\_DTFORMAT\_PLUG](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DTFORMAT_PLUG().html) | Format of displayed DT: Pin # 10624. |
| Public Property | [PROJ\_DTFORMAT\_TERMINAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DTFORMAT_TERMINAL().html) | Format of displayed DT: Terminal # 10622. |
| Public Property | [PROJ\_DTFORMAT\_TERMINAL\_DEF\_TEXT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_DTFORMAT_TERMINAL_DEF_TEXT().html) | Format of displayed DT: Terminal strip definition # 10621. |
| Public Property | [PROJ\_EDITEDPAGES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_EDITEDPAGES().html) | Created pages # 10301. |
| Public Property | [PROJ\_ENCLOSURES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENCLOSURES().html) | Enclosures # 10038. |
| Public Property | [PROJ\_ENDCUSTOMER\_LONGNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMER_LONGNAME().html) | End customer: Full name # 10145. |
| Public Property | [PROJ\_ENDCUSTOMER\_NOTE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMER_NOTE().html) | End customer: Description # 10147. |
| Public Property | [PROJ\_ENDCUSTOMER\_NUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMER_NUMBER().html) | End customer: Customer number # 10146. |
| Public Property | [PROJ\_ENDCUSTOMER\_REGION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMER_REGION().html) | End customer: State / Region # 10144. |
| Public Property | [PROJ\_ENDCUSTOMERCITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMERCITY().html) | End customer: City # 10138. |
| Public Property | [PROJ\_ENDCUSTOMERCOUNTRY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMERCOUNTRY().html) | End customer: Country # 10139. |
| Public Property | [PROJ\_ENDCUSTOMEREMAIL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMEREMAIL().html) | End customer: E-mail # 10142. |
| Public Property | [PROJ\_ENDCUSTOMERFAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMERFAX().html) | End customer: Fax # 10141. |
| Public Property | [PROJ\_ENDCUSTOMERID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMERID().html) | End customer: Short name # 10130. |
| Public Property | [PROJ\_ENDCUSTOMERNAME1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMERNAME1().html) | End customer: Name 1 # 10132. |
| Public Property | [PROJ\_ENDCUSTOMERNAME2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMERNAME2().html) | End customer: Name 2 # 10133. |
| Public Property | [PROJ\_ENDCUSTOMERNAME3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMERNAME3().html) | End customer: Name 3 # 10134. |
| Public Property | [PROJ\_ENDCUSTOMERPOBOX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMERPOBOX().html) | End customer: P.O. box # 10136. |
| Public Property | [PROJ\_ENDCUSTOMERSTREET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMERSTREET().html) | End customer: Street # 10135. |
| Public Property | [PROJ\_ENDCUSTOMERTELEPHONE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMERTELEPHONE().html) | End customer: Phone # 10140. |
| Public Property | [PROJ\_ENDCUSTOMERTITLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMERTITLE().html) | End customer: Title # 10131. |
| Public Property | [PROJ\_ENDCUSTOMERZIPCODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMERZIPCODE().html) | End customer: Zip code (City) # 10137. |
| Public Property | [PROJ\_ENDCUSTOMERZIPCODEPOBOX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMERZIPCODEPOBOX().html) | End customer: Zip code (P.O. box) # 10143. |
| Public Property | [PROJ\_ENVIRONMENTALCONSIDERATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENVIRONMENTALCONSIDERATION().html) | Environmental consideration # 10034. |
| Public Property | [PROJ\_FROZENPERPAGETYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_FROZENPERPAGETYPE(Int32).html) | Number of frozen pages per page type # 10065. |
| Public Property | [PROJ\_FULL\_PROJECTNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_FULL_PROJECTNAME().html) | Project name (full) # 10009. |
| Public Property | [PROJ\_FULL\_PROJECTPATH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_FULL_PROJECTPATH().html) | Project path (full) # 10045. |
| Public Property | [PROJ\_FULLDTFORMAT\_BLACKBOX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_FULLDTFORMAT_BLACKBOX().html) | Format of full DT: Black box # 10650. |
| Public Property | [PROJ\_FULLDTFORMAT\_BUSBAR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_FULLDTFORMAT_BUSBAR().html) | Format of full DT: Busbar # 10652. |
| Public Property | [PROJ\_FULLDTFORMAT\_CABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_FULLDTFORMAT_CABLE().html) | Format of full DT: Cable / shield # 10647. |
| Public Property | [PROJ\_FULLDTFORMAT\_CABLE\_CONNECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_FULLDTFORMAT_CABLE_CONNECTION().html) | Format of full DT: Cable connection # 10655. |
| Public Property | [PROJ\_FULLDTFORMAT\_CONNECTOR\_DEF\_TEXT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_FULLDTFORMAT_CONNECTOR_DEF_TEXT().html) | Format of full DT: Plug definition # 10643. |
| Public Property | [PROJ\_FULLDTFORMAT\_DEVICE\_END\_TERMINAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_FULLDTFORMAT_DEVICE_END_TERMINAL().html) | Format of full DT: Device connection point # 10651. |
| Public Property | [PROJ\_FULLDTFORMAT\_DISTRIBUTOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_FULLDTFORMAT_DISTRIBUTOR().html) | Format of full DT: Fluid connection splicer / line connector # 10654. |
| Public Property | [PROJ\_FULLDTFORMAT\_FLUIDDEVICE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_FULLDTFORMAT_FLUIDDEVICE().html) | Format of full DT: Fluid device # 10653. |
| Public Property | [PROJ\_FULLDTFORMAT\_FUNCTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_FULLDTFORMAT_FUNCTION().html) | Format of full DT: General devices # 10640. |
| Public Property | [PROJ\_FULLDTFORMAT\_INTERRUPTION\_POINT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_FULLDTFORMAT_INTERRUPTION_POINT().html) | Format of full DT: Interruption point # 10649. |
| Public Property | [PROJ\_FULLDTFORMAT\_PLC\_TERMINAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_FULLDTFORMAT_PLC_TERMINAL().html) | Format of full DT: PLC connection point # 10646. |
| Public Property | [PROJ\_FULLDTFORMAT\_PLCBOX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_FULLDTFORMAT_PLCBOX().html) | Format of full DT: PLC box # 10645. |
| Public Property | [PROJ\_FULLDTFORMAT\_PLUG](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_FULLDTFORMAT_PLUG().html) | Format of full DT: Pin # 10644. |
| Public Property | [PROJ\_FULLDTFORMAT\_TERMINAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_FULLDTFORMAT_TERMINAL().html) | Format of full DT: Terminal # 10642. |
| Public Property | [PROJ\_FULLDTFORMAT\_TERMINAL\_DEF\_TEXT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_FULLDTFORMAT_TERMINAL_DEF_TEXT().html) | Format of full DT: Terminal strip definition # 10641. |
| Public Property | [PROJ\_GENERATEDPAGES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_GENERATEDPAGES().html) | Generated report pages # 10302. |
| Public Property | [PROJ\_GUID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_GUID().html) | Unique project ID # 10184. |
| Public Property | [PROJ\_HIERARCHY\_BUSBAR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_BUSBAR().html) | Structure format for busbars # 10053. |
| Public Property | [PROJ\_HIERARCHY\_CABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_CABLE().html) | Structure format for cables # 10061. |
| Public Property | [PROJ\_HIERARCHY\_CODEDNESTINGSETTINGS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_CODEDNESTINGSETTINGS().html) | Nested device tags # 10019. |
| Public Property | [PROJ\_HIERARCHY\_CODEDSEPARATORS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_CODEDSEPARATORS().html) | Separator for structures # 10018. |
| Public Property | [PROJ\_HIERARCHY\_DEVICEBOX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_DEVICEBOX().html) | Structure format for black boxes # 10056. |
| Public Property | [PROJ\_HIERARCHY\_DISTRIBUTOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_DISTRIBUTOR().html) | Structure format for fluid connection splicer / line connector # 10064. |
| Public Property | [PROJ\_HIERARCHY\_DOCUMENTSTRUCTURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_DOCUMENTSTRUCTURE().html) | Project structure: Document type # 10006. |
| Public Property | [PROJ\_HIERARCHY\_FLUID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_FLUID().html) | Structure format for fluid devices # 10063. |
| Public Property | [PROJ\_HIERARCHY\_FUNCTIONALASSIGNMENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_FUNCTIONALASSIGNMENT().html) | Project structure: Functional assignment # 10001. |
| Public Property | [PROJ\_HIERARCHY\_INSTALLATIONNUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_INSTALLATIONNUMBER().html) | Project structure: Higher-level function number # 10005. |
| Public Property | [PROJ\_HIERARCHY\_INTERRUPTIONPOINT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_INTERRUPTIONPOINT().html) | Structure format for interruption points # 10051. |
| Public Property | [PROJ\_HIERARCHY\_LOCATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_LOCATION().html) | Project structure: Location designation # 10004. |
| Public Property | [PROJ\_HIERARCHY\_LOCATIONBOX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_LOCATIONBOX().html) | Structure format for structure boxes # 10062. |
| Public Property | [PROJ\_HIERARCHY\_MASTERDEVICES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_MASTERDEVICES().html) | Superior structure format for all devices # 10054. |
| Public Property | [PROJ\_HIERARCHY\_MECHANIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_MECHANIC().html) | Structure format for mechanical devices # 10085. |
| Public Property | [PROJ\_HIERARCHY\_PAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_PAGE().html) | Structure format for pages # 10050. |
| Public Property | [PROJ\_HIERARCHY\_PLACEOFINSTALLATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_PLACEOFINSTALLATION().html) | Project structure: Installation site # 10003. |
| Public Property | [PROJ\_HIERARCHY\_PLANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_PLANT().html) | Project structure: Function designation # 10002. |
| Public Property | [PROJ\_HIERARCHY\_PLC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_PLC().html) | Structure format for PLC / bus technology # 10057. |
| Public Property | [PROJ\_HIERARCHY\_PLUG](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_PLUG().html) | Structure format for plugs # 10060. |
| Public Property | [PROJ\_HIERARCHY\_PRODUCT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_PRODUCT().html) | Project structure: Product # 10099. |
| Public Property | [PROJ\_HIERARCHY\_SPECIALDINMODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_SPECIALDINMODE().html) | Superior structure formats # 10029. |
| Public Property | [PROJ\_HIERARCHY\_STANDARDDEVICE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_STANDARDDEVICE().html) | Structure format for general devices # 10055. |
| Public Property | [PROJ\_HIERARCHY\_TAKEOVERPAGENUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_TAKEOVERPAGENUMBER().html) | Use page name in DT # 10012. |
| Public Property | [PROJ\_HIERARCHY\_TERMINALSTRIP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_TERMINALSTRIP().html) | Structure format for terminal strips # 10059. |
| Public Property | [PROJ\_HIERARCHY\_USERDEFINED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_USERDEFINED().html) | Project structure: User-defined structure # 10007. |
| Public Property | [PROJ\_IDENTIFICATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_IDENTIFICATION().html) | User # 10181. |
| Public Property | [PROJ\_INSTALLATIONNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_INSTALLATIONNAME().html) | Project description # 10011. |
| Public Property | [PROJ\_LASTMODIFICATIONDATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_LASTMODIFICATIONDATE().html) | Modification date # 10023. |
| Public Property | [PROJ\_LASTMODIFICATIONTIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_LASTMODIFICATIONTIME().html) | Modification time # 10047. |
| Public Property | [PROJ\_LASTMODIFICATOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_LASTMODIFICATOR().html) | Last editor: Sign-in name # 10022. |
| Public Property | [PROJ\_LASTTRANSLATIONDATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_LASTTRANSLATIONDATE().html) | Last translation: Date # 10024. |
| Public Property | [PROJ\_LASTTRANSLATIONTIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_LASTTRANSLATIONTIME().html) | Last translation: Time # 10048. |
| Public Property | [PROJ\_LASTUSEDBUILDNUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_LASTUSEDBUILDNUMBER().html) | Eplan build number of the last modification or update # 10044. |
| Public Property | [PROJ\_LASTUSEDVERSION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_LASTUSEDVERSION().html) | Eplan version of the last modification or update # 10043. |
| Public Property | [PROJ\_LEADIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_LEADIN().html) | Input lead # 10040. |
| Public Property | [PROJ\_LOCATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_LOCATION().html) | Location # 10035. |
| Public Property | [PROJ\_LOCATIONOFINSTALLATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_LOCATIONOFINSTALLATION().html) | Place of installation # 10032. |
| Public Property | [PROJ\_MAKE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_MAKE().html) | Make # 10030. |
| Public Property | [PROJ\_MANUFACTURINGDATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_MANUFACTURINGDATE().html) | Manufacturing date # 10042. |
| Public Property | [PROJ\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_NAME().html) | Project name # 10000. |
| Public Property | [PROJ\_NAMEFORMAT\_BUSBAR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_NAMEFORMAT_BUSBAR().html) | Naming format for busbars # 10073. |
| Public Property | [PROJ\_NAMEFORMAT\_CABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_NAMEFORMAT_CABLE().html) | Naming format for cables # 10081. |
| Public Property | [PROJ\_NAMEFORMAT\_DEVICE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_NAMEFORMAT_DEVICE().html) | Naming format for devices # 10075. |
| Public Property | [PROJ\_NAMEFORMAT\_DEVICEBOX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_NAMEFORMAT_DEVICEBOX().html) | Naming format for black boxes # 10076. |
| Public Property | [PROJ\_NAMEFORMAT\_DISTRIBUTOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_NAMEFORMAT_DISTRIBUTOR().html) | Naming format for fluid connection splicer / line connector # 10084. |
| Public Property | [PROJ\_NAMEFORMAT\_FLUID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_NAMEFORMAT_FLUID().html) | Naming format for fluid devices # 10083. |
| Public Property | [PROJ\_NAMEFORMAT\_INTERRUPTIONPOINT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_NAMEFORMAT_INTERRUPTIONPOINT().html) | Naming format for interruption points # 10071. |
| Public Property | [PROJ\_NAMEFORMAT\_LOCATIONBOX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_NAMEFORMAT_LOCATIONBOX().html) | Naming format for structure boxes # 10082. |
| Public Property | [PROJ\_NAMEFORMAT\_MASTERDEVICES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_NAMEFORMAT_MASTERDEVICES().html) | Superior naming format for all devices # 10074. |
| Public Property | [PROJ\_NAMEFORMAT\_MECHANIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_NAMEFORMAT_MECHANIC().html) | Naming format for mechanical devices # 10086. |
| Public Property | [PROJ\_NAMEFORMAT\_PAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_NAMEFORMAT_PAGE().html) | Naming format for pages # 10070. |
| Public Property | [PROJ\_NAMEFORMAT\_PLC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_NAMEFORMAT_PLC().html) | Naming format for PLC / bus technology # 10077. |
| Public Property | [PROJ\_NAMEFORMAT\_PLUG](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_NAMEFORMAT_PLUG().html) | Naming format for plugs # 10080. |
| Public Property | [PROJ\_NAMEFORMAT\_TERMINALSTRIP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_NAMEFORMAT_TERMINALSTRIP().html) | Naming format for terminal strips # 10079. |
| Public Property | [PROJ\_NUMERICTYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_NUMERICTYPE().html) | Type of project # 10902. |
| Public Property | [PROJ\_ORIGIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ORIGIN().html) | Project: Template # 10069. |
| Public Property | [PROJ\_PAGECOUNT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_PAGECOUNT().html) | Total no. of pages # 10300. |
| Public Property | [PROJ\_PARTFEATURES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_PARTFEATURES().html) | Part features # 10033. |
| Public Property | [PROJ\_PDD\_DEVICES\_HIERARCHY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_PDD_DEVICES_HIERARCHY().html) | Structure of the tree structure in the device navigators # 10094. |
| Public Property | [PROJ\_PDD\_DEVICES\_SHOWDESCRSTRUCTURES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_PDD_DEVICES_SHOWDESCRSTRUCTURES().html) | Show descriptive identifiers in device navigators # 10095. |
| Public Property | [PROJ\_PDD\_PAGES\_HIERARCHY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_PDD_PAGES_HIERARCHY().html) | Structure of tree structure in page tree # 10092. |
| Public Property | [PROJ\_PDD\_PAGES\_SHOWDESCRSTRUCTURES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_PDD_PAGES_SHOWDESCRSTRUCTURES().html) | Show descriptive identifiers in page tree # 10093. |
| Public Property | [PROJ\_POWERINPUT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_POWERINPUT().html) | Feed-in # 10039. |
| Public Property | [PROJ\_PROJECTBEGIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_PROJECTBEGIN().html) | Project start # 10028. |
| Public Property | [PROJ\_PROJECTEND](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_PROJECTEND().html) | Project end # 10026. |
| Public Property | [PROJ\_PROJECTPATH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_PROJECTPATH().html) | Project path # 10010. |
| Public Property | [PROJ\_PROJECTSTATUS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_PROJECTSTATUS().html) | Project status # 10303. |
| Public Property | [PROJ\_REGULATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REGULATION().html) | Regulation # 10036. |
| Public Property | [PROJ\_RESPONSIBLEFORPROJECT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_RESPONSIBLEFORPROJECT().html) | Responsible for project # 10025. |
| Public Property | [PROJ\_REVISION\_APPROVEDBY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_APPROVEDBY().html) | Approved by # 10160. |
| Public Property | [PROJ\_REVISION\_APPROVEDDATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_APPROVEDDATE().html) | Approved date # 10161. |
| Public Property | [PROJ\_REVISION\_CHECKEDBY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_CHECKEDBY().html) | Checked by # 10162. |
| Public Property | [PROJ\_REVISION\_CHECKEDDATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_CHECKEDDATE().html) | Checked date # 10163. |
| Public Property | [PROJ\_REVISION\_LOG\_DATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_DATE(Int32).html) | Revision date (change tracking) # 10158. |
| Public Property | [PROJ\_REVISION\_LOG\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_DESCRIPTION(Int32).html) | Revision comment (change tracking) # 10156. |
| Public Property | [PROJ\_REVISION\_LOG\_EDITINGAREA](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_EDITINGAREA(Int32).html) | Defined working section (from change tracking) # 10195. |
| Public Property | [PROJ\_REVISION\_LOG\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_NAME(Int32).html) | Revision name (change tracking) # 10155. |
| Public Property | [PROJ\_REVISION\_LOG\_START](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_START().html) | Revision: Change tracking started # 10154. |
| Public Property | [PROJ\_REVISION\_LOG\_TIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_TIME(Int32).html) | Revision time (change tracking) # 10159. |
| Public Property | [PROJ\_REVISION\_LOG\_USER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_USER(Int32).html) | Revision created by (change tracking) # 10157. |
| Public Property | [PROJ\_REVISION\_LOG\_USERCODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_USERCODE(Int32).html) | User code (change tracking) # 10190. |
| Public Property | [PROJ\_REVISION\_LOG\_USEREMAIL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_USEREMAIL(Int32).html) | User: E-mail address (change tracking) # 10193. |
| Public Property | [PROJ\_REVISION\_LOG\_USERNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_USERNAME(Int32).html) | User name (change tracking) # 10191. |
| Public Property | [PROJ\_REVISION\_LOG\_USERPHONE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_USERPHONE(Int32).html) | User: Phone number (change tracking) # 10192. |
| Public Property | [PROJ\_REVISION\_TEMP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_TEMP().html) | Revision: Temporary reference project # 10164. |
| Public Property | [PROJ\_REVISIONS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISIONS(Int32).html) | Revisions # 10150. |
| Public Property | [PROJ\_REVISIONSPARENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISIONSPARENT().html) | Revision: Original project name (complete) # 10151. |
| Public Property | [PROJ\_REVISIONSPARENT\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISIONSPARENT_NAME().html) | Revision: Original project name # 10149. |
| Public Property | [PROJ\_SERIALNUMBERDONGLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_SERIALNUMBERDONGLE().html) | License number of dongle # 10185. |
| Public Property | [PROJ\_SHOWDTSTRUCTURETAB](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_SHOWDTSTRUCTURETAB().html) | Show tab for DT structures # 10008. |
| Public Property | [PROJ\_SOURCELANGUAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_SOURCELANGUAGE().html) | Source language # 10500. |
| Public Property | [PROJ\_STATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_STATION().html) | Workstation # 10182. |
| Public Property | [PROJ\_STRUCTURESEQUENCE\_PAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_STRUCTURESEQUENCE_PAGE().html) | Sequence of the project structures in the page name # 10089. |
| Public Property | [PROJ\_SUPPLEMENTARYFIELD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_SUPPLEMENTARYFIELD(Int32).html) | Supplementary field # 10901. |
| Public Property | [PROJ\_TIMEPERPAGETYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_TIMEPERPAGETYPE(Int32).html) | Last modification time per page type # 10251. |
| Public Property | [PROJ\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_TYPE().html) | Project: Type # 10031. |
| Public Property | [PROJECT\_AREA](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJECT_AREA().html) | AutomationML: Building # 10952. |
| Public Property | [PROJECT\_ENTERPRISE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJECT_ENTERPRISE().html) | AutomationML: Company # 10950. |
| Public Property | [PROJECT\_HIGHEST\_REVISION\_INDEX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJECT_HIGHEST_REVISION_INDEX().html) | Highest revision index (change tracking) # 10098. |
| Public Property | [PROJECT\_INSTALLATIONSPACECOUNT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJECT_INSTALLATIONSPACECOUNT().html) | Number of layout spaces # 10304. |
| Public Property | [PROJECT\_POWERDISSIPATION\_FREQUENCY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJECT_POWERDISSIPATION_FREQUENCY().html) | Thermal design: Frequency # 10311. |
| Public Property | [PROJECT\_POWERDISSIPATION\_POWER\_OF\_ZONE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJECT_POWERDISSIPATION_POWER_OF_ZONE(Int32).html) | Thermal design: Total power dissipation for air-conditioning field # 10313. |
| Public Property | [PROJECT\_POWERDISSIPATION\_SIMULTANEITYFACTOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJECT_POWERDISSIPATION_SIMULTANEITYFACTOR().html) | Thermal design: Simultaneity factor # 10312. |
| Public Property | [PROJECT\_POWERDISSIPATION\_VOLTAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJECT_POWERDISSIPATION_VOLTAGE().html) | Thermal design: Voltage # 10310. |
| Public Property | [PROJECT\_PRODUCTION\_LINE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJECT_PRODUCTION_LINE().html) | AutomationML: Plant # 10953. |
| Public Property | [PROJECT\_SITE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJECT_SITE().html) | AutomationML: Works # 10951. |
| Public Property | [PROJECT\_SUBPROJECTORIGIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJECT_SUBPROJECTORIGIN().html) | Subproject of # 25100. |
| Public Property | [PROJECT\_WORK\_CELL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJECT_WORK_CELL().html) | AutomationML: Area # 10954. |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |
| Public Property | [PROPUSER\_LAST\_USERCODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROPUSER_LAST_USERCODE().html) | Last editor: ID # 3010. |
| Public Property | [PROPUSER\_LAST\_USEREMAIL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROPUSER_LAST_USEREMAIL().html) | Last editor: E-mail # 3013. |
| Public Property | [PROPUSER\_LAST\_USERNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROPUSER_LAST_USERNAME().html) | Last editor: Name # 3011. |
| Public Property | [PROPUSER\_LAST\_USERPHONE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROPUSER_LAST_USERPHONE().html) | Last editor: Phone # 3012. |
| Public Property | [SUBPROJECT\_NUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~SUBPROJECT_NUMBER().html) | Subproject number # 25101. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of ProjectPropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |


