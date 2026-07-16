# ==============================================================================
# PROJECT: Multi-Level Security Gate Pass System
# FILE: security_gate.py
# DESCRIPTION: A checkpoint simulator that validates usernames and clearance 
#              levels using only lists, loops, and conditional statements.
# ==============================================================================

# 1. Set up our authorized lists (our whitelists)
approved_users = ["bol", "alice", "john", "mercy"]
high_clearance_levels = ["admin", "root", "security"]

# We use this to track if the overall access is granted
access_granted = False

# 2. Level 1 Check: Verify Username
username_verified = False
while username_verified == False:
    print("\n--- LEVEL 1 CHECK: USERNAME VERIFICATION ---")
    name_input = input("Enter your username: ").strip().lower()

    if name_input in approved_users:
        print("[SUCCESS] Username recognized.")
        username_verified = True  # Exits the first loop
    else:
        print("[FAILED] Access Denied: User not in database. Try again.")

# 3. Level 2 Check: Verify Clearance Level
clearance_verified = False
while clearance_verified == False:
    print("\n--- LEVEL 2 CHECK: CLEARANCE LEVEL ---")
    print("Available clearances: Public, Guest, Admin, Root, Security")
    role_input = input("Enter your clearance level: ").strip().lower()

    if role_input in high_clearance_levels:
        print("[SUCCESS] Clearance authorized.")
        clearance_verified = True  # Exits the second loop
        access_granted = True      # Grants entry to the gate
    else:
        print("[WARNING] Low clearance level. You do not have gate privileges.")
        print("Would you like to re-enter your clearance level? (yes / no)")
        retry = input(">> ").strip().lower()
        
        # If they choose not to retry, we break out and lock them out
        if retry == "no":
            print("\n[TERMINATED] Exiting verification process.")
            clearance_verified = True # Exits the loop without granting access

# 4. Final Verification Gate
print("\n==============================================")
if access_granted == True:
    print(f"WELCOME BACK, {name_input.upper()}!")
    print("STATUS: [GATE OPENED] - Access Granted to the Secure Zone.")
else:
    print("STATUS: [GATE LOCKED] - Access Denied. Contact Admin.")
print("==============================================")