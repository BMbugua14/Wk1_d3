#Task1
#grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
#Answer1
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sorted_grades = sorted(grades, reverse=True)
print(sorted_grades)
#Answer2
average_grade = sum(grades) / len(grades)
print(average_grade)
 
#Task2
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
week_two_temps = temperatures[7:14]
print(week_two_temps)
hot_day = temperatures[24:]
print(hot_day)
#answer3
select_temps = temperatures[4:10]
print(select_temps)
