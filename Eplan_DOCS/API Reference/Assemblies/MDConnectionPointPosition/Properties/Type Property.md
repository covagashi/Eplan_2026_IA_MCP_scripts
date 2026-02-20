# Type Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionPointPosition~Type.html

---

The type of end treatment for the connection that will be connected to the connection point

Syntax

**C#**



public int Type {get; set;}

public:

property int Type {

   int get();

   void set (    int value);

}


Remarks

0=undefined, 1=cut, 2=strip, 3=crimp, 4=other, 5..64=used defined
