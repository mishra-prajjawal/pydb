import os
class db:
    #we are making a Database in Python Json 
    """db object for db related operations"""
    def __init__(self):
        """initialize the db object"""
        if os.path.exists("pydb"):
            #if the file exists then we will load the data from the file
            self.db = None
            self.keys = {'keywords': {'db_cmd':{'keys':["mk","rm",],'cmd_type':0},'db_tbl_cmd': {'keys':["create table","drop table","alter table"]}},'cmds' :["mk","rm","show dbs","usedb"]}#{'keywords': {'db_cmd':{'keys':["mk","rm",],'cmd_type':0}},'cmds' :["mk","rm","show dbs","usedb"]}
        else:
            #if the file does not exists then we will create the file
            os.mkdir("pydb")
    def exe(self,command):
        """execute the command"""
        def indb(db_name):
            """check if the database exists"""
            if db_name in os.listdir("pydb"):
                return True
            else:
                return False
        def mkdb(name): 
            """create a database"""
            try:
                os.mkdir("pydb/"+name)
                return "Database Created"
            except FileExistsError:
                return ("(Database Error)-- pydb error: 002dbx -- Database already exists")
        def rmdb(name):
            """remove a database"""
            try:
                os.rmdir("pydb/"+name)
                return "Database Removed"
            except FileNotFoundError:
                return ("(Database Error)-- pydb error: 003dbx -- Database does not exists")
        def dbtype(command):
            """create a type"""
            if command == "mk" :
                return 1
            elif command == "rm":
                return 2
            elif command == "show dbs":
                return 3
            elif command == "usedb":
                return 4
            else:
                return 0
        #print(self.keys)[working]->8n print(command)[working]->9n
        data_const = (command.lower()).split()
        cmd_ = None
        keys = None
        type = None
        #print(data_const)[working]->11n print(data_const[len(data_const)-1][-1])[working]->12n
        if data_const[len(data_const)-1] != ";" and data_const[len(data_const)-1][-1] != ";":
            print("(End Line Error)-- pydb error: 001cx -- Invalid Syntax (Missing ';')")
        else: 
            #join a list of strings
            if "".join(data_const).split(";")[0] == "showdbs":
                print(os.listdir("pydb"))
            elif data_const[0] == "usedb":
                
                self.db = data_const[1].split(";")[0]
                if indb(self.db):
                    print("using db",data_const[1].split(";")[0])
                else:
                    print("(Not Found Error)-- pydb error: 004dbx -- Database does not exists")
            elif data_const[0] in self.keys["cmds"]:
                for i in self.keys["keywords"].keys():
                    if " ".join(data_const).split(";")[0] in self.keys["keywords"][i]["keys"]:
                        type = self.keys["keywords"][i]["cmd_type"]
                        cmd_ = " ".join(data_const).split(";")[0]
                        keys = self.keys["keywords"][i]["keys"]
                        print(cmd_)
                        break
                    elif data_const[0] in self.keys["keywords"][i]["keys"]:
                        type = self.keys["keywords"][i]["cmd_type"]
                        cmd_ = data_const.pop(0)
                        keys = self.keys["keywords"][i]["keys"]
                        break
                if self.db != None: 
                    print("self.db",self.db) 
                elif cmd_ == keys[dbtype(cmd_)-1] and cmd_=="mk" and type==0 and dbtype(cmd_)!=-1:
                    #create a folder in in directory named pydb 
                    # and name that folder with the name of the database given 
                    # by the user
                    print(mkdb(data_const[0].lower().split(";")[0]))
                elif cmd_ == "rm" and  cmd_ == keys[dbtype(cmd_)-1] and type==0 and dbtype(cmd_)!=-1:
                    print(rmdb(data_const[0].lower().split(";")[0]))
                else:
                    print("(Command Error)-- pydb error: 003cx -- Invalid Command (Command not found)")
            else:
                print("(Command must start with keywords)-- pydb error: 001dbx -- Invalid Syntax (Missing keywords)")
        
# Path: main.py
if __name__ == "__main__":
    db = db()
    while True:
        command = input("pydb> ").lower()
        if command == "exit;":
            print("bye")
            break
        elif command[-1] !=";" :
            a = []
            while True:
                cmd = input("> ")
                if cmd == ";":
                    a.append(cmd)
                    for i in a:
                        command +=" ".join(i)
                        print("")
                    break
                else: 
                    a.append(cmd)
                    continue
            db.exe(command) 
        else:
            db.exe(command)
            continue

