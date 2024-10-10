import requests
import time
import hashlib
import yagmail

sender_email = "mycourses.n.m@gmail.com"
receiver_email = "ninamaricc02@gmail.com"
message = 'Website has been updated'
password = 'baletanke'


def send_mail():    
    yag = yagmail.SMTP(sender_email)
    yag.send(
        to=receiver_email,
        subject='nicko licko',
        contents=message,

    )


def check_website_for_updates(url, previous_hash):
    try:
        response = requests.get(url)
        response.raise_for_status()
        current_content = response.text
        current_hash = hashlib.sha256(current_content.encode('utf-8')).hexdigest()
        if current_hash != previous_hash:
            send_mail
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error checking website: {e}")
        return False
    
if __name__ == "__main__":
    url = "https://ef.unibl.org/predmeti-i-predavaci/predmeti-stranica?predmet=23"
    previous_hash = None
    
    while True:
        if check_website_for_updates(url, previous_hash):
            previous_hash = hashlib.sha256(requests.get(url).text.encode('utf-8')).hexdigest()
        time.sleep(60)
