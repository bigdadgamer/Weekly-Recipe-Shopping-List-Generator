#!/bin/python

import _csv
import glob
import smtplib
import random
from random import randint
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

recipes = []
chck = 0
bf = 0
chicken = 'chicken'
beef = 'beef'
v = 0

for file_name in glob.glob("recipe_files/" + '*.csv'):
    with open(file_name, 'r') as f:
        data = [tuple(line) for line in _csv.reader(f)]
        recipes.append(data)

print(recipes)
i = 0
text_file = open("ShoppingList.txt", "w")
text_file.write(
    "THIS IS THIS WEEKS SHOPPING LIST HUMAN! PROCEED TO THE SHOPPING MARKET AND PURCHASE THE ITEMS INDICATED! \n \n")
text_file.write("Shopping List")

while i < 7:
    n = randint(0, len(recipes) - 1)
    current = recipes[n]
    if bf < 2 or not beef in current[2][2]:
        if chck < 2 or not chicken in current[2][2]:
            if chicken in current[2][2]:
                chck = chck + 1
            if beef in current[2][2]:
                bf = bf + 1
            c = 0
            for r in current:
                if c > 1:
                    text_file.write('\n')
                    if r[1] == 'lbs':
                        text_file.write(r[0] + " ")
                        text_file.write(r[1] + " ")
                        text_file.write(r[2])
                    elif r[1] == '':
                        text_file.write(r[0] + " ")
                        text_file.write(r[2])
                    else:
                        text_file.write(r[2])
                elif c == 1:
                    text_file.write('\n')
                    text_file.write(r[0])
                    c = c + 1
                elif c == 0:
                    text_file.write('\n')
                    text_file.write('\n')
                    text_file.write(r[0])
                    c = c + 1
            i = i + 1

text_file.close()

print(chck)
print(bf)

fromaddr = "simongolden1987@msn.com"
toaddr = ["simongolden1987@msn.com"] #This should be a list of strings

msg = MIMEMultipart()

msg['From'] = 'YOUR EMAIL GOES HERE'
msg['To'] = 'YOUR EMAIL GOES HERE' #This has to be a string, make sure to not make it a tuple or list.
msg['Subject'] = "Shopping List"

attachment = open("Shoppinglist.txt", "r")
sl = MIMEText(attachment.read())
attachment.close()

msg.attach(sl)

s = smtplib.SMTP('smtp-mail.outlook.com', 587)
s.starttls()
s.login(fromaddr, 'YOUR PASSWORD HERE')
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()

print("e-mail sent!")
