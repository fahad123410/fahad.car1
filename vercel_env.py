import os

def setup_vercel_env():
    """Setup environment variables for Vercel deployment"""
    os.environ.setdefault('ADMIN_PASSWORD', 'admin123')
    os.environ.setdefault('SECRET_KEY', 'vercel-secret-key-change-this')
    os.environ.setdefault('WHATSAPP_NUMBER', '94756656862')
    os.environ.setdefault('FIREBASE_ENABLED', 'false')
    os.environ.setdefault('BANK_NAME', 'Bank of Ceylon')
    os.environ.setdefault('ACCOUNT_NAME', 'Fahad Rental Service')
    os.environ.setdefault('ACCOUNT_NUMBER', '123456789012')
    os.environ.setdefault('BRANCH_CODE', '123')
    os.environ.setdefault('ACCOUNT_TYPE', 'Savings')
    print("✓ Vercel environment configured")