'''
Author: Nash Greenwood
Date: 10/14/2022

This script generates test records for the LPA_GSP_NONNBO table in the
lpa-manpower-db-dev server. Random values and inputs are used to
simulate an authentic record to allow testing for the frontend of
the LPA Manpower Application for the migration portion of the project.

'''

import random
from re import S
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
        if not 0 < recordAmount <= 50:
            print("Invalid range! Please enter amount (1-50)")
            return None
        return recordAmount
    except:
        print("Invalid input! Please enter an integer")
        return None


def writeFile(msg):
    try:
        with open('./nonNboInsert.txt', 'w') as f:
            f.write(msg)
    except FileNotFoundError:
        print("File Error - Unable to write")


def generateInsertValues():
    # random base product id list
    randomBaseProductId = ['32', '10', '47', '29', '40', '63', '8', '21']
    # random base product category
    randomBaseProduct = ['Pneu Massage', 'Pneu 2WP', 'Pneu 4WP',
                         'OM Cushion', 'Mech 2WP', 'Mech 4WP', 'Static Lumbar']
    # random phase
    randomProjectPhase = ['Phase 0', 'Phase 1', 'Phase 2',
                          'Phase 3', 'Phase 4', 'Phase 5', 'Prod Phase']
    # generate random SOP date
    start_dt = datetime.date(2023, 2, 1)
    end_dt = datetime.date(2025, 3, 1)
    time_between_dates = end_dt - start_dt
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_dt + datetime.timedelta(days=random_number_of_days)
    randmom_start_date = start_dt + \
        datetime.timedelta(days=random_number_of_days)

    # generate award confidence float
    confidence = round(random.random(), 2)

    # generate record Values Variables
    Status = 'Migrate'
    Project_Name = ''.join(random.choices(
        string.digits, k=9)) + '- Test-Record'
    LPA_Base_Product_ID = random.choice(randomBaseProductId)
    MigratedZOHOID = ''.join(random.choices(string.digits, k=20))
    Project_Owner = 'drew.detherage@leggett.com'
    Project_Created = 'No'
    EESupportNeeded = 'No'
    EEBaseProductID = 'NULL'
    DurationSupport = 'No'
    Start_Date = randmom_start_date
    SOPvalue = random_date
    Base_Product = random.choice(randomBaseProduct)
    Group_Name = 'Test Record'
    Project_Region = 'NA'
    Project_Branch = 'Test Record'
    Actual_Phase = random.choice(randomProjectPhase)
    Project_Number = ''.join(random.choices(string.digits, k=5))
    NBO_Number = '-'
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
    SubToggP0 = '1'
    SubToggP1 = '1'
    SubToggP2 = '1'
    SubToggP3 = '1'
    SubToggP4 = '1'
    SubToggP5 = '1'

    return Status, Project_Name, LPA_Base_Product_ID, MigratedZOHOID, Project_Owner, Project_Created, EESupportNeeded, EEBaseProductID, DurationSupport, Start_Date, SOPvalue, Base_Product, Group_Name, Project_Region, Project_Branch, Actual_Phase, Project_Number, NBO_Number, EngBaseWorkEffort, ProjectAdjFactor, MechPhase0Day, MechPhase1Day, MechPhase2Day, MechPhase3Day, MechPhase4Day, MechPhase5Day, HrsMechPhase0, HrsMechPhase1, HrsMechPhase2, HrsMechPhase3, HrsMechPhase4, HrsMechPhase5, HrsCadPhase0, HrsCadPhase1, HrsCadPhase2, HrsCadPhase3, HrsCadPhase4, HrsCadPhase5, HrsValidationPhase0, HrsValidationPhase1, HrsValidationPhase2, HrsValidationPhase3, HrsValidationPhase4, HrsValidationPhase5, HrsPrototypePhase0, HrsPrototypePhase1, HrsPrototypePhase2, HrsPrototypePhase3, HrsPrototypePhase4, HrsPrototypePhase5, AdjMechPhase0, AdjMechPhase1, AdjMechPhase2, AdjMechPhase3, AdjMechPhase4, AdjMechPhase5, AdjCadPhase0, AdjCadPhase1, AdjCadPhase2, AdjCadPhase3, AdjCadPhase4, AdjCadPhase5, AdjProtoPhase0, AdjProtoPhase1, AdjProtoPhase2, AdjProtoPhase3, AdjProtoPhase4, AdjProtoPhase5, AdjValPhase0, AdjValPhase1, AdjValPhase2, AdjValPhase3, AdjValPhase4, AdjValPhase5, SubToggP0, SubToggP1, SubToggP2, SubToggP3, SubToggP4, SubToggP5


def generateInsertQuery(recordAmount):
    # generate sql insert command
    sqlInsert = "INSERT INTO [dbo].[LPA_GSP_NONNBO] ([Status],[Project_Name],[LPA_Base_Product_ID],[MigratedZOHOID],[Project_Owner],[Project_Created],[EESupportNeeded],[EEBaseProductID],[DurationSupport],[Start_Date],[SOP],[Base_Product],[Group_Name],[Project_Region],[Project_Branch],[Actual_Phase],[Project_Number],[NBO_Number],[EngBaseWorkEffort],[ProjectAdjFactor],[MechPhase0Day],[MechPhase1Day],[MechPhase2Day],[MechPhase3Day],[MechPhase4Day],[MechPhase5Day],[HrsMechPhase0],[HrsMechPhase1],[HrsMechPhase2],[HrsMechPhase3],[HrsMechPhase4],[HrsMechPhase5],[HrsCadPhase0],[HrsCadPhase1],[HrsCadPhase2],[HrsCadPhase3],[HrsCadPhase4],[HrsCadPhase5],[HrsValidationPhase0],[HrsValidationPhase1],[HrsValidationPhase2],[HrsValidationPhase3],[HrsValidationPhase4],[HrsValidationPhase5],[HrsPrototypePhase0],[HrsPrototypePhase1],[HrsPrototypePhase2],[HrsPrototypePhase3],[HrsPrototypePhase4],[HrsPrototypePhase5],[AdjMechPhase0],[AdjMechPhase1],[AdjMechPhase2],[AdjMechPhase3],[AdjMechPhase4],[AdjMechPhase5],[AdjCadPhase0],[AdjCadPhase1],[AdjCadPhase2],[AdjCadPhase3],[AdjCadPhase4],[AdjCadPhase5],[AdjProtoPhase0],[AdjProtoPhase1],[AdjProtoPhase2],[AdjProtoPhase3],[AdjProtoPhase4],[AdjProtoPhase5],[AdjValPhase0],[AdjValPhase1],[AdjValPhase2],[AdjValPhase3],[AdjValPhase4],[AdjValPhase5],[SubToggP0],[SubToggP1],[SubToggP2],[SubToggP3],[SubToggP4],[SubToggP5])VALUES"

    recordValues = ""
    i = 0
    for i in range(recordAmount):
        values = generateInsertValues()

        Status, Project_Name, LPA_Base_Product_ID, MigratedZOHOID, Project_Owner, Project_Created, EESupportNeeded, EEBaseProductID, DurationSupport, Start_Date, SOPvalue, Base_Product, Group_Name, Project_Region, Project_Branch, Actual_Phase, Project_Number, NBO_Number, EngBaseWorkEffort, ProjectAdjFactor, MechPhase0Day, MechPhase1Day, MechPhase2Day, MechPhase3Day, MechPhase4Day, MechPhase5Day, HrsMechPhase0, HrsMechPhase1, HrsMechPhase2, HrsMechPhase3, HrsMechPhase4, HrsMechPhase5, HrsCadPhase0, HrsCadPhase1, HrsCadPhase2, HrsCadPhase3, HrsCadPhase4, HrsCadPhase5, HrsValidationPhase0, HrsValidationPhase1, HrsValidationPhase2, HrsValidationPhase3, HrsValidationPhase4, HrsValidationPhase5, HrsPrototypePhase0, HrsPrototypePhase1, HrsPrototypePhase2, HrsPrototypePhase3, HrsPrototypePhase4, HrsPrototypePhase5, AdjMechPhase0, AdjMechPhase1, AdjMechPhase2, AdjMechPhase3, AdjMechPhase4, AdjMechPhase5, AdjCadPhase0, AdjCadPhase1, AdjCadPhase2, AdjCadPhase3, AdjCadPhase4, AdjCadPhase5, AdjProtoPhase0, AdjProtoPhase1, AdjProtoPhase2, AdjProtoPhase3, AdjProtoPhase4, AdjProtoPhase5, AdjValPhase0, AdjValPhase1, AdjValPhase2, AdjValPhase3, AdjValPhase4, AdjValPhase5, SubToggP0, SubToggP1, SubToggP2, SubToggP3, SubToggP4, SubToggP5 = values

        sqlInsertValues = f"('{Status}','{Project_Name}',{LPA_Base_Product_ID},{MigratedZOHOID},'{Project_Owner}','{Project_Created}','{EESupportNeeded}',{EEBaseProductID},{DurationSupport},'{Start_Date}','{SOPvalue}','{Base_Product}','{Group_Name}','{Project_Region}','{Project_Branch}','{Actual_Phase}','{Project_Number}','{NBO_Number}',{EngBaseWorkEffort},{ProjectAdjFactor},{MechPhase0Day},{MechPhase1Day},{MechPhase2Day},{MechPhase3Day},{MechPhase4Day},{MechPhase5Day},{HrsMechPhase0},{HrsMechPhase1},{HrsMechPhase2},{HrsMechPhase3},{HrsMechPhase4},{HrsMechPhase5},{HrsCadPhase0},{HrsCadPhase1},{HrsCadPhase2},{HrsCadPhase3},{HrsCadPhase4},{HrsCadPhase5},{HrsValidationPhase0},{HrsValidationPhase1},{HrsValidationPhase2},{HrsValidationPhase3},{HrsValidationPhase4},{HrsValidationPhase5},{HrsPrototypePhase0},{HrsPrototypePhase1},{HrsPrototypePhase2},{HrsPrototypePhase3},{HrsPrototypePhase4},{HrsPrototypePhase5},{AdjMechPhase0},{AdjMechPhase1},{AdjMechPhase2},{AdjMechPhase3},{AdjMechPhase4},{AdjMechPhase5},{AdjCadPhase0},{AdjCadPhase1},{AdjCadPhase2},{AdjCadPhase3},{AdjCadPhase4},{AdjCadPhase5},{AdjProtoPhase0},{AdjProtoPhase1},{AdjProtoPhase2},{AdjProtoPhase3},{AdjProtoPhase4},{AdjProtoPhase5},{AdjValPhase0},{AdjValPhase1},{AdjValPhase2},{AdjValPhase3},{AdjValPhase4},{AdjValPhase5},{SubToggP0},{SubToggP1},{SubToggP2},{SubToggP3},{SubToggP4},{SubToggP5}),"

        # generate number of records
        recordValues += sqlInsertValues
        i += 1

    # trim comma from end of insert command
    recordValues = recordValues[:-1]
    # add ; to end of insert command
    recordValues += ';'
    return sqlInsert + recordValues


if __name__ == "__main__":
    main()
