# Structure

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Structure.html

---

### The folder structure

Every add-on has the same folder structure. The folder names are marked with  <>  when names are optional and can be changed by the add-on developer.

Note:

This add-on folder can exist anywhere on the disk!

An add-on always consists of the same folder structure, which basically looks like this:

<Add-on>

<Add-on version>

BIN         Here, all binaries of the add-on are installed.

CFG         Here, all XML files and the  install.xml  are installed. The  install.xml  file is the base data.  
                                            The names of the folders are listed in the  install.xml  for copying the data to the Eplan base data.

<Images>

<Scripts>

<XML>

<'¦>

### The files

The most important file is the  install.xml. It contains all the information about the add-on and the Eplan version.

This paragraph shows an  install.xml  file example, which is created with the  EplAddonUtility.exe.

Tip:

For further information, about how to create an add-on with the  EplAddonUtility.exe  and which terms and conditions you should follow, see the "EplAddonUtility" documentation.

| XML | Copy Code |
| --- | --- |
| ``` 
 <Settings format="2">
   <CAT name="INSTALL">
     <MOD name="AF">
 <!'The application modifier is the unique identifier for this add-on. Either spaces or dots are allowed. Otherwise, the registration is not possible then. -->
       <Setting name="ApplicationModifier" type="string" info="Name modification for specific application configuration">
         <Val>MyAddon</Val>
       </Setting>
     </MOD>
   </CAT>
   <CAT name="STATION">
     <MOD name="SYSTEM">
       <LEV1 name="MyAddon">
 <!'This is the path to the xml file. This setting is patched by the installer -->
         <Setting name="XMLPath" type="string" info="patched path to install.xml">
           <Val>C:\Users\ Username \Desktop\MyAddon\CFG\</Val>
         </Setting>
 <!'This is the version of the add-on this setting is patched by the installer. -->
         <Setting name="Version" type="string" info="version nr of this addon">
           <Val>1.0.0</Val>
         </Setting>
 <!'This node describe the main versions, this add-on belongsto.. -->
         <LEV2 name="MainVersion">
           <LEV3 name="Basic">
 <!'This setting is the license identifier for the main version. All these licences MUST be available, only then this add-on will be registered -->
             <Setting name="Licences" type="string" info="Licence of Main Product to identify it">
               <Val>700</Val>
             </Setting>
 <!'This setting is the version identifier for the main version. By multiple versions, ONE of this licenc-es MUST be identical to the main version number, then this add-on is registered. -->
             <Setting name="Versions" type="string" info="Version of Main Product to identify it">
               <Val>2.9.0</Val>
             </Setting>
           </LEV3>
           <LEV3 name="FLUID">
             <Setting name="Licences" type="string" info="Licence of Main Product to identify it">
               <Val>703</Val>
             </Setting>
             <Setting name="Versions" type="string" info="Version of Main Product to identify it">
               <Val>2.9.0</Val>
             </Setting>
           </LEV3>
           <LEV3 name="VIEWER">
             <Setting name="Licences" type="string" info="Licence of Main Product to identify it">
               <Val>701</Val>
             </Setting>
             <Setting name="Versions" type="string" info="Version of Main Product to identify it">
               <Val>2.9.0</Val>
             </Setting>
           </LEV3>
           <LEV3 name="EDUCATION">
             <Setting name="Licences" type="string" info="Licence of Main Product to identify it">
               <Val>790</Val>
             </Setting>
             <Setting name="Versions" type="string" info="Version of Main Product to identify it">
               <Val>2.9.0</Val>
             </Setting>
           </LEV3>
           <LEV3 name="CPM">
             <Setting name="Licences" type="string" info="Licence of Main Product to identify it">
               <Val>786</Val>
             </Setting>
             <Setting name="Versions" type="string" info="Version of Main Product to identify it">
               <Val>2.9.0</Val>
             </Setting>
           </LEV3>
           <LEV3 name="TRIAL">
             <Setting name="Licences" type="string" info="Licence of Main Product to identify it">
               <Val>702</Val>
             </Setting>
             <Setting name="Versions" type="string" info="Version of Main Product to identify it">
               <Val>2.9.0</Val>
             </Setting>
           </LEV3>
           <LEV3 name="Preplanning">
             <Setting name="Licences" type="string" info="Licence of Main Product to identify it">
               <Val>1132</Val>
             </Setting>
             <Setting name="Versions" type="string" info="Version of Main Product to identify it">
               <Val>2.9.0</Val>
             </Setting>
           </LEV3>
           <LEV3 name="FluidHoseConfigurator">
             <Setting name="Licences" type="string" info="Licence of Main Product to identify it">
               <Val>1192</Val>
             </Setting>
             <Setting name="Versions" type="string" info="Version of Main Product to identify it">
               <Val>2.9.0</Val>
             </Setting>
           </LEV3>
           <LEV3 name="ProPanel">
             <Setting name="Licences" type="string" info="Licence of Main Product to identify it">
               <Val>565</Val>
             </Setting>
             <Setting name="Versions" type="string" info="Version of Main Product to identify it">
               <Val>2.9.0</Val>
             </Setting>
           </LEV3>
         </LEV2>
       </LEV1>
 <!'Now the base data the add-on has will be copied to the Eplan base data. Define as many pathes as possible. -->
       <LEV1 name="Basedata">
         <LEV2 name="MyAddon">
 <!'Copy all files behind this setting pathes to pathes for master data'¦ -->
           <Setting name="CopyTo" type="string" info="copy-to pathes for masterData">
             <Val>USER.TrDMProject.Masterdata.Pathnames..Projects</Val>
             <Val>USER.TrDMProject.Masterdata.Pathnames..Templates</Val>
             <Val>USER.TrDMProject.Masterdata.Pathnames..Symbols</Val>
             <Val>USER.TrDMProject.Masterdata.Pathnames..Forms</Val>
             <Val>USER.TrDMProject.Masterdata.Pathnames..Frames</Val>
             <Val>USER.TrDMProject.Masterdata.Pathnames..FctDefs</Val>
             <Val>USER.TrDMProject.Masterdata.Pathnames..Revisions</Val>
             <Val>USER.TrDMProject.Masterdata.Pathnames..Images</Val>
             <Val>USER.TrDMProject.Masterdata.Pathnames..DXFDWG</Val>
             <Val>USER.TrDMProject.Masterdata.Pathnames..MechanicalModels</Val>
             <Val>USER.SYSTEM.Pathnames..ExternalDocuments</Val>
             <Val>USER.SYSTEM.Pathnames..Scheme</Val>
           </Setting>
         </LEV2>
 <!''¦from pathes for master data. The count of the settings of 'CopyTo' and 'CopyFrom' has to be identical. -->
         <Setting name="CopyFrom" type="string" info="copy-from pathes for masterData">
           <Val>USER.TrDMProject.Masterdata.Pathnames.MyAddon.Projects</Val>
           <Val>USER.TrDMProject.Masterdata.Pathnames.MyAddon.Templates</Val>
           <Val>USER.TrDMProject.Masterdata.Pathnames.MyAddon.Symbols</Val>
           <Val>USER.TrDMProject.Masterdata.Pathnames.MyAddon.Forms</Val>
           <Val>USER.TrDMProject.Masterdata.Pathnames.MyAddon.Frames</Val>
           <Val>USER.TrDMProject.Masterdata.Pathnames.MyAddon.FctDefs</Val>
           <Val>USER.TrDMProject.Masterdata.Pathnames.MyAddon.Macros</Val>
           <Val>USER.TrDMProject.Masterdata.Pathnames.MyAddon.Images</Val>
           <Val>USER.TrDMProject.Masterdata.Pathnames.MyAddon.DXFDWG</Val>
           <Val>USER.TrDMProject.Masterdata.Pathnames.MyAddon.MechanicalModels</Val>
           <Val>USER.SYSTEM.Pathnames.MyAddon.ExternalDocuments</Val>
           <Val>USER.SYSTEM.Pathnames.MyAddon.Scheme</Val>
         </Setting>
       </LEV1>
     </MOD>
   </CAT>
   <CAT name="USER">
     <MOD name="TrDMProject">
       <LEV1 name="Masterdata">
         <LEV2 name="Pathnames">
           <LEV3 name="MyAddon">
             <Setting name="Projects" type="string" info="file path to masterData">
               <Val>C:\Users\ Username \Desktop\MyAddon\CFG\MyAddon\Projects</Val>
             </Setting>
             <Setting name="Templates" type="string" info="file path to masterData">
               <Val>C:\Users\ Username \Desktop\MyAddon\CFG\MyAddon\Templates</Val>
             </Setting>
             <Setting name="Symbols" type="string" info="file path to masterData">
               <Val>C:\Users\ Username \Desktop\MyAddon\CFG\MyAddon\Symbols</Val>
             </Setting>
             <Setting name="Forms" type="string" info="file path to masterData">
               <Val>C:\Users\ Username \Desktop\MyAddon\CFG\MyAddon\Forms</Val>
             </Setting>
             <Setting name="Frames" type="string" info="file path to masterData">
               <Val>C:\Users\ Username \Desktop\MyAddon\CFG\MyAddon\PlotFrames</Val>
             </Setting>
             <Setting name="FctDefs" type="string" info="file path to masterData">
               <Val>C:\Users\ Username \Desktop\MyAddon\CFG\MyAddon\FunctionDefinition</Val>
             </Setting>
             <Setting name="Macros" type="string" info="file path to masterData">
               <Val>C:\Users\ Username \Desktop\MyAddon\CFG\MyAddon\Macros</Val>
             </Setting>
             <Setting name="Images" type="string" info="file path to masterData">
               <Val>C:\Users\ Username \Desktop\MyAddon\CFG\MyAddon\Images</Val>
             </Setting>
             <Setting name="DXFDWG" type="string" info="file path to masterData">
               <Val>C:\Users\ Username \Desktop\MyAddon\CFG\MyAddon\DXF_DWG</Val>
             </Setting>
             <Setting name="MechanicalModels" type="string" info="file path to masterData">
               <Val>C:\Users\ Username \Desktop\MyAddon\CFG\MyAddon\Mechanical models</Val>
             </Setting>
             <Setting name="Scripts" type="string" info="file path to masterData">
               <Val>C:\Users\ Username \Desktop\MyAddon\CFG\MyAddon\Documents</Val>
             </Setting>
             <Setting name="Scheme" type="string" info="file path to masterData">
               <Val>C:\Users\Username\Desktop\MyAddon\CFG\MyAddon\Schemes</Val>
             </Setting>
           </LEV3>
         </LEV2>
       </LEV1>
     </MOD>
     <MOD name="System">
       <LEV1 name="Pathnames">
         <LEV2 name="MyAddon" />
       </LEV1>
     </MOD>
   </CAT>
 </Settings>
 ``` | |

### Information about the settings

ApplicationModifier:  
The identifier for this add-on. This has to be a unique name without blanks and dots.

XMLPath:  
Location of CFG folder of add-on

Version:  
This is the version number of the add-on.

MainVersion:  
One sub-node belongs to one Eplan version. The  Basic  node contains the licence information and version information for Eplan Electric P8.

Licences:  
Add-on program validity. All of the licences must be available, so this add-on can be registered for this main version.

Versions:  
Add-on version validity. One of the version numbers must match the Eplan version number, so this add-on can be registered. The version number can contain a \* as a wildcard. This is interpreted as "any".

### The API add-ins

It is possible to list the API add-ins in an XML file with any name.

| XML | Copy Code |
| --- | --- |
| ``` 
 <Settings format="2">
   <CAT name="STATION">
     <MOD name="AF">
       <LEV1 name="ApiModules">
         <Setting name="MyAddon" type="string" info="">
           <Val>Eplan.EplAddin.Addin_2_8</Val>
         </Setting>
       </LEV1>
     </MOD>
   </CAT>
 </Settings>
 ``` | |

All API modules in the setting  ApiModules  are registered and loaded.

When an API add-in has a linked DLL in the add-on binary path, the DLL should be registered as a reference. This is the list in "[API Reference](API Reference.html)". Then Eplan will always be able to resolve this API add-in.

### The Scripts

If a script is to be registered when the add-on is registered, an XML file must have a content similar to this:

| XML | Copy Code |
| --- | --- |
| ``` 
 <Settings format="2">
   <CAT name="STATION">
     <MOD name="AF">
       <LEV1 name="Scripts">
         <Setting name="MyAddon" type="string" info="">
           <Val>BIN\myScript.cs</Val>
         </Setting>
       </LEV1>
     </MOD>
   </CAT>
 </Settings>
 ``` | |

The script file location is either an absolute path or a relative one. The relative path is calculated from the add-on path, where the  BIN  folder and the  CFG  folder is in.

### Ribbons

With the version 2022, it is possible to import a ribbon bar or rather ribbon tabs with their children (for more information, please take a look at the [Ribbon Bar](TheRibbon.html) chapter) when the add-on is registered.

| XML | Copy Code |
| --- | --- |
| ``` 
 <Settings format="2">
   <CAT name="USER">
     <MOD name="AF">
       <LEV1 name="Ribbon">
         <Setting name="Ribbonbartest" type="string" info="">
           <Val>CFG\myRibbonTab.xml</Val>
         </Setting>
       </LEV1>
     </MOD>
   </CAT>
 </Settings>
 ``` | |

The custom ribbon tab is imported from the XML file when the add-on is registered. The user can remove the ribbon tab by customizing the ribbon (i.e. when the user changes his workspace). Unregistering the add-on will also remove the ribbon tab.