from llama_cpp import Llama

model_path = "llama-2-7b.Q4_K_M.gguf"

llm = Llama(model_path=model_path)

prompt = "What is the tallest mountain in Japan?"

answer = llm(prompt=prompt)

print(answer)
