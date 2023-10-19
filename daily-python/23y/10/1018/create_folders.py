import xml.etree.ElementTree as ET
import os

def create_folders(node, parent_path):
    node_name = node.get("name")
    current_path = os.path.join(parent_path, node_name)
    os.makedirs(current_path, exist_ok=True)
    for child in node.findall("node"):
        create_folders(child, current_path)

tree = ET.parse('data.xml')
root = tree.getroot()

current_path = os.path.dirname(os.path.abspath(__file__))

create_folders(root, current_path)
