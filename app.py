from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)
snippets = []

@app.route("/")
def index(): return render_template("index.html", snippets=snippets)

@app.route("/add", methods=["POST"])
def add():
    t, c = request.form.get("title"), request.form.get("content")
    if t and c: snippets.append({"title": t, "content": c})
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    if 0 <= id < len(snippets): snippets.pop(id)
    return redirect("/")

@app.route("/health")
def health(): return jsonify(status="up")

if __name__ == "__main__": app.run(host="0.0.0.0", port=5000)
