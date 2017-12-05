# Pogo
A Programming Project Advisor: 
Project for CSE 6242 which aims to help programmers learn faster via topic modelling and graph analytics

Description
This is the code that has gone into the making of Pogo. It includes the following:

1. Input and Output form (Front-end elements)
2. Data preprocessing scripts: Preprocessing of Stack Overflow, GitHub and Libraries.io data acquired from Google BigQuery.
3. Graph Analytics: An implementation of suggestions for user query(input) as well as a dependency graph for packages(output) using the neo4j graph database on the Libraries.io dataset. 
4. Topic Modelling: An implementation of a two-fold LDA(Latent Dirichlet Association) model on Stack Overflow question tags and titles to obtain buzzing topics.

Installation
Setting up Neo4j for the Dependency Graph.
1. Download and install Neo4j (https://neo4j.com/download/)
2. Create a new Project in the Neo4j desktop and a new Database under that project.
3. Click on the "Open Folder" option in your database and then navigate to data/databases folder.
4. Copy the graph.db folder from DependencyGraphDb/data folder in GitHub/source code and paste it inside the data/databases folder of Step 3 (replace if graph.db already exists).
5. Click on the Start button to bring up the Neo4j graph database.
6. Wait until the 'Status' changes from "STARTING" to "RUNNING".

Installing Python libraries for topic modelling and natural language processing ( Python 3.x needed to run code)
1. Ensure latest version of pip is running by using the following command on cmd/terminal:

       Windows:  python -m pip install -U pip
       
       
       Linux or macOS: pip install -U pip
       
2. Install spacy using the following command (For Windows OS use py -X before pip on cmd where X is python version. Eg : py -3 for python 3):

       Windows, Linux or macOS:: pip install spacy
       
3. Download the spacy en-core-wb-sm model

       python -m spacy download en_core_wb_sm
       
4. Install gensim


      pip install -U gensim
      
      
5. Install pandas and numpy


      pip install -U pandas
      
      
     
      pip install -U numpy
 
 
 

Execution
To run the UI, please setup a localhost in the InputForm folder in GitHub/source code.
A localhost can be set up by running "python -m SimpleHTTPServer 8080" (or any other port number) in the folder.
Once the localhost is up, open any web browser and go to the URL: "http://localhost:8080/input.html"
The UI will be up and ready for use.
