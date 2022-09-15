from flask import Flask, render_template
import requests
app = Flask(__name__)
response = requests.get(url="https://api.npoint.io/2c21b2fca204fb30b798")
response.raise_for_status()
data = response.json()
@app.route('/')
def index():
    return render_template("index.html", all_posts=data)
@app.route('/about')
def aboutme():
    return render_template('about.html')
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/post/<int:post_id>")
def get_post(post_id):
    requested_post = None
    for posts in data:
        # print(post_id)
        # print(posts['id'])
        if int(posts['id']) == post_id:
            requested_post = posts
    return render_template("post.html", post=requested_post)



if __name__ == '__main__':
    app.run(debug=True, host="localhost",port=5000)