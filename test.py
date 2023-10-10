from tubelearns import Tokenization

with open("./raw_data/raw_data_1.txt","r") as f:
    content = f.read()
x = Tokenization()
x_Value = x.tokenize_rawlower(content)
punc = x.punct_raw(x_Value)
print(x_Value)