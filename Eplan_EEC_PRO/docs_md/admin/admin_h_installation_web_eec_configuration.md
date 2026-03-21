---
title: "Installing and configuring Web EEC"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_h_installation_web_eec_configuration.htm"
file: "admin_h_installation_web_eec_configuration"
category: "admin"
---

# Installing and configuring Web EEC

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
