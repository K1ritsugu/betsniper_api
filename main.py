from flask import request, jsonify, Flask
from database import insert_new_event, get_all_events

app = Flask(__name__)


@app.route("/getEvents", methods=['POST'])
def get_events():
    data = request.get_json()
    events = data["events"]

    for number_event, event in enumerate(events):

        type_bet = event["type_bet"]
        bookmaker = event["bookmaker"]
        link = event["link"]
        coef = event["coef"]
        match_name = event["match_name"]
        profit = event["profit"]
        first_time = event["first_time"]
        sport = event["sport"]
        operation = insert_new_event(type_bet, bookmaker, link, coef, match_name,
                                     profit, first_time, sport, number_event)

        if not operation["success"]:
            return jsonify(operation)

    return jsonify({"success": True}), 200


@app.route("/updateEvents", methods=['GET'])
def update_events():
    events = get_all_events()
    return jsonify({"events": events, "success": True}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=911, debug=True, ssl_context=('SSL/cert.pem', 'SSL/key.pem'))