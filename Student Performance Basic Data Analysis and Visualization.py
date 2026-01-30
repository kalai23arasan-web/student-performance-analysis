import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# -----------------------------
# Data Generation
# -----------------------------

#load dataset

np.random.seed(42)  # Ensures reproducibility

num_students = 200

study_hours = np.random.randint(1, 10, num_students)
previous_scores = np.random.randint(40, 90, num_students)

# Final exam grade depends on study hours and previous scores
final_exam_grade = (
    study_hours * 5 +
    previous_scores * 0.5 +
    np.random.normal(0, 5, num_students)
)

# Create DataFrame
data = pd.DataFrame({
    "StudyHours": study_hours,
    "PreviousScore": previous_scores,
    "FinalExamGrade": final_exam_grade
})

# Display first few rows
print(data.head())

# -----------------------------
# Data Analysis
# -----------------------------

# Check for Missing Values
# Missing values can distort statistics and correlations.

print("\nMissing Values:")
print(data.isnull().sum())

# Calculate Summary Statistics

summary_stats = data.describe()
print("\nSummary Statistics:")
print(summary_stats)

# Median separately (describe does not show median clearly)
print("\nMedian Values:")
print(data.median())

# Correlation Analysis
# Pearson correlation measures linear relationship strength (range: -1 to +1).
correlation = data["StudyHours"].corr(data["FinalExamGrade"])

print("\nPearson Correlation between StudyHours and FinalExamGrade:")
print(round(correlation, 2))

# Interpretation (Exam-Perfect Sentence)

if correlation > 0:
    interpretation = "There is a positive correlation, meaning higher study hours are associated with higher final exam grades."
elif correlation < 0:
    interpretation = "There is a negative correlation, meaning higher study hours are associated with lower final exam grades."
else:
    interpretation = "There is no correlation between study hours and final exam grades."

print("\nInterpretation:")
print(interpretation)

# -----------------------------
# Data Visualization
# -----------------------------

# Distribution Plot of FinalExamGrade
# Distribution plots help understand spread, skewness, and central tendency.

plt.figure()
sns.histplot(data["FinalExamGrade"], kde=True)
plt.title("Distribution of Final Exam Grades")
plt.xlabel("Final Exam Grade")
plt.ylabel("Frequency")
plt.show()


# Scatter Plot: StudyHours vs FinalExamGrade

plt.figure()
sns.scatterplot(
    x="StudyHours",
    y="FinalExamGrade",
    data=data
)
plt.title("Study Hours vs Final Exam Grade")
plt.xlabel("Study Hours")
plt.ylabel("Final Exam Grade")
plt.show()


