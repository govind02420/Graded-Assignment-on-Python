# 🧰 DevOps Python Automation Scripts

> A collection of **Python automation scripts** demonstrating essential **DevOps principles** — covering security, system monitoring, configuration management, and backup automation.

---

## 📂 Project Structure

```bash
DevOps_Python_Assignment/
│
├── Q1_password_checker.py       # Password strength validation script
├── Q2_cpu_monitor.py            # CPU usage monitoring tool
├── Q3_config_parser.py          # Configuration parser + REST API
├── Q4_backup.py                 # Automated file backup script
├── config.ini                   # Sample configuration file
└── README.md                    # Documentation file
```

---

## 🚀 Getting Started

### 🧩 Prerequisites

Make sure you have the following installed:
- **Python 3.8+**
- **pip** (Python package manager)

### 📦 Install Dependencies

Run the following command to install dependencies used in these scripts:
```bash
pip install psutil flask
```
---
## 🧱 Q1. Password Strength Checker

**File:** `Q1_password_checker.py`
### 🧠 Description
Validates a user’s password meets the required security standards.

**Validation criteria:**
- Minimum length: 8 characters  
- Uppercase & lowercase letters  
- At least one digit (0–9)  
- At least one special character (`!@#$%^&*()` etc.)


### ▶️ Run Command
```bash
python Q1_password_checker.py
```

### 💡 Example Output
```
Enter your password: MyPass@123
✅ Strong password! Your password meets all security criteria.
```

---

## 🧱 Q2. CPU Usage Monitor

**File:** `Q2_cpu_monitor.py`

### 🧠 Description
Monitors real-time CPU usage of your system.
Displays an **alert** if CPU usage exceeds **80%**.

### ▶️ Run Command
```bash
python Q2_cpu_monitor.py
```
### 💡 Example Output
```
Monitoring CPU usage... (Press Ctrl+C to stop)
Current CPU usage: 12.5%
Current CPU usage: 10.3%
⚠️ Alert! CPU usage exceeds threshold: 85%
⚠️ Alert! CPU usage exceeds threshold: 91%
```

### ⚙️ Notes
- Uses the `psutil` library.
- Press `Ctrl + C` to safely stop monitoring.

---

## 🧱 Q3. Configuration Parser + REST API

**File:** `Q3_config_parser.py`  
**Sample Config File:** `config.ini`

### 🧠 Description
This script automates **configuration management**:
- Reading `.ini` configuration files
- Extracting key-value pairs from [Database] and [Server] sections
- Saves the parsed data as a JSON file (simulating database storage)
- Exposing a **Flask REST API** to fetch the configuration as JSON (GET endpoint)

### ▶️ Run Command
```bash
python Q3_config_parser.py
```

### 🌐 Access via Browser
```
http://127.0.0.1:5000/get_config
```

### 📄 Sample `config.ini`
```
[Database]
host = localhost
port = 3306
username = admin
password = secret

[Server]
address = 192.168.0.1
port = 8080
```

### 💡 Example Console Output
```
✅ Configuration File Parser Results:
Database:
 - host: localhost
 - port: 3306
 - username: admin
 - password: secret
Server:
 - address: 192.168.0.1
 - port: 8080

💾 Data saved as config_data.json

🚀 Starting Flask API at http://127.0.0.1:5000/get_config
 * Serving Flask app 'config_parser'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
---


## 🧱 Q4. Backup Automation Script

**File:** `Q4_backup.py`
### 🧠 Description
Automates **file backups** to ensure data safety.

**Features:**
- Copies all files from source → destination
- If a file already exists, appends a timestamp to avoid overwriting
- Handles missing directories gracefully

### ▶️ Run Command
```bash
python Q4_backup.py <source_directory> <destination_directory>
```

### 💡 Example
```bash
python Q4_backup.py C:\Users\Govind\Documents\source C:\Users\Govind\Documents\backup
```

### 📤 Example Output
```
✅ Backed up: report.txt → C:\Users\Govind\Documents\backup\report.txt
✅ Backed up: data.csv → C:\Users\Govind\Documents\backup\data_20251017-200203.csv
```

---

## 🧩 Summary

```bash
| Task | Focus Area               | Key Modules Used                | Output Type       |
| ---- | ------------------------ | ------------------------------- | ----------------- |
| Q1   | Security                 | `re` (Regex)                    | Console Feedback  |
| Q2   | Monitoring               | `psutil`, `time`                | Continuous Alerts |
| Q3   | Configuration Management | `configparser`, `flask`, `json` | REST API + JSON   |
| Q4   | Backup Automation        | `os`, `shutil`, `time`          | File Copy Logs    |
```
---

## 🛡️ Error Handling

Each script includes error handling for:
- Invalid user inputs
- Missing files or directories  
- File read/write issues  
- Exception handling with safe program exit  
- Graceful shutdown via keyboard interrupt (Ctrl+C)

---


## 🪪 License

This project is licensed under the **MIT License** — you’re free to modify and distribute it.

---

### 🖼️ Preview

> Secure • Monitor • Configure • Backup — all in one place.

