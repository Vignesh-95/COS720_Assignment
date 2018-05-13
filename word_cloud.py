import os, email
import numpy
import pandas
import matplotlib.pyplot as matplot
import seaborn
import wordcloud
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from PIL import Image

seaborn.set_style('whitegrid')

emails_df = pandas.read_csv('./input/emails.csv')
emails_df.head()


# Get fields from parsed email objects
messages = list(map(email.message_from_string, emails_df['message']))
emails_df.drop('message', axis=1, inplace=True)
keys = messages[0].keys()
for key in keys:
    emails_df[key] = [doc[key] for doc in messages]

# Set index and drop columns with two few values
emails_df = emails_df.set_index('Message-ID') \
    .drop(['file', 'Mime-Version', 'Content-Type', 'Content-Transfer-Encoding'], axis=1)

subjects = ' '.join(emails_df['Subject'])

text_file = open("Output.txt", "w")
text_file.write(subjects)
text_file.close()

text_file = open("Output.txt", "r")
subjects = text_file.read()
text_file.close()

fig, ax = matplot.subplots(figsize=(16, 12))

d = os.path.dirname(__file__)
enron_coloring = numpy.array(Image.open(os.path.join(d, "enron_logo.jpg")))

wc = wordcloud.WordCloud(background_color="white", max_words=1000, mask=enron_coloring,
               stopwords=ENGLISH_STOP_WORDS, max_font_size=40, random_state=42)

wc.generate(subjects)

# create coloring from image
image_colors = wordcloud.ImageColorGenerator(enron_coloring)

wc.to_file(os.path.join(d, "enron.png"))

# show
ax.imshow(wc, interpolation="bilinear")
ax.axis("off")
ax.figure()
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
ax.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
ax.axis("off")
ax.figure()
ax.imshow(enron_coloring, cmap=matplot.cm.gray, interpolation="bilinear")
ax.axis("off")
ax.show()