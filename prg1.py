current_year=int(input("enter current year:"))
final_year=int(input("enter final year:"))
for year in range(current_year,final_year +1):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
     print(year)
