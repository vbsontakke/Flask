from flask import Flask, render_template

app = Flask(__name__)

allposts = [{
                'title': 'Post 1',
                'author': 'Vinayak',
                'content': 'Post 1 content'
            },
            {
                'title': 'Post 2',
                'content': 'Post 2 content'
            }
]

# Setting route
@app.route("/")
@app.route("/home")
def hello():
    return render_template('index.html')

# Setting route
@app.route("/posts")
def posts():
    return render_template('posts.html', posts = allposts)



if __name__ == "__main__":
    app.run(debug=True)