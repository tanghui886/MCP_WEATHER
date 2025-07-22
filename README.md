# mcp_weather

## 项目简介

mcp_weather 是一个基于 MCP（Model Context Protocol）协议的天气查询服务端项目。
它是通过用户输入或者模型智能判断输入城市 地区，使用spider获取中国天气网站未来7天的天气信息。

![Weather Demo](https://img.shields.io/badge/version-1.0.0-blue) 
![Python](https://img.shields.io/badge/Python-3.13%2B-green)
### 主要功能

- 城市未来7天天气查询
- 支持用户输入或大模型智能匹配城市/地区参数
- 支持SSE和stdio两种传输方式
- 轻量级部署，易于集成

## 快速开始

### 本地运行

#### 1. 克隆仓库
```bash
git clone https://github.com/tanghui886/MCP_WEATHER.git
cd MCP_WEATHER
```
#### 2. 安装依赖
```bash
pip install -r requirements.txt
```
#### 3. 启动服务
```bash
python -m mcpserver.get_weather_mcpserver --port 8000 --transport sse
```
参数说明:

--port: 服务监听端口，默认 8000

--transport: 传输方式，支持 stdio 或 sse
________________________________________
主要接口/工具
•	get_weather：查询天气信息
		参数：input_str（城市 地区）
		输入示例：北京 海淀
________________________________________
### MCP sever configuration

~~~json
{
    "mcpServers": {
        "MCP_WEATHER": {
            "command": "npx",
            "args": [
                "-y",
                "MCP_WEATHER"
            ]
        }
    }
}
~~~
________________________________________
### 项目结构
~~~text
MCP_WEATHER/
├── fc/                     # 功能模块
│   └── get_weather.py      # 天气获取主逻辑
├── mcpserver/              # MCP服务端
│   ├── __init__.py
│   └── get_weather_mcpserver.py  # 服务启动入口
├── spider/                 # 爬虫模块
│   ├── get_city_list.py    # 城市列表获取
│   └── get_weather_by_cityId.py  # 根据城市ID获取天气
├── README.md               # 项目文档
└── requirements.txt        # 依赖列表
~~~
________________________________________
联系方式
~~~text
维护者github: tanghui886

邮箱: 471450059@qq.com

问题反馈: GitHub Issues
~~~
