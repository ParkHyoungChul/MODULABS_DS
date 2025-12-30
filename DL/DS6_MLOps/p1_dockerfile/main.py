from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# 1. FastAPI 앱 객체 생성
app = FastAPI()

# 2. 질문-응답 모델 로드 (기본 모델)
# 처음 실행 시 모델 다운로드로 인해 시간이 다소 소요됩니다.
qa_pipeline = pipeline("question-answering")

# 3. 데이터 구조 정의 (입력 형식)
class QARequest(BaseModel):
    context: str    # 답변의 근거가 될 지문
    question: str   # 궁금한 질문

@app.get("/")
def health_check():
    return {"status": "Model is ready!"}

# 4. 실제 예측 엔드포인트
@app.post("/predict")
def answer_question(request: QARequest):
    # 모델 추론 실행
    result = qa_pipeline(question=request.question, context=request.context)
    
    return {
        "answer": result['answer'],
        "score": round(result['score'], 4)
    }