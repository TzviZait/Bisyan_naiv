import uvicorn
import webbrowser
import time
from multiprocessing import Process


def run_classifier_server():
    print("Starting classifier server on http://127.0.0.1:8001 ...")
    uvicorn.run("api_classifier:app", host="0.0.0.0", port=8001, reload=False)


if __name__ == "__main__":
    print("Launching classifier server in a separate process...")

    classifier_process = Process(target=run_classifier_server)
    classifier_process.start()

    time.sleep(3)

    classifier_url = "http://127.0.0.1:8001/classifier-form"
    print(f"Classifier form is available at: {classifier_url}")
    webbrowser.open(classifier_url)

    classifier_process.join()
