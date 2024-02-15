from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask,request
app = Flask(__name__)
@app.route('/notify/<name>', methods= ['GET'])
def ff(name):
    account_sid = 'your_account_sid_twilio'
    auth_token = 'auth_token_twilio'
    client = Client(account_sid, auth_token)
    print(name)
    ok = 'whatsapp:' +name
    print(ok)
    message = client.messages.create(
    from_='whatsapp:your_twilio_number',
    body = 'Jaldi waha se hato!! please give side to the emergency vehicle behind you',
    to=ok
    )
    # print(message.sid)
    return("Alert")

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the incoming message from Twilio
    incoming_msg = request.values.get('Body', '').lower()
    sender_number = request.values.get('From', '')
    
    # You can perform any processing here based on the incoming message
    
    # Prepare a response
    response_msg = "Received your message: " + incoming_msg
    print(incoming_msg)
    account_sid = 'your_account_sid_twilio'
    auth_token = 'auth_token_twilio'
    client = Client(account_sid, auth_token)
    # Send a response
    if incoming_msg == "start":
        # print("oi")
        mssg = "journey started"
    else:
        mssg = "enter valid keyword"
    client.messages.create(
        body=mssg,
        from_='whatsapp:your_twilio_number',
        to=sender_number
    )
    return '', 200
if __name__ == "__main__":
	app.run()
