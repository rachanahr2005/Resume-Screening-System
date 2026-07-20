from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_pdf(filename, name, content):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, f"Resume: {name}")
    
    # Body
    c.setFont("Helvetica", 12)
    text_object = c.beginText(100, height - 100)
    text_object.setLeading(15)
    
    # Wrap text manually for simplicity in this script
    lines = content.split('\n')
    for line in lines:
        text_object.textLine(line)
        
    c.drawText(text_object)
    c.save()
    print(f"Created: {filename}")

# --- Resume Data ---

resumes = [
    {
        "file": "top_tier.pdf",
        "name": "Alex Rivera",
        "body": """
Summary: Innovative Full Stack Developer with 5 years experience.
Expert in Python and Django, React.js and PostgreSQL.

Technical Skills:
- Languages: Python, JavaScript, SQL, HTML5, CSS3.
- Frameworks: Django, Flask, React, Redux, Bootstrap.
- Tools: Docker, AWS EC2, S3, Git, Jenkins, Redis.
- Backend: RESTful APIs, JSON, Celery, PostgreSQL.

Experience:
Senior Developer at TechCorp. Migrated legacy apps to Django.
Optimized PostgreSQL queries and integrated AWS S3.
"""
    },
    {
        "file": "partial_match.pdf",
        "name": "Jamie Chen",
        "body": """
Summary: Creative Frontend Developer focused on UI/UX.
Highly proficient in JavaScript and modern UI libraries.

Technical Skills:
- Frontend: React, Vue.js, jQuery, HTML, CSS, SASS.
- Design: Figma, Adobe XD, Tailwind CSS.
- Tools: Git, GitHub, NPM, Webpack.

Experience:
UI Developer at Creative Agency. Developed 20+ responsive sites.
Collaborated with teams to consume RESTful APIs.
"""
    },
    {
        "file": "no_match.pdf",
        "name": "Sarah Miller",
        "body": """
Summary: Results-driven Restaurant Manager.
Proven track record of increasing revenue and satisfaction.

Skills:
- Inventory Management, Staff Training, Financial Budgeting.
- Customer Service, Food Safety Standards, Leadership.

Experience:
General Manager at The Grand Bistro. Managed a staff of 50+.
Handled payroll, vendor negotiations, and marketing.
"""
    }
]

if __name__ == "__main__":
    for res in resumes:
        create_pdf(res["file"], res["name"], res["body"])
    print("\nAll test files are ready for your Smart Resume Screener!")