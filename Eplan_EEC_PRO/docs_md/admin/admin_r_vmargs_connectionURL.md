---
title: "org.foederal.sn.connectionURL"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_connectionURL.htm"
file: "admin_r_vmargs_connectionURL"
category: "admin"
---

# org.foederal.sn.connectionURL

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## org.foederal.sn.connectionURL

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dorg.foederal.sn.connectionURL=<Connection URL> |  Optional  
**Annotation**  
The connection URL indicates the connection path to the data back end. This can be an absolute or relative path to an EOX file or a statement for an EOX file selection. As an exception an empty model that only includes the system library can also be specified. By default the connection path to the <EEC installation folder>\eox\model.eox file is specified. EEC start with an empty model (only with system libraries:)
    
        -Dorg.foederal.sn.connectionURL=proxy://empty

Initial EOX file and in addition the selection of an EOX file at an EEC Start (default setting). At the next start the initial EOX file is used again: The connection path is specified according to the following syntax:
    
        -Dorg.foederal.sn.connectionURL=proxy://initial=eox:///.eox/model.eox?mode=rw

Selection of an EOX file at an EEC Start (default setting). At the next start the previously selected EOX file is used again: The connection path is specified according to the following syntax:
    
        -Dorg.foederal.sn.connectionURL=proxy://any

On start a file selection dialog for an EOX file appears. The dialog offers an option to select, whether access to the EOX file should be read-only. Any changes have to be exported as reusable library or as EOX file, if they should not be lost. If the option is deselected, the previous model will be changed. Any changes are stored in the selected EOX file. **EOX files:** The connection path to an EOX file for data back end is specified with the following syntax:
    
        -Dorg.foederal.sn.connectionURL=eox:///<absolute or relative path to EOX file>?mode=rw

| Statement | Meaning  
---|---  
<Drive letter:> | Any drive letter, e.g. D:  
<?> | Initiates further options  
<mode=rw> |  Defines the access rights. Possible values are:
     * r = read-only
     * rw = lead und write
Default value: r = read-only  
<&> | Initiates more options  
<validate=true> |  Defines whether the model should be validated while opening. This option is outdated and can be removed in future versions. Possible values are:
     * true = validate model
     * false = no model validation
Default value: true = validate model  
  
Examples:
    
        -Dorg.foederal.sn.connectionURL=eox:///C:/Users/Public/EPLAN/EngineeringConfiguration/<EEC installation folder>/eox/model.eox?mode=rw
    -Dorg.foederal.sn.connectionURL=eox:///./eox/model.eox?mode=rw
      
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.
