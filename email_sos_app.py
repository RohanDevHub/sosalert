from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# ⚠️ Hardcoded credentials — for demo/competition use only
EMAIL_ADDRESS = "rrc.company462@gmail.com"
EMAIL_PASSWORD = "drmlfvyhjnydbzfs"
TO_EMAIL = "chaurasiyarohan265@gmail.com"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_alert', methods=['POST'])
def send_alert():
    data = request.get_json()
    lat = data.get('latitude')
    lon = data.get('longitude')

    if lat and lon:
        location_link = f"https://maps.google.com/?q={lat},{lon}"
    else:
        location_link = "Location not available"

    message_body = f"🚨 SOS ALERT! This is an emergency.\nLive Location: {location_link}"

    msg = MIMEText(message_body)
    msg['Subject'] = 'SOS Emergency Alert'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return "✅ SOS Email Alert Sent!"
    except Exception as e:
        return f"❌ Failed to send email: {e}"

if __name__ == '__main__':
    app.run(debug=True)
