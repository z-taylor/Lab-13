# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Lab13A.py

#temps = "1 2 3 4 5 50 2 5 30 20 40 41 42 43 1 2 3"
#temps = temps.split(" ")
temps = input("Enter temperatures for each day separated by space: ").split(" ")
highStreaks, heatWaves, longestLowStreak, tempList1, lowStreakLengths, avgAdd = [], 0, [], [], [], 0
temps = [int(temp) for temp in temps]
for temp in temps:
    if temp > 30:
        tempList1.append(temp)
    elif temp <= 30 and tempList1 != [] and len(tempList1) >= 3:
        highStreaks.append(tempList1)
        tempList1 = []
if tempList1 != []:
    highStreaks.append(tempList1)
heatWaves = len(highStreaks)
tempList1 = []
for temp in temps:
    if temp < 15:
        tempList1.append(temp)
    elif temp >= 15 and tempList1 != []:
        lowStreakLengths.append(len(tempList1))
        tempList1 = []
if tempList1 != []:
    lowStreakLengths.append(len(tempList1))
longestLowStreak = max(lowStreakLengths)
for temp in temps:
    avgAdd += temp
averageTemp = round((avgAdd / len(temps)), 2)
print(f"Number of heat waves: {heatWaves}\nLongest cold streak: {longestLowStreak} days\nAverage temperature: {averageTemp}°C")