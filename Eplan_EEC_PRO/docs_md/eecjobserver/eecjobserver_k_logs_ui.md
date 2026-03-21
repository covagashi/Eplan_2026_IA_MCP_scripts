---
title: "User interface of the Logs"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecjobserver_k_logs_ui.htm"
file: "eecjobserver_k_logs_ui"
category: "eecjobserver"
---

# User interface of the Logs

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

User interface of the Logs

## User interface of the Logs

The user interface for the Logs shows the logged events of the Job Server.

The log shows the messages in chronological order with the most recent one being at the top. In addition the messages are divided into groups Today), This week) and Older than a week.

The messages are colored in accordance with their severity. Information is in black, the Job Server starts and stops in green, errors in red, warning orange and details in light gray.

The message can be displayed and hidden according to their severity by marking the filter of the same name.

If the time filter Today's jobs is used, only those messages are listed that occurred on the current day. This list is updated at regular intervals. The time filter All logs displays all the messages again.

The number of days after which log entries are removed is displayed below the list. Log entries that are older than the displayed number of days are removed. The number of days can be set through an entry in the initialization file (ec.ini) (see [de.eplan.eec.jobserver.cleanup.days](admin_r_vmargs_jobserver_cleanupdays.htm)).

The browser search function can be used to search through all messages.
