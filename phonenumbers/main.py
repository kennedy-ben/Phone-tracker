import phonenumbers
from phonenumbers import geocoder, carrier


number = "+25490908090"  

parsed_number = phonenumbers.parse(number, "CH")

location = geocoder.description_for_number(parsed_number, "en")
print("Geographic Location:", location)

carrier_name = carrier.name_for_number(parsed_number, "en")
print("Carrier Name:", carrier_name)
