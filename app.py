from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def result():
    input1 = request.form.get("input1", type=int, default=0)
    input2 = request.form.get("input2", type=int, default=0)
    operation = request.form.get("operation")
    if(operation == 'Addition'):
        result = input1 + input2
    elif(operation == 'Subtraction'):
        result = input1 - input2
    elif(operation == 'Multiplication'):
        result = input1 * input2
    elif(operation == 'Division'):
        if(input1 == 0 and input2 == 0):
            result = 0
        else:
            result = input1 / input2
    else:
        result = 0
    entry = result
    return render_template('form.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)
