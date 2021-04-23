# coding: utf-8
from utg import relations as r
from utg import logic
from utg import data
from utg import dictionary
from utg import words
from utg import templates
from utg import constructors

# описываем существительное для словаря
coins_word = words.Word(type=r.WORD_TYPE.NOUN,
                        forms=[ u'монета', u'монеты', u'монете', u'монету', u'монетой', u'монете',    # единственнео число
                                u'монеты', u'монет', u'монетам', u'монеты', u'монетами', u'монетах',  # множественное число
                                u'монеты', u'монет', u'монетам', u'монеты', u'монетами', u'монетах'], # счётное число (заполнено для пример, может быть заполнено методом autofill_missed_forms)
                        properties=words.Properties(r.ANIMALITY.INANIMATE, r.GENDER.FEMININE)) # свойства: неодушевлённое, женский род

# описываем глагол для словаря
action_word = words.Word(type=r.WORD_TYPE.VERB,
                         # описываем только нужны нам формы слова (порядок важен и определён в utg.data.WORDS_CACHES[r.WORD_TYPE.VERB])
                         forms=[u'подарить', u'подарил', u'подарило', u'подарила', u'подарили'] + [u''] * (len(data.WORDS_CACHES[r.WORD_TYPE.VERB]) - 5),
                         properties=words.Properties(r.ASPECT.PERFECTIVE, r.VOICE.DIRECT) )
action_word.autofill_missed_forms() # заполняем пропущенные формы на основе введённых (выбираются наиболее близкие)

# создаём словарь для использования в шаблонах
test_dictionary = dictionary.Dictionary(words=[coins_word, action_word])


# описываем внешние переменные
hero = words.WordForm(words.Word(type=r.WORD_TYPE.NOUN,
                                 forms=[u'герой', u'героя', u'герою', u'героя', u'героем', u'герое',
                                        u'герои', u'героев', u'героям', u'героев', u'героями', u'героях',
                                        u'герои', u'героев', u'героям', u'героев', u'героями', u'героях'],
                                 properties=words.Properties(r.ANIMALITY.ANIMATE, r.GENDER.MASCULINE)))

npc = words.WordForm(words.Word(type=r.WORD_TYPE.NOUN,
                                forms=[u'русалка', u'русалки', u'русалке', u'русалку', u'русалкой', u'русалке',
                                       u'русалки', u'русалок', u'русалкам', u'русалок', u'русалками', u'русалках',
                                       u'русалки', u'русалок', u'русалкам', u'русалок', u'русалками', u'русалках'],
                                 properties=words.Properties(r.ANIMALITY.ANIMATE, r.GENDER.FEMININE)))

fairy = words.WordForm(words.Word(type=r.WORD_TYPE.NOUN,
                                forms=[u'фея', u'феи', u'фее', u'фею', u'феей', u'фее',
                                       u'феи', u'фей', u'феям', u'фей', u'феями', u'феях',
                                       u'феи', u'фей', u'феям', u'фей', u'феями', u'феях'],
                                 properties=words.Properties(r.ANIMALITY.ANIMATE, r.GENDER.FEMININE)))

eleph= words.WordForm(words.Word(type=r.WORD_TYPE.NOUN,
                                 forms=[u'слон', u'слона', u'слону', u'слона', u'слоном', u'слоне',
                                        u'слоны', u'слонов', u'слонам', u'слонов', u'слонами', u'слонах',
                                        u'слоны', u'слонов', u'слонам', u'слонов', u'слонами', u'слонах'],
                                 properties=words.Properties(r.ANIMALITY.ANIMATE, r.GENDER.MASCULINE)))

#создаем шаблон
template1 = templates.Template()
template2 = templates.Template()
template3 = templates.Template()
template1.parse(u'[fairy] [подарил|fairy] [hero|дт] [coins] [монета|coins|вн].', externals=('hero', 'fairy', 'coins'))
result1 = template1.substitute(externals={'hero': hero,
                                        'fairy': fairy,
                                        'coins': constructors.construct_integer(125)},
                             dictionary=test_dictionary)


template2.parse(u'[fairy] и [eleph] [подарил|мн] [hero|дт] [coins] [монета|coins|вн].', externals=('hero', 'eleph', 'fairy', 'coins'))
result2 = template2.substitute(externals={'hero': hero,
                                        'eleph': eleph,
                                        'fairy': fairy,
                                        'coins': constructors.construct_integer(125)},
                             dictionary=test_dictionary)

template3.parse(u'[fairy] и [eleph] [подарил|мн] [hero|дт] [coins] [монета|coins|вн].', externals=('hero', 'eleph', 'fairy', 'coins'))
result3 = template3.substitute(externals={'hero': hero,
                                        'eleph': eleph,
                                        'fairy': fairy,
                                        'coins': constructors.construct_integer(1)},
                             dictionary=test_dictionary)


result1 == u'Фея подарила герою 125 монет.'
print(result1)
result2 == u'фея и слон подарили герою 125 монет.'
print(result2)
result3 == u'фея и слон подарили герою 1 монету.'
print(result3)


