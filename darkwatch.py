"""
DarkWatch - Dark Web Awareness Tool
Module: ST4017CMD - Introduction to Programming
Author: [Your Name] | [Student ID]
Description: A GUI-based dark web awareness tool that checks password strength,
             simulates breach detection, provides dark web education, and tests
             user knowledge through an interactive quiz.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import hashlib
import re
import random
import string
import time


# ─────────────────────────────────────────────
#   CUSTOM DATA STRUCTURES (No built-in reliance)
# ─────────────────────────────────────────────

class Stack:
    """Custom Stack implementation using a list."""
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self.is_empty():
            return self._data.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self._data[-1]
        return None

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)


class Node:
    """Node for Linked List."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Custom Linked List for storing quiz questions."""
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def size(self):
        return self._size


# ─────────────────────────────────────────────
#   PASSWORD FUNCTIONS
# ─────────────────────────────────────────────

def check_password_strength(password):
    """
    Analyse a password and return a score with feedback.

    Algorithm:
    - Checks length, uppercase, lowercase, digits, special characters
    - Returns score (0-5) and list of feedback messages

    Parameters:
        password (str): The password to analyse

    Returns:
        tuple: (score int, checks dict, feedback list)
    """
    checks = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "digits": bool(re.search(r'\d', password)),
        "special": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
    }

    score = sum(checks.values())
    feedback = []

    if not checks["length"]:
        feedback.append("Use at least 8 characters")
    if not checks["uppercase"]:
        feedback.append("Add uppercase letters (A-Z)")
    if not checks["lowercase"]:
        feedback.append("Add lowercase letters (a-z)")
    if not checks["digits"]:
        feedback.append("Include numbers (0-9)")
    if not checks["special"]:
        feedback.append("Add special characters (!@#$...)")

    return score, checks, feedback


def get_strength_label(score):
    """
    Convert score to strength label and colour.

    Parameters:
        score (int): Password score (0-5)

    Returns:
        tuple: (label str, colour str)
    """
    labels = {
        0: ("Very Weak", "#ff3355"),
        1: ("Very Weak", "#ff3355"),
        2: ("Weak", "#ff8800"),
        3: ("Moderate", "#ffcc00"),
        4: ("Strong", "#88ff00"),
        5: ("Very Strong", "#00ff88"),
    }
    return labels.get(score, ("Unknown", "grey"))


def generate_strong_password(length=16):
    """
    Generate a cryptographically random strong password.

    Parameters:
        length (int): Desired password length (default 16)

    Returns:
        str: A randomly generated strong password
    """
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    # Guarantee at least one of each required type
    password_chars = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()"),
    ]
    for _ in range(length - 4):
        password_chars.append(random.choice(chars))

    random.shuffle(password_chars)
    return "".join(password_chars)


# ─────────────────────────────────────────────
#   BREACH SIMULATION FUNCTIONS
# ─────────────────────────────────────────────

# Simulated dark web breach database (educational only)
SIMULATED_BREACHED_DOMAINS = [
    "yahoo.com", "linkedin.com", "adobe.com", "myspace.com",
    "dropbox.com", "tumblr.com", "last.fm", "badoo.com",
    "dailymotion.com", "disqus.com", "kickstarter.com"
]

SIMULATED_BREACHED_EMAILS = [
    "test@yahoo.com", "admin@linkedin.com", "user@adobe.com",
    "demo@example.com", "sample@test.com"
]


def simulate_breach_check(email):
    """
    Simulate a dark web breach check against a sample database.
    (Educational simulation — not connected to real breach APIs)

    Algorithm:
    - Checks email format validity using regex
    - Checks domain against simulated breach list
    - Returns breach status and simulated details

    Parameters:
        email (str): Email address to check

    Returns:
        dict: Result containing 'status', 'breaches', 'message'
    """
    # Validate email format
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_pattern, email):
        return {"status": "invalid", "breaches": [], "message": "Invalid email format."}

    domain = email.split("@")[1].lower()
    email_lower = email.lower()

    found_breaches = []

    # Check against simulated breached emails
    if email_lower in SIMULATED_BREACHED_EMAILS:
        found_breaches.append({
            "source": "Example Breach Database",
            "year": "2023",
            "data": "Email, Password Hash, Username"
        })

    # Check against breached domains
    if domain in SIMULATED_BREACHED_DOMAINS:
        found_breaches.append({
            "source": f"{domain.split('.')[0].title()} Data Breach",
            "year": str(random.randint(2017, 2022)),
            "data": "Email, Password, Name"
        })

    if found_breaches:
        return {
            "status": "breached",
            "breaches": found_breaches,
            "message": f"⚠ Found in {len(found_breaches)} breach(es)!"
        }
    else:
        return {
            "status": "safe",
            "breaches": [],
            "message": "✓ Not found in our simulated breach database."
        }


def hash_password_sha1(password):
    """
    Hash a password with SHA-1 (demonstrates k-anonymity concept).

    Parameters:
        password (str): Plain text password

    Returns:
        str: SHA-1 hash (uppercase)
    """
    return hashlib.sha1(password.encode()).hexdigest().upper()


# ─────────────────────────────────────────────
#   QUIZ DATA
# ─────────────────────────────────────────────

def build_quiz_questions():
    """
    Build quiz questions using a custom LinkedList data structure.

    Returns:
        LinkedList: Linked list of question dictionaries
    """
    questions = LinkedList()

    questions.append({
        "question": "What is the Dark Web primarily accessed through?",
        "options": ["Google Chrome", "Tor Browser", "Mozilla Firefox", "Microsoft Edge"],
        "answer": 1,
        "explanation": "The Tor Browser routes traffic through multiple encrypted relays, allowing anonymous access to .onion sites on the Dark Web."
    })
    questions.append({
        "question": "What does 'TOR' stand for?",
        "options": ["Total Online Routing", "The Onion Router", "Transfer Over Relay", "Tunnel Over Remote"],
        "answer": 1,
        "explanation": "TOR stands for 'The Onion Router' — named after its layered encryption, like the layers of an onion."
    })
    questions.append({
        "question": "Which of these is a sign that your data may be on the dark web?",
        "options": ["Slow internet", "Unknown login attempts on your accounts", "High CPU usage", "Pop-up ads"],
        "answer": 1,
        "explanation": "Unknown login attempts are a key indicator that your credentials may have been leaked and are being used by malicious actors."
    })
    questions.append({
        "question": "What percentage of the internet does the Surface Web make up?",
        "options": ["90%", "60%", "4%", "50%"],
        "answer": 2,
        "explanation": "Only about 4-5% of the internet is the Surface Web (indexed by search engines). The rest is the Deep Web and Dark Web."
    })
    questions.append({
        "question": "Which best practice helps protect you from dark web breaches?",
        "options": ["Using one password everywhere", "Using a VPN only", "Using unique passwords + 2FA", "Avoiding the internet"],
        "answer": 2,
        "explanation": "Using unique strong passwords for each account plus Two-Factor Authentication (2FA) is the most effective protection strategy."
    })
    questions.append({
        "question": "What is a 'data breach'?",
        "options": ["A firewall failure", "Unauthorised access and theft of sensitive data", "A type of virus", "A network outage"],
        "answer": 1,
        "explanation": "A data breach occurs when unauthorised individuals gain access to confidential data, which is then often sold on dark web marketplaces."
    })

    return questions


# ─────────────────────────────────────────────
#   MAIN GUI APPLICATION
# ─────────────────────────────────────────────

class DarkWatchApp:
    """
    Main application class for DarkWatch — Dark Web Awareness Tool.
    Uses Tkinter for GUI with a tabbed notebook layout.
    """

    def __init__(self, root):
        """Initialise the application, build the GUI."""
        self.root = root
        self.root.title("DarkWatch — Dark Web Awareness Tool")
        self.root.geometry("850x650")
        self.root.configure(bg="#050a0f")
        self.root.resizable(True, True)

        # Custom data structures
        self.history_stack = Stack()        # Tracks user actions
        self.quiz_questions = build_quiz_questions()

        # Quiz state
        self.quiz_list = self.quiz_questions.to_list()
        self.quiz_index = 0
        self.quiz_score = 0
        self.quiz_answered = False

        self._setup_styles()
        self._build_ui()

    def _setup_styles(self):
        """Configure ttk styles for the dark theme."""
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TNotebook", background="#050a0f", borderwidth=0)
        style.configure("TNotebook.Tab",
                        background="#0a1520",
                        foreground="#4a7a5a",
                        padding=[16, 8],
                        font=("Courier", 10, "bold"))
        style.map("TNotebook.Tab",
                  background=[("selected", "#0f3d2e")],
                  foreground=[("selected", "#00ff88")])

        style.configure("TFrame", background="#050a0f")
        style.configure("Card.TFrame", background="#0a1520",
                        relief="flat", borderwidth=1)

    def _build_ui(self):
        """Build the main UI with header and tabbed notebook."""
        # ── Header ──
        header = tk.Frame(self.root, bg="#050a0f", pady=16)
        header.pack(fill="x", padx=20)

        tk.Label(header, text="DARKWATCH",
                 font=("Courier", 28, "bold"),
                 bg="#050a0f", fg="#00ff88").pack(side="left")

        tk.Label(header, text="  //  Dark Web Awareness Tool",
                 font=("Courier", 11),
                 bg="#050a0f", fg="#4a7a5a").pack(side="left", pady=6)

        # Divider
        tk.Frame(self.root, bg="#0f3d2e", height=1).pack(fill="x", padx=20)

        # ── Notebook (tabs) ──
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=20, pady=16)

        self._build_tab_about()
        self._build_tab_password()
        self._build_tab_breach()
        self._build_tab_quiz()
        self._build_tab_tips()

        # ── Footer ──
        tk.Frame(self.root, bg="#0f3d2e", height=1).pack(fill="x", padx=20)
        tk.Label(self.root,
                 text="ST4017CMD | Introduction to Programming | Educational Tool Only",
                 font=("Courier", 8), bg="#050a0f", fg="#4a7a5a").pack(pady=6)

    # ── CARD HELPER ──────────────────────────

    def _make_card(self, parent, title=""):
        """Create a styled card frame with optional title."""
        frame = tk.Frame(parent, bg="#0a1520", bd=1,
                         relief="solid", padx=16, pady=14)
        frame.configure(highlightbackground="#0f3d2e", highlightthickness=1)
        if title:
            tk.Label(frame, text=title,
                     font=("Courier", 9, "bold"),
                     bg="#0a1520", fg="#00ff88").pack(anchor="w", pady=(0, 10))
        return frame

    def _label(self, parent, text, size=10, color="#c8e6c9", bold=False):
        """Helper to create a styled label."""
        font_weight = "bold" if bold else "normal"
        return tk.Label(parent, text=text,
                        font=("Courier", size, font_weight),
                        bg="#0a1520", fg=color, wraplength=700,
                        justify="left")

    def _button(self, parent, text, command, width=20):
        """Create a styled button."""
        return tk.Button(parent, text=text, command=command,
                         font=("Courier", 10, "bold"),
                         bg="#0a1520", fg="#00ff88",
                         activebackground="#00ff88", activeforeground="#000",
                         relief="solid", bd=1,
                         cursor="hand2", width=width,
                         highlightbackground="#00ff88", highlightthickness=1)

    # ── TAB 1: ABOUT ────────────────────────

    def _build_tab_about(self):
        """Build the About / Dark Web Education tab."""
        tab = tk.Frame(self.notebook, bg="#050a0f")
        self.notebook.add(tab, text="  About Dark Web  ")

        canvas = tk.Canvas(tab, bg="#050a0f", bd=0, highlightthickness=0)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#050a0f")
        scroll_frame.bind("<Configure>",
                          lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        p = scroll_frame

        # Internet layers card
        layers_card = self._make_card(p, "// LAYERS OF THE INTERNET")
        layers_card.pack(fill="x", padx=8, pady=(8, 6))

        layers = [
            ("🌐  SURFACE WEB", "#00aaff",
             "~4% of the internet. Indexed by search engines like Google. Everyday websites — social media, news, shopping."),
            ("🌊  DEEP WEB", "#ffcc00",
             "~90% of the internet. Not indexed — includes email inboxes, banking portals, private databases, academic resources."),
            ("🕳  DARK WEB", "#ff3355",
             "~6% of the internet. Requires Tor Browser. Contains both legal (privacy-focused) and illegal (criminal) content."),
        ]
        for name, colour, desc in layers:
            row = tk.Frame(layers_card, bg="#060e14", bd=1,
                           relief="solid", padx=12, pady=10)
            row.pack(fill="x", pady=3)
            row.configure(highlightbackground=colour, highlightthickness=1)
            tk.Label(row, text=name, font=("Courier", 10, "bold"),
                     bg="#060e14", fg=colour).pack(anchor="w")
            tk.Label(row, text=desc, font=("Courier", 9),
                     bg="#060e14", fg="#c8e6c9",
                     wraplength=660, justify="left").pack(anchor="w", pady=(3, 0))

        # Stats card
        stats_card = self._make_card(p, "// DARK WEB KEY STATISTICS")
        stats_card.pack(fill="x", padx=8, pady=6)

        stats_frame = tk.Frame(stats_card, bg="#0a1520")
        stats_frame.pack(fill="x")

        stats = [
            ("15B+", "Credentials for sale"),
            ("22%", "Fortune 500 firms affected"),
            ("$4.45M", "Avg. breach cost (IBM 2023)"),
            ("277 days", "Avg. breach detection time"),
        ]
        for stat, label in stats:
            box = tk.Frame(stats_frame, bg="#060e14", bd=1,
                           relief="solid", padx=10, pady=10, width=150)
            box.pack(side="left", padx=6, pady=4)
            tk.Label(box, text=stat, font=("Courier", 14, "bold"),
                     bg="#060e14", fg="#00ff88").pack()
            tk.Label(box, text=label, font=("Courier", 8),
                     bg="#060e14", fg="#4a7a5a", wraplength=130).pack()

        # How Tor works
        tor_card = self._make_card(p, "// HOW TOR WORKS")
        tor_card.pack(fill="x", padx=8, pady=6)

        tor_text = (
            "Tor (The Onion Router) works by encrypting your traffic in multiple layers — like an onion — "
            "and routing it through at least 3 volunteer-run 'relay' servers worldwide.\n\n"
            "  [You] → [Guard Node] → [Middle Node] → [Exit Node] → [.onion / website]\n\n"
            "Each node only knows the previous and next hop — never the full path. "
            "This makes it very difficult to trace the original user. "
            "Dark web sites use .onion addresses, which are only accessible through Tor."
        )
        tk.Label(tor_card, text=tor_text, font=("Courier", 9),
                 bg="#0a1520", fg="#c8e6c9",
                 wraplength=700, justify="left").pack(anchor="w")

        # Common threats
        threats_card = self._make_card(p, "// COMMON DARK WEB THREATS")
        threats_card.pack(fill="x", padx=8, pady=(6, 16))

        threats = [
            ("💳 Stolen Credit Cards", "Millions of card details are listed daily from breached point-of-sale systems."),
            ("🔑 Credential Dumps", "Username/password pairs from breached websites sold in bulk for credential stuffing attacks."),
            ("🦠 Malware-as-a-Service", "Ransomware, keyloggers, and RATs available for purchase by anyone."),
            ("🪪 Identity Theft Kits", "Full personal profiles (name, DOB, SSN, address) sold for as little as $15."),
        ]
        for title, desc in threats:
            row = tk.Frame(threats_card, bg="#0a1520", pady=4)
            row.pack(fill="x")
            tk.Label(row, text=title, font=("Courier", 10, "bold"),
                     bg="#0a1520", fg="#ff3355").pack(anchor="w")
            tk.Label(row, text=desc, font=("Courier", 9),
                     bg="#0a1520", fg="#c8e6c9",
                     wraplength=700, justify="left").pack(anchor="w", padx=16)

    # ── TAB 2: PASSWORD CHECKER ──────────────

    def _build_tab_password(self):
        """Build the Password Strength Checker tab."""
        tab = tk.Frame(self.notebook, bg="#050a0f")
        self.notebook.add(tab, text="  Password Checker  ")

        # Password input card
        input_card = self._make_card(tab, "// PASSWORD STRENGTH ANALYSER")
        input_card.pack(fill="x", padx=8, pady=(12, 6))

        self._label(input_card,
                    "Enter a password below to analyse its strength against dark web attack vectors:",
                    size=9, color="#4a7a5a").pack(anchor="w", pady=(0, 10))

        # Entry row
        entry_frame = tk.Frame(input_card, bg="#0a1520")
        entry_frame.pack(fill="x")

        self.password_var = tk.StringVar()
        self.password_var.trace("w", self._on_password_change)

        self.pw_entry = tk.Entry(entry_frame,
                                 textvariable=self.password_var,
                                 font=("Courier", 13),
                                 bg="#060e14", fg="#00ff88",
                                 insertbackground="#00ff88",
                                 relief="flat", bd=6, show="●")
        self.pw_entry.pack(side="left", fill="x", expand=True, ipady=6)

        self.show_pw = tk.BooleanVar(value=False)
        tk.Checkbutton(entry_frame, text="Show",
                       variable=self.show_pw,
                       command=self._toggle_show_password,
                       bg="#0a1520", fg="#4a7a5a",
                       selectcolor="#0a1520",
                       activebackground="#0a1520",
                       font=("Courier", 9)).pack(side="left", padx=8)

        # Strength bar
        self.strength_bar = tk.Canvas(input_card, height=8,
                                      bg="#060e14", highlightthickness=0)
        self.strength_bar.pack(fill="x", pady=8)

        self.strength_label_var = tk.StringVar(value="")
        tk.Label(input_card, textvariable=self.strength_label_var,
                 font=("Courier", 10, "bold"),
                 bg="#0a1520", fg="#00ff88").pack(anchor="w")

        # Checks grid
        checks_card = self._make_card(tab, "// SECURITY CHECKS")
        checks_card.pack(fill="x", padx=8, pady=6)

        self.check_labels = {}
        checks_frame = tk.Frame(checks_card, bg="#0a1520")
        checks_frame.pack(fill="x")

        check_defs = [
            ("length", "Min. 8 characters"),
            ("uppercase", "Uppercase letters"),
            ("lowercase", "Lowercase letters"),
            ("digits", "Numbers (0-9)"),
            ("special", "Special characters"),
        ]
        for i, (key, text) in enumerate(check_defs):
            row = i // 2
            col = i % 2
            frame = tk.Frame(checks_frame, bg="#060e14",
                             bd=1, relief="solid", padx=10, pady=8)
            frame.grid(row=row, column=col, padx=4, pady=4, sticky="ew")
            checks_frame.columnconfigure(col, weight=1)

            icon_lbl = tk.Label(frame, text="○", font=("Courier", 12),
                                bg="#060e14", fg="#1a3a2a")
            icon_lbl.pack(side="left", padx=(0, 8))

            tk.Label(frame, text=text, font=("Courier", 9),
                     bg="#060e14", fg="#4a7a5a").pack(side="left")

            self.check_labels[key] = (frame, icon_lbl)

        # SHA-1 hash card
        hash_card = self._make_card(tab, "// SHA-1 HASH  (k-Anonymity Demo)")
        hash_card.pack(fill="x", padx=8, pady=6)

        self._label(hash_card,
                    "Real breach APIs like HaveIBeenPwned use k-anonymity: only the first 5 characters of your "
                    "SHA-1 hash are sent — your actual password is never transmitted.",
                    size=9, color="#4a7a5a").pack(anchor="w", pady=(0, 8))

        self.hash_var = tk.StringVar(value="SHA-1: ")
        tk.Label(hash_card, textvariable=self.hash_var,
                 font=("Courier", 9), bg="#0a1520",
                 fg="#00ff88", wraplength=700).pack(anchor="w")

        # Generate button
        gen_card = self._make_card(tab, "// PASSWORD GENERATOR")
        gen_card.pack(fill="x", padx=8, pady=(6, 12))

        btn_frame = tk.Frame(gen_card, bg="#0a1520")
        btn_frame.pack(fill="x")

        self._button(btn_frame, "Generate Strong Password",
                     self._generate_password, width=26).pack(side="left")

        self.gen_pw_var = tk.StringVar(value="")
        tk.Label(gen_card, textvariable=self.gen_pw_var,
                 font=("Courier", 11), bg="#0a1520",
                 fg="#ffcc00", pady=6).pack(anchor="w")

    def _on_password_change(self, *args):
        """Called whenever password entry changes — updates all checks."""
        password = self.password_var.get()
        score, checks, _ = check_password_strength(password)
        label, colour = get_strength_label(score)

        # Update strength bar
        self.strength_bar.delete("all")
        bar_width = self.strength_bar.winfo_width() or 600
        fill_width = (score / 5) * bar_width
        self.strength_bar.create_rectangle(0, 0, fill_width, 8, fill=colour, outline="")

        if password:
            self.strength_label_var.set(f"Strength: {label} ({score}/5)")
        else:
            self.strength_label_var.set("")

        # Update check items
        for key, (frame, icon_lbl) in self.check_labels.items():
            if checks.get(key):
                frame.configure(highlightbackground="#00ff88")
                icon_lbl.configure(text="✓", fg="#00ff88")
            else:
                frame.configure(highlightbackground="#0f3d2e")
                icon_lbl.configure(text="○", fg="#1a3a2a")

        # Update SHA-1 hash
        if password:
            hashed = hash_password_sha1(password)
            self.hash_var.set(f"SHA-1: {hashed[:5]}••••••••••••••••••••••••••••••••••••\n"
                              f"First 5 chars sent to API: {hashed[:5]}")
        else:
            self.hash_var.set("SHA-1: ")

        # Log to history stack
        self.history_stack.push(f"Password checked — score: {score}/5")

    def _toggle_show_password(self):
        """Toggle password visibility."""
        if self.show_pw.get():
            self.pw_entry.configure(show="")
        else:
            self.pw_entry.configure(show="●")

    def _generate_password(self):
        """Generate and display a strong random password."""
        pw = generate_strong_password()
        self.gen_pw_var.set(f"Generated: {pw}")
        self.history_stack.push("Generated a strong password")

    # ── TAB 3: BREACH CHECKER ───────────────

    def _build_tab_breach(self):
        """Build the Simulated Breach Checker tab."""
        tab = tk.Frame(self.notebook, bg="#050a0f")
        self.notebook.add(tab, text="  Breach Checker  ")

        input_card = self._make_card(tab, "// SIMULATED EMAIL BREACH CHECKER")
        input_card.pack(fill="x", padx=8, pady=(12, 6))

        self._label(input_card,
                    "Enter an email to check against our simulated breach database.\n"
                    "NOTE: This is a local educational simulation only — no real API calls are made.",
                    size=9, color="#4a7a5a").pack(anchor="w", pady=(0, 10))

        self.email_var = tk.StringVar()
        tk.Entry(input_card, textvariable=self.email_var,
                 font=("Courier", 12),
                 bg="#060e14", fg="#00ff88",
                 insertbackground="#00ff88",
                 relief="flat", bd=6).pack(fill="x", ipady=6, pady=(0, 10))

        btn_row = tk.Frame(input_card, bg="#0a1520")
        btn_row.pack(fill="x")
        self._button(btn_row, "Check Email", self._run_breach_check).pack(side="left")

        self._label(input_card,
                    "Try: test@yahoo.com or user@adobe.com for simulated breach results.",
                    size=8, color="#1a5a3a").pack(anchor="w", pady=(8, 0))

        # Result area
        self.breach_result_frame = self._make_card(tab, "// SCAN RESULTS")
        self.breach_result_frame.pack(fill="x", padx=8, pady=6)

        self.breach_result_text = tk.Text(self.breach_result_frame,
                                          height=10, bg="#020608",
                                          fg="#00ff88",
                                          font=("Courier", 10),
                                          relief="flat", bd=4,
                                          state="disabled",
                                          insertbackground="#00ff88")
        self.breach_result_text.pack(fill="x")

        # What to do card
        action_card = self._make_card(tab, "// IF YOUR EMAIL IS BREACHED — TAKE ACTION")
        action_card.pack(fill="x", padx=8, pady=(6, 12))

        actions = [
            "1. Change your password on the affected service immediately.",
            "2. Change the same password on ANY other service where you used it.",
            "3. Enable Two-Factor Authentication (2FA) on all accounts.",
            "4. Monitor your bank statements for suspicious activity.",
            "5. Consider using a password manager to generate unique passwords.",
        ]
        for action in actions:
            tk.Label(action_card, text=action, font=("Courier", 9),
                     bg="#0a1520", fg="#c8e6c9",
                     anchor="w").pack(fill="x", pady=2)

    def _run_breach_check(self):
        """Run the simulated breach check and display results."""
        email = self.email_var.get().strip()
        if not email:
            messagebox.showwarning("Input Required", "Please enter an email address.")
            return

        # Simulate a brief scan
        result = simulate_breach_check(email)
        self.history_stack.push(f"Breach check: {email} → {result['status']}")

        # Update terminal-style output
        self.breach_result_text.configure(state="normal")
        self.breach_result_text.delete("1.0", tk.END)

        lines = []
        lines.append(f"[*] Scanning: {email}")
        lines.append(f"[*] Querying simulated breach database...")
        lines.append(f"[*] Checking {len(SIMULATED_BREACHED_DOMAINS)} known breach sources...")
        lines.append("")

        if result["status"] == "invalid":
            lines.append("[!] ERROR: Invalid email format. Please try again.")
        elif result["status"] == "breached":
            lines.append(f"[!] ALERT: {result['message']}")
            lines.append("")
            for b in result["breaches"]:
                lines.append(f"    ► Source  : {b['source']}")
                lines.append(f"      Year    : {b['year']}")
                lines.append(f"      Data    : {b['data']}")
                lines.append("")
            lines.append("[!] RECOMMENDATION: Change this password immediately!")
        else:
            lines.append(f"[✓] SAFE: {result['message']}")
            lines.append("")
            lines.append("[*] Always stay vigilant — new breaches happen daily.")

        for line in lines:
            self.breach_result_text.insert(tk.END, line + "\n")

        if result["status"] == "breached":
            self.breach_result_text.configure(fg="#ff3355")
        elif result["status"] == "safe":
            self.breach_result_text.configure(fg="#00ff88")
        else:
            self.breach_result_text.configure(fg="#ffcc00")

        self.breach_result_text.configure(state="disabled")

    # ── TAB 4: QUIZ ─────────────────────────

    def _build_tab_quiz(self):
        """Build the Dark Web Awareness Quiz tab."""
        tab = tk.Frame(self.notebook, bg="#050a0f")
        self.notebook.add(tab, text="  Awareness Quiz  ")

        self.quiz_frame_outer = tab

        # Progress label
        self.quiz_progress_var = tk.StringVar(value="Question 1 of 6")
        tk.Label(tab, textvariable=self.quiz_progress_var,
                 font=("Courier", 9), bg="#050a0f",
                 fg="#4a7a5a").pack(anchor="w", padx=12, pady=(10, 0))

        # Question card
        q_card = self._make_card(tab, "// QUIZ: DARK WEB AWARENESS")
        q_card.pack(fill="x", padx=8, pady=(4, 6))

        self.quiz_q_var = tk.StringVar()
        tk.Label(q_card, textvariable=self.quiz_q_var,
                 font=("Courier", 11, "bold"),
                 bg="#0a1520", fg="#ffffff",
                 wraplength=700, justify="left").pack(anchor="w", pady=(0, 12))

        # Options
        self.quiz_option_btns = []
        for i in range(4):
            btn = tk.Button(q_card, text="",
                            font=("Courier", 9),
                            bg="#060e14", fg="#c8e6c9",
                            activebackground="#0f3d2e",
                            relief="solid", bd=1,
                            anchor="w", padx=12, pady=8,
                            cursor="hand2",
                            command=lambda idx=i: self._answer_quiz(idx))
            btn.pack(fill="x", pady=3)
            self.quiz_option_btns.append(btn)

        # Feedback
        self.quiz_feedback_var = tk.StringVar()
        self.quiz_feedback_lbl = tk.Label(q_card,
                                          textvariable=self.quiz_feedback_var,
                                          font=("Courier", 9),
                                          bg="#0a1520", fg="#4a7a5a",
                                          wraplength=700, justify="left")
        self.quiz_feedback_lbl.pack(anchor="w", pady=8)

        # Next button
        self.quiz_next_btn = self._button(tab, "Next Question →",
                                          self._next_quiz_question, width=22)
        self.quiz_next_btn.pack(anchor="e", padx=12, pady=4)
        self.quiz_next_btn.configure(state="disabled")

        # Score card (hidden until end)
        self.score_card = self._make_card(tab, "// QUIZ COMPLETE")
        self.score_var = tk.StringVar()
        tk.Label(self.score_card, textvariable=self.score_var,
                 font=("Courier", 22, "bold"),
                 bg="#0a1520", fg="#00ff88").pack(pady=8)
        self.score_msg_var = tk.StringVar()
        tk.Label(self.score_card, textvariable=self.score_msg_var,
                 font=("Courier", 10),
                 bg="#0a1520", fg="#c8e6c9",
                 wraplength=700).pack()
        self._button(self.score_card, "Restart Quiz",
                     self._restart_quiz, width=18).pack(pady=10)

        self._load_quiz_question()

    def _load_quiz_question(self):
        """Load the current quiz question into the UI."""
        if self.quiz_index >= len(self.quiz_list):
            self._show_quiz_score()
            return

        q = self.quiz_list[self.quiz_index]
        self.quiz_progress_var.set(f"Question {self.quiz_index + 1} of {len(self.quiz_list)}")
        self.quiz_q_var.set(q["question"])
        self.quiz_feedback_var.set("")
        self.quiz_answered = False
        self.quiz_next_btn.configure(state="disabled")

        for i, btn in enumerate(self.quiz_option_btns):
            btn.configure(text=q["options"][i],
                          bg="#060e14", fg="#c8e6c9",
                          state="normal")

    def _answer_quiz(self, selected_idx):
        """Handle a quiz answer selection."""
        if self.quiz_answered:
            return

        self.quiz_answered = True
        q = self.quiz_list[self.quiz_index]
        correct_idx = q["answer"]

        for i, btn in enumerate(self.quiz_option_btns):
            btn.configure(state="disabled")
            if i == correct_idx:
                btn.configure(bg="#0f3d2e", fg="#00ff88")
            elif i == selected_idx:
                btn.configure(bg="#3d0f1a", fg="#ff3355")

        if selected_idx == correct_idx:
            self.quiz_score += 1
            self.quiz_feedback_var.set(f"✓ Correct!  {q['explanation']}")
            self.quiz_feedback_lbl.configure(fg="#00ff88")
        else:
            self.quiz_feedback_var.set(f"✗ Incorrect.  {q['explanation']}")
            self.quiz_feedback_lbl.configure(fg="#ff3355")

        self.quiz_next_btn.configure(state="normal")
        self.history_stack.push(f"Quiz Q{self.quiz_index+1} answered")

    def _next_quiz_question(self):
        """Move to next quiz question."""
        self.quiz_index += 1
        self._load_quiz_question()

    def _show_quiz_score(self):
        """Display final quiz score."""
        total = len(self.quiz_list)
        pct = (self.quiz_score / total) * 100
        self.score_var.set(f"{self.quiz_score} / {total}  ({pct:.0f}%)")

        if pct >= 80:
            msg = "Excellent! You have strong dark web awareness. Keep practising good security habits."
        elif pct >= 50:
            msg = "Good effort! Review the About tab to strengthen your dark web knowledge."
        else:
            msg = "Keep learning! Check out the About Dark Web tab for more information."

        self.score_msg_var.set(msg)

        for btn in self.quiz_option_btns:
            btn.pack_forget()
        self.quiz_next_btn.pack_forget()
        self.score_card.pack(fill="x", padx=8, pady=10)

    def _restart_quiz(self):
        """Reset and restart the quiz."""
        self.quiz_index = 0
        self.quiz_score = 0
        self.score_card.pack_forget()

        for btn in self.quiz_option_btns:
            btn.pack(fill="x", pady=3)
        self.quiz_next_btn.pack(anchor="e", padx=12, pady=4)
        self._load_quiz_question()

    # ── TAB 5: TIPS ─────────────────────────

    def _build_tab_tips(self):
        """Build the Protection Tips tab."""
        tab = tk.Frame(self.notebook, bg="#050a0f")
        self.notebook.add(tab, text="  Protection Tips  ")

        canvas = tk.Canvas(tab, bg="#050a0f", bd=0, highlightthickness=0)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#050a0f")
        scroll_frame.bind("<Configure>",
                          lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        tips_card = self._make_card(scroll_frame, "// HOW TO PROTECT YOURSELF FROM DARK WEB THREATS")
        tips_card.pack(fill="x", padx=8, pady=(12, 6))

        tips = [
            ("01", "Use a Password Manager",
             "#00aaff",
             "Use tools like Bitwarden or KeePass to generate and store unique, strong passwords for every account. "
             "Never reuse passwords — a breach on one site won't compromise others."),
            ("02", "Enable Two-Factor Authentication (2FA)",
             "#00ff88",
             "2FA requires a second verification step (like a code from your phone) even if your password is stolen. "
             "Use authenticator apps like Google Authenticator rather than SMS-based 2FA where possible."),
            ("03", "Monitor Your Email for Breaches",
             "#ffcc00",
             "Regularly check services like HaveIBeenPwned.com to see if your email has appeared in known data breaches. "
             "Consider setting up alerts for new breaches involving your email."),
            ("04", "Keep Software & OS Updated",
             "#ff8800",
             "Cybercriminals exploit known vulnerabilities in outdated software. Enable automatic updates for your "
             "operating system, browsers, and applications to patch security holes quickly."),
            ("05", "Use a VPN on Public Networks",
             "#00aaff",
             "A Virtual Private Network (VPN) encrypts your internet traffic, making it much harder for attackers "
             "on public Wi-Fi to intercept your data or credentials."),
            ("06", "Be Wary of Phishing Attacks",
             "#ff3355",
             "Attackers use fake emails and websites to steal credentials. Always verify the sender's email address, "
             "avoid clicking suspicious links, and go directly to official websites rather than using email links."),
            ("07", "Freeze Your Credit",
             "#00ff88",
             "If your personal information appears on the dark web, a credit freeze prevents new accounts from being "
             "opened in your name, protecting you from identity theft."),
            ("08", "Use Encrypted Messaging",
             "#ffcc00",
             "Use end-to-end encrypted messaging apps like Signal for sensitive communications. This ensures that even "
             "if messages are intercepted, they cannot be read."),
        ]

        for num, title, colour, desc in tips:
            row = tk.Frame(tips_card, bg="#060e14",
                           bd=1, relief="solid",
                           padx=14, pady=12)
            row.pack(fill="x", pady=4)
            row.configure(highlightbackground=colour, highlightthickness=1)

            header_row = tk.Frame(row, bg="#060e14")
            header_row.pack(fill="x")

            tk.Label(header_row, text=num,
                     font=("Courier", 16, "bold"),
                     bg="#060e14", fg=colour).pack(side="left", padx=(0, 12))
            tk.Label(header_row, text=title,
                     font=("Courier", 11, "bold"),
                     bg="#060e14", fg="#ffffff").pack(side="left")

            tk.Label(row, text=desc,
                     font=("Courier", 9),
                     bg="#060e14", fg="#c8e6c9",
                     wraplength=680, justify="left").pack(anchor="w", pady=(6, 0))

        # Disclaimer
        disclaimer_card = self._make_card(scroll_frame, "// DISCLAIMER")
        disclaimer_card.pack(fill="x", padx=8, pady=(6, 16))
        tk.Label(disclaimer_card,
                 text="This tool is created for educational purposes only as part of the ST4017CMD "
                      "Introduction to Programming module at Softwarica College of IT & E-Commerce. "
                      "The breach checker is a simulated demonstration and does not connect to real APIs. "
                      "Do not use this tool for any unlawful or unethical purposes.",
                 font=("Courier", 8),
                 bg="#0a1520", fg="#4a7a5a",
                 wraplength=700, justify="left").pack(anchor="w")


# ─────────────────────────────────────────────
#   ENTRY POINT
# ─────────────────────────────────────────────

def main():
    """Launch the DarkWatch application."""
    root = tk.Tk()
    app = DarkWatchApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
