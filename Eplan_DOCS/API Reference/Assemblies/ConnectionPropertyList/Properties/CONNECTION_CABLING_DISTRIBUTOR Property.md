# CONNECTION_CABLING_DISTRIBUTOR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_CABLING_DISTRIBUTOR(Int32).html

---

Topology: Connection splicers passed through (sorted) # 31137.

Syntax

**C#**



public PropertyValue CONNECTION_CABLING_DISTRIBUTOR( 

   int index

) {get; set;}

public:

property PropertyValue^ CONNECTION_CABLING_DISTRIBUTOR {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 20.

Outputs the DTs of the connection splicers which pass through the connection at a routing connection. The individual connection splicers are differentiated in the order from source to target through the index. This property can be used in reports.
