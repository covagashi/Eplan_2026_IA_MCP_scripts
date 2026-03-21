---
title: "Code basic objects"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_basic_codeobjects.htm"
file: "eecplc_k_basic_codeobjects"
category: "eecplc"
---

# Code basic objects

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Code basic objects

These are:

     * Controller
     * Coupler
     * Terminal
     * Fragment
     * Method

These basic objects are already predefined in the platform-specific system libraries (such as STEP 7, CoDeSys, etc.). The Method basic object is now contained in the CoDeSys system library. For communications purposes, they can be connected with each other via communication channels. Use of the PLC objects Coupler and Terminal is not mandatory. They can also be represented using basic mechatronic objects. The PLC object Controller, however, is always required if the program code is to be modeled in EEC, because this object is simultaneously used as a root object in the discipline structure. Regardless of the object being used, it is nevertheless important to pay attention to usage of the standard interfaces IController, ICoupler and ITerminal; otherwise, the IO generator cannot operate free of errors.
