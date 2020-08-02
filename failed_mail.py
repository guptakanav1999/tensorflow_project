import smtplib 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls()   
s.login("sender-mail", "password") 
message = "Hey Developer, you need to check your code once. Might be this have some error. " 
s.sendmail("sender-mail", "developer_mail", message) 
s.quit()
