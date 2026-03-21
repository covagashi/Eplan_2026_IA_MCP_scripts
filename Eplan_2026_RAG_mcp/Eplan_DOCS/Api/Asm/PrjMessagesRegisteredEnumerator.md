# PrjMessagesRegisteredEnumerator

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesRegisteredEnumerator.html

---

iterates over all registered electrotechnical messages of the system [Eplan::EplApi::EServices:](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesRegisteredCollection.html)

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.EServices.PrjMessagesRegisteredEnumerator**

Syntax

**C#**



public class PrjMessagesRegisteredEnumerator

public ref class PrjMessagesRegisteredEnumerator


Remarks

only electrotechnical messages that are licensed in the actual system will be returned

Example

getting all registered electrotechnical messages in the system

**C#**

```
PrjMessagesRegisteredCollection colPrjRegMsg = new PrjMessagesRegisteredCollection();

PrjMessagesRegisteredEnumerator itPrjRegMsg = colPrjRegMsg.GetRegisteredPrjMsgsEnumerator();

itPrjRegMsg.MoveNext();

int nNr=0;

do 

{

	ElectroMessage oEMsg = itPrjRegMsg.Current as ElectroMessage;

	if (oEMsg != null)

	{

		nNr++;

	}					

} while(itPrjRegMsg.MoveNext());
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [PrjMessagesRegisteredEnumerator Constructor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesRegisteredEnumerator~_ctor.html) | Default constructor |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Current](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesRegisteredEnumerator~Current.html) | gets the current element in [Eplan::EplApi::EServices:](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesRegisteredCollection.html) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Init](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesRegisteredEnumerator~Init.html) | Overloaded. initializes the enumerator for iterating over the collection of all registered electrotechnical messages in the system; |
| Public Method | [MoveNext](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesRegisteredEnumerator~MoveNext.html) | Advances the enumerator to the next element of [Eplan::EplApi::EServices:](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesRegisteredCollection.html) |
| Public Method | [Reset](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesRegisteredEnumerator~Reset.html) | Sets the enumerator to its initial position, which is before the first element in [Eplan::EplApi::EServices:](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesRegisteredCollection.html) |


