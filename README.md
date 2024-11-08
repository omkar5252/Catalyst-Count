# Catalyst Count

A Docker-based application for managing and analyzing company data through CSV uploads with user authentication and filtering capabilities.

## 🚀 Quick Start

### Prerequisites

- Git
- Docker and Docker Compose
- Python 3.x

### Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/omkar5252/Catalyst-Count.git
   cd Catalyst-Count
   ```

2. **Build Docker Containers**
   ```bash
   docker-compose -f docker-compose.local.yml build
   ```

3. **Start the Application**
   ```bash
   docker-compose -f docker-compose.local.yml up
   ```

4. **Create Superuser**
   ```bash
   docker-compose -f docker-compose.local.yml run --rm django python3 manage.py createsuperuser
   ```

## 🔑 User Authentication

### New User Registration

1. Visit the application at http://127.0.0.1:8000/
2. Click on the "Sign Up" option
3. Fill in your registration details
4. Check your email for verification link (using Mailpit)
5. For Mailpit Visit - http://127.0.0.1:8025

### Email Verification

Two methods available:
- Click the verification link in the email received
- Admin can verify through Django admin panel

### Accessing the Application

1. Visit http://127.0.0.1:8000/
2. Log in with your verified credentials

## 📊 Data Management

### Uploading Company Data

1. Log in to your account
2. Navigate to the upload section
3. Upload your CSV file with company data
   - Ensure your CSV follows the required format
   - Data will be automatically stored in the database

### Data Retrieval and Filtering

- Use the built-in filtering options to sort and view company data
- Apply multiple filters for precise data retrieval
- Export filtered data as needed

## 👨‍💼 Admin Access

To access the Django admin panel:
1. Navigate to `/admin` URL
2. Log in with superuser credentials
3. Manage users, verify email status, and handle data

## 🛠 Additional Information

- The application runs on port 8000 by default
- Email verification system is integrated with Mailpit
- All data is persisted in Docker volumes
