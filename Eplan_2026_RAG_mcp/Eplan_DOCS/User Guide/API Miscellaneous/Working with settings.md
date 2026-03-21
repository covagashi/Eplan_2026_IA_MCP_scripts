# Working with settings

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/WorkingWithSettings.html

---

Eplan has a settings database in which user preferences such as used fonts, colors, etc. are stored.

In the GUI it is visible under the ribbon item File > Settings....

Using the API, we can modify the database and also create custom values for use in API applications.

We can distinguish the following categories of settings:

- **Company settings**: These settings should be located on a server and should be the same for the entire company.
- **Workstation settings**: These settings apply to a single computer and should be stored on a local hard drive.
- **User settings**: These settings, such as dimensions and positions of toolbars and dialogs, also need to be stored on a central server so that a user can use his own settings on another workstation.
- **Project-related settings**: These settings are independent of a user or a workstation. They are stored in a project. See the ["Project Settings"](DM_ProjectSettings.html) chapter.

For more details, please refer to the "Settings: Operation" chapter of the Eplan Help.

### Format of settings

The settings database is organized in a tree structure: Particular branches refer to similar settings and leaves store relevant values.

Using the export functionality we can access their values, even those that are not visible in the Options > Settings dialog. The format of the file is  XML, and here is its XML scheme definition:

|  | Copy Code |
| --- | --- |
| ``` 
 <?xml version="1.0" encoding="utf-8"?>
 <xs:schema attributeFormDefault="unqualified" elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">
   <xs:group name="levlSettingGroup">
     <xs:sequence>
       <xs:element name="Setting">
         <xs:complexType>
           <xs:sequence>
             <xs:element minOccurs="0" maxOccurs="unbounded" name="Val" type="xs:anyType" />
           </xs:sequence>
           <xs:attribute name="name" use="required">
             <xs:simpleType>
               <xs:restriction base="xs:string">
                 <xs:pattern value="[a-zA-ZÃ¤Ã¶Ã¼ÃÃÃ0-9_\s\+\-#\[\]]*"/>
               </xs:restriction>
             </xs:simpleType>
           </xs:attribute>
           <xs:attribute name="type" use="required">
             <xs:simpleType>
               <xs:restriction base="xs:string">
                 <xs:enumeration value="bool"/>
                 <xs:enumeration value="int"/>
                 <xs:enumeration value="unsigned int"/>
                 <xs:enumeration value="long"/>
                 <xs:enumeration value="unsigned long"/>
                 <xs:enumeration value="double"/>
                 <xs:enumeration value="string"/>
                 <xs:enumeration value="mlstring"/>
               </xs:restriction>
             </xs:simpleType>
           </xs:attribute>
           <xs:attribute name="info" type="xs:string" use="optional" />
           <xs:attribute name="desc" type="xs:string" use="optional" />
           <xs:attribute name="range" type="xs:string" use="optional" />
         </xs:complexType>
       </xs:element>
     </xs:sequence>   
   </xs:group>
   <xs:attributeGroup name="levlAttrGroup">
     <xs:attribute name="name" use="required">
       <xs:simpleType>
         <xs:restriction base="xs:string">
           <xs:pattern value="[a-zA-ZÃ¤Ã¶Ã¼ÃÃÃÃ0-9_\s\+\-#\[\](),\/@:;\*&amp;]*"/>
         </xs:restriction>
       </xs:simpleType>
     </xs:attribute>
     <xs:attribute name="info" type="xs:string" use="optional" />
     <xs:attribute name="nodekind" type="xs:string" use="optional" />
   </xs:attributeGroup> 
   <xs:element name="Settings">
     <xs:complexType>
       <xs:sequence>
         <xs:element minOccurs="0" maxOccurs="5" name="CAT">                           
           <xs:complexType>               
             <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="unbounded" name="MOD">
                 <xs:complexType>
                   <xs:sequence>
                     <xs:choice minOccurs="0" maxOccurs="unbounded">
                       <xs:element name="LEV1">
                           <xs:complexType mixed="true">
                             <xs:sequence>
                               <xs:choice minOccurs="0" maxOccurs="unbounded">
                                 <xs:element name="LEV2">
                                   <xs:complexType>
                                     <xs:sequence>
                                       <xs:choice minOccurs="0" maxOccurs="unbounded">                                       
                                         <xs:element name="LEV3">
                                           <xs:complexType>
                                             <xs:sequence>
                                               <xs:choice minOccurs="0" maxOccurs="unbounded">
                                                 <xs:element name="LEV4">
                                                   <xs:complexType>
                                                     <xs:sequence>
                                                       <xs:choice minOccurs="0" maxOccurs="unbounded">
                                                         <xs:element name="LEV5">
                                                           <xs:complexType>
                                                             <xs:sequence>
                                                               <xs:choice minOccurs="0" maxOccurs="unbounded">
                                                                 <xs:element name="LEV6">
                                                                   <xs:complexType>
                                                                     <xs:sequence>
                                                                       <xs:choice minOccurs="0" maxOccurs="unbounded">
                                                                         <xs:element name="LEV7">
                                                                           <xs:complexType>
                                                                             <xs:sequence>
                                                                               <xs:choice minOccurs="0" maxOccurs="unbounded">
                                                                                 <xs:element name="LEV8">
                                                                                   <xs:complexType>
                                                                                     <xs:sequence>
                                                                                       <xs:choice minOccurs="0" maxOccurs="unbounded">
                                                                                         <xs:element name="LEV9">
                                                                                           <xs:complexType>
                                                                                             <xs:sequence>
                                                                                               <xs:choice minOccurs="0" maxOccurs="unbounded">
                                                                                                 <xs:element name="LEV10">
                                                                                                   <xs:complexType>
                                                                                                     <xs:group ref="levlSettingGroup"/>
                                                                                                     <xs:attributeGroup ref="levlAttrGroup"/>                                                                                                  
                                                                                                   </xs:complexType>
                                                                                                 </xs:element>
                                                                                                 <xs:group ref="levlSettingGroup"/>
                                                                                               </xs:choice>
                                                                                             </xs:sequence>                                                                                           
                                                                                             <xs:attributeGroup ref="levlAttrGroup"/>
                                                                                           </xs:complexType>
                                                                                         </xs:element>
                                                                                         <xs:group ref="levlSettingGroup"/>
                                                                                       </xs:choice>
                                                                                     </xs:sequence>
                                                                                     <xs:attributeGroup ref="levlAttrGroup"/>                                                                                
                                                                                   </xs:complexType>
                                                                                 </xs:element>
                                                                                 <xs:group ref="levlSettingGroup"/>
                                                                               </xs:choice>
                                                                             </xs:sequence>
                                                                             <xs:attributeGroup ref="levlAttrGroup"/>
                                                                           </xs:complexType>
                                                                         </xs:element>
                                                                         <xs:group ref="levlSettingGroup"/>
                                                                       </xs:choice>
                                                                     </xs:sequence>
                                                                     <xs:attributeGroup ref="levlAttrGroup"/>
                                                                   </xs:complexType>
                                                                 </xs:element>
                                                                 <xs:group ref="levlSettingGroup"/>
                                                               </xs:choice>
                                                             </xs:sequence>
                                                             <xs:attributeGroup ref="levlAttrGroup"/>
                                                           </xs:complexType>
                                                         </xs:element>
                                                         <xs:group ref="levlSettingGroup"/>
                                                       </xs:choice>
                                                     </xs:sequence>
                                                     <xs:attributeGroup ref="levlAttrGroup"/>
                                                   </xs:complexType>
                                                 </xs:element>
                                                 <xs:group ref="levlSettingGroup"/>
                                               </xs:choice>
                                             </xs:sequence>
                                             <xs:attributeGroup ref="levlAttrGroup"/>
                                           </xs:complexType>
                                         </xs:element>
                                         <xs:group ref="levlSettingGroup"/>
                                       </xs:choice>
                                     </xs:sequence>
                                     <xs:attributeGroup ref="levlAttrGroup"/>
                                   </xs:complexType>
                                 </xs:element>
                                 <xs:group ref="levlSettingGroup"/>
                               </xs:choice>
                             </xs:sequence>
                             <xs:attributeGroup ref="levlAttrGroup"/>                          
                           </xs:complexType>
                         </xs:element>
                       <xs:group ref="levlSettingGroup"/>                               
                     </xs:choice>
                   </xs:sequence>
                   <xs:attributeGroup ref="levlAttrGroup"/>
                 </xs:complexType>
               </xs:element>                 
             </xs:sequence>                 
             <xs:attribute name="name" use="required">               
               <xs:simpleType>
                 <xs:restriction base="xs:string">
                   <xs:enumeration value="COMPANY"/>
                   <xs:enumeration value="INSTALL"/>
                   <xs:enumeration value="PROJECT"/>
                   <xs:enumeration value="STATION"/>
                   <xs:enumeration value="USER"/>
                 </xs:restriction>
               </xs:simpleType>
             </xs:attribute>
           </xs:complexType>
         </xs:element>
       </xs:sequence>
       <xs:attribute name="format" type="xs:unsignedByte" use="required" />
     </xs:complexType>
   </xs:element>
 </xs:schema>
 ``` | |

Here is a simplified description of the settings file:

- **name**  ' The name of a setting that must be always unique within a setting node.
- **Settings**  ' This is the root node.
- **CAT**  ' Then there are 0-5 possible  CAT  nodes with the  name  attribute one of the following:  COMPANY,  PROJECT,  STATION,  USER,  INSTALL.
- **MOD**  ' Then there is a subnode  MOD, which is a kind of namespace for a setting.
- **LEV**  ' Then there are subnodes  LEV1  up to  LEV10  that specify a path to a leaf node.
- **Setting**  ' Next there is a leaf node  Setting  which stores the following data:
  - **Val**  ' The setting value in the  Val  node. There can be more such nodes, each of them is accessible by individual index parameter.
  - **type**  ' Defines the expected settings type.
  - **range**  ' The range of values
    - ... does not concern Boolean data types
    - ... can consist of a token list for strings: (for example "arial/courier/tahoma")
    - ... can have a upper and lower bound for numbers in the format "from/to" (separated by slash): "1/10;20/100"

### 

### Example of settings in XML format

Here is an example of a simple user setting from the User > Display > Identifier branch:

|  | Copy Code |
| --- | --- |
| ``` 
 <?xml version="1.0" encoding="utf-8" ?>
 <Settings ver="2.4.1" format="2">
  <CAT name="USER">
   <MOD name="PLEditorGui">
    <Setting name="SortMode" type="int">
     <Val>1</Val>
    </Setting>
   </MOD>
  </CAT>
 </Settings>
 ``` | |

Below is another example of workstation settings (Workstation > Graphical editing > Print):

|  | Copy Code |
| --- | --- |
| ``` 
 <?xml version="1.0" encoding="utf-8" ?>
 <Settings ver="2.4.1" format="2">
  <CAT name="STATION">
   <MOD name="Print">
    <Setting name="BlackWhite" type="bool">
     <Val>1</Val>
    </Setting>
    <Setting name="BottomMargin" type="double" range="0/1000">
     <Val>0</Val>
    </Setting>
    <Setting name="ConsiderPageScale" type="bool">
     <Val>1</Val>
    </Setting>
    <Setting name="FitToPage" type="bool">
     <Val>1</Val>
    </Setting>
    <Setting name="KeepAspectRatio" type="bool">
     <Val>1</Val>
    </Setting>
    <Setting name="LeftMargin" type="double" range="0/1000">
     <Val>0</Val>
    </Setting>
    <Setting name="Position" type="unsigned long" range="0/8">
     <Val>0</Val>
    </Setting>
    <Setting name="RightMargin" type="double" range="0/1000">
     <Val>0</Val>
    </Setting>
    <Setting name="ScaleHorizontal" type="double" range="0.001/1000">
     <Val>1.0</Val>
    </Setting>
    <Setting name="ScaleVertical" type="double" range="0.001/1000">
     <Val>1.0</Val>
    </Setting>
    <Setting name="TopMargin" type="double" range="0/1000">
     <Val>0</Val>
    </Setting>
   </MOD>
  </CAT>
 </Settings>
 ``` | |

Here is example of indexed settings from Company > Graphical editing > Fonts.

|  | Copy Code |
| --- | --- |
| ``` 
 <?xml version="1.0" encoding="utf-8" ?>
 <Settings ver="2.4.3" format="2">
  <CAT name="COMPANY">
   <MOD name="GedViewer">
    <Setting name="Fonts" type="mlstring">
     <Val>??_??@Arial;</Val>
     <Val>??_??@Verdana;</Val>
     <Val>??_??@Georgia;</Val>
     <Val>??_??@Tahoma;zh_CN@??;</Val>
     <Val>??_??@Tahoma;zh_CN@??;</Val>
     <Val>??_??@Tahoma;zh_CN@??;</Val>
     <Val>??_??@Tahoma;zh_CN@??;</Val>
     <Val>??_??@Tahoma;zh_CN@??;</Val>
     <Val>??_??@Tahoma;zh_CN@??;</Val>
     <Val>??_??@Tahoma;zh_CN@??;</Val>
    </Setting>
   </MOD>
  </CAT>
 </Settings>
 ``` | |

### API classes for working with settings

Settings  ' functions for reading, writing and creating User, Company or Workstation settings.

ProjectSettings  ' functions for reading, writing and creating project dependant settings. Refer to the "See Also" section.

SettingNode  ' functions for managing the settings hierarchy (only User, Company or Workstation settings).

SchemeSetting  ' functions for managing a settings group (scheme). Only for User, Company or Workstation settings.

ProjectSchemeSetting  ' the same as  SchemeSetting  but for project settings.

ProjectSettingNode  ' the same as  SettingNode  but for project settings.

### Examples

Adding, setting and getting settings:

**C#**
```csharp
Eplan.EplApi.Base.Settings oSettings = new Eplan.EplApi.Base.Settings();

    oSettings.AddStringSetting("USER.DEMOSETTINGS.TEST1", new string[] { },

    new string[] { }, ISettings.CreationFlag.Insert);

    oSettings.SetStringSetting("USER.DEMOSETTINGS.TEST1", "Testwert1", 0);

    String strTest1 = oSettings.GetStringSetting("USER.DEMOSETTINGS.TEST1", 0);

    if (strTest1 == "Testwert1")

         Console.Out.WriteLine("SetGetAddSetting OK!");

    else

         Console.Out.WriteLine("SetGetAddSetting not OK!");

oSettings.AddStringSetting("USER.DEMOSETTINGS.TEST1", New String() {}, New String() {}, ISettings.CreationFlag.Insert)

oSettings.SetStringSetting("USER.DEMOSETTINGS.TEST1", "Testwert1", 0)

    dec.Decide(EnumDecisionType.eOkDecision,"SetGetAddSetting OK!","", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)

Else

    dec.Decide(EnumDecisionType.eOkDecision,"SetGetAddSetting not OK!","",EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
```

Example of merging nodes using  SettingNode:

**C#**
```csharp
Eplan.EplApi.Base.SettingNode oSettingNode = new Eplan.EplApi.Base.SettingNode("STATION.AF.Interfaces");

        uint uiCountOfSettings = oSettingNode.GetCountOfSettings();

        uint uiCountOfNodes = oSettingNode.GetCountOfNodes();

        System.Collections.Specialized.StringCollection

          strColl1 = new System.Collections.Specialized.StringCollection();

        oSettingNode.GetListOfAllSettings(ref strColl1, false);

        System.Collections.Specialized.StringCollection

          strColl2 = new System.Collections.Specialized.StringCollection();

        oSettingNode.GetListOfNodes(ref strColl2, false);

        System.Collections.Specialized.StringCollection

          strColl3 = new System.Collections.Specialized.StringCollection();

        oSettingNode.GetListOfSettings(ref strColl3, false);

        Eplan.EplApi.Base.SettingNode oMuster = new

          Eplan.EplApi.Base.SettingNode("STATION.AF.DefaultSetting.ActionInterface");

        Eplan.EplApi.Base.SettingNode ownSetting = new

          Eplan.EplApi.Base.SettingNode("STATION.AF.ActionTestInterfaces");

        Eplan.EplApi.Base.SettingNode oNew = ownSetting.GetSubNode("TestNode1");

        oNew.MergeWithNode(oMuster);

        oNew.SetStringSetting("ModuleName", "Test1Value1", 0);

        oNew.SetBoolSetting("IsAddIn", true, 0);

        oNew.SetStringSetting("ActionName", "TestAction1", 0);

oSettingNode.GetListOfAllSettings(strColl1, False)

oSettingNode.GetListOfNodes(strColl2, False)

oSettingNode.GetListOfSettings(strColl3, False)

oNew.MergeWithNode(oMuster)

oNew.SetStringSetting("ModuleName", "Test1Value1", 0)

oNew.SetBoolSetting("IsAddIn", True, 0)

oNew.SetStringSetting("ActionName", "TestAction1", 0)
```

You can also combine settings into a group under a specific name ' it is called a "scheme". It is possible to have multiple groups under different names, but with the same settings structure. One of the groups is an active scheme.

**C#**
```csharp
SchemeSetting oSchemeSetting = new SchemeSetting();

    oSchemeSetting.Init("USER.DXF.SCHEMES");

    int iCount = oSchemeSetting.GetCount();

    String strName = oSchemeSetting.GetName();

    int iExportFormatVersion = oSchemeSetting.GetNumericSetting("EXPORT.FORMAT_VERSION", 0);

oSchemeSetting.Init("USER.DXF.SCHEMES")
```

As mentioned above, each setting has a default value. To return a setting to its default value, you must get the setting's default value and set it to the setting:

**C#**
```csharp
Eplan.EplApi.Base.Settings oSettings = new Eplan.EplApi.Base.Settings();

    // Set the path for projects back to its default

    string sProjectsPath = "";

    sProjectsPath = oSettings.GetStringDefault("USER.TrDMProject.Masterdata.Pathnames.Projects", 0);

    oSettings.SetStringSetting("USER.TrDMProject.Masterdata.Pathnames.Projects", sProjectsPath, 0);

sProjectsPath = oSettings.GetStringDefault("USER.TrDMProject.Masterdata.Pathnames.Projects", 0)

oSettings.SetStringSetting("USER.TrDMProject.Masterdata.Pathnames.Projects", sProjectsPath, 0)
```

To make it easier for the API user to find a particular settings key, the settings dialog provides a hidden feature. If you set the Boolean setting  USER.EnfMVC.ContextMenuSetting.ShowExtended  to "true", you will get an additional context menu item in the settings dialog that shows you the path of the selected setting.

### Remarks

Due to changes in Eplan, settings may change their type or name or some settings may be removed completely. We cannot guarantee the long-term compatibility of the settings. When updating to a newer version, please check your source code to see whether the settings you are using still working.

Indexed settings always have continuous indexes. If a value is removed, the following values move up to fill the gap. This means that if you want to get all the values of an indexed property, all you have to do is loop from index 0 to the number returned by  GetCountOfValues(...)  minus one. If you try to get the value from an index where no value exists, a  BaseException  is thrown.
