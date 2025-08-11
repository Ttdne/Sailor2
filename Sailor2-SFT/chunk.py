import os

# Cấu hình
input_path = "Sailor2-SFT\model.safetensors"
output_dir = "Sailor2-SFT\split_parts"
chunk_size = 90 * 1024 * 1024  # 90MB

# Đảm bảo thư mục output tồn tại
os.makedirs(output_dir, exist_ok=True)

with open(input_path, "rb") as in_f:
    i = 0
    while True:
        chunk = in_f.read(chunk_size)
        if not chunk:
            break
        
        out_path = os.path.join(output_dir, f"model.safetensors.part{i:03}")
        with open(out_path, "wb") as out_f:
            out_f.write(chunk)
        
        print(f"✅ Wrote: {out_path} ({len(chunk)/1024/1024:.2f} MB)")
        i += 1
