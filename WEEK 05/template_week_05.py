"""
RECORD CHECK  -  my version
===========================

Name  : Faith George
Lane  :  AI    
Date  : 22/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS

over_rows_expected_count = 0
class Record:
    def __init__(self, dataset_name, rows_loaded, rows_expected):
        self.dataset_name = dataset_name
        self.rows_loaded = rows_loaded
        self. rows_expected = rows_expected

    def status (self):
        percent = (self.rows_loaded / self.rows_expected) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"
 
# ==================================================================== RECORDS

records = [
    Record ("Survey_01_2026", 1187, 1200),
    Record ("Survey_02_2026", 1010, 1200),
    Record ("Survey_03_2026", 1396, 1200)
]   # replace with your code
for d in records:
    print (d.dataset_name, ":", d.status())
    print ("="*30)

with open ("dataset.txt", "w") as dt:
    dt.write ("Survey_01_2026, 1187, 1200\n")
    dt.write ("Survey_02_2026, 1010, 1200\n")
    dt.write ("Survey_03_2026, 1396, 1200\n")

with open ("dataset.txt") as dt:
    for t in dt:
        dataset_name, rows_loaded, rows_expected = t.strip().split(",")
        rows_loaded =  float(rows_loaded)
        rows_expected = float (rows_expected)
        print ()
        print (f"Dataset name: {dataset_name}\n Rows loaded: {rows_loaded}\n Rows expected: {rows_expected}")

# ==================================================================== OUTPUT

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.dataset_name}")
    print("=" * 34)
    print("Dataset name: ", record.dataset_name)
    print("Rows loaded: ", record.rows_loaded)
    print("Rows expected:", record.rows_expected)
    print("Status: ", record.status())
if record.status() == "OVER LIMIT":
    over_rows_expected_count += 1
    
    print ("="*50)
    print ()
print ("The amount of rows loaded exceeding rows expected are: ",over_rows_expected_count)
print("=" * 70)


# ========================================================================