import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# -----------------------------
# ส่วนหัว
# -----------------------------
title = widgets.HTML(
    value="""
    <div style="background:#F06292;padding:15px;border-radius:15px;color:white;text-align:center;font-size:22px;">
        💧 โปรแกรมคำนวณปริมาณน้ำที่เหมาะสมต่อวัน 💧
    </div>
    """
)

subtitle = widgets.HTML(
    value="""
    <div style="text-align:center;font-size:16px;margin-top:10px;color:#444;">
        กรอกน้ำหนักตัว แล้วกดปุ่มคำนวณได้เลย 💕
    </div>
    """
)

# -----------------------------
# ช่องกรอกน้ำหนัก
# -----------------------------
weight_input = widgets.FloatText(
    value=50.0,
    description="น้ำหนัก:",
    style={"description_width": "80px"},
    layout=widgets.Layout(width="250px")
)

unit_label = widgets.HTML("<b>กก.</b>")
input_row = widgets.HBox([weight_input, unit_label])

# -----------------------------
# ปุ่มคำนวณ
# -----------------------------
btn_calculate = widgets.Button(
    description="คำนวณ",
    button_style="danger",
    icon="calculator",
    layout=widgets.Layout(width="250px", height="40px")
)

# -----------------------------
# กล่องแสดงผล
# -----------------------------
output_box = widgets.Output()

# -----------------------------
# ฟังก์ชันคำนวณ
# -----------------------------
def calculate_water(weight):
    ml_per_kg = 33
    total_ml = weight * ml_per_kg
    total_liter = total_ml / 1000
    bottles_600 = math.ceil(total_ml / 600)
    glasses_250 = math.ceil(total_ml / 250)
    return total_ml, total_liter, bottles_600, glasses_250

def on_calculate_clicked(b):
    with output_box:
        clear_output()

        weight = weight_input.value

        if weight <= 0 or weight > 200:
            display(widgets.HTML(
                """
                <div style="background:#F8BBD0;color:#880E4F;
                            padding:12px;border-radius:12px;
                            text-align:center;font-size:16px;">
                    ⚠️ กรุณากรอกน้ำหนักให้ถูกต้อง (1 - 200 กก.)
                </div>
                """
            ))
            return

        total_ml, total_liter, bottles, glasses = calculate_water(weight)

        display(widgets.HTML(
            f"""
            <div style="background:#FCE4EC;
                        border:2px solid #F06292;
                        padding:18px;
                        border-radius:18px;">
                <h3 style="color:#C2185B;margin-top:0;">🌸 ผลการคำนวณ</h3>
                <hr style="border:1px dashed #F48FB1;">
                <p style="font-size:16px;color:#4A148C;">
                    <b>น้ำหนักตัว:</b> {weight:.1f} กก.<br><br>

                    <b>ปริมาณน้ำที่ควรดื่มต่อวัน</b><br>
                    • {total_ml:,.0f} มล.<br>
                    • {total_liter:.2f} ลิตร<br><br>

                    <b>เทียบเป็นภาชนะ</b><br>
                    • {bottles} ขวด (600 มล.)<br>
                    • {glasses} แก้ว (250 มล.)<br><br>

                    💖 <i>ดูแลสุขภาพด้วยการดื่มน้ำให้เพียงพอทุกวันนะคะ</i>
                </p>
            </div>
            """
        ))

btn_calculate.on_click(on_calculate_clicked)

# -----------------------------
# แสดง UI
# -----------------------------
ui = widgets.VBox([
    title,
    subtitle,
    widgets.HTML("<br>"),
    input_row,
    widgets.HTML("<br>"),
    btn_calculate,
    widgets.HTML("<br>"),
    output_box
])

display(ui)
