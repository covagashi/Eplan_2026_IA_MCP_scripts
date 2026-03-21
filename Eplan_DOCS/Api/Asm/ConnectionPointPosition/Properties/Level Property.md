# Level Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointPosition~Level.html

---

Level in a multi-level terminal.

Syntax

**C#**



public int Level {get; set;}

public:

property int Level {

   int get();

   void set (    int value);

}


Remarks

This property should be changed only for terminals. In other cases can cause abnormal behavior of local connection position points list.
