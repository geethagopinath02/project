changingParam = ['Gender','Breathing_Problem','Chest_Tightness','Cough','Allergy','Wheezing','Sleeping_Problem']
changingValues = [['Female','Male'],['No','Yes'],['No','Yes'],['No','Yes'],['No','Yes'],['No','Yes'],['No','Yes']]


def generateProfile(data):
    Person_Profile = []
    for x in data:
        if x in changingParam:
            X_index = changingParam.index(x)
            newStrings = x.replace('_'," ") + '  :  ' + changingValues[X_index][int(data[x])]
        else:
            newStrings = x.replace('_'," ") + '  :  ' + data[x]
        Person_Profile.append(newStrings)
    print(Person_Profile)
    return Person_Profile

def generateOutput(prediction):
    choice = ['The person does not have Asthma','The person does have Asthma']
    
    return choice[prediction]