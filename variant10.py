printers = {
    "BW":    {"cost": 0.10},
    "Color": {"cost": 0.50}
}

# Format: {ID: {"quota": float, "role": str}}
users = {
    "U1": {"quota": 2.00, "role": "Student"},
    "U2": {"quota": 5.00, "role": "Staff"}    # Prints for free
}

jobs = [
    ("U1", "BW", 10),      # Valid. Cost: 1.00. Rem: 1.00.
    ("U2", "Color", 20),   # Valid. Cost: 0.00 (Staff). Rem: 5.00.
    ("U1", "Color", 10),   # Error: Cost 5.00 > 1.00.
    ("U9", "BW", 1),       # Error: User unknown.
    ("U1", "3D", 1),       # Error: Invalid printer type.
    ("U1", "BW", 0)        # Error: Page count must be positive integer.
]

def print_document(users_db, printer_config, user_id, printer_type, pages):
    if user_id not in users_db:
        raise KeyError ("User unknown")
    if printer_type not in printer_config:
        raise KeyError ("Invalid printer type")
    if type(pages)!=int or pages<1:
       raise ValueError ("Page count must be positive integer")
    
    user = users_db[user_id]
    cost_per_page =float(printer_config[printer_type]["cost"])
    total_cost = pages * cost_per_page

    if user["role"] =="Staff":
         total_cost=0.0
    if user["quota"] <total_cost:
          raise ValueError ("Insufficient quota")
    
    users_db[user_id]["quota"]-=total_cost
    return total_cost

def process_print_queue(users_db, printer_config, job_list):
    total_credits = 0
    failed_jobs = 0
    for user_id, printer_type, pages in job_list:
        try:
            cost = print_document(users_db, printer_config, user_id, printer_type, pages)
            total_credits += cost
        except Exception as e:
            print(f"Print Error for {user_id}: {e}")
            failed_jobs += 1
    return {"total_credits_burned": total_credits,
            "failed_jobs": failed_jobs}
result = process_print_queue(users, printers, jobs)
print(result)