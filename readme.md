## 部署

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

## Bot使用

1. 输入 `/start` 指令启动机器人
2. 输入 `/muxia` +`<不多于十个字的文本消息>` 生成对应表情包