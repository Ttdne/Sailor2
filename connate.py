total_chunk = 37
with open("reconstructed.safetensors", "wb") as out_f:
    for i in range(total_chunk):
        print(i)
        part_path = f"split_parts/model-00001-of-00002.safetensors.part{i:03}"
        with open(part_path, "rb") as part_f:
            out_f.write(part_f.read())