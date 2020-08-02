import smtplib 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls()   
s.login("sender-mail", "password") 
message = "Hey Developer, Finally we got the model trained. "
s.sendmail("sender_mail", "developer_mail", message) 
s.quit()
