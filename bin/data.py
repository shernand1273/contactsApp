import json
import popup

def getData():

    try:
        with open("../data/contacts.json","r") as read_File:
            read_File.seek(0)
            data = read_File.read()
            jsonData=json.loads(data)
        return jsonData

    except FileNotFoundError:
        ###if this error takes place, use a GUI window to inform the user that the file was not found
        popup.window("The data file could not be found, the application will close now.")


class Data():
    def __init__(self):
        self.contacts = getData()
        self.states=["AL","AK","AZ","AR","CA","CO","CT","DE","FL",
                    "GA","HI","ID","IL","IN","IA","KS","KY",
                    "LA","ME","MD","MA","MI","MN","MS","MO",
                    "MT","NE","NV","NH","NJ","NM","NY",
                    "NC","ND","OH","OK","OR","PA","RI","SC",
                    "SD","TN","TX","UT","VT","VA","WA","WV",
                    "WI","WY","AS","DC","FM","GU","MH","MP","PW","PR","VI"]

    def getContacts(self):
        return self.contacts

    def getStateList(self):
        return self.states

    def retrieveData(self):
        return self.contacts
