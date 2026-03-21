---
title: "IUnitOfWork"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_unit_of_work.htm"
file: "refscripting_r_unit_of_work"
category: "refscripting"
---

# IUnitOfWork

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  IUnitOfWork The IUnitOfWork describes the interface for the data access layer in the EEC. The interface is implemented by the UnitOfWork class, which loads and manages the objects for editing from the data memory. The changes made to EngineeringObjects within the Unit-Of-Work only become visible for the application when they are saved. This behavior makes the Unit-Of-Work comparable to a sandbox for the changes made, which can simply be discarded without saving.
