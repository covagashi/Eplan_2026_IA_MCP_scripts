# API Parts Management Extension

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/PartsManagementExtension.html

---

The API parts management extension feature can be used to add your own custom information to parts stored in the Eplan parts database. It is intended for information that you don't want to set as part properties.

You store this information in your own database and can attach it to the part and visualize it. When a part that references such custom information is exported or stored in a project, the information is stored as a string in the indexed  ARTICLE\_CUSTOM\_DATA\_INDEX  and  ARTICLE\_CUSTOM\_DATA\_VALUE  properties. The first property contains the name of the add-in to which the information belongs, and the second property contains the data string at the same index position.

To use this feature, you need to create an add-in. In this add-in, you must call the  MDPartsManagement.RegisterAddin(<Add-inName>, <ActionName>)  and  MDPartsManagement.RegisterItem(<Add-inName>, <ItemType>)  methods.

- <Add-inName>: Assembly name of your add-in, which is usually the DLL title without the extension  .dll.
- <ActionName>: In your add-in, you implement an action with the name you set in the  <ActionName>  parameter. This action will be called on different events in the parts management.
- <ItemType>: Specifies the kind of item for which you want to add the additional information or whose changes should trigger the events. Set the string  eplan.part  for parts or the following values:

### Possible values of the ItemType parameter

| ItemType value | Type of item |
| --- | --- |
| eplan.part | Parts |
| eplan.construction | Drilling patterns |
| eplan.connectionpointinfo | Connection point patterns |
| eplan.customer | Customers |
| eplan.manufacturer | Manufacturers / suppliers |
| eplan.accessorylist | Accessory lists |
| eplan.accessoryplacement | Accessory placements |

You can register multiple item types in your add-in:

```csharp
MDPartsManagement mDPartsManagement = new MDPartsManagement();
 mDPartsManagement.RegisterAddin("YourAddInName", "YourActionName");
 mDPartsManagement.RegisterItem("YourAddInName", "eplan.part");
 mDPartsManagement.RegisterItem("YourAddInName", "eplan.construction");
 mDPartsManagement.RegisterItem("YourAddInName", "eplan.accessoryplacement");
```

### Define a custom item type

It is also possible to define your own custom items in the parts management tree. You have to register your personal item as custom item type and use it instead of the predefined Eplan item types from the list above. For this, call the  MDPartsManagement.RegisterItem(<Add-inName>, <ItemType>)  method with your custom item type name as a string:

```csharp
mDPartsManagement.RegisterItem("YourAddInName", "YourCustomItemType");
```

### Events that call your action

The action that you implemented in your add-in and specified as  <ActionName>  parameter will then be called on different events in the parts management. Depending on the event, different parameters are passed to and returned via the  ActionCallingContext  each time as you can see in the list below. The  action  parameter is always set and represents the name of the event that was invoked. The  action  parameter can contain the following values: 

### Possible values of the action parameter in the ActionCallingContext

| action parameter value | Description | Parameters | |
| --- | --- | --- | --- |
| input | output |
| GetRootLevel | The first tree level is requested. | itemtype: Type of the item for which the root node is being requested | key: Identifying key   text: Text to display in the tree   subnode: (bool) Are further sub nodes available? (1 = yes, 0 = no) |
| GetNextLevel | The next level of the tree is requested. | itemtype: Type of the item being expanded in the tree  key: Node below which the next tree level is requested | key: Identifying key   text: Text to display in the tree   subnode: (bool) Are further sub nodes available? (1 = yes, 0 = no) |
| CreateDatabase | A new parts database was created. | database: Name of the created database |  |
| OpenDatabase | A new parts database was opened. | database: (string) Name of the newly opened database   readonly: (bool) Read-only status of the opened parts database (1 = "read-only", 0 = "read/write") |  |
| CloseDatabase | The current database was closed. |  |  |
| SelectItem | An item / part was selected in parts management. | itemtype: Item type of the selected element   partnr: Selected part number (if only one part is selected)   variant: Selected part variant (if only one variant is selected)   key: Identifying key of the selected element |  |
| PreShowTab | An item / part was selected in parts management. You have now the possibility to show / hide tab sheets that are registered for this element. | itemtype: Item type of the selected element   partnr: Selected part number (if only one part is selected)   variant: Selected part variant (if only one variant is selected)    key: Identifying key of the selected element   tabsheet: Tab sheet to be checked. The tab sheet was previously registered using  MDPartsManagement.RegisterTabsheet(...) | show: (bool) Should the tab sheet be displayed? (1 = yes (default), 0 = no) |
| SaveItem | An item / part was saved in parts management. | partnr: Selected part number (if only one part is selected)  variant: Selected part variant (if only one variant is selected)    itemtype: Item type of the selected element   key: Identifying key of the selected element |  |
| CopyItem | An item / part was copied in parts management (by the context menu items Copy and Paste). | itemtype: Item type of the copied element   key: Identifying key of the currently selected element (optional)   sourcekey: Identifying key of the element to copy |  |
| CutCopyItem | An item / part was cut in parts management (by the context menu items Cut and Paste). | itemtype: Item type of the cut element   key: Identifying key of the currently selected element (optional)   sourcekey: Identifying key of the element to cut | key: Identifying key of the created element |
| SelectCopyItem | The context menu item Copy was clicked in parts management tree. | itemtype: Item type of the copied element   key: Identifying key of the selected element (optional) |  |
| SelectCutItem | The context menu item Cut was clicked in parts management tree. | itemtype: Item type of the cut element   key: Identifying key of the selected element (optional) |  |
| SelectPasteItem | The context menu item Paste was clicked in parts management tree. | itemtype: Item type of the pasted element   key: Identifying key of the selected element (optional) |  |
| NewItem | An item / part was created in parts management. | itemtype: Item type of the newly created element   key: Identifying key of the currently selected element (optional) | key: Identifying key of the created element |
| DeleteItem | An item / part is being deleted from parts management. | itemtype: Item type of the currently selected to be deleted element   partnr: Selected part number (if only one part is selected)  variant: Selected part variant (if only one variant is selected)   key: Identifying key of the element to be deleted |  |
| AddPartToProject | A part from parts management is stored in the project. The add-in can add additional custom data to the stored part. | itemtype: Item type of the stored part (always "eplan.part")   key: Identifying key of the stored part | value: (string) Custom part data to be stored with the part inside the project (in properties  ARTICLE\_CUSTOM\_DATA\_INDEX  and  ARTICLE\_CUSTOM\_DATA\_VALUE) |
| AddPartToDatabase | A part is synchronized from the project to the parts management. The additional custom data can now be extracted and stored by the add-in. | itemtype: Item type of the synchronized part (always "eplan.part")   key: Identifying key of the synchronized part   value: (string) Custom part data stored with the part inside the project |  |
| AddItemToProject | An item (part, manufacturer, drilling pattern, ...) is stored in the project. The add-in can add additional custom data to the stored item. | itemtype: Item types of stored items (eplan.part, eplan.manufacturer, ...)   key: Identifying field of stored item's name: name of the stored items (abbreviated name of the manufacturer, name of drilling pattern, ...) | value: (string) Custom data stored with an item inside a project (in properties  ARTICLE\_CUSTOM\_DATA\_INDEX  and  ARTICLE\_CUSTOM\_DATA\_VALUE) |
| ExportEplanItem | A part is exported from parts management to a file. The additional custom data from the add-in can now be added to the export file. | itemtype: Type of the item to export (always "eplan.part")   key: Identifying key of the part to export | value: (string) Custom part data to be added to the export file |
| ImportEplanItem | A part is imported to parts management. The additional custom data from the file can now be extracted and stored by the add-in. | itemtype: Item type of the part to import (always "eplan.part")   key: Identifying key of the imported part   mode: Import mode. Possible values:        0 = Append new records only        1 = Update existing records only        2 = Update existing records and append new ones   value: (string) Custom part data to be extracted from the file and stored by the add-in. |  |
| ExportCustomItem | All custom items of the respective item type are exported from parts management.   Please mind that this only works with the XML export ("[XPamExportXml](XPamExportXml.html)" converter). | itemtype: Type of the item to export | value: Custom data of all items to be exported |
| ImportCustomItem | All custom items of the respective item type are imported from a file into parts management. They have to be saved by the add-in.   Please mind that this only works with the XML import ("[XPamExportXml](XPamExportXml.html)" converter). | itemtype: Type of the item to import   value: Custom data of all items to be imported   mode: Import mode. Possible values:     0 = Append new records only      1 = Update existing records only      2 = Update existing records and append new ones |  |
| WillDeleteItem | An item / article is to be deleted in parts management | itemtype: Item type of the selected item  key: Identifying field of the currently selected element  partnr: Selected item number (only if an item is selected)  variant: Selected variant (only if an article is selected) objectid: ID of a transient object being modified, (before changes) | allow: If set to 0, then  DeleteItem  is not called (delete is not executed) |
| WillSaveItem | An item / part will be saved in parts management | itemtype: Item type of the selected element   key: Identifying key of the selected element   partnr: Selected part number (if only one part is selected)   variant: Selected part variant (if only one variant is selected)   objectid: ID of a transient object being modified (before changes) | allow: When set to 0,  SaveItem  is not called (save is not performed) |

Inside of the  Execute  method of the action that you defined in your add-in, you can handle the events handed over via  action  parameter in the  ActionCallingContext  as shown in the example below exemplarily for  AddPartToProject,  SelectItem,  SaveItem  and  OpenDatabase.

The API parts management extension allows **event handling** for the Parts management dialog. Here, for example, the Parts management dialog event  SaveItem  is triggered as soon as the  action  parameter in the the  ActionCallingContext  takes the value  SaveItem:

```csharp
public bool Execute(ActionCallingContext ctx)
 {
     string action = "";
     ctx.GetParameter("action", ref action);
     switch (action)
     {
         case "AddPartToProject":
             // Do something when a part information is added to the project
             break;
         case "SelectItem":
             // Do something when a part is selected
             break;
         case "SaveItem":
         {
             Eplan.EplSDK.WPF.EEvent.WPFDialogEventManager em = new Eplan.EplSDK.WPF.EEvent.WPFDialogEventManager();
             em.send("XPartsManagementDialog", "SaveItem", sKey);
         }
             break;
            
         case "OpenDatabase":
             // Do something when the API parts management extension information is read
             break;
     }
     return true;
 }
```

### Add a custom tab / dialog

You can add custom tabs to the Parts management dialog to display your additional information on a custom dialog. To do this, you must call the  MDPartsManagement.RegisterTabsheet

(<Add-inName>, <ItemType>, <TabsheetName>)  method. As  <TabsheetName>  you need to specify your custom WPF-dialog (in XAML format) that will be shown when an item of the correspronding item type is selected:

```csharp
mDPartsManagement.RegisterTabsheet("YourAddInName", "eplan.part", "YourPartsTabsheetName");
 mDPartsManagement.RegisterTabsheet("YourAddInName", "YourCustomItemType", "YourCustomItemTabsheetName");
```

The API parts management extension **event handling** for the Parts management dialog also works for your custom dialogs. In the following example, the  SaveItem  event of the Parts management dialog is subscribed to. As a result, whenever an item is saved in the dialog, the  YourDialog\_SaveItem  method of a custom dialog class can now handle the data of the item to be saved:

```csharp
public class YourDialog : UserControl, IDialog
 {
     public YourDialog()
     {
         InitializeComponent();
         Eplan.EplSDK.WPF.EEvent.WPFDialogEventManager em = new Eplan.EplSDK.WPF.EEvent.WPFDialogEventManager();
         em.getOnWPFNotifyEvent("XPartsManagementDialog", "SaveItem").Notify += new Eplan.EplSDK.WPF.Interfaces.EEvent.NotifyEvent(YourDialog_SaveItem);
     }
 
     void YourDialog_SaveItem(string data)
     {
         // Handle your data to be saved in here
     }
 }
```