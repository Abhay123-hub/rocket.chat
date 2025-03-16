from datasets import load_dataset

# Load dataset
ds = load_dataset("dnouv/rocketchat_qna_metadata", split="train")

# Define output file
output_file = "rocketchat_qna.txt"

# Write data to .txt file
with open(output_file, "w", encoding="utf-8") as f:
    for row in ds:
        f.write(f"Question: {row['question']}\n")
        f.write(f"Answer: {row['answer']}\n")
        f.write(f"Source: {row['source']}\n")
        f.write(f"Category: {row['category']}\n")
        f.write("-" * 50 + "\n")  # Separator for readability

print(f"Dataset saved to {output_file}")