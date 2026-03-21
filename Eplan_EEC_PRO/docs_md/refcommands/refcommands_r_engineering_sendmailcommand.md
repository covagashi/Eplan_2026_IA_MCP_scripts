---
title: "Engineering.SendMailCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_sendmailcommand.htm"
file: "refcommands_r_engineering_sendmailcommand"
category: "refcommands"
---

# Engineering.SendMailCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.SendMailCommand Sends an e-mail with the specified content from the specified sender to the specified addresses with the specified attachments. The user name and password can be specified for the authentication. Since the password is specified in plain text, an implicit authentication (via computer name or Windows authentication) is therefore recommended. The content is to be transferred in HTML format. If a file does not exist under the specified path, an error is reported and the e-mail is not sent. Argument | Type | Description  
---|---|---  
fromAddress | String | E-mail address of the sender. May not be empty. No validity check takes place.  
toAddress | String | E-mail address of the recipient. No validity check takes place. At least one of the arguments fromAddress, toAddress, ccAddress or bccAddress must be specified.  
ccAddress | String | E-mail address of the recipient in copy. No validity check takes place.  
bccAddress | String | E-mail address of the recipient of a blind copy. No validity check takes place.  
subject | String | Content of the subject  
htmlContent | String | Content of the e-mail. The content must be transferred in HTML format.  
username | String | User name for the login at the SMTP-mail server. If the username and password are not transferred, no authentication takes place.  
password | String | Password for the login at the SMTP-mail server. If the username and password are not transferred, no explicit authentication takes place.  
attachments | List | List of absolute paths of the files to be attached. Directory paths are not allowed.  
The following settings have to be made in the initialization file (for example ec.ini) or in the settings for successful application of the command:
     * Dde.eplan.eec.mail.host: Defines the host.
     * Dde.eplan.eec.mail.port: Defines the port.
     * Dde.eplan.eec.mail.username: Defines the user name for the authentication (optional).
If these settings have been made in the settings, they also apply for the e-mail dispatch of the Job Server.
