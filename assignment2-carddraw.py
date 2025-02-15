# Library Imports
from flask import Flask, request, jsonify, render_template
from two_hands_compare import *

# Initiate Flask App
app = Flask(__name__)

# Endpoint for the root of the API & using render_template to push results to pokertable.html
@app.route('/drawcards')
def poker_request():
    hand1_name, hand2_name, result, deal_one, deal_two = poker_request2()
    # Check that poker_request2() worked by verifying hand1_name <> None
    if hand1_name:
        return render_template('pokertable.html', hand1=hand1_name, hand2=hand2_name, result=result, cards1=deal_one, cards2=deal_two)
    else:
        return render_template('pokertable.html', error="You gotta know when to hold 'em, know when to fold 'em.")
    
    # Run the app
if __name__ == '__main__':
    app.run(debug=True)
