from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

facts = [
    "Wind turbines can be taller than 200 meters.",
    "The Eiffel Tower can grow 15 cm in summer due to heat expansion.",
    "Concrete is the most widely used man-made material.",
    "The first mechanical computer was designed by Charles Babbage.",
    "Bridges are designed to withstand both tension and compression forces.",
    "The world's longest bridge is over 164 kilometers long (Danyang–Kunshan Grand Bridge, China).",
    "The Burj Khalifa is 828 meters tall, the tallest building in the world.",
    "Airplanes are struck by lightning on average once a year but are designed to handle it safely.",
    "The Panama Canal uses massive locks to lift and lower ships.",
    "The Large Hadron Collider is the world's largest and most powerful particle accelerator.",
    "Roller coasters use gravity and momentum, not motors, for most of the ride.",
    "The Golden Gate Bridge cables contain over 27,000 individual wires.",
    "Steel expands when heated, which is why expansion joints are used in bridges.",
    "Hydraulic systems use incompressible fluids to transfer force efficiently.",
    "3D printing is now used to build houses in under 24 hours."
]

@app.route('/')
def home():
    today = datetime.date.today()
    fact_of_the_day = facts[today.toordinal() % len(facts)]
    date_str = today.strftime("%B %d, %Y")  # e.g., July 15, 2025

    return render_template_string('''
        <html>
        <head>
            <title>Daily Engineering Fact</title>
            <style>
                body {font-family: Arial; display: flex; justify-content: center; align-items: center; height: 100vh; background: #f2f2f2;}
                .card {background: white; padding: 30px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.2); text-align: center; max-width: 400px;}
                h1 {color: #333; font-size: 24px;}
                p {font-size: 18px; color: #555; margin-top: 15px;}
                .date {font-size: 14px; color: gray; margin-bottom: 10px;}
            </style>
        </head>
        <body>
            <div class="card">
                <div class="date">{{ date }}</div>
                <h1>⚙ Daily Engineering Fact</h1>
                <p>{{ fact }}</p>
            </div>
        </body>
        </html>
    ''', fact=fact_of_the_day, date=date_str)

if __name__ == '__main__':
    app.run(debug=True)
