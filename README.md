# rest-api-transliterate-mn
Rest API for transliterating Latin english to Cyrillic Mongolian

###### How to use
curl -H "Content-Type: application/json" -X POST -d '{"text":"hello world"}' http://localhost:5000/

###### Required packages
- flask
- request
- jsonify
- transliterate

###### Testing
curl localhost:5000/

###### Online Testing
App is deployed on Heroku. 
To test:
curl -H "Content-Type: application/json" -X POST -d '{"text":"hello world"}' https://dry-fortress-12068.herokuapp.com/
