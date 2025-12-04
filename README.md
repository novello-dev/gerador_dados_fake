# Fake Data Generator (Streamlit)

A simple and practical fake data generator brewed with **Python + Streamlit + Faker**.  
I built this project for my personal studies, but then I decided to upload it to GitHub to save it, document it, and leave it public for it may be useful for other people who need to generate data quickly.

---

## Features

- Fake data generation for three areas:
  - **Sales**
  - **Health**
  - **HR**
- Configurable quantity (10 to 1000 rows)
- Direct visualization in the Streamlit interface
- CSV data download
- Various fields to simulate real scenarios (names, dates, products, specialties, salaries, etc.)

---

## Tech stack

- **Python 3.11**
- **Streamlit**
- **Pandas**
- **Faker**

---

## How to install and run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USER/gerador_dados_fake.git
cd gerador_dados_fake
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Streamlit

```bash
streamlit run app.py
```

The app will automatically open in your browser.

---

## Why this project?

I work with data all the time and noticed that I often need fake records for:

- tests  
- studies  
- prototypes  
- feeding other scripts  
- playing with visualizations  

So I decided to create my own generator, and now I’m making it available on GitHub to keep it safe and maybe help someone else.

---

## Possible future improvements

- Generate Excel/XLSX
- Export JSON
- Create dashboard with charts
- Add more areas (finance, marketing, logistics…)
- Online deployment (Streamlit Cloud / HuggingFace)

If you'd like to contribute to any of these ideas, feel free!

---

## Contributions

Contributions are welcome!  
Open an issue, send suggestions, ideas, pull requests… anything is appreciated!

---

## License

This project is free for educational and personal use.  
You may use, modify, improve, and distribute it as you wish.
