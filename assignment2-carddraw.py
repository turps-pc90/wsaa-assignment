# Library Imports
from flask import Flask, request, jsonify, render_template
import requests

# Initiate Flask App
app = Flask(__name__)

# Endpoint for the root of the API & using render_template to push results to pokertable.html
@app.route('/drawcards')
def poker_request():
    deck_id = "new"
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
    response = requests.get(url)
    if response.status_code == 200:
        cards = response.json()
        return render_template('pokertable.html', cards=cards)
    else:
        return render_template('pokertable.html', error="You gotta know when to hold 'em, know when to fold 'em.")
    
    # Run the app
if __name__ == '__main__':
    app.run(debug=True)
