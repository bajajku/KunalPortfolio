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
                "Developed AI algorithms to predict NICU bed availability, reducing transfer decision time by 25%.",
                "Designed and optimized a SQL database, improving data retrieval speed by 35% for real-time decision-making.",
                "Implemented Test-Driven Development (TDD) practices, achieving 100% unit test coverage and reducing post-deployment bugs by 30%."
            ]
        },
        {
            "title": "Artificial Intelligence Research Assistant",
            "company": "Sheridan Centre for Applied AI",
            "period": "Oct 2023 – Sep 2024",
            "details": [
                "Received Sheridan’s Generator Student Award for Innovation in Research for contributions to this project.",
                "Researched and implemented state-of-the-art AI techniques, focusing on NLP and LLM, to create a chatbot for Oakville Public Library (OPL) that solved 90% of user queries accurately.",
                "Implemented a Retrieval Augmented Generation (RAG) system to enhance the chatbot’s accuracy and efficiency by over 80%.",
                "Developed a robust API using FAST API for the backend and designed a user-friendly frontend, reducing response time by 40% while integrating advanced NLP algorithms with the chatbot."
            ]
        },
        {
            "title": "Software Developer",
            "company": "Sheridan Centre for Applied AI (CAAI)",
            "period": "May 2024 – August 2024",
            "details": [
                "Implemented a communication layer for wearable sensors, optimizing data transfer speed by 20% and enhancing overall system integration.",
                "Developed software solutions using Arduino IDE with C++ for ESP32 hardware interfacing and Node-RED with JavaScript for backend integration, achieving 99% system reliability.",
                "Communicated technical specifications effectively between cross-functional teams from multiple colleges."
            ]
        }
    ]
    return render_template('index.html', title="Home", experiences=experiences)
