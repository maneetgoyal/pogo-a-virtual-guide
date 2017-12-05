# Pogo
A Programming Project Advisor: 
Project for CSE 6242 which aims to help programmers learn faster via topic modelling and graph analytics

- Description


- Installation
- Setting up Neo4j for the Dependency Graph.
1. Download and install Neo4j (https://neo4j.com/download/)
2. Create a new Project in the Neo4j desktop and a new Database under that project.
3. Click on the "Open Folder" option in your database and then navigate to data/databases folder.
4. Copy the graph.db folder from DependencyGraphDb/data folder in GitHub/source code and paste it inside the data/databases folder of Step 3 (replace if graph.db already exists).
5. Click on the Start button to bring up the Neo4j graph database.
6. Wait until the 'Status' changes from "STARTING" to "RUNNING".


- Execution
To run the UI, please setup a localhost in the InputForm folder in GitHub/source code.
A localhost can be set up by running "python -m SimpleHTTPServer 8080" (or any other port number) in the folder.
Once the localhost is up, open any web browser and go to the URL: "http://localhost:8080/input.html"
The UI will be up and ready for use.
