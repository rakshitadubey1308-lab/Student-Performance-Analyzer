# Student Performance Analyzer

## Project Details

| Field | Details |
|---|---|
| PS Number | 1 |
| Project Title | Student Performance Analyzer |
| Student Name | Rakshita Dubey |
| Email ID | rakshita.dubey@rungta.org |
| Course | BCA - First Semester |
| Section | 1C |

## 1. Project Description

The Student Performance Analyzer is a Python-based project that analyzes student academic performance using their marks in three subjects: Maths, Physics, and Chemistry.

It calculates total marks, percentages, and grades for each student. It also displays class statistics, identifies the class topper, calculates subject-wise averages, and generates graphical charts.

## 2. Objectives

- To calculate students' total marks.
- To calculate student percentages.
- To assign grades based on percentages.
- To identify the class topper.
- To calculate mean, median, and standard deviation.
- To calculate subject-wise average marks.
- To display student performance using charts.

## 3. Technologies Used

- **Python:** Main programming language.
- **NumPy:** Used for numerical calculations.
- **Pandas:** Used for data processing and analysis.
- **Matplotlib:** Used for graphical representation.
- **OS Module:** Used to check file existence.
- **Sys Module:** Used to exit the program.

## 4. Project Features

1. Student Data Loading
2. CSV File Validation
3. Total Marks Calculation
4. Percentage Calculation
5. Automatic Grade Assignment
6. Student Result Display
7. Class Statistics
8. Topper Identification
9. Subject-wise Average Calculation
10. Bar Chart and Histogram Generation

## 5. Grade Criteria

| Percentage | Grade |
|---|---|
| 90% and above | A |
| 75% - 89% | B |
| 60% - 74% | C |
| 40% - 59% | D |
| Below 40% | F |

## 6. Input File Format

The project uses a CSV file named `students.csv`.

Example:

```csv
Rahul,85,90,88
Priya,92,95,90
Aman,65,70,68
Neha,78,82,80
```

Each row contains:
- Student Name
- Maths Marks
- Physics Marks
- Chemistry Marks

## 7. Installation Requirements

Install Python and the required libraries.

Run these commands in the VS Code terminal:

```bash
pip install numpy pandas matplotlib
```

## 8. How to Run the Project

1. Open the project folder in VS Code.
2. Create a Python file named `student_analyzer.py`.
3. Save the project code in that file.
4. Create a CSV file named `students.csv`.
5. Add student records to the CSV file.
6. Open the VS Code terminal.
7. Run the following command:

```bash
python student_analyzer.py
```

## 9. Main Menu

The program displays the following menu:

```text
--- Student Performance Analyzer Menu ---

1. View Student Results
2. View Class Statistics & Charts
3. Exit

Select an option (1-3):
```

## 10. Output

### Option 1: View Student Results

Displays each student's name, total marks, percentage, and grade.

### Option 2: View Class Statistics & Charts

Displays:
- Mean Percentage
- Median Percentage
- Standard Deviation
- Class Topper
- Subject-wise Average Marks
- Student Percentage Bar Chart
- Percentage Distribution Histogram

### Option 3: Exit

Terminates the program.

## 11. Expected Graphs

The project generates two graphical representations:

1. **Bar Chart:** Displays the overall percentage of each student.
2. **Histogram:** Displays the distribution of student percentages.

## 12. Conclusion

The Student Performance Analyzer is a useful Python project that helps analyze student academic performance efficiently. It uses Python libraries such as NumPy, Pandas, and Matplotlib to perform calculations, process student records, and generate graphical reports.

This project demonstrates the practical application of Python programming, data analysis, and data visualization.

---

**Project Developed By:** Rakshita Dubey  
**Course:** BCA - First Semester  
**Section:** 1C  
**PS Number:** 1
