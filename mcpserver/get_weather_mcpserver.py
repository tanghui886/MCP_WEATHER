import gradio as gr

from fc.get_weather import get_weather

get_weather = gr.Interface(
    fn=get_weather,
    inputs=["text"], # 输入是一个文本框
    outputs="text",  # 输出是一个文本框
    title="天气查询",
    description="获取city district未来7天天气信息."
)
get_weather.launch(mcp_server=True) # 关键：以MCP Server模式启动