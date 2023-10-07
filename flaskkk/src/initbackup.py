from flask import Flask, redirect, url_for, render_template, request, session

app=Flask(__name__)
app.secret_key='qonda'


@app.route('/')
def home():
	return render_template('index.html',content=['para','bailar','la','bamba'],se=['se','necesita'],gracia=['una','poca','de','gracia'],patipami=["pa' ti","pa' mi",'y arriba y arriba'],bailalabamba=['baila la bamba'])


@app.route('/maine')
def ahre():
	return render_template('sobalia.html')



if __name__=='__main__':
	db.create_all()
	app.run(debug=True)