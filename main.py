import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pylab

d = {}
punctuation = ['“', '"', "'", ')', '(', ':', ';', '.', ',', '!', '?', '—', '’', '‘', '”', '-', '„', '[', ']', ' ', '…', '»', '«', '⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '{', '}']
fileIn = open("1984.txt", 'rb')
words_list = fileIn.read().split()
words_list_lower = []
words_list_lower_corrected = []
word_array = []
word1 = ''
count = 1
counter = 0
first10 = 0
first25 = 0
first50 = 0
first100 = 0
hapaxCount = 0

for word in words_list:
    words_list_lower.append(word.decode('utf8').lower())

# Кодировки: utf8, cp1251, latin-1, utf16, utf32, koi8-r

for word in words_list_lower:
    word_array = []
    for letter in list(str(word)):
        if letter not in punctuation:
            word_array.append(letter)
    word1 = ''.join(word_array)
    words_list_lower_corrected.append(word1)


for word in words_list_lower_corrected:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

listY = []
listYLim = []
reference = ''
print("Rank | Word | Number of appearances | Ziph's prediction")
for i in sorted(d.items(), key=lambda x: (-x[1], x[0])):
    if count == 1:
        reference = ' '.join(words_list_lower_corrected).count(' ' + i[0] + ' ')
    print(str(count) + '.', i[0], ' '.join(words_list_lower_corrected).count(' ' + i[0] + ' '), round(reference/count))
    if count <= 300:
        listYLim.append(' '.join(words_list_lower_corrected).count(' ' + i[0] + ' '))
    listY.append(' '.join(words_list_lower_corrected).count(' ' + i[0] + ' '))
    count += 1
    counter += ' '.join(words_list_lower_corrected).count(' ' + i[0] + ' ')
    if count <= 10:
        first10 += ' '.join(words_list_lower_corrected).count(' ' + i[0] + ' ')
        first25 += ' '.join(words_list_lower_corrected).count(' ' + i[0] + ' ')
        first50 += ' '.join(words_list_lower_corrected).count(' ' + i[0] + ' ')
        first100 += ' '.join(words_list_lower_corrected).count(' ' + i[0] + ' ')
    elif count <= 25:
        first25 += ' '.join(words_list_lower_corrected).count(' ' + i[0] + ' ')
        first50 += ' '.join(words_list_lower_corrected).count(' ' + i[0] + ' ')
        first100 += ' '.join(words_list_lower_corrected).count(' ' + i[0] + ' ')
    elif count <= 50:
        first50 += ' '.join(words_list_lower_corrected).count(' ' + i[0] + ' ')
        first100 += ' '.join(words_list_lower_corrected).count(' ' + i[0] + ' ')
    elif count <= 100:
        first100 += ' '.join(words_list_lower_corrected).count(' ' + i[0] + ' ')
    if ' '.join(words_list_lower_corrected).count(' ' + i[0] + ' ') == 1:
        hapaxCount += 1

print('\n---------------------------------------\n')
print('\nВсего в тексте', counter, 'слов\n')

print('Анализ частотности:')
print('Первые 10 слов составляют', str(round(first10/counter, 4)*100) + '% текста')
print('Первые 25 слов составляют', str(round(first25/counter, 4)*100) + '% текста')
print('Первые 50 слов составляют', str(round(first50/counter, 4)*100) + '% текста')
print('Первые 100 слов составляют', str(round(first100/counter, 4)*100) + '% текста\n')

print('В тексте', hapaxCount, 'Гапаксов, это', round(hapaxCount/count, 4)*100, '% от всех ' + str(count) + ' используемых слов в тексте')

listX = []
listXLim = []
for num in range(1, count):
    listX.append(num)
for num in range(1, 301):
    listXLim.append(num)

#print(listX)
#print(listY)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(listX, listY)
fig1.canvas.manager.set_window_title('ВсеЛин')

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(listX, listY)
fig2.canvas.manager.set_window_title('ВсеЛог')

fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
ax3.plot(listXLim, listYLim)
fig3.canvas.manager.set_window_title('300Лин')

fig4 = plt.figure()
ax4 = fig4.add_subplot(111)
ax4.plot(listXLim, listYLim)
fig4.canvas.manager.set_window_title('300Лог')

ax2.set_xscale('log')
ax2.set_yscale('log')
ax4.set_xscale('log')
ax4.set_yscale('log')

title = '1984'

ax1.set_title(f"{title} (All words, linear graph)")
ax1.set_xlabel('Кол-во использований')
ax1.set_ylabel('Ранг по частоте')
ax2.set_title(f"{title} (All words, log-log graph)")
ax2.set_xlabel('Кол-во использований')
ax2.set_ylabel('Ранг по частоте')
ax3.set_title(f"{title} (First 300, linear graph)")
ax3.set_xlabel('Кол-во использований')
ax3.set_ylabel('Ранг по частоте')
ax4.set_title(f"{title} (First 300, log-log graph)")
ax4.set_xlabel('Кол-во использований')
ax4.set_ylabel('Ранг по частоте')
pylab.show()
