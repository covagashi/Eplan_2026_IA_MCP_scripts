# PrjMessagesEnumerator

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesEnumerator.html

---

supports a simple iteration over [Eplan::EplApi::EServices:](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection.html)

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.EServices.PrjMessagesEnumerator**

Syntax

**C#**



public class PrjMessagesEnumerator

public ref class PrjMessagesEnumerator


Example

getting all project messages after an offline run

**C#**

```
Check oCheck = new Check();

oCheck.VerifyProject(oProject);

PrjMessagesCollection colPrjMsg = new PrjMessagesCollection(oProject);

PrjMessagesEnumerator itPrjMsg = colPrjMsg.GetPrjMsgEnumerator();

itPrjMsg.MoveNext();

int nNr=0;

do 

{

	ProjectMessage oPrjMsg = itPrjMsg.Current as ProjectMessage;

	if (oPrjMsg != null)

	{

		nNr++;

	}					

} while(itPrjMsg.MoveNext());
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [PrjMessagesEnumerator Constructor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesEnumerator~_ctor.html) | Default constructor |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Current](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesEnumerator~Current.html) | gets the current element in [Eplan::EplApi::EServices:](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection.html) |
| Public Property | [CurrentProjectMessage](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesEnumerator~CurrentProjectMessage.html) | gets the current element in [Eplan::EplApi::EServices:](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection.html) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesEnumerator~Dispose().html) |  |
| Public Method | [MoveNext](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesEnumerator~MoveNext.html) | Advances the enumerator to the next element of [Eplan::EplApi::EServices:](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection.html) |
| Public Method | [Reset](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesEnumerator~Reset.html) | Sets the enumerator to its initial position, which is before the first element in [Eplan::EplApi::EServices:](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection.html) |
| Public Method | [SetProject](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesEnumerator~SetProject.html) | initializes the enumerator for iterating over the project messages collection |


