# IdentityStatusCode

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityStatusCode.html

---

Available response status codes.

Syntax

**C#**



public enum IdentityStatusCode : System.Enum

public enum class IdentityStatusCode : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **AuthDataEmpty** | 27 | Authentication data is empty. |
| **AuthenticationInterfaceCouldNotBeInitialized** | 24 | Authentication interface could not be initialized. |
| **ClientError** | 6 | Client error. |
| **ClientIdNotRegistered** | 26 | ClientId not registered. |
| **ConnectionError** | 4 | Connection error. |
| **Failed** | -1 | Call failed, potential problems: time out, wrong credentials, canceled. |
| **IdentityClientNotInitialized** | 11 | IdentityClient not initialized. |
| **IdentityClientProcessCallFailed** | 21 | IdentityClient process call failed. |
| **IdentityClientProcessCreationFailed** | 20 | IdentityClient process creation failed. |
| **InitCefFailed** | 28 | Certificate initialization failed. |
| **InvalidSharedMemoryData** | 22 | Invalid shared memory data. |
| **MemoryMappedFileCreationFailed** | 14 | Memory mapped file creation failed. |
| **MutexCreationFailed** | 15 | Mutex creation failed. |
| **NoAuthentication** | 3 | Authentication not performed. Was not needed, i.e. automation processes. |
| **Offline** | 1 | Offline mode. |
| **ReadDataFromSharedMemoryFailed** | 17 | Read data from shared memory failed. |
| **ServerError** | 7 | Server error. |
| **SignInRequired** | 2 | If a grace period has expired, a sign in is required. |
| **Success** | 0 | Call success. |
| **TimeOut** | 13 | Connection time out. |
| **TokenManagementInterfaceCouldNotBeInitialized** | 25 | Token management interface could not be initialized. |
| **UnexpectedException** | 18 | Unexpected exception. |
| **UnknownError** | 5 | Unknown error. |
| **UnknownException** | 12 | Unknown exception. |
| **UnsupportedCall** | 19 | Unsupported call. |
| **UserProfileError** | 23 | User profile error. |
| **WriteDataIntoSharedMemoryFailed** | 16 | Write data into shared memory failed. |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.IdentityClient.IdentityStatusCode**
