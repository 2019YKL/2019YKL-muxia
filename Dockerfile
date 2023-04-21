# 使用官方Python镜像作为基础
FROM python:3.10

# 设置工作目录
WORKDIR /app

# 将bot文件夹中的所有文件复制到容器的/app文件夹
COPY bot/ /app

# 将asset文件夹复制到容器的/app/asset文件夹
COPY asset/ /app/asset

# 将根目录中的requirements.txt复制到容器的/app文件夹
COPY requirements.txt /app

# 安装依赖项
RUN pip install --no-cache-dir -r requirements.txt

# 运行Python脚本
CMD ["python", "main.py"]
