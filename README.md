# Weather Warning Hazardous Conditions Forecast Service

This project is a web service that allows users to subscribe to weather warnings for hazardous conditions in specified locations. Users can subscribe and unsubscribe from alerts, and the service will notify them of hazardous weather conditions via email or other notification methods.

## Features

- User subscription to hazardous weather alerts by email.
- API endpoints for subscribing and unsubscribing.
- Integration with a weather API for fetching weather data (planned).
- Notification system for sending alerts (planned).

## Getting Started

### Prerequisites

- Python 3.7+
- PostgreSQL

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/nbursa/weather_warning_service.git
   cd weather_warning_service
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   .\venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL database:**

   #### On macOS/Linux:

    - Start PostgreSQL service:

      ```bash
      brew services start postgresql
      ```

    - Create a PostgreSQL user and database:

      ```bash
      psql -h localhost -U $(whoami) -d $(whoami)
      CREATE DATABASE weather_warning;
      CREATE USER yourusername WITH PASSWORD 'yourpassword';
      GRANT ALL PRIVILEGES ON DATABASE weather_warning TO yourusername;
      \q
      ```

   #### On Windows:

    - Start PostgreSQL service from the Start menu or use the Services application to start PostgreSQL service.

    - Open the PostgreSQL command line tool (`psql`) and run:

      ```sql
      CREATE DATABASE weather_warning;
      CREATE USER yourusername WITH PASSWORD 'yourpassword';
      GRANT ALL PRIVILEGES ON DATABASE weather_warning TO yourusername;
      \q
      ```

5. **Create a `.env` file:**

   ```bash
   cp .env.example .env
   ```

   Update the `.env` file with your database credentials:

   ```env
   SQLALCHEMY_DATABASE_URI=postgresql://yourusername:yourpassword@localhost:5432/weather_warning
   ```

6. **Run database migrations:**

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

7. **Run the application:**

   ```bash
   flask run
   ```

### API Endpoints

- **Subscribe to alerts:**

  ```http
  POST /subscribe
  Content-Type: application/json
  {
    "email": "test@example.com",
    "location": "New York"
  }
  ```

- **Unsubscribe from alerts:**

  ```http
  POST /unsubscribe
  Content-Type: application/json
  {
    "email": "test@example.com"
  }
  ```

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
