
# ============================================================
# PS Number      : 1
# Project Title  : Student Performance Analyzer
# Student Name   : Rakshita Dubey
# Email ID       : rakshita.dubey@rungta.org
# Course         : BCA - First Semester
# Section        : 1C
# ============================================================

# Student Performance Analyzer
# This program reads student marks, calculates total marks,
# percentages and grades, displays class statistics, and
# generates charts using Pandas, NumPy and Matplotlib.

# Importing Required Libraries
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl



# Function to Calculate Student Grade
def get_grade(percentage):
    if percentage >= 90: return 'A'
    elif percentage >= 75: return 'B'
    elif percentage >= 60: return 'C'
    elif percentage >= 40: return 'D'
    else: return 'F'


# Function to Load and Process Student Data
def load_data(file_path):
    subjects = ['Maths', 'Physics', 'Chemistry']
    valid_rows = []

    # Checking whether the CSV file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return None

    # Reading student records from the file
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(',')
            if len(parts) != 4:
                continue

            name = parts[0]
            row_valid = True
            marks = []

            # Validating student marks
            for i, val in enumerate(parts[1:]):
                try:
                    marks.append(float(val))
                except ValueError:
                    print(f"Invalid marks for {name} in {subjects[i]}: '{val}'. Row skipped.")
                    row_valid = False
                    break

            if row_valid:
                valid_rows.append([name] + marks)

    if not valid_rows:
        return None

    # Creating DataFrame using Pandas
    df = pd.DataFrame(valid_rows, columns=['Name', 'Maths', 'Physics', 'Chemistry'])

    # Calculating Total Marks, Percentage and Grade
    df['Total'] = df[['Maths', 'Physics', 'Chemistry']].sum(axis=1)
    df['Percentage'] = (df['Total'] / 300) * 100
    df['Grade'] = df['Percentage'].apply(get_grade)

    return df


# Function to Display Student Results
def display_results(df):
    if df is None or df.empty:
        return

    # Displaying individual student performance
    for _, row in df.iterrows():
        print(f"{row['Name']} | {int(row['Total'])} | {row['Percentage']:.2f}% | {row['Grade']}")


# Function to Display Class Statistics and Charts
def display_statistics(df):
    if df is None or df.empty:
        return

    # Calculating Class Statistics using NumPy and Pandas
    mean_pct = np.mean(df['Percentage'])
    median_pct = np.median(df['Percentage'])
    std_pct = np.std(df['Percentage'], ddof=0)  # Population standard deviation

    # Finding Topper Details
    topper_idx = df['Percentage'].idxmax()
    topper_name = df.loc[topper_idx, 'Name']
    topper_pct = df.loc[topper_idx, 'Percentage']

    # Calculating Subject-wise Average Marks
    maths_avg = df['Maths'].mean()
    physics_avg = df['Physics'].mean()
    chem_avg = df['Chemistry'].mean()

    # Displaying Statistical Results
    print(f"Mean %: {mean_pct:.2f} | Median %: {median_pct:.2f} | Std Dev: {std_pct:.2f}")
    print(f"Topper: {topper_name} ({topper_pct:.2f}%)")
    print(f"Subject averages: Maths {maths_avg:.2f}, Physics {physics_avg:.2f}, Chemistry {chem_avg:.2f}")

    # Plotting Section
    plt.figure(figsize=(12, 5))

    # 1. Bar Chart for Student Percentages
    plt.subplot(1, 2, 1)
    plt.bar(df['Name'], df['Percentage'], color='skyblue', edgecolor='black')
    plt.title('Student Overall Percentages')
    plt.xlabel('Students')
    plt.ylabel('Percentage (%)')
    plt.ylim(0, 105)

    # 2. Histogram of Overall Percentages
    plt.subplot(1, 2, 2)
    plt.hist(df['Percentage'], bins=5, range=(0, 100), color='salmon', edgecolor='black')
    plt.title('Distribution of Percentages')
    plt.xlabel('Percentage Range')
    plt.ylabel('Number of Students')

    # Adjusting Chart Layout
    plt.tight_layout()
    plt.show()


# Main Function
def main():

    # Loading Student Data from CSV File
    file_path = 'students.csv'
    df = load_data(file_path)

    # Displaying Main Menu
    print("\n--- Student Performance Analyzer Menu ---")
    print("1. View Student Results")
    print("2. View Class Statistics & Charts")
    print("3. Exit")

    # Taking User Choice
    try:
        choice = input("Select an option (1-3): ").strip()
        print(f"Menu option {choice} (Selected)\n")

        if choice == '1':
            display_results(df)
        elif choice == '2':
            display_statistics(df)
        elif choice == '3':
            sys.exit()
        else:
            print("Invalid choice selected.")

    except ValueError:
        print("Please enter a valid numeric option.")


# Program Execution Starts Here
if __name__ == "__main__":
    main()
