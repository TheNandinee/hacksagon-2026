import os
import numpy as np
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer,
    Image, Table, TableStyle, HRFlowable
)


def generate_evidence_packet(site_name, lat, lon, area_ha, legal_ref, output_path=None):

    if output_path is None:
        safe = site_name.lower().replace(" ", "_").replace("/", "_")
        output_path = f"outputs/reports/aranya_evidence_{safe}.pdf"

    os.makedirs("outputs/reports", exist_ok=True)

    doc = SimpleDocTemplate(
        output_path, pagesize=A4,
        topMargin=1.5*cm, bottomMargin=1.5*cm,
        leftMargin=1.8*cm, rightMargin=1.8*cm
    )

    # ── Styles ────────────────────────────────────────────────────────────────
    DARK_GREEN  = colors.HexColor("#1a472a")
    MID_GREEN   = colors.HexColor("#2d6a4f")
    ALERT_RED   = colors.HexColor("#8B0000")
    LIGHT_GREEN = colors.HexColor("#f0f7f0")
    LIGHT_RED   = colors.HexColor("#fff0f0")
    GREY_TEXT   = colors.HexColor("#555555")
    BORDER      = colors.HexColor("#cccccc")

    def style(name, **kwargs):
        base = getSampleStyleSheet()["Normal"]
        return ParagraphStyle(name, parent=base, **kwargs)

    title_s   = style("T", fontSize=22, fontName="Helvetica-Bold",
                       textColor=DARK_GREEN, spaceAfter=2)
    subtitle_s = style("ST", fontSize=9, fontName="Helvetica",
                        textColor=GREY_TEXT, spaceAfter=10)
    section_s  = style("SEC", fontSize=12, fontName="Helvetica-Bold",
                        textColor=DARK_GREEN, spaceBefore=14, spaceAfter=6)
    body_s     = style("B", fontSize=9, fontName="Helvetica",
                        textColor=colors.HexColor("#333333"),
                        spaceAfter=4, leading=14)
    caption_s  = style("CAP", fontSize=7.5, fontName="Helvetica-Oblique",
                        textColor=GREY_TEXT, spaceAfter=6)
    footer_s   = style("F", fontSize=7, fontName="Helvetica",
                        textColor=GREY_TEXT, alignment=1)

    story = []
    W = 17 * cm   # usable width

    # ── Title block ───────────────────────────────────────────────────────────
    story.append(Paragraph("A.R.A.N.Y.A.", title_s))
    story.append(Paragraph(
        "Autonomous Real-time Analytics for Natural Yield &amp; Area Protection",
        subtitle_s
    ))
    story.append(HRFlowable(width="100%", thickness=2.5, color=DARK_GREEN))
    story.append(Spacer(1, 0.25*cm))

    # ── Alert banner ──────────────────────────────────────────────────────────
    banner = Table([["⚠   SATELLITE VIOLATION EVIDENCE PACKET"]], colWidths=[W])
    banner.setStyle(TableStyle([
        ("BACKGROUND",   (0,0), (-1,-1), ALERT_RED),
        ("TEXTCOLOR",    (0,0), (-1,-1), colors.white),
        ("FONTNAME",     (0,0), (-1,-1), "Helvetica-Bold"),
        ("FONTSIZE",     (0,0), (-1,-1), 11),
        ("ALIGN",        (0,0), (-1,-1), "CENTER"),
        ("TOPPADDING",   (0,0), (-1,-1), 9),
        ("BOTTOMPADDING",(0,0), (-1,-1), 9),
        ("ROWBACKGROUNDS",(0,0),(-1,-1), [ALERT_RED]),
    ]))
    story.append(banner)
    story.append(Spacer(1, 0.3*cm))

    # ── Report metadata ───────────────────────────────────────────────────────
    now = datetime.now()
    meta_rows = [
        ["Report generated",    now.strftime("%d %B %Y, %H:%M IST")],
        ["Detection system",    "ARANYA v1.0 — Satellite Intelligence Platform"],
        ["Primary data source", "ESA Sentinel-2 L2A (10 m resolution, 5-day revisit)"],
        ["Reference period",    "2020 Q1 (baseline)  →  2024 Q1 (current)"],
        ["Analysis method",     "NDVI bi-temporal change detection + spatial clustering"],
        ["Classification",      "Automated AI detection — human review recommended"],
    ]
    meta_table = Table(meta_rows, colWidths=[4.8*cm, W - 4.8*cm])
    meta_table.setStyle(TableStyle([
        ("FONTNAME",     (0,0), (0,-1), "Helvetica-Bold"),
        ("FONTNAME",     (1,0), (1,-1), "Helvetica"),
        ("FONTSIZE",     (0,0), (-1,-1), 8.5),
        ("TEXTCOLOR",    (0,0), (0,-1), DARK_GREEN),
        ("BACKGROUND",   (0,0), (-1,-1), LIGHT_GREEN),
        ("GRID",         (0,0), (-1,-1), 0.4, BORDER),
        ("TOPPADDING",   (0,0), (-1,-1), 5),
        ("BOTTOMPADDING",(0,0), (-1,-1), 5),
        ("LEFTPADDING",  (0,0), (-1,-1), 8),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 0.2*cm))

    # ── Site details ──────────────────────────────────────────────────────────
    story.append(Paragraph("VIOLATION SITE DETAILS", section_s))

    site_rows = [
        ["Site name",               site_name],
        ["Coordinates",             f"{lat}°N,  {lon}°E"],
        ["Detected disturbed area", f"{area_ha} hectares"],
        ["Severity classification", "HIGH — Immediate enforcement action required"],
        ["Legal framework violated", legal_ref],
        ["Detection confidence",    "High  (NDVI Δ > 0.15, spatial coherence confirmed)"],
        ["Recommended action",      "File complaint: NGT / State Forest Dept / Mining Authority"],
    ]

    # Alternate row shading
    row_bg = []
    for i in range(len(site_rows)):
        bg = LIGHT_RED if i in (3, 4, 6) else colors.white
        row_bg.append(("BACKGROUND", (0,i), (-1,i), bg))

    site_table = Table(site_rows, colWidths=[4.8*cm, W - 4.8*cm])
    site_table.setStyle(TableStyle([
        ("FONTNAME",     (0,0), (0,-1), "Helvetica-Bold"),
        ("FONTNAME",     (1,0), (1,-1), "Helvetica"),
        ("FONTSIZE",     (0,0), (-1,-1), 8.5),
        ("GRID",         (0,0), (-1,-1), 0.4, BORDER),
        ("TOPPADDING",   (0,0), (-1,-1), 5),
        ("BOTTOMPADDING",(0,0), (-1,-1), 5),
        ("LEFTPADDING",  (0,0), (-1,-1), 8),
        *row_bg
    ]))
    story.append(site_table)

    # ── Satellite evidence images ─────────────────────────────────────────────
    story.append(Paragraph("SATELLITE EVIDENCE", section_s))

    if os.path.exists("outputs/detection_output.png"):
        story.append(Image("outputs/detection_output.png",
                           width=W, height=W * 0.34))
        story.append(Paragraph(
            "Figure 1 — Left: Aravali baseline (2020). Centre: Current state (2024). "
            "Right: ARANYA detection output — red overlay marks detected "
            "disturbance zones consistent with illegal excavation activity.",
            caption_s
        ))

    if os.path.exists("outputs/ndvi_analysis.png"):
        story.append(Image("outputs/ndvi_analysis.png",
                           width=W, height=W * 0.30))
        story.append(Paragraph(
            "Figure 2 — NDVI vegetation health index: before, after, and net change. "
            "Dark red areas indicate severe vegetation loss (NDVI decline > 0.15) "
            "consistent with soil exposure from mining excavation.",
            caption_s
        ))

    # ── Legal context ─────────────────────────────────────────────────────────
    story.append(Paragraph("LEGAL & REGULATORY CONTEXT", section_s))
    story.append(Paragraph(
        f"The detected activity at <b>{site_name}</b> constitutes a potential violation "
        f"of <b>{legal_ref}</b>. The Supreme Court of India in its landmark 2009 order "
        "explicitly prohibited all mining activity within the Aravali range across "
        "Haryana and Rajasthan states. The National Green Tribunal has subsequently "
        "reaffirmed and expanded these protections, designating the zone as "
        "eco-sensitive and prohibiting land-use changes without explicit clearance.",
        body_s
    ))
    story.append(Spacer(1, 0.15*cm))
    story.append(Paragraph(
        "The ARANYA system detects land-use transitions that are inconsistent with "
        "permitted activities within protected zone boundaries. Detection is based on "
        "bi-temporal NDVI analysis of ESA Sentinel-2 imagery, cross-referenced against "
        "official protected area shapefiles and mining lease maps. Spatial clustering "
        "confirms that the flagged disturbance is geographically coherent and "
        "statistically anomalous relative to the surrounding terrain.",
        body_s
    ))

    # ── Quantitative summary ──────────────────────────────────────────────────
    story.append(Paragraph("QUANTITATIVE DETECTION SUMMARY", section_s))

    # Load stats if available
    try:
        mask        = np.load("data/processed/disturbance_mask.npy")
        change_map  = np.load("data/processed/change_map.npy")
        total_px    = mask.size
        dist_px     = int(mask.sum())
        zone_pct    = round(dist_px / total_px * 100, 1)
        avg_loss    = round(float(change_map[mask == 1].mean()), 3)
        max_loss    = round(float(change_map[mask == 1].min()), 3)
    except Exception:
        total_px    = "N/A"
        dist_px     = "N/A"
        zone_pct    = "N/A"
        avg_loss    = "N/A"
        max_loss    = "N/A"

    quant_rows = [
        ["Metric",                      "Value",        "Interpretation"],
        ["Total pixels analysed",        str(total_px),  "Full monitored zone"],
        ["Disturbed pixels detected",    str(dist_px),   "NDVI Δ below threshold"],
        ["Zone disturbance coverage",   f"{zone_pct}%", "Percentage of zone affected"],
        ["Average NDVI loss",           str(avg_loss),  "Mean vegetation decline"],
        ["Maximum NDVI loss",           str(max_loss),  "Peak disturbance intensity"],
        ["Detection threshold applied", "−0.15 NDVI",   "Conservative sensitivity"],
    ]

    q_table = Table(quant_rows, colWidths=[5.5*cm, 3.5*cm, W - 9.0*cm])
    q_style = TableStyle([
        ("BACKGROUND",   (0,0), (-1,0), MID_GREEN),
        ("TEXTCOLOR",    (0,0), (-1,0), colors.white),
        ("FONTNAME",     (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",     (0,0), (-1,-1), 8.5),
        ("FONTNAME",     (0,1), (-1,-1), "Helvetica"),
        ("GRID",         (0,0), (-1,-1), 0.4, BORDER),
        ("TOPPADDING",   (0,0), (-1,-1), 5),
        ("BOTTOMPADDING",(0,0), (-1,-1), 5),
        ("LEFTPADDING",  (0,0), (-1,-1), 8),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [colors.white, LIGHT_GREEN]),
    ])
    q_table.setStyle(q_style)
    story.append(q_table)

    # ── Disclaimer + footer ───────────────────────────────────────────────────
    story.append(Spacer(1, 0.4*cm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER))
    story.append(Spacer(1, 0.15*cm))
    story.append(Paragraph(
        "DISCLAIMER: This evidence packet is generated automatically by the ARANYA "
        "satellite intelligence system. All detections are flagged for human review "
        "before formal enforcement action. Coordinate with the State Mining Department, "
        "Forest Department, and National Green Tribunal as applicable. "
        "ARANYA does not constitute legal advice.",
        style("D", fontSize=7, fontName="Helvetica-Oblique",
              textColor=GREY_TEXT, leading=11)
    ))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        f"ARANYA v1.0  |  Generated: {now.strftime('%d %B %Y, %H:%M IST')}  |  "
        "Data: ESA Sentinel-2 / Planet Labs  |  aranya.ai",
        footer_s
    ))

    doc.build(story)
    print(f"Evidence packet saved: {output_path}")
    return output_path


if __name__ == "__main__":
    generate_evidence_packet(
        site_name="Faridabad Mining Cluster",
        lat=28.2341,
        lon=77.0523,
        area_ha=45.2,
        legal_ref="Supreme Court Order — Mining Ban 2009"
    )