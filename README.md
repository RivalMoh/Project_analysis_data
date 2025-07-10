# 🚲 Bike Rental Data Analysis & Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://projectanalysisdata-wtnefzmnscjcgyjvhzsr5l.streamlit.app/)

> A comprehensive data analysis project exploring bike rental patterns and trends across different seasons, months, and weather conditions, featuring an interactive Streamlit dashboard.

## � Project Overview

This project analyzes bike rental data from a bike-sharing system over two years (2011-2012) to uncover valuable business insights. The analysis focuses on understanding customer demographics, seasonal patterns, and weather impacts on bike rental demand.

### 🎯 Key Business Questions Addressed

1. **User Demographics**: What proportion of users are casual vs. registered customers?
2. **Seasonal Trends**: How does bike rental demand vary across different months and seasons?
3. **Weather Impact**: What weather conditions drive the highest bike rental volumes?
4. **Temporal Patterns**: When do we see peak and low rental periods?

## 📈 Key Findings & Insights

- **Customer Segmentation**: Analysis reveals the split between casual and registered users
- **Seasonal Patterns**: Clear seasonal variations in bike rental demand
- **Weather Correlation**: Strong correlation between weather conditions and rental volumes
- **Peak Performance**: Identification of high-demand periods for business optimization

## 🛠️ Technology Stack

- **Python**: Core programming language
- **Pandas**: Data manipulation and analysis
- **Matplotlib & Seaborn**: Data visualization
- **Streamlit**: Interactive web dashboard
- **Jupyter Notebook**: Data exploration and analysis
- **Statsmodels**: Statistical analysis

## 📁 Project Structure

```
📦 Bike_Rental_Analysis/
├── 📊 Project.ipynb           # Main analysis notebook
├── 📈 dashboard/              # Streamlit dashboard
│   ├── dashboard.py           # Dashboard application
│   ├── final_data.csv         # Processed dataset
│   ├── bike_logo.jpg          # Dashboard logo
│   └── requirements.txt       # Dashboard dependencies
├── 📄 bike_rental/            # Raw dataset
│   ├── day.csv               # Daily rental data
│   ├── hour.csv              # Hourly rental data
│   └── Readme.txt            # Dataset documentation
├── 📋 final_data.csv          # Processed dataset
├── 📝 requirements.txt        # Project dependencies
└── 🌐 url.txt                 # Live dashboard URL
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip or conda package manager

### Installation & Setup

#### Option 1: Using Conda (Recommended)

```bash
# Create a new conda environment
conda create --name bike_rental_analysis python=3.9

# Activate the environment
conda activate bike_rental_analysis

# Install dependencies
pip install -r requirements.txt
```

#### Option 2: Using Virtual Environment

```bash
# Create project directory
mkdir bike_rental_analysis
cd bike_rental_analysis

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 🎮 Running the Application

#### Launch Interactive Dashboard

```bash
# Navigate to dashboard directory
cd dashboard

# Run Streamlit application
streamlit run dashboard.py
```

The dashboard will open in your browser at `http://localhost:8501`

#### Explore Data Analysis

Open and run the Jupyter notebook:

```bash
jupyter notebook Project.ipynb
```

## 📊 Dashboard Features

### 🎛️ Interactive Controls
- **Date Range Selector**: Filter data by custom date ranges
- **Real-time Metrics**: Live updates of key performance indicators

### 📈 Visualizations
- **User Demographics**: Pie chart showing casual vs. registered users
- **Monthly Trends**: Line charts comparing rental patterns across 2011-2012
- **Seasonal Analysis**: Seasonal rental volume comparisons
- **Weather Impact**: Analysis of weather conditions on rental demand

### 🔢 Key Metrics
- Total casual users
- Total registered users
- Overall rental volume
- Monthly and seasonal breakdowns

## 📊 Dataset Information

### Data Source
- **Provider**: Hadi Fanaee-T, University of Porto
- **Period**: 2011-2012
- **Records**: 17,379 hourly records / 731 daily records
- **Features**: 16 variables including weather, temporal, and rental data

### Key Variables
- `dteday`: Date of rental
- `season`: Season (Spring, Summer, Fall, Winter)
- `weathersit`: Weather conditions (Clear, Mist, Light Rain/Snow, Heavy Rain/Snow)
- `temp`: Normalized temperature
- `casual`: Count of casual users
- `registered`: Count of registered users
- `cnt`: Total rental count

## 🔍 Analysis Highlights

### Business Intelligence
- **Peak Seasons**: Fall shows highest rental volumes
- **Weather Patterns**: Clear weather drives 70%+ of rentals
- **User Behavior**: Registered users dominate overall usage
- **Growth Trends**: 2012 showed significant growth over 2011

### Statistical Insights
- Strong correlation between temperature and rental demand
- Seasonal variations follow predictable patterns
- Weather conditions significantly impact daily rental volumes

## 🌐 Live Demo

Experience the interactive dashboard: [Bike Rental Dashboard](https://projectanalysisdata-wtnefzmnscjcgyjvhzsr5l.streamlit.app/)

## 📚 Dependencies

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
streamlit>=1.37.0
statsmodels>=0.13.0
babel>=2.15.0
```

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📄 License

This project uses the Bike Sharing Dataset provided by Hadi Fanaee-T and Joao Gama. Please cite the original work:

```
Fanaee-T, Hadi, and Gama, Joao, "Event labeling combining ensemble detectors and background knowledge", 
Progress in Artificial Intelligence (2013): pp. 1-15, Springer Berlin Heidelberg
```

## 📧 Contact

**Author**: Rival Moh. Wahyudi  
**Email**: vallllwhy@students.unnes.ac.id  
**ID Dicoding**: Rival Moh. Wahyudi

---

*Built with ❤️ for data-driven insights into bike sharing systems*
