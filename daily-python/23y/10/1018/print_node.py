import xml.etree.ElementTree as ET

# 读取XML文件
tree = ET.parse('data.xml')
root = tree.getroot()

# # 遍历XML数据
def process_node(node, indent=0):
    print(' ' * indent + node.get("name"))
    for child in node:
        process_node(child, indent + 2)

# 从根节点开始处理
process_node(root)
