from flask import Flask,jsonify, request

app=Flask(__name__)

@app.route('/hello')
def hello () :
    return "hello"

tasks=[
{
    "id":1,
    "Name":'raju',
    'Contact':'6578456787',
    'done':False
},
{
    "id":2,
    "Name":'sohan',
    'Contact':'8376684598',
    'done':False 
}
]

@app.route('/get')
def getData():
    return jsonify({
    "data":tasks
    })

@app.route('/add-data',methods=['POST'])
def add_data():
    if not request.json:
        return jsonify({
            "status":'error',
            "message":'error message please provide data'
        },400)
    
    task={
        "id":tasks[-1]['id']+1,
        "Name":request.json['Name'],
        "Contact":request.json.get('Contact',''),
        'done':False
    }
    tasks.append(task)
    return jsonify({
            "status":'success',
            "message":'task added succesfully'
        })

if(__name__=="__main__"):
    app.run(debug=True)