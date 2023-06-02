DAILY_ORUNDUM = 100
WEEKLY_ORUNDUM = 500
ANNIHIL_ORUNDUM = 1800


months = int(input("Months before pulling: "))

days = months * 30
weeks = days // 7

total_orundums = (days * DAILY_ORUNDUM) + (WEEKLY_ORUNDUM * weeks) + (ANNIHIL_ORUNDUM * weeks)


print(f"Total Orundums: {total_orundums}")