# XPartsSetDataSourceAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XPartsSetDataSourceAction.html

---

```
 Changes the setting responsible for parts management database type.

```

| Parameter | Description |
| --- | --- |
| ``` DataSourceType
 ``` | ```  0 = EPLAN Database (default value), 1 = SQL server, 3 = eSTOCK collection 
 ``` |
| ``` DataBaseFileName
 ``` | ```  Full database path name 
 ``` |
| ``` SqlServer
 ``` | ```  SQL server name 
 ``` |
| ``` SqlCatalog
 ``` | ```  SQL database name 
 ``` |
| ``` SqlUserName
 ``` | ```  SQL user name 
 ``` |
| ``` SqlPassword
 ``` | ```  SQL user password 
 ``` |
| ``` SqlLogin
 ``` | ```  0 = Windows registration (default value), 1 = SQL server registration (username + password) 
 ``` |
| ``` SqlFullName
 ``` | ```  If set, then SqlServer, SqlCatalog, SqlUserName and SqlPassword parameters are not used. 
 ``` |
| ``` CollectionName
 ``` | ```  Name of the eSTOCK collection 
 ``` |
| ``` CollectionId
 ``` | ```  ID of the eSTOCK collection 
 ``` |
| ``` Force
 ``` | ```  force downloading of all data of a eSTOCK collection 
 ``` |

**Remarks**

```
 When DataSourceType = 1, SqlServer, SqlCatalog, SqlUserName, SqlPassword, SqlLogin and SqlFullName parameters can be used. SqlFullName would be used only when SqlLogin = 1.

 When DataSourceType = 0, DataBaseFileName can be used.

 When DataSourceType = 3, CollectionName and CollectionId can be used.

```

**Example**

```
 Example 1

 XPartsSetDataSourceAction /DataSourceType:0 /DataBaseFileName:C:\Users\Public\EPLAN\Data\Article\COMPANY_NAME\Database.alk

 Example 2

 XPartsSetDataSourceAction /DataSourceType:1 /SqlLogin:0 /SqlServer:SQL_SERVER_NAME /SqlCatalog:SQL_DATABASE

 Example 3

 XPartsSetDataSourceAction /DataSourceType:1 /SqlLogin:1 /SqlServer:SQL_SERVER_NAME /SqlCatalog:SQL_DATABASE /SqlUserName:SQL_USERNAME /SqlPassword:SQL_PASSWORD

 Example 4

 XPartsSetDataSourceAction /DataSourceType:1 /SqlLogin:1 /SqlFullName:SQL_SERVER_NAME|SQL_DATABASE|2|SQL_USERNAME|SQL_PASSWORD

 Example 5

 XPartsSetDataSourceAction /DataSourceType:3 /CollectionName:ESTOCK_COLLECTION_NAME /CollectionId:ESTOCK_COLLECTION_ID

```