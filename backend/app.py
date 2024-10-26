from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator() :
    result = None
    error = None
    if request.method == 'POST' :
        
        try :
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']
            if num1 == '' or num2 == '' :
                error = 'ERROR: Pls enter both nums'
            else :

                if operation == 'add' :
                    result = num1 + num2 
                elif operation == 'substract' :
                    result = num1 - num2
                elif operation == 'multiply' :
                    result = num1 * num2 
                elif operation == 'divide' :
                    if num2 != 0 :
                        result = num1 / num2
                    else :
                        result = 'Too bad, cant divided by 0'
        except ValueError :
            error = 'ERROR: Pls enter valid nums'
        
    return render_template('index.html', result=result, error=error)



if __name__ == '__main__' :
    app.run(debug=True)


