import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
msg="I can send a mail!"
server.login("", "") ## Username , Password
server.sendmail("Sender", "Reciever", msg)
server.quit()
print("Sent")
