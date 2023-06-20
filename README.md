# Analyze


# Text Analysis and Comparison

This Python script analyzes text conversations by calculating similarity, performing sentiment analysis, and topic modeling. It can be used to compare a new text with a set of reference texts to determine similarity, sentiment scores, and the top words per topic.

## Installation

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/CalebFIN/Analyze.git
   ```

2. Navigate to the cloned repository:

   ```
   cd Analyze
   ```

3. Install the required Python libraries:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Prepare a text file (`conversation.txt`) containing the example texts. Each line in the file represents a separate text message.

   ```
   Hey, how are you?
   I'm good, thanks! What about you?
   ...
   ```

2. Run the script using the following command:

   ```
   python main.py previous_texts.txt "Hello, how have you been?"
   ```

   Replace `"Hello, how have you been?"` with the simulated text you want to compare with the reference texts.

3. The script will analyze the reference texts and compare them with the new text. It will display the similarity percentage, sentiment scores, and the top words per topic.

## Customization

- You can modify the script (`main.py`) to incorporate additional functionality or make improvements according to your specific requirements. Refer to the code comments for guidance on different sections.

- Feel free to experiment with different preprocessing techniques, feature extraction methods, or topic modeling parameters to enhance the analysis.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please submit a pull request or open an issue on the GitHub repository.

## License

This project is open source and does not have a specific license. You are free to use, modify, and distribute the code as per your requirements.
