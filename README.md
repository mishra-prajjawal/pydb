<div align="center">
  <img src="https://lh3.googleusercontent.com/drive-viewer/AJc5JmSynRJaUcThwO17y6ysw5hzhK7CW0lWatwhOVAJM6tn91JS7cGrvIgV9JDTA3KRpkNLRU8amCc=w1366-h657">
</div>

An open source folder-document(Hierarchy) model JSON(Javascript Object Notation) based Nosql Database Management System(DBMS) for fast data gathering,saving and reliable data redundancy without data loss and data transformation. 

pydb is developed as an hobby project  by I, Prajjawal Mishra and was made to tackle the complexity of other dbms for students but soon we realised that this can be used in vivid domains.

pydb is currently available in python only.
#### python 3.6 or above [Runs like hell]
### Official Languages Supported

Build Type                    | Status                                                                                                                                                                           | Stable
----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------
**Python** | Available | NO
**Javascript** | Not Available | No
**C++** | Not Available | No
**Rust** | Not Available | No
**Go** | Not Available | No
**Ruby** | Not Available | No
**C** | Not Available | No
**GO** | Not Available | No
**C#** | Not Available | No
**Java** | Not Available | No

## installation 
### python
```
$ pip install pydbms
```
To update pydb to the latest version, add `--upgrade` flag to the above
commands.
```
$ pip install pydbms --upgrade
```
# Your first database in pydb
## Python 3.6<
```
$ python
```
```python 
>>>import pydb 
>>>db = pydb.dbms()
>>>db.exe("mk mydb;")
```
`> Database Created`


`src => pydb/mydb/`


# docs - basic
Keyword | function | type of command
| :---:   | :---: | :---:|
mk | (Derived From - Make) Used to make a database | DDL
rm | (Derived From - Remove) Used to remove a database |DDL
crable | (Derived From - Create Table) | DDL
dable | (Derived From - Drop Table) | DDL
able | (Derived From - Alter Table)| DML



## License

[MIT](https://choosealicense.com/licenses/mit/)

## Authors

- [@mishra-prajjawal](https://www.github.com/mishra-prajjawal)




