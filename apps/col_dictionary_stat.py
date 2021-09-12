from apps.utils import DICTIONARY_FILE
import yaml

if __name__ == '__main__':
    with open(DICTIONARY_FILE) as f:
        content = f.read()

    words = yaml.safe_load(content)
    n_words = len(words)
    print('Head words:', len(words))
    n_descriptions = 0
    n_examples = 0
    for word in words:
        for sense in words[word]:
            if "description" in sense:
                n_descriptions += 1
            if "examples" in sense:
                n_examples += len(sense["examples"])
    print("Descriptions:", n_descriptions)
    print("Examples:", n_examples)
