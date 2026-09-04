import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("data/student_data.csv")


print("Average Study Hours:",
data["Study_Hours"].mean())
print("Average Attendance:",
data["Attendance"].mean())
print("Average Previous Score:",
data["Previous_Score"].mean())
print("Average final Score:",
data["Final_Score"].mean())   

print("\nStudy Hours vs Final Score:")
print(data[["Study_Hours","Final_Score"]])

plt.scatter(data["Study_Hours"],
data["Final_Score"])
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Study Hours vs Final Score")
plt.savefig("Study_Hours_vs_Final_Score.png")

plt.figure()
plt.scatter(data["Attendance"],
data["Final_Score"])
plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.title("Attendance_vs_Final_Score")  

plt.savefig("attendance_vs_final_score.png" )

plt.figure()
plt.scatter(data["Attendance"],
data["Final_Score"])
plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.title("Attendance vs Final Score")

plt.savefig("attendance_vs_final_score.png")
