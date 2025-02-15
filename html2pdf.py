from weasyprint import HTML

string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Authorization for Release of Medical Information</title>
    <style>
        @page {
            size: A4;
            margin: 20mm;
        }
        body {
            font-family: Arial, sans-serif;
            font-size: 12px;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 100%;
            max-width: 800px;
            margin: auto;
            padding: 20px;
            border: 1px solid #000;
        }
        h2, h3 {
            text-align: center;
            margin-bottom: 10px;
        }
        .section {
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #ccc;
        }
        label {
            font-weight: bold;
            display: block;
            margin-top: 5px;
        }
        input, select, textarea {
            width: 100%;
            padding: 5px;
            margin-top: 3px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .checkbox-group {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Authorization for Release of Medical Information</h2>

        <div class="section">
            <h3>Patient Information</h3>
            <label>Printed Name:</label>
            <input type="text">
            
            <label>DOB:</label>
            <input type="date">
            
            <label>Former Name (if any):</label>
            <input type="text">
            
            <label>Email Address:</label>
            <input type="email">
            
            <label>Address:</label>
            <input type="text">
            
            <label>Home Phone:</label>
            <input type="text">
            
            <label>Work Phone:</label>
            <input type="text">
            
            <label>Cell Phone:</label>
            <input type="text">
        </div>

        <div class="section">
            <h3>Information to be Disclosed</h3>
            <label>Provider Name:</label>
            <input type="text">
            
            <label>Provider Address:</label>
            <input type="text">
            
            <label>City, State, Zip Code:</label>
            <input type="text">
            
            <label>Telephone Number:</label>
            <input type="text">
        </div>

        <div class="section">
            <h3>Recipient Authorization</h3>
            <label>To the attention of:</label>
            <input type="text">
            
            <label>MIT Health Location:</label>
            <select>
                <option>77 Massachusetts Ave., Room E23, Cambridge, MA 01239</option>
                <option>244 Wood St., Bldg V-110, Lexington, MA 02421</option>
            </select>
        </div>

        <div class="section">
            <h3>Medical Records to Release</h3>
            <div class="checkbox-group">
                <input type="checkbox" id="notes"><label for="notes">Admission Notes</label>
                <input type="checkbox" id="ekg"><label for="ekg">EKGs/Echo</label>
                <input type="checkbox" id="pathology"><label for="pathology">Pathology Reports</label>
                <input type="checkbox" id="progress"><label for="progress">Progress Notes</label>
                <input type="checkbox" id="xray"><label for="xray">X-Ray Reports</label>
                <input type="checkbox" id="mental_health"><label for="mental_health">Mental Health</label>
                <input type="checkbox" id="hiv"><label for="hiv">HIV Testing</label>
                <input type="checkbox" id="stds"><label for="stds">Sexually Transmitted Diseases</label>
                <input type="checkbox" id="substance_abuse"><label for="substance_abuse">Substance Abuse</label>
            </div>
        </div>

        <div class="section">
            <h3>Authorization</h3>
            <p>I understand that I do not have to sign this authorization to receive treatment...</p>
            
            <label>Patient Signature:</label>
            <input type="text">
            
            <label>Date:</label>
            <input type="date">
        </div>
    </div>
</body>
</html>
"""

# Convert to PDF
#HTML(filename="example.html").write_pdf("pof.pdf")
HTML(string=string).write_pdf("mit.pdf")
print("PDF generated successfully!")