# Deployment Guide

## Database Configuration

This project supports multiple database backends:
- **SQLite** (default, for development)
- **MySQL/MariaDB** (recommended for production)
- **PostgreSQL** (also good for production)

### Choosing a Database

**Use SQLite if:**
- Development/testing environment
- Single user application
- Low traffic (< 100 concurrent users)
- Simple deployment without database server

**Use MySQL/PostgreSQL if:**
- Production environment
- Multiple users/concurrent access
- Need scalability
- Hosting provider offers managed databases
- Need better backup/replication options

### Configuration via Environment Variables

The database type is controlled by the `DB_TYPE` environment variable:

#### SQLite (Default)
```bash
DB_TYPE=sqlite
DB_FILE_PATH=./db.sqlite3
```

#### MySQL/MariaDB
```bash
DB_TYPE=mysql
DB_HOST=localhost
DB_PORT=3306
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database
```

#### PostgreSQL
```bash
DB_TYPE=postgres
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database
```

### Production Deployment Steps

#### Option 1: Using MySQL (Recommended)

1. **Install MySQL dependencies:**
   ```bash
   pip install tortoise-orm[asyncmy]
   ```

2. **Set environment variables:**
   ```bash
   export DB_TYPE=mysql
   export DB_HOST=your-mysql-host
   export DB_PORT=3306
   export DB_USER=your_username
   export DB_PASSWORD=your_password
   export DB_NAME=your_database
   ```

3. **Create database:**
   ```sql
   CREATE DATABASE your_database CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

4. **Run migrations:**
   ```bash
   aerich upgrade
   ```

#### Option 2: Using PostgreSQL

1. **Install PostgreSQL dependencies:**
   ```bash
   pip install tortoise-orm[asyncpg]
   ```

2. **Set environment variables:**
   ```bash
   export DB_TYPE=postgres
   export DB_HOST=your-postgres-host
   export DB_PORT=5432
   export DB_USER=your_username
   export DB_PASSWORD=your_password
   export DB_NAME=your_database
   ```

3. **Create database:**
   ```sql
   CREATE DATABASE your_database;
   ```

4. **Run migrations:**
   ```bash
   aerich upgrade
   ```

### Docker Deployment

For Docker, you can use environment variables in `docker-compose.yml`:

```yaml
services:
  app:
    environment:
      - DB_TYPE=mysql
      - DB_HOST=mysql
      - DB_PORT=3306
      - DB_USER=app_user
      - DB_PASSWORD=secure_password
      - DB_NAME=vue_fastapi_admin
  
  mysql:
    image: mysql:8.0
    environment:
      MYSQL_DATABASE: vue_fastapi_admin
      MYSQL_USER: app_user
      MYSQL_PASSWORD: secure_password
      MYSQL_ROOT_PASSWORD: root_password
```

### Hosting Provider Examples

#### Heroku
```bash
# Uses PostgreSQL by default
export DB_TYPE=postgres
export DB_HOST=$DATABASE_URL  # Heroku provides this
```

#### DigitalOcean/AWS/Railway
- Use their managed MySQL or PostgreSQL services
- Set environment variables according to their provided credentials

### Migration from SQLite to MySQL/PostgreSQL

If you're migrating existing data:

1. Export data from SQLite:
   ```bash
   sqlite3 db.sqlite3 .dump > backup.sql
   ```

2. Switch to MySQL/PostgreSQL (update environment variables)

3. Run migrations:
   ```bash
   aerich upgrade
   ```

4. Import data (may require conversion scripts)

### Benefits of MySQL/PostgreSQL in Production

✅ **Better Performance**: Optimized for concurrent connections  
✅ **Scalability**: Handle thousands of concurrent users  
✅ **Reliability**: ACID compliance, better transaction handling  
✅ **Backups**: Easier automated backups and point-in-time recovery  
✅ **Monitoring**: Better tools for monitoring and optimization  
✅ **Network Access**: Database can be on separate server  
✅ **Migration Support**: No issues with aerich migrations

