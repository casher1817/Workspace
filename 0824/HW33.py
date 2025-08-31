time_str = input("請輸入時間 (HH:MM:SS):")
seconds = int(input("請輸入要增加的秒數:"))

def add_seconds(time_str, seconds):
  
    h, m, s = map(int, time_str.split(":"))
    total_seconds = h * 3600 + m * 60 + s

    total_seconds = (total_seconds + seconds) % (24 * 3600)
    
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

new_time = add_seconds(time_str, seconds)
print(new_time)
