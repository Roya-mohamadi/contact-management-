import sqlite3
class datbas:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        self.cur.execute("create table if not exists cantact (id integer primary key,fname text lname text phon text adress text )")
        self.con.commit()

    def fetch(self):
        self.cur.execute("select * from cantact")
        rows=self.cur.fetchall()
        return rows

    def insert(self,lname,fname,adress,phon):
        self.cur.execute("insert into cantact  values (null,?,?,?,?)",(lname,fname,phon,adress))
        self.con.commit()

    def delete(self,id):
        sql_delete="delete from cantact where id=?"
        self.cur.execute(sql_delete,(id,))
        self.con.commit()
        