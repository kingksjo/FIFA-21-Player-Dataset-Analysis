
---

# FIFA 21 Player Dataset Analysis

## Project Overview

This project focuses on the **data cleaning and exploration** of the EA Sports FIFA 21 player dataset i found on Kaggle. The goal is to preprocess and transform the data, enabling us to identify undervalued players with high potential and performance. This involves cleaning the dataset, normalizing data formats, and making it suitable for in-depth analysis.

## Objectives

- Clean and transform the FIFA 21 dataset to ensure consistency.
- Identify valuable players who are underpaid based on various metrics.

## Steps and Process

### 1. Data Cleaning and Preparation

- **Handled Missing Values**: Replaced missing values in the `Hits` column with the mean of non-missing values.
- **Normalized Numeric Values**: Converted string representations of numbers (e.g., "1.6K") to integers for ease of computation.
- **Standardized Data Types**: Ensured all values in the `Hits` column were of integer type.

### 2. Data Cleaning and Standardization of Units

- **Height and Weight Adjustments**:
  - Converted height measurements from feet/inches to centimeters.
  - Converted weight measurements from pounds to kilograms.
  - Updated data types for `Height` and `Weight` to integers, enabling easier analysis.

## Key Libraries

The project utilizes the following libraries:
- `pandas`: for data manipulation and cleaning.
- `numpy`: for numerical operations and transformations.
- `matplotlib` and `seaborn`: for data visualization and insights.

## Usage

1. **Clone the Repository**: Clone this repository to your local machine.
2. **Open the Notebook**: Launch the `fifa21.ipynb` notebook file in Jupyter Notebook or JupyterLab.
3. **Run the Cells**: Execute each cell sequentially to perform data cleaning, transformation, and exploration.

## Findings

After data processing, the analysis focuses on identifying players with valuable performance attributes who may be underpaid. The Visualizations help identify player valuation.

---
