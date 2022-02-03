import phonenumber

from test import number

from phonenumber import geocoder
ch_number = phonenumber.parse(number,"CH")
print(geocoder.description_for_number(ch_number,"en"))

from phonenumber import carrier

service_number = phonenumber.parse(number, "RO")

print(carrier.name_for_number(service_number,"en"))