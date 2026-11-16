import os
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

pdf_path = '/Users/jainil.30/Downloads/RR/SupeRR_Selector_Season_2_Methodology_and_Strategy_Report.pdf'

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_decorations(self, page_count):
        self.saveState()
        
        # Header on page 2 onwards
        if self._pageNumber > 1:
            self.setFont('Helvetica-Bold', 8)
            self.setFillColor(colors.HexColor('#001D48')) # Royals Navy
            self.drawString(45, 755, 'RAJASTHAN ROYALS')
            self.setFont('Helvetica', 8)
            self.setFillColor(colors.HexColor('#666666'))
            self.drawString(145, 755, '|  SupeRR Selector Season 2 — Uncapped Auction Strategy')
            self.drawRightString(567, 755, 'IPL 2027 WAR ROOM REPORT')
            
            self.setStrokeColor(colors.HexColor('#E6196E')) # Royals Pink
            self.setLineWidth(1)
            self.line(45, 749, 567, 749)

        # Footer on all pages
        self.setFont('Helvetica', 8)
        self.setFillColor(colors.HexColor('#777777'))
        self.drawString(45, 30, 'CONFIDENTIAL & PROPRIETARY — PREPARED FOR RAJASTHAN ROYALS AUCTION WAR ROOM')
        page_text = f'Page {self._pageNumber} of {page_count}'
        self.drawRightString(567, 30, page_text)
        
        self.setStrokeColor(colors.HexColor('#DDDDDD'))
        self.setLineWidth(0.5)
        self.line(45, 40, 567, 40)
        
        self.restoreState()

# Margins set to 45pt to maximize printable width (522pt width)
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=45,
    rightMargin=45,
    topMargin=45,
    bottomMargin=45
)

styles = getSampleStyleSheet()

primary_color = colors.HexColor('#001D48') # Deep Royals Blue
accent_pink = colors.HexColor('#E6196E')   # Royals Pink
gold_color = colors.HexColor('#C59B27')    # Royal Gold
dark_text = colors.HexColor('#1A1A1A')
light_bg = colors.HexColor('#F8F9FA')

title_style = ParagraphStyle(
    'CoverTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=20,
    leading=24,
    textColor=primary_color,
    spaceAfter=4
)

subtitle_style = ParagraphStyle(
    'CoverSubtitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=15,
    textColor=accent_pink,
    spaceAfter=10
)

meta_style = ParagraphStyle(
    'CoverMeta',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor('#444444')
)

h1_style = ParagraphStyle(
    'Heading1_Custom',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=17,
    textColor=primary_color,
    spaceBefore=8,
    spaceAfter=6,
    keepWithNext=True
)

h2_style = ParagraphStyle(
    'Heading2_Custom',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=13,
    textColor=accent_pink,
    spaceBefore=6,
    spaceAfter=3,
    keepWithNext=True
)

body_style = ParagraphStyle(
    'Body_Custom',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=12,
    textColor=dark_text,
    spaceAfter=5
)

callout_style = ParagraphStyle(
    'Callout_Text',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor('#1E3D59')
)

th_style = ParagraphStyle(
    'TableHeader',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=7.5,
    leading=9.5,
    textColor=colors.white,
    alignment=1
)

td_style = ParagraphStyle(
    'TableCell',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=7.5,
    leading=9.5,
    textColor=dark_text,
    alignment=1
)

td_bold = ParagraphStyle(
    'TableCellBold',
    parent=td_style,
    fontName='Helvetica-Bold'
)

td_left = ParagraphStyle(
    'TableCellLeft',
    parent=td_style,
    alignment=0
)

td_left_bold = ParagraphStyle(
    'TableCellLeftBold',
    parent=td_style,
    fontName='Helvetica-Bold',
    alignment=0
)

story = []

# ==================== PAGE 1: TITLE & METHODOLOGY ====================
story.append(Paragraph('SupeRR Selector Season 2: Franchise Analytics Challenge', subtitle_style))
story.append(Paragraph('Identify the Most Reliable Players Under Pressure', title_style))
story.append(Paragraph('Official Round 1 Submission & Rajasthan Royals IPL 2027 Auction Strategy<br/>'
                       '<b>Core Focus:</b> Top 10 Uncapped Domestic Batsmen & Top 10 Uncapped Domestic Bowlers Available in the Auction', meta_style))

story.append(Spacer(1, 6))
story.append(HRFlowable(width="100%", thickness=2, color=accent_pink, spaceAfter=8))

eval_data = [
    [Paragraph('<b>Franchise Evaluators:</b> Kumar Sangakkara (Head Coach & Director of Cricket) | Giles Lindsay (Director of Analytics & Technology)', meta_style)],
    [Paragraph('<b>Dataset Scope:</b> 201,000 delivery records across 867 matches (IPL 2022–2026, T20Is, Emerging Asia Cups). All retained stars strictly filtered out.', meta_style)]
]
eval_table = Table(eval_data, colWidths=[522])
eval_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), light_bg),
    ('PADDING', (0,0), (-1,-1), 5),
    ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
]))
story.append(eval_table)
story.append(Spacer(1, 8))

story.append(Paragraph('1. Executive Summary & Franchise Context', h1_style))
story.append(Paragraph(
    'In an IPL mega auction, acquiring established international finishers and death bowlers often consumes over 60% of a franchise\'s purse. '
    'For <b>Rajasthan Royals</b>, continuing the franchise\'s <i>Moneyball</i> legacy requires discovering <b>Uncapped Domestic Talents</b> '
    'whose empirical performance under pressure rivals elite capped stars at a fraction of the valuation. '
    'Furthermore, Rajasthan Royals\' home ground—<b>Sawai Mansingh Stadium (Jaipur)</b>—features 75m+ square boundaries and pace-off grip, '
    'requiring batters with high boundary-clearing velocity and bowlers with deceptive slower variations and tight spin control.',
    body_style
))

story.append(Paragraph('2. Analytical Methodology: The Dynamic Pressure Index (PI)', h1_style))
story.append(Paragraph(
    'In professional sabermetrics, match pressure is modeled as <b>game-state leverage</b>—the variance in expected win probability '
    'contingent on the outcome of an individual delivery. Our system calculates a continuous delivery-level <b>Pressure Index (PI &isin; [0, 1])</b>:',
    body_style
))

story.append(Paragraph(
    '<b>• Innings 2 (The Chase):</b> Direct scoreboard strain is modeled via a sigmoidal Required Run Rate function '
    '<i>S<sub>RRR</sub> = 1 / (1 + e<sup>-0.60(RRR - 9.50)</sup>)</i>, scaled by resource depletion <i>(Wickets Lost / 9)<sup>1.20</sup></i>, '
    'temporal urgency <i>[0.40 + 0.60 &times; (1 - Balls Remaining / 120)]</i>, and a +0.15 clutch bonus in close finishes (&le; 24 balls, &le; 50 runs). '
    'When the target is achieved, pressure terminates (PI = 0.0).<br/>'
    '<b>• Innings 1 (Target Setting):</b> Evaluates crisis recovery when early wickets fall ahead of stage expectation '
    '<i>(W - 0.25 &times; Over) / 4.50</i>, alongside death-over maximization in overs 16–20 (PI: 0.65 to 1.00).<br/>'
    '<b>• Playoff Multiplier & Threshold:</b> Knockouts receive a +15% stakes multiplier; Super Overs are pegged at PI &equiv; 1.00. '
    'Across all 201,000 deliveries, the 75th percentile falls at 0.661. Setting <b>PI &ge; 0.65</b> isolates exactly the <b>top 25.5% (51,176 deliveries)</b> '
    'of high-pressure match situations.<br/>'
    '<b>• Performance Measurement:</b> Measures how players elevate under heat compared to their baseline (Strike Rate Elevation &Delta;SR, '
    'Economy Outperformance &Delta;Econ vs. league HP average of 9.61 RPO, boundary %, dot %, and match-by-match repeatability).<br/>'
    '<b>• Auction Eligibility Filter:</b> All 10 franchises\' official retained players (e.g., Surya, Kohli, Tilak, Klaasen, Rinku, Gill, Stubbs, '
    'Shashank, Mayank Yadav, Mohsin Khan, Bumrah, Narine) are strictly excluded. Only <b>True Uncapped Domestic Players</b> available in the auction pool are ranked.',
    body_style
))

story.append(PageBreak())

# ==================== PAGE 2: TOP 10 UNCAPPED BATSMEN ====================
story.append(Paragraph('3. Top 10 Uncapped Domestic Batsmen Available in the IPL Auction', h1_style))
story.append(Paragraph(
    'These domestic Indian batters have <b>never represented the senior national team</b> and are confirmed in the <b>auction pool</b>. '
    'Ranked 1 to 10 by empirical Composite Batting Rating (CBR) under high pressure (PI &ge; 0.65):',
    body_style
))

bat_headers = ['Rk', 'Player Name', 'Primary Tactical Role', 'HP SR', 'Base SR', 'ΔSR', 'HP Avg', 'Bnd %', 'Dot %', 'Consistency', 'Auction Tier']
bat_rows = [
    [Paragraph(f'<b>{h}</b>', th_style) for h in bat_headers],
    [Paragraph('<b>1</b>', td_bold), Paragraph('<b>Ashutosh Sharma</b>', td_left_bold), Paragraph('Lower-Order Finisher (#6/#7)', td_left), Paragraph('<b>186.6</b>', td_bold), Paragraph('103.5', td_style), Paragraph('<b>+83.1</b>', td_bold), Paragraph('25.7', td_style), Paragraph('<b>27.1%</b>', td_style), Paragraph('29.8%', td_style), Paragraph('46.2%', td_style), Paragraph('INR 2.5–4.5 Cr', td_style)],
    [Paragraph('<b>2</b>', td_bold), Paragraph('<b>Sameer Rizvi</b>', td_left_bold), Paragraph('Spin-Punishing Middle-Order (#4/#5)', td_left), Paragraph('<b>182.7</b>', td_bold), Paragraph('131.7', td_style), Paragraph('<b>+51.0</b>', td_bold), Paragraph('22.8', td_style), Paragraph('25.3%', td_style), Paragraph('<b>25.3%</b>', td_style), Paragraph('<b>50.0%</b>', td_style), Paragraph('INR 1.5–3.0 Cr', td_style)],
    [Paragraph('<b>3</b>', td_bold), Paragraph('<b>Aniket Verma</b>', td_left_bold), Paragraph('High-Tempo Impact Striker', td_left), Paragraph('<b>190.5</b>', td_bold), Paragraph('138.4', td_style), Paragraph('<b>+52.1</b>', td_bold), Paragraph('17.8', td_style), Paragraph('<b>27.4%</b>', td_style), Paragraph('32.1%', td_style), Paragraph('25.0%', td_style), Paragraph('INR 50L–1.5 Cr', td_style)],
    [Paragraph('<b>4</b>', td_bold), Paragraph('<b>Nehal Wadhera</b>', td_left_bold), Paragraph('Left-Handed Middle-Order (#4/#6)', td_left), Paragraph('<b>170.7</b>', td_bold), Paragraph('121.3', td_style), Paragraph('<b>+49.4</b>', td_bold), Paragraph('17.5', td_style), Paragraph('25.3%', td_style), Paragraph('32.8%', td_style), Paragraph('31.6%', td_style), Paragraph('INR 1.5–3.5 Cr', td_style)],
    [Paragraph('<b>5</b>', td_bold), Paragraph('<b>Anuj Rawat</b>', td_left_bold), Paragraph('Wicketkeeper-Batter / Stabilizer', td_left), Paragraph('149.0', td_style), Paragraph('101.1', td_style), Paragraph('<b>+47.9</b>', td_bold), Paragraph('<b>35.8</b>', td_bold), Paragraph('19.8%', td_style), Paragraph('31.3%', td_style), Paragraph('40.0%', td_style), Paragraph('INR 50L–1.5 Cr', td_style)],
    [Paragraph('<b>6</b>', td_bold), Paragraph('<b>Mukul Choudhary</b>', td_left_bold), Paragraph('Aggressive Middle-Order Utility', td_left), Paragraph('158.1', td_style), Paragraph('115.2', td_style), Paragraph('<b>+42.9</b>', td_bold), Paragraph('23.4', td_style), Paragraph('20.3%', td_style), Paragraph('37.8%', td_style), Paragraph('<b>57.1%</b>', td_style), Paragraph('INR 30L–80L', td_style)],
    [Paragraph('<b>7</b>', td_bold), Paragraph('<b>Mahipal Lomror</b>', td_left_bold), Paragraph('Left-Hand Power Striker (#5/#6)', td_left), Paragraph('166.1', td_style), Paragraph('144.9', td_style), Paragraph('+21.2', td_style), Paragraph('13.6', td_style), Paragraph('24.3%', td_style), Paragraph('30.4%', td_style), Paragraph('41.2%', td_style), Paragraph('INR 1.0–2.5 Cr', td_style)],
    [Paragraph('<b>8</b>', td_bold), Paragraph('<b>M Shahrukh Khan</b>', td_left_bold), Paragraph('High-Pace Muscle Finisher (#7)', td_left), Paragraph('168.2', td_style), Paragraph('134.2', td_style), Paragraph('+34.1', td_style), Paragraph('18.7', td_style), Paragraph('21.3%', td_style), Paragraph('28.0%', td_style), Paragraph('18.8%', td_style), Paragraph('INR 2.0–4.0 Cr', td_style)],
    [Paragraph('<b>9</b>', td_bold), Paragraph('<b>Shubham Dubey</b>', td_left_bold), Paragraph('Lower-Order Left-Hand Finisher', td_left), Paragraph('160.2', td_style), Paragraph('130.0', td_style), Paragraph('+30.2', td_style), Paragraph('18.1', td_style), Paragraph('21.2%', td_style), Paragraph('31.9%', td_style), Paragraph('33.3%', td_style), Paragraph('INR 40L–1.0 Cr', td_style)],
    [Paragraph('<b>10</b>', td_bold), Paragraph('<b>Angkrish Raghuvanshi</b>', td_left_bold), Paragraph('Dynamic Stroke-Maker (#3/#4)', td_left), Paragraph('151.1', td_style), Paragraph('144.6', td_style), Paragraph('+6.5', td_style), Paragraph('20.3', td_style), Paragraph('20.2%', td_style), Paragraph('<b>26.6%</b>', td_style), Paragraph('40.0%', td_style), Paragraph('INR 1.0–2.5 Cr', td_style)]
]

t_bat = Table(bat_rows, colWidths=[18, 98, 102, 34, 34, 32, 34, 34, 34, 44, 58])
t_bat.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), primary_color),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, light_bg]),
    ('PADDING', (0,0), (-1,-1), 3.5),
]))
story.append(t_bat)
story.append(Spacer(1, 10))

story.append(Paragraph('How Each Uncapped Batsman Strengthens Rajasthan Royals for IPL 2027:', h2_style))
story.append(Paragraph(
    '<b>1. Ashutosh Sharma (Priority #1 Target):</b> Rajasthan Royals have historically suffered from a lack of death-over acceleration from Indian batters '
    'when games enter RRR > 11.5. Ashutosh possesses the <b>highest strike-rate elevation in the entire competition (+83.1)</b>, jumping from 103.5 base to 186.6 under fire. '
    'Acquiring him for under INR 4.5 Cr permanently solves RR\'s #6/#7 finishing void without consuming an overseas slot.<br/>'
    '<b>2. Sameer Rizvi (Priority #2 Target):</b> Sawai Mansingh Stadium has cavernous square boundaries where opposing spinners attempt to choke the middle overs. '
    'Rizvi steps out with elite intent (+51.0 SR elevation, 182.7 HP SR), providing the exact aggression needed between overs 7 and 14.<br/>'
    '<b>3. Aniket Verma:</b> High-velocity boundary hitter (190.5 HP SR) with a boundary rate of 27.4%, ideal as a game-breaking Impact Player.<br/>'
    '<b>4. Nehal Wadhera:</b> Left-handed middle-order striker (+49.4 elevation) who handles leg-spin and off-spin effectively, balancing RR\'s batting lineup.<br/>'
    '<b>5. Anuj Rawat:</b> Crisis-recovery stabilizer holding an elite 35.8 HP average; provides domestic wicketkeeping backup and anchors during top-order collapses.<br/>'
    '<b>6. Mukul Choudhary:</b> Outstanding 57.1% outing consistency rate under pressure; under-the-radar domestic value asset.<br/>'
    '<b>7. Mahipal Lomror:</b> Former RR player with deep familiarity with Jaipur conditions; clears the ropes straight against express pace.<br/>'
    '<b>8. M Shahrukh Khan:</b> Proven power hitter against 140+ kph bowling; delivers extreme bat speed in the final 12 deliveries of an innings.<br/>'
    '<b>9. Shubham Dubey:</b> Powerful domestic left-hander (+30.2 elevation); provides specialized death-over depth.<br/>'
    '<b>10. Angkrish Raghuvanshi:</b> Low dot-ball frequency (26.6%); keeps chases alive by rotating strike smoothly without freezing under scoreboard pressure.',
    body_style
))

story.append(PageBreak())

# ==================== PAGE 3: TOP 10 UNCAPPED BOWLERS ====================
story.append(Paragraph('4. Top 10 Uncapped Domestic Bowlers Available in the IPL Auction', h1_style))
story.append(Paragraph(
    'These domestic Indian bowlers have <b>never represented the senior national team</b> and are confirmed in the <b>auction pool</b>. '
    'Ranked 1 to 10 by empirical Composite Bowling Rating (CBR) under high pressure (PI &ge; 0.65, vs. league average HP economy of 9.61 RPO):',
    body_style
))

bowl_headers = ['Rk', 'Player Name', 'Bowling Style / Role', 'HP Econ', 'Base Econ', 'ΔEcon', 'HP SR', 'Dot %', 'Bnd %', 'Consistency', 'Auction Tier']
bowl_rows = [
    [Paragraph(f'<b>{h}</b>', th_style) for h in bowl_headers],
    [Paragraph('<b>1</b>', td_bold), Paragraph('<b>Sakib Hussain</b>', td_left_bold), Paragraph('Right-Arm Fast / Yorker Weapon', td_left), Paragraph('<b>8.39</b>', td_bold), Paragraph('10.14', td_style), Paragraph('<b>+1.75</b>', td_bold), Paragraph('12.00', td_style), Paragraph('31.6%', td_style), Paragraph('<b>15.4%</b>', td_style), Paragraph('<b>80.0%</b>', td_style), Paragraph('INR 50L–1.5 Cr', td_style)],
    [Paragraph('<b>2</b>', td_bold), Paragraph('<b>Rasikh Salam</b>', td_left_bold), Paragraph('Right-Arm Fast / Dipping Cutters', td_left), Paragraph('9.41', td_style), Paragraph('9.71', td_style), Paragraph('<b>+0.30</b>', td_bold), Paragraph('<b>9.08</b>', td_bold), Paragraph('31.6%', td_style), Paragraph('18.6%', td_style), Paragraph('<b>70.0%</b>', td_style), Paragraph('INR 1.5–3.0 Cr', td_style)],
    [Paragraph('<b>3</b>', td_bold), Paragraph('<b>Gurjapneet Singh</b>', td_left_bold), Paragraph('Left-Arm Fast / Tall Seamer', td_left), Paragraph('<b>8.47</b>', td_bold), Paragraph('9.04', td_style), Paragraph('<b>+0.57</b>', td_bold), Paragraph('14.17', td_style), Paragraph('27.8%', td_style), Paragraph('<b>13.3%</b>', td_style), Paragraph('66.7%', td_style), Paragraph('INR 30L–1.0 Cr', td_style)],
    [Paragraph('<b>4</b>', td_bold), Paragraph('<b>Anshul Kamboj</b>', td_left_bold), Paragraph('Right-Arm Medium / Hit-The-Deck', td_left), Paragraph('9.85', td_style), Paragraph('10.01', td_style), Paragraph('+0.16', td_style), Paragraph('<b>9.46</b>', td_bold), Paragraph('<b>36.2%</b>', td_style), Paragraph('21.5%', td_style), Paragraph('53.8%', td_style), Paragraph('INR 1.0–2.5 Cr', td_style)],
    [Paragraph('<b>5</b>', td_bold), Paragraph('<b>Suyash Sharma</b>', td_left_bold), Paragraph('Leg-Break Spin / Mystery Control', td_left), Paragraph('<b>8.42</b>', td_bold), Paragraph('8.76', td_style), Paragraph('<b>+0.34</b>', td_bold), Paragraph('21.50', td_style), Paragraph('<b>37.5%</b>', td_style), Paragraph('<b>16.2%</b>', td_style), Paragraph('50.0%', td_style), Paragraph('INR 1.0–2.0 Cr', td_style)],
    [Paragraph('<b>6</b>', td_bold), Paragraph('<b>Ashwani Kumar</b>', td_left_bold), Paragraph('Right-Arm Fast / Express Pace', td_left), Paragraph('11.01', td_style), Paragraph('10.74', td_style), Paragraph('-0.27', td_style), Paragraph('<b>8.78</b>', td_bold), Paragraph('<b>36.8%</b>', td_style), Paragraph('25.3%', td_style), Paragraph('<b>85.7%</b>', td_style), Paragraph('INR 30L–80L', td_style)],
    [Paragraph('<b>7</b>', td_bold), Paragraph('<b>Praful Hinge</b>', td_left_bold), Paragraph('Right-Arm Medium / Death Pacer', td_left), Paragraph('10.82', td_style), Paragraph('11.76', td_style), Paragraph('<b>+0.94</b>', td_bold), Paragraph('12.20', td_style), Paragraph('<b>38.5%</b>', td_style), Paragraph('24.6%', td_style), Paragraph('<b>85.7%</b>', td_style), Paragraph('INR 30L–60L', td_style)],
    [Paragraph('<b>8</b>', td_bold), Paragraph('<b>Brijesh Sharma</b>', td_left_bold), Paragraph('Right-Arm Fast / Hard Length', td_left), Paragraph('<b>9.27</b>', td_bold), Paragraph('9.92', td_style), Paragraph('<b>+0.64</b>', td_bold), Paragraph('15.71', td_style), Paragraph('30.3%', td_style), Paragraph('18.5%', td_style), Paragraph('36.4%', td_style), Paragraph('INR 30L–75L', td_style)],
    [Paragraph('<b>9</b>', td_bold), Paragraph('<b>Harpreet Brar</b>', td_left_bold), Paragraph('Slow Left-Arm Orthodox / Dart', td_left), Paragraph('10.11', td_style), Paragraph('8.02', td_style), Paragraph('-2.09', td_style), Paragraph('14.60', td_style), Paragraph('<b>35.5%</b>', td_style), Paragraph('22.4%', td_style), Paragraph('40.0%', td_style), Paragraph('INR 1.5–3.0 Cr', td_style)],
    [Paragraph('<b>10</b>', td_bold), Paragraph('<b>Akash Madhwal</b>', td_left_bold), Paragraph('Right-Arm Fast / Blockhole Pacer', td_left), Paragraph('10.64', td_style), Paragraph('9.57', td_style), Paragraph('-1.08', td_style), Paragraph('13.27', td_style), Paragraph('28.8%', td_style), Paragraph('20.9%', td_style), Paragraph('50.0%', td_style), Paragraph('INR 1.0–2.5 Cr', td_style)]
]

t_bowl = Table(bowl_rows, colWidths=[18, 98, 102, 34, 34, 32, 34, 34, 34, 44, 58])
t_bowl.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), primary_color),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, light_bg]),
    ('PADDING', (0,0), (-1,-1), 3.5),
]))
story.append(t_bowl)
story.append(Spacer(1, 10))

story.append(Paragraph('How Each Uncapped Bowler Strengthens Rajasthan Royals for IPL 2027:', h2_style))
story.append(Paragraph(
    '<b>1. Sakib Hussain (Priority #1 Pacer Target):</b> League average economy under high pressure is 9.61 RPO. '
    'Sakib Hussain not only outperforms the league but <b>improves his economy from 10.14 base down to 8.39 (+1.75 swing)</b> under heat, '
    'holding an elite 80.0% spell consistency rate. He provides RR an ice-cool domestic death specialist for under INR 1.5 Cr.<br/>'
    '<b>2. Rasikh Salam (Priority #2 Pacer Target):</b> Delivers an astonishing <b>strike rate of 9.08 balls per wicket</b> in high-pressure situations across '
    '236 deliveries. His dipping slower ball and yorker variations make him an elite wicket-taker at the death, preserving overseas slots.<br/>'
    '<b>3. Gurjapneet Singh:</b> Tall left-arm seamer restricting boundaries to just 13.3% with an 8.47 HP economy; brings crucial left-arm trajectory to RR.<br/>'
    '<b>4. Anshul Kamboj:</b> Breakthrough pacer averaging a wicket every 9.46 balls in high pressure; 36.2% dot balls shows relentless attacking intent.<br/>'
    '<b>5. Suyash Sharma:</b> 8.42 HP economy and 37.5% dot ball rate; uses fast leg-spin variations to exploit Sawai Mansingh Stadium\'s 75m+ square ropes.<br/>'
    '<b>6. Ashwani Kumar:</b> High-pace strike weapon taking a wicket every 8.78 balls in high pressure with an 85.7% consistency rate.<br/>'
    '<b>7. Praful Hinge:</b> High dot-ball rate (38.5%) and +0.94 economy improvement under pressure; disciplined death-over bowler.<br/>'
    '<b>8. Brijesh Sharma:</b> Sub-9.30 economy in high pressure; delivers hard lengths that rush batters into mistimed aerial hits.<br/>'
    '<b>9. Harpreet Brar:</b> Flat left-arm darts restricting right-handers; delivers 35.5% dot balls in high-pressure middle overs.<br/>'
    '<b>10. Akash Madhwal:</b> Experienced blockhole yorker specialist with proven IPL playoff pedigree, capable of defending under 12 runs in the 20th over.',
    body_style
))

story.append(PageBreak())

# ==================== PAGE 4: STRATEGY & BUDGET BLUEPRINT ====================
story.append(Paragraph('5. Rajasthan Royals War Room Action Plan & Purse Allocation', h1_style))
story.append(Paragraph(
    '<b>The Moneyball Surplus Advantage:</b> In recent IPL auctions, franchises frequently spend INR 14–18 Cr on overseas finishers '
    'and INR 12–15 Cr on overseas fast bowlers, causing severe budget imbalances. '
    'By identifying and acquiring <b>Ashutosh Sharma</b> (Top Uncapped Batter) alongside <b>Rasikh Salam and Sakib Hussain</b> (Top Uncapped Bowlers), '
    'Rajasthan Royals can secure tier-1 clutch execution for <b>under INR 7.5 Cr combined</b>. '
    'This frees up over INR 15 Cr in purse capital, allowing Kumar Sangakkara and Giles Lindsay to retain/bid for marquee anchors like '
    '<b>Jos Buttler</b> and <b>Matheesha Pathirana</b> while building an unbeatable, deep 25-man squad.',
    body_style
))

story.append(Spacer(1, 4))

budget_data = [
    [Paragraph('<b>Target Asset</b>', th_style), Paragraph('<b>Category</b>', th_style), Paragraph('<b>Role in RR Playing XI</b>', th_style), Paragraph('<b>Projected Purse</b>', th_style), Paragraph('<b>Surplus Value Created for RR</b>', th_style)],
    [Paragraph('Ashutosh Sharma', td_bold), Paragraph('Uncapped Batter', td_style), Paragraph('Designated Finisher (#6/#7)', td_left), Paragraph('INR 2.5 – 4.5 Cr', td_style), Paragraph('+83.1 SR elevation; delivers INR 15 Cr finisher impact', td_left)],
    [Paragraph('Sameer Rizvi', td_bold), Paragraph('Uncapped Batter', td_style), Paragraph('Middle-Order Spin Counter (#5)', td_left), Paragraph('INR 1.5 – 3.0 Cr', td_style), Paragraph('+51.0 SR elevation; neutralizes spin squeeze at Jaipur', td_left)],
    [Paragraph('Rasikh Salam', td_bold), Paragraph('Uncapped Bowler', td_style), Paragraph('Death-Overs Wicket Specialist (17 & 19)', td_left), Paragraph('INR 1.5 – 3.0 Cr', td_style), Paragraph('9.08 balls/wkt; replaces expensive overseas pacer', td_left)],
    [Paragraph('Sakib Hussain', td_bold), Paragraph('Uncapped Bowler', td_style), Paragraph('Blockhole Yorker Specialist (18 & 20)', td_left), Paragraph('INR 50L – 1.5 Cr', td_style), Paragraph('8.39 HP Econ (+1.75 diff); sub-9 death economy', td_left)],
    [Paragraph('Suyash Sharma', td_bold), Paragraph('Uncapped Bowler', td_style), Paragraph('Mystery Wrist Spinner (Jaipur Fortress)', td_left), Paragraph('INR 1.0 – 2.0 Cr', td_style), Paragraph('37.5% dot ball rate; perfect fit for SMS boundary size', td_left)],
    [Paragraph('Nehal Wadhera', td_bold), Paragraph('Uncapped Batter', td_style), Paragraph('Left-Hand Match-Up Hitter (#4/#6)', td_left), Paragraph('INR 1.5 – 3.5 Cr', td_style), Paragraph('+49.4 SR elevation; tactical counter to leg-spinners', td_left)],
]
budget_table = Table(budget_data, colWidths=[95, 75, 125, 65, 162])
budget_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), primary_color),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, light_bg]),
    ('PADDING', (0,0), (-1,-1), 4),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
]))
story.append(budget_table)
story.append(Spacer(1, 10))

story.append(Paragraph('Hypothetical Rajasthan Royals High-Pressure Blueprint (IPL 2027):', h2_style))
story.append(Paragraph(
    '<b>1. Yashasvi Jaiswal</b> (Retained Anchor/Aggressor)<br/>'
    '<b>2. Jos Buttler</b> (Target / RTM: 195.1 HP SR, 63% Consistency)<br/>'
    '<b>3. Sanju Samson (C & WK)</b> (Retained Elite Captain)<br/>'
    '<b>4. Riyan Parag</b> (Retained Middle-Order Spin Hitter)<br/>'
    '<b>5. Sameer Rizvi / Nehal Wadhera</b> (Auction Target: +51.0 &Delta;SR, spin aggressor)<br/>'
    '<b>6. Dhruv Jurel</b> (Retained Clutch Finisher / WK)<br/>'
    '<b>7. Ashutosh Sharma</b> (Auction Target: #1 Uncapped Batter, +83.1 &Delta;SR)<br/>'
    '<b>8. Wanindu Hasaranga / Mitchell Santner</b> (Auction Target: Sub-10 Wkt SR at SMS Jaipur)<br/>'
    '<b>9. Rasikh Salam</b> (Auction Target: #1 Uncapped Strike Pacer, 9.08 Wkt SR)<br/>'
    '<b>10. Sandeep Sharma</b> (Retained Uncapped Knuckle-ball Specialist)<br/>'
    '<b>11. Matheesha Pathirana</b> (Marquee Auction Target: 51 HP Wickets, 11.0 SR)<br/>'
    '<i>Impact Sub Options:</i> <b>Suyash Sharma</b> (8.42 HP Econ, 37.5% dots) / <b>Sakib Hussain</b> (8.39 HP Econ, 80% consistency).',
    body_style
))

story.append(Spacer(1, 8))
story.append(HRFlowable(width="100%", thickness=1, color=accent_pink, spaceAfter=8))

story.append(Paragraph(
    '<b>Conclusion & Submission Sign-Off:</b> By quantifying delivery-level pressure across 201,000 balls rather than relying on reputation, '
    'this data framework proves that <b>Ashutosh Sharma</b> and <b>Rasikh Salam / Sakib Hussain</b> are the most undervalued clutch assets in Indian cricket. '
    'Backing them at the IPL 2027 Auction provides Rajasthan Royals with a sustainable, mathematically optimized route to the IPL trophy.',
    callout_style
))

doc.build(story, canvasmaker=NumberedCanvas)
print('Optimized 4-page PDF generated successfully at:', pdf_path)
