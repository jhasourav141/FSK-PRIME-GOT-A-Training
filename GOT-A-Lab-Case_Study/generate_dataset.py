"""Generates a synthetic 500-row CPGRAMS-style grievance dataset (jan_samadhan_grievances.csv).
All data is fictional: names, phone numbers and Aadhaar-like numbers are randomly generated."""
import numpy as np, pandas as pd

rng = np.random.default_rng(42)
N = 500

# (issue text, urgency)  H=High, M=Medium, L=Low
DEPTS = {
 "Railways": [("my train was running {n} hours late and nobody gave any information", "M"),
   ("AC coach was not working during the whole journey", "M"),
   ("refund for my cancelled train ticket has not been received", "L"),
   ("toilets in the coach were extremely dirty", "L"),
   ("money was deducted on IRCTC but the ticket was not confirmed", "M"),
   ("a railway staff member at the station behaved rudely with senior citizens", "M")],
 "Telecom": [("my broadband connection has not worked for {n} days", "M"),
   ("mobile network keeps dropping calls in our area", "L"),
   ("I was charged a wrong amount on my postpaid mobile bill", "L"),
   ("my landline is dead since the rains and nobody has come to repair it", "M"),
   ("my SIM was deactivated without any notice", "M"),
   ("the tower signal in our village is very weak, emergency calls fail", "H")],
 "Banking & Finance": [("money was debited from my account but the ATM did not dispense cash", "M"),
   ("my loan EMI was deducted twice this month", "M"),
   ("my KYC update was rejected without any reason", "L"),
   ("the bank is refusing to open a Jan Dhan account for me", "M"),
   ("there is an unauthorised transaction on my savings account", "H"),
   ("my cheque was returned wrongly and I was fined", "L")],
 "Health & Family Welfare": [("my Ayushman Bharat card was rejected at the hospital during treatment", "H"),
   ("there is no doctor available at the primary health centre for {n} days", "H"),
   ("medicines are out of stock at the government hospital", "H"),
   ("the ambulance did not arrive on time for a patient", "H"),
   ("my vaccination certificate has not been generated", "L"),
   ("the hospital is demanding money for free treatment", "M")],
 "Education": [("my scholarship amount has not been credited for {n} months", "M"),
   ("the school teacher has been absent regularly", "L"),
   ("the quality of the mid-day meal is very poor", "M"),
   ("my marksheet correction request is still pending", "L"),
   ("admission was denied to my child under the RTE quota", "M"),
   ("the school building roof is leaking and children are at risk", "H")],
 "Urban Development": [("garbage has not been collected in our colony for {n} days", "L"),
   ("the streetlight in our lane has not been working", "L"),
   ("potholes on the main road are causing accidents", "H"),
   ("drain overflow near my house is spreading disease", "H"),
   ("the municipal water supply is irregular", "M"),
   ("illegal construction is going on next to my plot", "L")],
 "Pension & Welfare": [("my old age pension has not been received for {n} months", "H"),
   ("my family pension case is pending for a long time", "M"),
   ("my life certificate was rejected by the pension office", "M"),
   ("my widow pension was stopped without any notice", "H"),
   ("my pension amount has been calculated wrongly", "M"),
   ("the PPO number has still not been issued to me", "L")],
 "Rural Development": [("MGNREGA wages have not been paid for {n} weeks", "H"),
   ("my MGNREGA job card has not been issued", "M"),
   ("the PM Awas Yojana instalment is pending", "M"),
   ("the village road work has been left incomplete", "L"),
   ("the hand pump in our village has not been repaired", "M"),
   ("the gram panchayat is ignoring my application", "L")],
}
DEPT_WEIGHTS = [.14, .10, .13, .12, .12, .15, .12, .12]
RES_MEAN = {"Railways": 9, "Telecom": 12, "Banking & Finance": 15, "Health & Family Welfare": 7,
            "Education": 22, "Urban Development": 18, "Pension & Welfare": 25, "Rural Development": 28}
OPENERS = ["I am writing to complain that ", "This is to bring to your notice that ", "Sir/Madam, ",
           "I am very upset because ", "Respected Sir, ", "URGENT: ", "Kindly look into this. ", ""]
CLOSERS = ["Please take action immediately.", "I have complained several times but nobody listens.",
           "Request you to resolve this at the earliest.", "This is harassment of a common citizen!!",
           "I will approach the court if this is not solved.", "Kindly help.",
           "My family is suffering a lot.", "Please resolve soon."]
STATES = ["Jharkhand", "Bihar", "Uttar Pradesh", "Delhi", "Maharashtra", "Tamil Nadu", "West Bengal",
          "Rajasthan", "Odisha", "Madhya Pradesh", "Karnataka", "Gujarat"]
NAMES = ["Ravi Kumar", "Sunita Devi", "Mohammad Aslam", "Anita Sharma", "Rajesh Singh", "Lakshmi Iyer",
         "Pooja Verma", "Amit Mishra", "Kavita Yadav", "Suresh Patel"]
LOCS = ["Gandhi Nagar", "Station Road", "Ambedkar Colony", "Shastri Nagar", "Nehru Market", "Subhash Chowk"]
DEPT_NAMES = list(DEPTS)

def pii_sentence():
    k = rng.integers(0, 4)
    phone = f"{rng.choice([6,7,8,9])}{rng.integers(10**8, 10**9)}"
    aad = f"{rng.integers(2,10)}{rng.integers(100,1000)} {rng.integers(1000,10000)} {rng.integers(1000,10000)}"
    nm = rng.choice(NAMES)
    if k == 0: return f" My phone number is {phone}."
    if k == 1: return f" My Aadhaar number is {aad} and my mobile is +91 {phone}."
    if k == 2: return f" I live at House No {rng.integers(1,200)}, {rng.choice(LOCS)}, Garhwa. Contact: {nm.split()[0].lower()}{rng.integers(10,99)}@gmail.com"
    return f" My name is {nm}, Aadhaar {aad}."

def messy(t):
    if rng.random() < .35: t = t.replace(" ", "  ", 2)
    if rng.random() < .25: t = t.replace(".", "...", 1)
    if rng.random() < .2: t += " ###"
    if rng.random() < .15: t = "@@ " + t
    if rng.random() < .15: t = t.replace(" and ", " & ")
    return t

dates = pd.to_datetime("2025-01-01") + pd.to_timedelta(
    rng.choice(669, N, p=np.linspace(0.6, 1.4, 669) / np.linspace(0.6, 1.4, 669).sum()), unit="D")
rows = []
for i in range(N):
    dept = rng.choice(DEPT_NAMES, p=DEPT_WEIGHTS)
    issue, urg = DEPTS[dept][rng.integers(0, 6)]
    text = (rng.choice(OPENERS) + issue.format(n=rng.integers(2, 30)) + ". ")
    if rng.random() < .12:  # cross-department noise sentence
        other = rng.choice([d for d in DEPT_NAMES if d != dept])
        text += "Earlier also " + DEPTS[other][rng.integers(0, 6)][0].format(n=5) + ". "
    text += rng.choice(CLOSERS)
    if rng.random() < .30: text += pii_sentence()
    if rng.random() < .10: urg = rng.choice(["High", "Medium", "Low"])
    else: urg = {"H": "High", "M": "Medium", "L": "Low"}.get(urg, urg)
    label = dept if rng.random() > .03 else rng.choice(DEPT_NAMES)   # ~3% label noise
    status = rng.choice(["Resolved", "In Progress", "Pending"], p=[.7, .15, .15])
    res = round(float(rng.gamma(3, RES_MEAN[dept] / 3)), 1) if status == "Resolved" else np.nan
    rows.append([f"JS/2026/{i+1:05d}", dates[i].date(), rng.choice(STATES), label, urg, status, res, messy(text)])

df = pd.DataFrame(rows, columns=["Complaint_ID", "Date", "State", "Department", "Urgency", "Status",
                                 "Resolution_Days", "Complaint_Text"])
df.loc[rng.choice(N, 20, replace=False), "State"] = np.nan          # missing states
df.loc[rng.choice(N, 10, replace=False), "Complaint_Text"] = np.nan  # missing text
df.to_csv("jan_samadhan_grievances.csv", index=False)
print("Saved jan_samadhan_grievances.csv", df.shape)
