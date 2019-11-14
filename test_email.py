import imaplib
import base64
import os
import email

email_user = 'rbender4@liberty.edu'
email_pass = ''

mail = imaplib.IMAP4_SSL('imap.mail.yahoo.com')
mail.login('ryanbender65@yahoo.com', email_pass)
print(mail)
