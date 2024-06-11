import mysql.connector

class database:
    def __init__(self,db):
        self.con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="janakikandasamy",
            database=db
        )

        self.cur=self.con.cursor()



        sql = '''
        create table IF NOT EXISTS details(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name varchar(100),
        age varchar(5),
        doj varchar(20),
        email varchar(100),
        gender varchar(20),
        contact varchar(20),
        address varchar(100)
        );
        '''
        self.cur.execute(sql)
        self.con.commit()


    def insert(self,name,age,doj,email,gender,contact,address):
        sql1 = '''
        INSERT INTO details (name, age, doj, email, gender, contact, address)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        values=(name,age,doj,email,gender,contact,address)

        self.cur.execute(sql1,values)
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * from details")
        rows = self.cur.fetchall()
        #print(rows)
        return rows


    def delete(self,id):
        self.cur.execute("delete from details where id = %s",(id,))
        self.con.commit()


    def update(self,name,age,doj,email,gender,contact,address,id):
        sql2 = '''
        update details set name = %s,
        age = %s,
        doj = %s,
        email = %s,
        gender = %s,
        contact = %s,
        address = %s
        where id = %s
        '''

        self.cur.execute(sql2 , (name,age,doj,email,gender,contact,address,id))
        self.con.commit()






