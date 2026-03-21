---
title: "Installing EEC servers"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_h_installation_web_eec_eec_server.htm"
file: "admin_h_installation_web_eec_eec_server"
category: "admin"
---

# Installing EEC servers

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Installing and configuring Web EEC

### [Requirement](javascript:void\(0\);)

The Tomcat web server service is stopped.

Variant 1 to stop the Tomcat web server service:

  1. If required, open the hidden symbols in the task bar.
  2. Right-click the symbol of the Tomcat Monitor.
  3. Select Stop service from the popup menu.
  4. The symbol  in the task bar indicates that the Tomcat web server service is stopped.



Variant 2 to stop the Tomcat web server service:

  1. Open the Windows Explorer task manager.
  2. Open the Services tabs.
  3. Navigate to the Tomcat9 service.
  4. Right-click the name and select Stop from the popup menu.
  5. The Status column shows the Tomcat web server service as Finished.



The Web EEC is provided as a Web archive with the file extension .war in the <EEC installation folder>\install\webec folder. This file format represents a JAR and / or ZIP archive, and can be opened and edited using a compression program, for example, 7-ZIP.

  1. Unpack the file webec.war into a new folder called webec.
  2. Open the file \webec\WEB-INF\web.xml in an editor.
  3. Change the following configuration parameters:
Configuration parameter | Description  
---|---  
com.mind8.formui.aliasUrl | Modifies the URL of the download link.  
com.mind8.formui.eox | Name of the model EOX file without file extension. This information must match the information in the file ec.ini of the EEC Server.  
com.mind8.formui.perspective.objectThis functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here: 

## Installing and configuring Web EEC

### [Requirement](javascript:void\(0\);)

The Tomcat web server service is stopped. Variant 1 to stop the Tomcat web server service:
    1. If required, open the hidden symbols in the task bar.
    2. Right-click the symbol of the Tomcat Monitor.
    3. Select Stop service from the popup menu.
    4. The symbol  in the task bar indicates that the Tomcat web server service is stopped.
Variant 2 to stop the Tomcat web server service:
    1. Open the Windows Explorer task manager.
    2. Open the Services tabs.
    3. Navigate to the Tomcat9 service.
    4. Right-click the name and select Stop from the popup menu.
    5. The Status column shows the Tomcat web server service as Finished.
The Web EEC is provided as a Web archive with the file extension .war in the <EEC installation folder>\install\webec folder. This file format represents a JAR and / or ZIP archive, and can be opened and edited using a compression program, for example, 7-ZIP.
    1. Unpack the file webec.war into a new folder called webec.
    2. Open the file \webec\WEB-INF\web.xml in an editor.
    3. Change the following configuration parameters:
| Configuration parameter | Description  
---|---  
com.mind8.formui.aliasUrl | Modifies the URL of the download link.  
com.mind8.formui.eox | Name of the model EOX file without file extension. This information must match the information in the file ec.ini of the EEC Server.  
com.mind8.formui.perspective.object | Path to the project component that contains the Form-UI to be displayed initially.  
com.mind8.formui.perspective.form-id | The ID of the Form-UI to be displayed initially.  
com.mind8.formui.host | Host of the EEC Server.  
com.mind8.formui.port | Port of the EEC Server. This information must match the information in the file ec.ini of the EEC Server.  
com.mind8.formui.timeout | Waiting time until a session-timeout is triggered after inactivity (in seconds).  
  
### Note

Parameter values to be entered by the user are identified by a comment:

<!-- TODO: Comment text -->.

The complete comment, including <!-- and \--> has to be replaced by a parameter value.

Example for a parameter value before the change by the user:

<param-value><!-- TODO: ExampleEOX (without file type .eox) --></param-value>

Example for a parameter value after the changes by the user:

<param-value>TutorialModel</param-value>

### Example of a configuration
        
                <web-app id="WebApp">
        ...
        	<context-param>
        		<param-name>com.mind8.formui.eox</param-name>
        		<param-value>**Tutorial_model** </param-value>	
        	</context-param>
        	<context-param>
        	<param-name>com.mind8.formui.perspective.object</param-name>
        	<param-value>**Feeder.Mechatronic.Feeder** </param-value>
        	</context-param>
        	<context-param>
        		<param-name>com.mind8.formui.perspective.form-id</param-name>
        		<param-value>**feeder** </param-value>
        	</context-param>
        	<context-param>
        		<param-name>com.mind8.formui.host</param-name>
        		<param-value>**localhost** </param-value>
        	</context-param>
        	<context-param>
        		<param-name>com.mind8.formui.port</param-name>
        		<param-value>**7171** </param-value>
        	</context-param>
        ...
        </web-app>

    4. Copy the folder \webec into the folder <Tomcat installation folder>\Tomcat <Tomcat version>\webapps.
    5. Delete the contents of the folder <Tomcat installation folder\Tomcat <Tomcat version>\work.

Start the Tomcat web server service.

Variant 1 to start the Tomcat web server service:

    1. If required, open the hidden symbols in the task bar.
    2. Right-click the symbol of the Tomcat Monitor.
    3. Select Start service from the popup menu.
    4. The symbol in the task bar indicates that the Tomcat web server service is started.

Variant 2 to start the Tomcat web server service:

    1. Open the Windows Explorer task manager.
    2. Open the Services tabs.
    3. Navigate to the Tomcat9 service.
    4. Right-click the name and select Start from the popup menu.
    5. The symbol  in the task bar indicates that the Tomcat web server service is started.

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Installing EEC servers

#### Requirements

     * A folder that contains the basic model exists.
     * A folder in which the generated models are stored exists.

Installation of the EEC Server can be carried out in two variants:

    1. Select the EEC server installations option in the installation wizard.
    2. Select the Stand-alone installation in the installation wizard and then edit the installation file.

### [Variant 1](javascript:void\(0\);)

Installation:

    1. Start the installation file.
    2. Select the language of the installation wizard.
    3. Click [OK].
    4. Acknowledge the following information page with [Next >].
    5. Accept the license agreement.
    6. Click [Next >].
    7. Select the installation variant EEC server installation.
    8. Click [Next >].
    9. Enter the same value for the server port that you have already specified in the web.xml file (see [Installing and configuring Web EEC](admin_h_installation_web_eec_configuration.htm)).
    10. Click [Next >].
    11. Specify a folder for the storage location of the basic models in which the EOX file is located as a back-end.
    12. Click [Next >].
    13. Specify a folder for the storage location of the session models in which the EOX files of each session are stored.
    14. Click [Next >].
    15. Enter the target folder for the installation.
    16. Click [Next >].
    17. Indicate whether an entry is to be created in the start menu and/or desktop symbol.
    18. Click [Next >].
    19. Complete the installation overview with [Install].

### [Variant 2](javascript:void\(0\);)

    1. Start a stand-alone installation.
    2. Deactivate the option Start EEC.
    3. If required, deactivate the option Open 'Feature Releases' list.
    4. Complete the installation with [Finish].
    5. Open the initialization file <EEC installation folder>\ec.ini in an editor (for example Notepad++).
    6. Add the following lines to the end of the file:
    
        -Dcom.mind8.ecserver.port=<Port des EEC-Servers z.B. 7171>
    -Dcom.mind8.ecserver.baseEOXPath=<absoluter Pfad zum Ordner der Basismodelle, z.B. .\eox>
    -Dcom.mind8.remote.server.repository.file=<absoluter Pfad zum Ordner der Sessionmodelle, z.B. .\sessionmodels>

    1. Save the initialization file.

### Note

This port number must match that in the file web.xml.  
The folder for basic models contains models that are available for the Web EEC. This specification is mandatory! The path must be specified using forward slashes /, and not backslashes \\. The specific model is stated in the file web.xml without the file extension .eox. This is also true of the system model.  
The folder of the session models contains the model files that are created for a new session. This specification is mandatory!   
The resources required for the model must be provided, and configured on the side of the EEC Server.
