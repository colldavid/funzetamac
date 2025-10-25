from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
  <body style="margin:0; font-family:sans-serif;">
    <div style="position:absolute; top:10px; left:10px;">
      <div id="problem" style="margin-top:8px; color:#555;"></div>

      <form id="form" style="margin-top:8px;">
        <input name="text" id="text" type="text" placeholder="type here…"
               style="width:240px; padding:4px;">
        <button type="submit" style="padding:4px 8px; margin-left:4px;">Submit</button>
      </form>
      <div id="output" style="margin-top:8px; color:#555;"></div>
    </div>

    <script>
      const problem = document.getElementById('problem');
      const form = document.getElementById('form');
      const output = document.getElementById('output');

      form.addEventListener('submit', async (e) => {
        e.preventDefault(); // stop page refresh
        const text = document.getElementById('text').value;

        // send to Flask asynchronously
        const response = await fetch('/process', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({text})
        });

        const data = await response.json();
        problem.textContent = data.problem;
        output.textContent = data.output;
      });
    </script>
  </body>
</html>
"""

@app.route("/")
def index():
    return HTML

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    text = (data.get("text") or "").strip()
    # print(text)
    try:
        num = int(text)
    except:
        num = "enter an integer!!"

    num1 = np.random.randint(0,10)
    num2 = np.random.randint(0,10)
    problem = f"{num1} + {num2}"
    output = "Correct!" if num == num1+num2 else "Wrong!"
    return jsonify({"output": f"{output}",
                    "problem": problem})

if __name__ == "__main__":
    app.run(debug=True)
