# Active Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Option~Active.html

---

State of the Option.

Syntax

**C#**



public bool Active {get; set;}

public:

property bool Active {

   bool get();

   void set (    bool value);

}


#### Property Value

State of the option object. (true if active, false if not active)

Remarks

\Note that objects that are included in OptionFragment(s) of this Option become invalid after setting this property to false. After changing the state of an Option, please update the connections, using the Eplan.EplApi.HEServices.Generate.Connections()" /> method. The connections probably will be changed after toggling activation
