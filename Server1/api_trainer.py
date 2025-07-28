
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from train_bisean_naiv import Geting_Data
from typing import Dict, Any

app = FastAPI()

selected_column = "Buy_Computer"

@app.get("/trainer")
async def trainer(column: str = Query("Buy_Computer", description="Column name for training, e.g., Buy_Computer")) -> Dict[str, Any]:
    global selected_column
    selected_column = column
    try:
        result = Geting_Data.return_data('Data/buy_computer_data.csv', column)
        if not result:
            return {"error": f"No data returned for column: {column}"}
        return result
    except Exception as e:
        return {"error": f"Failed to process data for column {column}: {str(e)}"}

@app.get("/trainer-form", response_class=HTMLResponse)
async def trainer_form():
    html_content = """
    <html>
        <head>
            <title>Trainer Column Selection</title>
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
            <h2>Select Training Column</h2>
            <form action="/trainer" method="get">
                <label for="column">Column name (e.g., Buy_Computer):</label><br>
                <input type="text" id="column" name="column" required><br><br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/get-selected-column")
async def get_selected_column():
    return {"column": selected_column}