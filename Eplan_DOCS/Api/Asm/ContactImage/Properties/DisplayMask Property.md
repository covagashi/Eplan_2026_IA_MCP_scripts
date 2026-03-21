# DisplayMask Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ContactImage~DisplayMask.html

---

Gets or sets a value indicating whether position of this object is calculated automatically.

Syntax

**C#**



public ContactImage.Enums.DisplayMaskType DisplayMask {get; set;}

public:

property ContactImage.Enums.DisplayMaskType DisplayMask {

   ContactImage.Enums.DisplayMaskType get();

   void set (    ContactImage.Enums.DisplayMaskType value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectNotCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectNotCreatedException.html) | Thrown when object has not been created yet. |

Remarks

If property [AreUserDefinedSettings](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ContactImage~AreUserDefinedSettings.html) is false then default project settings are used for displaying this object in GED instead of this value.

Project settings are stored under path: 'EsCrossReference.ContactImage.MotorSwitchDisplayBitMask' when property [IsOnComponent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ContactImage~IsOnComponent.html) is `true`; 'EsCrossReference.ContactImage.ContactorDisplayBitMask' when property is `false`.
