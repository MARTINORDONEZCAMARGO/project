# import the nltk library   
import nltk

#desde nltk descargar el paquete de stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')

lista_stopwords = stopwords.words('english')

#imprimir la lista de stopwords
print(lista_stopwords)
