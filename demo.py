import smtplib
import sys
import email.mime.text
# my test mail
mail_username='yuanyao428@gmail.com'
mail_password='y13838250011y'
from_addr = mail_username
to_addrs=('yuanyao428@gmail.com')

# HOST & PORT
HOST = 'smtp.gmail.com'
PORT = 587

# Create SMTP Object
smtp = smtplib.SMTP()
print('connecting ...')

# show the debug log
smtp.set_debuglevel(1)

# connet
try:
    print(smtp.connect(HOST,PORT))
except:
    print('CONNECT ERROR ****')
# gmail uses ssl
smtp.starttls()
# login with username & password
try:
    print('loginning ...')
    smtp.login(mail_username,mail_password)
except:
    print('LOGIN ERROR ****')
# fill content with MIMEText's object 
msg = email.mime.text.MIMEText('明日の朝何食べる？ from python')
msg['From'] = from_addr
msg['To'] = ';'.join(to_addrs)
msg['Subject']='test'
print(msg.as_string())
smtp.sendmail(from_addr,to_addrs,msg.as_string())
smtp.quit()