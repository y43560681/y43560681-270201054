month = input("Please enter month : ")
day = int(input("Please enter day : "))

month = month.lower()

if (month == "december") or (month == "january") or (month == "february"):
  season = "winter"

elif (month == "march") or (month == "april") or (month == "may"):
  season = "spring"

elif (month == "june") or (month == "july") or (month == "augst"):
 season = "summer"

elif (month == "september") or (month == "october") or (month == "november"):
  season = "autumn"

if (month =="march") and (day<19): 
 season = "winter"

elif (month =="june") and (day<21):
  season = "spring"

elif (month =="september") and (day<22):
  season = "summer"

elif (month =="december") and (day<21):
 season = "autumn"

print("Season is", season)