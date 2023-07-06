# import requests module
import requests
import io
from fastapi import FastAPI, Request, Response
from chat import get_markdown_content, built_content_docs
from starlette.responses import FileResponse
import os

openai_model= os.getenv("OPENAI_MODEL")

app = FastAPI()

@app.post("/translate")
async def trans_md(current_language: str, document_url: str):
    content = built_content_docs(model=openai_model,language=current_language, text=get_markdown_content(document_url))
    
    file_object = io.BytesIO(content.encode())

    # 构建响应对象，设置必要的头信息和内容
    response = Response(content=file_object.getvalue(), media_type="text/markdown")

    # 设置文件名和下载头信息
    response.headers["Content-Disposition"] = "attachment; filename=example.md"

    return response


if __name__ == "__main__":
    uvicorn.run(app, worker=4 ,host="0.0.0.0", port=8000)
