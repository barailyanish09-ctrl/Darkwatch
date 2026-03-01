# 🕵️ DarkWatch — Dark Web Awareness Tool

> **ST4017CMD — Introduction to Programming**  
> Softwarica College of IT & E-Commerce | Coventry University

A Python-based dark web awareness and education tool featuring a GUI built with Tkinter.

---

## 🚀 Run in GitHub Codespaces (Recommended)

**Step 1:** Click the green **`< > Code`** button on this repository page  
**Step 2:** Click the **`Codespaces`** tab  
**Step 3:** Click **`Create codespace on main`**  
**Step 4:** Wait ~2 minutes for the environment to build  
**Step 5:** A browser tab will open automatically — this is your **virtual desktop**  
**Step 6:** In the Codespaces terminal at the bottom, type:

```bash
DISPLAY=:1 python3 darkwatch.py
```

**Step 7:** The DarkWatch app will appear on the virtual desktop in your browser! ✅

> 🔑 **Desktop password:** `darkwatch`

---

## 💻 Run Locally (On Your Own Computer)

Make sure Python 3 is installed, then:

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Navigate into the folder
cd YOUR_REPO_NAME

# Run the tool
python darkwatch.py
```

> ✅ No extra libraries needed — uses Python standard library only!

---

## 🛠 Features

| Feature | Description |
|---|---|
| 🌐 About Dark Web | Learn about Surface, Deep & Dark Web layers, Tor, and threats |
| 🔐 Password Checker | Real-time strength analyser with 5 security checks |
| 🔑 Password Generator | Generate strong 16-character random passwords |
| #️⃣ SHA-1 Demo | See how k-anonymity works in real breach APIs |
| 📧 Breach Checker | Simulated email breach scanner with terminal output |
| 🧠 Awareness Quiz | 6-question interactive dark web knowledge quiz |
| 🛡️ Protection Tips | 8 actionable tips to stay safe online |

---

## 📁 Project Structure

```
📦 darkwatch/
 ┣ 📄 darkwatch.py          ← Main Python application
 ┣ 📄 README.md             ← This file
 ┗ 📁 .devcontainer/
    ┗ 📄 devcontainer.json  ← GitHub Codespaces configuration
```

---

## 🧱 Custom Data Structures Used

- **Stack** — LIFO structure for tracking user action history
- **LinkedList** — Singly linked list for storing quiz questions

---

## ⚠️ Disclaimer

This tool is created for **educational purposes only** as part of the ST4017CMD module.  
The breach checker is a **simulated demonstration** — it does not connect to real APIs.  
Do not use this tool for any unlawful or unethical purposes.

---

## 📚 Module Information

- **Module:** ST4017CMD — Introduction to Programming  
- **College:** Softwarica College of IT & E-Commerce  
- **Partner University:** Coventry University  
- **Due Date:** 1st March, 2026
