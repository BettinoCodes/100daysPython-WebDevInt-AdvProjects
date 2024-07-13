import requests
from bs4 import BeautifulSoup
import smtplib
import twilio
from twilio.rest import Client

#SMS OR EMAIL
account_sid = 'yours'
auth_token = 'yours'

item_url="https://www.amazon.com/Corsair-Vengeance-i7500-Gaming-PC/dp/B0CKXTTRKG/ref=sr_1_3?dib=eyJ2IjoiMSJ9.kwM9ErUA9on9WD1Ifc_IvwBV085CkexD_I7jKtHPrV1wemhxgVcekYxuKSAqDf_2ljbccUhFNpU27LlkaEpBBbOMr3C1MZYUkxDHiq7yGiCbQfAiWWbF0cPGdgfUTKkleTSC-i95TI0PGMT1S2pxniUeY1avUz9CnPpv7MnTdZahDFuJs_mOv-Zjb0xVnrjI9eXL2_F79g2a4JL8eYFHpJKNAyyqSCmbEdkLwPZmIF8._12E49Z87QjJfZ2bhKxfBhlt3mOH8N2tbSKPEAoK518&dib_tag=se&keywords=best%2Bgaming%2Bpc&qid=1720907327&sr=8-3&th=1"

response = requests.get(item_url)
data = response.text

soup = BeautifulSoup(data, "html.parser")

price = soup.find_all(name="span", class_="a-offscreen")

item_price = price[1].getText()[1:]
prc_no_comma = ""

i = 0
while i < len(item_price):
    if item_price[i] == ",":
        i += 1
    else:
        prc_no_comma += item_price[i]
        i += 1

float_prc = float(prc_no_comma)
print(f"Floated price: {float_prc}")


#price to float 

if float_prc < 3500:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:thenum',
        body=f'THE CRAZY GAMING PC YOU WATCHING IS ON SALE B. {item_url}',
        to='whatsapp:+yournum'
    )
    print(message.status)
    print(message.sid)
    #TEST FOR EMAIL
    # my_email = "YOURSS@gmail.com"
    # password = "randomcode"

    # connection = smtplib.SMTP("smtp.gmail.com", port=587)
    # connection.starttls()

    # connection.login(user=my_email, password=password)
    # connection.sendmail(
    #     from_addr=my_email,
    #     to_addrs="recieve email",
    #     msg=f"Subject:LOWER PRICE PC AMAZON\n\n THE CRAZY GAMING PC YOU WATCHING IS ON SALE B. {item_url}"
    #     )

    # connection.close()
