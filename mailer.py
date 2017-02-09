import smtplib

def send_emails(emails,shows,forecast):
    # connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')
    #start TLS encryption
    server.starttls()
    #login
    password = input('Please enter your password:')
    from_email = 'example@gmail.com'
    server.login(from_email, password)

    # send email to entire email list in the emails_file.txt
    for to_email,name in emails.items():
        message = 'Subject: Welcome to the e-shows for Southampton\n'
        message += 'Hi, ' + name + '!\n\n'
        message += forecast + '\n\n'
        message += shows + '\n\n'
        message += 'Hope to see you there!'
        server.sendmail(from_email,to_email, message)

    server.quit()
