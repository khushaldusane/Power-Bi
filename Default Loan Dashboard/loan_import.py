import pandas as pd
import mysql.connector

# ==========================================
# 1. MYSQL CONNECTION
# ==========================================

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Khushal@2003",
    database="loan"
)

cursor = connection.cursor()

# ==========================================
# 2. READ CSV FILE
# ==========================================

csv_file = "loan.csv"

df = pd.read_csv(csv_file)

print("CSV loaded successfully!")
print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))

print("\nColumns:")
print(df.columns.tolist())

# ==========================================
# 3. CREATE MYSQL TABLE
# ==========================================

create_table = """
CREATE TABLE IF NOT EXISTS loans (
    LoanID VARCHAR(20),
    Age INT,
    Income INT,
    LoanAmount INT,
    CreditScore INT,
    MonthsEmployed INT,
    NumCreditLines INT,
    InterestRate DECIMAL(10,2),
    LoanTerm INT,
    DTIRatio DECIMAL(10,2),
    Education VARCHAR(100),
    EmploymentType VARCHAR(100),
    MaritalStatus VARCHAR(100),
    HasMortgage VARCHAR(10),
    HasDependents VARCHAR(10),
    LoanPurpose VARCHAR(100),
    HasCoSigner VARCHAR(10),
    `Default` INT,
    `Loan Date` VARCHAR(30)
)
"""

cursor.execute(create_table)

print("\nMySQL table created.")

# ==========================================
# 4. INSERT DATA
# ==========================================

insert_query = """
INSERT INTO loans (
    LoanID,
    Age,
    Income,
    LoanAmount,
    CreditScore,
    MonthsEmployed,
    NumCreditLines,
    InterestRate,
    LoanTerm,
    DTIRatio,
    Education,
    EmploymentType,
    MaritalStatus,
    HasMortgage,
    HasDependents,
    LoanPurpose,
    HasCoSigner,
    `Default`,
    `Loan Date`
)
VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s
)
"""

# Convert CSV rows directly into tuples
data = [tuple(row) for row in df.itertuples(index=False, name=None)]

# Insert all rows
cursor.executemany(insert_query, data)

# Save changes
connection.commit()

print("\n================================")
print("IMPORT SUCCESSFUL")
print("Rows imported:", cursor.rowcount)
print("================================")

# ==========================================
# 5. CLOSE CONNECTION
# ==========================================

cursor.close()
connection.close()

print("\nConnection closed.")