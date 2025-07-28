

from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from classifier import Classifier
import httpx
from typing import List, Dict, Any

app = FastAPI()

@app.get("/classifier", response_model=str)
async def classifier(features: str = Query(..., description="Comma-separated features, e.g., youth,high,desktop")):
    async with httpx.AsyncClient() as client:
        try:
            column_response = await client.get("http://running_server1:8000/get-selected-column")
            column_response.raise_for_status()
            column = column_response.json().get("column", "Buy_Computer")

            response = await client.get(f"http://running_server1:8000/trainer?column={column}")
            response.raise_for_status()
            trainer_data: Dict[str, Any] = response.json()
        except httpx.RequestError as e:
            return {"error": f"Failed to fetch data from /trainer: {str(e)}"}

    specific_data: List[str] = Classifier.data_classifier(features)
    result: Dict[str, float] = Classifier.return_calculete(trainer_data, specific_data)
    new_result = Classifier.print_result(result)
    return new_result

@app.get("/classifier-form", response_class=HTMLResponse)
async def classifier_form():
    html_content = """
    <html>
        <head>
            <title>Classifier Input Form</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                h2 { color: #333; }
                label { font-size: 16px; }
                input[type="text"] { width: 300px; padding: 8px; margin: 10px 0; }
                input[type="submit"] { padding: 10px 20px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
                input[type="submit"]:hover { background-color: #45a049; }
            </style>
        </head>
        <body>
            <h2>Enter Your Features</h2>
            <form action="/classifier" method="get">
                <label for="features">Features (comma-separated, e.g., youth,high,desktop):</label><br>
                <input type="text" id="features" name="features" required><br><br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)