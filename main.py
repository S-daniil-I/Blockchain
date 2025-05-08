from flask import Flask, render_template, redirect, url_for, request
from block import write_block, check_integrity
import re

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    error_lender = None
    error_amount = None
    error_borrower = None

    if request.method == 'POST':
        lender = request.form['lender']
        amount = request.form['amount']
        borrower = request.form['borrower']

        valid = True

        if not re.match(r'^[a-zA-Z]+$', lender):
            error_lender = "Имя кредитора должно содержать только латинские буквы."
            valid = False

        try:
            float(amount)
        except ValueError:
            error_amount = "Сумма должна быть числом."
            valid = False

        if not re.match(r'^[a-zA-Z]+$', borrower):
            error_borrower = "Имя заемщика должно содержать только латинские буквы."
            valid = False

        if valid:
            write_block(name=lender, amount=amount, to_whom=borrower)
            return redirect(url_for('index'))
        else:
            return render_template('index.html', error_lender=error_lender, error_amount=error_amount, error_borrower=error_borrower, lender=lender, amount=amount, borrower=borrower)

    return render_template('index.html')

@app.route('/checking', methods=['GET'])
def check():
    results = check_integrity()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)