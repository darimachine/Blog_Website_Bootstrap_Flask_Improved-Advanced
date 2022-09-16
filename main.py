from flask import Flask, render_template,request
import requests, smtplib

app = Flask(__name__)
#api
response = requests.get(url="https://api.npoint.io/2c21b2fca204fb30b798")
response.raise_for_status()
data = response.json()
#flask posts
@app.route('/')
def index():
    return render_template("index.html", all_posts=data)
@app.route('/about')
def aboutme():
    return render_template('about.html')
#changing posts in post
@app.route("/post/<int:post_id>")
def get_post(post_id):
    requested_post = None
    for posts in data:
        # print(post_id)
        # print(posts['id'])
        if int(posts['id']) == post_id:
            requested_post = posts
    return render_template("post.html", post=requested_post)
#contact form methods
@app.route('/contact', methods=['GET','POST'])
def get_data():
    msg_header=False
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone_number = request.form['number']
        message = request.form['message']
        print(name)
        print(email)
        print(phone_number)
        print(message)
        sent_mail(name,email,phone_number,message)
        msg_header = True
        return render_template('contact.html', msg_sent=msg_header)
    return render_template("contact.html", msg_sent=msg_header)
#sent_email
def sent_mail(name,email,phone,msg):
    my_email = "serhan.chavdarliev@suborino.eu"
    password = "gizefsujxnrlxklu"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(my_email,my_email,msg=f"Subject:New Message\n\n Name: {name} \nEmail: {email} \nPhone-Number: {phone} \nMessage: {msg}")

if __name__ == '__main__':
    app.run(debug=True, host="localhost",port=5000)