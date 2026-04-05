from scr.generate_data import generate_friend_csv, generate_students_csv
from scr.load_data import load_csv
from scr.basic_stats import calculate_basic_stats
from scr.analysis import add_column, detect_outliers, group_by_city
import os

print("Generate data")
generate_friend_csv()
print("Load data")
# students_df = generate_students_csv()
path = "data/raw/students.csv"
students_df = load_csv(path)
students_df = add_column(students_df)
os.makedirs(os.path.dirname(path), exist_ok=True)
students_df.to_csv(path, index=False)
print(students_df)
print("-" * 20)

print("Task 1")
friends_df = load_csv("data/raw/friends.csv")
calculate_basic_stats(friends_df)
print("-" * 20)

print("Task 2") #вивести середній бал і кількість студентів в кожному місті
print("Average score:",
        students_df["Score"].mean())
print(students_df["City"].value_counts())
print("-" * 20)

print("Task 3") #Для студентів додати колонки винятків та згрупувати по місту
students_df = add_column(students_df)
detect_outliers(students_df)
group_by_city(students_df)