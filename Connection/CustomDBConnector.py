import pyodbc

def Connect_To_Export_SQLSRV():
    server = "LCITDBSRV,1433"  # เซิร์ฟเวอร์
    database = "Customs_Interchange"  # ฐานข้อมูล
    user = "sa"  # ชื่อผู้ใช้
    password = "J*n8k3FV2N"  # รหัสผ่าน
    
    try:
        # เชื่อมต่อฐานข้อมูล SQL Server โดยใช้ User และ Password
        conn = pyodbc.connect(
            f"DRIVER={{SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={user};"
            f"PWD={password};"
        )
        # print("Connected to the database successfully.")
        return conn
    except pyodbc.Error as e:
        print(f"Error connecting to the database: {e}")
        return f"Error connecting to the database: {e}"

def close_connection(conn):
    try:
        if conn is not None and conn.closed == 0:  # ตรวจสอบว่าเชื่อมต่ออยู่หรือไม่
            conn.close()
            print("Database connection closed successfully.")
        else:
            print("Connection already closed or not established.")
    except Exception as e:
        print(f"Error closing connection: {e}")