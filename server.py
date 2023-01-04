from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('./web server/database.txt', mode='a') as database: # here was the stinky bug!
        email = data["email"] 
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}') 

def write_to_csv(data):
    with open('./web server/database.csv', newline='\n', mode='a', ) as database2: # another bug here! newline needed '\n' between the quotes.
        email = data["email"] 
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "Could not save to database."

    else:
        return 'something went terribly wrong.'