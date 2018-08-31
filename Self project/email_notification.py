import feedparser
import notify2
import time
import os
import email
import getpass
import imaplib
import dbus

mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
user = input("Please enter the gmail usename: ")
password = getpass.getpass("Enter the password: ")
mail.login(user,password)
mail.select("INBOX")
ICON_PATH = os.getcwd() + '/gmail.ico'
notify2.init("Unread emails")
def loop():
    mail.select("INBOX")
    unread_mails = 0
    (retcode,messages) = mail.search(None,'(Unseen)')
    if retcode == 'OK':
        for num in messages[0].split():
            unread_mails += 1
            
    stat = notify2.Notification(unread_mails,icon=ICON_PATH)
    stat.set_urgency(notify2.URGENCY_NORMAL)
    stat.show()
    stat.set_timeout(15000)
    time.sleep(1200)
    

if __name__ == '__main__':
    try:
        while True:
            loop()
    finally:
        print("Thanks")
