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
