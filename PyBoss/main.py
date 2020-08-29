# import and path the csv
import os
import csv
path = os.path.join("resources", "employee_data.csv")

# reading csv file
with open(path, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # declare the columns for new csv as list
    emp_id = []
    f_name = []
    l_name = []
    dob = []
    ssn = []
    state = []

    # US State abbreviation dictionary (copied from github)
    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }

    # skip the header line
    next(csvreader)

    # loop the csv
    for row in csvreader:

        # adding employee id
        emp_id.append(row[0])
        
        # splitting name into first and last name
        split_name = row[1].split(" ")
        f_name.append(split_name[0])
        l_name.append(split_name[1])
        
        # reformatting the dob into mm/dd/yyyy
        split_dob = row[2].split("-")
        new_dob_str = f'{split_dob[1]}/{split_dob[2]}/{split_dob[0]}'
        dob.append(new_dob_str)

        # grabbing last 4 digit of ssn only
        split_ssn = row[3].split("-")
        new_ssn_str = f'***-**-{split_ssn[2]}'
        ssn.append(new_ssn_str)

        # changing state into abbreviation format
        state.append(us_state_abbrev[row[4]])

# zip the created list to export as csv
newcsv = zip(emp_id, f_name, l_name, dob, ssn, state)

# export as text
outpath = os.path.join("analysis", "updated_employee_data.csv")
with open(outpath, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    writer.writerows(newcsv)