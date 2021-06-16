import smtplib
def gmail():
    print("CONNECTING TO GMAIL")
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        print("CONNECTED")
        print("STARTING SECURE CONNECTION")
        try:
            server.starttls()
            print("SECURED CONNECTION REACHED")
        except:
            print("WARNING: ITS NOT SAFE SEND THIS EMAIL")
        gmailUser = str(input("USERNAME: "))
        gmailPasswd = str(input("PASSWORD: "))
        print("CHECKING USERNAME AND PASSWORD")
        try:
            server.login(gmailUser, gmailPasswd)
            print("YOUR USERNAME AND PASSWORD ARE CORRECT")
        except:
            print("YOUR USERNAME, PASSWORD OR BOTH IS INCORRECT")
            quit
        recipient = str(input("RECIPIENT: "))
        message = str(raw_input("MESSAGE:\n"))
        print("SENDING EMAIL")
        try:
            server.sendmail(gmailUser, recipient, message)
            print("MESSAGE SENT FROM: " + gmailUser)
            quit
        except:
            print("AN ERROR OCCURED WHILE SENDING YOUR E-MAIL")
            quit
    except:
        print("CANNOT CONNECT TO GMAIL")
        quit

choice = str(input("IM Network? GMAIL/YAHOO: "))
if choice == "GMAIL":
    gmail()
elif choice == "YAHOO":
    yahoo()
else:
    print("IM NETWORK NOT RECOGNISED")
    quit





    
