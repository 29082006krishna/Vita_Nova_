import random
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mail import Mail, Message

app = Flask(__name__)
# IMPORTANT: Change this to a random string for security
app.secret_key = 'analytix_secret_key_123' 

# --- Flask-Mail Configuration ---
# --- Flask-Mail Configuration ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'aadityachitroda1203@gmail.com'  # Replace with your Gmail
app.config['MAIL_PASSWORD'] = 'khra cvlz dtml dzyr'  # Paste the 16-digit code here
mail = Mail(app)

# --- Existing Routes ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

# --- Updated Signup with OTP Logic ---
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        action = request.form.get('action')
        contact_info = request.form.get('contact')
        
        if action == 'get_otp':
            # 1. Generate OTP
            otp = str(random.randint(100000, 999999))
            session['otp'] = otp
            
            # 2. Send the actual email
            msg = Message('Analytix Verification Code', 
                          sender=app.config['MAIL_USERNAME'], 
                          recipients=[contact_info])
            msg.body = f"Your OTP is: {otp}"
            mail.send(msg) # This sends the email using your App Password
            
            print(f"OTP sent to {contact_info}")
            # This reloads your page with your original UI
            return render_template('signup.html') 

        elif action == 'create_account':
            user_otp = request.form.get('otp_input')
            
            # Verify the code
            if user_otp == session.get('otp'):
                return redirect(url_for('dashboard'))
            else:
                return "Invalid OTP. Please go back and try again."

    return render_template('signup.html')
# --- New Verification Route ---

@app.route('/verify-otp', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        # Get the OTP entered by the user
        user_otp = request.form.get('otp_input')
        
        # Compare with the one stored in session
        if user_otp == session.get('otp'):
            return redirect(url_for('dashboard'))
        else:
            return "Invalid OTP. Please go back and try again."
            
    return render_template('forgetPass.html')

# --- Other Dashboard Routes ---

@app.route('/forgot-password')
def forgot_password():
    return render_template('forgetPass.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/demand_forecasting') # This is the browser address
def demandForcasting():           # This is the "endpoint" name Flask is looking for
    return render_template('demandForcasting.html')

@app.route('/top-sellers')
def top_sellers():
    return render_template('top5.html')

@app.route('/product-insights')
def product_insights():
    return render_template('amul.html')

@app.route('/generate-report')
def generate_report():
    return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=True)