from flask import Flask

app  = Flask(__name__)


@app.route("/")
def index():
    return {"message": "Welcome to DevOps course."}

@app.route("/health")
def health():
    return { "status": "ok" }

@app.route("/services")
def services():
    services_list = [
        "Web Development",
        "Cloud Computing",
        "DevOps",
        "Data Science"
        "Security"
    ]

    return { "services": services_list }



if __name__ == "__main__":
    app.run("0.0.0.0", 8080)