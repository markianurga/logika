import sqlite3

con = sqlite3.connect("extra/dib.db")
cocor = con.cursor()

cocor.execute("""
INSERT INTO students(
stndent_neme,avy_ckore,class,peret_neme)
VALUES(
'лукян', 11, '6б', 'іван')             
              """)
con.commit()

cocor.execute("""
SELECT * FROM students              
              """)
data = cocor.fetchall() 
print(data)