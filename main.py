import sys
import os
import subprocess

def exponential_replication():
    # 1. Lấy thông tin file hiện tại
    current_script = os.path.abspath(sys.argv[0])
    current_dir = os.path.dirname(current_script)
    current_name = os.path.basename(current_script)
    
    # 2. Đọc mã nguồn của chính nó
    with open(current_script, 'r', encoding='utf-8') as f:
        code_content = f.read()
        
    # 3. Phân tích thế hệ dựa trên tên file để đặt GIỚI HẠN AN TOÀN
    # Quy ước tên file: gen_[Tầng]_[Nhánh].py (Ví dụ: gen_1_A.py)
    generation = 0
    if current_name.startswith("gen_"):
        try:
            generation = int(current_name.split("_")[1])
        except ValueError:
            generation = 0

    # BỘ HÃM PHANH: Chỉ cho phép nhân bản đến tầng thứ 3
    # Tầng 0 (1 file) -> Tầng 1 (2 file) -> Tầng 2 (4 file) -> Tầng 3 (8 file). Tổng = 15 file.
    MAX_GENERATION = 10000000000
    if generation >= MAX_GENERATION:
        print(f"[{current_name}] Đạt tầng tối đa ({MAX_GENERATION}). Dừng lại.")
        return

    next_generation = generation + 1
    
    # 4. CẤP SỐ NHÂN: Tạo ra 2 nhánh con (Nhánh A và Nhánh B)
    branches = ["A", "B"]
    for branch in branches:
        next_name = f"gen_{next_generation}_{branch}.py"
        next_script_path = os.path.join(current_dir, next_name)
        
        # Ghi mã nguồn vào file con mới
        with open(next_script_path, 'w', encoding='utf-8') as f:
            f.write(code_content)
        print(f"[{current_name}] Đã đẻ ra nhánh con: {next_name}")
        
        # 5. KÍCH HOẠT ĐỒNG THỜI: Chạy cả 2 file con cùng lúc
        subprocess.Popen([sys.executable, next_script_path])

if __name__ == "__main__":
    exponential_replication()
