import sys
import os
import subprocess

def replicate():
    # 1. Lấy đường dẫn và tên của file hiện tại đang chạy
    current_script = os.path.abspath(sys.argv[0])
    current_dir = os.path.dirname(current_script)
    current_name = os.path.basename(current_script)
    
    # 2. Đọc toàn bộ nội dung mã nguồn của chính nó
    with open(current_script, 'r', encoding='utf-8') as f:
        code_content = f.read()
        
    # 3. Tính toán số thứ tự cho thế hệ tiếp theo
    if "replica_" in current_name:
        try:
            # Tách chuỗi để lấy số thứ tự hiện tại
            current_num = int(current_name.split("replica_")[1].split(".py")[0])
            next_num = current_num + 1
        except ValueError:
            next_num = 1
    else:
        next_num = 1
        
    # 4. GIỚI HẠN AN TOÀN: Dừng lại khi đạt đến thế hệ thứ 5
    MAX_GENERATIONS = 10000000
    if next_num > MAX_GENERATIONS:
        print(f"[{current_name}] Đã đạt giới hạn an toàn ({MAX_GENERATIONS} thế hệ). Dừng lại.")
        return

    # 5. Tạo tên và đường dẫn cho file thế hệ tiếp theo
    next_name = f"replica_{next_num}.py"
    next_script_path = os.path.join(current_dir, next_name)
    
    # 6. Ghi nội dung mã nguồn vào file mới
    with open(next_script_path, 'w', encoding='utf-8') as f:
        f.write(code_content)
    print(f"[{current_name}] Đã tạo thành công: {next_name}")
    
    # 7. TỰ ĐỘNG KÍCH HOẠT: Gọi hệ điều hành chạy file mới vừa tạo
    # Sử dụng sys.executable để đảm bảo chạy đúng môi trường Python hiện tại
    subprocess.Popen([sys.executable, next_script_path])

if __name__ == "__main__":
    replicate()
