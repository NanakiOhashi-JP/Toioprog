from graphviz import Digraph

# Create a flowchart
flowchart = Digraph("Toio_Flowchart", format="png")

# Add nodes
flowchart.node("Start", "Start (main)", shape="ellipse")
flowchart.node("ConnectCube", "Connect to SimpleCube ('m78')", shape="box")
flowchart.node("GetName", "Get Cube Name", shape="box")
flowchart.node("PrintName", "Print Cube Name", shape="box")
flowchart.node("Move1", "Move to (30, -50, 50)", shape="box")
flowchart.node("Orient1", "Set Orientation (15, 30)", shape="box")
flowchart.node("Move2", "Move to (30, 0, 56)", shape="box")
flowchart.node("Orient2", "Set Orientation (15, 120)", shape="box")
flowchart.node("Move3", "Move to (30, 50, -50)", shape="box")
flowchart.node("Orient3", "Set Orientation (15, 270)", shape="box")
flowchart.node("Return", "Move to (30, -50, 50)", shape="box")
flowchart.node("End", "End", shape="ellipse")

# Add edges
flowchart.edge("Start", "ConnectCube")
flowchart.edge("ConnectCube", "GetName")
flowchart.edge("GetName", "PrintName")
flowchart.edge("PrintName", "Move1")
flowchart.edge("Move1", "Orient1")
flowchart.edge("Orient1", "Move2")
flowchart.edge("Move2", "Orient2")
flowchart.edge("Orient2", "Move3")
flowchart.edge("Move3", "Orient3")
flowchart.edge("Orient3", "Return")
flowchart.edge("Return", "End")

# Render and display the flowchart
file_path = "/mnt/data/Toio_Flowchart"
flowchart.render(file_path, view=False)

file_path + ".png"
