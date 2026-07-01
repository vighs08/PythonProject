"""
==============================================================
  Village Workforce Connect
  Rural Employment Opportunity Management System
  Chanakya University - PPS Mini Project | B.Tech II Sem 2025-26
==============================================================
"""

import json
import os
from datetime import datetime

# ─────────────────────────────────────────────
#  FILE PATHS  (data stored as JSON files)
# ─────────────────────────────────────────────
USERS_FILE = "users.json"
JOBS_FILE  = "jobs.json"
APPS_FILE  = "applications.json"

# ─────────────────────────────────────────────
#  HELPER : Load / Save JSON
# ─────────────────────────────────────────────
def load_data(filepath):
    """Load JSON data from file; return empty list if file not found."""
    try:
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                return json.load(f)
    except Exception as e:
        print(f"[Warning] Could not load {filepath}: {e}")
    return []

def save_data(filepath, data):
    """Save data as JSON to file."""
    try:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"[Error] Could not save {filepath}: {e}")

# ─────────────────────────────────────────────
#  HELPER : ID generators
# ─────────────────────────────────────────────
def generate_user_id(users):
    return f"U{len(users) + 1:04d}"

def generate_job_id(jobs):
    return f"J{len(jobs) + 1:04d}"

def generate_app_id(apps):
    return f"A{len(apps) + 1:04d}"

# ─────────────────────────────────────────────
#  HELPER : Display separator
# ─────────────────────────────────────────────
def sep(char="─", width=55):
    print(char * width)

def header(title):
    sep("═")
    print(f"  {title}")
    sep("═")

# ══════════════════════════════════════════════
#  MODULE 1 : USER MANAGEMENT
# ══════════════════════════════════════════════

def register_user():
    """Register a new Employer or Worker."""
    header("USER REGISTRATION")
    users = load_data(USERS_FILE)

    name    = input("  Enter your full name        : ").strip()
    contact = input("  Enter contact number        : ").strip()
    village = input("  Enter your village/location : ").strip()

    print("  Select role:")
    print("    1. Employer / Job Provider")
    print("    2. Worker  / Job Seeker")
    role_choice = input("  Your choice (1/2)           : ").strip()

    if role_choice == "1":
        role = "employer"
    elif role_choice == "2":
        role = "worker"
    else:
        print("  [!] Invalid role choice. Registration cancelled.")
        return

    password = input("  Set a password              : ").strip()

    # Validate: no empty fields
    if not all([name, contact, village, password]):
        print("  [!] All fields are required. Registration cancelled.")
        return

    # Check duplicate contact
    for u in users:
        if u["contact"] == contact:
            print("  [!] A user with this contact number already exists.")
            return

    user_id = generate_user_id(users)
    user = {
        "user_id"  : user_id,
        "name"     : name,
        "contact"  : contact,
        "village"  : village,
        "role"     : role,
        "password" : password,
        "joined"   : datetime.now().strftime("%Y-%m-%d")
    }
    users.append(user)
    save_data(USERS_FILE, users)
    print(f"\n  ✔ Registration successful! Your User ID: {user_id}")


def login_user():
    """
    Validate credentials and return the user dict if successful,
    else return None.
    """
    header("LOGIN")
    users = load_data(USERS_FILE)

    contact  = input("  Contact number : ").strip()
    password = input("  Password       : ").strip()

    for u in users:
        if u["contact"] == contact and u["password"] == password:
            print(f"\n  ✔ Welcome back, {u['name']}! (Role: {u['role'].capitalize()})")
            return u

    print("  [!] Invalid credentials. Please try again.")
    return None


# ══════════════════════════════════════════════
#  MODULE 2 : JOB POSTING  (Employer only)
# ══════════════════════════════════════════════

def post_job(employer):
    """Create a new job posting."""
    header("POST A JOB")
    jobs = load_data(JOBS_FILE)

    title       = input("  Job Title                     : ").strip()
    description = input("  Work Description              : ").strip()
    work_type   = input("  Work Type (e.g. Harvesting)   : ").strip()
    workers_req = input("  Number of Workers Required    : ").strip()
    hours       = input("  Working Hours per day         : ").strip()
    wage        = input("  Wage / Salary (per day ₹)     : ").strip()
    location    = input("  Work Location / Village       : ").strip()
    start_date  = input("  Start Date (DD-MM-YYYY)       : ").strip()
    contact_inf = input("  Contact Information           : ").strip()
    notes       = input("  Additional Notes (optional)   : ").strip()

    if not all([title, description, work_type, workers_req, wage, location, start_date]):
        print("  [!] Required fields missing. Job not posted.")
        return

    try:
        workers_req = int(workers_req)
        float(wage)
    except ValueError:
        print("  [!] Workers Required and Wage must be numbers.")
        return

    job_id = generate_job_id(jobs)
    job = {
        "job_id"         : job_id,
        "employer_id"    : employer["user_id"],
        "employer_name"  : employer["name"],
        "title"          : title,
        "description"    : description,
        "work_type"      : work_type,
        "workers_required": workers_req,
        "working_hours"  : hours,
        "wage"           : wage,
        "location"       : location,
        "start_date"     : start_date,
        "contact_info"   : contact_inf,
        "notes"          : notes,
        "status"         : "Open",
        "posted_on"      : datetime.now().strftime("%Y-%m-%d")
    }
    jobs.append(job)
    save_data(JOBS_FILE, jobs)
    print(f"\n  ✔ Job posted successfully! Job ID: {job_id}")


def view_my_jobs(employer):
    """Employer views their own job postings."""
    header(f"MY JOB POSTINGS  [{employer['name']}]")
    jobs = load_data(JOBS_FILE)
    my_jobs = [j for j in jobs if j["employer_id"] == employer["user_id"]]

    if not my_jobs:
        print("  No jobs posted yet.")
        return my_jobs

    for j in my_jobs:
        sep()
        print(f"  Job ID    : {j['job_id']}  |  Status: {j['status']}")
        print(f"  Title     : {j['title']}")
        print(f"  Type      : {j['work_type']}  |  Location: {j['location']}")
        print(f"  Wage      : ₹{j['wage']}/day  |  Start: {j['start_date']}")
        print(f"  Workers   : {j['workers_required']}  |  Posted: {j['posted_on']}")
    sep()
    return my_jobs


def update_job(employer):
    """Employer updates an existing job posting."""
    my_jobs = view_my_jobs(employer)
    if not my_jobs:
        return

    job_id = input("\n  Enter Job ID to update : ").strip().upper()
    jobs   = load_data(JOBS_FILE)

    for i, j in enumerate(jobs):
        if j["job_id"] == job_id and j["employer_id"] == employer["user_id"]:
            print("  (Press ENTER to keep existing value)")
            title    = input(f"  Title [{j['title']}]: ").strip()
            wage     = input(f"  Wage  [{j['wage']}] : ").strip()
            location = input(f"  Location [{j['location']}]: ").strip()
            notes    = input(f"  Notes [{j['notes']}]: ").strip()

            if title:    jobs[i]["title"]    = title
            if wage:     jobs[i]["wage"]     = wage
            if location: jobs[i]["location"] = location
            if notes:    jobs[i]["notes"]    = notes

            save_data(JOBS_FILE, jobs)
            print("  ✔ Job updated successfully.")
            return

    print("  [!] Job ID not found or you don't own this job.")


def delete_job(employer):
    """Employer deletes a job posting."""
    my_jobs = view_my_jobs(employer)
    if not my_jobs:
        return

    job_id = input("\n  Enter Job ID to delete : ").strip().upper()
    jobs   = load_data(JOBS_FILE)

    for i, j in enumerate(jobs):
        if j["job_id"] == job_id and j["employer_id"] == employer["user_id"]:
            confirm = input(f"  Delete job '{j['title']}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                jobs.pop(i)
                save_data(JOBS_FILE, jobs)
                print("  ✔ Job deleted.")
            else:
                print("  Deletion cancelled.")
            return

    print("  [!] Job ID not found or you don't own this job.")


# ══════════════════════════════════════════════
#  MODULE 3 : JOB SEARCH & APPLICATION (Worker)
# ══════════════════════════════════════════════

def view_all_jobs():
    """Display all open job listings."""
    header("AVAILABLE JOBS")
    jobs = load_data(JOBS_FILE)
    open_jobs = [j for j in jobs if j["status"] == "Open"]

    if not open_jobs:
        print("  No open jobs available at the moment.")
        return open_jobs

    for j in open_jobs:
        sep()
        print(f"  Job ID    : {j['job_id']}")
        print(f"  Title     : {j['title']}")
        print(f"  Type      : {j['work_type']}")
        print(f"  Location  : {j['location']}")
        print(f"  Wage      : ₹{j['wage']}/day")
        print(f"  Workers   : {j['workers_required']} needed")
        print(f"  Start     : {j['start_date']}")
        print(f"  Contact   : {j['contact_info']}")
        print(f"  Notes     : {j['notes']}")
    sep()
    return open_jobs


def search_jobs():
    """Filter jobs by location, work type, or wage range."""
    header("SEARCH JOBS")
    print("  Filter by:")
    print("    1. Village / Location")
    print("    2. Work Type")
    print("    3. Wage Range")
    choice = input("  Your choice (1/2/3): ").strip()

    jobs      = load_data(JOBS_FILE)
    open_jobs = [j for j in jobs if j["status"] == "Open"]
    results   = []

    if choice == "1":
        keyword = input("  Enter village/location keyword: ").strip().lower()
        results = [j for j in open_jobs if keyword in j["location"].lower()]

    elif choice == "2":
        keyword = input("  Enter work type keyword       : ").strip().lower()
        results = [j for j in open_jobs if keyword in j["work_type"].lower()]

    elif choice == "3":
        try:
            min_w = float(input("  Minimum wage (₹/day)         : ").strip())
            max_w = float(input("  Maximum wage (₹/day)         : ").strip())
            results = [j for j in open_jobs
                       if min_w <= float(j["wage"]) <= max_w]
        except ValueError:
            print("  [!] Please enter valid numbers for wage range.")
            return
    else:
        print("  [!] Invalid choice.")
        return

    if not results:
        print("  No jobs found matching your criteria.")
        return

    print(f"\n  Found {len(results)} job(s):\n")
    for j in results:
        sep()
        print(f"  Job ID   : {j['job_id']}  |  {j['title']}")
        print(f"  Type     : {j['work_type']}  |  Location: {j['location']}")
        print(f"  Wage     : ₹{j['wage']}/day  |  Start: {j['start_date']}")
    sep()


def apply_for_job(worker):
    """Worker applies for a job."""
    view_all_jobs()
    job_id = input("\n  Enter Job ID to apply for : ").strip().upper()

    jobs = load_data(JOBS_FILE)
    apps = load_data(APPS_FILE)

    # Find job
    job = next((j for j in jobs if j["job_id"] == job_id), None)
    if not job:
        print("  [!] Job ID not found.")
        return
    if job["status"] != "Open":
        print("  [!] This job is no longer open.")
        return

    # Check duplicate application
    for a in apps:
        if a["job_id"] == job_id and a["worker_id"] == worker["user_id"]:
            print("  [!] You have already applied for this job.")
            return

    app_id = generate_app_id(apps)
    application = {
        "app_id"       : app_id,
        "job_id"       : job_id,
        "job_title"    : job["title"],
        "worker_id"    : worker["user_id"],
        "worker_name"  : worker["name"],
        "worker_contact": worker["contact"],
        "worker_village": worker["village"],
        "employer_id"  : job["employer_id"],
        "status"       : "Applied",
        "applied_on"   : datetime.now().strftime("%Y-%m-%d")
    }
    apps.append(application)
    save_data(APPS_FILE, apps)
    print(f"\n  ✔ Application submitted! Application ID: {app_id}")


def view_my_applications(worker):
    """Worker views their applications and statuses."""
    header(f"MY APPLICATIONS  [{worker['name']}]")
    apps = load_data(APPS_FILE)
    my_apps = [a for a in apps if a["worker_id"] == worker["user_id"]]

    if not my_apps:
        print("  No applications yet.")
        return

    for a in my_apps:
        sep()
        print(f"  App ID   : {a['app_id']}  |  Status : {a['status']}")
        print(f"  Job ID   : {a['job_id']}  |  Title  : {a['job_title']}")
        print(f"  Applied  : {a['applied_on']}")
    sep()


# ══════════════════════════════════════════════
#  MODULE 4 : JOB ASSIGNMENT & STATUS (Employer)
# ══════════════════════════════════════════════

def view_applications_for_job(employer):
    """Employer views all worker applications for their jobs."""
    header("WORKER APPLICATIONS")
    my_jobs = view_my_jobs(employer)
    if not my_jobs:
        return

    job_id = input("\n  Enter Job ID to view applications : ").strip().upper()

    # Verify employer owns the job
    if not any(j["job_id"] == job_id for j in my_jobs):
        print("  [!] Job not found in your postings.")
        return

    apps = load_data(APPS_FILE)
    job_apps = [a for a in apps if a["job_id"] == job_id]

    if not job_apps:
        print("  No applications received for this job yet.")
        return

    for a in job_apps:
        sep()
        print(f"  App ID  : {a['app_id']}  |  Status : {a['status']}")
        print(f"  Worker  : {a['worker_name']}  |  Contact: {a['worker_contact']}")
        print(f"  Village : {a['worker_village']}  |  Applied : {a['applied_on']}")
    sep()
    return job_apps


def assign_worker(employer):
    """Employer approves/assigns a worker application."""
    job_apps = view_applications_for_job(employer)
    if not job_apps:
        return

    app_id = input("\n  Enter Application ID to assign worker : ").strip().upper()
    apps   = load_data(APPS_FILE)
    jobs   = load_data(JOBS_FILE)

    for i, a in enumerate(apps):
        if a["app_id"] == app_id and a["employer_id"] == employer["user_id"]:
            apps[i]["status"] = "Assigned"
            save_data(APPS_FILE, apps)

            # Update job status to In Progress
            for k, j in enumerate(jobs):
                if j["job_id"] == a["job_id"]:
                    jobs[k]["status"] = "In Progress"
                    break
            save_data(JOBS_FILE, jobs)

            print(f"  ✔ Worker '{a['worker_name']}' has been assigned to the job.")
            return

    print("  [!] Application ID not found or not authorized.")


def mark_job_completed(employer):
    """Employer marks a job as completed."""
    view_my_jobs(employer)
    job_id = input("\n  Enter Job ID to mark as Completed : ").strip().upper()

    jobs = load_data(JOBS_FILE)
    for i, j in enumerate(jobs):
        if j["job_id"] == job_id and j["employer_id"] == employer["user_id"]:
            jobs[i]["status"] = "Completed"
            save_data(JOBS_FILE, jobs)

            # Update all assigned applications for this job
            apps = load_data(APPS_FILE)
            for k, a in enumerate(apps):
                if a["job_id"] == job_id and a["status"] == "Assigned":
                    apps[k]["status"] = "Completed"
            save_data(APPS_FILE, apps)

            print(f"  ✔ Job '{j['title']}' marked as Completed.")
            return

    print("  [!] Job ID not found or not authorized.")


# ══════════════════════════════════════════════
#  MODULE 5 : HISTORY & REPORTS
# ══════════════════════════════════════════════

def history_and_reports():
    """Display summary statistics."""
    header("HISTORY & REPORTS")
    jobs = load_data(JOBS_FILE)
    apps = load_data(APPS_FILE)

    total_jobs      = len(jobs)
    open_jobs       = sum(1 for j in jobs if j["status"] == "Open")
    in_progress     = sum(1 for j in jobs if j["status"] == "In Progress")
    completed_jobs  = sum(1 for j in jobs if j["status"] == "Completed")
    total_apps      = len(apps)
    total_assigned  = sum(1 for a in apps if a["status"] in ("Assigned", "Completed"))

    sep()
    print(f"  Total Jobs Posted      : {total_jobs}")
    print(f"  Open Jobs              : {open_jobs}")
    print(f"  Jobs In Progress       : {in_progress}")
    print(f"  Jobs Completed         : {completed_jobs}")
    sep()
    print(f"  Total Applications     : {total_apps}")
    print(f"  Workers Assigned       : {total_assigned}")
    sep()

    # Wage report: total wages for completed jobs
    total_wages = sum(float(j["wage"]) for j in jobs if j["status"] == "Completed")
    print(f"  Est. Total Wages Paid  : ₹{total_wages:.2f}")
    sep()

    # List completed jobs
    print("\n  Completed Jobs:")
    completed = [j for j in jobs if j["status"] == "Completed"]
    if completed:
        for j in completed:
            print(f"    [{j['job_id']}] {j['title']} | {j['location']} | ₹{j['wage']}/day")
    else:
        print("    None yet.")
    sep()


# ══════════════════════════════════════════════
#  WORKER  DASHBOARD
# ══════════════════════════════════════════════

def worker_dashboard(worker):
    while True:
        header(f"WORKER DASHBOARD  —  {worker['name']}")
        print("  1. View All Open Jobs")
        print("  2. Search / Filter Jobs")
        print("  3. Apply for a Job")
        print("  4. My Applications & Status")
        print("  5. History & Reports")
        print("  0. Logout")
        sep()
        choice = input("  Enter choice : ").strip()

        if   choice == "1": view_all_jobs()
        elif choice == "2": search_jobs()
        elif choice == "3": apply_for_job(worker)
        elif choice == "4": view_my_applications(worker)
        elif choice == "5": history_and_reports()
        elif choice == "0":
            print(f"\n  Goodbye, {worker['name']}!\n")
            break
        else:
            print("  [!] Invalid choice. Try again.")

        input("\n  Press ENTER to continue...")


# ══════════════════════════════════════════════
#  EMPLOYER  DASHBOARD
# ══════════════════════════════════════════════

def employer_dashboard(employer):
    while True:
        header(f"EMPLOYER DASHBOARD  —  {employer['name']}")
        print("  1. Post a New Job")
        print("  2. View My Job Postings")
        print("  3. Update a Job Posting")
        print("  4. Delete a Job Posting")
        print("  5. View Worker Applications")
        print("  6. Assign / Approve a Worker")
        print("  7. Mark Job as Completed")
        print("  8. History & Reports")
        print("  0. Logout")
        sep()
        choice = input("  Enter choice : ").strip()

        if   choice == "1": post_job(employer)
        elif choice == "2": view_my_jobs(employer)
        elif choice == "3": update_job(employer)
        elif choice == "4": delete_job(employer)
        elif choice == "5": view_applications_for_job(employer)
        elif choice == "6": assign_worker(employer)
        elif choice == "7": mark_job_completed(employer)
        elif choice == "8": history_and_reports()
        elif choice == "0":
            print(f"\n  Goodbye, {employer['name']}!\n")
            break
        else:
            print("  [!] Invalid choice. Try again.")

        input("\n  Press ENTER to continue...")


# ══════════════════════════════════════════════
#  MAIN MENU
# ══════════════════════════════════════════════

def main():
    while True:
        header("VILLAGE WORKFORCE CONNECT")
        print("  Rural Employment Opportunity Management System")
        sep()
        print("  1. Register")
        print("  2. Login")
        print("  3. View All Open Jobs (Guest)")
        print("  4. History & Reports  (Guest)")
        print("  0. Exit")
        sep()
        choice = input("  Enter choice : ").strip()

        if choice == "1":
            register_user()

        elif choice == "2":
            user = login_user()
            if user:
                if user["role"] == "employer":
                    employer_dashboard(user)
                elif user["role"] == "worker":
                    worker_dashboard(user)

        elif choice == "3":
            view_all_jobs()
            input("\n  Press ENTER to continue...")

        elif choice == "4":
            history_and_reports()
            input("\n  Press ENTER to continue...")

        elif choice == "0":
            print("\n  Thank you for using Village Workforce Connect. Goodbye!\n")
            break

        else:
            print("  [!] Invalid choice. Please try again.")


# ─────────────────────────────────────────────
if __name__ == "__main__":
    main()