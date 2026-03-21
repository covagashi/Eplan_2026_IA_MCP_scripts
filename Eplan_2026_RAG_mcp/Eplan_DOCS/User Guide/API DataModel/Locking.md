# Locking

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Locking.html

---

In computer science, locking is a synchronization mechanism for enforcing limits on access to a resource in a multi-threaded environment (multiple-user environment). Locks are one way of enforcing concurrency control policies.

In Eplan API, the term "**locking an object**" means to set an object reference to a state, where it can be edited by the current user / process, whereas no other user / process can edit it. In general, the user can always get an object in an un-locked / read-only way, even if it is locked by another user. If even this read-only access is not possible, we speak of an "**exclusive lock**". Exclusive locking is necessary, if e.g. the structure of an Eplan project is changed or if a project is copied, renamed or a backup is done.

Please take into account that API locking only wraps P8 locking techniques. For further details about this functionality please refer to Eplan Help > Editing and Managing Project > Multi-user Operation chapter of P8 help.

### What can be locked "automatically"?

- **All project data** ' This can be done by getting the project from the  SelectionSet  (in add-ins) or by opening it via the  ProjectManager. This depends on the  LockProjectByDefault  property, which is set to "true" by default. Also getting the selected project by the  HeServices.SelectionSet.GetCurrentProject  method locks the project (and its data) completely. Please note that read-only access is still possible from other P8 instances.
- **Exclusive project locking** ' This is done by setting the  USER.TrDMProject.OperationMode.OpenProjectsExclusive  setting to "true" before opening the project. As mentioned above, some project-wide operations require such an exclusive lock of a project, where it can be used by only one single P8 instance.
- **Selected elements** ' This is possible by setting the  SelectionSet.LockSelectionByDefault  property  to "true". By default, the option is enabled (set to "true"), so when getting selected items of a project, they can be changed in the API without setting this property.

### SafetyPoint

The  SafetyPoint  class provides automatic locking of data model objects. The mechanism is enabled from the time a  SafetyPoint  object is created until it is distroyed, so it is recommended to use it with the  using  keyword:

```csharp
var project = new ProjectManager {LockProjectByDefault = false}.OpenProject(@"$(MD_PROJECTS)\EPLAN-DEMO.elk");
 // View placement '8' (on page =EB3+ETM/4)
 ViewPlacement viewPlacement8 = project
 .Pages[42]
 .AllFirstLevelPlacements
 .OfType<ViewPlacement>()
 .FirstOrDefault(item => item.Properties.DMG_VIEWPLACEMENT_DESIGNATION.ToString() == "8");
 using (SafetyPoint safetyPoint = SafetyPoint.Create())
 {               
     Console.WriteLine(viewPlacement8.IsLocked);     // False
     viewPlacement8.Scale = 44.44;                   // Set another scale
     Console.WriteLine(viewPlacement8.IsLocked);     // True                  
     safetyPoint.Commit();                           // Necessary, otherwise changes are rolled back
 }
 Console.WriteLine(viewPlacement8.IsLocked);         // Again false
```

"Automatic" means that they are locked internally before any change is made and unlocked after  SafetyPoint  is disposed of. This way is recommended when you need to lock as little as possible and it is not clear which objects need to be locked to perform a change. After the SafetyPoint block, please call the  Commit  method, otherwise the changes will be rolled back.

### What is a LockingStep?

A  LockingStep  is an object used to automatically unlock API resources (such as projects, functions, etc). There are 2 ways to create this object:

- **Explicitly** ' Must be done in modeless dialog boxes and in offline API applications:

```csharp
using(LockingStep oLockingStep = new LockingStep())
 {
    ....
 }
```

When there is necessary access to some resources and the LockingStep is not created, an exception will be thrown (NoLockingStepException).

- **P8 framework a****ctions** **and scripts**

Anyway, there is no "Unlock" method in any data model class. The  LockingStep  class remembers all locks set during its lifespan and releases them when the LockingStep is being disposed. This guarantees that objects are released, even if an exception was thrown within the block.

In rare cases, however, it may be necessary to switch off  LockingStep  creation (manual or automatical). This can be done using the  PauseManualLock()  and  ResumeManualLock()  methods of the  LockingVector  class. Please use them only in exceptional cases, i.e. when it is necessary to "manually" decide what to lock instead of relying on the P8 framework (see below).

### Manual locking mode

In addition to the automatic locking mechanism, it is also possible to call locking methods directly on the required objects. This low-level type of locking can be used concurrently with "automatic" locking or as the only locking.

- **Locking single StorableObject** ' This is done by calling  LockObject  on the required object. Please note that only properties directly connected with objects can be locked this way (such as internal / normal properties, sub-functions or sub-placements are excluded).

- **Locking all placements of a page in exclusive mode** ' This can be done by calling  Page::LockAllObjects. Please consider that it is different than calling  Page::LockObject, which locks only properties of a page.

- **Locking all objects of a project** ' This can be done with  Project::LockAllObjects.

- **Locking all objects of a device** ' This is done with  Function::LockDevice. Calling this method also locks all functions placed on the same page as functions of a device.

### Guideline to Locking of data model objects

If you don't need to mind multiple-user issues, e.g. when creating a new project with your own schematics generator, you should always lock the entire project. The project is locked by default when it is opened or created using the respective methods (OpenProject(...)  /  CreateProject(...)) of the  ProjectManager  class in  DataModel. Also, getting the selected project through the method  GetCurrentProject(...)  in the  HeServices.SelectionSet  class, will lock the project completely.

If you need to consider other users or processes working on the same project, you should lock **as little of the project data as possible**. To do this, you should first get, open, or create the project in an unlocked way. This can be done by setting the  LockProjectByDefault  property of a  ProjectManager  or the  SelectionSet  object to "false". With this unlocked project object, you simply lock the object (e.g. page) you want to change. Also mind that the locks are only released when disposing the respective LockingSteps, so set as few locks as possible in one locking step.

### Differences between add-ins and offline API

The main difference between locking in add-ins and offline API applications is that the  Execute(...)  method of the  IEplAction  interface, is already surrounded by a locking step, while the API programmer needs to implement the locking step(s) in an offline application by himself.

### API [Verifications](Verifications.html)

Verification methods called by the Eplan framework are not surrounded by a locking step. If this is necessary, the user needs to implement it himself. Please have in mind that the creation of a locking step inside a verification method has a great influence on the performance of the entire check. Therefore, this should be done as little as possible.

### Locking in service methods (HeServices/[Actions](Actions.html))

All service functionality to which you pass a project resource as a string parameter will always automatically lock / unlock that resource. If locking is not possible due to multi-user issues, an exception will be thrown. This applies to all command line actions that take only string parameters. The  HeServices  classes have most of the time method overloads with both string-based and object passed parameters. If you pass an object to the method, you need to take care for the locking.

### Determining which users currently have the project open

To find out which users are currently working on the project, the  Project  class provides a  CurrentUsers  property that returns an array of  UserInfo  structures of the users who are accessing the project.