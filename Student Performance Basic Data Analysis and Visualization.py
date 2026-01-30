import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
