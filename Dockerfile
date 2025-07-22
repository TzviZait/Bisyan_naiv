# תמונת בסיס של Python 3.11
FROM python:3.11-slim

# עדכון pip לגרסה העדכנית
RUN pip install --no-cache-dir --upgrade pip

# הגדרת תיקיית עבודה בתוך הקונטיינר
WORKDIR /app

# העתקת קובץ התלויות והתקנתן
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# העתקת כל קבצי הפרויקט
COPY . .

# חשיפת הפורט שבו FastAPI ירוץ
EXPOSE 8000

# הרצת האפליקציה עם uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]