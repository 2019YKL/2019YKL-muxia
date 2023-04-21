1. Git clone 本项目文件

2. 创建 `docker-compose.yml` 文件，写入你的Token

3. 拉取镜像 
    ```
    docker pull jk2077/muxia_bot:latest
    ```

4. 构建并启动

    ```
    docker-compose build
    docker-compose up -d
    ```