from fastapi import HTTPException
from database import database_instance  # Correct import of the 'database' class

class StaffDetails:
    def get_staffdetails(self):
        # Establishing the database connection using the static method
        connection = database_instance.get_db_connection()
        if not connection:
            raise HTTPException(status_code=500, detail="Failed to connect to the database")
        
        cursor = connection.cursor(dictionary=True)
        
        try:
            cursor.execute("SELECT * FROM staffdetails")  # Query to fetch staffdetails data
            staffdetails_members = cursor.fetchall()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching data from the database: {str(e)}")
        finally:
            cursor.close()  # Ensure the cursor is closed after the operation
            connection.close()  # Ensure the connection is closed after the operation
        
        if not staffdetails_members:
            raise HTTPException(status_code=404, detail="No staff details found")
        
        return staffdetails_members  # Return the result as JSON

# Create an instance of the StaffDetails class
staffdetails_instance = StaffDetails()  # This is correct; no changes needed here
