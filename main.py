from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)


@app.route('/')
def yes_home():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline="", mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "Did not save to database"
    else:
        return 'Something went wrong. Try again!'


#
# @app.route("/index.html")
# def return_home():
#     return render_template("index.html")
#
#
# @app.route('/about.html')
# def about():
#     return render_template("about.html")
#
#
# @app.route('/works.html')
# def works():
#     return render_template("works.html")
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template("contact.html")
#
#
# @app.route('/work_001.html')
# def work_1():
#     return render_template('/work_001.html')
#
#
# @app.route('/work_002.html')
# def work_2():
#     return render_template('/work_002.html')
#
#
# @app.route('/work_003.html')
# def work_3():
#     return render_template('/work_003.html')
#
#
# @app.route('/work_004.html')
# def work_4():
#     return render_template('/work_004.html')
#
#
# @app.route('/work_005.html')
# def work_5():
#     return render_template('/work_005.html')
#
#
# @app.route('/work_006.html')
# def work_6():
#     return render_template('/work_006.html')


# if __name__ == "__main__":
#     app.run()
