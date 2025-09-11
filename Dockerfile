# 使用官方 Python 镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# Back4App 要求监听 8080 端口
EXPOSE 8080

# 使用 gunicorn 启动 Flask (app.py 里的 app 实例)
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
