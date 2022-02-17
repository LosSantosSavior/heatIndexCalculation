#<<<<<<<<<<Heat Index Calculator>>>>>>>>>>>>
#This program will take in a series of inputs from the user about the location, the amount of locations, the temperature, and
#the relative humidity percentage, and give the user an average.
#Created by Nicholas Russell, COMP-151-001 (MW 12:20-1:35PM)
#Extra credit completed (error testing for invalid inputs for temperature and humidity)
def main():
    heatIndexSum = 0.0
    humiditySum = 0
    tempSum = 0
    minTemp = float('inf')
    minHI = float('inf')
    maxHumidity = float('-inf')


    print("<<<<<<<<<<<<<<<<<<<<<<Heat Index Calculator>>>>>>>>>>>>>>>>>>>>>>>>>>")
    locNum = int(float(input("\tHow many locations would you like to calculate the heat index of?")))
    if locNum < 1:
        print("Number of locations cannot be 0 or less than 0.")
        exit(-1)
    decPrecision = int(input("\tEnter decimal precision for calculations (1<-->4):"))
    if decPrecision < 1 or decPrecision > 4:
        print("Decimal precision number cannot be less than 0 or greater than 4.")
        exit(-1)

    for i in range(locNum):
        locName = str(input(f"\tEnter name of Location {i+1}:"))
        temp = int(input("\tEnter temperature for this location (degrees fahrenheit):"))
        if temp < minTemp:
            minTemp = temp
            minTempLoc = locName
        if temp < -138 or temp > 138:
            print("Temperature out of range, your temperature is either too hot or too cold to be calculated.")
            exit(-1)
        humidity = int(input("\tEnter humidity (percentage):"))
        if humidity > maxHumidity:
            maxHumidity = humidity
            maxHumidLoc = locName
        if humidity < 0 or humidity > 100:
            print("Humidity percentage cannot be less than 0% or more than 100%.")
            exit(-1)
        HI = -42.379 + 2.04901523*temp + 10.14333127*humidity - 0.22475541*temp*humidity - 0.00683783*temp*temp - 0.05481717*humidity*humidity +0.00122874*temp*temp*humidity + 0.00085282*temp*humidity*humidity - 0.00000199*temp*temp*humidity*humidity
        if HI < minHI:
            minHI = HI
            minHILoc = locName
        print(round(HI, decPrecision))
        heatIndexSum = heatIndexSum + HI
        humiditySum = humiditySum + humidity
        tempSum = tempSum + temp

    print("<<<<<<<<<<<<<<<<<<<<<<Summary>>>>>>>>>>>>>>>>>>>>>>>>>>")

    print("HI:")
    print("\tAverage recorded HI:",round(heatIndexSum / locNum,decPrecision), "degrees Fahrenheit")
    print("\tLocation with lowest HI:")
    print(minHILoc,",",round(minHI,decPrecision), "degrees Fahrenheit")

    print("Air Temperature:")
    print("\tAverage recorded air temperature: ",round(tempSum / locNum,decPrecision), "degrees Fahrenheit")
    print("\tLocation with lowest air temperature:")
    print(minTempLoc,",",round(minTemp,decPrecision), "degrees Fahrenheit")

    print("Relative Humidity:")
    print("\tAverage recorded relative humidity:",round(humiditySum / locNum,decPrecision), "%")
    print("\tLocation with highest relative humidity:")
    print(maxHumidLoc,",",round(maxHumidity,decPrecision), "%")

main()