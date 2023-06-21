# Analyze: Text Analysis and Author Identification

Analyze is a Python script dedicated to processing and examining text conversations, applying similarity computations, sentiment analysis, and topic modeling. The core functionality lies in comparing a new piece of text to a set of reference texts, thereby assessing similarity and predicting authorship.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/CalebFIN/Analyze.git
    ```

2. Change to the repository directory:

    ```
    cd Analyze
    ```

3. Install the necessary Python libraries using the `requirements.txt` file:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Prepare two text files named `author1.txt` and `author2.txt` containing the example texts you want to analyze. The text should be saved with UTF-8 encoding.

2. Each line in the file should represent a separate text message. For instance:

    ```
    Hey, how are you?
    I'm good, thanks! What about you?
    ...
    ```

3. Run the script with the following command:

    ```
    python main.py
    ```

4. The script will analyze the reference texts, compare them with a new text, and infer the probable author. The result will be displayed in the console.

## Customization

- You can adapt the script (`main.py`) to incorporate additional features or improvements as per your needs. Code comments provide guidance about different sections of the script.
- Feel free to experiment with different preprocessing techniques, feature extraction methods, or topic modeling parameters to optimize the analysis.

## Contributing

We welcome your contributions! If you discover any issues or have suggestions for enhancements, please open an issue or submit a pull request on the GitHub repository.

## License

This project is open source and available for anyone to use, modify, and distribute. Please ensure any derivative work provides credit and references back to this source.

## Support

If you need help with the script, please feel free to reach out or open an issue. Pull requests for improvements are more than welcome.
