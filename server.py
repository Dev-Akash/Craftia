from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

connection = sqlite3.connect("db_Ak47.db")

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/dashboard", methods=["POST"])
def dashboard():
	if request.method == "POST":
		connection = sqlite3.connect("db_Ak47.db")
		crsr = connection.cursor()
		crsr.execute("SELECT Username, Password, Type FROM data_cred")
		ans = crsr.fetchall()
		flag = 0
		typeOF = ""
		for i in ans:
			#print(i)
			if (request.form["uname"] == i[0] and request.form["upass"]==i[1]):
				flag= 1
				typeOF = i[2]
				break
		if (flag == 1 and typeOF=="Industry"):
			return render_template("industry_dash.html")
		elif (flag == 1 and typeOF == "Individual"):
			return render_template("Individual_dash.html")
		elif (flag == 1 and typeOF == "NGO"):
			return render_template("NGO_dash.html")
		else:
			return "Access Denied"

@app.route("/industryDBSave", methods = ['GET','POST'])
def industryDBSave():
	if request.method == "POST":
		task = request.args.get("task")
		desc = request.args.get("des")
		quan = request.args.get("quant")
		dead = request.args.get("deadline")
		postD = datetime.now().strftime("%Y-%m-%d")
		postT = datetime.now().strftime("%H%M%S")
		postI = postD+postT
		postI = postI.replace("-","")
		postB = "indo"
		print(postI)
		skill = request.args.get("skill")

		connection = sqlite3.connect("db_Ak47.db")
		crsr = connection.cursor()
		param = (task, desc, quan, dead, postD, postT, postI, postB, skill)
		sqlcommand = ("""INSERT INTO 'posts' VALUES (?,?,?,?,?,?,?,?,?)""")
		crsr.execute(sqlcommand,param)
		connection.commit()
		connection.close()
		return "Thanks!"