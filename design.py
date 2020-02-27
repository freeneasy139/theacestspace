from flask import Flask, render_template#, request

@app.route("/design")
def design():

        title = "ankesand.com | home"

        return render_template("design.html", title = title)
