# ARTICLE_SURFACE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_SURFACE().html

---

Type of surface # 26225.

Syntax

**C#**



public MDPropertyValue ARTICLE_SURFACE {get; set;}

public:

property MDPropertyValue^ ARTICLE_SURFACE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Nature of the surface (machining, top coat). The following values are possible:

0 = Undefined

1 = Anodized

2 = Bichromated

3 = Chromated

4 = Hot galvanized

5 = Galvanic / electrolytic zinc-plated

6 = Brushed

7 = Primed

8 = Plastic-coated

9 = Spray-finished

10 = Powder-coated

11 = Other

12 = Hot-dip galvanized

13 = Untreated

14 = Copper-plated

15 = Nickel-plated

16 = Zinc-plated

17 = Tin-plated
