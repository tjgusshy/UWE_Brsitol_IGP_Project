# 📑 CSV Data Documentation

This document describes the CSV files in the `csv_data` folder, which are used for student analytics and performance analysis in the UWE Bristol IGP Project.

---

## 📁 Folder: `csv_data/`

### Contents:
- **data1.xlsx** / **data2.xlsx**: Source Excel files containing raw student data and weekly activity.
- **demo_week_2.csv** / **demo_week_2_numeric.csv**: Demographic and engagement data for week 2, in both categorical and numeric formats.
- **Retro_numeric.csv** / **Retrospective.csv**: Retrospective student performance and engagement data, including numeric scores and categorical responses.
- **week1.csv** / **week1_demo.csv**: Week 1 student activity and demo data, including attendance, participation, and demographic details.
- **week2.csv** / **week2_demo.csv**: Week 2 student activity and demo data, similar structure to week 1 files.

---

## 🗂️ File Descriptions

- **data1.xlsx / data2.xlsx**
  - Raw source data from institutional records and LMS exports.
  - Multiple sheets may contain demographic, performance, and engagement metrics.

- **demo_week_2.csv**
  - Student demographic and engagement data for week 2.
  - Columns: `student_id`, `age`, `gender`, `course`, `attendance`, `participation`, etc.

- **demo_week_2_numeric.csv**
  - Numeric encoding of week 2 demographic and engagement data.
  - Useful for statistical analysis and machine learning models.

- **Retro_numeric.csv**
  - Retrospective numeric scores for students across multiple weeks.
  - Columns: `student_id`, `week`, `score`, `assignment_completion`, etc.

- **Retrospective.csv**
  - Categorical and text-based retrospective data.
  - Includes survey responses, feedback, and qualitative metrics.

- **week1.csv / week2.csv**
  - Weekly student activity data (attendance, scores, engagement).
  - Columns: `student_id`, `date`, `activity_type`, `score`, etc.

- **week1_demo.csv / week2_demo.csv**
  - Demo versions of weekly data for testing and validation.
  - Useful for code development and pipeline testing.

---

## 🛠️ Usage

- Use these CSV files as input for ETL scripts, data cleaning notebooks, and analysis workflows.
- All files are UTF-8 encoded and compatible with pandas, Excel, and most data tools.
- For column details, see the header row in each file or refer to the main project documentation.

---

## 📋 Notes

- Some files may be updated or replaced as new data is collected.
- Demo files are for development/testing and may not reflect final analysis results.
- For questions about data structure, contact the project maintainer.

---

**These CSV files are the foundation for all student analytics and performance modeling in this project.**
