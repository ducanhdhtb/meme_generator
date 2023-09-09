1.Installation
    Clone the repository: git clone <repository-url>
    Navigate to the project directory: cd meme-generator
2.Create a virtual environment: python3 -m venv venv
3.Activate the virtual environment:
    For Windows: venv\Scripts\activate
    For macOS/Linux: source venv/bin/activate
4.Install the required dependencies: pip install -r requirements.txt

5.Usage
    Command Line Tool
    To use the command line tool, run the following command:

    python main.py --body "Quote body" --author "Quote author" --image "path/to/image.jpg"
If any argument is not defined, a random selection will be used.

6.Web Service
To run the web service, execute the following command:
python app.py

Access the web service at http://127.0.0.1:5000 in your browser.
Use the web interface to enter the quote body, author, and image URL to generate a meme.


** Library Requirement
Pillow - Python Imaging Library
python-docx - Python library for creating and updating Microsoft Word (.docx) files
pandas - Python library for data manipulation and analysis
Flask - Python web framework
requests - Python library for making HTTP requests


