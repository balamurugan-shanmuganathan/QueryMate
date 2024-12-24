# QueryMate

**QueryMate** is a smart, interactive application that allows users to query and explore CSV files effortlessly using two powerful agent types:  
1. **Python DataFrame Agent**: For Python-based data manipulation using Pandas.  
2. **SQL Agent**: For SQL-like querying of your data.

With QueryMate, you can load CSV files, interact with the data, and gain insights quickly and intuitively.

---

## Features
- **CSV File Support**: Upload and explore CSV files with ease.  
- **Agent Selection**: Choose between Python DataFrame Agent and SQL Agent depending on your query style.  
- **Interactive Querying**: Enter natural-language queries or SQL commands to analyze your data dynamically.  
- **User-Friendly Interface**: Built with Streamlit for a smooth and intuitive user experience.  

---

## Getting Started

### Prerequisites
- Python 3.9 or later
- Install the required Python packages:
  ```bash
  pip install -r requirements.txt
  ```

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/QueryMate.git
   cd QueryMate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## Usage
1. Launch the app.
2. Upload a CSV file via the sidebar.
3. Select an agent type:
   - **Python DataFrame Agent**: Use natural language to query your data with Pandas.
   - **SQL Agent**: Write SQL queries directly to explore your data.
4. Enter your query in the provided input box.
5. View the results and insights instantly.

---

## Application Flow
1. **CSV Upload**: Drag and drop your CSV file into the uploader.
2. **Agent Selection**:
   - **Python DataFrame Agent**: Ideal for Python-style manipulations.
   - **SQL Agent**: Perfect for those who prefer SQL syntax.
3. **Query Execution**: Enter your query and execute it to see the results.

---

## Technologies Used
- **Streamlit**: For building the web interface.
- **LangChain**: To enable agent-based data querying.
- **Pandas**: For DataFrame manipulation.
- **SQLAlchemy**: For SQL-style queries.
- **Python**: The core programming language.

---

## Example Queries
  - "What is the total sales value in column 'Revenue'?"
  - "Show the top 5 rows sorted by 'Profit'."

---


