import os

print("--- DEBUG INFO ---")
print(f"1. Python is currently working in: {os.getcwd()}")
print("2. Here are the files I can see in this folder:")
files = os.listdir()
for f in files:
    print(f"   - {f}")

print("------------------")
if "Audit_Dataset_Master.xlsx" in files:
    print("SUCCESS: I found the file!")
else:
    print("FAILURE: The Excel file is NOT in the list above.")
    print("Please move the Excel file into the folder shown in Step 1.")