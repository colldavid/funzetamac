# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <body style="margin:0; font-family:sans-serif;">
        <div style="position:absolute; top:10px; left:10px;">
          <div>hello world</div>
          <input id="box" type="text" placeholder="type here…" style="margin-top:8px; width:240px; padding:4px;" />
          <div id="out" style="margin-top:8px; color:#555;"></div>
        </div>
        <script>
          const box = document.getElementById('box');
          const out = document.getElementById('out');
          box.addEventListener('input', () => { out.textContent = box.value; });
        </script>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
