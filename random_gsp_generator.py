'''
Author: Nash Greenwood
Date: 10/4/2022

This script generates test records for the LPA_GSP table in the
lpa-manpower-db-dev server. Random values and inputs are used to
simulate an authentic record to allow testing for the frontend of
the LPA Manpower Application.

'''

import random
import string
import datetime


def main():
    while True:
        recordAmount = prompt(
            input("How many GSP Test Records would you like to create?\n >: "))
        if recordAmount:
            break
    msg = generateInsertQuery(recordAmount)
    writeFile(msg)


def prompt(message):
    try:
        recordAmount = int(message)
        if not 0 < recordAmount < 50:
            print("Invalid range! Please enter amount (1-50)")
            return None
        return recordAmount
    except:
        print("Invalid input! Please enter an integer")
        return None


def writeFile(msg):
    try:
        with open('./sqlInsert.txt', 'w') as f:
            f.write(msg)
    except FileNotFoundError:
        print("File Error - Unable to write")


def generateInsertValues():
    # random base product list
    randomBaseProduct = ['32', '10', '47', '29', '40', '63', '8', '21']
    # generate random SOP date
    start_dt = datetime.date(2023, 2, 1)
    end_dt = datetime.date(2025, 3, 1)
    time_between_dates = end_dt - start_dt
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_dt + datetime.timedelta(days=random_number_of_days)
    # generate award confidence float
    confidence = random.random()
    # generate record Values Variables
    Status = 'New'
    NBO_Number = 'NBO-'+''.join(random.choices(string.ascii_uppercase +
                                               string.digits, k=5))
    LPA_Base_Product_ID = random.choice(randomBaseProduct)
    Project_Owner = 'Null'
    Project_Created = 'No'
    EESupportNeeded = 'No'
    EEBaseProductID = 'Null'
    DurationSupport = 'No'
    Program = 'Test Record'
    Production_Brand = 'Test Record'
    Product_Line = 'Test Record'
    Customer_Name = 'Test Record'
    Start_Date = 'Null'
    SOPvalue = random_date
    COPvalue = 'No'
    Base_Product = 'Test Record'
    OEM_Engineering_Region = 'Test Record'
    Support_Needed = 'No support required'
    EOPvalue = '0.50'
    Award_Confidence = confidence
    Product_Line_Group = 'Test Record'
    EngBaseWorkEffort = confidence
    ProjectAdjFactor = '1.00'
    MechPhase0Day = '33'
    MechPhase1Day = '32'
    MechPhase2Day = '152'
    MechPhase3Day = '219'
    MechPhase4Day = '241'
    MechPhase5Day = '73'
    HrsMechPhase0 = '7'
    HrsMechPhase1 = '14'
    HrsMechPhase2 = '176'
    HrsMechPhase3 = '188'
    HrsMechPhase4 = '137'
    HrsMechPhase5 = '17'
    HrsCadPhase0 = '15'
    HrsCadPhase1 = '15'
    HrsCadPhase2 = '117'
    HrsCadPhase3 = '102'
    HrsCadPhase4 = '29'
    HrsCadPhase5 = '15'
    HrsValidationPhase0 = '0'
    HrsValidationPhase1 = '8'
    HrsValidationPhase2 = '65'
    HrsValidationPhase3 = '16'
    HrsValidationPhase4 = '65'
    HrsValidationPhase5 = '8'
    HrsPrototypePhase0 = '10'
    HrsPrototypePhase1 = '41'
    HrsPrototypePhase2 = '81'
    HrsPrototypePhase3 = '61'
    HrsPrototypePhase4 = '10'
    HrsPrototypePhase5 = '0'
    AdjMechPhase0 = '1'
    AdjMechPhase1 = '1'
    AdjMechPhase2 = '1'
    AdjMechPhase3 = '1'
    AdjMechPhase4 = '1'
    AdjMechPhase5 = '1'
    AdjCadPhase0 = '1'
    AdjCadPhase1 = '1'
    AdjCadPhase2 = '1'
    AdjCadPhase3 = '1'
    AdjCadPhase4 = '1'
    AdjCadPhase5 = '1'
    AdjProtoPhase0 = '1'
    AdjProtoPhase1 = '1'
    AdjProtoPhase2 = '1'
    AdjProtoPhase3 = '1'
    AdjProtoPhase4 = '1'
    AdjProtoPhase5 = '1'
    AdjValPhase0 = '1'
    AdjValPhase1 = '1'
    AdjValPhase2 = '1'
    AdjValPhase3 = '1'
    AdjValPhase4 = '1'
    AdjValPhase5 = '1'
    UpdatedDateTime = 'Null'

    return Status, NBO_Number, LPA_Base_Product_ID, Project_Owner, Project_Created, EESupportNeeded, EEBaseProductID, DurationSupport, Program, Production_Brand, Product_Line, Customer_Name, Start_Date, SOPvalue, COPvalue, Base_Product, OEM_Engineering_Region, Support_Needed, EOPvalue, Award_Confidence, Product_Line_Group, EngBaseWorkEffort, ProjectAdjFactor, MechPhase0Day, MechPhase1Day, MechPhase2Day, MechPhase3Day, MechPhase4Day, MechPhase5Day, HrsMechPhase0, HrsMechPhase1, HrsMechPhase2, HrsMechPhase3, HrsMechPhase4, HrsMechPhase5, HrsCadPhase0, HrsCadPhase1, HrsCadPhase2, HrsCadPhase3, HrsCadPhase4, HrsCadPhase5, HrsValidationPhase0, HrsValidationPhase1, HrsValidationPhase2, HrsValidationPhase3, HrsValidationPhase4, HrsValidationPhase5, HrsPrototypePhase0, HrsPrototypePhase1, HrsPrototypePhase2, HrsPrototypePhase3, HrsPrototypePhase4, HrsPrototypePhase5, AdjMechPhase0, AdjMechPhase1, AdjMechPhase2, AdjMechPhase3, AdjMechPhase4, AdjMechPhase5, AdjCadPhase0, AdjCadPhase1, AdjCadPhase2, AdjCadPhase3, AdjCadPhase4, AdjCadPhase5, AdjProtoPhase0, AdjProtoPhase1, AdjProtoPhase2, AdjProtoPhase3, AdjProtoPhase4, AdjProtoPhase5, AdjValPhase0, AdjValPhase1, AdjValPhase2, AdjValPhase3, AdjValPhase4, AdjValPhase5, UpdatedDateTime


def generateInsertQuery(recordAmount):
    # generate sql insert command
    sqlInsert = "INSERT INTO lpa-manpower-db-dev.LPA_GSP (Status,NBO_Number,LPA_Base_Product_ID,Project_Owner,Project_Created,EESupportNeeded,EEBaseProductID,DurationSupport,Program,Production_Brand,Product_Line,Customer_Name,Start_Date,SOP,COP,Base_Product,OEM_Engineering_Region,Support_Needed,EOP,Award_Confidence,Product_Line_Group,EngBaseWorkEffort,ProjectAdjFactor,MechPhase0Day,MechPhase1Day,MechPhase2Day,MechPhase3Day,MechPhase4Day,MechPhase5Day,HrsMechPhase0,HrsMechPhase1,HrsMechPhase2,HrsMechPhase3,HrsMechPhase4,HrsMechPhase5,HrsCadPhase0,HrsCadPhase1,HrsCadPhase2,HrsCadPhase3,HrsCadPhase4,HrsCadPhase5,HrsValidationPhase0,HrsValidationPhase1,HrsValidationPhase2,HrsValidationPhase3,HrsValidationPhase4,HrsValidationPhase5,HrsPrototypePhase0,HrsPrototypePhase1,HrsPrototypePhase2,HrsPrototypePhase3,HrsPrototypePhase4,HrsPrototypePhase5,AdjMechPhase0,AdjMechPhase1,AdjMechPhase2,AdjMechPhase3,AdjMechPhase4,AdjMechPhase5,AdjCadPhase0,AdjCadPhase1,AdjCadPhase2,AdjCadPhase3,AdjCadPhase4,AdjCadPhase5,AdjProtoPhase0,AdjProtoPhase1,AdjProtoPhase2,AdjProtoPhase3,AdjProtoPhase4,AdjProtoPhase5,AdjValPhase0,AdjValPhase1,AdjValPhase2,AdjValPhase3,AdjValPhase4,AdjValPhase5,UpdatedDateTime,)VALUES"

    recordValues = ""
    i = 0
    for i in range(recordAmount):
        values = generateInsertValues()

        Status, NBO_Number, LPA_Base_Product_ID, Project_Owner, Project_Created, EESupportNeeded, EEBaseProductID, DurationSupport, Program, Production_Brand, Product_Line, Customer_Name, Start_Date, SOPvalue, COPvalue, Base_Product, OEM_Engineering_Region, Support_Needed, EOPvalue, Award_Confidence, Product_Line_Group, EngBaseWorkEffort, ProjectAdjFactor, MechPhase0Day, MechPhase1Day, MechPhase2Day, MechPhase3Day, MechPhase4Day, MechPhase5Day, HrsMechPhase0, HrsMechPhase1, HrsMechPhase2, HrsMechPhase3, HrsMechPhase4, HrsMechPhase5, HrsCadPhase0, HrsCadPhase1, HrsCadPhase2, HrsCadPhase3, HrsCadPhase4, HrsCadPhase5, HrsValidationPhase0, HrsValidationPhase1, HrsValidationPhase2, HrsValidationPhase3, HrsValidationPhase4, HrsValidationPhase5, HrsPrototypePhase0, HrsPrototypePhase1, HrsPrototypePhase2, HrsPrototypePhase3, HrsPrototypePhase4, HrsPrototypePhase5, AdjMechPhase0, AdjMechPhase1, AdjMechPhase2, AdjMechPhase3, AdjMechPhase4, AdjMechPhase5, AdjCadPhase0, AdjCadPhase1, AdjCadPhase2, AdjCadPhase3, AdjCadPhase4, AdjCadPhase5, AdjProtoPhase0, AdjProtoPhase1, AdjProtoPhase2, AdjProtoPhase3, AdjProtoPhase4, AdjProtoPhase5, AdjValPhase0, AdjValPhase1, AdjValPhase2, AdjValPhase3, AdjValPhase4, AdjValPhase5, UpdatedDateTime = values

        sqlInserValues = f'({Status},{NBO_Number},{LPA_Base_Product_ID},{Project_Owner},{Project_Created},{EESupportNeeded},{EEBaseProductID},{DurationSupport},{Program},{Production_Brand},{Product_Line},{Customer_Name},{Start_Date},{SOPvalue},{COPvalue},{Base_Product},{OEM_Engineering_Region},{Support_Needed},{EOPvalue},{Award_Confidence},{Product_Line_Group},{EngBaseWorkEffort},{ProjectAdjFactor},{MechPhase0Day},{MechPhase1Day},{MechPhase2Day},{MechPhase3Day},{MechPhase4Day},{MechPhase5Day},{HrsMechPhase0},{HrsMechPhase1},{HrsMechPhase2},{HrsMechPhase3},{HrsMechPhase4},{HrsMechPhase5},{HrsCadPhase0},{HrsCadPhase1},{HrsCadPhase2},{HrsCadPhase3},{HrsCadPhase4},{HrsCadPhase5},{HrsValidationPhase0},{HrsValidationPhase1},{HrsValidationPhase2},{HrsValidationPhase3},{HrsValidationPhase4},{HrsValidationPhase5},{HrsPrototypePhase0},{HrsPrototypePhase1},{HrsPrototypePhase2},{HrsPrototypePhase3},{HrsPrototypePhase4},{HrsPrototypePhase5},{AdjMechPhase0},{AdjMechPhase1},{AdjMechPhase2},{AdjMechPhase3},{AdjMechPhase4},{AdjMechPhase5},{AdjCadPhase0},{AdjCadPhase1},{AdjCadPhase2},{AdjCadPhase3},{AdjCadPhase4},{AdjCadPhase5},{AdjProtoPhase0},{AdjProtoPhase1},{AdjProtoPhase2},{AdjProtoPhase3},{AdjProtoPhase4},{AdjProtoPhase5},{AdjValPhase0},{AdjValPhase1},{AdjValPhase2},{AdjValPhase3},{AdjValPhase4},{AdjValPhase5},{UpdatedDateTime}),'

        # generate number of records
        recordValues += sqlInserValues
        i += 1

    # trim comma from end of insert command
    recordValues = recordValues[:-1]
    # add ; to end of insert command
    recordValues += ';'
    return sqlInsert + recordValues


main()
