import openpyxl
import os
import datetime


dir_path = r"template"

# file_name = r"Vessel's Daily Report.xlsx" # r"VDR Template - BLANK.xlsx"
file_name = r"VDR Template - BLANK.xlsx"



xlsx_file = os.path.join(dir_path,file_name)
wb_obj = openpyxl.load_workbook(xlsx_file)

# Read the active sheet:
sheet = wb_obj.worksheets[0]


vdr_mapping = {
        "Vessel":"B4",
        "Date":"B5",
        "Current Location":"B6",
        "Next location":"B7",
        "Time":"D5",
        "ETA":"D7",
        "Draft (Fwd/Aft)":"F6",
        "Dist to Go":"F7",

        "Wind/Speed":"B9",
        "Ship's Speed":"B10",
        "Dist. Run 24 Hrs":"D9",
        "Avg Speed 24-hrs":"D10",
        "Sea / Swell":"F9",
        "Visibilty":"F10",

        "FO 1S":"B14",
        "FO 1P":"B15",
        "FO 2S":"B16",
        "FO 2P":"B17",
        "FO 2C":"B18",
        "FO 3S":"B19",
        "FO 3P":"B20",
        "FO 4S":"B21",
        "FO 4P":"B22",
        "FO 4C":"B23",
        "FO 5C":"B24",

}

sample_ship = {
        "Vessel":"DeathStar",
        "Current Location":"Singapore",
        "Next location":"London",
        "ETA":"01/01/22",
        "Draft (Fwd/Aft)":"4.70M / 4.60M",
        "Dist to Go":"5863 NM",

        "Wind/Speed":"NE / 07-10 KTS",
        "Ship's Speed":"Faster than light speed",
        "Dist. Run 24 Hrs":"0",
        "Avg Speed 24-hrs":"0",
        "Sea / Swell":"SLIGHT/ 1.0-1.5 m",
        "Visibilty":"7 NM",

        "FO 1S":"0",
        "FO 1P":"0",
        "FO 2S":"0",
        "FO 2P":"0",
        "FO 2C":"0",
        "FO 3S":"0",
        "FO 3P":"0",
        "FO 4S":"0",
        "FO 4P":"0",
        "FO 4C":"0",
        "FO 5C":"0",

}

auto_update_headers = ["Date","Time"]

def update_autofill():
        #Time
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        change_val("Time",current_time)

        #Date
        current_date = now.strftime("%d/%m/%Y")
        change_val("Date",current_date)

def change_val(header,value):
        location = get_vdr_mapping(header)
        sheet[location] = value

def get_vdr_mapping(header):
        return vdr_mapping[header]

for key,value in sample_ship.items():
        change_val(key,value)

update_autofill()


wb_obj.save(filename = 'sample_book.xlsx')



# class Daily_report():
#     def __init__(self):
#
#         self.info = {}
#
#         self.info["Vessel"]
#         self.info["Date"]
#         self.info["Current Location"]
#         self.info["Next location"]
#         self.info["Time"]
#         self.info["ETA"]
#         self.info["Draft (Fwd/Aft)"]
#         self.info["Dist to Go"]
#
#
#         self.info["Wind/Speed"]
#         self.info["Ship's Speed"]
#         self.info["Dist. Run 24 Hrs"]
#         self.info["Avg Speed 24-hrs"]
#         self.info["Sea / Swell"]
#         self.info["Visibilty"]
#
#         self.ship_rob = {}
#
#         self.ship_rob["FO 1S"]
#         self.ship_rob["FO 1P"]
#         self.ship_rob["FO 2S"]
#         self.ship_rob["FO 2P"]
#         self.ship_rob["FO 2C"]
#         self.ship_rob["FO 3S"]
#         self.ship_rob["FO 3P"]
#         self.ship_rob["FO 4S"]
#         self.ship_rob["FO 4P"]
#         self.ship_rob["FO 4C"]
#         self.ship_rob["FO 5C"]
#         self.ship_rob["Day Tank S"]
#         self.ship_rob["Day Tank P"]
#         self.ship_rob["Settling Tank"]
#         self.ship_rob["POT WATER"]
#         self.ship_rob["DRILL WATER"]
#         self.ship_rob["LO (ME)"]
#         self.ship_rob["LO (AE & E'cy Gen)"]
#         self.ship_rob["LO (Air Compressor)"]
#         self.ship_rob["LO (AC Compressor)"]
#         self.ship_rob["HO (St.Gear)"]
#         self.ship_rob["GO"]
#
#         self.fuel_oil_meter_reading = {}
#
#         self.fuel_oil_meter_reading["Port/Stbd : - Inlet"] = {}
#         self.fuel_oil_meter_reading["Port / Stbd - Outlet"] = {}
#
#         self.fuel_oil_meter_reading["Port/Stbd : - Inlet"] = {
#             "Reading at 0000hrs": ,
#             "Reading at 2400hrs": ,
#             "Consumption":
#         }
#
#         self.fuel_oil_meter_reading["Port / Stbd - Outlet"] = {
#             "Reading at 0000hrs": ,
#             "Reading at 2400hrs": ,
#             "Consumption":
#         }
#
#
#
# class Ship_info():
#     def __init__(self, this_vessel_name):
#         self.vessel_name = this_vessel_name
#         self.daily_reports = []
#
#
#     def add_daily_report(self, todays_report):
#
#         self.daily_reports.append(todays_report)
#




