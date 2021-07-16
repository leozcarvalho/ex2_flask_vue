from flask import Flask, jsonify, request
from flask_cors import CORS

NUMBERS = [
{
    'numbers': [1, 2, 3]
}
]

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})
    
@app.route('/numbers', methods=['GET'])
def get_result():
    response_object = {'status': 'success'}
    response_object['numbers'] = NUMBERS
    return jsonify(response_object)

@app.route('/numbers', methods=['POST'])
def post_numbers():
    post_data = request.get_json()
    numbers = post_data.get('numbers')
    NUMBERS.append({
        'numbers': post_data.get('numbers')
    })

    reverseNumbers = reverseList(numbers)

    sumNumbers = sumList(numbers)

    medNumbers = medList(numbers)

    upMedNumbers = upMed(numbers)

    underValuesSeven = underSeven(numbers)

    return jsonify(numbers, reverseNumbers, sumNumbers, medNumbers, upMedNumbers, underValuesSeven)

def reverseList(list):
    return list[::-1]

def sumList(list):
    
    sumNumbers = 0
    
    for index in range(0, len(list)):
        sumNumbers = sumNumbers + list[index]
    
    return sumNumbers

def medList(list):
    return sumList(list) / len(list)

def upMed(list):
    upMed = []
    for index in range(0, len(list)):
        if list[index] > medList(list):
            upMed.append(list[index])
    return upMed

def underSeven(list):
    underServen = []
    for index in range(0, len(list)):
        if list[index] < 7:
            underServen.append(list[index])
    return underServen

if __name__ == '__main__':
    app.run()