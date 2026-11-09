# CIS-117 Lab3
# Read country data from a CSV file and create one new CSV file per region, separating the countries into their respective files.
# Nicholas Bordner

import csv

try:
    with open("country_full.csv", "r") as file:
        print(file.name)

        # Make a dictionary to hold the countries by region
        reader = csv.reader(file)
        countries_by_region = {}

        for country in list(reader)[1:]:
            name = country[0].strip()
            region = country[5].strip()

            # If the region is blank, this will assign it to "Unspecified Region"
            # Example: Antarctica is in the file, but its region is blank, so it will be put in the unspecified section.
            if region == "":
                region = "Unspecified Region"

            if region not in countries_by_region:
                countries_by_region[region] = []

            countries_by_region[region].append(name)


        # Create a new CSV file for each region and write the countries into it.
        for region, countries in countries_by_region.items():
            with open(f"{region}.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([f"Countries in {region}"])
                writer.writerows([[country] for country in countries])

# Exception handling
except FileNotFoundError as error:
    print(f"Could not find {error.filename}: {error}")
except PermissionError as error:
    print(f"Permission denied: {error}")
except csv.Error as error:
    print(f"CSV error: {error}")
except IOError as error:
    print(f"File I/O error: {error}")
except Exception as error:
    print(f"Unexpected error: {error}")