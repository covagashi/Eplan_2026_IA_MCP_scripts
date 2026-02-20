# TakeConnectionPointDesignationsIntoAccount Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~TakeConnectionPointDesignationsIntoAccount.html

---

Gets or sets take connection point designations into account property.

Syntax

**C#**



public MacroBox.Enums.TakeConnectionPointDesignationsIntoAccount TakeConnectionPointDesignationsIntoAccount {get; set;}

public:

property MacroBox.Enums.TakeConnectionPointDesignationsIntoAccount TakeConnectionPointDesignationsIntoAccount {

   MacroBox.Enums.TakeConnectionPointDesignationsIntoAccount get();

   void set (    MacroBox.Enums.TakeConnectionPointDesignationsIntoAccount value);

}


Remarks

Property determines if connection point designations should be taken into account. When property is set to [MacroBox.Enums.TakeConnectionPointDesignationsIntoAccount.FromUserSettings](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox+Enums+TakeConnectionPointDesignationsIntoAccount.html), "User->Devices->General->Take the connection point designations into account during the device assignment" checkbox is considered.
