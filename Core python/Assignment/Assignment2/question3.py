##3.Convert distant given in feet and inches into meter and centimeter.

feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

total_inches = (feet * 12) + inches

cm = total_inches * 2.54
meter = cm / 100

print("Distance in meter:", meter)
print("Distance in centimeter:", cm)