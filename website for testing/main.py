from flask import Flask, render_template,request
from flask_mail import Mail

app = Flask(__name__)

app.config.update(

    MAIL_SERVER  = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'vision.official0119@gmail.com',
    MAIL_PASSWORD = 'PRATAP20'

    )

mail = Mail(app)



@app.route('/')
def Home():
    return render_template("index.html")   

@app.route('/contact',methods = ["GET","POST"])
def contact():
    if (request.method == 'POST'):
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        msg = request.form.get('msg')
        mail.send_message(
            
            'New mail by: '+ name,
            sender = email,
            recipients = ['vision.official0119@gmail.com'],
            body = msg + '\n Phone : ' + phone + '\n email : ' + email
        )
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/products')
def products():
    return render_template('product.html')

if __name__ == "__main__":
    app.run()
