[Bilingual-AI-Assistant ]

Local AI chatbot supporting Arabic &amp; English. Uses Sentence Transformers for semantic search and a pre-built JSON database.Answers questions about Data Science, ML, DL, CV, and NLP. Also handles basic conversations like greetings, how are you, and goodbye.

 [Features]
- 🌐 Bilingual (Arabic/English).
- 🧠 Semantic search with Sentence Transformers.                                   
- 📚 Pre-built knowledge base.
- 🎨 Modern UI with dark mode.
- ⚡ Fast & local (no API needed).

   [Required libraries for the Chatbot project]
  
   -flask.
   -sentence-transformers.
   -langdetect.                |
   -numpy.                     |              
                               |_ _ _  _ _ _ _ _  pip install flask sentence-transformers langdetect numpy
                                                  pip install -r requirements.txt
 [How to Run]
 ⚡Clone the repository⚡
  (1) git clone https://github.com/your-username/Bilingual-AI-Assistant.git                       
  (2) cd Bilingual-AI-Assistant
                                                                    
  ⚡Create a virtual environment (optional but recommended)⚡
  (3)  Windows:                       Linux / Mac:                                                
       python -m venv venv            python3 -m venv venv
       venv\Scripts\activate          source venv/bin/activate
  
  (4) pip install -r requirements.txt    ⚡Install required libraries⚡                                                    
  (5) python build_vectors.py            ⚡Build the vector database (run once) ⚡                                                                           
  (6) python app.py                      ⚡Run the chatbot⚡                                                                           
  (7) http://127.0.0.1:5000              ⚡Open your browser and go to⚡

  


                                                            
