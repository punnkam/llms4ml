from flask import Flask, request, redirect, url_for
import boto3
import os

app = Flask(__name__)
s3 = boto3.client("s3")


@app.route("/", methods=["GET"])
def index():
    return "Hello World!"


@app.route("/upload", methods=["POST"])
def upload_file_to_s3():
    if "file" not in request.files:
        return "No 'file' key in request.files", 400

    file = request.files["file"]

    if file.filename == "":
        return "No selected file", 400

    try:
        s3.upload_fileobj(
            file, os.getenv("S3_BUCKET_NAME"), file.filename  # the name of your bucket
        )
    except Exception as e:
        return str(e), 500

    return "File uploaded successfully", 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
