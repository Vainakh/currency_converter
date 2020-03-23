from flask import Flask, render_template, request, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, Decimal, requests

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

url = "https://api.exchangeratesapi.io/api/" #current times could be imported

legit_currencies = ['USD', 'GBP']

@app.route('/', methods=['GET','POST'])
def render_converter():
    """Show converter form and get conversion rate"""
    if request.method == 'POST':
        # instead '/converter' i am using url_for
        return redirect('/converter')
    else:

    #     # for error message, rendering template again with errors
        return render_template("base.html")

@app.route('/converter', methods=['POST'])
def convert():
    """ Display converted amount"""
    if request.method == 'POST':
        # storing three form inputs into variables
        first_currency = request.form.get("convert-from")
        second_currency = request.form.get("convert-to")
        amt = request.form.get("amount")
        # write 3 validation in the form of if statements 
        if (first_currency in legit_currencies and second_currency in 
            legit_currencies and amt.isalpha() is False):
        # if first_currency in legit_currencies 
        # if they all pass, this is the HAPPY path
            currency_rate = CurrencyRates(force_decimal=True)
            converted_amount = round(currency_rate.convert(first_currency,
                                                     second_currency, 
                                                     Decimal(amt)),2)
            return render_template('converter.html', converted_amt=converted_amount)
        else:
            return render_template('base.html', first_currency=first_currency,
                                                second_currency=second_currency,
                                                error=True)



# @app.route('/errors', methods=['POST'])
# def errors():
#     """Display errors"""
#     if request.method == 'POST':
#         first_currency = request.form.get("convert-from")
#         second_currency = request.form.get("convert-to")

#         return render_template('errors.html', first_currency=first_currency, 
#                                               second_currency=second_currency)


    
