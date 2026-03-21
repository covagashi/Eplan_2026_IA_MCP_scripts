---
title: "Message log settings"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_searching_errors_by_means_of_messagelog_user_preferences.htm"
file: "eecbase_k_searching_errors_by_means_of_messagelog_user_preferences"
category: "eecbase"
---

# Message log settings

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Message log settings

The message log lists all user-relevant activities, and thus assists in the search for errors in the model. Under Settings > Message Log the maximum number of activities to be logged can be limited.

    1. The maximum number of retained activities is entered in the Number of retained activities field. If the maximum number is reached, then the oldest message is deleted from the message log as soon as a new message occurs (FIFO - First In First Out principle).
    2. The logging period , for how many hours messages are to be kept in memory so that for example, only the messages of the last 2 hours are stored, is entered in the Protocol timescale for activities (h) field. The oldest message is deleted from the message log as soon as a new message occurs (FIFO - First In First Out principle). If a null or nothing is entered, then activities are stored without limit.

### Note

The protocol timescale for activities only takes place when new adding new messages, so that messages can be displayed in the log, which are older than the protocol timescale allows in principle.
