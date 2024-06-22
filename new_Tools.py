import re




# Enter the API of your OpenAI account here
api_key = ""




def get_chatgpt_request(content):
    import requests

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": content}],
        "temperature": 0.7
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()


def get_hypernyms(word):

    import nltk
    from nltk.corpus import wordnet
    nltk.download('wordnet')

    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())

    hypernyms = []
    for syn in wordnet.synsets(word):
        for hypernym in syn.hypernyms():
            hypernyms.append(hypernym.lemmas()[0].name())

    print("Synonyms:", synonyms)
    print("Hypernyms:", hypernyms)
def get_synonyms_and_hyper(word):

    from nltk.corpus import wordnet

    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())

    synonyms = list(set(synonyms))
    synonyms_ed = [synset.split('.')[0] for synset in synonyms]

    hypernyms = []
    for syn in wordnet.synsets(word):
        for hypernym in syn.hypernyms():
            hypernyms.append(hypernym.lemmas()[0].name())
    hypernyms = list(set(hypernyms))

    return synonyms_ed, hypernyms
def cal_similarity(word_to_classify, wordnet):

    # Define a list of topic categories
    TOPICS = "Animals,Body,Botany,Boundary,Chess,Color,Combustion,Cooking,Courtship,Cut,force,Drug,Electricity,Energy,Entry,Fishing,Flight,Gambling,Grasp,Health,Height,Light,Liquid,Machine,Maritime,Money,Motion,Mythology,Disasters,Nuclear,Odor,Plants,Race,Religion,Sick,Size,Sound,Sports,Taste,Temperature,Texture,Theater,Time,Toxicity,Vehicle,War,Weaponry,Weather,Family,Pathways,Weight,Farming,structure,Fight,Planning"
    theme_categories = TOPICS.split(",")

    # Used to store subordinate words for each topic category
    theme_hyponyms = {}

    # Get the subordinate words of the topic category
    for category in theme_categories:
        synsets = wordnet.synsets(category)
        hyponyms = set()
        for synset in synsets:
            hyponyms.update(synset.hyponyms())
        theme_hyponyms[category] = hyponyms

    # Initialize the highest similarity and corresponding topic categories
    top_3_sim = [-1, -1, -1]
    top_3_name = ["none", "none", "none"]

    # Find synonym sets for the vocabulary to be tested
    word_synsets = wordnet.synsets(word_to_classify)

    # Calculate the similarity between the tested vocabulary and the subordinate words of each topic category
    for category, hyponyms in theme_hyponyms.items():
        for synset in word_synsets:
            for hyponym in hyponyms:
                similarity = synset.wup_similarity(hyponym)
                if not similarity:
                    continue
                if similarity > top_3_sim[0]:
                    top_3_sim[0] = similarity
                    top_3_name[0] = category
                elif similarity < top_3_sim[0] and similarity > top_3_sim[1]:
                    top_3_sim[1] = similarity
                    top_3_name[1] = category
                elif similarity < top_3_sim[1] and similarity > top_3_sim[2]:
                    top_3_sim[2] = similarity
                    top_3_name[2] = category

    # Assign the tested vocabulary to the topic category with the highest similarity to it
    print(f"The word '{word_to_classify}' belongs to the category: {top_3_name} and in {top_3_sim}")

    new_top_3_name = []
    for t3n in top_3_name:
        if t3n not in new_top_3_name:
            new_top_3_name.append(t3n)

    return new_top_3_name


def plural_to_singular(word):

    import inflect
    p = inflect.engine()
    singular = p.singular_noun(word)
    if singular:
        return singular
    else:
        return word
def if_people_pronoun(text):
    if text == "I" or text == "me" or text.lower() == "we" \
            or text.lower() == "you" or text.lower() == "yours" \
            or text == "us" or text == "ours" or text.lower() == "she" \
            or text.lower() == "he" or text.lower() == "him" or text.lower() == "hers"\
            or text == "Mr." or text == "Ms.":
        return True
    else:
        return False
def pronoun_replace(source_file, target_file):

    import csv

    ff = open(source_file, "r")
    fff = open(target_file, "w", newline="")

    cr = csv.reader(ff)
    cw = csv.writer(fff)

    for row in cr:

        assert len(eval(row[5])) == 4
        old_svo_sub = eval(row[5])[0]
        old_svo_ob = eval(row[5])[1]
        old_svo_adv = eval(row[5])[2]
        old_svo_pro = eval(row[5])[3]

        new_svo = []

        if isinstance(old_svo_sub, list):
            new_svo_sub = []
            for oss in old_svo_sub:
                if oss.lower() == "he" or oss.lower() == "she" or oss == "I" or oss.lower() == "we" or oss.lower() == "him" or oss.lower() == "her" or oss.lower() == "you":
                    new_svo_sub.append("people")
                else:
                    new_svo_sub.append(oss)
        else:
            if old_svo_sub.lower() == "he" or old_svo_sub.lower() == "she" or old_svo_sub == "I" or old_svo_sub.lower() == "we" or old_svo_sub.lower() == "him" or old_svo_sub.lower() == "her" or old_svo_sub.lower() == "you":
                new_svo_sub = "people"
            else:
                new_svo_sub = old_svo_sub


        if isinstance(old_svo_ob, list):
            new_svo_ob = []
            for oso in old_svo_ob:
                if oso.lower() == "he" or oso.lower() == "she" or oso == "I" or oso.lower() == "we" or oso.lower() == "him" or oso.lower() == "her" or oso.lower() == "you":
                    new_svo_ob.append("people")
                else:
                    new_svo_ob.append(oso)
        else:
            if old_svo_ob.lower() == "he" or old_svo_ob.lower() == "she" or old_svo_ob == "I" or old_svo_ob.lower() == "we" or old_svo_ob.lower() == "him" or old_svo_ob.lower() == "her" or old_svo_ob.lower() == "you":
                new_svo_ob = "people"
            else:
                new_svo_ob = old_svo_ob

        new_svo.append(new_svo_sub)
        new_svo.append(new_svo_ob)
        new_svo.append(old_svo_adv)
        new_svo.append(old_svo_pro)

        cw.writerow([row[0], row[1], row[2], row[3], row[4], new_svo, row[6]])
def SVO_not_none(tag_list):

    if isinstance(tag_list, list):
        for tl in tag_list:
            if tl and tl != "none" and tl != "-":
                return True
        return False
    else:
        if tag_list and tag_list != "none" and tag_list != "-":
            return True
        else:
            return False
def word_deel(text):
    # Delete stop words

    custom_stopwords = ["the", "this", "that", "these", "a", "an"]
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in custom_stopwords]
    filtered_text = " ".join(filtered_words)
    return filtered_text
def remove_csv_stopword(source_file, target_file):
    import csv

    with open(source_file, 'r', newline='') as source_csv, \
            open(target_file, 'w', newline='') as new_csv:
        csv_reader = csv.reader(source_csv)
        csv_writer = csv.writer(new_csv)

        for i, row in enumerate(csv_reader):
            index = row[3]
            verb = row[1]
            sent = row[2]
            label = row[4]
            text = eval(row[5])

            new_text = []
            for t in text:
                if t == "none":
                    new_text.append(t)
                else:
                    new_text.append(word_deel(t))

            print(i, verb, sent, index, label, new_text)
            csv_writer.writerow([i, verb, sent, index, label, new_text])


def get_first_noun(text):

    from nltk.tokenize import word_tokenize
    from nltk import pos_tag

    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    # print("pos_tag:", pos_tags)
    if pos_tags:
        pos_s = pos_tags[0][0]
    else:
        pos_s = ""
    for pt in pos_tags:
        if pt[1] == "NN" or pt[1] == "NNP" or pt[1] == "NNS" or pt[1] == "NNPS":
            pos_s = pt[0]
            break
    return pos_s
def get_top_k_noun(k, text):

    from nltk.tokenize import word_tokenize
    from nltk import pos_tag

    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    # print("pos_tag:", pos_tags)
    pos_s = []

    pos_k = 0
    for pt in pos_tags:
        if pt[1] == "NN" or pt[1] == "NNP" or pt[1] == "NNS" or pt[1] == "NNPS":
            pos_s.append(pt[0])
            pos_k += 1
            if pos_k >= k:
                break

    if not pos_s and pos_tags:
        pos_s = [pos_tags[0][0]]

    return pos_s
def get_top_k_content(k, lists):

    if isinstance(lists, list):
        lists = list(set(lists))
        new_list = []
        for i, l in enumerate(lists):
            if i >= k:
                break
            if if_people_pronoun(l):
                new_list.append("people")
                continue
            if l.lower() == "it" or l.lower() == "its" or l.lower() == "they" or l.lower() == "theirs" \
                    or l.lower == "who" or l.lower == "which" or l.lower == "this" or l.lower() == "that":
                new_list.append("none")
            else:
                new_list.append(l)
    else:
        if if_people_pronoun(lists):
            lists = "people"
        if lists.lower() == "it" or lists.lower() == "its" or lists.lower() == "they" or lists.lower() == "theirs" \
                or lists.lower == "who" or lists.lower == "which" or lists.lower == "this" or lists.lower() == "that":
            lists = "none"
        new_list = [lists]
    return new_list
def get_top_k_in_double_list(k, d_list):

    if not d_list:
        final_list = ["none"]
    else:
        final_list = []
        new_list = []
        for l in d_list:
            if isinstance(l, list):
                new_list += l
            else:
                if l.lower() == "it" or l.lower() == "its" or l.lower() == "they" or l.lower() == "theirs" \
                        or l.lower == "who" or l.lower == "which" or l.lower == "this" or l.lower() == "that"\
                        or l.lower() == "a":
                    new_list.append("none")
                else:
                    new_list.append(l)

        for i, l in enumerate(new_list):
            if i >= k:
                break
            final_list.append(l)
    return final_list
def get_top_k_in_double_list2(k, d_list):

    if not d_list:
        final_list = ["none"]
    else:
        final_list = []
        new_list = []
        for l in d_list:
            if isinstance(l, list) and l[0] != "none":
                new_list.append(l[0])
            elif l != "none":
                new_list.append(l)

        for i, l in enumerate(new_list):
            if i >= k:
                break
            final_list.append(l)
    return final_list


def list1_if_in_list2(list1, list2):
    for l1 in list1:
        for l2 in list2:
            if l1 in l2:
                return True
    return False
def list1_if_in_list22(list1, list2):
    for l1 in list1:
        if l1 in list2:
            return True
            break
    return False




def get_verb_dir(TOP_K, file):

    import csv
    f2 = open(file, "r", errors="ignore")
    cr2 = csv.reader(f2)

    verb_sub_dir = {}
    verb_ob_dir = {}

    List_TOP_k = 2
    for c2 in cr2:

        verb = c2[1]
        subs = eval(c2[2])
        obs = eval(c2[3])

        new_subs = []
        for ll, sub in enumerate(subs):
            if ll >= TOP_K:
                break
            sub = get_top_k_content(List_TOP_k, sub)
            new_subs += sub

        new_obs = []
        for ll, ob in enumerate(obs):
            if ll >= TOP_K:
                break
            ob = get_top_k_content(List_TOP_k, ob)
            new_obs += ob

        verb_sub_dir[verb] = new_subs
        verb_ob_dir[verb] = new_obs

    return verb_sub_dir, verb_ob_dir
def get_verb_dir_total(TOP_K, file):

    import csv
    f2 = open(file, "r")
    cr2 = csv.reader(f2)

    verb_sub_dir = {}
    verb_ob_dir = {}

    List_TOP_k = 1000

    for c2 in cr2:

        verb = c2[1]
        subs = eval(c2[2])
        obs = eval(c2[3])

        new_subs = []
        for ll, sub in enumerate(subs):
            if ll >= TOP_K:
                break
            sub = get_top_k_content(List_TOP_k, sub)
            new_subs += sub

        new_obs = []
        for ll, ob in enumerate(obs):
            if ll >= TOP_K:
                break
            ob = get_top_k_content(List_TOP_k, ob)
            new_obs += ob

        verb_sub_dir[verb] = new_subs
        verb_ob_dir[verb] = new_obs
    return verb_sub_dir, verb_ob_dir








def svo_to_topic(NOUN_TOP_K, svo_sent):

    pos_s = get_top_k_noun(NOUN_TOP_K, svo_sent)
    new_s = []
    for ss in pos_s:
        if if_people_pronoun(ss):
            new_s.append("people")
        else:
            new_s.append(ss)

    ns_list = []
    for ns in new_s:
        if ns and ns != "people" and ns != "none" and ns != "-":
            INDEX = 0
            hyper_list = []
            while(True):
                INDEX += 1
                if INDEX > 50:
                    break
                print("request the", INDEX)
                try:
                    hyper_list = get_topic_from_oxford_dir(ns)
                    break
                except:
                    print("request error and try again")
            if hyper_list:
                print("hyper exist:", ns, "->", hyper_list)
                ns_list.append(hyper_list)
            else:
                print("hyper is none:", ns, "->", ns)
                ns_list.append(ns)
        else:
            ns_list.append(ns)
    return ns_list
def get_topic_from_oxford_dir(word):

    import requests
    from bs4 import BeautifulSoup

    url = "https://www.oxfordlearnersdictionaries.com/"
    final_url = url + "search/english/?q=" + word
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    response = requests.get(final_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        topic_elements = soup.find_all('span', class_='topic_name')
        topics = [element.get_text() for element in topic_elements]
        print("topic info：", topics)
        return topics
    else:
        print("Request failed with status code:", response.status_code)
        return []
def get_basic_sense_from_oxford_dir(word):

    import requests
    from bs4 import BeautifulSoup

    url = "https://www.oxfordlearnersdictionaries.com/"
    final_url = url + "search/english/?q=" + word

    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }

    response = requests.get(final_url, headers=headers)
    result = ""
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        sense_li_tags = soup.find_all('li', class_='sense')
        if sense_li_tags:
            for sense_li in sense_li_tags:
                span_tag = sense_li.find('span', class_='def', htag='span')
                if span_tag:
                    result = span_tag.get_text()
                    break
    else:
        print("error")
    return result
def convert_old_by_add_basic_sense_and_oxford_topic(TOP_K, old_list):
    import time

    new_list = []
    for kk, s in enumerate(old_list):
        if isinstance(s, list):
            new_list.append(s)
            continue
        else:
            nonetype_pair = s.split("&")
            if len(nonetype_pair) == 2 and nonetype_pair[0] == "none":
                nonetype_s = nonetype_pair[1]
                INDEX = 0
                max_loop = 50
                while (True):
                    INDEX += 1
                    if INDEX > max_loop:
                        break
                    print("basic sense request and the ", INDEX, "begin")
                    try:
                        basic_sense = get_basic_sense_from_oxford_dir(nonetype_s)
                        break
                    except:
                        print("request error and try again")
                        time.sleep(3)

                print("get nonetype basic sense:", nonetype_s, "->", basic_sense)

                if basic_sense:
                    basic_k_noun = get_top_k_noun(TOP_K, basic_sense)
                else:
                    basic_k_noun = []
                print("get top k noun:", basic_sense, "->", basic_k_noun)

                if basic_k_noun:
                    bkn_list = []
                    for bkn in basic_k_noun:
                        bkn = plural_to_singular(bkn)
                        if bkn.lower() == "person":
                            bkn = "people"
                        if bkn and bkn != "people" and bkn != "none" and bkn != "-":
                            INDEX = 0
                            typer_list = []
                            while (True):
                                INDEX += 1
                                if INDEX > 50:
                                    break
                                print("topic request and the ", INDEX, "begin")
                                try:
                                    typer_list = get_topic_from_oxford_dir(bkn)
                                    break
                                except:
                                    print("request error and try again")
                                    time.sleep(3)
                            if typer_list:
                                print("hyper exist:", bkn, "->", typer_list)
                                if len(typer_list) > 2:
                                    bkn_list += typer_list[:2]
                                else:
                                    bkn_list += typer_list
                            else:
                                print("hyper is none:", bkn, "->", "none2&" + bkn)
                                bkn_list += ["none2&" + bkn]
                        else:
                            bkn_list += [bkn]

                    new_list.append(bkn_list)
                    print("basic_k_noun->bkn_list:", basic_k_noun, "->", bkn_list)

            elif s != "none":
                new_list.append(s)
            else:
                print("not need to add to new_sub_list:", s)
    return new_list