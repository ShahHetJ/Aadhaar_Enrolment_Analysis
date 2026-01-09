<p align="center">
  <img src="https://lh3.googleusercontent.com/gg-dl/ABS2GSm42Mb-5WKUl9ZiJPZses8uh9_ms76-rET0vyi60IMxz0-m7QfPMG141fvTxjX2wEH0JnQVzBDpPanXV8Exv7Mw2Y5Eo2cv2ylu7jdcDLSamhszKCZ2CLTBD2tOhwKquZYuQa2xF1bHhACAbQChVKE3K7qS7YqPNWHvtG_KtHJglzN6=s1024-rj"
       alt="Aadhaar Enrollment Analysis Poster"
       width="100%">
</p>



# Aadhaar_Enrolment_Analysis
<h1>Project Overview</h1>

This project focuses on cleaning, standardizing, and analyzing Aadhaar enrollment data to enable accurate geographic insights at the state, district, and pincode levels.
The workflow handles large CSV datasets, resolves inconsistent text values, removes invalid records, and produces aggregated outputs suitable for dashboards and further analysis (e.g., Power BI).

The primary goal is to ensure data quality, consistency, and reliable aggregation before visualization or decision-making.

<h1>File Descriptions</h1>
procees_to_merge.py

Purpose:
Merges multiple CSV files into a single dataset.

What it does:

Reads part_1.csv, part_2.csv, and part_3.csv

Concatenates them into one DataFrame

Saves the combined output as merege.csv

Why it matters:
Creates a unified dataset for all downstream cleaning and analysis steps.

checking.py

Purpose:
Performs a basic data quality check.

What it does:

Loads merege.csv

Prints the count of missing values for each column

Why it matters:
Helps identify incomplete or problematic columns early in the pipeline.

state_wise_enrollments.py

Purpose:
Generates state-wise enrollment counts with standardized state names.

What it does:

Normalizes state names (lowercase, trimmed, consistent spacing)

Removes numeric/invalid state entries

Fixes known spelling variations and merged UT names

Aggregates user counts per state

Why it matters:
Ensures accurate state-level aggregation by eliminating naming inconsistencies.

district_wise.py

Purpose:
Calculates district-wise enrollment counts.

What it does:

Cleans district names (lowercase, trimmed, standardized spacing)

Removes numeric/invalid district values

Groups data by district and counts enrollments

Why it matters:
Provides district-level insights while removing obvious data errors.

pincode_wise.py

Purpose:
Generates pincode-wise enrollment statistics.

What it does:

Cleans pincode values

Keeps only valid 6-digit numeric pincodes

Aggregates enrollment counts per pincode

Saves results to pincode_user_count.csv

Why it matters:
Ensures only valid geographic pincodes are used for fine-grained analysis.

data_cleaning.py

Purpose:
Advanced, automated cleaning of district names using fuzzy matching.

What it does:

Applies text normalization (lowercasing, removing special characters)

Uses frequency-based canonical naming

Automatically clusters similar district names using fuzzy matching (difflib)

Corrects spelling variations without a predefined master list

Outputs cleaned_district_usercount.csv

Why it matters:
Scales efficiently for large datasets and minimizes manual correction while significantly improving data consistency.

Output Files

merege.csv – Combined raw dataset

pincode_user_count.csv – Valid pincode-wise enrollment counts

cleaned_district_usercount.csv – Fully standardized district-level data

Technologies Used

Python

Pandas

Regular Expressions (re)

Fuzzy Matching (difflib)
