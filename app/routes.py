from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    experiences = [
        {
            "title": "AI and Process Optimization Analyst",
            "company": "Korah Limited",
            "period": "Sep 2024 – Present",
            "details": [
                "Developed AI algorithms predicting NICU bed availability, reducing transfer decision time by 25%.",
                "Designed and optimized a SQL database, improving data retrieval speed by 35%.",
                "Implemented Test-Driven Development (TDD), achieving 100% unit test coverage."
            ]
        },
        {
            "title": "Artificial Intelligence Research Assistant",
            "company": "Sheridan Centre for Applied AI",
            "period": "Oct 2023 – Sep 2024",
            "details": [
                "Created a chatbot solving 90% of queries with 40% faster response time.",
                "Developed Retrieval Augmented Generation (RAG) systems for accuracy improvement."
            ]
        }
    ]
    return render_template('index.html', title="Home", experiences=experiences)
