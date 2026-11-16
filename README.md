# Rajasthan Royals — SupeRR Selector Season 2: IPL 2027 Auction Strategy

[![Rajasthan Royals](https://img.shields.io/badge/Rajasthan_Royals-IPL_2027-E6196E?style=for-the-badge&logo=cricket)](https://www.rajasthanroyals.com)
[![Status](https://img.shields.io/badge/War_Room-Submission_Ready-001D48?style=for-the-badge)](https://unstop.com)
[![License](https://img.shields.io/badge/Analytics-Proprietary-C59B27?style=for-the-badge)]()

Empirical Sabermetric Scouting System developed for **Rajasthan Royals (RR)** on **Unstop** for the **SupeRR Selector Season 2 Competition**. Evaluated for Head Coach **Kumar Sangakkara** and Director of Strategy and Analytics **Giles Lindsay**.

---

## 📌 Executive Summary
In IPL mega auctions, acquiring established international finishers and death bowlers often consumes over 60% of a franchise's total purse. This repository introduces an empirical sabermetric methodology to identify **Uncapped Domestic Players** who perform reliably under high match pressure ($PI \ge 0.65$) at a fraction of marquee valuations.

- **Dataset Crucible**: 201,000 Deliveries across 867 Matches (IPL 2022–2026, T20Is, Asia Cups).
- **Auction Pool Filter**: All 10 franchises' officially retained stars (Bumrah, Narine, Surya, Klaasen, Tilak, Rinku, Gill, Shashank, etc.) are strictly excluded.
- **Venue Optimization**: Tailored specifically for **Sawai Mansingh Stadium (Jaipur)** with its 75m+ square boundaries and pace-off friction.

---

## 🎯 Top 10 Target Boards (Uncapped Domestic)

### Top 10 Uncapped Batsmen Available in Auction
| Rank | Player Name | HP Strike Rate | Base SR | $\Delta$SR Elevation | HP Avg | Boundary % | Repeatability | Tactical Role for Rajasthan Royals |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **Ashutosh Sharma** | **186.6** | 103.5 | **+83.1** | 25.7 | **27.1%** | 46.2% | **Primary #6/#7 Finisher**: Solves death-overs scoring lag |
| **2** | **Sameer Rizvi** | **182.7** | 131.7 | **+51.0** | 22.8 | 25.3% | 50.0% | **Middle-Overs Spin Enforcer**: Clears 75m Jaipur ropes |
| **3** | **Aniket Verma** | **190.5** | 138.4 | **+52.1** | 17.8 | **27.4%** | 25.0% | **Dynamic Impact Accelerator**: Highest raw HP strike rate |
| **4** | **Nehal Wadhera** | **170.7** | 121.3 | **+49.4** | 17.5 | 25.3% | 31.6% | **Middle-Order Match-up Anchor**: Left-handed presence |
| **5** | **Anuj Rawat** | 149.0 | 101.1 | **+47.9** | **35.8** | 19.8% | 40.0% | **Crisis Rebuilder & Backup WK**: Elite 35.8 crisis average |
| **6** | **Mukul Choudhary** | 158.1 | 115.2 | **+42.9** | 23.4 | 20.3% | **57.1%** | **Developmental Striker**: High ceiling at bargain price |
| **7** | **Mahipal Lomror** | 166.1 | 144.9 | **+21.2** | 13.6 | 24.3% | 41.2% | **Jaipur Venue Specialist**: Local SMS Stadium familiarity |
| **8** | **M Shahrukh Khan** | 168.2 | 134.2 | **+34.1** | 18.7 | 21.3% | 18.8% | **High-Pace Muscle Hitter**: Clears 145+ kph bowling |
| **9** | **Shubham Dubey** | 160.2 | 130.0 | **+30.2** | 18.1 | 21.2% | 33.3% | **Left-Hand Floater**: Boundary hitter against wide lines |
| **10** | **Angkrish Raghuvanshi** | 151.1 | 144.6 | **+6.5** | 20.3 | 20.2% | 40.0% | **Low-Dot Anchor**: 26.6% dot rate keeps board ticking |

### Top 10 Uncapped Bowlers Available in Auction
*(League High-Pressure Economy Average = 9.61 RPO)*
| Rank | Player Name | Style | HP Economy | Base Econ | $\Delta$Econ Diff | HP Strike Rate | Wkts | Dot % | Repeatability | Tactical Role for Rajasthan Royals |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **Sakib Hussain** | Pace | **8.39** | 10.14 | **+1.75** | 12.0 | 9 | 31.6% | **80.0%** | **Elite Death Specialist**: Sub-9 RPO for < ₹1.5 Cr |
| **2** | **Rasikh Salam** | Pace | 9.41 | 9.71 | **+0.30** | **9.08** | **26** | 31.6% | **70.0%** | **Strike Wicket-Taker**: 26 wickets under intense heat |
| **3** | **Gurjapneet Singh** | Pace | **8.47** | 9.04 | **+0.57** | 14.2 | 6 | 27.8% | 66.7% | **Left-Arm Seam Angle**: Awkward bounce, 13.3% bnd rate |
| **4** | **Anshul Kamboj** | Pace | 9.85 | 10.01 | **+0.16** | **9.46** | 13 | **36.2%** | 53.8% | **Hit-the-Deck Enforcer**: Extracts steepling bounce |
| **5** | **Suyash Sharma** | Spin | **8.42** | 8.76 | **+0.34** | 21.5 | 12 | **37.5%** | 50.0% | **SMS Stadium Squeeze**: 75m ropes trap mis-hit googlies |
| **6** | **Ashwani Kumar** | Pace | 11.01 | 10.74 | -0.27 | **8.78** | 9 | **36.8%** | **85.7%** | **Express Pace Weapon**: 8.78 strike rate at the death |
| **7** | **Praful Hinge** | Pace | 10.82 | 11.76 | **+0.94** | 12.2 | 5 | **38.5%** | **85.7%** | **Dot-Ball Machine**: 38.5% death overs dot ball rate |
| **8** | **Brijesh Sharma** | Pace | **9.27** | 9.92 | **+0.64** | 15.7 | 7 | 30.3% | 36.4% | **Second-Innings Squeeze**: Disciplined back-of-length lines |
| **9** | **Harpreet Brar** | Spin | 10.11 | 8.02 | -2.09 | 14.6 | 5 | 35.5% | 40.0% | **Match-up Dart**: Skids into stumps against RH power |
| **10** | **Akash Madhwal** | Pace | 10.64 | 9.57 | -1.08 | 13.3 | 11 | 28.8% | 50.0% | **Blockhole Yorker**: Proven IPL playoff experience |

---

## 💻 Interactive War Room Dashboard
The repository includes `rr_pressure_war_room_dashboard.html`, a standalone sports analytics command dashboard styled in Rajasthan Royals' official **White and Pink** brand system.

- **100% Native Inline CSS**: Zero external CDN dependencies, fully offline-compatible.
- **Official Brand Assets**: Embedded high-resolution vector emblem and authentic Rajasthan Royals crest.
- **Contextual Search & Role Filters**: Filter by Finishers, Spin Hitters, Keepers, Pace, or Death Bowlers.
- **Live Auction Purse Allocator**: Check/uncheck targets to live-calculate total expenditure and remaining budget from ₹44.50 Cr.

To view locally:
```bash
open rr_pressure_war_room_dashboard.html
```

---

## 📁 Repository Structure
```text
├── rr_pressure_war_room_dashboard.html                   # Interactive White & Pink War Room Dashboard
├── SupeRR_Selector_Season_2_Methodology_and_Strategy_Report.pdf  # Official 4-Page Submission PDF
├── SupeRR_Selector_Season_2_Strategy_Presentation.pptx   # Executive 16:9 Slide Presentation
├── SupeRR_Selector_Season_2_Methodology_Report.md        # Comprehensive Sabermetric Methodology Report
├── top_10_uncapped_auction_batters.csv                   # Top 10 Uncapped Batters Dataset
├── top_10_uncapped_auction_bowlers.csv                   # Top 10 Uncapped Bowlers Dataset
├── top_10_auction_batters.csv                            # Overall Top 10 Batters Dataset
├── rr_ipl2027_auction_target_board.csv                   # Mixed Master Target Board
├── full_batting_pressure_rankings.csv                    # Complete Batting Rankings
├── full_bowling_pressure_rankings.csv                    # Complete Bowling Rankings
├── generate_pdf_report.py                                # Python script to build 4-page submission PDF
├── generate_pptx_deck.py                                 # Python script to build 16:9 presentation deck
├── build_white_pink_dashboard.py                         # Python builder for the interactive dashboard
├── batting_pressure_matrix.png                           # Pressure vs Baseline Batting Quadrant
├── bowling_pressure_matrix.png                           # Economy vs Strike Rate Bowling Quadrant
└── pressure_index_distribution.png                       # Empirical Dynamic Pressure Index Curve
```

---

## ⚖️ License
Proprietary analytics prepared for Rajasthan Royals Cricket Limited and Unstop SupeRR Selector Season 2.
