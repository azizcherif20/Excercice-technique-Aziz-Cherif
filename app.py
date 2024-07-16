from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuration de la base de données
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'projet_amiral_gestion_db'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fonds')
def fonds():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM referentiel_fonds")
    fonds = cursor.fetchall()
    return render_template('fonds.html', fonds=fonds)

@app.route('/instruments')
def instruments():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM referentiel_instruments")
    instruments = cursor.fetchall()
    return render_template('instruments.html', instruments=instruments)

@app.route('/historique_prix/<int:instrument_id>')
def historique_prix(instrument_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT date, prix FROM historique_prix WHERE instrument_id = %s ORDER BY date", (instrument_id,))
    historique = cursor.fetchall()
    return {
        "dates": [str(date) for (date, prix) in historique],
        "prix": [float(prix) for (date, prix) in historique]
    }

@app.route('/positions/<int:fond_id>')
def positions(fond_id):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT p.id, i.nom, p.quantite, p.date_achat
        FROM positions p
        JOIN referentiel_instruments i ON p.instrument_id = i.id
        WHERE p.fond_id = %s
    """, (fond_id,))
    positions = cursor.fetchall()
    return render_template('positions.html', positions=positions)

@app.route('/search_fonds', methods=['GET', 'POST'])
def search_fonds():
    if request.method == 'POST':
        search_query = request.form['search']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM referentiel_fonds WHERE nom LIKE %s", ('%' + search_query + '%',))
        fonds = cursor.fetchall()
        return render_template('fonds.html', fonds=fonds)
    return redirect(url_for('fonds'))

@app.route('/search_instruments', methods=['GET', 'POST'])
def search_instruments():
    if request.method == 'POST':
        search_query = request.form['search']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM referentiel_instruments WHERE nom LIKE %s", ('%' + search_query + '%',))
        instruments = cursor.fetchall()
        return render_template('instruments.html', instruments=instruments)
    return redirect(url_for('instruments'))


if __name__ == '__main__':
    app.run(debug=True)
