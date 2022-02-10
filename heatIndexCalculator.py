#<<<<<<<<<<Heat Index Calculator>>>>>>>>>>>>
#This program will take in a series of inputs from the user about the location, the amount of locations, the temperature, and
#the relative humidity percentage, and give the user an average.
#Created by Nicholas Russell, COMP-151-001 (MW 12:20-1:35PM)

temp = 0
relHumidity = 0
HI = 42.379 + 2.04901523*temp + 10.14333127*relHumidity - 0.22475541*temp*relHumidity - 0.00683783*temp*temp - 0.05481717*relHumidity*relHumidity
+ 0.00122874*temp*temp*relHumidity + 0.00085282*temp*relHumidity*relHumidity - 0.00000199*temp*temp*relHumidity*relHumidity

def main():
    heatIndexSum = 0
    humiditySum = 0
    tempSum = 0
    print("<<<<<<<<<<<<<<<<<<<<<<Heat Index Calculator>>>>>>>>>>>>>>>>>>>>>>>>>>")
    locNum = int(input("How many locations would you like to calculate the heat index of?"))
    decPrecision = int(input("Enter decimal precision for calculations:"))

    for i in range(locNum):
        locName = str(input("Enter name of Location ",locNum,":"))
        temp = int(input("Enter temperature for this location:"))
        humidity = int(input("Enter humidity (percentage):"))