import base64
import matplotlib.pyplot as plt
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,4))
    if chart_type == '#10':
        plt.bar(data['Name'], data['Age'])
        print('Scatter chart')
    plt.tight_layout()
    chart = get_graph()
    return chart
