from transformers import T5Tokenizer, AutoModelForCausalLM
# T5Tokenizer AutoTokenizer
# トークナイザーとモデルの準備
tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium")
model = AutoModelForCausalLM.from_pretrained("finetuned model path")

# 推論
ques = input('ご案内内容を入力してください：')
input = tokenizer.encode(ques, return_tensors="pt")
output = model.generate(input, do_sample=True, max_length=250, num_return_sequences=5)
print(tokenizer.batch_decode(output))


# Thanks to  GPT-2 model provided by Rinna 