from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    er = None
    if request.method == "POST":
        try:
            jumlah_likes = int(request.form["likes"])
            jumlah_comment = int(request.form["comments"])
            jumlah_share = int(request.form["shares"])
            jumlah_follower = int(request.form["followers"])

            if jumlah_follower == 0:
                return "Jumlah pengikut tidak boleh nol!"
            
            # Hitung Engagament Rate
            er = ((jumlah_likes + jumlah_comment + jumlah_share) / jumlah_follower) * 100

        except ValueError:
            return "Terjadi kesalahan input. Mohon periksa kembali dan masukkan angka yang benar."
        
    return render_template("index.html", er=round(er, 2) if er is not None else None)

if __name__ == "__main__":
    app.run(debug=True)