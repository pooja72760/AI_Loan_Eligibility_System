from flask import Flask, render_template, request, redirect, url_for, send_file
from inference import forward_chaining, backward_chaining
from database import create_database, save_application, get_applications
from secure_cloud import secure_split_file, reconstruct_file
from cloud_storage import get_cloud_files

app = Flask(__name__)
create_database()

# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Check loan eligibility
@app.route("/check", methods=["POST"])
def check_eligibility():

    applicant = {
        "age": int(request.form["age"]),
        "income": float(request.form["income"]),
        "credit_score": int(request.form["credit_score"]),
        "existing_loan": request.form["existing_loan"],
        "repayment_history": request.form["repayment_history"]
    }

    # Forward Chaining
    forward_result, forward_reasons = forward_chaining(applicant)

    # Backward Chaining
    backward_result, backward_reasons = backward_chaining(applicant)

    # Final decision
    if forward_result == "ELIGIBLE" and backward_result == "ELIGIBLE":
        final_decision = "ELIGIBLE"
    else:
        final_decision = "NOT ELIGIBLE"

    # Risk level
    if final_decision == "NOT ELIGIBLE":
        risk_level = "HIGH"
    elif applicant["credit_score"] >= 750 and applicant["income"] >= 40000:
        risk_level = "LOW"
    else:
        risk_level = "MEDIUM"
        
    save_application(
    applicant["age"],
    applicant["income"],
    applicant["credit_score"],
    applicant["existing_loan"],
    applicant["repayment_history"],
    final_decision,
    risk_level
    )    

    return render_template(
        "result.html",
        decision=final_decision,
        risk=risk_level,
        forward_result=forward_result,
        backward_result=backward_result,
        reasons=forward_reasons
    )
@app.route("/history")
def history():

    applications = get_applications()

    return render_template(
        "history.html",
        applications=applications
    )
@app.route("/cloud")
def cloud_storage():

    cloud_files = get_cloud_files()

    return render_template(
        "cloud.html",
        cloud_files=cloud_files
    )

@app.route("/upload", methods=["GET", "POST"])
def upload_document():

    if request.method == "POST":

        application_id = request.form["application_id"]
        document = request.files["document"]

        if document:

            filename = document.filename

            input_path = "uploads/" + filename

            document.save(input_path)

            secure_folder = "secure_storage/application_" + application_id

            blocks = secure_split_file(
                input_path,
                secure_folder
            )
            with open(
                secure_folder + "/filename.txt",
                "w"
            ) as file:
                file.write(filename)

            return render_template(
                "upload.html",
                success=True,
                application_id=application_id,
                filename=filename
            )

    return render_template("upload.html")
@app.route("/download/<application_id>/<filename>")
def download_document(application_id, filename):

    secure_folder = "secure_storage/application_" + application_id

    output_file = "downloads/" + filename

    import os
    os.makedirs("downloads", exist_ok=True)

    reconstruct_file(
        secure_folder,
        output_file
    )

    return send_file(
        output_file,
        as_attachment=True,
        download_name=filename
    )
if __name__ == "__main__":
    app.run(debug=True)