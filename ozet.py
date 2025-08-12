from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from wordcloud import WordCloud
from matplotlib import pyplot as plt


def summarization (text,count):
  sentences = sent_tokenize(text, language='turkish')
  words = word_tokenize(text)
  stop_words = set(stopwords.words('turkish'))
  words = [word.lower() for word in words if word.isalpha()]
  words = [word for word in words if word not in stop_words]
  lemmatizer = WordNetLemmatizer()

  words = [lemmatizer.lemmatize(word) for word in words]

  freq_dist = FreqDist(words)

  sentence_scores = {}

  for i, sentence in enumerate(sentences):
    sentence_words = word_tokenize(sentence.lower())
    sentence_score = sum([freq_dist[word] for word in sentence_words if word in freq_dist])

    sentence_scores[i] = sentence_score

  sorted_scores = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
  selected_sentences = sorted_scores[:count]
  selected_sentences = sorted(selected_sentences)


  summary = ' '.join([sentences[i] for i, _ in selected_sentences])
  return summary

if __name__ == '__main__':
  text = '''
  Şu tarlaya bir şinik kekere mekere ekmişler.

  Bu tarlaya da bir şinik kekere mekere ekmişler.

  Şu tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlıklı pis porsuk,

  bu tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlıklı pis porsuğa demiş ki;

  "ben bu tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlıklı pis porsuğum" demiş.

  Öteki tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlıklı pis porsukta;

  ben de; "bu tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlıklı pis porsuğum" demiş.
          '''
  print(summarization (text,1))