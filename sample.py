from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm, ForgotForm, ChangePasswordForm
import pyrebase

doctors = [

		{
		    'name': 'Dr Amresh Singh',
		    'location': 'Sector 31'
		},
		{
		    'name': 'Dr Randhava',
		    'location': 'Sector 31'
		},
		{
		    'name': 'Dr Samriti',
		    'location': 'Sector 32'
		},
		{
		    'name': 'Dr Anuj Jain',
		    'location': 'Sector 32'
		},
]

config = {
    'apiKey': "AIzaSyChVd-mQiwDpsy1CXdSltW2zDb9nXdD64g",
    'authDomain': "wecare-aeaca.firebaseapp.com",
    'databaseURL': "https://wecare-aeaca.firebaseio.com",
    'projectId': "wecare-aeaca",
    'storageBucket': "wecare-aeaca.appspot.com",
    'messagingSenderId': "532997492953",
    'appId': "1:532997492953:web:aa073f4ed16a2efac56ec8",
    'measurementId': "G-40RQWLBGZH"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()



app = Flask(__name__)

app.config['SECRET_KEY'] = 'e36717e1ebacf355e2404185940d8910'




@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',data=doctors)


@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return "Value Getting"+form.email.data
	return render_template('login.html',title='Login',form=form)


@app.route('/sign_up',methods=['GET','POST'])
def sign_up():
	return render_template('sign_up_subs_select.html',title='Sign Up')


@app.route('/patient_sign_up',methods=['GET','POST'])
def patient():
	form = RegistrationForm()
	if form.validate_on_submit():
		return "Value getting"
	return render_template('patient_sign_up.html',title='Sign Up',form=form)

@app.route('/mail')
def mail():
	return render_template('mail.html',title='Booking Done')

@app.route('/doctor_sign_up',methods=['GET','POST'])
def doctor():
	return "Signing up as Doctor"



@app.route('/about')
def about():
	data = db.child("Doctors").get()
	print(data.val())
	return render_template('about.html',title='About us')



if __name__ == '__main__':
    app.run(debug=True)