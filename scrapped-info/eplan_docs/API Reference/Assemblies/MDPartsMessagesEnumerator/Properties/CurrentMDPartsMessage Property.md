# CurrentMDPartsMessage Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsMessagesEnumerator~CurrentMDPartsMessage.html

---

gets the current element in [Eplan::EplApi::MasterData:](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseMessages.html)

Syntax

**C#**



public virtual MDPartsMessage CurrentMDPartsMessage {get;}

public:

virtual property MDPartsMessage^ CurrentMDPartsMessage {

   MDPartsMessage^ get();

}


#### Property Value

the current element

Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown when the enumerator is positioned before the first element of the collection or after the last element. |

Remarks

must be called to advance the enumerator to the first element of the collection before reading the current value
