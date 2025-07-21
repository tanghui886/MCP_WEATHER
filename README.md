# mcp_weather

## 项目简介

mcp_weather 是一个基于 MCP（Model Context Protocol）协议的天气查询服务端项目。
它是通过用户输入或者模型智能判断输入城市 地区，使用spider获取中国天气网站未来7天天气信息。

### 主要功能

•	城市未来7天天气查询
•	通过用户输入或者大模型智能匹配输入城市 地区等参数，查询该城市未来7天的天气信息。
________________________________________
## <div align="center">⚙️Installation</div>

~~~bash
git clone https://github.com/tanghui886/MCP_WEATHER.git
npm i
~~~


## <div align="center">▶️Quick Start</div>

### CLI
~~~bash
npx -y MCP_WEATHER
~~~

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
主要接口/工具
•	get_weather：查询火车票信息
		参数：input_str（城市 地区）
		输入示例：北京 海淀
________________________________________
项目结构
MCP_WEATHER/
├── fc
		└── get_weather.py
├──mcpserver
		└──get_weather_mcpserver.py
├──spider
		├──get_city_list.py
		└──get_weather_by_cityId.py
├── README.md
└── requirements.txt
________________________________________
贡献与反馈
如有疑问可联系维护者：471450059@qq.com

