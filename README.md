<p align="center">
  <img src="https://github.com/medouzer/AirBnB_clone/blob/master/hbnb_logo.png" >
</p>

<h1 align="center">HBnB</h1>
<p align="center">An AirBnB clone.</p>

---

## Description :house:

BnB is a complete web application, integrating database storage,
a back-end API, and front-end interfacing in a clone of AirBnB.

The project currently only implements the back-end console.

## Classes :cl:

HBnB utilizes the following classes:

|                                | BaseModel                            | FileStorage                          | User                                                 | State                     | City                      | Amenity                   | Place                                                                                                                                                                      | Review                            |
| ------------------------------ | ------------------------------------ | ------------------------------------ | ---------------------------------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| **PUBLIC INSTANCE ATTRIBUTES** | `id`<br>`created_at`<br>`updated_at` |                                      | Inherits from `BaseModel`                            | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel`                                                                                                                                                  | Inherits from `BaseModel`         |
| **PUBLIC INSTANCE METHODS**    | `save`<br>`to_dict`                  | `all`<br>`new`<br>`save`<br>`reload` | ""                                                   | ""                        | ""                        | ""                        | ""                                                                                                                                                                         | ""                                |
| **PUBLIC CLASS ATTRIBUTES**    |                                      |                                      | `email`<br>`password`<br>`first_name`<br>`last_name` | `name`                    | `state_id`<br>`name`      | `name`                    | `city_id`<br>`user_id`<br>`name`<br>`description`<br>`number_rooms`<br>`number_bathrooms`<br>`max_guest`<br>`price_by_night`<br>`latitude`<br>`longitude`<br>`amenity_ids` | `place_id`<br>`user_id`<br>`text` |
| **PRIVATE CLASS ATTRIBUTES**   |                                      | `file_path`<br>`objects`             |                                                      |                           |                           |                           |                                                                                                                                                                            |                                   |

## Storage :baggage_claim:

The above classes are handled by the abstracted storage engine defined in the
[FileStorage](./models/engine/file_storage.py) class.

Every time the backend is initialized, HBnB instantiates an instance of
`FileStorage` called `storage`. The `storage` object is loaded/re-loaded from
any class instances stored in the JSON file `file.json`. As class instances are
created, updated, or deleted, the `storage` object is used to register
corresponding changes in the `file.json`.

## Console :computer:

The console is a command line interpreter that permits management of the backend
of HBnB. It can be used to handle and manipulate all classes utilized by
the application (achieved by calls on the `storage` object defined above).

### Using the Console

The HBnB console can be run both interactively and non-interactively.
To run the console in non-interactive mode, pipe any command(s) into an execution
of the file `console.py` at the command line.

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
```

Alternatively, to use the HBnB console in interactive mode, run the
file `console.py` by itself:

```
$ ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb)
```

To quit the console, enter the command `quit`, or input an EOF signal
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

### Console Commands

The HBnB console supports the following commands:

- **create**
  - Usage: `create <class>`

Creates a new instance of a given class. The class' ID is printed and
the instance is saved to the file `file.json`.

```
root@KALI:~/AirBnB_clone# ./console.py
(hbnb)create BaseModel
b32fd90d-48ba-42fb-9b4c-14a75a54418c
(hbnb)quit
root@KALI:~/AirBnB_clone# cat file.json ; echo ""
{"BaseModel.836496ff-3945-469e-a581-d4314e97bb7a": {"id": "836496ff-3945-469e-a581-d4314e97bb7a", "created_at": "2023-12-08T19:04:40.103980", "updated_at": "2023-12-08T19:04:40.131653", "name": "Holberton", "my_number": 89, "__class__": "BaseModel"}, "BaseModel.0929c12a-bbc0-4fb8-bd0c-6d2dcdb7e3a9": {"id": "0929c12a-bbc0-4fb8-bd0c-6d2dcdb7e3a9", "created_at": "2023-12-08T19:10:33.371556", "updated_at": "2023-12-08T19:10:33.371927", "name": "My First Model", "my_number": 89, "__class__": "BaseModel"}, "BaseModel.cc6b4b37-2e4a-4e73-9c72-709f0b7fdbb7": {"id": "cc6b4b37-2e4a-4e73-9c72-709f0b7fdbb7", "created_at": "2023-12-08T19:18:34.569135", "updated_at": "2023-12-08T19:18:34.569155", "name": "My_First_Model", "my_number": 89, "__class__": "BaseModel"}, "BaseModel.2aca4fca-688b-4dbc-85fa-7a224285a3af": {"id": "2aca4fca-688b-4dbc-85fa-7a224285a3af", "created_at": "2023-12-08T19:21:09.811775", "updated_at": "2023-12-08T19:21:09.811795", "name": "My_First_Model", "my_number": 89, "__class__": "BaseModel"}, "BaseModel.c9e51fae-4779-4739-8e86-356ca6b28ee0": {"id": "c9e51fae-4779-4739-8e86-356ca6b28ee0", "created_at": "2023-12-08T19:23:16.822689", "updated_at": "2023-12-08T19:23:16.822699", "__class__": "BaseModel"}, "BaseModel.d79fb64e-9b07-45cb-a2f3-6d23fbed010c": {"id": "d79fb64e-9b07-45cb-a2f3-6d23fbed010c", "created_at": "2023-12-08T19:31:56.264959", "updated_at": "2023-12-08T19:31:56.264970", "__class__": "BaseModel"}, "User.046949e5-7920-4708-88d0-c53f0cf2f4a4": {"id": "046949e5-7920-4708-88d0-c53f0cf2f4a4", "created_at": "2023-12-08T19:34:21.079451", "updated_at": "2023-12-08T19:34:21.079481", "first_name": "Betty", "last_name": "Bar", "email": "airbnb@mail.com", "password": "root", "__class__": "User"}, "User.cd2729e9-ebd5-4af3-ad59-abf28391bcb5": {"id": "cd2729e9-ebd5-4af3-ad59-abf28391bcb5", "created_at": "2023-12-08T19:34:21.084024", "updated_at": "2023-12-08T19:34:21.084050", "first_name": "John", "email": "airbnb2@mail.com", "password": "root", "__class__": "User"}, "User.2b115574-c056-43f4-bcde-bcceaf57342c": {"id": "2b115574-c056-43f4-bcde-bcceaf57342c", "created_at": "2023-12-08T19:34:58.727363", "updated_at": "2023-12-08T19:34:58.727383", "first_name": "John", "email": "airbnb2@mail.com", "password": "root", "__class__": "User"}, "BaseModel.b32fd90d-48ba-42fb-9b4c-14a75a54418c": {"id": "b32fd90d-48ba-42fb-9b4c-14a75a54418c", "created_at": "2023-12-10T18:33:13.991813", "updated_at": "2023-12-10T18:33:13.991821", "__class__": "BaseModel"}}
```

- **show**
  - Usage: `show <class> <id>` or `<class>.show(<id>)`

Prints the string representation of a class instance based on a given id.

```
 root@KALI:~/AirBnB_clone# ./console.py
(hbnb) create User
348b50a1-92af-47cb-bc7e-31d275c00a8c
(hbnb) show User 348b50a1-92af-47cb-bc7e-31d275c00a8c
[User] (348b50a1-92af-47cb-bc7e-31d275c00a8c) {'id': '348b50a1-92af-47cb-bc7e-31d275c00a8c', 'created_at': datetime.datetime(2023, 12, 10, 18, 35, 39, 277587), 'updated_at': datetime.datetime(2023, 12, 10, 18, 35, 39, 277596)}
(hbnb) show User 348b50a1-92af-47cb-bc7e-31d275c00a8c
[User] (348b50a1-92af-47cb-bc7e-31d275c00a8c) {'id': '348b50a1-92af-47cb-bc7e-31d275c00a8c', 'created_at': datetime.datetime(2023, 12, 10, 18, 35, 39, 277587), 'updated_at': datetime.datetime(2023, 12, 10, 18, 35, 39, 277596)}
(hbnb)
```

- **destroy**
  - Usage: `destroy <class> <id>` or `<class>.destroy(<id>)`

Deletes a class instance based on a given id. The storage file `file.json`
is updated accordingly.

```
root@KALI:~/AirBnB_clone# ./console.py
(hbnb)create State
ca0f7b21-43f1-42a5-ba00-a3f683e51109
(hbnb)create Place
ffb01403-d3b6-4994-9aad-049ac6b58f51
(hbnb)destroy State ca0f7b21-43f1-42a5-ba00-a3f683e51109
(hbnb)Place.destroy (ffb01403-d3b6-4994-9aad-049ac6b58f51)
(hbnb)quit
```

- **all**
  - Usage: `all` or `all <class>` or `<class>.all()`

Prints the string representations of all instances of a given class. If no
class name is provided, the command prints all instances of every class.

```
 root@KALI:~/AirBnB_clone# ./console.py
(hbnb)create BaseModel
24c34c81-49b3-4600-90e1-4bea8f819a75
(hbnb) create BaseModel
ebc082e8-c330-4a05-b8a9-7d043aff8ec7
(hbnb)create User
da07341b-989e-4e23-995f-0ff447d44a81
(hbnb)create User
e0fd42d2-a713-4ac5-8ae0-f1e8497bda07
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (836496ff-3945-469e-a581-d4314e97bb7a) {'id': '836496ff-3945-469e-a581-d4314e97bb7a', 'created_at': datetime.datetime(2023, 12, 8, 19, 4, 40, 103980), 'updated_at': datetime.datetime(2023, 12, 8, 19, 4, 40, 131653), 'name': 'Holberton', 'my_number': 89}", "[BaseModel] (0929c12a-bbc0-4fb8-bd0c-6d2dcdb7e3a9) {'id': '0929c12a-bbc0-4fb8-bd0c-6d2dcdb7e3a9', 'created_at': datetime.datetime(2023, 12, 8, 19, 10, 33, 371556), 'updated_at': datetime.datetime(2023, 12, 8, 19, 10, 33, 371927), 'name': 'My First Model', 'my_number': 89}", "[BaseModel] (cc6b4b37-2e4a-4e73-9c72-709f0b7fdbb7) {'id': 'cc6b4b37-2e4a-4e73-9c72-709f0b7fdbb7', 'created_at': datetime.datetime(2023, 12, 8, 19, 18, 34, 569135), 'updated_at': datetime.datetime(2023, 12, 8, 19, 18, 34, 569155), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (2aca4fca-688b-4dbc-85fa-7a224285a3af) {'id': '2aca4fca-688b-4dbc-85fa-7a224285a3af', 'created_at': datetime.datetime(2023, 12, 8, 19, 21, 9, 811775), 'updated_at': datetime.datetime(2023, 12, 8, 19, 21, 9, 811795), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (c9e51fae-4779-4739-8e86-356ca6b28ee0) {'id': 'c9e51fae-4779-4739-8e86-356ca6b28ee0', 'created_at': datetime.datetime(2023, 12, 8, 19, 23, 16, 822689), 'updated_at': datetime.datetime(2023, 12, 8, 19, 23, 16, 822699)}", "[BaseModel] (d79fb64e-9b07-45cb-a2f3-6d23fbed010c) {'id': 'd79fb64e-9b07-45cb-a2f3-6d23fbed010c', 'created_at': datetime.datetime(2023, 12, 8, 19, 31, 56, 264959), 'updated_at': datetime.datetime(2023, 12, 8, 19, 31, 56, 264970)}", "[BaseModel] (b32fd90d-48ba-42fb-9b4c-14a75a54418c) {'id': 'b32fd90d-48ba-42fb-9b4c-14a75a54418c', 'created_at': datetime.datetime(2023, 12, 10, 18, 33, 13, 991813), 'updated_at': datetime.datetime(2023, 12, 10, 18, 33, 13, 991821)}", "[BaseModel] (24c34c81-49b3-4600-90e1-4bea8f819a75) {'id': '24c34c81-49b3-4600-90e1-4bea8f819a75', 'created_at': datetime.datetime(2023, 12, 10, 18, 42, 30, 525408), 'updated_at': datetime.datetime(2023, 12, 10, 18, 42, 30, 525414)}", "[BaseModel] (ebc082e8-c330-4a05-b8a9-7d043aff8ec7) {'id': 'ebc082e8-c330-4a05-b8a9-7d043aff8ec7', 'created_at': datetime.datetime(2023, 12, 10, 18, 42, 36, 603049), 'updated_at': datetime.datetime(2023, 12, 10, 18, 42, 36, 603059)}"]
(hbnb)User.all()
["[User] (046949e5-7920-4708-88d0-c53f0cf2f4a4) {'id': '046949e5-7920-4708-88d0-c53f0cf2f4a4', 'created_at': datetime.datetime(2023, 12, 8, 19, 34, 21, 79451), 'updated_at': datetime.datetime(2023, 12, 8, 19, 34, 21, 79481), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (cd2729e9-ebd5-4af3-ad59-abf28391bcb5) {'id': 'cd2729e9-ebd5-4af3-ad59-abf28391bcb5', 'created_at': datetime.datetime(2023, 12, 8, 19, 34, 21, 84024), 'updated_at': datetime.datetime(2023, 12, 8, 19, 34, 21, 84050), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}", "[User] (2b115574-c056-43f4-bcde-bcceaf57342c) {'id': '2b115574-c056-43f4-bcde-bcceaf57342c', 'created_at': datetime.datetime(2023, 12, 8, 19, 34, 58, 727363), 'updated_at': datetime.datetime(2023, 12, 8, 19, 34, 58, 727383), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}", "[User] (348b50a1-92af-47cb-bc7e-31d275c00a8c) {'id': '348b50a1-92af-47cb-bc7e-31d275c00a8c', 'created_at': datetime.datetime(2023, 12, 10, 18, 35, 39, 277587), 'updated_at': datetime.datetime(2023, 12, 10, 18, 35, 39, 277596)}", "[User] (da07341b-989e-4e23-995f-0ff447d44a81) {'id': 'da07341b-989e-4e23-995f-0ff447d44a81', 'created_at': datetime.datetime(2023, 12, 10, 18, 42, 43, 265317), 'updated_at': datetime.datetime(2023, 12, 10, 18, 42, 43, 265328)}", "[User] (e0fd42d2-a713-4ac5-8ae0-f1e8497bda07) {'id': 'e0fd42d2-a713-4ac5-8ae0-f1e8497bda07', 'created_at': datetime.datetime(2023, 12, 10, 18, 42, 50, 220327), 'updated_at': datetime.datetime(2023, 12, 10, 18, 42, 50, 220333)}"]
(hbnb)all
["[BaseModel] (836496ff-3945-469e-a581-d4314e97bb7a) {'id': '836496ff-3945-469e-a581-d4314e97bb7a', 'created_at': datetime.datetime(2023, 12, 8, 19, 4, 40, 103980), 'updated_at': datetime.datetime(2023, 12, 8, 19, 4, 40, 131653), 'name': 'Holberton', 'my_number': 89}", "[BaseModel] (0929c12a-bbc0-4fb8-bd0c-6d2dcdb7e3a9) {'id': '0929c12a-bbc0-4fb8-bd0c-6d2dcdb7e3a9', 'created_at': datetime.datetime(2023, 12, 8, 19, 10, 33, 371556), 'updated_at': datetime.datetime(2023, 12, 8, 19, 10, 33, 371927), 'name': 'My First Model', 'my_number': 89}", "[BaseModel] (cc6b4b37-2e4a-4e73-9c72-709f0b7fdbb7) {'id': 'cc6b4b37-2e4a-4e73-9c72-709f0b7fdbb7', 'created_at': datetime.datetime(2023, 12, 8, 19, 18, 34, 569135), 'updated_at': datetime.datetime(2023, 12, 8, 19, 18, 34, 569155), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (2aca4fca-688b-4dbc-85fa-7a224285a3af) {'id': '2aca4fca-688b-4dbc-85fa-7a224285a3af', 'created_at': datetime.datetime(2023, 12, 8, 19, 21, 9, 811775), 'updated_at': datetime.datetime(2023, 12, 8, 19, 21, 9, 811795), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (c9e51fae-4779-4739-8e86-356ca6b28ee0) {'id': 'c9e51fae-4779-4739-8e86-356ca6b28ee0', 'created_at': datetime.datetime(2023, 12, 8, 19, 23, 16, 822689), 'updated_at': datetime.datetime(2023, 12, 8, 19, 23, 16, 822699)}", "[BaseModel] (d79fb64e-9b07-45cb-a2f3-6d23fbed010c) {'id': 'd79fb64e-9b07-45cb-a2f3-6d23fbed010c', 'created_at': datetime.datetime(2023, 12, 8, 19, 31, 56, 264959), 'updated_at': datetime.datetime(2023, 12, 8, 19, 31, 56, 264970)}", "[User] (046949e5-7920-4708-88d0-c53f0cf2f4a4) {'id': '046949e5-7920-4708-88d0-c53f0cf2f4a4', 'created_at': datetime.datetime(2023, 12, 8, 19, 34, 21, 79451), 'updated_at': datetime.datetime(2023, 12, 8, 19, 34, 21, 79481), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (cd2729e9-ebd5-4af3-ad59-abf28391bcb5) {'id': 'cd2729e9-ebd5-4af3-ad59-abf28391bcb5', 'created_at': datetime.datetime(2023, 12, 8, 19, 34, 21, 84024), 'updated_at': datetime.datetime(2023, 12, 8, 19, 34, 21, 84050), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}", "[User] (2b115574-c056-43f4-bcde-bcceaf57342c) {'id': '2b115574-c056-43f4-bcde-bcceaf57342c', 'created_at': datetime.datetime(2023, 12, 8, 19, 34, 58, 727363), 'updated_at': datetime.datetime(2023, 12, 8, 19, 34, 58, 727383), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}", "[BaseModel] (b32fd90d-48ba-42fb-9b4c-14a75a54418c) {'id': 'b32fd90d-48ba-42fb-9b4c-14a75a54418c', 'created_at': datetime.datetime(2023, 12, 10, 18, 33, 13, 991813), 'updated_at': datetime.datetime(2023, 12, 10, 18, 33, 13, 991821)}", "[User] (348b50a1-92af-47cb-bc7e-31d275c00a8c) {'id': '348b50a1-92af-47cb-bc7e-31d275c00a8c', 'created_at': datetime.datetime(2023, 12, 10, 18, 35, 39, 277587), 'updated_at': datetime.datetime(2023, 12, 10, 18, 35, 39, 277596)}", "[Place] (ffb01403-d3b6-4994-9aad-049ac6b58f51) {'id': 'ffb01403-d3b6-4994-9aad-049ac6b58f51', 'created_at': datetime.datetime(2023, 12, 10, 18, 38, 36, 963395), 'updated_at': datetime.datetime(2023, 12, 10, 18, 38, 36, 963404)}", "[BaseModel] (24c34c81-49b3-4600-90e1-4bea8f819a75) {'id': '24c34c81-49b3-4600-90e1-4bea8f819a75', 'created_at': datetime.datetime(2023, 12, 10, 18, 42, 30, 525408), 'updated_at': datetime.datetime(2023, 12, 10, 18, 42, 30, 525414)}", "[BaseModel] (ebc082e8-c330-4a05-b8a9-7d043aff8ec7) {'id': 'ebc082e8-c330-4a05-b8a9-7d043aff8ec7', 'created_at': datetime.datetime(2023, 12, 10, 18, 42, 36, 603049), 'updated_at': datetime.datetime(2023, 12, 10, 18, 42, 36, 603059)}", "[User] (da07341b-989e-4e23-995f-0ff447d44a81) {'id': 'da07341b-989e-4e23-995f-0ff447d44a81', 'created_at': datetime.datetime(2023, 12, 10, 18, 42, 43, 265317), 'updated_at': datetime.datetime(2023, 12, 10, 18, 42, 43, 265328)}", "[User] (e0fd42d2-a713-4ac5-8ae0-f1e8497bda07) {'id': 'e0fd42d2-a713-4ac5-8ae0-f1e8497bda07', 'created_at': datetime.datetime(2023, 12, 10, 18, 42, 50, 220327), 'updated_at': datetime.datetime(2023, 12, 10, 18, 42, 50, 220333)}"]
(hbnb)
```

- **count**
  - Usage: `count <class>` or `<class>.count()`

Retrieves the number of instances of a given class.

```
root@KALI:~/AirBnB_clone# ./console.py
(hbnb) create Place
1d10cd47-94c4-484f-b66c-3777263fafb1
(hbnb) create Place
b93266af-c68b-4ec3-a095-b6f36dbb173e
(hbnb)create City
e116e6cd-b3c4-4501-9df9-ff689a428a9a
(hbnb)
(hbnb)count Place
3
(hbnb) city.count()
(hbnb)
```

- **update**
  - Usage: `update <class> <id> <attribute name> "<attribute value>"` or
    `<class>.update(<id>, <attribute name>, <attribute value>)` or `<class>.update(
<id>, <attribute dictionary>)`.

Updates a class instance based on a given id with a given key/value attribute
pair or dictionary of attribute pairs. If `update` is called with a single
key/value attribute pair, only "simple" attributes can be updated (ie. not
`id`, `created_at`, and `updated_at`). However, any attribute can be updated by
providing a dictionary.

```
 root@KALI:~/AirBnB_clone# ./console.py
(hbnb) create User
e9518a50-fc58-43c7-b4c7-197814902c1f
(hbnb)update User e9518a50-fc58-43c7-b4c7-197814902c1f first_name "ALX SCHOOOL"
['User', 'e9518a50-fc58-43c7-b4c7-197814902c1f', 'first_name', 'ALX SCHOOOL']
(hbnb)show User e9518a50-fc58-43c7-b4c7-197814902c1f
[User] (e9518a50-fc58-43c7-b4c7-197814902c1f) {'id': 'e9518a50-fc58-43c7-b4c7-197814902c1f', 'created_at': datetime.datetime(2023, 12, 10, 18, 46, 1, 440965), 'updated_at': datetime.datetime(2023, 12, 10, 18, 46, 1, 440974), 'first_name': 'ALX SCHOOOL'}
(hbnb)
```

## Testing :straight_ruler:

Unittests for the HBnB project are defined in the [tests](./tests)
folder. To run the entire test suite simultaneously, execute the following command:

```
$ python3 unittest -m discover tests
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```

## Authors :black_nib:

- **Mohammed OUZER** <[medouzer](https://github.com/medouzer)>
- **Mohammed EL HADDOUMI** <[elhaddoumi](https://github.com/elhaddoumi1999)>
