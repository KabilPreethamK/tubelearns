import spacy

def main():
    spacy.cli.download("en_core_web_sm")

if __name__ == "__main__":
    main()