# AIR_PORT_SCENARIO.PY

print("~~~~~~~~~~~~~~~~~~~~~~~~~welcome to chennai international airport~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

gatepass_checking=input("verifing gatepass_checking:").lower().strip()
if gatepass_checking=="verified" or gatepass_checking=="not verified":
    if gatepass_checking=="verified":
        print("you are verified and please go to both 2 and checking for RTPCR")
        print("~~~~~~~~~~RTPCR_checking~~~~~~~~~~~")
    elif gatepass_checking=="not verified":
        print("you are not verified")
else:
    print("you are not verified")

RTPCR_checking=input("sample taken for RTPCR_checking:").lower().strip()
if RTPCR_checking=="negative" or RTPCR_checking=="":
    if RTPCR_checking=="negative":
        print("you are eligible, you can go for id proof checking")
    elif RTPCR_checking=="positive":
        print("you are tested positive so, you are not eligible")
else:
    print("you are tested positive so, you are not eligible")

print("~~~~~~~i'd proof checking~~~~~~~~")

passenger_id_proof_checking=input("show your i'd_proof:").lower().strip()
if passenger_id_proof_checking== "yes this is my proof" or passenger_id_proof_checking=="i forget to kept it at my home":
    if passenger_id_proof_checking== "yes this is my proof":
        print("your i'd proof has been verified")
        print("you can go now lagguage weiging check")
    elif passenger_id_proof_checking=="i forget to kept it at my home":
        print("sorry you has been not allowed")
else:
    print("sorry you has been not allowed")

lagguage_check=input("placed your lagguge in weighing machine:").lower().strip()
if lagguage_check<="20" or lagguage_check>="20":
    if lagguage_check<="20":
        print("your weight is perfect")
        print("you can go immegration procees now")
    elif lagguage_check>="20":
        print("your weight is above 20 kg's ")
        print("please pay each kg's 2000 rupees above 20 kg's")
else:
    print("sorry you are not complete previous process")
    
immegration_process=input("show your passport:").lower().strip()
ticket=input("your ticket please:").lower().strip()
visa=input("your visa:").lower().strip()
question=input("why should you go for canada?").lower().strip()
if immegration_process=="yes this is my passport" and ticket=="yes this is my ticket" and visa=="yes this is my visa" and question=="for my job":
    print("your immegration process has been verified")
    print("you can get boarding pass")
    
else:
    print("sorry your immegration process has not been done")

boarding_pass=input("ticket please:").lower().strip()
if boarding_pass=="yes this is my ticket" or boarding_pass=="sorry i have lost my tickets":
    if boarding_pass=="yes this is my ticket":
        print("yes you can board now!")
        print("~~~~~~~~~please consider our annoucement~~~~~~")
    elif boarding_pass=="sorry i have lost my tickets":
        print("sorry if you have not tickets , you will be not flied")
else:
    print("sorry you are not complete previous process")

boarding=input("please welcome show your boarding pass:").lower().strip()
if boarding=="yeah sure" or boarding=="iam sorry i lost my boarding pass":
    if boarding=="yeah sure":
        print("welcome to CANADIAN AIRWAYS")
        print("your seat is apart from business class ,THE SEAT NUMBER 24 , WINDOW SEATS ")
        print("THANK YOU FOR CHOOSING OUR AIRLINE")
    elif boarding=="iam sorry i lost my boarding pass":
        print("sorry sir,you have no boarding pass you cant fly our airline ")
else:
    print("sorry sir,you have no boarding pass you cant fly our airline ")

safe_journey=input("!!!!!!!!!!!!!!!HAVE A SAFE JOURNEY!!!!!!!!!!!!!!!!")


