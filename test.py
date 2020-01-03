import CiscoAXL
from CiscoAXL import Site

print("Creating site")


newsite = Site("TX999") # created an instance of the class
newsite.TZ = "CMLocal"
newsite.Carrier = "ATT"
newsite.CallManagerGroup = "2A"
newsite.CAC = 4444
newsite.Build()

