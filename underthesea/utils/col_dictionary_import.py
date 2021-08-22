from os.path import dirname, join

from underthesea.utils.col_dictionary import Dictionary

PROJECT_FOLDER = dirname(dirname(dirname(__file__)))
DATASETS_FOLDER = join(PROJECT_FOLDER, "datasets")
COL_FOLDER = join(DATASETS_FOLDER, "UD_Vietnamese-COL")
DICTIONARY_FOLDER = join(DATASETS_FOLDER, "UD_Vietnamese-COL", "dictionary")
DICTIONARY_FILE = join(DICTIONARY_FOLDER, "202108.yaml")

if __name__ == '__main__':
    dictionary = Dictionary.load(DICTIONARY_FILE)
    dictionary.describe()
    dictionary.import_words(join(DICTIONARY_FOLDER, "words_noun_candidate.xlsx"))
    dictionary.describe()
    dictionary.save(join(DICTIONARY_FOLDER, "202108_1.yaml"))
