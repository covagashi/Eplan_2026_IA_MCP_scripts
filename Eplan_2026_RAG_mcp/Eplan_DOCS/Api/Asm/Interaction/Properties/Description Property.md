# Description Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~Description.html

---

Description of undo step for this interaction.

Syntax

**C#**



public string Description {get; set;}

public:

property String^ Description {

   String^ get();

   void set (    String^ value);

}


Remarks

This text is used as description of undo step which is being created to handle changes made in method OnSuccess. Because the undo step is created just before OnSuccess is called it is necessary to set the description before this method is invoked (before ReqeustCode::Success is returned).

If the interaction is being started by a button, P8 sets a default description the same as tooltip of the button.
