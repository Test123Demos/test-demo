from flask import Flask,redirect,url_for,request,render_template

app=Flask(__name__)

def index():
    return "hello word!"
app.add_url_rule("/",view_func=index)

@app.route("/l",methods=["get"])
def login():
    return "登录成功！"

@app.route("/<name>")
def name(name):
    return f"{name}"

@app.route("/path/<path:sub_path>") #http://127.0.0.1:5000/path/as/as
def path(sub_path):
    return f"{sub_path}" #返回/as/as

@app.route("/admin/<name>")
def admin(name):
    return f"{name}"

@app.route("/user/<name>")
def user(name):
    return f"{name}"

@app.route("/all/<name>")
def all(name):
    if name=="admin":
        return redirect(url_for("admin",name=name)) #url_for重定向到别的路由函数上去
    else:
        return redirect(url_for("user",name=name))


@app.route("/tm")
def tm():
    return render_template("login.html") #访问login.html，里面的接口调、login的接口


@app.route("/weclome/<name>")
def weclocme(name):
    return f"欢迎：{name}"

@app.route("/login",methods=["POST"])
def hello_user():
    if request.method=="GET":
        return "GET"
    elif request.method=="POST":
        user=request.form["nm"] #获取请求的nm值
        return redirect(url_for("weclocme",name=user))


if __name__ == '__main__':
    app.debug=True
    app.run()
