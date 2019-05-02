import uuid
stringLength = 9
randomString = uuid.uuid4().hex # get a random string in a UUID fromat
randomString  = randomString.upper()[0:stringLength] # convert it in a uppercase letter and trim to your size.
print("random string using a UUID module is ",randomString )
