#Steven Hernandez
#This application allows the user to create a contact list of people.  The user can add the person's information like email, phone, and addressself.
#The user can then see a list of contacts as well as retrieve information from the contacts listself.
#The data store for this application is a json file(contacts.json)

import json
import data
import re
from PyQt5 import QtCore, QtGui, QtWidgets


#this class will hold a list of all the QlineEdit fields in the add contact information section
class AddInformationFields():
    def __init__(self):
        self.list = []


    def setInputFieldOBJ(self,obj):
        self.list.append(obj)

    def getInputFieldOBJ(self):
        return self.list




inputFields = AddInformationFields()


class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setStyleSheet("background-color:#46484c")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ##########################Scroll Area####################################
        self.contactScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.contactScrollArea.setGeometry(QtCore.QRect(9, 80, 171, 511))
        self.contactScrollArea.setStyleSheet("background-color: (255, 255, 255)")
        self.contactScrollArea.setWidgetResizable(True)
        self.contactScrollArea.setObjectName("contactScrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QTextEdit()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 169, 509))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")#we are using this to add text to the scroll area
        self.scrollAreaWidgetContents.setStyleSheet("background-color:white")
        self.scrollAreaWidgetContents.setLineWrapColumnOrWidth(220)

        self.scrollAreaWidgetContents.setLineWrapMode(QtWidgets.QTextEdit.FixedPixelWidth)
        self.contactScrollArea.setWidget(self.scrollAreaWidgetContents)





        #########################################################################

        self.contactsHeader = QtWidgets.QLabel(self.centralwidget)
        self.contactsHeader.setGeometry(QtCore.QRect(-2, 0, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.contactsHeader.setFont(font)
        self.contactsHeader.setAutoFillBackground(False)
        self.contactsHeader.setStyleSheet("background-color: #42b6f4;\n"
"margin:5px")
        self.contactsHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.contactsHeader.setObjectName("contactsHeader")
        self.firstNameLbl = QtWidgets.QLabel(self.centralwidget)
        self.firstNameLbl.setGeometry(QtCore.QRect(210, 320, 31, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.firstNameLbl.setFont(font)
        self.firstNameLbl.setObjectName("firstNameLbl")
        self.firstNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.firstNameInput.setGeometry(QtCore.QRect(250, 320, 101, 21))
        self.firstNameInput.setText("")
        self.firstNameInput.setObjectName("firstNameInput")
        self.firstNameInput.setPlaceholderText("Required")
        inputFields.setInputFieldOBJ(self.firstNameInput) #adds first name QLineEdit field to the obj list
        self.lastNamelbl = QtWidgets.QLabel(self.centralwidget)
        self.lastNamelbl.setGeometry(QtCore.QRect(370, 320, 31, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lastNamelbl.setFont(font)
        self.lastNamelbl.setObjectName("lastNamelbl")
        self.lastNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.lastNameInput.setGeometry(QtCore.QRect(410, 320, 151, 21))
        self.lastNameInput.setText("")
        self.lastNameInput.setObjectName("lastNameInput")
        self.lastNameInput.setPlaceholderText("Required")
        inputFields.setInputFieldOBJ(self.lastNameInput)#adds the last name QLineEdit field to the obj list
        self.phoneLbl = QtWidgets.QLabel(self.centralwidget)
        self.phoneLbl.setGeometry(QtCore.QRect(210, 360, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.phoneLbl.setFont(font)
        self.phoneLbl.setObjectName("phoneLbl")
        self.emailLbl = QtWidgets.QLabel(self.centralwidget)
        self.emailLbl.setGeometry(QtCore.QRect(390, 360, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.emailLbl.setFont(font)
        self.emailLbl.setObjectName("emailLbl")
        self.phon3Input = QtWidgets.QLineEdit(self.centralwidget)
        self.phon3Input.setGeometry(QtCore.QRect(260, 360, 113, 21))
        self.phon3Input.setObjectName("phon3Input")
        self.phon3Input.setPlaceholderText("###-###-###")
        inputFields.setInputFieldOBJ(self.phon3Input) #adds the phone QLineEdit field to the obj list
        self.emailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.emailInput.setGeometry(QtCore.QRect(440, 360, 261, 21))
        self.emailInput.setText("")
        self.emailInput.setObjectName("emailInput")
        inputFields.setInputFieldOBJ(self.emailInput)#adds the email QLineEdit field to the obj list

        ########################BUttons in add Contact information label########
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(270, 550, 60, 25))
        self.addButton.setObjectName("addButton")
        self.addButton.setStyleSheet("background-color:#42b6f4;color:white;border-radius:3px;font-weight:bold")
        self.addButton.clicked.connect(lambda: self.addData(self.addButton))
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(200, 550, 60, 25))
        self.clearButton.setObjectName("clearButton")
        self.clearButton.setStyleSheet("background-color:#42b6f4;color:white;border-radius:3px;font-weight:bold")
        self.clearButton.clicked.connect(lambda: self.clearInputFields(inputFields.getInputFieldOBJ()))

        ########################################################################

        self.addressLbl = QtWidgets.QLabel(self.centralwidget)
        self.addressLbl.setGeometry(QtCore.QRect(210, 410, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.addressLbl.setFont(font)
        self.addressLbl.setObjectName("addressLbl")
        self.addContactLabel = QtWidgets.QLabel(self.centralwidget)
        self.addContactLabel.setGeometry(QtCore.QRect(190, 274, 611, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.addContactLabel.setFont(font)
        self.addContactLabel.setAutoFillBackground(False)
        self.addContactLabel.setStyleSheet("background-color: #42b6f4;\n"
"margin:5px")
        self.addContactLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.addContactLabel.setObjectName("addContactLabel")
        self.line1Lbl = QtWidgets.QLabel(self.centralwidget)
        self.line1Lbl.setGeometry(QtCore.QRect(280, 410, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line1Lbl.setFont(font)
        self.line1Lbl.setObjectName("line1Lbl")
        self.Line2Lbl = QtWidgets.QLabel(self.centralwidget)
        self.Line2Lbl.setGeometry(QtCore.QRect(280, 440, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Line2Lbl.setFont(font)
        self.Line2Lbl.setObjectName("Line2Lbl")
        self.addressLine1Input = QtWidgets.QLineEdit(self.centralwidget)
        self.addressLine1Input.setGeometry(QtCore.QRect(330, 410, 211, 21))
        self.addressLine1Input.setText("")
        self.addressLine1Input.setObjectName("addressLine1Input")
        inputFields.setInputFieldOBJ(self.addressLine1Input)#this adds the address line 1 QLineEdit field to the obj list
        self.addressLine2Input = QtWidgets.QLineEdit(self.centralwidget)
        self.addressLine2Input.setGeometry(QtCore.QRect(330, 440, 211, 21))
        self.addressLine2Input.setObjectName("addressLine2Input")
        inputFields.setInputFieldOBJ(self.addressLine2Input)#This adds the address line 2 QLineEdit field to the obj list
        self.cityInput = QtWidgets.QLineEdit(self.centralwidget)
        self.cityInput.setGeometry(QtCore.QRect(330, 470, 113, 21))
        self.cityInput.setText("")
        self.cityInput.setObjectName("cityInput")
        inputFields.setInputFieldOBJ(self.cityInput)#adds the city QLineEdit field to the obj list
        self.cityLbl = QtWidgets.QLabel(self.centralwidget)
        self.cityLbl.setGeometry(QtCore.QRect(280, 470, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cityLbl.setFont(font)
        self.cityLbl.setObjectName("cityLbl")
        self.stateLbl = QtWidgets.QLabel(self.centralwidget)
        self.stateLbl.setGeometry(QtCore.QRect(460, 470, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.stateLbl.setFont(font)
        self.stateLbl.setObjectName("stateLbl")
        self.zipLbl = QtWidgets.QLabel(self.centralwidget)
        self.zipLbl.setGeometry(QtCore.QRect(560, 470, 31, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.zipLbl.setFont(font)
        self.zipLbl.setObjectName("zipLbl")
        self.stateInput = QtWidgets.QLineEdit(self.centralwidget)
        self.stateInput.setGeometry(QtCore.QRect(500, 470, 41, 21))
        self.stateInput.setText("")
        self.stateInput.setObjectName("stateInput")
        inputFields.setInputFieldOBJ(self.stateInput)#This adds the state QLineEdit field to the obj list
        self.zipInput = QtWidgets.QLineEdit(self.centralwidget)
        self.zipInput.setGeometry(QtCore.QRect(590, 470, 61, 21))
        self.zipInput.setText("")
        self.zipInput.setObjectName("zipInput")
        inputFields.setInputFieldOBJ(self.zipInput)#This adds the zip QLineEdit field to the obj list
        self.contactInformationHeader = QtWidgets.QLabel(self.centralwidget)
        self.contactInformationHeader.setGeometry(QtCore.QRect(190, 0, 611, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.contactInformationHeader.setFont(font)
        self.contactInformationHeader.setAutoFillBackground(False)
        self.contactInformationHeader.setStyleSheet("background-color: #42b6f4;\n"
"margin:5px\n"
"")
        self.contactInformationHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.contactInformationHeader.setObjectName("contactInformationHeader")
        self.verticalDivider = QtWidgets.QFrame(self.centralwidget)
        self.verticalDivider.setGeometry(QtCore.QRect(180, 0, 20, 571))
        self.verticalDivider.setFrameShape(QtWidgets.QFrame.VLine)
        self.verticalDivider.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalDivider.setObjectName("verticalDivider")
        self.horizontalDivider = QtWidgets.QFrame(self.centralwidget)
        self.horizontalDivider.setGeometry(QtCore.QRect(197, 260, 601, 20))
        self.horizontalDivider.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontalDivider.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalDivider.setObjectName("horizontalDivider")
        self.informationViewFeedback = QtWidgets.QLabel(self.centralwidget)
        self.informationViewFeedback.setGeometry(QtCore.QRect(200, 210, 301, 31))
        self.informationViewFeedback.setStyleSheet("color: rgb(252, 1, 7)")
        self.informationViewFeedback.setObjectName("informationViewFeedback")
        self.informationNameLbl = QtWidgets.QLabel(self.centralwidget)
        self.informationNameLbl.setGeometry(QtCore.QRect(200, 80, 59, 16))
        self.informationNameLbl.setObjectName("informationNameLbl")
        self.informationPhoneLbl = QtWidgets.QLabel(self.centralwidget)
        self.informationPhoneLbl.setGeometry(QtCore.QRect(200, 100, 59, 16))
        self.informationPhoneLbl.setObjectName("informationPhoneLbl")
        self.informationEmailLbl = QtWidgets.QLabel(self.centralwidget)
        self.informationEmailLbl.setGeometry(QtCore.QRect(200, 120, 59, 16))
        self.informationEmailLbl.setObjectName("informationEmailLbl")
        self.showNameLbl = QtWidgets.QLabel(self.centralwidget)
        self.showNameLbl.setGeometry(QtCore.QRect(250, 80, 221, 16))
        self.showNameLbl.setObjectName("showNameLbl")
        self.showPhoneLbl = QtWidgets.QLabel(self.centralwidget)
        self.showPhoneLbl.setGeometry(QtCore.QRect(250, 100, 261, 16))
        self.showPhoneLbl.setObjectName("showPhoneLbl")
        self.showEmailLbl = QtWidgets.QLabel(self.centralwidget)
        self.showEmailLbl.setGeometry(QtCore.QRect(250, 120, 281, 16))
        self.showEmailLbl.setObjectName("showEmailLbl")
        self.addressInformationLbl = QtWidgets.QLabel(self.centralwidget)
        self.addressInformationLbl.setGeometry(QtCore.QRect(200, 160, 59, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.addressInformationLbl.setFont(font)
        self.addressInformationLbl.setObjectName("addressInformationLbl")
        self.showAddressLbl1 = QtWidgets.QLabel(self.centralwidget)
        self.showAddressLbl1.setGeometry(QtCore.QRect(270, 160, 271, 16))
        self.showAddressLbl1.setObjectName("showAddressLbl1")
        self.showAddressLbl2 = QtWidgets.QLabel(self.centralwidget)
        self.showAddressLbl2.setGeometry(QtCore.QRect(270, 180, 271, 16))
        self.showAddressLbl2.setObjectName("showAddressLbl2")
        self.showAddressLbl3 =QtWidgets.QLabel(self.centralwidget)
        self.showAddressLbl3.setGeometry(QtCore.QRect(270,200,271,16))
        self.showAddressLbl3.setObjectName("showAddressLbl3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(200, 40, 231, 33))
        self.widget.setObjectName("widget")
        self.contactInput = QtWidgets.QLineEdit(self.centralwidget)
        self.contactInput.setObjectName("contactInput")
        self.contactInput.setPlaceholderText("Enter contact name")
        self.contactInput.setGeometry(200,240,180,25)
        self.informationViewButton = QtWidgets.QPushButton(self.centralwidget)
        self.informationViewButton.setObjectName("informationViewButton")
        self.informationViewButton.setGeometry(390,240,60,25)
        self.informationViewButton.setStyleSheet("background-color:#42b6f4;color:white;border-radius:3px;font-weight:bold")
        self.informationViewButton.clicked.connect(lambda: self.view())
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionInformation = QtWidgets.QAction(MainWindow)
        self.actionInformation.setObjectName("actionInformation")
        self.addFeedbackLabel = QtWidgets.QLabel(self.centralwidget)
        self.addFeedbackLabel.setGeometry(200,525,550,20)
        self.addFeedbackLabel.setStyleSheet("color:white")
        self.totalContacts=QtWidgets.QLabel(self.centralwidget)
        self.totalContacts.setStyleSheet("color:white")
        self.totalContacts.setGeometry(10,50,160,20)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.updateScrollArea()#This will update the scroll area every time the applicatino is started


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My Contacts"))
        self.contactsHeader.setText(_translate("MainWindow", "Contacts"))
        self.firstNameLbl.setText(_translate("MainWindow", "First"))
        self.firstNameLbl.setStyleSheet("color:#d1d2d3")
        self.lastNamelbl.setText(_translate("MainWindow", "Last"))
        self.lastNamelbl.setStyleSheet("color:#d1d2d3")
        self.phoneLbl.setText(_translate("MainWindow", "Phone"))
        self.phoneLbl.setStyleSheet("color:#d1d2d3")
        self.emailLbl.setText(_translate("MainWindow", "E-mail"))
        self.emailLbl.setStyleSheet("color:#d1d2d3")
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.addressLbl.setText(_translate("MainWindow", "Address"))
        self.addressLbl.setStyleSheet("color:#d1d2d3")
        self.addContactLabel.setText(_translate("MainWindow", "Add Contact"))
        self.line1Lbl.setText(_translate("MainWindow", "Line 1"))
        self.line1Lbl.setStyleSheet("color:#d1d2d3")
        self.Line2Lbl.setText(_translate("MainWindow", "Line 2"))
        self.Line2Lbl.setStyleSheet("color:#d1d2d3")
        self.cityLbl.setText(_translate("MainWindow", "City"))
        self.cityLbl.setStyleSheet("color:#d1d2d3")
        self.stateLbl.setText(_translate("MainWindow", "State"))
        self.stateLbl.setStyleSheet("color:#d1d2d3")
        self.zipLbl.setText(_translate("MainWindow", "Zip"))
        self.zipLbl.setStyleSheet("color:#d1d2d3")
        self.contactInformationHeader.setText(_translate("MainWindow", "Contact Information"))
        self.informationNameLbl.setText(_translate("MainWindow", "Name"))
        self.informationNameLbl.setStyleSheet("color:white;font-weight:bold")
        self.informationPhoneLbl.setText(_translate("MainWindow", "Phone"))
        self.informationPhoneLbl.setStyleSheet("color:white;font-weight:bold")
        self.informationEmailLbl.setText(_translate("MainWindow", "E-mail"))
        self.informationEmailLbl.setStyleSheet("color:white;font-weight:bold")
        self.showNameLbl.setText(_translate("MainWindow", ""))
        self.showNameLbl.setStyleSheet("color:#20c41d")
        self.showPhoneLbl.setText(_translate("MainWindow", ""))
        self.showPhoneLbl.setStyleSheet("color:#20c41d")
        self.showEmailLbl.setText(_translate("MainWindow", ""))
        self.showEmailLbl.setStyleSheet("color:#20c41d")
        self.addressInformationLbl.setText(_translate("MainWindow", "Address"))
        self.addressInformationLbl.setStyleSheet("color:white")
        self.showAddressLbl1.setText(_translate("MainWindow", ""))
        self.showAddressLbl1.setStyleSheet("color:#20c41d")
        self.showAddressLbl2.setText(_translate("MainWindow", ""))
        self.showAddressLbl2.setStyleSheet("color:#20c41d")
        self.showAddressLbl3.setStyleSheet("color:#20c41d")
        self.contactInput.setText(_translate("MainWindow",""))
        self.informationViewButton.setText(_translate("MainWindow", "view"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionInformation.setText(_translate("MainWindow", "Information"))



    def addData(self,button):
        if(button.text()=="Add"):
            #we have to get all the values in the field, we also have to validate them
            #required fields are:first Name, last name, phone
            #the address is not required
            #get all the information from the field
            self.addressInputList=[]
            self.firstName = self.firstNameInput.text()
            self.lastName=self.lastNameInput.text()
            self.phone=self.phon3Input.text()
            self.email=self.emailInput.text()
            self.addressLine1 =self.addressLine1Input.text()
            self.addressLine2=self.addressLine2Input.text()
            self.city=self.cityInput.text()
            self.state=self.stateInput.text()
            self.zip=self.zipInput.text()
            #lets add all the address related values to a list because we will be using the list in another function
            self.addressInputList.append(self.addressLine1)
            self.addressInputList.append(self.addressLine2)
            self.addressInputList.append(self.city)
            self.addressInputList.append(self.state)
            self.addressInputList.append(self.zip)



            #Now that we have all the data from the fields, we have to validate every piece
            #once all the data is verified, we are going to build up a string and call a function to add the string to the json file
        if(self.valid(self.firstName,self.lastName,self.phone,self.email,self.addressLine1,self.addressLine2,self.city,self.state,self.zip,self.addressInputList)==True):


                #create the first part of the dictionary
            #dictionary ={"first":self.firstName.title(),"last":self.lastName.title(),"phone":self.phone,"email":self.email}
            #addressDictionary ={"streetLine1":self.addressLine1,"streetLine2":self.addressLine2,"city":self.city,"state":self.state,"zip":self.zip}
                #add the address dictionary to the first dictionary to complete the body of the json Data
            #dictionary["address"]=addressDictionary
            #objectName = self.firstName.title()+self.lastName.title()#this is the object name

            #first open and read the json file
            self.objectName = str(self.firstName.title()+self.lastName.title())

            with open("../data/contacts.json","r")as read_File:
                self.rawData = read_File.read()
                self.jsonData = json.loads(self.rawData)
                self.dictionary =self.jsonData


                self.dictionary[self.objectName]={"first":self.firstName.title(),
                                            "last":self.lastName.title(),
                                            "phone":self.phone,
                                            "email":self.email,
                                            "address":{
                                                    "line1":self.addressLine1,
                                                    "line2":self.addressLine2,
                                                    "city":self.city,
                                                    "state":self.state,
                                                    "zip":self.zip
                                                    }
                                            }


                #now that we have the data written, we need to pass it to json format
                self.writeData = json.dumps(self.dictionary)



                #open up the json file and write this data to the File
                self.w_file= open("../data/contacts.json","w+")
                self.w_file.write(self.writeData)
                self.updateLabel(self.addFeedbackLabel,"Contact Saved","valid")
                self.w_file.close()

                self.updateScrollArea()



    def clearInputFields(self,fieldData):
        #get the list of objects held in the inputFields class
        self.field = fieldData
        #loop through this object and clear all fields
        for fields in self.field:
            fields.clear()




    def valid(self,first,last,phone,email,addressLine1,addressLine2,city,state,zip,allAddressInputs):
        #first - holds the text in the first name line QLineEdit
        #last - holds the text in the last name QLineEdit field
        #phone- holds phone text from QLineEdit
        #email - pretty self explanatory at this point right? lol
        #allAddressInputs - this holds a list of all the text retrieved from the address fields, we are using This
        #list to iterate through and check if any input was entered.  Since the address fields are optional, they are not required
        #until the user enters something.  If the user enters something, then the information better damn well be valid.
        #for this function to work, we have to make sure the user entered the required fields first(first,last,phone)
        #email and address are optional, but if one field in the address is entered, then all are required and need to be valid
        self.isValid=False #this is the flag that will be returned
        self.addressEmpty=0#we are going to assume that the address field was not added by the user.  It will make more sense below

        #These are all the errors that can be sent to the updateLabel() to show the user what is going on, we are using that same function for feedback if all input is valid as well
        self.error1 ="Invalid: One or more required field is empty."
        self.error2 ="Invalid: Only letters allowed in name fields."
        self.error3 ="Invalid: The phone number entered is not valid, use the right format."
        self.error4 ="Invalid: Check your e-mail and make sure its correct."
        self.error5 ="Invalid: Missing a required address field."
        self.error6 ="Invalid: One or more address fields missing."
        #check that the required fields are entered
        if(len(first)==0 or len(last)==0 or len(phone)==0):
            #call the updateLabel() to let the user know the input is not valid
            self.updateLabel(self.addFeedbackLabel,self.error1,"error")
            return self.isValid

        #if all the required fields have something in them, then check all values to make sure they are valid.
        if(len(first)>0 and len(last)>0 and len(phone)>0):
            #regex used to check for the right phone pattern (###-###-####)-the placeholder in the phone QLineEdit shows the right format
            self.phonePattern = r"(\d\d\d[-]\d\d\d[-]\d\d\d\d)"

            #check that first name field is all letters
            if(first.isalpha()):
                #print("first Name passess")
                self.isValid=True
            else:
                #let user know there is an error
                self.updateLabel(self.addFeedbackLabel,self.error2,"error")
                self.isValid =False
                return self.isValid

            #check for all letters in the last name field
            if(last.isalpha()):
                #print("last name passess")
                self.isValid=True
            else:
                #let the user know there is an error
                self.updateLabel(self.addFeedbackLabel,self.error2,"error")
                self.isValid = False
                return self.isValid

            #user regular expression to test the number format and that it passess
            if(re.search(self.phonePattern,phone)):
                #print("Phone matches format")
                self.isValid = True
            else:
                #the user messed up, so we are going to let him know
                self.updateLabel(self.addFeedbackLabel,self.error3,"error")
                self.isValid=False
                return self.isValid

        #the email is not required, but if the user enters somethign in the email, we have to make sure the input is validated
        if(len(email)==0):
            email = "" # we are passing it None because Json will recognize it
        elif(len(email)>0):#if there is something in the email field, validate it using a regex
            self.emailPattern =r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
            if(re.search(self.emailPattern,email)):
                #print("The email is valid")
                self.isValid = True

            else:
                #let the user know that he needs to go back and check the email
                self.updateLabel(self.addFeedbackLabel,self.error4,"error")
                self.isValid = False
                return self.isValid

        #if the user enters something in the address QLineEdit line1, then everything has to check out
        #we are determining this by looping through the allAddressInputs list to check for anything that might have been filled out.  If anything
        #ended up being filled out, then the input is invalid because its either all or none for the address
        for addressField in allAddressInputs:
            if(len(addressField)>0):
                self.addressEmpty+=1

        if(self.addressEmpty!=0):
            #so if the user entered something, lets check the self.addressEmpty count to make sure that all fields were filled
            #keep in mind that line two is not a requirement, its just a second line the user can enter extra information such as apartment# or PO Box
            if(self.addressEmpty ==5):
                if(self.validateStateAndZip(state,zip)==True):
                    self.isValid=True
                    #print("Everything is good")
                else:
                    self.isValid=False

            elif(self.addressEmpty==4):
                #make sure that the only empty field remaining is line 2 (optional), otherwise spit out an error
                if(len(addressLine2)==0):

                    #proceed to validate all the data in a separate function
                    if(self.validateStateAndZip(state,zip))==True:
                        self.isValid=True
                        #print("Its all good baby")
                    else:
                        self.isValid=False

                else:
                    self.updateLabel(self.addFeedself,self.error5,"error")
                    self.isValid=False
                    return self.isValid
            else:
                self.updateLabel(self.addFeedbackLabel,self.error6,"error")
                self.isValid=False
                return self.isValid

        else:
            #print("all address fields are empty, cool")
            self.isValid=True
            #BECAUSE all the fields are empty, we are going through all the fields again and giving them a value of None
            for fields in allAddressInputs:
                fields = ""

        return self.isValid

    def updateLabel(self,theLabel,message,event):
        theLabel.setText(message)

        if(event =="error"):
            theLabel.setStyleSheet("color:#ed1a12;font:14pt")
        if(event=="valid"):
            theLabel.setStyleSheet("color:#20c41d;font:14pt")
        if(event=="notFound"):
            theLabel.setStyleSheet("color:white;font:14pt")

    def validateStateAndZip(self,theState,thezip):
        #create a state object taht calls the Data() class to retreive the state list
        states = data.Data()
        stateList= states.getStateList()
        stateValid = False
        zipValid = False


        #test the state to make sure its only 2 letters and nothing else
        if(len(theState)==2 and theState.isalpha()):
            stateValid =True

        else:
            self.updateLabel(self.addFeedbackLabel,"Invalid: Make sure the state is the abbreviation (example - vt or VT).","error")
            stateValid=False


        if(len(thezip)==5 and thezip.isdigit()):
            zipValid =True

        else:
            self.updateLabel(self.addFeedbackLabel,"Invalid: Make sure that you entered a five digit zip code","error")
            zipValid =False


        if(zipValid ==False or stateValid==False):
            return False

        elif(zipValid ==True and stateValid==True):
            return True

    #This fucntion is used to update the scroll area contets when the program first starts and when the program adds new data or removes it.
    def updateScrollArea(self):
        self.updatedData = data.Data()
        self.updatedContacts = self.updatedData.getContacts()
        self.allContacts = self.updatedContacts.keys()
        self.outString=""
        self.obj = ""
        self.first=""
        self.last=""
        self.count=0

        for contacts in self.allContacts:
            self.count = self.count +1
            self.obj = self.updatedContacts[contacts]
            self.first = self.obj["first"]
            self.last = self.obj["last"]
            self.outString+= "{}. {} {}\n".format(self.count,self.first,self.last)
            self.scrollAreaWidgetContents.setText(self.outString)

        self.totalContacts.setText("Total Contacts: "+str(self.count))


    def view(self):
        self.regexPattern =r"(\w+\s{1}\w+)"
        self.objName = self.contactInput.text()

        if(len(self.objName)==0):
            self.updateLabel(self.informationViewFeedback,"Name field is empty.","error")

        else:
            #use a regular expression to check for the name pattern
            if(re.search(self.regexPattern,self.objName)):
                #split the string to count how many words in it, the regex tests against the pattern, but the test case is still true if the user enters another space and word(ie name lastname extraWord)
                self.nameString = self.objName.split()
                #check the length of the name string, if it is equal to 2, then the test fully passess
                if(len(self.nameString)==2):
                    #lets combine both strings into one because our object names do not have spaces between them

                    self.f=self.nameString[0]
                    self.l=self.nameString[1]
                    #capitalize the first letter of both strings before combining them
                    self.displayName=self.f+" "+self.l
                    self.objName = self.f.title()+self.l.title()
                    self.informationViewFeedback.setText("")
                    #use another function to find the object and show the information to the user
                    self.showInfo(self.objName,self.displayName)
                else:
                    self.updateLabel(self.informationViewFeedback,"Invalid: Too many values entered","error")
            #if its not in the kesy, updateLabel() to tell the user that the name was not found

            else:
                self.updateLabel(self.informationViewFeedback,"Invalid: enter first and last name.","error")

    #this function will find the object in the json file and retrieve the data to display it
    def showInfo(self, theKey,theName):
            #get the data keys from the json file
        self.tempData = data.Data()
        self.tempData = self.tempData.getContacts()
        self.dictKeys = self.tempData.keys()
        print(self.dictKeys)

        if (theKey in self.dictKeys):
            #if the name was fond, get the dictionary for it
            self.tempData =self.tempData[theKey]
            #get the first name
            self.fst = self.tempData["first"]
            #get the last name
            self.lst = self.tempData["last"]
            #get the phone
            self.ph = self.tempData["phone"]
            #get the email
            self.eml = self.tempData["email"]
            #get the address dictionary
            self.addressDict = self.tempData["address"]
            #get line1
            self.l1 = self.addressDict["line1"]
            #get line2
            self.l2 = self.addressDict["line2"]
            #get city
            self.cty = self.addressDict["city"]
            #get state
            self.stt = self.addressDict["state"]
            #get zip
            self.zp = self.addressDict["zip"]

            #start updating the labels with the information
            self.showNameLbl.setText(theName.title())
            self.showPhoneLbl.setText(self.ph)

            #chec to see if the email is empty, if it is set the value to n/a
            if(len(self.eml)==0):
                self.showEmailLbl.setText("n/a")
            else:
                self.showEmailLbl.setText(self.eml)

            #check that the first address line is empty, if it is, then we just update the address label with n/a

            if(len(self.l1)==0):
                print("No address Provided")
                self.showAddressLbl1.setText("n/a")

                #check if line 2 is empty or not (line2 is not required when entering an address)
            else:
                #there must be something in line1, so we are checking line 2 since its not necessary
                if(len(self.l2)==0):
                    #build the address display without line 2
                    self.showAddressLbl1.setText(self.l1)
                    self.showAddressLbl2.setText("{}, {} {}".format(self.cty.title(),self.stt.upper(),self.zp))

                else:
                    #build the address label with everything
                    self.showAddressLbl1.setText(self.l1)
                    self.showAddressLbl2.setText(self.l2)
                    self.showAddressLbl3.setText("{}, {} {}".format(self.cty.title(),self.stt.upper(),self.zp))







        elif(theKey not in self.dictKeys):
            self.updateLabel(self.informationViewFeedback,"{} was not found in your contacts.".format(theName),"error")








    #create a button "view in map/ the symbolfor map" and a button to "edit/ the ... vertical simbol" the contact


def main():

    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

main()

#to do

#-button click event when the user pressess a button
#-split up the object names so that there is a space between the first and last name in the scroll area
