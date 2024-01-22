from flask import Flask, render_template, request, redirect

import dao

app = Flask(__name__)

@app.route("/")
def list():
  result = dao.findall()
  return render_template("list.html", list=result)

@app.route("/read")
def read():
  bno = request.args.get('bno', type=int)
  result = dao.findone(bno)
  return render_template("read.html", board=result)

@app.route("/write")
def view_write():
  return render_template("write.html")

@app.route("/write", methods=['post'])
def do_write():
  writer = request.form.get('writer', type=str)
  title = request.form.get('title', type=str)
  content = request.form.get('content', type=str)
  dao.save(writer=writer, content=content, title=title)
  return redirect("/")

@app.route("/update", methods=['post'])
def update():
  bno = request.form.get('bno', type=int)
  title = request.form.get('title', type=str)
  content = request.form.get('content', type=str)
  dao.update(bno=bno, title=title, content=content)
  return redirect("/")

@app.route("/delete", methods=['post'])
def delete():
  bno = request.form.get('bno', type=int)
  dao.delete(bno=bno)
  return redirect("/")

app.run(debug=True)
