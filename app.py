from flask import Flask, render_template, make_response
from firebase import firebase
 
app = Flask(__name__)
 
@app.route('/')
def index():
    firebase1 = firebase.FirebaseApplication('https://my-project-1524197842100.firebaseio.com/', None)
    data =  { 'Name': 'John Doe',
              'RollNo': 3,
              'Percentage': 70.02
              }
    result = firebase1.post('/users/pfQFoBG3WMnHV5jhdOtd/',data)
    firebase1.put('/users/pfQFoBG3WMnHV5jhdOtd/-M2XJ34bRQthJwG0S2lT','Name','Bob')
    firebase1.delete('/users/pfQFoBG3WMnHV5jhdOtd/', '-M2XJUf1F_aE_eftBcrt')
    result1 = firebase1.get('/users/pfQFoBG3WMnHV5jhdOtd/', '')
    print(result)
    print(result1)
    return render_template('index.html', context=result1)

if __name__ == '__main__':
    app.run(debug=True)
