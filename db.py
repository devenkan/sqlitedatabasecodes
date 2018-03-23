'''
In our definition of the connection, you see we're connecting to a database, called 'tutorial.db.'
This didn't exist prior in my case, but, when we run the code, if the database doesn't exist, it will be created. 
If it does exist, it will not be overwritten or re-created. Next, we defined the cursor. 
Think of the cursor like your mouse cursor, it simply does things, like select things, delete things, add things, and so on.
Now, most people think of a database, and think of rows and columns of data. That's actually a table.
Tables go in databases, and data goes in the tables.
A database may only contain a single table, or it may contain a thousand tables. Let's make a table:
Here, the cursor executes an SQL query. This one is an INSERT INTO, and the table name follows.
Then, we insert a tuple of values. After inserting we use conn.commit(). Think of conn.commit() much like saving the document. 
Recall how SQLite works. You have a file part before actually committing. You do not need to commit after every INSERT. 
Instead, you commit when you are done with that specific insertion task. You then close the cursor, and connection when you are totally
done. If you may be doing more inserts in a moment, then there's no reason to close the connection. If instead you are using SQLite on a registration page, 
for example, once the user has registered, you wouldn't want to leave that connection open wasting memory, you'd want to close it off.
Finally, in the code above, we run the functions, creating the table and entering a row. All set. How do we know it's done? We could run
another SQL query to request some data, but you may want to visually see your table from time to time. This can be done in a variety of
ways, but I prefer and recommend: SQLite Browser Notice that when we execute the query, we're executing it with the cursor as usual.
Then, to access the data from the cursor, we use c.fetchall(). Think of this again, much like the computer cursor. 
The select is like you highlighted, then you do c.fetchall(), so this is like you are copying your highlighted information.
Finally, we can either just print the data, or iterate through it, like pasting the information.
Also, note that we are not needing to do a conn.commit(). There's nothing to save.
'''


import sqlite3
conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")


def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")


def view():
        v=c.execute("SELECT * FROM stuffToPlot")
        rows = v.fetchall()
        print("\n unix and time frame")
        for row in rows:
        	print(row[0],row[1])



def delete(id):
	 c.execute("DELETE FROM stuffToPlot WHERE value=?", (id,))

def update(unix,datestamp,keyword,value):
	c.execute("UPDATE stuffToPlot SET unix=?,datestamp=? ,keyword=? WHERE Value=?",(unix,datestamp,keyword,value))

	
#create_table()	
#data_entry() //insertion of data
#view()
#delete(22)



update(22,2112,2,6);

view();

conn.commit()
c.close()
conn.close()
