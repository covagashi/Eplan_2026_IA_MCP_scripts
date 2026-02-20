# SymbolLibraryPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList.html

---

This class represents collection of properties of [SymbolLibrary](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibrary.html) class. Please check also base classes for other properties which are available for [SymbolLibrary](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibrary.html) objects: [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         **Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList**

Syntax

**C#**



[DefaultMember("Property")]

public class SymbolLibraryPropertyList : Eplan.EplApi.DataModel.StorableObjectPropertyList

[DefaultMember("Property")]

public ref class SymbolLibraryPropertyList : public Eplan.EplApi.DataModel.StorableObjectPropertyList


Remarks

It uses operator[] in order to access its elements (stored properties).

Property list is a container for property values and just like them can be `online` or `offline`. If property list is `online` it means that is associated with properties of some StorableObject or other property list. In this case if any property is added, changed or removed from property list the result is also visible in related objects. Whether property list is online or offline is being determine in time of it's creation and can not be changed.

Example

Example shows usage of online an offline property list:

**C#**

```
// creation of persistent property list

FunctionPropertyList oPersistentPropertyList1 = oFunction.Properties;

oPersistentPropertyList1.FUNC_COMMENT = "Comment";

// now oFunction.Properties.FUNC_COMMENT is equal "Comment"

FunctionPropertyList oPersistentPropertyList2 = new FunctionPropertyList(oFunction);

oPersistentPropertyList2.FUNC_COMMENT = "Test";

// now oFunction.Properties.FUNC_COMMENT is equal "Test"

// creation of transient property list

FunctionPropertyList oTransientPropertyList = new FunctionPropertyList();

oTransientPropertyList.FUNC_COMMENT = "Test comment";

oFunction.Properties.FUNC_COMMENT = oTransientPropertyList.FUNC_COMMENT;

oTransientPropertyList.FUNC_COMMENT = "Transient comment";

// now oTransientPropertyList.FUNC_COMMENT is equal "Test comment"

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [SymbolLibraryPropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [INSTANCE\_SIZE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~INSTANCE_SIZE().html) | Font size # 19017. |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |
| Public Property | [PROPUSER\_LAST\_USERCODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~PROPUSER_LAST_USERCODE().html) | Last editor: ID # 3010. |
| Public Property | [PROPUSER\_LAST\_USEREMAIL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~PROPUSER_LAST_USEREMAIL().html) | Last editor: E-mail # 3013. |
| Public Property | [PROPUSER\_LAST\_USERNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~PROPUSER_LAST_USERNAME().html) | Last editor: Name # 3011. |
| Public Property | [PROPUSER\_LAST\_USERPHONE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~PROPUSER_LAST_USERPHONE().html) | Last editor: Phone # 3012. |
| Public Property | [SYMBLIB\_COMPANY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_COMPANY().html) | Company code # 15019. |
| Public Property | [SYMBLIB\_CONNECTIONERROR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_CONNECTIONERROR(Int32).html) | Error: Connection point # 15101. |
| Public Property | [SYMBLIB\_CREATIONDATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_CREATIONDATE().html) | Creation date # 15021. |
| Public Property | [SYMBLIB\_CREATOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_CREATOR().html) | Creator # 15020. |
| Public Property | [SYMBLIB\_DESC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_DESC().html) | Symbol library description # 15011. |
| Public Property | [SYMBLIB\_ERRORCOUNT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_ERRORCOUNT().html) | Number of messages # 15099. |
| Public Property | [SYMBLIB\_ERRORSYMBOLED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_ERRORSYMBOLED(Int32).html) | Error (symbol editor) # 15201. |
| Public Property | [SYMBLIB\_FRAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_FRAME().html) | Plot frame to edit symbol # 15030. |
| Public Property | [SYMBLIB\_FUNCDEFERROR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_FUNCDEFERROR(Int32).html) | Error: Function definition # 15100. |
| Public Property | [SYMBLIB\_FUNCTYPEERROR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_FUNCTYPEERROR(Int32).html) | Error: Representation type # 15103. |
| Public Property | [SYMBLIB\_GRAPHICERROR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_GRAPHICERROR(Int32).html) | Error: Symbol graphic # 15105. |
| Public Property | [SYMBLIB\_IMPORTERROR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_IMPORTERROR(Int32).html) | Error (import) # 15200. |
| Public Property | [SYMBLIB\_LASTMODIFICATIONDATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_LASTMODIFICATIONDATE().html) | Modification date (automatic) # 15023. |
| Public Property | [SYMBLIB\_LASTMODIFICATOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_LASTMODIFICATOR().html) | Last editor: Sign-in name # 15022. |
| Public Property | [SYMBLIB\_LOCKEDSYMBOLCOUNT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_LOCKEDSYMBOLCOUNT().html) | Number of locked symbols # 15016. |
| Public Property | [SYMBLIB\_LOGICERROR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_LOGICERROR(Int32).html) | Error: Connection point logic # 15104. |
| Public Property | [SYMBLIB\_LOGICGRID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_LOGICGRID().html) | Grid # 15013. |
| Public Property | [SYMBLIB\_MANUALDATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_MANUALDATE().html) | Modification date (manual) # 15024. |
| Public Property | [SYMBLIB\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_NAME().html) | Symbol library # 15000. |
| Public Property | [SYMBLIB\_OLDNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_OLDNAME().html) | Name of original symbol library # 15098. |
| Public Property | [SYMBLIB\_PLACEDPROPERROR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_PLACEDPROPERROR(Int32).html) | Error: Property placement # 15106. |
| Public Property | [SYMBLIB\_SUPPLEMENTARYFIELD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_SUPPLEMENTARYFIELD(Int32).html) | Supplementary field # 15901. |
| Public Property | [SYMBLIB\_SYMBOLCOUNT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_SYMBOLCOUNT().html) | Number of symbols # 15015. |
| Public Property | [SYMBLIB\_VARIANTCOUNT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_VARIANTCOUNT().html) | Number of symbol variants # 15017. |
| Public Property | [SYMBLIB\_VARIANTERROR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_VARIANTERROR(Int32).html) | Error: Symbol variant # 15102. |
| Public Property | [SYMBLIB\_VERSION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_VERSION().html) | Version # 15012. |
| Public Property | [SYMBOLLIBRARY\_REMOVED\_VARIANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBOLLIBRARY_REMOVED_VARIANT().html) | Compressed symbol library # 15031. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of SymbolLibraryPropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |


