# Sheridan Datathon Project - 2025

![Sheridan Sigma Squad](Logo/SSS_Logo.png)

# Education as an Engine for Growth: Analyzing SDG #4

### Sheridan Datathon 2025 Team Project

![Project Status](https://img.shields.io/badge/Status-Active-green)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

This repository contains the work of our team for the **Sheridan Datathon 2025**. Our project focuses on **United Nations Sustainable Development Goal (SDG) #4: Quality Education**.

Using global educational and economic data, we aim to quantify the relationship between educational attainment (literacy rates, school enrollment, government expenditure) and economic stability (GDP, growth rates). This project demonstrates our ability to deliver business value through data analysis, statistical modeling, and team collaboration.

## The Team

| Name                      | Role                                 | GitHub Profile                                       |
| ------------------------- | ------------------------------------ | ---------------------------------------------------- |
| Ernani Fantinatti         | AI / ML / Data Engineer / Team Lead  | [@efantinatti](https://github.com/efantinatti)       |
| Broinson Jeyarajah        | Frontend / Backend                   | [@broin806](https://github.com/broin806)             |
| Youstina Botros           | Data Analyst / Python.               | [@Youstina1811](https://github.com/Youstina1811)     |
| Nguyen Anh Khoa Tran      | Data Analyst                         | [@David277353](https://github.com/David277353)       |
| Christian George-Igbinidu | UX / Frontend                        | [@Christiangbhub](https://github.com/Christiangbhub) |


## Website
![Sheridan Sigma Squad](https://sd.fantinatti.net)

---

## Business Case & Objective

**The Problem:**
While it is widely accepted that education is good for society, policymakers and NGOs (Non-Governmental Organizations) often struggle to determine _which specific_ educational investments yield the highest economic returns. Without clear data, funding may be misallocated.

**Our Objective:**
To analyze historical data to determine how specific "Quality Education" metrics (such as tertiary enrollment rates and literacy) correlate with and predict a nation's Economic Growth.

**Guiding Questions:**

- **Audience:** Government Education Ministries, The World Bank, and Global NGOs.
- **Key Question:** _To what extent does investment in quality education predict a nation's GDP growth over time?_
- **Business Value:** Providing data-driven insights to help stakeholders prioritize educational funding for maximum economic impact.

---

## The Dataset

We are utilizing the **"How Education Drives Economic Growth"** dataset sourced from Kaggle.

- **Source:** [Kaggle Link](https://www.kaggle.com/datasets/omarmohammed70/how-education-drives-economic-growth)
- **Description:** The dataset includes key indicators for various countries over a time series.
- **Key Features:**
  - `GDP`: Gross Domestic Product.
  - `Literacy Rate`: Percentage of the population that can read/write.
  - `School Enrollment`: Enrollment figures for primary, secondary, and tertiary levels.
  - `Government Expenditure`: Spending on education as a % of GDP.

> _Note: See the `data/raw` folder for the original dataset and `data/processed` for the cleaned version used for modeling._

---

## Repository Structure

We have organized our repository to ensure reproducibility and clean workflow management:

├── data
│   ├── processed      # Cleaned data used for analysis
│   ├── raw            # Original immutable data dump
│   └── sql            # SQL exports of data tables
├── experiments        # Notebooks for testing ideas (sandbox)
├── models             # Serialized models (pkl/joblib) and predictions
├── reports            # Generated analysis reports (HTML/PDF)
│   └── figures        # Saved PNGs of plots
├── src                # Source code for use in this project
│   ├── data_cleaning.py
│   ├── visualization.py
│   └── modeling.py
├── .gitignore         # Files to exclude (e.g., large data)
└── README.md          # Project documentation

-----

## Methodology

### 1\. Data Processing

  * **Cleaning:** Handled missing values in GDP and Literacy columns using [Method, e.g., forward-fill or mean imputation].
  * **Normalization:** Scaled economic features to account for vast differences in currency magnitude.
  * **Feature Engineering:** Created a "Quality Index" combining literacy and enrollment rates.

### 2\. Exploratory Data Analysis (EDA)

We explored relationships between variables using correlation matrices and scatter plots.

  * *Key Finding:* [e.g., We found a 0.78 correlation between Tertiary Enrollment and GDP per Capita].

### 3\. Modeling / Visualization

  * **Tools Used:** Python, Pandas, Scikit-Learn, Matplotlib/Seaborn.
  * **Approach:** [Describe if you used Linear Regression to predict GDP or Clustering to group countries by education level].

-----

## Key Insights & Deliverables

### Visualization Highlight

*Description: This chart demonstrates the positive trend between [Variable A] and [Variable B], indicating that...*

### Business Takeaways

1.  **Insight 1:** [e.g., Investment in primary education shows a delayed economic ROI of 5 years.]
2.  **Insight 2:** [e.g., Literacy rates above 90% are a prerequisite for reaching "High Income" status.]
3.  **Recommendation:** Stakeholders should prioritize [X] to maximize [Y].

-----

## Project Video

Each team member has reflected on the journey. Watch our project overview and individual reflections here:

  * **Project Showcase Video:** [Link to YouTube/Vimeo]
  * **Team Reflections:**
    \*
    \*
    \*
    \*

-----

## Reproducibility: Getting Started

To reproduce our findings, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/YourUsername/Sheridan-Datathon-2025-Education.git](https://github.com/YourUsername/Sheridan-Datathon-2025-Education.git)
    cd Sheridan-Datathon-2025-Education
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the analysis:**

      * To clean data: `python src/data_cleaning.py`
      * To generate plots: `python src/visualization.py`
      * To run models: `python src/modeling.py`

-----

## Collaboration & Workflow

  * **Git Strategy:** We utilized feature branches for every new task and mandated Pull Requests (PRs) with at least one peer review before merging into `main`.
  * **Communication:** Daily stand-ups via Slack to discuss blockers and progress.
  * **Task Management:** Used GitHub Projects to track "To Do," "In Progress," and "Done."

## Contact

For questions regarding this analysis, please reach out to the team via our GitHub profiles listed above.

-----

*For the Sheridan Datathon 2025.*