###################################################################################################################
#############################  Whatsapp for Linux (Ver: 1.0)  #####################################################
#############################  By (Denver009)       ALPHA     #####################################################
###################################################################################################################


import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://web.whatsapp.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Connection": "keep-alive",
}
x=requests.get("https://web.whatsapp.com", auth=('user','pass'),headers=headers)
print(x.text)
print("whats next")
