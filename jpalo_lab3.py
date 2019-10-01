#Lab 3

#Problem 1: MagicDates

month = int(input("Enter 2-digit month:"))
day = int(input("Enter 2-digit day:"))
year = int(input("Enter 2-digit year:"))

if year == month * day:
    print("The date is magic!")

else:
   print("The date is not magic.")

#Problem 2: ColorMixer

primary_color1 = input("Enter your first primary color:")
primary_color2 = input("Enter your second primary color:")

if primary_color1 == "red" and primary_color2 == "blue":
    print("When you mix red and blue, you get purple.")

elif primary_color1 == "blue" and primary_color2 == "red":
    print("When you mix blue and red, you get purple.")

elif primary_color1 == "red" and primary_color2 == "yellow":
    print("When you mix red and yellow, you get orange.")

elif primary_color1 == "yellow" and primary_color2 == "red":
    print("When you mix yellow and red, you get orange.")

elif primary_color1 == "blue" and primary_color2 == "yellow":
    print("When you mix blue and yellow, you get green.")

elif primary_color1 == "yellow" and primary_color2 == "blue":
    print("When you mix yellow and blue, you get green.")

else:
    print("You didn't input two primary colors.")

#Problem 3: TimeCalculator >> DEBUG

seconds = int(input("Enter the number of seconds:"))
day = seconds//86400
hour = (seconds - day*86400)//3600
minute = (seconds- day*86400 - hour*3600)//60
converted_seconds = seconds - day*86400 - hour*3600 - minute*60

print("{} day(s), {} hour(s), {} minute(s), and {} second(s)".format(day, hour, minute, converted_seconds))






    
    
