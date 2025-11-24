import pandas as pd
import re
import os

# --- CONFIGURATION ---
PATTERNS = {
    "PII_EMAIL": r'[\w\.-]+@[\w\.-]+\.\w+',
    "PII_PHONE": r'(\+91[\-\s]?)?[6-9]\d{9}',
    "SECRET_KEY": r'(sk-[a-zA-Z0-9]{20,})|(AKIA[0-9A-Z]{16})', 
    "CREDENTIAL_PASS": r'(password|passwd|pwd)\s*=\s*[\'"][^\'"]+[\'"]',
    "TOXIC_CONTENT": r'(bomb|hack|kill|hate)'
}

def scan_prompt(text):
    text = str(text)
    violations = []
    for rule_name, pattern in PATTERNS.items():
        if re.search(pattern, text, re.IGNORECASE):
            violations.append(rule_name)
            text = re.sub(pattern, f"[{rule_name}_REDACTED]", text, flags=re.IGNORECASE)

    if violations:
        return False, ", ".join(violations), text
    return True, "None", text

def run_audit():
    # 1. Look for the CSV file
    input_file = "data.csv"
    
    # DEBUG: Check if file exists before crashing
    if not os.path.exists(input_file):
        print(f"ERROR: I cannot find '{input_file}'.")
        print(f"Please make sure you saved the Excel file as CSV in: {os.getcwd()}")
        return

    print(f"Loading Audit Dataset from {input_file}...")
    
    # 2. Read CSV (No openpyxl needed!)
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    print(f"Scanning {len(df)} rows...")

    df['Agent_Decision'] = ""
    df['Agent_Reason'] = ""
    df['Sanitized_Prompt'] = ""

    for index, row in df.iterrows():
        # Handle case where column names might be slightly different
        prompt_text = row.get('Raw_Prompt', row.iloc[1]) # Try name first, then index 1
        
        is_safe, violation, clean_text = scan_prompt(prompt_text)
        
        df.at[index, 'Agent_Decision'] = "APPROVED" if is_safe else "BLOCKED"
        df.at[index, 'Agent_Reason'] = violation
        df.at[index, 'Sanitized_Prompt'] = clean_text

    blocked_count = len(df[df['Agent_Decision'] == 'BLOCKED'])
    print(f"Audit Complete! Blocked {blocked_count} unsafe prompts.")
    
    # 3. Save as CSV
    output_file = "Audit_Results_Final.csv"
    df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    run_audit()