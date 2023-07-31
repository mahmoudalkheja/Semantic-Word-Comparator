import re
import math


def read_reference_text(filename: str) -> list[list[str]]:
    """
    :param filename: a txt file
    :return: a list contains lists for each line from the txt in lower letter,using the split condition.

    """
    f = open(filename, "r")
    list1 = [re.split("[ .,;:\’\"\?!]+", line.lower().strip()) for line in f]
    f.close()
    return list1


def make_word_vector(w: str, txt: list[list[str]]) -> dict[str, int]:
    """
    :param w: string word
    :param txt: list contains lists of strings
    :return: dictionary of vectors where the W occurs not including the stopwords
    """
    vector = dict()
    stopwords = set(
        ["s", "a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost",
         "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount",
         "an", "and", "another", "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are", "around", "as",
         "at", "back", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand",
         "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom", "but", "by",
         "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do",
         "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven", "else", "elsewhere", "empty",
         "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen",
         "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from",
         "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here",
         "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however",
         "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last",
         "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill",
         "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely",
         "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing",
         "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others",
         "otherwise", "our", "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps", "please", "put",
         "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should",
         "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something",
         "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their",
         "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon",
         "these", "they", "thick", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru",
         "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until",
         "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence",
         "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether",
         "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within",
         "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"])
    for line in txt:
        if w in line:
            for word in line:
                if len(word) >= 3 and word not in stopwords and w != word:
                    if word not in vector:
                        vector[word] = 1
                    else:
                        vector[word] += 1
    return vector


def product(v1: dict[str, int], v2: dict[str, int]) -> float:
    """
    :param v1: dictionary of vectors where the word 1 occurs
    :param v2: dictionary of vectors where the word 1 occurs
    :return: float number of scalar product of two vectors
    """
    sp = 0.0
    for word in v1:
        sp += v1[word] * v2.get(word, 0)  # word not in v2  → 0
    return sp


def sim_word_vec(v1: dict[str, int], v2: dict[str, int]) -> float:
    """
    :param v1: dictionary of vectors  where the word 1 occurs
    :param v2: dictionary of vectors  where the word 2 occurs
    :return: float number the cosine similarity of two words
    """
    return product(v1, v2) / math.sqrt(product(v1, v1) * product(v2, v2))


def main():
    f = read_reference_text("ref-sentences.txt")
    words_try = ["spain", "anchovy", "france", "internet", "china", "mexico", "fish", "industry", "agriculture",
                 "fishery", "tuna", "transport", "italy", "web", "communication", "labour", "fish", "cod"]

    for word in words_try:
        similarity = 0
        same_word = None
        for other_word in words_try:
            if word != other_word:
                current_similarity = sim_word_vec(make_word_vector(word, f), make_word_vector(other_word, f))
                if similarity < current_similarity:
                    similarity = current_similarity
                    same_word = other_word
        print(word, "->", same_word, similarity)

if __name__ == '__main__':
    main()
