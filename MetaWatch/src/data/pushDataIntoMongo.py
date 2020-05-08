import csv
import pymongo

# Database informations
##f = open("../../auth/auth.private","r")
##lines = f.readlines()
##dbUsername = lines[0].split("=")[1][:-1]
##dbPassword = lines[1].split("=")[1][:-1]
##dbURL = lines[2].split("=")[1][:-1]
##f.close()

# Connect to database
try: 
##    client = pymongo.MongoClient("mongodb+srv://"+dbUsername+":"+dbPassword+"@"+dbURL)
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    print("Connected successfully!!!")
except:   
    print("Could not connect to MongoDB")

db = client.metawatch
collection = db.interest
##collection.delete_many({"vid_UUID":31})
##
##for x in collection.find({"vid_UUID":31}):
##    print(x)

# Datafile to push in database
vid_uuid = 31
analysis_uuid = 91
listRequest = []
with open("../../data/processed/extracted/"+str(vid_uuid)+"-"+str(analysis_uuid)+"_extracted.interest.csv") as interestfile:
    interest_reader = csv.reader(interestfile, delimiter=',')
    interest_header = next(interest_reader, None)
    with open("../../data/processed/extracted/"+str(vid_uuid)+"-"+str(analysis_uuid)+"_extracted.ft.csv") as featurefile:
        feature_reader = csv.reader(featurefile, delimiter=',')
        feature_header = next(feature_reader, None)
        while True:
            interest_data = next(interest_reader, None)
            if interest_data == None:
                break
            feature_data = next(feature_reader, None)
            request = {"vid_UUID":vid_uuid, "analysis_UUID":analysis_uuid}
            
            for i in range(len(interest_header)):
                request[interest_header[i]] = interest_data[i]
            for i in range(len(feature_header)):
                request[feature_header[i]] = feature_data[i]
            listRequest.append(request)
        # Insert Data 
        request_id = collection.insert_many(listRequest)
        print("Data inserted with record ids", request_id) 
print("All request done")





