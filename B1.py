# Đoạn code của hệ thống bị lỗi do đặt điều kiện của if sai thứu tự,
# khi có điều kiện nhảy vào khoảng trên 100 sẽ không bao giờ nhảy 
# vào khoảng trên 120 được vì thứ thự thực hiện code từ trên xuống dưới
# Sửa:

print(" -- EMERGENCY TRIAGE SYSTEM --- ")
heart_rate = int(input("Enter patient's heart rate (bpm): "))

if heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")