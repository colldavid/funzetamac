# app.py
from flask import Flask, request

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
  <body style="margin:0; font-family:sans-serif;">
    <div style="position:absolute; top:10px; left:10px;">
      <div>hello world</div>
      <form method="POST" style="margin-top:8px;">
        <input name="text" type="text" placeholder="type here…"
               style="width:240px; padding:4px;" value="{value}">
        <button type="submit" style="padding:4px 8px; margin-left:4px;">Submit</button>
      </form>
      {output}
    </div>
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = (request.form.get("text") or "").strip()
        out = f'<div style="margin-top:8px; color:#555;">You typed: {text}</div>'
        return HTML.format(value=text, output=out)
    # GET
    return HTML.format(value="", output="")

if __name__ == "__main__":
    app.run(debug=True)
