from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        print('Something went wrong, Try Again!')

def write_to_csv(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    with open('database.csv',newline='', mode='a' ) as database:
        csv_writer = csv.writer(databsase, delimiter=',')
        csv_writer.writerow([email, subject, message])



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
