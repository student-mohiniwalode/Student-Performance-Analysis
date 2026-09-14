import pandas as pd
import matplotlib.pyplot as plt

#load dataset
df = pd.read_csv("StudentsPerformance.csv")

#show first 5 rows
print(df.head())

#show no. of rows and coloumns
print("Dataset Shape:",df.shape)

#show coloumn name
print("Columns:",df.columns.tolist())

#checks missing values
print("\nMissing Values:")
print(df.isnull().sum())

#checks duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

#basic statistics
print("\nBasic Statistics:")
print(df.describe())

#Avarage score by gender
print("\nAverage Score By Gender:")
print(df.groupby("gender")[["math score", "reading score", "writing score"]].mean())

#Average score by parental education
print("\nAverage Score By Parental Education:")
print(df.groupby("parental level of education")[["math score", "reading score", "writing score"]].mean())

#Students who completed test preperation
print("\nTest Preparation Course:")
df.columns = df.columns.str.strip()
print(df["test preparation course"].value_counts())

#Overall average score
df["average score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)

print("\nOverall Average Score:")
print(df["average score"].mean())

# Highest scoring students
print("\nTop 10 Students:")
print(df.sort_values("average score", ascending = False).head(10))

#Average score by lunch 
print("\nAverage Score By Lunch:")
print(df.groupby("lunch")[["math score", "reading score", "writing score"]].mean())

#Average score by test preperation
print("\nAverage Score By Test Preparation:")
print(df.groupby("test preparation course")[["math score", "reading score", "writing score"]].mean())

#Average Score by gender
gender_score = df.groupby("gender")[["math score", "reading score", "writing score"]].mean()
gender_score.plot(kind="bar")
plt.title("Average Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#Average score by test preparation
prep_scores = df.groupby("test preparation course")[["math score", "reading score", "writing score"]].mean()

prep_scores.plot(kind="bar")

plt.title("Average score By Test Preparation")
plt.xlabel("Test Preparation Couurse")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#Average score by parantal education
parental_scores = df.groupby("parental level of education")[["math score", "reading score", "writing score"]].mean()

parental_scores.plot(kind="bar")

plt.title(" Average Score By Parantal Education")
plt.xlabel("Parantal Lavel Of Education")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Average score by lunch
lunch_scores = df.groupby("lunch")[["math score", "reading score", "writing score"]].mean()

lunch_scores.plot(kind="bar")

plt.title("Average Score By Lunch")
plt.xlabel("Lunch")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()



