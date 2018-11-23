import os

def check_ping():
    hostname = "8.8.8.8"
    response = os.system("ping " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = True
    else:
        pingstatus = False

    return pingstatus

pingstatus = check_ping()

print(pingstatus)


