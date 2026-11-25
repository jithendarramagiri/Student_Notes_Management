from database.connection import DatabaseConnection
class AuthenticationQueries:
    @staticmethod
    def getUserData(email:str):
        db_config = cursor = None
        try:
            db_config = DatabaseConnection()
            cursor = db_config.cursor(dictionary=True)
            query = "select * from users where email = %s"
            cursor.execute(query,(email, ))
            user = cursor.fetchone()
            return user 
        except Exception as e:
            return f"Something wrong in \
                        database.utilsDB.AuthneticationQueries.getUserData():{e}"
        finally:
            if cursor: 
                cursor.close()
            if db_config: 
                db_config.close()


    # Insert user record into users table
    @staticmethod
    def createUserAccount(name:str, email:str,password:str):
        db_config = cursor = None
        try:
            db_config = DatabaseConnection()
            cursor = db_config.cursor(dictionary=True)
            query = """insert into users(username, email, hashpassword) values(%s, %s, %s)"""
            cursor.execute(query,(name, email, password))
            db_config.commit()
            return "Successfully account created" 
        except Exception as e:
            return f"Something wrong in \
                        database.utilsDB.AuthneticationQueries.createUserAccount():{e}"
        finally:
            if cursor: 
                cursor.close()
            if db_config: 
                db_config.close()



class NotesQueries:
    @staticmethod
    def addNotes(userid:int, title:str, content:str):
        db_config = cursor = None
        try:
            db_config = DatabaseConnection()
            cursor = db_config.cursor(dictionary=True)
            query = """insert into notes(userid, title, content) values(%s, %s, %s)"""
            cursor.execute(query,(userid, title, content))
            db_config.commit()
            return "Successfully Notes created" 
        except Exception as e:
            return f"Something wrong in \
                        database.utilsDB.NotesQueries.addNotes():{e}"
        finally:
            if cursor: 
                cursor.close()
            if db_config: 
                db_config.close()

    # get the user notes
    @staticmethod
    def getNotesByUserId(userid:int, title:str=None):
        db_config = cursor = None
        try:
            db_config = DatabaseConnection()
            cursor = db_config.cursor(dictionary=True)
            query = """select * from notes where userid = %s"""
            values = [userid]
            if title:
                query += " and title like %s"
                values.append(f"%{title}%")

            query += " order by updated_at desc"
            cursor.execute(query,values)
            data = cursor.fetchall()
            return data
        except Exception as e:
            return f"Something wrong in \
                        database.utilsDB.NotesQueries.getNotesByUserId():{e}"
        finally:
            if cursor: 
                cursor.close()
            if db_config: 
                db_config.close()


    # get notes by notes id 
    @staticmethod
    def getNotesByNotesId(userid:int, notesid:int):
        db_config = cursor = None
        try:
            db_config = DatabaseConnection()
            cursor = db_config.cursor(dictionary=True)
            query = """select * from notes where userid = %s and notesid = %s"""
            cursor.execute(query,(userid,notesid ))
            data = cursor.fetchone()
            return data
        except Exception as e:
            return f"Something wrong in \
                        database.utilsDB.NotesQueries.getNotesByNotesId():{e}"
        finally:
            if cursor: 
                cursor.close()
            if db_config: 
                db_config.close()


    # Update notes by notes id 
    @staticmethod
    def updateNotes(userid:int, notesid:int, title:str, content:str):
        db_config = cursor = None
        try:
            db_config = DatabaseConnection()
            cursor = db_config.cursor(dictionary=True)
            query = """update notes set title = %s, content = %s 
                        where notesid = %s and userid =%s"""
            cursor.execute(query,(title, content, notesid, userid))
            db_config.commit()
            return "Notes Updated"
        except Exception as e:
            return f"Something wrong in \
                        database.utilsDB.NotesQueries.updateNotes():{e}"
        finally:
            if cursor: 
                cursor.close()
            if db_config: 
                db_config.close()


    # Delete notes by notes id 
    @staticmethod
    def deleteNotes(userid:int, notesid:int):
        db_config = cursor = None
        try:
            db_config = DatabaseConnection()
            cursor = db_config.cursor(dictionary=True)
            query = """delete from notes where notesid = %s and userid =%s"""
            cursor.execute(query,(notesid, userid))
            db_config.commit()
            if cursor.rowcount == 0:
                return "Notes id not found"
            return "Notes deleted succefully"
        except Exception as e:
            return f"Something wrong in \
                        database.utilsDB.NotesQueries.deleteNotes():{e}"
        finally:
            if cursor: 
                cursor.close()
            if db_config: 
                db_config.close()




