import uvicorn
import webbrowser
import time
from multiprocessing import Process


def run_trainer_server():
    print("Starting server 1 on http://127.0.0.1:8000 ...")
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=False)


if __name__ == "__main__":
    print("Launching trainer server in a separate process...")

    # הפעלת השרת בתהליך נפרד כדי לא לחסום את ההמשך
    trainer_process = Process(target=run_trainer_server)
    trainer_process.start()


    time.sleep(3)

    trainer_url = "http://127.0.0.1:8000/trainer-form"
    print(f"Trainer form is available at: {trainer_url}")
    webbrowser.open(trainer_url)

    trainer_process.join()