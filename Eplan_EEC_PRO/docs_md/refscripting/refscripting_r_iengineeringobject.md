---
title: "IEngineeringObject"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_iengineeringobject.htm"
file: "refscripting_r_iengineeringobject"
category: "refscripting"
---

# IEngineeringObject

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  IEngineeringObject IEngineeringObject is the interface that is implemented by all objects in the EEC. The actual implementation EngineeringObject is the super class of all objects. The following methods are available within the scripting in the IEngineeringObject interface:
     * IUnitOfWork getUnitOfWork() returns the UnitOfWork in which the IEngineeringObject is loaded.
     * boolean isClassEO() returns a Boolean value indicating whether it is a class.
     * boolean isInstanceEO() returns a Boolean value indicating whether it is an instance.
