# Transactions

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Transactions.html

---

The term "**transaction**" refers to a set of operations that form a working unit in the Eplan project database. They can be executed only all together or not a single one. This grouping ensures data integrity and consistency even in the case of a system failure. For example:

```csharp
using (Transaction oTransaction = new TransactionManager().CreateTransaction())
 {
      oFunction1.Name = "=+-NewTestFunctionName_1";
      oFunction2.Name = "=+-NewTestFunctionName_2";
      oTransaction.Commit();
 }
```

So if the execution of the code is aborted before the  Commit()  was called, the "Name"properties remain unchanged.

### Nesting API transactions

It is also possible to nest transactions in API. For example:

```csharp
oFunction.Name = "oFunction0";
 using (Transaction oTransaction1 = new TransactionManager().CreateTransaction())
 {
      using(Transaction oTransaction2 = new TransactionManager().CreateTransaction())
      {
           oFunction.Name = "Function2";
           oTransaction2.Commit();
      }
      Console.Writeline(oFunction.Name) // Will be "oFunction2" returned,
      oFunction.Name = "Function1";
      Console.Writeline(oFunction.Name) // Will be "oFunction1" returned,
 }
 Console.Writeline(oFunction.Name) // Will be "oFunction0" returned, because outer transaction oTransaction1 wasn't committed
```

In this case, an inner transaction is treated as one of the operations of the outer transaction.

### Internal Eplan and API transactions

We distinguish two types of transaction:

**1. API transactions** ' They are opened explicitly or implicitly from API. Explicit opening is done by creating a  Transaction  object from the  TransactionManager:

```csharp
Transaction oTransaction = new TransactionManager().CreateTransaction();

```

 Implicit opening is done by creating the same  Transaction  object by some Eplan operations, (like creating new objects, changing a property) in a way that is invisible for API user

**2. Eplan internal transactions** ' They are started inside of the Eplan framework, so they are opened and closed implicitly.

### Using API transactions and internal transactions at the same

Using API transactions and internal transactions at the same time can cause problems. So please consider the following rules to avoid them:

- API transaction within an internal transaction

An API transaction may always be opened within an internal transaction. The API developer has a possibility to check whether an API transaction is opened using the following property:

```csharp
TransactionManager::IsTransactionRunning
```

A commit of an API transaction does not result in a change to the database and is not saved in the database until the termination of the internal transaction. Aborting an API transaction does not abort an internal transaction, but throws an exception because an internal transaction is running and cannot be aborted.

- An internal transaction within an API transaction

An internal transaction may always be opened within an API transaction. The API developer has the possibility to check whether an internal transaction is opened using the following property:

```csharp
TransactionManager::IsEplanTransactionRunning

```

If an internal transaction is to be opened, the API transaction becomes committed. If an internal transaction is again closed (Abort  or  Commit), then the API transaction will be started again. The API transaction class also has a property that indicates whether an internal transaction was opened and closed within the API transaction:

```csharp
Transaction::IsImplicitEplanTransactionCommited
```