
### File based Key-Value datastore

   Supports basic CRD (Create, Read, Delete)

**Functionalities:**
  1. It can be initialized using an optional file path. If one is not provided, it will reliably create itself using current date and time for nameing file.
  2. Key string capped at 32 characters.
  3. Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.
  4. Only one process can access the datastore (local file) at a time.
  5. Thread safe.


**Usage : **

###### Creating an instance
```
import keyvalue
key_value = keyvalue.keyvalue()
```

Note: If `File Path` is provided in the `keyvalue()` call, it will obtain lock on that file using `fcntl`. If object is created for the same file path twice, `BlockingIOError` is thrown.

###### Creating an data
```

key_value.Create('ujwal', 'singh')  #Here TimeToLive is By Default set to None 

key_value.Create(1, 2, 5) #Here int obect is set to string '1' and TimeToLive is set to 5 seconds
```

###### Reading data
```
key_value.Read('ujwal') #It will Return {'ujwal':'singh'}
```

###### Deleting data
```
key_value.Delete('ujwal') #It will remove ujwal from file only if it is in TimeToLive limit (if applicable)
```
