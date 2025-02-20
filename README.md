# Drink Adviser with RAG

This is my first attempt at using **Retrieval-Augmented Generation (RAG)** and **Gemini 1.5** to create a chatbot that answers questions about drinks. The chatbot leverages my Obsidian notes on drinks, providing accurate and context-aware responses based on the information stored in my files.

## Features

- **RAG Integration**: Combines retrieval-based and generative AI to provide precise answers.
- **Gemini 1.5**: Utilizes the latest advancements in natural language processing for enhanced understanding and response generation.
- **Obsidian Knowledge Base**: Pulls information from my Obsidian vault, which contains detailed notes on various drinks, recipes, and related topics.

## How It Works

1. **Input Query**: The user asks a question about drinks (e.g., "What’s the best cocktail for summer?").
2. **Retrieval**: The system retrieves relevant information from my Obsidian files.
3. **Generation**: Gemini 1.5 processes the retrieved data and generates a coherent response.
4. **Output**: The chatbot provides an accurate and contextually relevant answer.

## Example Queries

- "What’s a good non-alcoholic drink for a party?"
- "How do I make a classic mojito?"
- "What are the health benefits of green tea?"

## Future Improvements

- Expand the knowledge base by adding more drink-related notes to Obsidian.
- Fine-tune the RAG model for better accuracy and relevance.
- Add support for multi-language queries.

## Tools and Technologies

- **RAG Framework**: For retrieval-augmented generation.
- **Gemini 1.5**: For advanced natural language processing.
- **Obsidian**: As the knowledge base for drink-related information.
- **Python**: For backend development and integration.
- **Flask**: For building the chatbot API.
- **React**: For the frontend interface.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/marsh090/LANGCHAIN-RAG.git
   ```

2. Navigate to the project directory:

   ```bash
    cd LANGCHAIN-RAG
    ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   python app.py
   ```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## About Me

My name is Lucas, and I'm a backend developer with a passion for AI and machine learning. I created this project as a way to explore the capabilities of RAG and Gemini 1.5.


<div align="center">
    <p>
        You can find more of me on my Github profile:
    </p>
    <a href="https://github.com/marsh090">
        <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/6fc51b6e7fe44a0464e80663634fce034aa17033/icons/github.svg" width="50">
    </a>
</div>
