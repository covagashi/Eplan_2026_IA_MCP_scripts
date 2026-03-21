# ARTICLE_MATERIAL_LIST Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_MATERIAL_LIST().html

---

Material selection list # 26656.

Syntax

**C#**



public MDPropertyValue ARTICLE_MATERIAL_LIST {get; set;}

public:

property MDPropertyValue^ ARTICLE_MATERIAL_LIST {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Material or material composition from which an item is manufactured as a result of a manufacturing process in which the raw materials are brought into the final form by extrusion, forming, welding, etc. The following values are possible:

0 = Undefined

1 = Genuine glass

2 = ABS

3 = Die-cast aluminum

4 = Aluminum

5 = Aluminum, spray-finished

6 = Cast aluminum

7 = Brass

8 = Brass, nickel-plated

9 = Cast

10 = Cast iron

11 = Ceramic

12 = Copper

13 = Glass

14 = Metal

15 = Precious metal

16 = Non-ferrous metal

17 = Plastic

18 = Aluminum sheet

19 = Sheet steel, spray-finished

20 = Special metallic materials

21 = Stainless steel

22 = Steel, rust-proof

23 = Stainless steel - 1.4301

24 = Stainless steel - 1.4305

25 = Stainless steel - 1.4401

26 = Stainless steel - 1.4404

27 = Stainless steel - 1.4435

28 = Stainless steel - 1.4539

29 = Stainless steel - 1.4541

30 = Stainless steel - 1.4571

31 = Stainless steel - 1.4581

32 = Precision-cast stainless steel

33 = Steel

34 = Steel, coated

35 = Steel, zinc-coated

36 = Steel, galvanic zinc-plated

37 = Steel, highly corrosion-resistant

38 = Steel, hot galvanized

39 = Steel, stainless (stainless steel, rust-proof)

40 = Steel, sherardized

41 = Cast steel

42 = Plastic, metalized

43 = Aluminum, copper-clad

44 = Steel, copper-coated

45 = Aluminum alloy

46 = Stainless steel V2A

47 = Stainless steel V4A

48 = Copper / zinc-coated steel

49 = Copper / stainless steel

50 = Polycarbonate, fiberglass-reinforced (PC GF)
