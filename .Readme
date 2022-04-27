for running the application 
create a virtualenvironment and activate it then run
pip install -r requirements.txt

then run the server with python manage.py runserver


APIs
http://127.0.0.1:8000/app --get
list all the apps -both for admin and user

Js Code:
var myHeaders = new Headers();
myHeaders.append("Authorization", "Token 8fb866555b9015548c3fade150b909dac982294e");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("http://127.0.0.1:8000/app", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));


  


http://127.0.0.1:8000/get-list-of-apps-data   --post
by passing the list of values it returns all the apps with that ids
eg: values:[1,2,3]
Js Code:
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("Authorization", "Token 8fb866555b9015548c3fade150b909dac982294e");

var raw = JSON.stringify({
  "values": [
    1,
    2,
    3
  ]
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("http://127.0.0.1:8000/get-list-of-apps-data", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));







http://127.0.0.1:8000/app     --post
creating apps
works only for admin
for user it donot create apps because of custom permissions

Js Code:
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("Authorization", "Token 8fb866555b9015548c3fade150b909dac982294e");

var raw = JSON.stringify({
  "name": "Snapchat",
  "url": "com.snapchat.com",
  "points": 100,
  "category": 1,
  "sub_category": 1
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("http://127.0.0.1:8000/app", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));