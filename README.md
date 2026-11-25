<div align="center">

# 📊 Student Performance Analyzer

**Raw marks in. Grades, insights and charts out.**

A tidy little command-line tool that turns a plain CSV of exam scores into totals, percentages, grades, class statistics and clean visualisations.

![Python](https://img.shields.io/badge/Python-3.8%2B-1F618D?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data-148F77?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Stats-154360?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Charts-0E6251?style=for-the-badge)

</div>

---

## 🪪 Project Details

| | |
|---|---|
| **PS Number** | 1 |
| **Project Title** | Student Performance Analyzer |
| **Student Name** | Rakshita Dubey |
| **Email ID** | rakshita.dubey@rungta.org |
| **Course** | Bachelor of Computer Applications (Full Stack in association with Google) |
| **Section** | 1C |
| **REF No.** | RU-26-02060 |
| **University** | Rungta International Skills University, Bhilai (C.G.) |

---

## ✨ What It Does

Drop a `students.csv` next to the script, run it, and get an interactive menu that handles the rest.

- 🧮 **Results**: total marks, percentage and letter grade for every student
- 📈 **Statistics**: mean, median, standard deviation, class topper and per-subject averages
- 📊 **Bar chart**: side-by-side percentage comparison, auto-labelled
- 🗂️ **Histogram**: see how the whole class is distributed across score ranges
- 🔄 **Live reload**: edit the CSV, press `4`, no restart needed
- 🛡️ **Forgiving input**: missing files, bad numbers and out-of-range marks are caught and skipped with a clear message instead of crashing

---

## 🏅 Grading Scale

| Percentage | Grade |
|:---:|:---:|
| 90 and above | **A** |
| 75 – 89.99 | **B** |
| 60 – 74.99 | **C** |
| 40 – 59.99 | **D** |
| Below 40 | **F** |

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/student-performance-analyzer.git
cd student-performance-analyzer
```

### 2. Install dependencies

```bash
pip install pandas numpy matplotlib
```

### 3. Run it

```bash
python main.py
```

---

## 📁 Dataset Format

`students.csv` has one student per row. The header row is optional and detected automatically.

```csv
Name,Maths,Physics,Chemistry
Aman,80,70,90
Riya,60,65,70
Karan,40,35,50
```

Marks must be numbers between **0 and 100**. Any row that breaks this rule is skipped and reported.

---

## 🖥️ Demo

```text
=== Student Performance Analyzer ===

1. Result (Totals, Percentages & Grades)
2. Statistics (Mean, Median, Std Dev, Topper & Bar Chart)
3. Plot Histogram (Percentage Distribution)
4. Reload Dataset
5. Exit
Enter choice (1-5): 1

--- Student Results ---
Aman | 240 | 80.00% | B
Riya | 195 | 65.00% | C
Karan | 125 | 41.67% | D
```

```text
Enter choice (1-5): 2

--- Class Statistics ---
Mean %: 62.22 | Median %: 65.00 | Std Dev: 15.77
Topper: Aman (80.00%)
Subject averages: Maths 60.00, Physics 56.67, Chemistry 70.00
Bar chart displayed
```

> 💡 Drop your own screenshots of the bar chart and histogram here, e.g. `![Bar chart](screenshots/bar_chart.png)`

---

## 🧠 How It Works

```
students.csv ──► load_students() ──► validate & clean ──► DataFrame
                                                             │
                     ┌───────────────────────────────────────┤
                     ▼                    ▼                  ▼
              display_results()   display_statistics()  plot_histogram()
              totals · % · grade   mean · median · σ      distribution
                                   topper · bar chart
```

| Function | Role |
|---|---|
| `load_students()` | Reads the CSV, skips the header, validates every mark, computes Total, Percentage and Grade |
| `assign_grade()` | Maps a percentage to a letter grade |
| `display_results()` | Prints the per-student result table |
| `display_statistics()` | Computes class-level stats with NumPy and finds the topper |
| `plot_bar_chart()` | Draws the labelled percentage comparison |
| `plot_histogram()` | Draws the percentage distribution in 20-point bins |

> Standard deviation is the **population** standard deviation (`ddof=0`), which treats the class as the full group rather than a sample.

---

## 🧰 Tech Stack

| Tool | Used for |
|---|---|
| **Python** | Core logic and the CLI menu |
| **Pandas** | Loading, cleaning and aggregating data |
| **NumPy** | Mean, median and standard deviation |
| **Matplotlib** | Bar chart and histogram |

---

## 🌱 Ideas for Next Steps

- [ ] Export results to a new CSV or Excel report
- [ ] Add more subjects dynamically from the CSV header
- [ ] Per-student radar chart across subjects
- [ ] A small Streamlit dashboard version

---

<div align="center">

**Built by Rakshita Dubey** · BCA (Full Stack in association with Google) · Section 1C
Rungta International Skills University, Bhilai

⭐ If you found this useful, consider starring the repo.

</div>

For Test 2, temporarily change the initial `health` value to `30` and set `TEST_MODE = True`. For Test 4, set `health = ...` and `TEST_MODE = True`. Restore `health = 100` and `TEST_MODE = False` for normal gameplay.

## Conclusion

This project demonstrates how basic Python concepts can be combined to create an interactive text-based game with player choices, random damage, scoring, and game-ending conditions.

## Project Mentor

**Mentored by:** [Mr. Satyaprakash Sethy](https://github.com)

**GitHub:** [@SATYAPRAKASHSETHY](https://github.com)

**Role:** Python Mentor / Technical Guide

