from flask import Flask, request, render_template_string
from EmotionDetection import emotion_detector

app = Flask(__name__)

HTML = """
<form method="POST">
  <input name="text">
  <input type="submit">
</form>
<p>{{result}}</p>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        text = request.form["text"]

        if text == "":
            result = "Invalid input! Please enter text."
        else:
            response = emotion_detector(text)

            if response is None:
                result = "Error in API call"
            else:
                result = f"""
                Anger: {response['anger']} <br>
                Disgust: {response['disgust']} <br>
                Fear: {response['fear']} <br>
                Joy: {response['joy']} <br>
                Sadness: {response['sadness']} <br>
                <b>Dominant Emotion: {response['dominant_emotion']}</b>
                """

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)