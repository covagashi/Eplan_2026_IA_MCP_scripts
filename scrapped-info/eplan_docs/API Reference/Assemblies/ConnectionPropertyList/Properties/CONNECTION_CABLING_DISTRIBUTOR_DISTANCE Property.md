# CONNECTION_CABLING_DISTRIBUTOR_DISTANCE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_CABLING_DISTRIBUTOR_DISTANCE(Int32).html

---

Topology: Distance between connection splicers and source # 31138.

Syntax

**C#**



public PropertyValue CONNECTION_CABLING_DISTRIBUTOR_DISTANCE( 

   int index

) {get; set;}

public:

property PropertyValue^ CONNECTION_CABLING_DISTRIBUTOR_DISTANCE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 20.

Outputs the position of the connection splicers passed through on this connection at a routing connection. To this purpose the distance between the connection splicer and the source of the connection is specified. The individual connection splicers are differentiated in the order from source to target through the index. This property can be used in reports.
