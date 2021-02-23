import random #to generate random number as a code
import email #inbuild fuction to encode email messages
import smtplib #to send smtp messages

"""to generate the password random and send the code to the user and save it in the lock too"""
def password_genrator():
    number=[x for x in range(0,9)] #generate a series of 0-9 numbers for the password generation
    password=random.sample(number,6) #getting a random sample from the series of numbers 
    a=[str(x) for x in password] #the obtained number will be in the int formate to send it to the user converting it in the form of string
    a1="".join(a) #adding all the string into one string so that we can send the code
    return(a1) #returning the string code value

""" to add the generated code with extra word to make it more appeling"""

def adding_code_with_body(password):
    code="The one time password for unlocking the lock was\n"+password+"\nThank you"
    return code
""" adding the essential component of the sender and receiver id to the device and compiling it as the message"""
def mail_sender(code):
    sender="device01@gmail.com" #locks specified email id
    rece="user01@gmail.com" #receivers email id
    message = email.message.EmailMessage() #initiallizing the message as a email variable
    message["From"] = sender # sender user id must be sepcified for each device
    message["To"] = rece #user email id have to be changed
    message["Subject"] = "One time pass word for the lock" #message can be altered in the future
    message.set_content(code)  #the one time password 
    mail_server = smtplib.SMTP('smtp.gmail.com',587) #connecting to the smtp server 
    mail_server.starttls() #strating the session
    paas= "XXXXXXX" #password
    mail_server.login(sender,paas) #logging in the server using senders email and password
    mail_server.send_message(message) #sending the message
    print("Email sent successfully") #acknowlegement for sending mail
    mail_server.quit() #quiting the server
""" emergency mail fuction to alert the user about the intruders"""
def emergency_mail():
    code='''       warning someone is trying to breach inside the room without proper authenticion 
    please look into the alert kindly please check on the authentication system room and alert the 
    concern peoples''' 
    sender="device01@gmail.com" #locks specified email id
    rece="user01@gmail.com" #receivers email id
    message = email.message.EmailMessage() #initiallizing the message as a email variable
    message["From"] = sender # sender user id must be sepcified for each device
    message["To"] = rece #user email id have to be changed
    message["Subject"] = "Warning intruder alert!!!!!" #message can be altered in the future
    message.set_content(code)  #the one time password 
    mail_server = smtplib.SMTP('smtp.gmail.com',587) #connecting to the smtp server 
    mail_server.starttls() #strating the session
    paas= "XXXXXXX" #password
    mail_server.login(sender,paas) #logging in the server using senders email and password
    mail_server.send_message(message) #sending the message
    print("Alerting the Authenticated person") #acknowlegement for sending mail
    mail_server.quit() #quiting the server
""" authentication fuction to make sure the enterd code the real generated code is same and help imporves the security"""
def authentication(code):
    p=0 #intializing the trial variable
    while True: #intializing the infinite loop for the code correction
        real_password=code #setting up with the random code to the variable
        in_password=str(input("Enter your password:")) #getting input
        emergency="123456" #emergency value
        if(in_password==emergency): #emergency value check up
            print("1")
            break
        elif(in_password==real_password): #real password is correct welcomeing the user and breaking the operation
            print("Unlocked welcome master!!!!")
            break
        elif(in_password!=real_password): # if password is incorrect folling action and message will be displayed and the code will send the alert to the user
            p+=1
            if (p==1):
                print("have a look at the code again")
            elif(p==2):
                print("Are You alright master!!!!")
            elif(p==3):
                print("Bummer you little piece of shit warning master")
                emergency_mail() # call the function to send the alert mail to the user
                break


if __name__ == "__main__": #the place where the mail exection starts 
    password=password_genrator() #creating the variable
    mail_sender(adding_code_with_body(password)) #sending the mail using the funtion 
    authentication(password) #authenticating the user and password