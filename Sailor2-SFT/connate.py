total_chunk = 21
with open("model.safetensors", "wb") as out_f:
    for i in range(total_chunk):
        print(i)
        part_path = f"Sailor2-SFT/split_parts/model.safetensors.part{i:03}"
        with open(part_path, "rb") as part_f:
            out_f.write(part_f.read())