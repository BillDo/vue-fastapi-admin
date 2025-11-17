# PostgreSQL Setup Guide

## ✅ Project Status: Ready for PostgreSQL

Your project is **fully configured** to use PostgreSQL. Here's what's been set up:

### ✅ What's Ready

1. **Configuration Support** (`app/settings/config.py`)
   - Dynamic database configuration via environment variables
   - Supports SQLite, MySQL, and PostgreSQL
   - Automatic connection setup based on `DB_TYPE`

2. **Database Drivers** (`pyproject.toml`)
   - `asyncpg` - PostgreSQL driver ✅ Added
   - `asyncmy` - MySQL driver ✅ Added
   - `aiosqlite` - SQLite driver ✅ Already present

3. **Tortoise ORM Integration**
   - Uses `tortoise.backends.asyncpg` for PostgreSQL
   - Properly configured connection strings
   - Compatible with all your existing models

4. **Aerich Migrations**
   - Works with PostgreSQL
   - No more SQLite migration limitations

### 📋 Quick Start with PostgreSQL

#### Step 1: Install Dependencies

```bash
# Install PostgreSQL driver
uv pip install asyncpg

# Or install all database drivers
uv pip install -r pyproject.toml
```

#### Step 2: Set Environment Variables

**Option A: Create `.env` file** (recommended)
```bash
DB_TYPE=postgres
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_NAME=vue_fastapi_admin
```

**Option B: Set in terminal/shell**
```bash
export DB_TYPE=postgres
export DB_HOST=localhost
export DB_PORT=5432
export DB_USER=postgres
export DB_PASSWORD=yourpassword
export DB_NAME=vue_fastapi_admin
```

#### Step 3: Create PostgreSQL Database

```bash
# Connect to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE vue_fastapi_admin;

# Exit psql
\q
```

#### Step 4: Run Migrations

```bash
# Initialize (if first time)
aerich init-db

# Or upgrade existing migrations
aerich upgrade
```

#### Step 5: Start Your App

```bash
python run.py
```

### 🔍 Verify PostgreSQL Connection

The app will automatically:
- Detect `DB_TYPE=postgres` from environment
- Use `asyncpg` driver
- Connect to PostgreSQL database
- Run all migrations

### 📝 Environment Variables Reference

| Variable | PostgreSQL Default | MySQL Default | Description |
|----------|-------------------|--------------|-------------|
| `DB_TYPE` | `postgres` | `mysql` | Database type |
| `DB_HOST` | `localhost` | `localhost` | Database host |
| `DB_PORT` | `5432` | `3306` | Database port |
| `DB_USER` | `postgres` | `root` | Database user |
| `DB_PASSWORD` | (required) | (required) | Database password |
| `DB_NAME` | `vue_fastapi_admin` | `vue_fastapi_admin` | Database name |

### 🚀 Production Deployment

For production, set these environment variables in your hosting platform:

**Docker Example:**
```yaml
environment:
  - DB_TYPE=postgres
  - DB_HOST=postgres
  - DB_PORT=5432
  - DB_USER=app_user
  - DB_PASSWORD=secure_password
  - DB_NAME=vue_fastapi_admin
```

**Hosting Provider (Heroku/Railway/etc):**
- Set environment variables in your hosting dashboard
- The app will automatically use PostgreSQL

### ✅ Testing Checklist

- [ ] `asyncpg` driver installed
- [ ] PostgreSQL database created
- [ ] Environment variables set
- [ ] `aerich upgrade` runs successfully
- [ ] App starts without errors
- [ ] Can connect to database and query data

### 🔄 Switching Between Databases

To switch databases, just change `DB_TYPE`:

```bash
# Use SQLite (default, development)
DB_TYPE=sqlite

# Use MySQL
DB_TYPE=mysql
DB_PORT=3306
DB_USER=root

# Use PostgreSQL
DB_TYPE=postgres
DB_PORT=5432
DB_USER=postgres
```

No code changes needed! 🎉

