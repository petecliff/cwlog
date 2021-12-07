import sqlite3
from pprint import pprint
from flask import render_template, request
from app import app

def get_db_connection():
    conn = sqlite3.connect('cwlog.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def item():

    app.logger.error(request.form.get('action'))

    conn = get_db_connection()

    if request.method == 'POST':
        if request.form.get('action') == 'Clear':
            conn.execute("DELETE FROM items")
        else:    
            item = request.form.get('item')
            conn.execute("INSERT INTO items (item) VALUES (?)", (item,))
        conn.commit()

    items = conn.execute('SELECT * FROM items').fetchall()

    conn.close()

    return render_template('index.html', items=items)
