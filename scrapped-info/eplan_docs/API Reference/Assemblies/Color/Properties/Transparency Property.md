# Transparency Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Color~Transparency.html

---

Gets or sets transparency (0-255) due to internal technical limitations transparency is always stored as even value so 13 will be stored as 12 for example

Syntax

**C#**



public byte Transparency {get; set;}

public:

property byte Transparency {

   byte get();

   void set (    byte value);

}

