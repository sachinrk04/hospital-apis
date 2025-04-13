from datetime import datetime


# The %f in the format string adds microseconds to the timestamp, which ensures that the generated ID is unique even if two requests are made at the same microsecond.
def generateCustomId():
    return datetime.now().strftime("%Y%m%d%H%M%S%f")

# This function takes an id as input and returns a datetime object representing the timestamp of when the ID was generated. It uses the strptime() method to parse the id string into a datetime object using the same format string used by generate_custom_id().
def getDateTimeFromId(id):
    return datetime.strptime(id, "%Y%m%d%H%M%S%f")
