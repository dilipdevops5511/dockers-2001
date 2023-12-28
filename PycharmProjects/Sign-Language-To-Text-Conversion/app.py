import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)


# Define an endpoint where you want to run the Python script
@app.route('/run-python-script', methods=['POST'])
def run_python_script():
    try:
        # Path to your Python script
        python_script_path = './Application.py'

        # Run the Python script using subprocess
        subprocess.run(['python', python_script_path], check=True, shell=True)

        result = "Python script executed successfully."
        return jsonify({'result': result})

    except Exception as e:
        error_message = str(e)
        return jsonify({'error': error_message}), 500  # Return a 500 Internal Server Error on failure


if __name__ == '__main__':
    app.run(debug=True)
