from flask import Flask, render_template, request

app = Flask(__name__)

def calc_bmi(weight, height):
    bmi_value = round(weight / ((height / 100) ** 2), 2)
    return bmi_value

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi_result = None
    if request.method == 'POST':
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi_value = calc_bmi(weight, height)
        bmi_result = (bmi_value, determine_bmi_category(bmi_value))
    return render_template("bmi_calc.html", bmi_result=bmi_result)

def determine_bmi_category(bmi_value):
    if bmi_value < 18.5:
        return "Underweight"
    elif 18.5 <= bmi_value < 24.9:
        return "Normal"
    elif 25 <= bmi_value < 29.9:
        return "Overweight"
    elif 30 <= bmi_value < 34.9:
        return "Obese"
    else:
        return "Extremely Obese"

if __name__ == '__main__':
    app.run(debug=True)
