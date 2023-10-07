from flask import Flask, redirect, url_for, render_template, request, session

from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key='qonda'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://dgosqamu:FdPAFGmhWD8vCXffF569JwEj_fIRMpQn@isilo.db.elephantsql.com/dgosqamu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db=SQLAlchemy(app)

class users(db.Model):
	_id=db.Column('id',db.Integer,primary_key=True)
	name=db.Column(db.String(100))
	email=db.Column(db.String(100))
	profesion=db.Column(db.String(100))

	def __init__(self,name,email,profesion):
		self.name=name
		self.email=email
		self.profesion=profesion


@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
	return render_template('index.html',content=['para','bailar','la','bamba'],se=['se','necesita'],gracia=['una','poca','de','gracia'],patipami=["pa' ti","pa' mi",'y arriba y arriba'],bailalabamba=['baila la bamba'])

@app.route('/view')
def view():
	return render_template('view.html',values=users.query.all())

@app.route('/maine')
def ahre():
	return render_template('sobalia.html')

@app.route('/login',methods=['POST','GET'])
def login():
	if request.method=='POST':
		session.permanent=True
		user=request.form['nm']
		profesion=request.form['profesion']
		session['user']=user
		session['profesion']=profesion
		founuser=users.query.filter_by(name=user).first()
		if founuser:
			session['email']=founuser.email
			if len(profesion) > 0:
				founuser.profesion=profesion
				db.session.commit()
			else:
				session['profesion']=founuser.profesion
		else:
			usr=users(user,'',profesion)
			db.session.add(usr)
			db.session.commit()
		return redirect(url_for('user'))
	else:	
		return render_template('inloggen.html')

@app.route('/user',methods=['POST','GET'])
def user():
	mail="a definir"
	profesion="a definir"
	if 'user' in session:
		user=session['user']
		if request.method=='POST':
			mail=request.form['mail']
			session['mail']=mail
			founuser=users.query.filter_by(name=user).first()
			founuser.email=mail
			db.session.commit()
		else:
			if 'mail' in session:
				mail=session['mail']
			if 'profesion' in session:
				profesion=session['profesion']
		return render_template('qhacestodobien.html',usr=user,mail=mail,profesion=profesion)
	else: 
		return redirect(url_for('login'))

@app.route('/logout')
def logout():
	session.pop('user',None)
	session.pop('mail',None)
	return redirect(url_for('login'))

if __name__=='__main__':
	db.create_all()
	app.run(debug=True, host='0.0.0.0', port=6050)