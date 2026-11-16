import os
import pandas as pd
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# Initialize Presentation
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Color Palette (Rajasthan Royals Brand)
NAVY = RGBColor(0, 29, 72)       # #001D48
PINK = RGBColor(230, 25, 110)    # #E6196E
GOLD = RGBColor(197, 155, 39)    # #C59B27
WHITE = RGBColor(255, 255, 255)
DARK_TEXT = RGBColor(30, 41, 59) # #1E293B
MUTED_TEXT = RGBColor(100, 116, 139) # #64748B
LIGHT_BG = RGBColor(248, 250, 252)   # #F8FAFC
CARD_BG = RGBColor(241, 245, 249)    # #F1F5F9
BORDER_COLOR = RGBColor(226, 232, 240)

def set_slide_background(slide, color):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_header(slide, title_text, category_text="RAJASTHAN ROYALS | IPL 2027 AUCTION STRATEGY"):
    # Category Tracker
    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.3))
    tf_c = cat_box.text_frame
    tf_c.word_wrap = True
    p_c = tf_c.paragraphs[0]
    p_c.text = category_text.upper()
    p_c.font.size = Pt(10)
    p_c.font.bold = True
    p_c.font.color.rgb = PINK
    
    # Slide Title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.65), Inches(11.7), Inches(0.6))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title_text
    p_t.font.size = Pt(22)
    p_t.font.bold = True
    p_t.font.color.rgb = NAVY

    # Accent line
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.3), Inches(11.733), Inches(0.02))
    line.fill.solid()
    line.fill.fore_color.rgb = PINK
    line.line.color.rgb = PINK

# ==========================================
# SLIDE 1: TITLE SLIDE (Royals Navy Theme)
# ==========================================
slide1 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_background(slide1, NAVY)

# Title Card Accent
pink_bar = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.2), Inches(1.8), Inches(0.15), Inches(3.2))
pink_bar.fill.solid()
pink_bar.fill.fore_color.rgb = PINK
pink_bar.line.color.rgb = PINK

# Title Box
tbox = slide1.shapes.add_textbox(Inches(1.5), Inches(1.6), Inches(10.5), Inches(3.5))
tf = tbox.text_frame
tf.word_wrap = True

p0 = tf.paragraphs[0]
p0.text = "SUPERR SELECTOR SEASON 2"
p0.font.size = Pt(14)
p0.font.bold = True
p0.font.color.rgb = PINK

p1 = tf.add_paragraph()
p1.text = "Most Reliable Players Under Pressure"
p1.font.size = Pt(36)
p1.font.bold = True
p1.font.color.rgb = WHITE
p1.space_before = Pt(8)

p2 = tf.add_paragraph()
p2.text = "Empirical Sabermetric Scouting & Roster Optimization for Rajasthan Royals"
p2.font.size = Pt(18)
p2.font.color.rgb = GOLD
p2.space_before = Pt(8)

p3 = tf.add_paragraph()
p3.text = "Featuring: Top 10 Uncapped Domestic Batsmen & Top 10 Uncapped Domestic Bowlers Available in the IPL Auction"
p3.font.size = Pt(13)
p3.font.color.rgb = RGBColor(203, 213, 225)
p3.space_before = Pt(12)

# Footer metadata card
meta_box = slide1.shapes.add_textbox(Inches(1.2), Inches(5.6), Inches(10.8), Inches(1.2))
tf_m = meta_box.text_frame
p_m1 = tf_m.paragraphs[0]
p_m1.text = "Evaluators: Kumar Sangakkara (Head Coach & Director of Cricket) | Giles Lindsay (Director of Strategy & Analytics)"
p_m1.font.size = Pt(11)
p_m1.font.bold = True
p_m1.font.color.rgb = WHITE

p_m2 = tf_m.add_paragraph()
p_m2.text = "Dataset: 201,000 Deliveries, 867 Matches (IPL 2022–2026, T20Is, Asia Cups). Retained Stars Strictly Filtered Out."
p_m2.font.size = Pt(10)
p_m2.font.color.rgb = RGBColor(148, 163, 184)
p_m2.space_before = Pt(4)


# ==========================================
# SLIDE 2: METHODOLOGY & PRESSURE MODELING
# ==========================================
slide2 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_background(slide2, LIGHT_BG)
add_header(slide2, "Dynamic Pressure Modeling & Auction Pool Eligibility", "METHODOLOGY & SABERMETRIC ARCHITECTURE")

# Methodology Cards (Left Side)
card1 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(6.0), Inches(5.4))
card1.fill.solid()
card1.fill.fore_color.rgb = WHITE
card1.line.color.rgb = BORDER_COLOR

tf1 = card1.text_frame
tf1.word_wrap = True
tf1.margin_left = Inches(0.3)
tf1.margin_right = Inches(0.3)
tf1.margin_top = Inches(0.3)

p = tf1.paragraphs[0]
p.text = "Dynamic Pressure Index (PI) Formulation"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY

bullets = [
    ("Scoreboard Strain (Chases):", "Modeled via sigmoidal Required Run Rate: S_RRR = 1 / (1 + exp(-0.60 * (RRR - 9.50))). Wickets lost accelerate strain via (W / 9)^1.20."),
    ("Temporal Urgency Multiplier:", "Urgency escalates late: M_time = 0.40 + 0.60 * (1 - Balls_Remaining / 120). Final 24 balls chasing <= 50 runs receive a +0.15 clutch kicker."),
    ("Target-Setting (1st Innings):", "Early collapse recovery (W - 0.25*Over)/4.50 combined with death-over acceleration ramp (overs 16-20 scaled to PI 0.65 - 1.00)."),
    ("Playoffs & High-Pressure Cutoff:", "+15% knockout multiplier. Across 201k deliveries, PI >= 0.65 isolates exactly the top 25.5% (51,176 deliveries) of pure match crucible."),
    ("Strict Auction Pool Filtering:", "All 10 franchises' retained stars (Bumrah, Narine, Surya, Klaasen, Rinku, Gill, Shashank, etc.) strictly excluded. Focus is 100% on actionable auction targets.")
]

for title, desc in bullets:
    p = tf1.add_paragraph()
    p.text = f"• {title} "
    p.font.bold = True
    p.font.size = Pt(10)
    p.font.color.rgb = PINK
    p.space_before = Pt(8)
    
    run = p.add_run()
    run.text = desc
    run.font.bold = False
    run.font.size = Pt(9.5)
    run.font.color.rgb = DARK_TEXT

# Chart on Right Side
chart_path = '/Users/jainil.30/Downloads/RR/pressure_index_distribution.png'
if os.path.exists(chart_path):
    slide2.shapes.add_picture(chart_path, Inches(7.1), Inches(1.5), width=Inches(5.4))


# ==========================================
# SLIDE 3: TOP 10 UNCAPPED BATSMEN (TABLE)
# ==========================================
slide3 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_background(slide3, LIGHT_BG)
add_header(slide3, "Top 10 Uncapped Domestic Batsmen Available in Auction", "AUCTION TARGET BOARD | BATTING DEPARTMENT")

# Read Data
df_bat = pd.read_csv('/Users/jainil.30/Downloads/RR/top_10_uncapped_auction_batters.csv')

# Create Table
rows = 11
cols = 9
table_shape = slide3.shapes.add_table(rows, cols, Inches(0.8), Inches(1.5), Inches(11.733), Inches(5.4))
table = table_shape.table

# Column Widths
col_widths = [Inches(0.6), Inches(2.2), Inches(1.1), Inches(1.1), Inches(1.1), Inches(1.1), Inches(1.0), Inches(1.1), Inches(2.433)]
for i, w in enumerate(col_widths):
    table.columns[i].width = w

headers = ["Rank", "Batter Name", "HP SR", "Base SR", "Δ SR", "HP Avg", "Bnd %", "Repeat %", "Tactical Fit for RR"]
roles_bat = {
    "Ashutosh Sharma": "Primary #6/#7 death finisher; fixes lower-order finishing void",
    "Sameer Rizvi": "Middle-overs spin destroyer; high boundary % in crisis",
    "Aniket Verma": "Elite strike-rate accelerator; dynamic Impact Sub",
    "Nehal Wadhera": "High-tempo left-handed middle-order anchor & crisis rebuilder",
    "Anuj Rawat": "Crisis stabilizer & domestic backup wicketkeeper",
    "Mukul Choudhary": "High-ceiling power-hitting developmental asset",
    "Mahipal Lomror": "Jaipur home ground expert; middle-overs pace/spin basher",
    "M Shahrukh Khan": "Proven high-pace muscle hitter for death-over boundaries",
    "Shubham Dubey": "Left-handed lower-order boundary clearer",
    "Angkrish Raghuvanshi": "Low-dot rotation anchor with high baseline adaptability"
}

for j, h in enumerate(headers):
    cell = table.cell(0, j)
    cell.fill.solid()
    cell.fill.fore_color.rgb = NAVY
    p = cell.text_frame.paragraphs[0]
    p.text = h
    p.font.bold = True
    p.font.size = Pt(10)
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER if j not in [1, 8] else (PP_ALIGN.LEFT if j == 8 else PP_ALIGN.LEFT)

for i, row in df_bat.iterrows():
    r_idx = i + 1
    p_name = row['striker_name']
    c_bg = WHITE if i % 2 == 0 else CARD_BG
    
    vals = [
        str(row['rank']),
        p_name,
        f"{row['hp_sr']:.1f}",
        f"{row['base_sr']:.1f}",
        f"+{row['sr_diff']:.1f}",
        f"{row['hp_avg']:.1f}",
        f"{row['hp_bnd_pct']:.1f}%",
        f"{row['success_rate']*100:.0f}%",
        roles_bat.get(p_name, "Auction target")
    ]
    
    for j, val in enumerate(vals):
        cell = table.cell(r_idx, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = c_bg
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.size = Pt(9)
        p.font.color.rgb = DARK_TEXT
        if j == 0:
            p.font.bold = True
            p.alignment = PP_ALIGN.CENTER
        elif j == 1:
            p.font.bold = True
            p.font.color.rgb = NAVY
            p.alignment = PP_ALIGN.LEFT
        elif j == 4:
            p.font.bold = True
            p.font.color.rgb = PINK
            p.alignment = PP_ALIGN.CENTER
        elif j in [2, 3, 5, 6, 7]:
            p.alignment = PP_ALIGN.CENTER
        else:
            p.alignment = PP_ALIGN.LEFT


# ==========================================
# SLIDE 4: BATSMEN SCOUTING & ROSTER FIT
# ==========================================
slide4 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_background(slide4, LIGHT_BG)
add_header(slide4, "Key Batsmen Strategic Deep Dive & Jaipur Fit", "TACTICAL BLUEPRINT | BATTING DEPARTMENT")

top_batters_scout = [
    ("Ashutosh Sharma (Rank 1 | CBR: 63.71)",
     "HP SR: 186.6 | Base SR: 103.5 | Elevation: +83.1 SR | Boundary: 27.1%",
     "The #1 pressure batter in the auction. Showcased unmatched composure in near-impossible chases (e.g. 61 off 28 vs MI, 31* off 17 vs GT). Directly solves Rajasthan's biggest vulnerability in recent seasons: lower-order collapse when Samson or Parag fall. Expected bid: INR 3.5 - 5.5 Cr."),
    
    ("Sameer Rizvi (Rank 2 | CBR: 60.94)",
     "HP SR: 182.7 | Base SR: 131.7 | Elevation: +51.0 SR | 50% Match Consistency",
     "Elite hitter of spin bowling under crisis. At Jaipur's Sawai Mansingh Stadium where square boundaries are 75m+, his high trajectory arc clears long-on and mid-wicket effortlessly. Perfect #5 or #6 floater. Expected bid: INR 2.0 - 4.0 Cr."),
     
    ("Aniket Verma (Rank 3 | CBR: 58.35)",
     "HP SR: 190.5 | Highest HP SR in Auction | Elevation: +52.1 SR | Boundary: 27.4%",
     "Highest raw strike rate under heat in the domestic pool. Explosive high-impact boundary hunter who minimizes dot balls and attacks from delivery one. Ideal Impact Player weapon. Expected bid: INR 0.8 - 1.8 Cr."),
     
    ("Nehal Wadhera & Anuj Rawat (Ranks 4 & 5)",
     "Wadhera: HP SR 170.7 (+49.4 diff) | Rawat: HP Avg 35.8 (+47.9 SR diff)",
     "Wadhera brings proven IPL pressure knocks for MI and provides a tactical left-handed match-up against off-spin and leg-spin. Rawat offers high crisis average (35.8) plus domestic wicketkeeping redundancy behind Sanju Samson.")
]

for idx, (b_title, b_metrics, b_desc) in enumerate(top_batters_scout):
    y_pos = Inches(1.5 + idx * 1.35)
    card = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y_pos, Inches(11.733), Inches(1.22))
    card.fill.solid()
    card.fill.fore_color.rgb = WHITE
    card.line.color.rgb = BORDER_COLOR
    
    # Left vertical accent
    acc = slide4.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), y_pos, Inches(0.1), Inches(1.22))
    acc.fill.solid()
    acc.fill.fore_color.rgb = PINK if idx == 0 else (GOLD if idx == 1 else NAVY)
    acc.line.color.rgb = acc.fill.fore_color.rgb
    
    tf_card = card.text_frame
    tf_card.word_wrap = True
    tf_card.margin_left = Inches(0.25)
    tf_card.margin_top = Inches(0.12)
    
    p = tf_card.paragraphs[0]
    p.text = b_title
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = NAVY
    
    p_m = tf_card.add_paragraph()
    p_m.text = b_metrics
    p_m.font.size = Pt(9.5)
    p_m.font.bold = True
    p_m.font.color.rgb = PINK
    p_m.space_before = Pt(2)
    
    p_d = tf_card.add_paragraph()
    p_d.text = b_desc
    p_d.font.size = Pt(9)
    p_d.font.color.rgb = DARK_TEXT
    p_d.space_before = Pt(3)


# ==========================================
# SLIDE 5: TOP 10 UNCAPPED BOWLERS (TABLE)
# ==========================================
slide5 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_background(slide5, LIGHT_BG)
add_header(slide5, "Top 10 Uncapped Domestic Bowlers Available in Auction", "AUCTION TARGET BOARD | BOWLING DEPARTMENT")

# Read Data
df_bowl = pd.read_csv('/Users/jainil.30/Downloads/RR/top_10_uncapped_auction_bowlers.csv')

# Create Table
rows = 11
cols = 10
table_shape5 = slide5.shapes.add_table(rows, cols, Inches(0.8), Inches(1.5), Inches(11.733), Inches(5.4))
table5 = table_shape5.table

col_widths5 = [Inches(0.55), Inches(2.0), Inches(0.8), Inches(1.0), Inches(1.0), Inches(0.95), Inches(0.95), Inches(0.95), Inches(0.95), Inches(2.633)]
for i, w in enumerate(col_widths5):
    table5.columns[i].width = w

headers5 = ["Rank", "Bowler Name", "Type", "HP Econ", "Base Econ", "Diff", "HP SR", "Dot %", "Repeat %", "Tactical Fit for RR"]
roles_bowl = {
    "Sakib Hussain": "Elite death over yorker specialist; out-economizes base by +1.75 RPO",
    "Rasikh Salam": "High-strike death wicket-taker (9.08 balls/wkt); 26 pressure wickets",
    "Gurjapneet Singh": "Tall left-arm pace angle; stingy 13.3% boundary concession",
    "Anshul Kamboj": "Hit-the-deck pace enforcer; 9.46 strike rate and 36.2% dots",
    "Suyash Sharma": "Jaipur 75m spin squeeze weapon; 8.42 HP Econ & 37.5% dot ball rate",
    "Ashwani Kumar": "High-velocity strike bowler (8.78 HP SR); 85.7% repeatability",
    "Praful Hinge": "Disciplined hit-the-deck pacer with 38.5% dot ball suppression",
    "Brijesh Sharma": "Containment seam bowler; tight economy under second-innings heat",
    "Harpreet Brar": "Flat stump-to-stump dart specialist against right-handed power hitters",
    "Akash Madhwal": "Proven IPL playoff yorker specialist; executes under high scrutiny"
}

for j, h in enumerate(headers5):
    cell = table5.cell(0, j)
    cell.fill.solid()
    cell.fill.fore_color.rgb = NAVY
    p = cell.text_frame.paragraphs[0]
    p.text = h
    p.font.bold = True
    p.font.size = Pt(9.5)
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER if j not in [1, 9] else PP_ALIGN.LEFT

for i, row in df_bowl.iterrows():
    r_idx = i + 1
    p_name = row['bowler_name']
    c_bg = WHITE if i % 2 == 0 else CARD_BG
    diff_sign = "+" if row['econ_diff'] > 0 else ""
    
    vals = [
        str(row['rank']),
        p_name,
        row['pace_or_spin'],
        f"{row['hp_econ']:.2f}",
        f"{row['base_econ']:.2f}",
        f"{diff_sign}{row['econ_diff']:.2f}",
        f"{row['hp_sr']:.1f}",
        f"{row['hp_dot_pct']:.1f}%",
        f"{row['success_rate']*100:.0f}%",
        roles_bowl.get(p_name, "Auction target")
    ]
    
    for j, val in enumerate(vals):
        cell = table5.cell(r_idx, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = c_bg
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.size = Pt(8.5)
        p.font.color.rgb = DARK_TEXT
        if j == 0:
            p.font.bold = True
            p.alignment = PP_ALIGN.CENTER
        elif j == 1:
            p.font.bold = True
            p.font.color.rgb = NAVY
            p.alignment = PP_ALIGN.LEFT
        elif j == 5:
            p.font.bold = True
            p.font.color.rgb = RGBColor(16, 185, 129) if row['econ_diff'] > 0 else PINK
            p.alignment = PP_ALIGN.CENTER
        elif j in [2, 3, 4, 6, 7, 8]:
            p.alignment = PP_ALIGN.CENTER
        else:
            p.alignment = PP_ALIGN.LEFT


# ==========================================
# SLIDE 6: BOWLERS SCOUTING & ROSTER FIT
# ==========================================
slide6 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_background(slide6, LIGHT_BG)
add_header(slide6, "Key Bowlers Strategic Deep Dive & Jaipur Fit", "TACTICAL BLUEPRINT | BOWLING DEPARTMENT")

top_bowlers_scout = [
    ("Sakib Hussain (Rank 1 | CBR: 61.02)",
     "HP Econ: 8.39 RPO | Base Econ: 10.14 | Econ Outperformance: +1.75 RPO | 80% Consistency",
     "Top uncapped bowler in the dataset. While the tournament average under pressure explodes to 9.61 RPO, Sakib drops his economy by 1.75 RPO below his baseline. Concedes only 15.4% boundaries. Ideal death-over specialist to partner Sandeep Sharma. Target Valuation: INR 0.8 - 1.8 Cr."),
     
    ("Rasikh Salam (Rank 2 | CBR: 58.86)",
     "HP Strike Rate: 9.08 balls/wkt | 26 Pressure Wickets | 70% Repeatability",
     "The premier domestic death-over strike wicket-taker. Possesses an extraordinary strike rate under heat (9.08 balls per wicket) with high reverse-swing execution. Breaks partnerships in overs 17-20. Target Valuation: INR 1.5 - 3.5 Cr."),
     
    ("Gurjapneet Singh (Rank 3 | CBR: 57.95)",
     "HP Econ: 8.47 RPO | Boundary Conceded: 13.3% | 66.7% Consistency",
     "Tall left-arm seamer who generates awkward steep bounce. Restricts boundary concession under pressure to just 13.3% (best in class). Provides the critical left-arm angle Rajasthan has prized since Trent Boult. Target Valuation: INR 0.8 - 2.0 Cr."),
     
    ("Suyash Sharma & Anshul Kamboj (Ranks 4 & 5)",
     "Suyash: 8.42 HP Econ, 37.5% Dots | Kamboj: 9.46 HP Strike Rate, 36.2% Dots",
     "Suyash is tailor-made for Jaipur's Sawai Mansingh Stadium: 75m square boundaries allow him to toss the ball up with quick googlies without fearing mishits going for sixes. Kamboj provides heavy hit-the-deck pace into the pitch.")
]

for idx, (b_title, b_metrics, b_desc) in enumerate(top_bowlers_scout):
    y_pos = Inches(1.5 + idx * 1.35)
    card = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y_pos, Inches(11.733), Inches(1.22))
    card.fill.solid()
    card.fill.fore_color.rgb = WHITE
    card.line.color.rgb = BORDER_COLOR
    
    acc = slide6.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), y_pos, Inches(0.1), Inches(1.22))
    acc.fill.solid()
    acc.fill.fore_color.rgb = PINK if idx == 0 else (GOLD if idx == 1 else NAVY)
    acc.line.color.rgb = acc.fill.fore_color.rgb
    
    tf_card = card.text_frame
    tf_card.word_wrap = True
    tf_card.margin_left = Inches(0.25)
    tf_card.margin_top = Inches(0.12)
    
    p = tf_card.paragraphs[0]
    p.text = b_title
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = NAVY
    
    p_m = tf_card.add_paragraph()
    p_m.text = b_metrics
    p_m.font.size = Pt(9.5)
    p_m.font.bold = True
    p_m.font.color.rgb = PINK
    p_m.space_before = Pt(2)
    
    p_d = tf_card.add_paragraph()
    p_d.text = b_desc
    p_d.font.size = Pt(9)
    p_d.font.color.rgb = DARK_TEXT
    p_d.space_before = Pt(3)


# ==========================================
# SLIDE 7: AUCTION WAR ROOM STRATEGY & BUDGET
# ==========================================
slide7 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_background(slide7, LIGHT_BG)
add_header(slide7, "Rajasthan Royals IPL 2027 Auction War Room Execution Plan", "EXECUTION & PURSE ALLOCATION BLUEPRINT")

# Left Box: Tactical Roster Synergy
box_l = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.4))
box_l.fill.solid()
box_l.fill.fore_color.rgb = WHITE
box_l.line.color.rgb = BORDER_COLOR

tfl = box_l.text_frame
tfl.word_wrap = True
tfl.margin_left = Inches(0.3)
tfl.margin_right = Inches(0.3)
tfl.margin_top = Inches(0.3)

p = tfl.paragraphs[0]
p.text = "Roster Synergy with Core Retentions"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY

syn_points = [
    ("Closing the #6/#7 Death Void:", "With Samson, Jaiswal, and Parag commanding the top 4, RR previously suffered when matches went down to the wire. Adding Ashutosh Sharma (+83.1 SR diff) transforms RR's closing equity."),
    ("Jaipur Home Fortress Fortress (SMS Stadium):", "The 75m square boundaries punish errant spin and rewards defensive leg-spin. Suyash Sharma (8.42 HP Econ, 37.5% Dots) strangles batters who try to slog against long boundaries."),
    ("Relieving Sandeep Sharma at the Death:", "Sandeep Sharma requires a reliable partner in overs 18 & 20. Sakib Hussain (8.39 HP Econ) or Rasikh Salam (9.08 HP SR) eliminates dependence on expensive overseas fast bowlers."),
    ("Impact Sub Versatility:", "Aniket Verma (190.5 HP SR) and Gurjapneet Singh provide situational tactical leverage depending on pitch conditions and match toss.")
]

for title, desc in syn_points:
    p = tfl.add_paragraph()
    p.text = f"• {title} "
    p.font.bold = True
    p.font.size = Pt(10)
    p.font.color.rgb = PINK
    p.space_before = Pt(8)
    
    run = p.add_run()
    run.text = desc
    run.font.bold = False
    run.font.size = Pt(9.5)
    run.font.color.rgb = DARK_TEXT

# Right Box: Auction Purse Allocation Strategy
box_r = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.4))
box_r.fill.solid()
box_r.fill.fore_color.rgb = WHITE
box_r.line.color.rgb = BORDER_COLOR

tfr = box_r.text_frame
tfr.word_wrap = True
tfr.margin_left = Inches(0.3)
tfr.margin_right = Inches(0.3)
tfr.margin_top = Inches(0.3)

p = tfr.paragraphs[0]
p.text = "Target Tiers & Purse Valuation Model"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY

tiers = [
    ("Tier 1 Marquee Uncapped Targets (Budget: INR 8.0 - 10.5 Cr Total):",
     "Ashutosh Sharma (INR 4.0 - 5.5 Cr) and Rasikh Salam (INR 2.5 - 4.0 Cr). These two players immediately step into RR's starting XI in high-pressure crunch roles."),
    ("Tier 2 Tactical Accelerators (Budget: INR 4.0 - 6.5 Cr Total):",
     "Sameer Rizvi (INR 2.5 - 3.5 Cr) and Suyash Sharma (INR 1.5 - 2.5 Cr). Match-up winners specifically aligned to Jaipur pitch conditions and spin bottlenecks."),
    ("Tier 3 Value Steals & Base-Price Assets (Budget: INR 2.0 - 3.5 Cr Total):",
     "Sakib Hussain (INR 0.8 - 1.5 Cr), Gurjapneet Singh (INR 0.5 - 1.2 Cr), and Aniket Verma (INR 0.5 - 1.0 Cr). Extreme analytical upside with zero financial downside."),
    ("Franchise ROI Conclusion:",
     "Securing 4-5 of these uncapped pressure assets preserves over 65% of the auction purse for top-tier marquee acquisitions while structurally solving the franchise's crunch-over reliability.")
]

for title, desc in tiers:
    p = tfr.add_paragraph()
    p.text = f"• {title} "
    p.font.bold = True
    p.font.size = Pt(10)
    p.font.color.rgb = GOLD
    p.space_before = Pt(8)
    
    run = p.add_run()
    run.text = desc
    run.font.bold = False
    run.font.size = Pt(9.5)
    run.font.color.rgb = DARK_TEXT

# Save Presentation
pptx_path = '/Users/jainil.30/Downloads/RR/SupeRR_Selector_Season_2_Strategy_Presentation.pptx'
prs.save(pptx_path)
print(f"Presentation saved successfully to {pptx_path}")
