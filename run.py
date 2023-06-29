import os 
from app import app

if __name__ == "__main__":
   app.run(debug=False, port=os.getenv('PORT') or 5000)