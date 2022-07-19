from flask import Flask,render_template, request, session
import os

app = Flask(__name__)

app.secret_key = ''


@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def index():
    user_response =''
    if request.method == 'POST':
        if request.form['name'] != '':           
            user_response = request.form['name']
            session['user'] = user_response
            session['logged_in'] = True
    return  render_template('index.html', user_response= user_response)


@app.route('/status', methods= ['GET', 'POST'])
def status():
    if session['logged_in'] == True:
            boss = session['user'] 

            return render_template('status.html', boss=boss,)
    else:
        return render_template(index.html)
                


@app.route('/submessage', methods= ['GET', 'POST'])
def submessage(): 
    if session['logged_in'] == True:
        if request.method == 'POST':
            your_message = request.form['message']
            with open('musoye.txt', 'a') as chatfile:
                chatfile.write(your_message + '\n')
        #session['message'] = your_message
        

        boss = session['user']
        with open('musoye.txt') as chatfile:
            messages = chatfile.read() 
        #boss2 = session['message']
        #new_message = boss2


    

        return render_template('status.html', boss=boss, messages = messages)
    else:
        return render_template(index.html)




@app.route('/logout', methods= ['GET', 'POST'] )
def logout():
    if request.method == 'post':
        session.pop('logged_in')
        session.pop('user')
        with open('musoye.txt', 'w') as chatfile:
            chatfile.write('')

    return render_template('index.html')






if __name__ == "__main__":
    app.run(debug=True)