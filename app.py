from flask import Flask, jsonify, request

app = Flask(__name__)

# methods that represent URLs or links

# Home or Root route!
REMINDERS = []


@app.route("/")
def index():
    return jsonify({"name": "Nadia"})


# we want to store "reminders"
#
# how do we save the reminders?





@app.route("/add-reminder", methods=["POST"])
def add_reminder():
    print("@@@@@@@@")
    print(request.json) 
    print("@@@@@@@@")
    REMINDERS.append(request.json)
    # Exercise, add the reminders (dictionaries) to the REMINDERS constant
    return jsonify({"reminders": REMINDERS })

# Core HTTP verbs a developer must know
# - GET
# - POST
# - DELETE
# - PATCH

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5050)
    
    
    
    
    
    
#     # create an empty list
# l = []

# # create a dictionary with student details
# student = {7058:'sravan kumsr Gottumukkala',
# 7059:'ojaswi',7060:'bobby',
# 7061:'gnanesh',7062:'rohith'}

# # append this dictionary to the empty list
# l.append(student)

# # display list
# l 