from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# STORAGE
feedbacks = []
complaints = []
ratings = []

menuData = {
    "breakfast": "Idli & Sambar",
    "lunch": "Rice & Curry",
    "snacks": "Samosa & Tea",
    "dinner": "Chapati & Paneer Curry"
}

# HOME PAGE
@app.route('/')
def home():
    with open("index.html", "r", encoding="utf-8") as file:
        return render_template_string(file.read())

# UPDATE MENU
@app.route('/update_menu', methods=['POST'])
def update_menu():

    data = request.json

    menuData["breakfast"] = data["breakfast"]
    menuData["lunch"] = data["lunch"]
    menuData["snacks"] = data["snacks"]
    menuData["dinner"] = data["dinner"]

    return jsonify({
        "message": "Menu Updated Successfully"
    })

# GET MENU
@app.route('/get_menu')
def get_menu():
    return jsonify(menuData)

# FEEDBACK
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():

    data = request.json

    feedbacks.append({
        "name": data["name"],
        "feedback": data["feedback"]
    })

    return jsonify({
        "message": "Feedback Submitted"
    })

# COMPLAINT
@app.route('/submit_complaint', methods=['POST'])
def submit_complaint():

    data = request.json

    complaints.append({
        "name": data["name"],
        "complaint": data["complaint"]
    })

    return jsonify({
        "message": "Complaint Submitted"
    })

# RATING
@app.route('/submit_rating', methods=['POST'])
def submit_rating():

    data = request.json

    ratings.append(data["rating"])

    return jsonify({
        "message": "Rating Submitted"
    })

# VIEW FEEDBACKS
@app.route('/feedbacks')
def get_feedbacks():
    return jsonify(feedbacks)

# VIEW COMPLAINTS
@app.route('/complaints')
def get_complaints():
    return jsonify(complaints)

# VIEW RATINGS
@app.route('/ratings')
def get_ratings():
    return jsonify(ratings)

if __name__ == '__main__':
    app.run(debug=True)