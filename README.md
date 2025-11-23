# Sheridan Datathon Project - 2025

# Education as an Engine for Growth: Analyzing SDG \#4

### Sheridan Datathon 2025 Team Project

## Overview

This repository contains the work of our team for the **Sheridan Datathon 2025**. Our project focuses on **United Nations Sustainable Development Goal (SDG) \#4: Quality Education**.

Using global educational and economic data, we aim to quantify the relationship between educational attainment (literacy rates, school enrollment, government expenditure) and economic stability (GDP, growth rates). This project demonstrates our ability to deliver business value through data analysis, statistical modeling, and team collaboration.

## The Team

| Name | Role | GitHub Profile |
| :--- | :--- | :--- |
| Ernani Fantinatti | AI / ML / Data Engineer / Team Lead | [@efantinatti](https://github.com/efantinatti) |
| Broinson Jeyarajah | Frontend / Backend | [@broin806](https://github.com/broin806) |
| Youstina Botros | Data Analyst / Python | [@Youstina1811](https://github.com/Youstina1811) |
| Nguyen Anh Khoa Tran | Data Analyst | [@David277353](https://github.com/David277353) |
| Christian George-Igbinidu | UX / Frontend | [@Christiangbhub](https://github.com/Christiangbhub) |

## Website

[Sheridan Sigma Squad](https://sd.fantinatti.net)

-----

## Business Case & Objective

**The Problem:**
While it is widely accepted that education is good for society, policymakers and NGOs (Non-Governmental Organizations) often struggle to determine *which specific* educational investments yield the highest economic returns. Without clear data, funding may be misallocated.

**Our Objective:**
To analyze historical data to determine how specific "Quality Education" metrics (such as tertiary enrollment rates and literacy) correlate with and predict a nation's Economic Growth.

**Guiding Questions:**

  * **Audience:** Government Education Ministries, The World Bank, and Global NGOs.
  * **Key Question:** *To what extent does investment in quality education predict a nation's GDP growth over time?*
  * **Business Value:** Providing data-driven insights to help stakeholders prioritize educational funding for maximum economic impact.

-----

## The Dataset

We are utilizing the **"How Education Drives Economic Growth"** dataset sourced from Kaggle, containing data on **191 countries**.

  * **Source:** [Kaggle Link](https://www.kaggle.com/datasets/omarmohammed70/how-education-drives-economic-growth)
  * **Description:** The dataset includes key indicators for various countries over a time series.
  * **Key Metrics:**
      * **Social:** `Literacy Rate`, `Physician Density`, `School Enrollment`.
      * **Economic:** `GDP`, `GDP Growth`, `GDP per Capita`, `Unemployment Rate`, `Government Expenditure`.
  * **Categorical Data:** `Continent`, `GDP per Capita Category` (Very Low, Low, Mid, High).

> *Note: See the `Dataset` folder for the original csv files.*

-----

## Repository Structure

We have organized our repository to ensure reproducibility and clean workflow management:

```text
├── app.py                     # Main application entry point
├── Dataset
│   ├── archive.zip            # Original compressed dataset
│   └── education-economy-data.csv  # Working dataset
├── EDA
│   ├── EDA.ipynb              # Exploratory Data Analysis notebook
│   └── Figures                # Generated plots and visualizations
├── Logo
│   └── SSS_Logo.png           # Team logo
├── src
│   └── gemini_agent.py        # Logic for AI agent integration
├── templates
│   └── index.html             # Web application template
├── requirements.txt           # Python dependencies
├── service_account_key.json   # Cloud credentials
└── README.md                  # Project documentation
````

-----

## Methodology

### 1\. AI-Powered Data Processing

Instead of static data cleaning scripts, we have implemented a dynamic processing engine using **Gemini 2.5 with Vertex AI**.

  * **Conversational Interface:** Users can ask questions about the data in a completely human, natural way (e.g., *"Show me the correlation between literacy and GDP in Asia"*).
  * **On-the-Go Processing:** The AI agent interprets these queries in real-time, performs the necessary data filtering, cleaning, and calculations instantly, and returns the results. This allows for fluid, unstructured exploration of the dataset without pre-defined constraints.

### 2\. Exploratory Data Analysis (EDA)

We explored relationships between variables using correlation matrices and scatter plots to understand the global landscape.

-----

## Key Insights & Deliverables

### 1\. Visual Analysis & Findings

We generated several key visualizations to understand the global landscape:

  * **Distributions of Key Indicators:**

      * **Literacy:** Skewed heavily towards 100%. While most of the world is literate, the "tail" (countries with \<60% literacy) represents areas requiring significant educational infrastructure planning.
      * **GDP per Capita:** Highly unequal. Most nations are clustered at the lower end, with a few wealthy outliers.
      * **Unemployment:** Mostly concentrated below 10%, but with a long tail of nations facing severe unemployment crises.

  * **Correlation Heatmap:**

      * **Strong Positive Correlation:** Literacy Rate vs. Physician Density (0.5+) and GDP per Capita (0.4+). This validates that educated populations tend to have better healthcare and economic outcomes—key pillars for a "Smart City" or developed urban area.
      * **Unemployment:** Weak negative correlation with Literacy. Education helps, but it is not the only factor in solving unemployment.

  * **The "Development Curve" (Literacy vs. GDP per Capita):**

      * **Insight:** There is a clear threshold. Countries typically need to hit **\~80-90% literacy** before they see exponential growth in GDP per Capita.
      * **Relevance:** For developing regions (often in Africa/Asia), the priority is not just "building offices" (economic zones) but "building schools" (social infrastructure) to unlock that growth potential.

  * **Unemployment by Economic Status:**

      * **Insight:** Wealthier nations (High category) generally have lower and more stable unemployment rates. However, the Low and Very Low categories show massive volatility—some poor nations have low unemployment (likely subsistence/informal labor), while others have very high rates.

### 2\. Strategic Implications: Urban Planning

Since our challenge focuses on Predictive Analytics in Urban Planning, we framed our data to address specific planning challenges:

  * **Infrastructure Allocation:** Using Physician Density and Literacy Rate as proxies for Social Infrastructure demand. High GDP but low Physician Density indicates a "rich but under-serviced" urban area needing hospital zoning.
  * **Zoning for Jobs (Economic Zones):** Analyzing Unemployment Rate vs. GDP Growth. High unemployment combined with High GDP growth suggests "jobless growth" (potentially resource extraction). Urban planning here requires mixed-use zoning to encourage SMEs and service jobs, not just industrial plants.
  * **Targeting Intervention:** Grouping countries into "Urban Development Phases" (e.g., "Emerging," "Transitioning," "Mature") using clustering to apply different urban planning playbooks.

### 3\. Future Roadmap: Predictive Models

To further the "Predictive" aspect of the challenge, we recommend the following models:

  * **Predicting "Brain Drain" (Migration Pressure):**
      * *Hypothesis:* Low GDP + High Unemployment + High Literacy = High potential for skilled migration.
      * *Model:* Create a "Migration Risk Score" based on these features.
  * **The "Next Tiger" Prediction:**
      * Predict which "Low" or "Mid" income countries are about to jump to "High" based on their Literacy and GDP Growth trajectory to identify the next hotspots for urbanization.
  * **Resource Planning Model:**
      * Use GDP and Population (derived from GDP/GDP per Capita) to predict future demand for physicians/hospitals, guiding health infrastructure planning.

-----

## Project Video

Watch our project overview and showcase here:

  * **Project Showcase Video:** [Link to YouTube/Vimeo]

-----

## Reproducibility: Getting Started

To reproduce our findings, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/efantinatti/DFG-SD.git](https://github.com/efantinatti/DFG-SD.git)
    cd DFG-SD
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the analysis:**

      * **Exploratory Analysis:** Open and run `EDA/EDA.ipynb` in Jupyter Notebook/Lab to see the data cleaning and visualization steps.
      * **Run the Application:** Start the web interface by running:
        ```bash
        python app.py
        ```

-----

## Collaboration & Workflow

  * **Git Strategy:** We utilized feature branches for every new task and mandated Pull Requests (PRs) with at least one peer review before merging into `main`.
  * **Communication:** Daily stand-ups via Slack to discuss blockers and progress.
  * **Task Management:** Used GitHub Projects to track "To Do," "In Progress," and "Done."

## Contact

For questions regarding this analysis, please reach out to the team via our GitHub profiles listed above.

-----

*For the Sheridan Datathon 2025.*