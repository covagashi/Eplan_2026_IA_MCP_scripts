# API Pre-planning

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/API Pre-planning.html

---

The Eplan API now provides full access to pre-planning data. The following extensions were created for this purpose:

- Project-related classes from  Eplan.EplApi.DataModel.Planning  namespace

- The PrePlanningMacro  class and  Insert::PrePlanning  for the macro access

- PrePlanningService  for more complex operations

- New enum values

### Eplan.EplApi.DataModel.Planning namespace

Pre-Planning related objects are stored in the  Eplan.EplApi.DataModel.Planning  namespace. Here is an UML class diagram that shows their inheritance hierarchy:

[](graphs/preplanning.JPG "Click to enlarge")

### Migration of PPE API to Preplanning

Since Eplan 2.4, there is a new product for the pre-planning and basic engineering of plant and machinery:

**Eplan Preplanning Professional**

The product was developed on the basis of the Eplan Platform and in parallel to the Eplan PPE solution. Now it is the replacement of the Eplan PPE.

Because of this, Eplan PPE is no longer supported nor described in API Help since version 2.7. So please migrate your applications using PPE API to Preplanning API.

As a replacement, use classes from Eplan.EplApi.DataModel.Planning namespace and PrePlanningService.

Please note also, there will be no further development of the Eplan PPE system.
