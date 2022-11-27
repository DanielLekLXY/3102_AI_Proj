from question_generation.pipelines import pipeline
import json
from fastapi import FastAPI

app = FastAPI()
print("Loading model...")
nlp = pipeline("question-generation")
print("Model Loaded")
@app.get('/')
def main():
    return {'response': 'ok'}


@app.get('/transformer')
def exec_transformer(captions: str):

    try:
        result = nlp(captions)
        # print(result)
        return result
        

    except Exception as e:
        print(e)
        return {'Error': e}


# if __name__ == '__main__':
#     print("Loading model...")
#     nlp = pipeline("question-generation")
#     print("Model Loaded")
#     uvicorn.run(app, host='0.0.0.0', port='8888')
