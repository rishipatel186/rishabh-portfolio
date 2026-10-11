import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

def generate_resume(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#111827'),
        alignment=1 # Center
    )
    
    headline_style = ParagraphStyle(
        'HeadlineStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#4B5563'),
        alignment=1 # Center
    )

    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#374151'),
        alignment=1 # Center
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#1F2937'),
        spaceAfter=3,
        textTransform='uppercase'
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#374151')
    )

    entry_title = ParagraphStyle(
        'EntryTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=colors.HexColor('#111827')
    )

    entry_subtitle = ParagraphStyle(
        'EntrySubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#4B5563')
    )

    entry_date = ParagraphStyle(
        'EntryDate',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#6B7280'),
        alignment=2 # Right
    )

    skill_label = ParagraphStyle(
        'SkillLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#1F2937')
    )

    elements = []

    # Header
    elements.append(Paragraph("RISHABH PATEL", name_style))
    elements.append(Paragraph("Full-Stack Developer | MERN Stack Developer | AI &amp; Automation Enthusiast", headline_style))
    elements.append(Spacer(1, 3))
    
    contact_line = (
        'Gujarat, India &nbsp;|&nbsp; '
        '<a href="mailto:jp0578171@gmail.com" color="#2563EB"><u>jp0578171@gmail.com</u></a> &nbsp;|&nbsp; '
        '<a href="https://patelrishabh.me" color="#2563EB"><u>patelrishabh.me</u></a> &nbsp;|&nbsp; '
        '<a href="https://github.com/rishipatel186" color="#2563EB"><u>github.com/rishipatel186</u></a> &nbsp;|&nbsp; '
        '<a href="https://linkedin.com/in/rishabh-patel-984637372/" color="#2563EB"><u>linkedin.com/in/rishabh-patel-984637372</u></a>'
    )
    elements.append(Paragraph(contact_line, contact_style))
    elements.append(Spacer(1, 6))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1F2937'), spaceAfter=8))

    # Professional Summary
    elements.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#D1D5DB'), spaceAfter=4))
    summary_text = (
        "MCA student at CHARUSAT with a strong interest in full-stack web development and modern JavaScript "
        "technologies. Familiar with building web applications using React.js, Node.js, Express.js, and MongoDB. "
        "Interested in practical software development, responsive interfaces, API integration, and AI-assisted automation. "
        "Focused on strengthening development skills through hands-on projects and continuous learning."
    )
    elements.append(Paragraph(summary_text, body_style))
    elements.append(Spacer(1, 7))

    # Education
    elements.append(Paragraph("EDUCATION", section_heading))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#D1D5DB'), spaceAfter=4))
    
    # MCA
    t1 = Table([
        [Paragraph("<b>Master of Computer Applications (MCA)</b>", entry_title), Paragraph("2026 &ndash; 2027 (Semester 1)", entry_date)],
        [Paragraph("CHARUSAT University &mdash; Smt. Chandaben Mohanbhai Patel Institute of Computer Applications (CMPICA)", entry_subtitle), Paragraph("", entry_date)]
    ], colWidths=[410, 130])
    t1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 0), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    elements.append(t1)
    elements.append(Paragraph("&bull; Faculty of Computer Science and Applications (FCA) &bull; Location: Gujarat, India", body_style))
    elements.append(Spacer(1, 3))

    # BCA
    t2 = Table([
        [Paragraph("<b>Bachelor of Computer Applications (BCA)</b>", entry_title), Paragraph("2023 &ndash; 2026", entry_date)],
        [Paragraph("Undergraduate Degree &mdash; Academic Score: 72.05%", entry_subtitle), Paragraph("", entry_date)]
    ], colWidths=[410, 130])
    t2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 0), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    elements.append(t2)
    elements.append(Paragraph("&bull; Solid foundation in computer science, software engineering, DBMS, data structures, and web technologies.", body_style))
    elements.append(Spacer(1, 7))

    # Technical Skills
    elements.append(Paragraph("TECHNICAL SKILLS", section_heading))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#D1D5DB'), spaceAfter=4))
    
    skills_data = [
        [Paragraph("Programming Languages:", skill_label), Paragraph("JavaScript (ES6+), Python, C, C++, Java, C#", body_style)],
        [Paragraph("Frontend Development:", skill_label), Paragraph("HTML5, CSS3, JavaScript, React.js, Responsive Web Design", body_style)],
        [Paragraph("Backend &amp; APIs:", skill_label), Paragraph("Node.js, Express.js, RESTful APIs", body_style)],
        [Paragraph("Databases:", skill_label), Paragraph("MongoDB, SQL", body_style)],
        [Paragraph("Full-Stack Development:", skill_label), Paragraph("MERN Stack (React.js, Node.js, Express.js, MongoDB)", body_style)],
        [Paragraph("Tools &amp; Platforms:", skill_label), Paragraph("Git, GitHub, Visual Studio Code, Cursor, AI-assisted development tools", body_style)],
        [Paragraph("Other Fundamentals:", skill_label), Paragraph(".NET fundamentals, Linux fundamentals, Python fundamentals, Desktop Automation", body_style)],
    ]
    t_skills = Table(skills_data, colWidths=[140, 400])
    t_skills.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 1.5), ('TOPPADDING', (0,0), (-1,-1), 0.5), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    elements.append(t_skills)
    elements.append(Spacer(1, 7))

    # Featured Projects
    elements.append(Paragraph("FEATURED PROJECTS", section_heading))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#D1D5DB'), spaceAfter=4))

    projects = [
        ("OTT Streaming Platform", "React.js, Node.js, Express.js, MongoDB, JavaScript",
         "Full-stack video discovery and streaming application inspired by modern OTT services. Implemented movie discovery, category filtering, search functionality, favorites, and persistent watchlist backed by MongoDB and REST APIs."),
        ("Smart Study", "React.js, JavaScript, HTML5, CSS3, Node.js",
         "Educational web application designed to help students engage with study materials, featuring quizzes, summaries, and interactive study modules with intuitive responsive design."),
        ("College Event Management System", "React.js, Node.js, Express.js, MongoDB",
         "Campus event management platform focused on organizing events, student participation, schedule coordination, and simplifying administration workflows."),
        ("Ultron AI Desktop Assistant", "Python, JavaScript, Automation APIs",
         "Personal desktop assistant combining voice interaction, conversational assistance, application launching, and desktop automation to streamline routine computing tasks."),
        ("Personal Developer Portfolio & RedxChess", "React.js, TypeScript, Three.js, GSAP, Chess.js",
         "Interactive developer portfolio showcasing projects and skills with WebGL character rendering, GSAP scroll animations, and an integrated chess engine at /play.")
    ]

    for title, tech, desc in projects:
        t_proj = Table([
            [Paragraph(f"<b>{title}</b>", entry_title), Paragraph(tech, entry_date)]
        ], colWidths=[280, 260])
        t_proj.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
        elements.append(t_proj)
        elements.append(Paragraph(f"&bull; {desc}", body_style))
        elements.append(Spacer(1, 3))

    elements.append(Spacer(1, 4))

    # Experience & Development Journey
    elements.append(Paragraph("EXPERIENCE &amp; DEVELOPMENT JOURNEY", section_heading))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#D1D5DB'), spaceAfter=4))

    t_exp = Table([
        [Paragraph("<b>Software Developer Intern</b> &mdash; Maxgen Technologies Pvt Ltd", entry_title), Paragraph("2025 &ndash; 2026", entry_date)],
        [Paragraph("Ahmedabad, Gujarat &bull; Full-Stack Web Development &amp; APIs", entry_subtitle), Paragraph("", entry_date)]
    ], colWidths=[410, 130])
    t_exp.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 0), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    elements.append(t_exp)
    elements.append(Paragraph("&bull; Contributed to web application features and API integrations using React, Node.js, and MongoDB.", body_style))
    elements.append(Paragraph("&bull; Gained practical experience in engineering workflows, database operations, and maintainable software practices.", body_style))
    elements.append(Spacer(1, 3))

    t_journey = Table([
        [Paragraph("<b>Full-Stack Development &amp; Automation Projects</b> &mdash; Self-Driven Journey", entry_title), Paragraph("2024 &ndash; Present", entry_date)],
        [Paragraph("Independent Software Building &bull; India", entry_subtitle), Paragraph("", entry_date)]
    ], colWidths=[410, 130])
    t_journey.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 0), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    elements.append(t_journey)
    elements.append(Paragraph("&bull; Developing full-stack web applications connecting responsive frontend interfaces with backend APIs.", body_style))
    elements.append(Paragraph("&bull; Exploring AI-assisted development and desktop automation to solve practical programming problems.", body_style))

    doc.build(elements)
    print(f"Resume PDF successfully generated at {output_path}")

if __name__ == '__main__':
    out = os.path.abspath('d:/portfolio/reference/public/resume.pdf')
    generate_resume(out)
