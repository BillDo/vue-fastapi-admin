# Step-by-Step: Switch to PostgreSQL

## ✅ Step 1: Install PostgreSQL Driver (DONE)
```bash
pip install asyncpg
```
✅ Already installed!

## 📝 Step 2: Create .env File

Create a `.env` file in your project root with these contents:

```env
# Database Configuration
DB_TYPE=postgres

# PostgreSQL Configuration
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_NAME=vue_fastapi_admin
```

**Quick copy command (Windows PowerShell):**
```powershell
Copy-Item .env.example .env
# Then edit .env and add your PostgreSQL password
```

## 🗄️ Step 3: Install and Setup PostgreSQL

### Option A: Install PostgreSQL Locally

1. **Download PostgreSQL:**
   - Visit: https://www.postgresql.org/download/windows/
   - Or use: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
   - Download and install PostgreSQL (remember the password you set!)

2. **Verify Installation:**
   ```powershell
   psql --version
   ```

### Option B: Use Docker (Recommended for Development)

```powershell
# Start PostgreSQL in Docker
docker run --name postgres-dev `
  -e POSTGRES_PASSWORD=postgres `
  -e POSTGRES_DB=vue_fastapi_admin `
  -p 5432:5432 `
  -d postgres:15

# Your .env should be:
# DB_PASSWORD=postgres
```

### Option C: Use Cloud/Remote PostgreSQL

If you have a remote PostgreSQL server, just update your `.env`:
```env
DB_HOST=your-postgres-host.com
DB_PORT=5432
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=vue_fastapi_admin
```

## 🎯 Step 4: Create Database

### If PostgreSQL is installed locally:

```powershell
# Connect to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE vue_fastapi_admin;

# Exit psql
\q
```

### Or using psql command line:
```powershell
psql -U postgres -c "CREATE DATABASE vue_fastapi_admin;"
```

## 🔄 Step 5: Run Migrations

```powershell
# Make sure your .env file has DB_TYPE=postgres
aerich upgrade
```

This will:
- Create all tables in PostgreSQL
- Run all migrations
- Set up your database schema

## ✅ Step 6: Test Connection

Start your application:
```powershell
python run.py
```

You should see:
- ✅ No database connection errors
- ✅ Application starts successfully
- ✅ Can login to admin dashboard

## 🔍 Verify PostgreSQL is Working

You can verify by connecting to PostgreSQL:

```powershell
psql -U postgres -d vue_fastapi_admin

# List tables
\dt

# Check if tables exist
SELECT table_name FROM information_schema.tables 
WHERE table_schema = 'public';

# Exit
\q
```

## 📋 Quick Checklist

- [ ] PostgreSQL installed/running
- [ ] `.env` file created with PostgreSQL config
- [ ] Database `vue_fastapi_admin` created
- [ ] `aerich upgrade` completed successfully
- [ ] Application starts without errors
- [ ] Can access admin dashboard

## 🆘 Troubleshooting

### Error: "could not connect to server"
- **Solution**: Make sure PostgreSQL service is running
  ```powershell
  # Check PostgreSQL service (Windows)
  Get-Service postgresql*
  
  # Start if stopped
  Start-Service postgresql-x64-15  # Adjust version number
  ```

### Error: "password authentication failed"
- **Solution**: Check your password in `.env` file matches PostgreSQL password

### Error: "database does not exist"
- **Solution**: Create the database (Step 4 above)

### Error: "module 'asyncpg' has no attribute..."
- **Solution**: Reinstall asyncpg
  ```powershell
  pip install --upgrade asyncpg
  ```

## 🔄 Switching Back to SQLite

If you need to switch back:
```env
DB_TYPE=sqlite
```
Then restart your application.

