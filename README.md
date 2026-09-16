
Student Success Pipeline

An automated data pipeline that processes student academic records to surface early risk indicators — built as a personal data engineering project using PySpark.

What it does

The pipeline ingests raw student data (demographics, enrolment, and semester performance) and transforms it into a clean, analysis-ready dataset with:

- Standardized column names
- Null handling for missing target outcomes
- A derived average grade metric across semesters
- A simple dropout risk score (low / medium / high) based on academic performance
- A summary aggregation comparing outcomes (Dropout / Enrolled / Graduate) by mean grade and risk score

Tech stack

PySpark — distributed data processing and transformations
Python — orchestration and scripting
pandas — supporting data handling

Pipeline stages

1. Extract — read the raw CSV dataset into a Spark DataFrame
2. Clean — standardize column names, drop rows with missing target values
3. Transform — calculate average grade per student, assign a risk score
4. Aggregate — summarize outcomes by mean grade and mean risk score

Dataset

Uses the [Predict Students' Dropout and Academic Success](https://www.kaggle.com/datasets/adilshamim8/predict-students-dropout-and-academic-success) dataset (36 features, 4,424 records), covering academic path, demographics, and socio-economic factors at enrolment.

Results

The pipeline confirms a clear relationship between academic performance and outcome:

| Outcome | Mean grade | Mean risk score |
|---|---|---|
| Graduate | 12.67 | 1.53 |
| Enrolled | 11.12 | 1.92 |
| Dropout | 6.58 | 2.43 |

Running it locally

bash
python -m venv venv
source venv/Scripts/activate
pip install pyspark pandas
python etl.py
```

Author

Juliet Chinenye Duru
