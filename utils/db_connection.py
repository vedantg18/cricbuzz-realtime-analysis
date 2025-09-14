# utils/db_connection.py
import psycopg2
from psycopg2 import sql, extras
import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "LiveIPLScore")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "admin")

def get_connection():
    """
    Establish a connection to the PostgreSQL database.
    Returns:
        conn: psycopg2 connection object
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("✅ Database connection successful")
        return conn
    except Exception as e:
        print(f"❌ Error connecting to database: {e}")
        return None

def close_connection(conn):
    """
    Close the database connection.
    """
    if conn:
        conn.close()
        print("✅ Database connection closed")
