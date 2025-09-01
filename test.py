import ollama
import time

image_path = "esp32-devkitC-v4-pinout.png"
query = "Describe the contents of this image in 100 words."

start_time = time.time()

response = ollama.chat(
    model="qwen2.5vl:3b",
    messages=[
        {
            "role": "user",
            "content": query,
            "images": [image_path],
        }
    ]
)

end_time = time.time()

print("Model Output:\n", response["message"]["content"])
print("\nGeneration Time: {:.2f} seconds".format(end_time - start_time))
