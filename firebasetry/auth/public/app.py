from flask import Flask, render_template
from twilio.rest import Client

app = Flask(__name__)
values = []
f = open('data.txt', 'r+')
for line in f:
    values.append(float(line))
f.close()
a = values[-1]




def driver():
    if(a<22):

        name = 'Full'
        sendText()
        return render_template("driver.html", name=name)
    else:
        name = 'Empty'
        return render_template("driver.html", name=name)


if __name__ == "__main__":
    app.run(port=4995)

def sendText():
    account_sid = 'AC3e1ccc9a78e3fa13f07fd7f3a3411578'
    auth_token = '3b3860439badcf0467bb59ff4ff619c6'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Your trash can with ID: 001 is full!",
        from_='+12052932976',
        to='+18065070617'
    )

    print(message.sid)
