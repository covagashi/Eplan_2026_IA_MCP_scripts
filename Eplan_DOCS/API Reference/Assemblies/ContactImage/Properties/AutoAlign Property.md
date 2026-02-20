# AutoAlign Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ContactImage~AutoAlign.html

---

If `true` properties [Location](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ContactImage~Location.html) and [RelativeLocation](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ContactImage~RelativeLocation.html) are not used to display of ContactImage on page.

Syntax

**C#**



public bool AutoAlign {get; set;}

public:

property bool AutoAlign {

   bool get();

   void set (    bool value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectNotCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectNotCreatedException.html) | Thrown when object has not been created yet. |

Remarks

When auto align is enabled P8 is displaying the object base on value of property [IsOnComponent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ContactImage~IsOnComponent.html). In case when auto align is disabled contact image is displayed based on relative location to its parent.
