"""
Student Performance Analyzer
Student: Rakshita Dubey (REF No.: RU-26-02060)
Program: Bachelor of Computer Applications (Full Stack in association with Google)
University: Rungta International Skills University, Bhilai (C.G.)
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = "students.csv"
SUBJECTS = ["Maths", "Physics", "Chemistry"]


def assign_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def load_students(file_path=FILE_NAME):
    if not Path(file_path).exists():
        print(f"File '{file_path}' not found.")
        return pd.DataFrame(columns=["Name"] + SUBJECTS)

    raw_df = pd.read_csv(file_path, header=None, dtype=str)
    if raw_df.empty:
        return pd.DataFrame(columns=["Name"] + SUBJECTS)

    # Detect and skip optional header row
    first_row = [str(val).strip().lower() for val in raw_df.iloc[0].tolist()]
    if first_row[:4] == ["name", "maths", "physics", "chemistry"]:
        raw_df = raw_df.iloc[1:].reset_index(drop=True)

    valid_rows = []
    for _, row in raw_df.iterrows():
        if len(row) < 4:
            continue

        name = str(row.iloc[0]).strip()
        marks = {}
        row_valid = True

        for idx, subject in enumerate(SUBJECTS, start=1):
            raw_val = str(row.iloc[idx]).strip()
            try:
                score = float(raw_val)
                if score < 0 or score > 100:
                    print(f"Invalid marks for {name} in {subject}: '{raw_val}'. Row skipped.")
                    row_valid = False
                    break
                marks[subject] = score
            except ValueError:
                print(f"Invalid marks for {name} in {subject}: '{raw_val}'. Row skipped.")
                row_valid = False
                break

        if row_valid:
            valid_rows.append({
                "Name": name,
                "Maths": marks["Maths"],
                "Physics": marks["Physics"],
                "Chemistry": marks["Chemistry"],
            })

    df = pd.DataFrame(valid_rows, columns=["Name"] + SUBJECTS)
    if not df.empty:
        df["Total"] = df[SUBJECTS].sum(axis=1)
        df["Percentage"] = (df["Total"] / (len(SUBJECTS) * 100)) * 100
        df["Grade"] = df["Percentage"].apply(assign_grade)
    return df


def format_total(val):
    return str(int(val)) if val == int(val) else f"{val:.2f}"


def display_results(df):
    if df.empty:
        print("No valid student records available.")
        return

    print("\n--- Student Results ---")
    for _, row in df.iterrows():
        total_str = format_total(row["Total"])
        print(f"{row['Name']} | {total_str} | {row['Percentage']:.2f}% | {row['Grade']}")


def display_statistics(df, show_charts=True):
    if df.empty:
        print("No valid student records available for statistics.")
        return

    percentages = df["Percentage"].to_numpy()
    mean_pct = np.mean(percentages)
    median_pct = np.median(percentages)
    std_pct = np.std(percentages)  # population std dev (ddof=0)

    topper_idx = df["Percentage"].idxmax()
    topper = df.loc[topper_idx]

    subject_avgs = df[SUBJECTS].mean()

    print("\n--- Class Statistics ---")
    print(f"Mean %: {mean_pct:.2f} | Median %: {median_pct:.2f} | Std Dev: {std_pct:.2f}")
    print(f"Topper: {topper['Name']} ({topper['Percentage']:.2f}%)")
    print(
        f"Subject averages: Maths {subject_avgs['Maths']:.2f}, "
        f"Physics {subject_avgs['Physics']:.2f}, "
        f"Chemistry {subject_avgs['Chemistry']:.2f}"
    )

    if show_charts:
        plot_bar_chart(df)


def plot_bar_chart(df):
    if df.empty:
        print("No data to plot.")
        return

    plt.figure(figsize=(8, 4.8))
    bars = plt.bar(df["Name"], df["Percentage"], color="#1F618D", edgecolor="#154360", width=0.52)
    plt.title("Student Performance — Overall Percentage Comparison", fontsize=13, fontweight="bold")
    plt.xlabel("Student Name", fontsize=11)
    plt.ylabel("Percentage (%)", fontsize=11)
    plt.ylim(0, 110)
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    for bar, pct in zip(bars, df["Percentage"]):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 2,
            f"{pct:.2f}%",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
        )

    plt.tight_layout()
    print("Bar chart displayed")
    plt.show()


def plot_histogram(df):
    if df.empty:
        print("No data to plot.")
        return

    plt.figure(figsize=(8, 4.8))
    bins = [0, 20, 40, 60, 80, 100]
    plt.hist(df["Percentage"], bins=bins, color="#148F77", edgecolor="#0E6251", rwidth=0.82)
    plt.title("Distribution of Student Percentages (Histogram)", fontsize=13, fontweight="bold")
    plt.xlabel("Percentage Range (%)", fontsize=11)
    plt.ylabel("Number of Students", fontsize=11)
    plt.xticks(bins)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    print("Histogram displayed")
    plt.show()


def main():
    print("=== Student Performance Analyzer ===")
    df = load_students(FILE_NAME)

    while True:
        print("\n1. Result (Totals, Percentages & Grades)")
        print("2. Statistics (Mean, Median, Std Dev, Topper & Bar Chart)")
        print("3. Plot Histogram (Percentage Distribution)")
        print("4. Reload Dataset")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            display_results(df)
        elif choice == "2":
            display_statistics(df, show_charts=True)
        elif choice == "3":
            plot_histogram(df)
        elif choice == "4":
            df = load_students(FILE_NAME)
            print("Dataset reloaded.")
        elif choice == "5":
            print("Exiting Student Performance Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()
