# Necessary Imports
import json

def main():
    # Create an empty array that will eventually be filled with all the alert infromation
    # Also create an array of all the valid alert types
    arrayOfAlerts = []
    validAlertTypes = ["Weather", "Shooter", "Amber Alert", "Other"]

    # Create an infinite loop that will eventually
    # populate the json dictionary
    while True:
        # Create a dictionary that will store specific alert infromation
        alertDictionary = {}

        # Have the user initialize the type of alert they are generating
        # If the type of alert is not valid, have the loop skip this 
        alertType = input("Please enter a valid alert type: ")
        if (alertType not in validAlertTypes):
            ("The alert type you entered is invalid, please try again")
            continue
        alertDescription['Type'] = alertType

        # Have the user create a description to go along with alert message
        alertDescription = input("Please enter a description to go along with your alert:\n")
        alertDictionary['Description'] = alertDictionary

        # Once all the infromation is collected, add the completed alert to the alert array
        arrayOfAlerts.append(alertDictionary)

        # Check to see if the user would like to continue generating alerts
        doNotAcceptMoreAlerts = input("Would you like to generate another alert? (yes or no)\n").lower
        if (doNotAcceptMoreAlerts is not "yes"):
            break

    # Once all the alerts are completed, add the array to a general json dictionary
    jsonDictionary = {'alerts' : arrayOfAlerts}

    with open("/var/www/html/TestAlert.json", "w") as outfile:
        json.dump(jsonDictionary, outfile)

if __name__ == "__main__":
    main()