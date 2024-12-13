# Data Engineering Project

This repository contains the code and dataset for a data engineering task involving patient details and prescriptions. The project focuses on various aspects such as data cleaning, processing, and analysis using Python, without relying on external libraries for certain validations.

## Project Overview

The project involves processing a dataset containing patient details, including:
- **Patient Name, Gender, Date of Birth, Phone Number**
- **Medicines Prescribed** and other consultation details

The tasks include:
1. **Missing Value Handling**: Calculating the percentage of missing values for specific fields like `firstName`, `lastName`, and `DOB`.
2. **Gender Imputation**: Filling missing gender values based on the mode of the column.
3. **Age Group Categorization**: Classifying patients into age groups and counting those in specific categories.
4. **Medicine Analysis**: Determining the average number of medicines prescribed and identifying the third most frequently prescribed medicine.
5. **Phone Number Validation**: Creating a logic to validate whether a phone number is a valid Indian phone number based on specific rules.
6. **Correlation Analysis**: Calculating the Pearson correlation between the number of prescribed medicines and the patient's age.

## Project Structure


data-engineering-project/
│
├── data/
│   └── DataEngineeringQ2.json           # Original dataset
│
├── scripts/
│   └── data_processing.py              # Python script for processing the data
│
├── README.md                          # Project documentation
└── Updated_DataEngineeringQ2.json      # Updated dataset after processing


## Setup and Usage

1. Clone the repository:

   bash
   git clone https://github.com/Saumya454/data-engineering-project.git
   cd data-engineering-project
   

3. Place the original dataset (`DataEngineeringQ2.json`) in the `data` folder.

4. Run the data processing script:
   ```
   bash
   python scripts/data_processing.py

5. The updated dataset will be saved as Updated_DataEngineeringQ2.json.

## License

This project is licensed under the MIT License.
