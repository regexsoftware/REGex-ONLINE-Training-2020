import csv
from faker import Faker
import datetime
import random
from textblob import TextBlob
def datagenerate(records, headers):
    #fake2 = Faker('hi_IN')
    fake = Faker('en_US')
    fake1 = Faker('en_GB')   # To generate phone numbers
    with open("People_data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            #full_name = fake2.name()
            #name = TextBlob(full_name)
	    #name = name.translate(to='hi')
	    full_name = fake.name()
            FLname = full_name.split(" ")
            Fname = FLname[0]
            Lname = FLname[1]
            domain_name = "@gmail.com"
            userId = Fname +"."+ Lname + domain_name
            writer.writerow({
		    "Name": full_name,
		    #"surname": fake.surname(),
		    "age" : random.randint(18, 60),
                    "Email Id" : userId,
                    "Phone Number" : fake1.phone_number(),
                    
                    "Birth Date" : fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1,1)),
                    
                    
                    "Address" : fake.address(),
                    "Zip Code" : fake.zipcode(),
		    "Country": "India"
                    
                    })
    
if __name__ == '__main__':
    records = 1000
    headers = ["Name", "age", "Email Id", "Phone Number", "Birth Date",
               "Address", "Zip Code", "Country"]
    datagenerate(records, headers)
    print("CSV generation complete!")
