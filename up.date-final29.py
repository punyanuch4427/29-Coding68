from datetime import datetime
from IPython.display import display, HTML

# แสดงหัวข้อสีชมพู
display(HTML("""
<div style="background-color:#ffe6f2;
            padding:20px;
            border-radius:15px;
            text-align:center;
            font-size:24px;
            font-weight:bold;
            color:#ff3399;">
💖 โปรแกรมคำนวณอายุตามปีเกิด 💖
</div>
"""))

try:
    year_be = int(input("กรุณากรอกปีเกิด (พ.ศ.) : "))
    
    # คำนวณปีปัจจุบัน (พ.ศ.)
    current_year_be = datetime.now().year + 543
    age = current_year_be - year_be

    if age < 0:
        display(HTML("""
        <h3 style="color:red;">⚠ ปีเกิดไม่ถูกต้อง กรุณาลองใหม่ค่ะ</h3>
        """))
    else:
        display(HTML(f"""
        <div style="background-color:#fff0f5;
                    padding:15px;
                    margin-top:15px;
                    border-radius:10px;
                    text-align:center;
                    font-size:20px;
                    color:#ff1493;">
        🎀 อายุของคุณคือ {age} ปี 🎀
        </div>
        """))

except ValueError:
    display(HTML("""
    <h3 style="color:red;">⚠ กรุณากรอกตัวเลขเท่านั้นค่ะ</h3>
    """))

display(HTML("""
<p style="color:#ff66b2; text-align:center; margin-top:20px;">
Create by Punyanuch (N'Aoey) 💗
</p>
"""))
