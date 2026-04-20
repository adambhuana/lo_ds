import openpyxl
import re

wb = openpyxl.load_workbook('learning_outcome_ds.xlsx')
ws = wb.active

def get_lo(row):
    """Get learning outcomes from a row, split into list"""
    lo_text = ws.cell(row, 4).value
    if not lo_text:
        return []
    # Split by pattern: "1. xxx 2. xxx 3. xxx"
    # Use regex to split on number followed by period and space
    items = re.split(r'\s*\d+\.\s+', lo_text.strip())
    # Filter out empty strings
    items = [item.strip() for item in items if item.strip()]
    return items

def lo_to_html(lo_items, indent=24):
    """Convert LO items to HTML list"""
    if not lo_items:
        return ""
    sp = ' ' * indent
    html = f'{sp}<ol class="lo-list">\n'
    for i, item in enumerate(lo_items, 1):
        html += f'{sp}    <li data-num="{i}.">{item}</li>\n'
    html += f'{sp}</ol>'
    return html

def tools_to_html(tools, indent=24):
    """Convert tools list to HTML badges"""
    if not tools:
        return ""
    sp = ' ' * indent
    html = f'{sp}<div class="tools-wrap">\n'
    for tool in tools:
        html += f'{sp}    <span class="tool-badge">{tool}</span>\n'
    html += f'{sp}</div>'
    return html

# Test the LO parsing
test_lo = get_lo(7)
print("Test LO parsing for Foundations of Data Science:")
for i, item in enumerate(test_lo, 1):
    print(f"  {i}. {item}")
print()

# ============================================================
# LEARNING TOOLS per course (aligned with CDC requirements)
# ============================================================
# CDC Categories mapped:
# 1. Software Engineering: JavaScript, Python, Java, PHP, React, Next.js, Laravel, Node.js, GitHub/GitLab, Docker
# 2. Web & CMS: WordPress, Elementor, HTML, CSS, JavaScript
# 3. DevOps: Docker, Kubernetes, CI/CD (Jenkins, GitHub Actions), Cloud (AWS, GCP, Azure), Terraform, Ansible
# 4. Data & Analytics: SQL, Excel/Google Sheets, Python (Pandas), Power BI/Tableau
# 5. QA & Testing: Test case tools, Selenium
# 6. System & Business Analyst: Draw.io/Lucidchart, Notion/Confluence
# 7. UI/UX & Product Design: Figma, Adobe XD, Maze
# 8. Product Management: Notion/Jira, Google Docs
# 9. IT Security: Kali Linux, Nmap, Wireshark
# 10. IoT: Arduino, ESP32, MQTT
# 13. Solution Engineer: Postman (API), CRM/ERP tools

learning_tools = {
    # Semester 1
    7:  ["Python", "Jupyter Notebook", "Google Colab", "Pandas", "NumPy"],
    8:  ["Figma", "Miro", "Draw.io", "Notion"],
    9:  ["Python", "MATLAB", "LaTeX"],
    10: ["Figma", "Adobe XD", "Maze", "InVision"],
    11: ["Python", "C++", "LeetCode", "GitHub"],
    12: ["Python", "R", "Excel", "SPSS"],
    13: ["Wireshark", "Cisco Packet Tracer", "Nmap"],
    14: ["Python", "MATLAB", "Wolfram Alpha", "GeoGebra"],

    # Semester 2
    18: ["Python", "Java", "GitHub/GitLab", "VS Code", "UML Tools"],
    19: ["MySQL", "PostgreSQL", "MongoDB", "SQL", "DBeaver"],
    20: ["Python", "Java", "C++", "GitHub"],
    21: ["HTML", "CSS", "JavaScript", "React", "Bootstrap", "VS Code"],
    22: ["Python", "R", "SPSS", "Pandas", "Matplotlib"],
    23: ["Wireshark", "Postman", "cURL", "MQTT"],
    24: ["Python", "Pandas", "NumPy", "OpenRefine", "Excel"],

    # Semester 3
    35: ["Node.js", "React", "Next.js", "Laravel", "Express.js", "GitHub"],
    36: ["PostgreSQL", "MongoDB", "Redis", "Cassandra", "DBeaver"],
    37: ["Python", "R", "SciPy", "SimPy"],
    38: ["Python", "MATLAB", "NumPy", "SciPy"],
    39: ["Python", "MATLAB", "Wolfram Alpha", "LaTeX"],
    40: ["Tableau", "Power BI", "D3.js", "Matplotlib", "Seaborn", "Plotly"],
    41: ["Python", "SciPy", "PuLP", "MATLAB", "Gurobi"],

    # Semester 4
    46: ["Python", "NLTK", "spaCy", "Hugging Face", "Scikit-learn"],
    47: ["SQL", "Pentaho", "Apache Spark", "Power BI", "Tableau"],
    48: ["LaTeX", "Notion", "Confluence", "Google Docs", "Markdown"],
    49: ["Flutter", "React Native", "Android Studio", "Firebase"],
    50: ["Apache Spark", "Hadoop", "Kafka", "Python", "Databricks"],
    51: ["Python", "Scikit-learn", "TensorFlow", "XGBoost", "MLflow"],
    52: ["Kali Linux", "Wireshark", "Python", "OWASP ZAP", "Nmap"],

    # Semester 5 - Concentration I: Data Engineering
    64: ["Hadoop", "Apache Spark", "HDFS", "YARN", "Mesos"],
    65: ["Apache Kafka", "ZooKeeper", "gRPC", "Docker", "Kubernetes"],
    66: ["Apache Airflow", "Luigi", "Prefect", "dbt", "Python"],
    67: ["AWS", "GCP", "Azure", "Terraform", "Docker"],
    68: ["Apache NiFi", "Talend", "Informatica", "Python", "SQL"],
    69: ["AWS S3", "Delta Lake", "Apache Iceberg", "Hive", "Presto"],

    # Semester 5 - Concentration II: AI/ML
    74: ["TensorFlow", "PyTorch", "Keras", "CUDA", "Google Colab"],
    75: ["Hugging Face", "spaCy", "NLTK", "Transformers", "GPT API"],
    76: ["OpenCV", "YOLO", "TensorFlow", "PyTorch", "Pillow"],
    77: ["OpenAI Gym", "Stable Baselines3", "PyTorch", "Ray RLlib"],
    78: ["Python", "PDDL", "A* Search", "NetworkX", "OR-Tools"],
    79: ["Docker", "FastAPI", "Flask", "MLflow", "BentoML", "AWS SageMaker"],

    # Semester 5 - Concentration III: Business Intelligence
    84: ["Tableau", "Power BI", "Looker", "Metabase", "QlikView"],
    85: ["R", "Python", "SPSS", "Stata", "Excel"],
    86: ["Python", "SQL", "Mixpanel", "Google Analytics", "HubSpot"],
    87: ["Python", "Scikit-learn", "XGBoost", "AutoML", "H2O.ai"],
    88: ["Power BI", "Tableau", "Looker", "SQL", "DAX"],
    89: ["SAP", "Oracle SCM", "Python", "Excel", "Arena Simulation"],

    # Semester 5 - Professional Ethics (common)
    71: ["Case Studies", "Notion", "IEEE/ACM Ethics Guidelines"],

    # Semester 6 - MBKM I
    116: ["Jira", "Notion", "Trello", "MS Project", "GitHub Projects"],
    117: ["Apache Airflow", "Talend", "Python", "SQL", "dbt", "Spark"],
    118: ["Python", "Pandas", "NumPy", "OpenRefine", "Great Expectations"],
    119: ["Python", "R", "Stata", "SAS", "PyMC3", "Statsmodels"],
    120: ["Power BI", "Tableau", "Google Slides", "Canva", "Prezi"],
    122: ["Presentation Tools", "Discussion Forums"],
    123: ["Presentation Tools", "Research Databases"],

    # Semester 7 - MBKM II
    127: ["Python", "Scikit-learn", "TensorFlow", "PyTorch", "MLflow", "Docker"],
    128: ["Apache Spark", "Kafka", "AWS", "GCP", "Azure", "Databricks"],
    129: ["Python", "Prophet", "ARIMA", "XGBoost", "Statsmodels"],
    130: ["OWASP ZAP", "Python", "Kali Linux", "GDPR Tools"],
    131: ["Full Stack", "Python", "Docker", "GitHub", "Cloud Platform"],
    133: ["MS Word", "LaTeX", "Turnitin"],
    134: ["Presentation Tools", "Research Databases"],

    # Semester 8
    137: ["Full Stack", "Python", "Docker", "GitHub", "Cloud Platform", "CI/CD"],
    138: ["GitHub", "Jira", "Notion", "Slack", "MS Teams"],
    139: ["GitHub Pages", "Behance", "LinkedIn", "Personal Website"],
    140: ["Figma", "Docker", "GitHub", "Cloud Platform", "Postman"],
    141: ["LaTeX", "Mendeley", "Zotero", "Google Scholar", "Turnitin"],
    142: ["LaTeX", "Mendeley", "SPSS", "Python", "Turnitin"],
    144: ["LaTeX", "Grammarly", "Mendeley", "Zotero", "MS Word"],
    145: ["SPSS", "Python", "R", "LaTeX", "Mendeley", "Google Scholar"],
}

# ============================================================
# Build the HTML
# ============================================================

html = '''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Perbaikan &amp; Penyelarasan Learning Outcomes — Program Studi Data Science</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #0f1117;
            --surface: #1a1d27;
            --surface2: #232734;
            --border: #2e3345;
            --text: #e4e6ed;
            --text-muted: #9ca0b0;
            --accent: #6c63ff;
            --accent-glow: rgba(108,99,255,.25);
            --sem1: #3b82f6;
            --sem2: #06b6d4;
            --sem3: #8b5cf6;
            --sem4: #f59e0b;
            --sem5: #10b981;
            --sem6: #ec4899;
            --sem7: #f97316;
            --sem8: #ef4444;
            --highlight-bg: linear-gradient(135deg,rgba(108,99,255,.12),rgba(59,130,246,.10));
            --highlight-border: rgba(108,99,255,.35);
            --praktik-bg: rgba(16,185,129,.12);
            --praktik-border: rgba(16,185,129,.40);
            --radius: 14px;
        }

        * { margin:0; padding:0; box-sizing:border-box; }

        body {
            font-family:'Inter',system-ui,-apple-system,sans-serif;
            background:var(--bg);
            color:var(--text);
            line-height:1.65;
            padding:0 0 80px;
        }

        /* -- Hero / Header -- */
        .hero {
            position:relative;
            overflow:hidden;
            padding:72px 40px 56px;
            text-align:center;
            background:linear-gradient(160deg,#12132a 0%,#1b1045 40%,#0e1a3a 100%);
        }
        .hero::before {
            content:'';
            position:absolute;
            inset:0;
            background:radial-gradient(ellipse 60% 50% at 50% 0%,rgba(108,99,255,.22),transparent 70%);
            pointer-events:none;
        }
        .hero h1 {
            font-size:clamp(1.6rem,3.4vw,2.6rem);
            font-weight:800;
            letter-spacing:-.02em;
            background:linear-gradient(135deg,#c7d2fe,#818cf8,#6c63ff);
            -webkit-background-clip:text;
            -webkit-text-fill-color:transparent;
            background-clip:text;
            margin-bottom:12px;
        }
        .hero .subtitle {
            font-size:clamp(.95rem,1.6vw,1.15rem);
            color:var(--text-muted);
            max-width:680px;
            margin:0 auto;
        }
        .hero .badge-row {
            margin-top:28px;
            display:flex;
            flex-wrap:wrap;
            justify-content:center;
            gap:10px;
        }
        .badge {
            display:inline-flex;
            align-items:center;
            gap:6px;
            padding:7px 16px;
            border-radius:999px;
            font-size:.78rem;
            font-weight:600;
            border:1px solid var(--border);
            background:var(--surface);
            backdrop-filter:blur(8px);
        }
        .badge.accent { border-color:var(--highlight-border); background:rgba(108,99,255,.10); color:#a5b4fc; }

        /* -- Container -- */
        .container { max-width:1440px; margin:0 auto; padding:0 28px; }

        /* -- Section titles -- */
        .section-title {
            font-size:1.45rem;
            font-weight:700;
            margin:52px 0 8px;
            display:flex;
            align-items:center;
            gap:10px;
        }
        .section-title .dot {
            width:10px;height:10px;border-radius:50%;display:inline-block;
        }

        /* -- Summary card -- */
        .summary-card {
            background:var(--surface);
            border:1px solid var(--border);
            border-radius:var(--radius);
            padding:32px 36px;
            margin:24px 0 36px;
        }
        .summary-card h3 { font-size:1.05rem; font-weight:700; margin-bottom:14px; color:#a5b4fc; }
        .summary-card ul { list-style:none; }
        .summary-card li {
            position:relative;
            padding-left:22px;
            margin-bottom:10px;
            font-size:.93rem;
            color:var(--text-muted);
        }
        .summary-card li::before {
            content:'\\2726';
            position:absolute;
            left:0;
            color:var(--accent);
            font-size:.7rem;
            top:4px;
        }

        /* -- Semester block -- */
        .semester-block {
            margin-bottom:48px;
        }
        .semester-header {
            display:flex;
            align-items:center;
            gap:14px;
            margin-bottom:18px;
        }
        .semester-header .pill {
            padding:7px 20px;
            border-radius:10px;
            font-size:.82rem;
            font-weight:700;
            color:#fff;
            text-transform:uppercase;
            letter-spacing:.04em;
        }
        .semester-header .info {
            font-size:.85rem;
            color:var(--text-muted);
        }

        /* -- Table -- */
        .lo-table {
            width:100%;
            border-collapse:separate;
            border-spacing:0;
            font-size:.84rem;
            border-radius:var(--radius);
            overflow:hidden;
            border:1px solid var(--border);
            background:var(--surface);
        }
        .lo-table thead th {
            background:var(--surface2);
            color:var(--text-muted);
            font-weight:700;
            text-transform:uppercase;
            font-size:.72rem;
            letter-spacing:.06em;
            padding:14px 16px;
            text-align:left;
            border-bottom:1px solid var(--border);
            position:sticky;
            top:0;
            z-index:2;
        }
        .lo-table tbody td {
            padding:14px 16px;
            vertical-align:top;
            border-bottom:1px solid var(--border);
        }
        .lo-table tbody tr:last-child td { border-bottom:none; }
        .lo-table tbody tr:hover { background:rgba(108,99,255,.04); }

        .lo-table .col-no { width:42px; text-align:center; font-weight:700; color:var(--text-muted); }
        .lo-table .col-mk { width:190px; font-weight:600; }
        .lo-table .col-lo { width:42%; }
        .lo-table .col-tools { width:25%; }

        .lo-table .lo-list { list-style:none; padding:0; }
        .lo-table .lo-list li { margin-bottom:7px; padding-left:18px; position:relative; }
        .lo-table .lo-list li::before {
            content:attr(data-num);
            position:absolute;
            left:0;
            font-weight:700;
            font-size:.72rem;
            color:var(--accent);
        }

        /* -- Tool badges -- */
        .tools-wrap {
            display:flex;
            flex-wrap:wrap;
            gap:6px;
        }
        .tool-badge {
            display:inline-flex;
            align-items:center;
            padding:4px 10px;
            border-radius:6px;
            font-size:.72rem;
            font-weight:600;
            background:rgba(108,99,255,.10);
            border:1px solid rgba(108,99,255,.25);
            color:#a5b4fc;
            white-space:nowrap;
            transition:all .2s ease;
        }
        .tool-badge:hover {
            background:rgba(108,99,255,.18);
            border-color:rgba(108,99,255,.45);
            transform:translateY(-1px);
        }

        /* -- Concentration Card -- */
        .concentration-card {
            background:var(--surface);
            border:1px solid var(--border);
            border-radius:var(--radius);
            padding:24px 28px;
            margin-bottom:20px;
        }
        .concentration-card h4 {
            font-size:.95rem;
            font-weight:700;
            color:#a5b4fc;
            margin-bottom:14px;
            display:flex;
            align-items:center;
            gap:8px;
        }

        /* -- Output row -- */
        .output-row {
            margin-top:8px;
            padding:10px 14px;
            border-radius:8px;
            background:rgba(245,158,11,.07);
            border:1px solid rgba(245,158,11,.25);
        }
        .output-row strong { color:#fcd34d; font-size:.78rem; }
        .output-row span { font-size:.8rem; color:var(--text-muted); }

        /* -- CDC Legend -- */
        .cdc-legend {
            background:var(--surface);
            border:1px solid var(--border);
            border-radius:var(--radius);
            padding:24px 28px;
            margin:24px 0 36px;
        }
        .cdc-legend h3 { font-size:1.05rem; font-weight:700; margin-bottom:14px; color:#a5b4fc; }
        .cdc-grid {
            display:grid;
            grid-template-columns:repeat(auto-fill, minmax(280px, 1fr));
            gap:12px;
        }
        .cdc-item {
            display:flex;
            align-items:flex-start;
            gap:10px;
            padding:10px 14px;
            border-radius:10px;
            background:rgba(108,99,255,.05);
            border:1px solid rgba(108,99,255,.12);
        }
        .cdc-item .cdc-num {
            flex-shrink:0;
            width:28px; height:28px;
            display:flex; align-items:center; justify-content:center;
            border-radius:8px;
            background:rgba(108,99,255,.15);
            color:#818cf8;
            font-size:.72rem;
            font-weight:700;
        }
        .cdc-item .cdc-info { font-size:.8rem; }
        .cdc-item .cdc-title { font-weight:600; color:var(--text); display:block; margin-bottom:2px; }
        .cdc-item .cdc-tools { color:var(--text-muted); font-size:.72rem; }

        /* -- Footer -- */
        .footer {
            margin-top:56px;
            text-align:center;
            color:var(--text-muted);
            font-size:.78rem;
            padding:24px;
            border-top:1px solid var(--border);
        }

        /* -- Export PDF Button -- */
        .export-btn {
            position:fixed;
            bottom:32px;
            right:32px;
            z-index:1000;
            display:inline-flex;
            align-items:center;
            gap:10px;
            padding:14px 28px;
            border:none;
            border-radius:14px;
            font-family:'Inter',sans-serif;
            font-size:.88rem;
            font-weight:700;
            color:#fff;
            background:linear-gradient(135deg,#6c63ff 0%,#3b82f6 100%);
            box-shadow:0 8px 32px rgba(108,99,255,.35), 0 2px 8px rgba(0,0,0,.2);
            cursor:pointer;
            transition:all .3s cubic-bezier(.4,0,.2,1);
            letter-spacing:.02em;
        }
        .export-btn:hover {
            transform:translateY(-3px) scale(1.03);
            box-shadow:0 12px 40px rgba(108,99,255,.45), 0 4px 12px rgba(0,0,0,.3);
        }
        .export-btn:active {
            transform:translateY(0) scale(.98);
        }
        .export-btn .btn-icon {
            font-size:1.15rem;
        }

        /* -- Toast notification -- */
        .toast {
            position:fixed;
            bottom:100px;
            right:32px;
            z-index:1001;
            padding:14px 24px;
            border-radius:12px;
            background:rgba(16,185,129,.95);
            color:#fff;
            font-family:'Inter',sans-serif;
            font-size:.85rem;
            font-weight:600;
            box-shadow:0 8px 24px rgba(16,185,129,.3);
            transform:translateY(20px);
            opacity:0;
            transition:all .4s cubic-bezier(.4,0,.2,1);
            pointer-events:none;
        }
        .toast.show {
            transform:translateY(0);
            opacity:1;
        }

        /* -- Responsive -- */
        @media(max-width:900px){
            .hero { padding:48px 20px 36px; }
            .container { padding:0 12px; }
            .lo-table { font-size:.78rem; }
            .lo-table thead th, .lo-table tbody td { padding:10px 10px; }
            .export-btn { bottom:20px; right:20px; padding:12px 22px; font-size:.82rem; }
            .cdc-grid { grid-template-columns:1fr; }
        }

        /* -- Print / PDF-specific styles -- */
        @media print {
            @page { size: A4 portrait; margin: 10mm 8mm; }

            /* CRITICAL: Prevent Chrome from rasterizing elements as images */
            * {
                -webkit-text-fill-color: initial;
                overflow: visible !important;
                border-radius: 0 !important;
                backdrop-filter: none !important;
                -webkit-backdrop-filter: none !important;
                filter: none !important;
                box-shadow: none !important;
                text-shadow: none !important;
                transform: none !important;
                transition: none !important;
                animation: none !important;
            }

            body {
                background: #fff !important;
                color: #000 !important;
                -webkit-text-fill-color: #000 !important;
                padding: 0 !important;
                font-size: 6.5pt !important;
                line-height: 1.35 !important;
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }

            .export-btn, .toast { display: none !important; }

            .hero {
                background: #fff !important;
                padding: 12px 8px 10px !important;
                page-break-after: avoid;
                text-align: center;
                border-bottom: 2px solid #000 !important;
                overflow: visible !important;
            }
            .hero::before { display: none !important; }
            .hero h1 {
                -webkit-text-fill-color: #000 !important;
                color: #000 !important;
                background: none !important;
                background-clip: initial !important;
                -webkit-background-clip: initial !important;
                font-size: 12pt !important;
                font-weight: 800 !important;
            }

            .hero .subtitle { color: #333 !important; -webkit-text-fill-color: #333 !important; font-size: 7pt !important; }
            .badge { background: #fff !important; border: 1px solid #999 !important; color: #000 !important; -webkit-text-fill-color: #000 !important; font-size: 5.5pt !important; padding: 2px 6px !important; }
            .badge.accent { background: #fff !important; border-color: #666 !important; color: #000 !important; -webkit-text-fill-color: #000 !important; }
            .container { max-width: 100% !important; padding: 0 2px !important; }
            .section-title { color: #000 !important; -webkit-text-fill-color: #000 !important; font-size: 9pt !important; margin-top: 10px !important; margin-bottom: 3px !important; page-break-after: avoid; border-bottom: 1px solid #000; padding-bottom: 2px; }
            .section-title .dot { background: #000 !important; }
            .summary-card, .cdc-legend { background: #fff !important; border: 1px solid #999 !important; color: #000 !important; -webkit-text-fill-color: #000 !important; padding: 6px 8px !important; margin: 4px 0 8px !important; page-break-inside: avoid; overflow: visible !important; }
            .summary-card h3, .cdc-legend h3 { color: #000 !important; -webkit-text-fill-color: #000 !important; font-size: 7pt !important; font-weight: 700 !important; }
            .summary-card li { color: #000 !important; -webkit-text-fill-color: #000 !important; font-size: 6pt !important; margin-bottom: 2px !important; }
            .summary-card li::before { color: #000 !important; -webkit-text-fill-color: #000 !important; }
            .summary-card strong { color: #000 !important; -webkit-text-fill-color: #000 !important; }
            .cdc-grid { grid-template-columns: repeat(3, 1fr) !important; gap: 4px !important; }
            .cdc-item { background: #f5f5f5 !important; border: 1px solid #ccc !important; padding: 4px 6px !important; -webkit-print-color-adjust: exact !important; }
            .cdc-item .cdc-num { background: #ddd !important; color: #000 !important; -webkit-text-fill-color: #000 !important; width: 18px !important; height: 18px !important; font-size: 5.5pt !important; -webkit-print-color-adjust: exact !important; }
            .cdc-item .cdc-info { font-size: 5.5pt !important; color: #000 !important; -webkit-text-fill-color: #000 !important; }
            .cdc-item .cdc-title { color: #000 !important; -webkit-text-fill-color: #000 !important; font-size: 6pt !important; }
            .cdc-item .cdc-tools { color: #333 !important; -webkit-text-fill-color: #333 !important; font-size: 5pt !important; }
            .semester-block { margin-bottom: 8px !important; }
            .semester-header { margin-bottom: 3px !important; }
            .semester-header .pill { background: #000 !important; color: #fff !important; -webkit-text-fill-color: #fff !important; font-size: 6pt !important; padding: 2px 8px !important; -webkit-print-color-adjust: exact !important; }
            .semester-header .info { color: #333 !important; -webkit-text-fill-color: #333 !important; font-size: 6pt !important; }

            /* Tables - remove overflow:hidden to prevent rasterization */
            .lo-table { background: #fff !important; border: 1px solid #000 !important; font-size: 5.5pt !important; border-collapse: collapse !important; overflow: visible !important; }
            .lo-table .col-no { width: 22px !important; }
            .lo-table .col-mk { width: 100px !important; font-size: 5.5pt !important; }
            .lo-table .col-lo { width: auto !important; }
            .lo-table .col-tools { width: 120px !important; }
            .lo-table thead th { background: #e0e0e0 !important; color: #000 !important; -webkit-text-fill-color: #000 !important; border: 1px solid #000 !important; font-size: 5pt !important; padding: 3px 3px !important; position: static !important; -webkit-print-color-adjust: exact !important; }
            .lo-table tbody td { color: #000 !important; -webkit-text-fill-color: #000 !important; border: 1px solid #999 !important; padding: 2px 3px !important; background: #fff !important; }
            .lo-table tbody tr:nth-child(even) td { background: #f5f5f5 !important; -webkit-print-color-adjust: exact !important; }
            .lo-table tbody tr:hover { background: transparent !important; }
            .lo-table .lo-list li { font-size: 5pt !important; margin-bottom: 1px !important; color: #000 !important; -webkit-text-fill-color: #000 !important; padding-left: 10px !important; }
            .lo-table .lo-list li::before { color: #000 !important; -webkit-text-fill-color: #000 !important; font-size: 5pt !important; }
            .tools-wrap { gap: 2px !important; }
            .tool-badge { background: #eee !important; border: 1px solid #999 !important; color: #000 !important; -webkit-text-fill-color: #000 !important; font-size: 4.5pt !important; padding: 1px 3px !important; -webkit-print-color-adjust: exact !important; }
            .concentration-card { background: #fff !important; border: 1px solid #999 !important; padding: 4px 6px !important; margin-bottom: 6px !important; page-break-inside: avoid; overflow: visible !important; }
            .concentration-card h4 { color: #000 !important; -webkit-text-fill-color: #000 !important; font-size: 7pt !important; margin-bottom: 4px !important; }
            .output-row { background: #fff !important; border: 1px solid #999 !important; }
            .output-row strong { color: #000 !important; -webkit-text-fill-color: #000 !important; }
            .output-row span { color: #333 !important; -webkit-text-fill-color: #333 !important; }
            .footer { color: #666 !important; -webkit-text-fill-color: #666 !important; border-top: 1px solid #000 !important; font-size: 6pt !important; padding: 8px !important; }
            small { color: #333 !important; -webkit-text-fill-color: #333 !important; font-size: 5pt !important; }
            strong { color: #000 !important; -webkit-text-fill-color: #000 !important; }
            h2, h3 { page-break-after: avoid !important; -webkit-text-fill-color: #000 !important; }
            tr { page-break-inside: avoid !important; }
            .semester-block { page-break-inside: auto !important; }
            .lo-table { page-break-inside: auto !important; }
        }
    </style>
</head>
<body>

<header class="hero">
    <h1>Perbaikan &amp; Penyelarasan Learning Outcomes</h1>
    <p class="subtitle">Program Studi Data Science -- Diselaraskan dengan Kebutuhan Industri &amp; Career Development Center (CDC)</p>
    <div class="badge-row">
        <span class="badge">8 Semester + 2 Short Semester</span>
        <span class="badge">152 SKS Total</span>
        <span class="badge accent">3 Concentration Tracks</span>
        <span class="badge">MBKM Semester 6 &amp; 7</span>
        <span class="badge accent">CDC-Aligned Tools</span>
    </div>
</header>

<main class="container">

    <h2 class="section-title"><span class="dot" style="background:var(--accent)"></span> Ringkasan Perbaikan</h2>
    <div class="summary-card">
        <h3>Perubahan Strategis yang Dilakukan</h3>
        <ul>
            <li>Merestrukturisasi learning outcomes agar <strong>berbasis kompetensi terukur</strong> (menggunakan kata kerja Bloom's Taxonomy: Apply, Implement, Design, Evaluate).</li>
            <li>Memperkuat mata kuliah semester awal dengan <strong>proyek praktik langsung</strong> agar mahasiswa memiliki portofolio dan siap kerja.</li>
            <li>Menambahkan <strong>jalur konsentrasi</strong> di Semester 5 untuk spesialisasi: Data Engineering, AI/ML, Business Intelligence.</li>
            <li>Mengintegrasikan <strong>program MBKM</strong> di Semester 6 dan 7 untuk pengalaman industri langsung.</li>
            <li>Menambahkan <strong>output terukur per semester</strong>: mini-project, portofolio, capstone project, dan publikasi ilmiah.</li>
            <li>Menyelaraskan kurikulum dengan <strong>kebutuhan CDC Fakultas IT</strong> sehingga lulusan siap memasuki pasar kerja.</li>
            <li>Menambahkan <strong>Learning Tools</strong> yang relevan dengan industri pada setiap mata kuliah, diselaraskan dengan kebutuhan CDC.</li>
        </ul>
    </div>

    <h2 class="section-title"><span class="dot" style="background:var(--sem5)"></span> Kebutuhan CDC Fakultas IT</h2>
    <div class="cdc-legend">
        <h3>Posisi Kerja &amp; Tools yang Dibutuhkan</h3>
        <div class="cdc-grid">
            <div class="cdc-item"><span class="cdc-num">1</span><div class="cdc-info"><span class="cdc-title">Software Engineering</span><span class="cdc-tools">JavaScript, Python, Java, React, Next.js, Laravel, Node.js, GitHub, Docker</span></div></div>
            <div class="cdc-item"><span class="cdc-num">2</span><div class="cdc-info"><span class="cdc-title">Web &amp; CMS Development</span><span class="cdc-tools">WordPress, Elementor, HTML, CSS, JavaScript</span></div></div>
            <div class="cdc-item"><span class="cdc-num">3</span><div class="cdc-info"><span class="cdc-title">DevOps &amp; Infrastructure</span><span class="cdc-tools">Docker, Kubernetes, Jenkins, GitHub Actions, AWS, GCP, Azure, Terraform</span></div></div>
            <div class="cdc-item"><span class="cdc-num">4</span><div class="cdc-info"><span class="cdc-title">Data &amp; Analytics</span><span class="cdc-tools">SQL, Excel, Python (Pandas), Power BI, Tableau</span></div></div>
            <div class="cdc-item"><span class="cdc-num">5</span><div class="cdc-info"><span class="cdc-title">QA &amp; Testing</span><span class="cdc-tools">Test case tools, Selenium</span></div></div>
            <div class="cdc-item"><span class="cdc-num">6</span><div class="cdc-info"><span class="cdc-title">System &amp; Business Analyst</span><span class="cdc-tools">Draw.io, Lucidchart, Notion, Confluence</span></div></div>
            <div class="cdc-item"><span class="cdc-num">7</span><div class="cdc-info"><span class="cdc-title">UI/UX &amp; Product Design</span><span class="cdc-tools">Figma, Adobe XD, Maze</span></div></div>
            <div class="cdc-item"><span class="cdc-num">8</span><div class="cdc-info"><span class="cdc-title">Product Management</span><span class="cdc-tools">Notion, Jira, Google Docs</span></div></div>
            <div class="cdc-item"><span class="cdc-num">9</span><div class="cdc-info"><span class="cdc-title">IT Security &amp; Cybersecurity</span><span class="cdc-tools">Kali Linux, Nmap, Wireshark</span></div></div>
            <div class="cdc-item"><span class="cdc-num">10</span><div class="cdc-info"><span class="cdc-title">IoT</span><span class="cdc-tools">Arduino, ESP32, MQTT</span></div></div>
            <div class="cdc-item"><span class="cdc-num">11</span><div class="cdc-info"><span class="cdc-title">Game Development</span><span class="cdc-tools">Unity, Unreal Engine</span></div></div>
            <div class="cdc-item"><span class="cdc-num">12</span><div class="cdc-info"><span class="cdc-title">IT Support &amp; Compliance</span><span class="cdc-tools">OS knowledge, Basic networking tools</span></div></div>
            <div class="cdc-item"><span class="cdc-num">13</span><div class="cdc-info"><span class="cdc-title">Solution Engineer</span><span class="cdc-tools">Postman (API), CRM/ERP tools</span></div></div>
        </div>
    </div>

'''

def build_semester_table(courses, indent=8):
    """Build a semester table with Learning Tools column from list of (row, name, cp) tuples"""
    sp = ' ' * indent
    sp2 = ' ' * (indent + 4)
    sp3 = ' ' * (indent + 8)
    sp4 = ' ' * (indent + 12)

    t = f'{sp}<table class="lo-table">\n'
    t += f'{sp2}<thead>\n'
    t += f'{sp3}<tr><th class="col-no">No</th><th class="col-mk">Mata Kuliah</th><th class="col-lo">Learning Outcomes</th><th class="col-tools">Learning Tools</th></tr>\n'
    t += f'{sp2}</thead>\n'
    t += f'{sp2}<tbody>\n'

    for i, (row, name, cp) in enumerate(courses, 1):
        los = get_lo(row)
        lo_html = lo_to_html(los, indent + 16)
        tools = learning_tools.get(row, [])
        tools_html = tools_to_html(tools, indent + 16)
        t += f'{sp3}<tr>\n'
        t += f'{sp4}<td class="col-no">{i}</td>\n'
        t += f'{sp4}<td class="col-mk">{name}<br><small>{cp} SKS</small></td>\n'
        t += f'{sp4}<td class="col-lo">\n{lo_html}\n{sp4}</td>\n'
        t += f'{sp4}<td class="col-tools">\n{tools_html}\n{sp4}</td>\n'
        t += f'{sp3}</tr>\n'

    t += f'{sp2}</tbody>\n'
    t += f'{sp}</table>\n'
    return t

# ============================================================
# SEMESTER 1 -- 20 SKS
# ============================================================
sem1_courses = [
    (7, "Foundations of Data Science", 3),
    (8, "Design Thinking", 2),
    (9, "Discrete Mathematics", 3),
    (10, "Human-Computer Interaction", 3),
    (11, "Algorithms", 3),
    (12, "Mathematical and Statistical Foundations", 2),
    (13, "Networks", 2),
    (14, "Differential Calculus", 2),
]

html += '''    <div class="semester-block">
        <div class="semester-header">
            <span class="pill" style="background:var(--sem1);">Semester 1</span>
            <span class="info">20 SKS &bull; Fondasi Data Science &amp; Kompetensi Dasar</span>
        </div>
'''
html += build_semester_table(sem1_courses)
html += '''    </div>

'''

# ============================================================
# SEMESTER 2 -- 20 SKS
# ============================================================
sem2_courses = [
    (18, "Object-Oriented Programming", 3),
    (19, "Database Systems", 3),
    (20, "Data Structures", 3),
    (21, "Web Client Development", 3),
    (22, "Statistical Thinking", 3),
    (23, "Communication Protocols", 3),
    (24, "Data Wrangling", 2),
]

html += '''    <div class="semester-block">
        <div class="semester-header">
            <span class="pill" style="background:var(--sem2);">Semester 2</span>
            <span class="info">20 SKS &bull; Pemrograman Lanjut, Database &amp; Data Wrangling</span>
        </div>
'''
html += build_semester_table(sem2_courses)
html += '''    </div>

'''

# ============================================================
# SHORT SEMESTER 1 -- 9 SKS
# ============================================================
html += '''    <div class="semester-block">
        <div class="semester-header">
            <span class="pill" style="background:linear-gradient(135deg,var(--sem1),var(--sem2));">Short Semester 1</span>
            <span class="info">9 SKS &bull; Independent Study / Remedial / Elective</span>
        </div>
        <table class="lo-table">
            <thead>
                <tr><th class="col-no">No</th><th class="col-mk">Mata Kuliah</th><th class="col-lo">Keterangan</th><th class="col-tools">Learning Tools</th></tr>
            </thead>
            <tbody>
                <tr>
                    <td class="col-no">1</td>
                    <td class="col-mk">Independent Study Project<br><small>9 SKS</small></td>
                    <td class="col-lo">Proyek mandiri berbasis data science</td>
                    <td class="col-tools"><div class="tools-wrap"><span class="tool-badge">Sesuai Topik</span><span class="tool-badge">GitHub</span><span class="tool-badge">Python</span></div></td>
                </tr>
                <tr>
                    <td class="col-no">2</td>
                    <td class="col-mk">Remedial Course<br><small>9 SKS</small></td>
                    <td class="col-lo">Mata kuliah remedial (bila diperlukan)</td>
                    <td class="col-tools"><div class="tools-wrap"><span class="tool-badge">Sesuai MK</span></div></td>
                </tr>
                <tr>
                    <td class="col-no">3</td>
                    <td class="col-mk">Elective Course<br><small>9 SKS</small></td>
                    <td class="col-lo">Mata kuliah pilihan sesuai minat</td>
                    <td class="col-tools"><div class="tools-wrap"><span class="tool-badge">Sesuai MK</span></div></td>
                </tr>
            </tbody>
        </table>
    </div>

'''

# ============================================================
# SEMESTER 3 -- 18 SKS
# ============================================================
sem3_courses = [
    (35, "Web Application Development", 3),
    (36, "Advanced Database Systems", 3),
    (37, "Stochastic Modeling", 2),
    (38, "Numerical Methods", 2),
    (39, "Advanced Computational Mathematics", 2),
    (40, "Data Visualization", 3),
    (41, "Optimization Methods", 3),
]

html += '''    <div class="semester-block">
        <div class="semester-header">
            <span class="pill" style="background:var(--sem3);">Semester 3</span>
            <span class="info">18 SKS &bull; Full-Stack Development, Visualisasi &amp; Metode Numerik</span>
        </div>
'''
html += build_semester_table(sem3_courses)
html += '''    </div>

'''

# ============================================================
# SEMESTER 4 -- 18 SKS
# ============================================================
sem4_courses = [
    (46, "Text Mining", 3),
    (47, "Data Warehousing and Mining", 3),
    (48, "Technical / Professional Writing", 2),
    (49, "Mobile Computing", 3),
    (50, "Big Data Analytics", 2),
    (51, "Advanced Methods for Data Analytics", 3),
    (52, "Data Privacy and Security", 2),
]

html += '''    <div class="semester-block">
        <div class="semester-header">
            <span class="pill" style="background:var(--sem4);">Semester 4</span>
            <span class="info">18 SKS &bull; Text Mining, Big Data &amp; Advanced Analytics</span>
        </div>
'''
html += build_semester_table(sem4_courses)
html += '''    </div>

'''

# ============================================================
# SHORT SEMESTER 2 -- 9 SKS
# ============================================================
html += '''    <div class="semester-block">
        <div class="semester-header">
            <span class="pill" style="background:linear-gradient(135deg,var(--sem4),var(--sem5));">Short Semester 2</span>
            <span class="info">9 SKS &bull; Independent Study / Remedial / Elective</span>
        </div>
        <table class="lo-table">
            <thead>
                <tr><th class="col-no">No</th><th class="col-mk">Mata Kuliah</th><th class="col-lo">Keterangan</th><th class="col-tools">Learning Tools</th></tr>
            </thead>
            <tbody>
                <tr>
                    <td class="col-no">1</td>
                    <td class="col-mk">Independent Study Project<br><small>9 SKS</small></td>
                    <td class="col-lo">Proyek mandiri spesialisasi data science</td>
                    <td class="col-tools"><div class="tools-wrap"><span class="tool-badge">Sesuai Topik</span><span class="tool-badge">GitHub</span><span class="tool-badge">Python</span></div></td>
                </tr>
                <tr>
                    <td class="col-no">2</td>
                    <td class="col-mk">Remedial Course<br><small>9 SKS</small></td>
                    <td class="col-lo">Mata kuliah remedial (bila diperlukan)</td>
                    <td class="col-tools"><div class="tools-wrap"><span class="tool-badge">Sesuai MK</span></div></td>
                </tr>
                <tr>
                    <td class="col-no">3</td>
                    <td class="col-mk">Elective Course<br><small>9 SKS</small></td>
                    <td class="col-lo">Mata kuliah pilihan sesuai minat</td>
                    <td class="col-tools"><div class="tools-wrap"><span class="tool-badge">Sesuai MK</span></div></td>
                </tr>
            </tbody>
        </table>
    </div>

'''

# ============================================================
# SEMESTER 5 -- 18 SKS (Concentration Tracks)
# ============================================================
conc1_courses = [
    (64, "Big Data Infrastructure", 2),
    (65, "Distributed Systems", 3),
    (66, "Data Pipeline Development", 3),
    (67, "Cloud Computing", 2),
    (68, "ETL Processes", 3),
    (69, "Data Lakes", 3),
]

conc2_courses = [
    (74, "Deep Learning", 3),
    (75, "Natural Language Processing (NLP)", 3),
    (76, "Computer Vision", 3),
    (77, "Reinforcement Learning", 3),
    (78, "AI-Planning and Search Strategies", 2),
    (79, "Model Deployment", 2),
]

conc3_courses = [
    (84, "Business Intelligence Tools", 2),
    (85, "Statistical Modeling", 2),
    (86, "Customer Analytics", 3),
    (87, "Predictive Analytics", 3),
    (88, "Business Intelligence and Reporting", 3),
    (89, "Supply Chain Management Systems", 3),
]

html += '''    <div class="semester-block">
        <div class="semester-header">
            <span class="pill" style="background:var(--sem5);">Semester 5</span>
            <span class="info">18 SKS &bull; Concentration Tracks (pilih salah satu) + Professional Ethics</span>
        </div>

'''

# Concentration I
html += '''        <div class="concentration-card">
            <h4>Concentration I: Data Engineering and Big Data Analytics</h4>
'''
html += build_semester_table(conc1_courses, 12)
html += '''        </div>

'''

# Concentration II
html += '''        <div class="concentration-card">
            <h4>Concentration II: Artificial Intelligence (AI) and Machine Learning (ML) Development</h4>
'''
html += build_semester_table(conc2_courses, 12)
html += '''        </div>

'''

# Concentration III
html += '''        <div class="concentration-card">
            <h4>Concentration III: Business Intelligence and Advanced Data Analytics</h4>
'''
html += build_semester_table(conc3_courses, 12)
html += '''        </div>

'''

# Professional Ethics (common)
los_ethics = get_lo(71)
lo_html_ethics = lo_to_html(los_ethics, 28)
tools_ethics = learning_tools.get(71, [])
tools_html_ethics = tools_to_html(tools_ethics, 28)
html += f'''        <div class="concentration-card">
            <h4>Mata Kuliah Wajib Semua Konsentrasi</h4>
            <table class="lo-table">
                <thead>
                    <tr><th class="col-no">No</th><th class="col-mk">Mata Kuliah</th><th class="col-lo">Learning Outcomes</th><th class="col-tools">Learning Tools</th></tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-no">1</td>
                        <td class="col-mk">Professional Ethics<br><small>2 SKS</small></td>
                        <td class="col-lo">
{lo_html_ethics}
                        </td>
                        <td class="col-tools">
{tools_html_ethics}
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

'''

# ============================================================
# SEMESTER 6 -- 24 SKS (MBKM I)
# ============================================================
sem6_courses = [
    (116, "Data Science Project Management", 4),
    (117, "Advanced Data Processing and ETL", 4),
    (118, "Data Wrangling and Preprocessing Techniques", 4),
    (119, "Statistical Modeling and Inference", 4),
    (120, "Business Communication and Data Presentation", 4),
    (122, "Indonesian Way of Life / Pancasila", 2),
    (123, "Religions of the World", 2),
]

html += '''    <div class="semester-block">
        <div class="semester-header">
            <span class="pill" style="background:var(--sem6);">Semester 6 -- MBKM I</span>
            <span class="info">24 SKS &bull; Data Science Project Management, ETL, Statistical Modeling &amp; MK Umum</span>
        </div>
'''
html += build_semester_table(sem6_courses)
html += '''    </div>

'''

# ============================================================
# SEMESTER 7 -- 24 SKS (MBKM II)
# ============================================================
sem7_courses = [
    (127, "Machine Learning Applications", 4),
    (128, "Big Data Technologies and Cloud Integration", 4),
    (129, "Predictive Analytics and Forecasting", 4),
    (130, "Data Ethics and Privacy", 4),
    (131, "Capstone Data Science Project", 4),
    (133, "Applied Indonesian Language", 2),
    (134, "Civic / Kewarganegaraan", 2),
]

html += '''    <div class="semester-block">
        <div class="semester-header">
            <span class="pill" style="background:var(--sem7);">Semester 7 -- MBKM II</span>
            <span class="info">24 SKS &bull; ML Applications, Big Data, Predictive Analytics &amp; Capstone</span>
        </div>
'''
html += build_semester_table(sem7_courses)
html += '''    </div>

'''

# ============================================================
# SEMESTER 8 -- 10 SKS
# ============================================================
# Capstone Project main + components
sem8_main = [(137, "Capstone Project", 6)]
sem8_components = [
    (138, "Collaborative Project", 0),
    (139, "Portfolio", 0),
    (140, "Product Prototype", 0),
    (141, "Scientific Publication", 0),
    (142, "Thesis", 0),
]
sem8_mk = [
    (144, "Academic Writing in English", 2),
    (145, "Research Methodology", 2),
]

html += '''    <div class="semester-block">
        <div class="semester-header">
            <span class="pill" style="background:var(--sem8);">Semester 8</span>
            <span class="info">10 SKS &bull; Capstone Project, Thesis, Portfolio &amp; Publikasi</span>
        </div>
        <table class="lo-table">
            <thead>
                <tr><th class="col-no">No</th><th class="col-mk">Mata Kuliah</th><th class="col-lo">Learning Outcomes</th><th class="col-tools">Learning Tools</th></tr>
            </thead>
            <tbody>
'''

# Capstone Project (6 CP)
los = get_lo(137)
lo_html = lo_to_html(los)
tools = learning_tools.get(137, [])
tools_html = tools_to_html(tools)
html += f'''                <tr>
                    <td class="col-no">1</td>
                    <td class="col-mk">Capstone Project<br><small>6 SKS</small></td>
                    <td class="col-lo">
{lo_html}
                    </td>
                    <td class="col-tools">
{tools_html}
                    </td>
                </tr>
'''

# Components of Capstone
cnt = 2
for row, name, cp in sem8_components:
    los = get_lo(row)
    lo_html = lo_to_html(los)
    tools = learning_tools.get(row, [])
    tools_html = tools_to_html(tools)
    cp_label = "Komponen Capstone"
    html += f'''                <tr>
                    <td class="col-no">{cnt}</td>
                    <td class="col-mk">{name}<br><small>{cp_label}</small></td>
                    <td class="col-lo">
{lo_html}
                    </td>
                    <td class="col-tools">
{tools_html}
                    </td>
                </tr>
'''
    cnt += 1

# MK Umum
for row, name, cp in sem8_mk:
    los = get_lo(row)
    lo_html = lo_to_html(los)
    tools = learning_tools.get(row, [])
    tools_html = tools_to_html(tools)
    html += f'''                <tr>
                    <td class="col-no">{cnt}</td>
                    <td class="col-mk">{name}<br><small>{cp} SKS</small></td>
                    <td class="col-lo">
{lo_html}
                    </td>
                    <td class="col-tools">
{tools_html}
                    </td>
                </tr>
'''
    cnt += 1

html += '''            </tbody>
        </table>
    </div>

'''

# ============================================================
# TOTAL SKS SUMMARY
# ============================================================
html += '''    <h2 class="section-title"><span class="dot" style="background:var(--sem5)"></span> Ringkasan Total SKS</h2>
    <div class="summary-card" style="display:flex;flex-wrap:wrap;gap:16px;align-items:center;">
        <div style="flex:1;min-width:200px;">
            <table class="lo-table" style="font-size:.82rem;">
                <thead><tr><th>Semester</th><th style="text-align:center;">SKS</th></tr></thead>
                <tbody>
                    <tr><td>Semester 1</td><td style="text-align:center;">20</td></tr>
                    <tr><td>Semester 2</td><td style="text-align:center;">20</td></tr>
                    <tr><td>Short Semester 1</td><td style="text-align:center;">9</td></tr>
                    <tr><td>Semester 3</td><td style="text-align:center;">18</td></tr>
                    <tr><td>Semester 4</td><td style="text-align:center;">18</td></tr>
                    <tr><td>Short Semester 2</td><td style="text-align:center;">9</td></tr>
                    <tr><td>Semester 5 (Concentration)</td><td style="text-align:center;">18</td></tr>
                    <tr><td>Semester 6 (MBKM I)</td><td style="text-align:center;">24</td></tr>
                    <tr><td>Semester 7 (MBKM II)</td><td style="text-align:center;">24</td></tr>
                    <tr><td>Semester 8</td><td style="text-align:center;">10</td></tr>
                    <tr style="background:rgba(108,99,255,.08);"><td><strong>TOTAL</strong></td><td style="text-align:center;"><strong>152 + 18 (Extra) = 170 SKS</strong></td></tr>
                </tbody>
            </table>
        </div>
    </div>

</main>

<footer class="footer">
    <p>Dokumen Perbaikan &amp; Penyelarasan Learning Outcomes -- Program Studi Data Science</p>
    <p>Diselaraskan dengan Kebutuhan CDC Fakultas IT &bull; Terakhir diperbarui: April 2026</p>
</footer>

<button class="export-btn" id="exportPdfBtn" onclick="exportToPDF()">
    <span class="btn-icon">Export PDF</span>
</button>

<div class="toast" id="toast">PDF berhasil di-download!</div>

<script>
function exportToPDF() {
    window.print();
}
</script>

</body>
</html>
'''

with open('hasil_perbaikan_learning_outcome.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML generated successfully!")
print(f"Total characters: {len(html)}")
