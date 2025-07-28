from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from classifier import Classifier
from train_bisean_naiv import Geting_Data
from typing import List, Dict, Any

app = FastAPI()

trained_data: Dict[str, Any] = {}

@app.on_event("startup")
async def train_on_startup():
    global trained_data
    data_path = "buy_computer_data.csv"
    uniq_column = "Buy_Computer"
    trained_data = Geting_Data.return_data(data_path, uniq_column)
    print("Training completed")

@app.get("/classifier")
async def classifier(features: str = Query(..., description="Comma-separated features, e.g., youth,high,desktop")):
    try:
        specific_data: List[str] = Classifier.data_classifier(features)
        result: Dict[str, float] = Classifier.return_calculete(trained_data, specific_data)
        final_result = Classifier.print_result(result)
        return final_result
    except Exception as e:
        return {"error": str(e)}

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
