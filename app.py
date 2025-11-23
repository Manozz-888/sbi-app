from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory account storage
accounts = {}

@app.route('/')
def index():
    return redirect('/home')

@app.route('/home', methods=['GET'])
def home():
    return render_template("home.html", message="")

@app.route('/create', methods=['POST'])
def create_account():
    acc_id = request.form.get('id')
    name = request.form.get('name')

    if not acc_id or not name:
        message = "Account number and name are required."
    elif acc_id in accounts:
        message = f"Account number {acc_id} already exists!"
    else:
        accounts[acc_id] = {"name": name.lower(), "balance": 0.0}
        message = f"Account created for {name} (Account No: {acc_id})"
    return render_template("home.html", message=message)

@app.route('/deposit', methods=['POST'])
def deposit():
    acc_id = request.form.get('id')
    name = request.form.get('name')
    amount = request.form.get('amount')

    if acc_id not in accounts:
        message = "Account number not found."
    elif accounts[acc_id]["name"] != name.lower():
        message = "Name does not match the account number."
    else:
        try:
            amount = float(amount)
            if amount <= 0:
                message = "Amount must be positive."
            else:
                accounts[acc_id]["balance"] += amount
                message = f"Deposited ₹{amount} to {name}'s account."
        except:
            message = "Invalid amount."
    return render_template("home.html", message=message)

@app.route('/withdraw', methods=['POST'])
def withdraw():
    acc_id = request.form.get('id')
    name = request.form.get('name')
    amount = request.form.get('amount')

    if acc_id not in accounts:
        message = "Account number not found."
    elif accounts[acc_id]["name"] != name.lower():
        message = "Name does not match the account number."
    else:
        try:
            amount = float(amount)
            if amount <= 0:
                message = "Amount must be positive."
            elif accounts[acc_id]["balance"] < amount:
                message = "Insufficient balance."
            else:
                accounts[acc_id]["balance"] -= amount
                message = f"Withdrew ₹{amount} from {name}'s account."
        except:
            message = "Invalid amount."
    return render_template("home.html", message=message)

@app.route('/balance', methods=['POST'])
def check_balance():
    acc_id = request.form.get('id')
    name = request.form.get('name')

    if acc_id not in accounts:
        message = "Account number not found."
    elif accounts[acc_id]["name"] != name.lower():
        message = "Name does not match the account number."
    else:
        bal = accounts[acc_id]["balance"]
        message = f"{name}'s Balance (Acc No: {acc_id}): ₹{bal:.2f}"
    return render_template("home.html", message=message)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001)