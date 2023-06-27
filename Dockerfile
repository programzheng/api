# 使用官方 Python 鏡像作為基礎鏡像
FROM python:3.7

# 設置工作目錄
WORKDIR /app

# 複製應用程式相依文件
COPY Pipfile .
COPY Pipfile.lock .

# 安裝應用程式相依
RUN pip install pipenv
RUN pipenv install --system --deploy

# 複製應用程式程式碼到工作目錄
COPY . .

# 設置環境變數
ENV FLASK_APP=app.py

# 暴露容器的端口號
EXPOSE 5000

# 執行應用程式
CMD ["flask", "run", "--host=0.0.0.0"]
