# WEEK1
# Assignment
# A Banks swift code consist of 11 character as for example: ICICINMY111
# first 4 character represents bank
# next 2 character represents country
# next 2 character represents location
# next 3 character represents branch code
# Create a program to separate our these value to find out the bank name, country name, location name?
# For Assistance: Create an inventory(using any Python data structure of your choice) of Banks, countries and
# locations as required for the above problem (edited)

from pip._vendor.distlib.compat import raw_input


def extract_details(code):
    """
    function to extract bank name, country, location & branch codes
    :param code: swift code
    :return:
    """
    print("Bank Name: {}".format(banks[code[:4]]))
    print("Country: {}".format(countries[code[4:6]]))
    print("Location: {}".format(locations[code[6:8]]))
    print("Branch: {}".format(branches[code[8:11]]))


if __name__ == "__main__":
    # create a dictionary for banks
    banks = {"SBIN": "State Bank Of India", "ICIC": "ICICI Bank", "AXIS": "Axis Bank", "HDFC": "HDFC Bank",
             "PNBN": "Punjab National Bank"}
    # create dictionary for countries
    countries = {"IN": "India", "US": "United States Of America", "DE": "Germany", "FR": "France",
                 "UK": "United Kingdom",
                 "RU": "Russia"}
    # create dictionary for location
    locations = {"MY": "Mysore", "DL": "Delhi", "NY": "NewYork", "BE": "Berlin", "PR": "Paris", "LN": "London",
                 "MO": "Moscow"}
    # create dictionary for branch codes
    branches = {"111": "Rama Vilas Road", "232": "Chandni Chowk", "444": "Mukherjee Nagar", "888": "Wall Street"}
    # Ask for input
    swiftcode = raw_input("Enter Swift code :")
    if len(swiftcode) == 11:
        extract_details(swiftcode)
    else:
        print("Invalid SwiftCode! Should be exactly equal to 11 characters")
