---
title: "E-mail settings"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_prefs_js_email.htm"
file: "admin_r_prefs_js_email"
category: "admin"
---

# E-mail settings

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## E-mail settings

After finishing a job certain e-mail recipients can be informed about the result. Different recipients, subjects and contents can be provided for successful and failed jobs. In addition the mail server preferences can be set.

Path to the settings:

Menu Window > Preferences

Dialog Preferences > Job Server > Job Server Worker > Email preferences

     * To enable messages in the event of success or an error, the check boxes Send mail on success and / or Send mail on failure must be selected.
     * The recipient of the message is specified along with the sender (Worker) and a subject line in Mail Settings.
     * To allow the e-mail to be sent, the following preferences have to be carried out in the area of the SMTP connection:
       * In the Connection security field, select one of the protocols None, STARTTLS or SSL/TLS.
       * In the Server field, specify the SMTP mail server that is used in your company to send the e-mail. The default is http://localhost.
       * Enter the appropriate port number for the selected protocol in the Port field. The default value for unencrypted mailing is 25, for encrypted mailing via STARTTLS is 587, via SSL/TLS is 465.
     * If the SMTP mail server requires authentication, the Use SMTP authentication check box must be selected and the User and Password must be entered in the fields with those names.

### Note

The specified port numbers are default values and can differ from the specifications for your mail server. Contact the responsible administrator of your company to obtain the combination in question.
