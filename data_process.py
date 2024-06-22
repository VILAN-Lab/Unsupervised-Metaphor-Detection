import re
import time
from new_Tools import *





def get_MOX_unique_verb_file(source_file, target_file):
    import csv
    from nltk.stem import WordNetLemmatizer
    from nltk.tokenize import word_tokenize

    lemmatizer = WordNetLemmatizer()
    unique_words = set()

    ff = open(target_file, "w")
    with open(source_file, "r", newline="") as file:
        csv_reader = csv.reader(file, delimiter="\t")
        for row in csv_reader:
            if row:
                text = row[1]
                words = word_tokenize(text)
                for word in words:
                    lemma = lemmatizer.lemmatize(word.lower(), pos="v")
                    unique_words.add(lemma)

    print(len(list(unique_words)), list(unique_words))
    ff.write(str(list(unique_words)))
def get_TroFi_unique_verb_file(source_file, target_file):
    import csv
    from nltk.stem import WordNetLemmatizer
    from nltk.tokenize import word_tokenize

    lemmatizer = WordNetLemmatizer()

    unique_words = set()
    out = open(target_file, "w")

    with open(source_file, "r", newline="") as file:
        csv_reader = csv.reader(file, delimiter="\t")
        for row in csv_reader:
            if row:
                text = row[1]
                words = word_tokenize(text)
                for word in words:
                    lemma = lemmatizer.lemmatize(word.lower(), pos="v")
                    unique_words.add(lemma)
    print(list(unique_words))
    out.write(str(list(unique_words)))
def get_VUAverb_unique_verb_file(source_file, target_file):
    import csv
    import nltk
    from nltk.stem import WordNetLemmatizer
    nltk.download('wordnet')
    lemmatizer = WordNetLemmatizer()

    f = open(source_file, "r")
    cr = csv.reader(f, delimiter="\t")
    ff = open(target_file, "w")

    verb_list = []
    for row in cr:
        verb = row[4]
        verb = lemmatizer.lemmatize(verb.lower(), pos='v')
        verb_list.append(verb)

    verb_list = list(set(verb_list))
    print(len(verb_list), verb_list)
    ff.write(str(verb_list))


def get_MOH_unique_verb_file(source_file, target_file):
    import csv
    import nltk
    from nltk.stem import WordNetLemmatizer
    nltk.download('wordnet')
    lemmatizer = WordNetLemmatizer()

    f = open(source_file, "r")
    cr = csv.reader(f)
    ff = open(target_file, "w")

    verb_list = []
    for row in cr:
        verb = row[0]
        verb = lemmatizer.lemmatize(verb.lower(), pos='v')
        verb_list.append(verb)

    verb_list = list(set(verb_list))
    print(len(verb_list), verb_list)
    ff.write(str(verb_list))



# chatgpt direct predict
def Add_TroFi_label_by_Chatgpt_Api(source_tsv_file, target_file):
    import csv
    import time

    start = -1
    end = 10000

    with open(source_tsv_file, 'r', newline='') as source_csv, \
            open(target_file, 'w', newline='') as new_csv:

        csv_reader = csv.reader(source_csv, delimiter="\t")
        csv_writer = csv.writer(new_csv)

        for i, row in enumerate(csv_reader):

            if i <= start:
                continue
            if i > end:
                break

            index = row[0]
            verb = row[1]
            sent = row[3]
            label = row[4]

            content = "Whether the verb '" + verb + "' in '" + sent + "' is a metaphorical expression (output yes or no)."
            print(content)

            max_loop = 30
            INDEX = 0
            answer = "error"
            while(True):
                INDEX += 1
                if INDEX > max_loop:
                    break
                print("start the ", INDEX, "request")
                try:
                    answer = get_chatgpt_request(content)
                    print("request success")
                    print(answer['choices'][0]['message']['content'], "->", label)
                    answer = answer['choices'][0]['message']['content']
                    break
                except:
                    print("request error and sleep 3s")
                    time.sleep(3)

            csv_writer.writerow([i, index, verb, sent, label, answer])
            print(i, "has been written")
def Add_VUAverb_label_by_Chatgpt_Api(source_file, target_file):
    import csv
    import time

    start = -1
    end = 10000

    with open(source_file, 'r', newline='') as source_csv, \
            open(target_file, 'w', newline='') as new_csv:

        csv_reader = csv.reader(source_csv)
        csv_writer = csv.writer(new_csv)

        for i, row in enumerate(csv_reader):

            if i <= start:
                continue
            if i > end:
                break

            index = row[1]
            verb = row[2]
            sent = row[3]
            label = row[4]

            content = "Whether the verb '" + verb + "' in '" + sent + "' is a metaphorical expression (output yes or no)."
            print(content)

            max_loop = 30
            INDEX = 0
            answer = "error"
            while(True):
                INDEX += 1
                if INDEX > max_loop:
                    break
                print("start the ", INDEX, "request")
                try:
                    answer = get_chatgpt_request(content)
                    print("request success")
                    print(answer['choices'][0]['message']['content'], "->", label)
                    answer = answer['choices'][0]['message']['content']
                    break
                except:
                    print("request error and sleep 3s")
                    time.sleep(3)

            csv_writer.writerow([i, index, verb, sent, label, answer])
            print(i, "has been written")





def Build_verb_lists_by_Chatgpt_Api(verb_txt_file, target_file):
    import csv
    import time

    start = -1
    end = 10000

    with open(verb_txt_file, 'r') as source, \
            open(target_file, 'w', newline='') as new_csv:

        verb_list = eval(source.read())
        csv_writer = csv.writer(new_csv)

        for i, verb in enumerate(verb_list):

            if i <= start:
                continue
            if i > end:
                break

            content = "Please provide as many examples as possible of subject and object subject categories that go with the verb " + verb + " in non-metaphorical or literal usage. Format: Subject Categories:\n1.\n2.\n Object Categories:\n1.\n2."
            print(content)

            max_loop = 30
            INDEX = 0
            answer = "max loop error"
            while(True):
                INDEX += 1
                if INDEX > max_loop:
                    break
                print("start the ", INDEX, "request")
                try:
                    answer = get_chatgpt_request(content)
                    print("request success")
                    answer = answer['choices'][0]['message']['content']
                    print(answer)
                    break
                except:
                    print("request error and sleep 3s")
                    time.sleep(3)

            csv_writer.writerow([i, verb, answer])
            print(i, "has been written")

def Build_VUAverb_verb_lists_by_Chatgpt_Api(verb_txt_file, target_file):
    import csv
    import time

    start = -1
    end = 10000

    with open(verb_txt_file, 'r') as source, \
            open(target_file, 'a', newline='') as new_csv:

        verb_list = eval(source.read())
        csv_writer = csv.writer(new_csv)

        for i, verb in enumerate(verb_list):

            if i <= start:
                continue
            if i > end:
                break

            content = "Please provide as many examples as possible of subject and object subject categories that go with the verb " + verb + " in non-metaphorical or literal usage. Format: Subject Categories:\n1.\n2.\n Object Categories:\n1.\n2."

            max_loop = 30
            INDEX = 0
            answer = "max loop error"
            while(True):
                INDEX += 1
                if INDEX > max_loop:
                    break
                print("start the ", INDEX, "request")
                try:
                    answer = get_chatgpt_request(content)
                    print("request success")
                    print(answer['choices'][0]['message']['content'])
                    break
                except:
                    print("request error and sleep 3s")
                    time.sleep(3)

            csv_writer.writerow([i, verb, answer])
            print(i, "has been written")

def Add_TroFi_sent_svo_by_Chatgpt_Api(source_tsv_file, target_file):
    import csv
    import time

    start = -1
    end = 10000

    with open(source_tsv_file, 'r', newline='') as source_csv, \
            open(target_file, 'w', newline='') as new_csv:

        csv_reader = csv.reader(source_csv, delimiter="\t")
        csv_writer = csv.writer(new_csv)

        for i, row in enumerate(csv_reader):

            if i <= start:
                continue
            if i > end:
                break

            index = row[0]
            verb = row[1]
            sent = row[3]
            label = row[4]

            content = "For sentences" + sent + ". Please provide the subject and object of the verb " + verb + " located at " + index + " in order of format. For example, subject: \nobject:"
            print(content)

            max_loop = 30
            INDEX = 0
            answer = "error"
            while(True):
                INDEX += 1
                if INDEX > max_loop:
                    break
                print("start the ", INDEX, "request")
                try:
                    answer = get_chatgpt_request(content)
                    print("request success")
                    print(answer['choices'][0]['message']['content'])
                    break
                except:
                    print("request error and sleep 3s")
                    time.sleep(3)

            csv_writer.writerow([i, index, verb, sent, label, answer])
            print(i, "has been written")
def Add_VUAverb_sent_svo_by_Chatgpt_Api(source_tsv_file, target_file):
    import csv
    import time
    import nltk
    import string
    from nltk.stem import WordNetLemmatizer
    nltk.download('wordnet')
    lemmatizer = WordNetLemmatizer()

    start = -1
    end = 10000

    with open(source_tsv_file, 'r', newline='') as source_csv, \
            open(target_file, 'w', newline='') as new_csv:

        csv_reader = csv.reader(source_csv, delimiter="\t")
        csv_writer = csv.writer(new_csv)

        for i, row in enumerate(csv_reader):

            if i <= start:
                continue
            if i > end:
                break

            label = row[0]
            sent = row[1]
            POS = row[2]
            index = row[3]

            sent_list = sent.split()

            if POS != "VERB":
                continue

            try:
                verb = sent_list[int(index)]
            except:
                continue

            verb = verb.rstrip(string.punctuation)
            verb = verb.lower()
            verb = lemmatizer.lemmatize(verb, pos="v")

            content = "For sentences" + sent + ". Please provide the subject and object of the verb " + verb + " located at " + index + " in order of format. For example, subject: \nobject:"
            print(content)

            max_loop = 30
            INDEX = 0
            answer = "error"
            while(True):
                INDEX += 1
                if INDEX > max_loop:
                    break
                print("start the ", INDEX, "request")
                try:
                    answer = get_chatgpt_request(content)
                    print("request success")
                    answer = answer['choices'][0]['message']['content']
                    print(answer)
                    break
                except:
                    print("request error and sleep 3s")
                    time.sleep(3)

            csv_writer.writerow([i, index, verb, sent, label, answer])
            print(i, "has been written")

def convert_dataset_svo_answer_to_list(source_file, target_file):

    import csv

    start = -1
    end = 10000

    with open(source_file, 'r') as source_csv, \
            open(target_file, 'w', newline='') as new_csv:

        csv_reader = csv.reader(source_csv)
        csv_writer = csv.writer(new_csv)

        for i, row in enumerate(csv_reader):

            if i <= start:
                continue
            if i > end:
                break

            index = row[1]
            verb = row[2]
            sent = row[3]
            label = row[4]
            svo = eval(row[5])

            new_svo = svo['choices'][0]['message']['content']

            subject_pattern = "Subject：(.+)\n"
            object_pattern = "Object：(.+)\n"

            # Extract subject, object, adverb, preposition
            subject_match = re.search(subject_pattern, new_svo)
            object_match = re.search(object_pattern, new_svo)

            subject = subject_match.group(1) if subject_match else ""
            object = object_match.group(1) if object_match else ""

            new_svo_list = [subject.strip(), object.strip()]
            print(svo, "->", new_svo_list)
            csv_writer.writerow([i, index, verb, sent, label, new_svo_list])
def convert_VUAverb_svo_answer_to_list(source_file, target_file):
    import csv

    f = open(source_file, "r")
    ff = open(target_file, "w")
    cr = csv.reader(f)
    cw = csv.writer(ff)

    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        elif i > end:
            break

        verb = row[2]
        content = row[5]

        sub = ""
        ob = ""

        for kk, t in enumerate(content.split("\n")):

            if not t:
                continue

            t = t.strip()

            c1 = t.split("：")

            if len(c1) > 1 and c1[0] == "Subject":
                sub = c1[1]
                continue

            if len(c1) > 1 and c1[0] == "Object":
                ob = c1[1]
                continue

        print(verb, "->", [sub, ob])
        svo_list = [sub, ob]

        cw.writerow([i, row[1], row[2], row[3], row[4], svo_list])
        print(i, "correct writted")



def convert_MOX_verb_lists_to_synonyms_and_hyper(source_file, target_file):

    import csv
    f = open(source_file, "r")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    for i, tran in enumerate(cr):


        content = tran[2]

        new_content_sub = []
        new_hyper_sub = []
        new_sym_sub = []
        new_content_ob = []
        new_hyper_ob = []
        new_sym_ob = []


        if_sub = False
        if_ob = False


        for kk, t in enumerate(content.split("\n")):

            t = re.sub(r'\([^)]*\)', '', t)
            t = re.sub("\*\*", "", t)
            t = re.sub(r':[^:]*', '', t)
            t = re.sub(r'In a non-metaphorical sense, .*?\.', '', t)
            t = re.sub(r'In these non-metaphorical or literal contexts, .*?\.', '', t)
            t = re.sub(r'In non-metaphorical usage, .*?\.', '', t)
            t = re.sub(r'In this context, .*?\.', '', t)

            t = re.sub(r'^\d+\.', '', t)

            if len(t.split()) > 5 and kk == len(content.split("\n")) - 1:
                break

            if "Subject Categories" in t:
                if_sub = True
                continue
            if "Object Categories" in t:
                if_sub = False
                if_ob = True
                continue

            if if_sub and t:
                t = get_first_noun(t)
                sym_list, hyper_list = get_synonyms_and_hyper(t)
                if sym_list:
                    new_sym_sub.append(sym_list)
                    print(t, "->", sym_list)
                else:
                    new_sym_sub.append(t)
                    print(t, "->", t)

                if hyper_list:
                    new_hyper_sub.append(hyper_list)
                    print(t, "->", hyper_list)
                else:
                    new_hyper_sub.append(t)
                    print(t, "->", t)

                if t.lower() not in new_content_sub:
                    new_content_sub.append(t)


            if if_ob and t:
                t = get_first_noun(t)
                sym_list, hyper_list = get_synonyms_and_hyper(t)
                if sym_list:
                    new_sym_ob.append(sym_list)
                    print(t, "->", sym_list)
                else:
                    new_sym_ob.append(t)
                    print(t, "->", t)

                if hyper_list:
                    new_hyper_ob.append(hyper_list)
                    print(t, "->", hyper_list)
                else:
                    new_hyper_ob.append(t)
                    print(t, "->", t)

                if t.lower() not in new_content_ob:
                    new_content_ob.append(t)

        print(tran[1])
        print(new_content_sub)
        print(new_content_ob)
        print("-----------------")
        print(new_hyper_sub)
        print(new_hyper_ob)
        print("-----------------")
        print(new_sym_sub)
        print(new_sym_ob)

        cw.writerow([tran[1], new_sym_sub, new_sym_ob, new_hyper_sub, new_hyper_ob, new_content_sub, new_content_ob])
def convert_MOX_verb_lists_to_hypernyms(source_file, target_file):

    import csv
    from nltk.corpus import wordnet

    f = open(source_file, "r")
    ff = open(target_file, "w")
    cr = csv.reader(f)
    cw = csv.writer(ff)

    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        elif i > end:
            break

        verb = row[1]
        content = row[2]

        new_content_sub = []
        new_type_sub = []
        new_content_ob = []
        new_type_ob = []

        if_sub = False
        if_ob = False

        if content == "error" or content == "[]":
            cw.writerow([i, verb, "[]"])
            print(i, "error or [] writted")
            continue

        new_content = ""
        for kk, t in enumerate(content.split("\n")):

            if not t:
                continue

            t = t.strip()

            if len(t.split(":")) > 1:
                new_t = t.split(":")[0]
                # print(": change", t, "->", new_t)
                t = new_t

            pattern = r'^-[\w\s]+'
            matches = re.findall(pattern, t)
            if matches:
                continue

            t = re.sub(r'^\d+\.', '', t)

            pattern = r'\([^)]*\)'
            t = re.sub(pattern, '', t)

            new_content += str(t)
            new_content += "\n"

            if "Subject Categories" in t:
                if_sub = True
                continue
            if "Object Categories" in t:
                if_sub = False
                if_ob = True
                continue

            if if_sub and t:
                if len(t.split("/")) > 1:
                    t = t.split("/")[0]
                t = get_first_noun(t)
                t = plural_to_singular(t)
                print(t)
                typer_list = get_hypernyms(t, wordnet)

                if typer_list and typer_list not in new_type_sub:
                    new_type_sub.append(typer_list)
                    print(t, "->", typer_list)
                else:
                    new_type_sub.append(t)
                    print(t, "->", t)

                if t.lower() not in new_content_sub:
                    new_content_sub.append(t)

            if if_ob and t:
                if len(t.split("/")) > 1:
                    t = t.split("/")[0]
                t = get_first_noun(t)
                t = plural_to_singular(t)
                typer_list = get_hypernyms(t, wordnet)

                if typer_list and typer_list not in new_content_ob:
                    new_type_ob.append(typer_list)
                    print(t, "->", typer_list)
                else:
                    new_type_ob.append(t)
                    print(t, "->", t)

                if t.lower() not in new_content_ob:
                    new_content_ob.append(t)

        print(verb)
        print(new_content_sub)
        print(new_content_ob)
        print("-----------------")
        print(new_type_sub)
        print(new_type_ob)
        print("-----------------")


        cw.writerow([i, verb, new_type_sub, new_type_ob, new_content_sub, new_content_ob])
        print(i, "correct writted")
def convert_MOH_verb_lists_to_wn_topic(source_file, target_file):

    import csv
    from nltk.corpus import wordnet

    f = open(source_file, "r", errors="ignore")
    ff = open(target_file, "a")
    cr = csv.reader(f)
    cw = csv.writer(ff)

    start = -1
    end = 1000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        elif i > end:
            break

        verb = row[1]
        content = row[2]

        new_content_sub = []
        new_type_sub = []
        new_content_ob = []
        new_type_ob = []

        if_sub = False
        if_ob = False

        if content == "error" or content == "[]":
            cw.writerow([i, verb, "[]"])
            print(i, "error or [] writted")
            continue


        new_content = ""
        for kk, t in enumerate(content.split("\n")):

            if not t:
                continue

            t = t.strip()

            if len(t.split(":")) > 1:
                new_t = t.split(":")[0]
                # print(": change", t, "->", new_t)
                t = new_t

            pattern = r'^-[\w\s]+'
            matches = re.findall(pattern, t)
            if matches:
                continue

            t = re.sub(r'^\d+\.', '', t)

            pattern = r'\([^)]*\)'
            t = re.sub(pattern, '', t)

            new_content += str(t)
            new_content += "\n"

            if "Subject Categories" in t:
                if_sub = True
                continue
            if "Object Categories" in t:
                if_sub = False
                if_ob = True
                continue

            if if_sub and t:
                if len(t.split("/")) > 1:
                    t = t.split("/")[0]
                t = get_first_noun(t)
                t = plural_to_singular(t)
                typer_list = cal_similarity(t, wordnet)

                if typer_list and typer_list not in new_type_sub:
                    new_type_sub.append(typer_list)
                    print(t, "->", typer_list)
                else:
                    new_type_sub.append(t)
                    print(t, "->", t)

                if t.lower() not in new_content_sub:
                    new_content_sub.append(t)

            if if_ob and t:
                if len(t.split("/")) > 1:
                    t = t.split("/")[0]
                t = get_first_noun(t)
                t = plural_to_singular(t)
                typer_list = cal_similarity(t, wordnet)

                if typer_list and typer_list not in new_content_ob:
                    new_type_ob.append(typer_list)
                    print(t, "->", typer_list)
                else:
                    new_type_ob.append(t)
                    print(t, "->", t)

                if t.lower() not in new_content_ob:
                    new_content_ob.append(t)

        print(verb)
        print(new_content_sub)
        print(new_content_ob)
        print("-----------------")
        print(new_type_sub)
        print(new_type_ob)
        print("-----------------")


        cw.writerow([i, verb, new_type_sub, new_type_ob, new_content_sub, new_content_ob])
        print(i, "correct writted")
def convert_MOX_verb_lists_to_oxford_topic(source_file, target_file):
    import csv
    f = open(source_file, "r", errors="ignore")
    ff = open(target_file, "a")
    cr = csv.reader(f)
    cw = csv.writer(ff)

    start = 83
    end = 1000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        elif i > end:
            break

        verb = row[1]
        content = row[2]

        new_content_sub = []
        new_type_sub = []
        new_content_ob = []
        new_type_ob = []

        if_sub = False
        if_ob = False

        if content == "error" or content == "[]":
            cw.writerow([i, verb, "[]"])
            print(i, "error or [] writted")
            continue

        new_content = ""
        for kk, t in enumerate(content.split("\n")):

            if not t:
                continue

            t = t.strip()

            if len(t.split(":")) > 1:
                new_t = t.split(":")[0]
                # print(": change", t, "->", new_t)
                t = new_t

            pattern = r'^-[\w\s]+'

            matches = re.findall(pattern, t)
            if matches:
                continue

            t = re.sub(r'^\d+\.', '', t)

            pattern = r'\([^)]*\)'
            t = re.sub(pattern, '', t)

            new_content += str(t)
            new_content += "\n"

            if "Subject Categories" in t:
                if_sub = True
                continue
            if "Object Categories" in t:
                if_sub = False
                if_ob = True
                continue

            if if_sub and t:
                if len(t.split("/")) > 1:
                    t = t.split("/")[0]
                t = get_first_noun(t)
                t = plural_to_singular(t)
                INDEX = 0
                typer_list = []
                while (True):
                    INDEX += 1
                    if INDEX > 50:
                        break
                    print("request the", INDEX)
                    try:
                        typer_list = get_topic_from_oxford_dir(t)
                        break
                    except:
                        print("request error and try again")
                        time.sleep(3)

                if typer_list and typer_list not in new_type_sub:
                    new_type_sub.append(typer_list)
                    print(t, "->", typer_list)
                else:
                    new_type_sub.append(t)
                    print(t, "->", t)

                if t.lower() not in new_content_sub:
                    new_content_sub.append(t)

            if if_ob and t:
                if len(t.split("/")) > 1:
                    t = t.split("/")[0]
                t = get_first_noun(t)
                t = plural_to_singular(t)
                INDEX = 0
                typer_list = []
                while (True):
                    INDEX += 1
                    if INDEX > 50:
                        break
                    print("request the", INDEX)
                    try:
                        typer_list = get_topic_from_oxford_dir(t)
                        break
                    except:
                        print("request error and try again")
                        time.sleep(3)

                if typer_list and typer_list not in new_content_ob:
                    new_type_ob.append(typer_list)
                    print(t, "->", typer_list)
                else:
                    new_type_ob.append(t)
                    print(t, "->", t)

                if t.lower() not in new_content_ob:
                    new_content_ob.append(t)

        print(verb)
        print(new_content_sub)
        print(new_content_ob)
        print("-----------------")
        print(new_type_sub)
        print(new_type_ob)
        print("-----------------")

        cw.writerow([i, verb, new_type_sub, new_type_ob, new_content_sub, new_content_ob])
        print(i, "correct writted")
def convert_MOX_sent_svo_to_synonyms_and_hyper(source_file, target_file):

    import csv

    f = open(source_file, "r")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    for i, row in enumerate(cr):

        svo = eval(row[5])
        sent = row[2]

        new_svo_hyper = []
        new_svo_sym = []

        for kk, s in enumerate(svo):

            if kk == 0 or kk == 1:
                pos_s = get_first_noun(s)
            else:
                pos_s = s

            print(s, "->", pos_s)

            new_s = ""
            for ss in pos_s.split():

                if ss == "he" or ss == "she" or ss == "He" or ss == "She" or ss == "I" or ss == "we" or ss == "We" or ss == "him" or ss == "her":
                    new_s += "people"
                    new_s += " "
                else:
                    new_s += ss
                    new_s += " "
            new_s = new_s[:-1]

            if (kk == 0 or kk == 1) and new_s and new_s != "people" and new_s != "none":
                sym_list, hyper_list = get_synonyms_and_hyper(new_s)
                if sym_list:
                    print(new_s, "->", sym_list)
                    new_svo_sym.append(list(sym_list))
                else:
                    print(new_s, "->", new_s)
                    new_svo_sym.append(new_s)

                if hyper_list:
                    print(new_s, "->", hyper_list)
                    new_svo_hyper.append(list(hyper_list))
                else:
                    print(new_s, "->", new_s)
                    new_svo_hyper.append(new_s)
            else:
                new_svo_hyper.append(new_s)
                new_svo_sym.append(new_s)

        print(svo)
        print(new_svo_hyper)
        print(new_svo_sym)
        print(sent)
        print("-----------------")

        cw.writerow([row[0], row[1], row[2], row[3], row[4], new_svo_sym, new_svo_hyper, row[6]])
def convert_MOX_sent_svo_to_hypernyms(source_file, target_file):

    import csv
    from nltk.corpus import wordnet

    f = open(source_file, "r")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        if i > end:
            break

        svo = eval(row[5])
        sent = row[2]

        new_svo = []
        for kk, s in enumerate(svo):

            if kk == 0 or kk == 1:
                pos_s = get_first_noun(s)
            else:
                pos_s = s

            print(s, "->", pos_s)

            new_s = ""
            for ss in pos_s.split():

                if if_people_pronoun(ss):
                    new_s += "people"
                    new_s += " "
                else:
                    new_s += ss
                    new_s += " "
            new_s = new_s[:-1]

            if (kk == 0 or kk == 1) and new_s and new_s != "person" and new_s != "people" and new_s != "none" and new_s != "-":
                typer_list = get_hypernyms(new_s, wordnet)
                if typer_list:
                    print("hyper exist:", new_s, "->", typer_list)
                    new_svo.append(typer_list)
                else:
                    print("hyper is none:", new_s, "->", "none&" + new_s)
                    new_svo.append("none&" + new_s)
            else:
                new_svo.append(new_s)

        print(svo)
        print(new_svo)
        print(sent)
        print("-----------------")

        cw.writerow([row[0], row[1], row[2], row[3], row[4], new_svo])
def convert_MOX_sent_to_hypernyms_k(source_file, target_file):

    import csv
    from nltk.corpus import wordnet

    f = open(source_file, "r")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    TOP_K = 3
    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        if i > end:
            break

        svo = eval(row[5])
        sent = row[2]

        new_svo = []
        for kk, s in enumerate(svo):

            if kk == 0 or kk == 1:
                pos_s = get_top_k_noun(TOP_K, s)
            else:
                pos_s = [s]

            print("get top" + str(TOP_K) + ":", s, "->", pos_s)

            new_s = []
            for ss in pos_s:
                if if_people_pronoun(ss):
                    new_s.append("people")
                else:
                    new_s.append(ss)

            ns_list = []
            for ns in new_s:
                if (kk == 0 or kk == 1) and ns and ns != "person" and ns != "people" and ns != "none" and ns != "-":
                    typer_list = get_hypernyms(ns, wordnet)
                    if typer_list:
                        print("hyper exist:", ns, "->", typer_list)
                        ns_list.append(typer_list)
                    else:
                        print("hyper is none:", ns, "->", "none&" + ns)
                        ns_list.append("none&" + ns)
                else:
                    ns_list.append(ns)

            new_svo.append(ns_list)
            print("new_s->ns_list:", new_s, "->", ns_list)

        print(svo)
        print(new_svo)
        print(sent)
        print("-----------------")

        cw.writerow([row[0], row[1], row[2], row[3], row[4], new_svo])
def convert_MOX_sent_svo_to_wn_topic(source_file, target_file):
    import time
    import csv
    from nltk.corpus import wordnet

    f = open(source_file, "r")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        if i > end:
            break

        svo = eval(row[5])
        sent = row[2]

        new_svo = []
        for kk, s in enumerate(svo):

            if kk == 0 or kk == 1:
                pos_s = get_first_noun(s)
            else:
                pos_s = s

            print(s, "->", pos_s)

            new_s = ""
            for ss in pos_s.split():

                if if_people_pronoun(ss):
                    new_s += "people"
                    new_s += " "
                else:
                    new_s += ss
                    new_s += " "
            new_s = new_s[:-1]

            if (kk == 0 or kk == 1) and new_s and new_s != "person" and new_s != "people" and new_s != "none" and new_s != "-":
                typer_list = cal_similarity(new_s, wordnet)
                if typer_list:
                    print("hyper exist:", new_s, "->", typer_list)
                    new_svo.append(typer_list)
                else:
                    print("hyper is none:", new_s, "->", "none&" + new_s)
                    new_svo.append("none&" + new_s)
            else:
                new_svo.append(new_s)

        print(svo)
        print(new_svo)
        print(sent)
        print("-----------------")

        cw.writerow([row[0], row[1], row[2], row[3], row[4], new_svo])
def convert_MOX_sent_svo_to_wn_topic_k(source_file, target_file):

    import csv
    from nltk.corpus import wordnet

    f = open(source_file, "r")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    TOP_K = 3
    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        if i > end:
            break

        svo = eval(row[5])
        sent = row[2]

        new_svo = []
        for kk, s in enumerate(svo):

            if kk == 0 or kk == 1:
                pos_s = get_top_k_noun(TOP_K, s)
            else:
                pos_s = [s]

            print("get top" + str(TOP_K) + ":", s, "->", pos_s)

            new_s = []
            for ss in pos_s:
                if if_people_pronoun(ss):
                    new_s.append("people")
                else:
                    new_s.append(ss)

            ns_list = []
            for ns in new_s:
                if (kk == 0 or kk == 1) and ns and ns != "person" and ns != "people" and ns != "none" and ns != "-":
                    typer_list = cal_similarity(ns, wordnet)
                    if typer_list:
                        print("hyper exist:", ns, "->", typer_list)
                        ns_list.append(typer_list)
                    else:
                        print("hyper is none:", ns, "->", "none&" + ns)
                        ns_list.append("none&" + ns)
                else:
                    ns_list.append(ns)

            new_svo.append(ns_list)
            print("new_s->ns_list:", new_s, "->", ns_list)

        print(svo)
        print(new_svo)
        print(sent)
        print("-----------------")

        cw.writerow([row[0], row[1], row[2], row[3], row[4], new_svo])
def convert_MOX_sent_svo_to_oxford_topic_k(source_file, target_file):

    import csv

    f = open(source_file, "r", errors="ignore")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    TOP_K = 3
    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        if i > end:
            break

        svo = eval(row[5])
        sent = row[2]

        new_svo = []
        for kk, s in enumerate(svo):

            if kk == 0 or kk == 1:
                pos_s = get_top_k_noun(TOP_K, s)
            else:
                pos_s = [s]

            print("get top" + str(TOP_K) + ":", s, "->", pos_s)

            new_s = []
            for ss in pos_s:
                if if_people_pronoun(ss):
                    new_s.append("people")
                else:
                    new_s.append(ss)

            ns_list = []
            for ns in new_s:
                if (kk == 0 or kk == 1) and ns and ns != "person" and ns != "people" and ns != "none" and ns != "-":
                    INDEX = 0
                    typer_list = []
                    while (True):
                        INDEX += 1
                        if INDEX > 50:
                            break
                        print("request the", INDEX)
                        try:
                            typer_list = get_topic_from_oxford_dir(ns)
                            break
                        except:
                            print("request error and try again")
                            time.sleep(3)
                    if typer_list:
                        print("hyper exist:", ns, "->", typer_list)
                        ns_list.append(typer_list)
                    else:
                        print("hyper is none:", ns, "->", "none&" + ns)
                        ns_list.append("none&" + ns)
                else:
                    ns_list.append(ns)

            new_svo.append(ns_list)
            print("new_s->ns_list:", new_s, "->", ns_list)

        print(svo)
        print(new_svo)
        print(sent)
        print("-----------------")

        cw.writerow([row[0], row[1], row[2], row[3], row[4], new_svo])
def convert_TroFi_sent_svo_to_hypernyms_k(source_file, target_file):

    import csv
    from nltk.corpus import wordnet

    f = open(source_file, "r")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    TOP_K = 3
    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        if i > end:
            break

        svo = eval(row[5])
        sent = row[2]

        new_svo = []
        for kk, s in enumerate(svo):

            if kk == 0 or kk == 1:
                pos_s = get_top_k_noun(TOP_K, s)
            else:
                pos_s = [s]

            print("get top" + str(TOP_K) + ":", s, "->", pos_s)

            new_s = []
            for ss in pos_s:
                if if_people_pronoun(ss):
                    new_s.append("people")
                else:
                    new_s.append(ss)

            ns_list = []
            for ns in new_s:
                if (kk == 0 or kk == 1) and ns and ns != "person" and ns != "people" and ns != "none" and ns != "-":
                    typer_list = get_hypernyms(ns, wordnet)
                    if typer_list:
                        print("hyper exist:", ns, "->", typer_list)
                        ns_list.append(typer_list)
                    else:
                        print("hyper is none:", ns, "->", "none&" + ns)
                        ns_list.append("none&" + ns)
                else:
                    ns_list.append(ns)

            new_svo.append(ns_list)
            print("new_s->ns_list:", new_s, "->", ns_list)

        print(svo)
        print(new_svo)
        print(sent)
        print("-----------------")

        cw.writerow([row[0], row[1], row[2], row[3], row[4], new_svo])
def convert_TroFi_sent_svo_to_hypernyms(source_file, target_file):

    import csv
    from nltk.corpus import wordnet

    f = open(source_file, "r")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        if i > end:
            break

        svo = eval(row[5])
        sent = row[2]

        new_svo = []
        for kk, s in enumerate(svo):

            if kk == 0 or kk == 1:
                pos_s = get_first_noun(s)
            else:
                pos_s = s

            print(s, "->", pos_s)

            new_s = ""
            for ss in pos_s.split():

                if if_people_pronoun(ss):
                    new_s += "people"
                    new_s += " "
                else:
                    new_s += ss
                    new_s += " "
            new_s = new_s[:-1]

            if (kk == 0 or kk == 1) and new_s and new_s != "person" and new_s != "people" and new_s != "none" and new_s != "-":
                typer_list = get_hypernyms(new_s, wordnet)
                if typer_list:
                    print("hyper exist:", new_s, "->", typer_list)
                    new_svo.append(typer_list)
                else:
                    print("hyper is none:", new_s, "->", "none&" + new_s)
                    new_svo.append("none&" + new_s)
            else:
                new_svo.append(new_s)

        print(svo)
        print(new_svo)
        print(sent)
        print("-----------------")

        cw.writerow([row[0], row[1], row[2], row[3], row[4], new_svo])
def convert_TroFi_sent_svo_to_wn_topic(source_file, target_file):
    import time
    import csv
    from nltk.corpus import wordnet

    f = open(source_file, "r")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        if i > end:
            break

        svo = eval(row[5])
        sent = row[2]

        new_svo = []
        for kk, s in enumerate(svo):

            if kk == 0 or kk == 1:
                pos_s = get_first_noun(s)
            else:
                pos_s = s

            print(s, "->", pos_s)

            new_s = ""
            for ss in pos_s.split():

                if if_people_pronoun(ss):
                    new_s += "people"
                    new_s += " "
                else:
                    new_s += ss
                    new_s += " "
            new_s = new_s[:-1]

            if (kk == 0 or kk == 1) and new_s and new_s != "person" and new_s != "people" and new_s != "none" and new_s != "-":
                typer_list = cal_similarity(new_s, wordnet)
                if typer_list:
                    print("hyper exist:", new_s, "->", typer_list)
                    new_svo.append(typer_list)
                else:
                    print("hyper is none:", new_s, "->", "none&" + new_s)
                    new_svo.append("none&" + new_s)
            else:
                new_svo.append(new_s)

        print(svo)
        print(new_svo)
        print(sent)
        print("-----------------")

        cw.writerow([row[0], row[1], row[2], row[3], row[4], new_svo])
def convert_TroFi_sent_svo_to_wn_topic_k(source_file, target_file):
    import csv
    from nltk.corpus import wordnet

    f = open(source_file, "r")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    TOP_K = 3
    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        if i > end:
            break

        svo = eval(row[5])
        sent = row[2]

        new_svo = []
        for kk, s in enumerate(svo):

            if kk == 0 or kk == 1:
                pos_s = get_top_k_noun(TOP_K, s)
            else:
                pos_s = [s]

            print("get top" + str(TOP_K) + ":", s, "->", pos_s)

            new_s = []
            for ss in pos_s:
                if if_people_pronoun(ss):
                    new_s.append("people")
                else:
                    new_s.append(ss)

            ns_list = []
            for ns in new_s:
                if (kk == 0 or kk == 1) and ns and ns != "person" and ns != "people" and ns != "none" and ns != "-":
                    typer_list = cal_similarity(ns, wordnet)
                    if typer_list:
                        print("hyper exist:", ns, "->", typer_list)
                        ns_list.append(typer_list)
                    else:
                        print("hyper is none:", ns, "->", "none&" + ns)
                        ns_list.append("none&" + ns)
                else:
                    ns_list.append(ns)

            new_svo.append(ns_list)
            print("new_s->ns_list:", new_s, "->", ns_list)

        print(svo)
        print(new_svo)
        print(sent)
        print("-----------------")

        cw.writerow([row[0], row[1], row[2], row[3], row[4], new_svo])
def convert_TroFi_sent_svo_oxford_topic_k(source_file, target_file):
    import csv

    f = open(source_file, "r")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    TOP_K = 3
    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        if i > end:
            break

        svo = eval(row[5])
        sent = row[2]

        new_svo = []
        for kk, s in enumerate(svo):

            if kk == 0 or kk == 1:
                pos_s = get_top_k_noun(TOP_K, s)
            else:
                pos_s = [s]

            print("get top" + str(TOP_K) + ":", s, "->", pos_s)

            new_s = []
            for ss in pos_s:
                if if_people_pronoun(ss):
                    new_s.append("people")
                else:
                    new_s.append(ss)

            ns_list = []
            for ns in new_s:
                if (kk == 0 or kk == 1) and ns and ns != "people" and ns != "none" and ns != "-":
                    try:
                        hyper_list = get_topic_from_oxford_dir(ns)
                    except:
                        print("request error:", ns, "->", '["404"]')
                        hyper_list = ["404"]
                    if hyper_list:
                        print("hyper exist:", ns, "->", hyper_list)
                        ns_list.append(hyper_list)
                    else:
                        print("hyper is none:", ns, "->", ns)
                        ns_list.append(ns)
                else:
                    ns_list.append(ns)

            new_svo.append(ns_list)
            print("new_s->ns_list:", new_s, "->", ns_list)

        print(svo)
        print(new_svo)
        print(sent)
        print("-----------------")

        cw.writerow([row[0], row[1], row[2], row[3], row[4], new_svo])
def convert_TroFi_verbs_lists_to_hypernyms(source_file, target_file):

    import csv
    from nltk.corpus import wordnet

    f = open(source_file, "r")
    ff = open(target_file, "w")
    cr = csv.reader(f)
    cw = csv.writer(ff)

    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        elif i > end:
            break

        verb = row[1]
        content = row[2]

        new_content_sub = []
        new_type_sub = []
        new_content_ob = []
        new_type_ob = []

        if_sub = False
        if_ob = False

        if content == "error" or content == "[]":
            cw.writerow([i, verb, "[]"])
            print(i, "error or [] writted")
            continue

        new_content = ""
        for kk, t in enumerate(content.split("\n")):

            if not t:
                continue

            t = t.strip()
            if len(t.split(":")) > 1:
                new_t = t.split(":")[0]
                # print(": change", t, "->", new_t)
                t = new_t

            pattern = r'^-[\w\s]+'

            matches = re.findall(pattern, t)
            if matches:
                continue

            t = re.sub(r'^\d+\.', '', t)

            pattern = r'\([^)]*\)'
            t = re.sub(pattern, '', t)

            new_content += str(t)
            new_content += "\n"

            if "Subject Categories" in t:
                if_sub = True
                continue
            if "Object Categories" in t:
                if_sub = False
                if_ob = True
                continue

            if if_sub and t:
                if len(t.split("/")) > 1:
                    t = t.split("/")[0]
                t = get_first_noun(t)
                t = plural_to_singular(t)
                print(t)
                typer_list = get_hypernyms(t, wordnet)

                if typer_list and typer_list not in new_type_sub:
                    new_type_sub.append(typer_list)
                    print(t, "->", typer_list)
                else:
                    new_type_sub.append(t)
                    print(t, "->", t)

                if t.lower() not in new_content_sub:
                    new_content_sub.append(t)

            if if_ob and t:
                if len(t.split("/")) > 1:
                    t = t.split("/")[0]
                t = get_first_noun(t)
                t = plural_to_singular(t)
                typer_list = get_hypernyms(t, wordnet)

                if typer_list and typer_list not in new_content_ob:
                    new_type_ob.append(typer_list)
                    print(t, "->", typer_list)
                else:
                    new_type_ob.append(t)
                    print(t, "->", t)

                if t.lower() not in new_content_ob:
                    new_content_ob.append(t)

        print(verb)
        print(new_content_sub)
        print(new_content_ob)
        print("-----------------")
        print(new_type_sub)
        print(new_type_ob)
        print("-----------------")


        cw.writerow([i, verb, new_type_sub, new_type_ob, new_content_sub, new_content_ob])
        print(i, "correct writted")
def convert_TroFi_verb_lists_to_wordnet_topic(source_file, target_file):
    from nltk.corpus import wordnet
    import csv

    f = open(source_file, "r")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    start = -1
    end = 10000


    for i, tran in enumerate(cr):


        if i <= start:
            continue
        if i > end:
            break

        content = tran[2]

        new_content_sub = []
        new_type_sub = []
        new_content_ob = []
        new_type_ob = []


        if_sub = False
        if_ob = False


        for kk, t in enumerate(content.split("\n")):

            t = re.sub(r'\([^)]*\)', '', t)
            t = re.sub("\*\*", "", t)
            t = re.sub(r':[^:]*', '', t)
            t = re.sub(r'In a non-metaphorical sense, .*?\.', '', t)
            t = re.sub(r'In these non-metaphorical or literal contexts, .*?\.', '', t)
            t = re.sub(r'In non-metaphorical usage, .*?\.', '', t)
            t = re.sub(r'In this context, .*?\.', '', t)

            t = re.sub(r'^\d+\.', '', t)

            if len(t.split()) > 5 and kk == len(content.split("\n")) - 1:
                break

            if "Subject Categories" in t:
                if_sub = True
                continue
            if "Object Categories" in t:
                if_sub = False
                if_ob = True
                continue

            if if_sub and t:
                t = get_first_noun(t)
                typer_list = cal_similarity(t, wordnet)
                if typer_list and typer_list not in new_type_sub:
                    new_type_sub.append(typer_list)
                    print(t, "->", typer_list)
                else:
                    new_type_sub.append(t)
                    print(t, "->", t)

                if t.lower() not in new_content_sub:
                    new_content_sub.append(t)

            if if_ob and t:
                t = get_first_noun(t)
                typer_list = cal_similarity(t, wordnet)
                if typer_list and typer_list not in new_content_ob:
                    new_type_ob.append(typer_list)
                    print(t, "->", typer_list)
                else:
                    new_type_ob.append(t)
                    print(t, "->", t)

                if t.lower() not in new_content_ob:
                    new_content_ob.append(t)

        print(tran[1])
        print(new_content_sub)
        print(new_content_ob)
        print("-----------------")
        print(new_type_sub)
        print(new_type_ob)
        print("-----------------")

        cw.writerow([tran[1], new_type_sub, new_type_ob, new_content_sub, new_content_ob])
def convert_TroFi_verbs_lists_to_oxford_topic(source_file, target_file):
    import time
    import csv

    f = open(source_file, "r")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        if i > end:
            break

        svo = eval(row[5])
        sent = row[2]

        new_svo = []
        for kk, s in enumerate(svo):

            if kk == 0 or kk == 1:
                pos_s = get_first_noun(s)
            else:
                pos_s = s

            print(s, "->", pos_s)

            new_s = ""
            for ss in pos_s.split():

                if if_people_pronoun(ss):
                    new_s += "people"
                    new_s += " "
                else:
                    new_s += ss
                    new_s += " "
            new_s = new_s[:-1]

            if (kk == 0 or kk == 1) and new_s and new_s != "person" and new_s != "people" and new_s != "none" and new_s != "-":
                INDEX = 0
                typer_list = []
                while (True):
                    INDEX += 1
                    if INDEX > 50:
                        break
                    print("request the", INDEX)
                    try:
                        typer_list = get_topic_from_oxford_dir(new_s)
                        break
                    except:
                        print("request error and try again")
                        time.sleep(3)
                if typer_list:
                    print("hyper exist:", new_s, "->", typer_list)
                    new_svo.append(typer_list)
                else:
                    print("hyper is none:", new_s, "->", "none&" + new_s)
                    new_svo.append("none&" + new_s)
            else:
                new_svo.append(new_s)

        print(svo)
        print(new_svo)
        print(sent)
        print("-----------------")

        cw.writerow([row[0], row[1], row[2], row[3], row[4], new_svo])
def convert_VUAverb_verb_lists_to_oxford_topic(source_file, target_file):

    import csv
    f = open(source_file, "r")
    ff = open(target_file, "w")
    cr = csv.reader(f)
    cw = csv.writer(ff)

    start = -1
    end = 1000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        elif i > end:
            break

        verb = row[1]
        content = row[2]

        new_content_sub = []
        new_type_sub = []
        new_content_ob = []
        new_type_ob = []

        if_sub = False
        if_ob = False

        if content == "error" or content == "[]":
            cw.writerow([i, verb, "[]"])
            print(i, "error or [] writted")
            continue


        new_content = ""
        for kk, t in enumerate(content.split("\n")):

            if not t:
                continue

            t = t.strip()

            if len(t.split(":")) > 1:
                new_t = t.split(":")[0]
                # print(": change", t, "->", new_t)
                t = new_t

            pattern = r'^-[\w\s]+'

            matches = re.findall(pattern, t)
            if matches:
                continue

            t = re.sub(r'^\d+\.', '', t)

            pattern = r'\([^)]*\)'
            t = re.sub(pattern, '', t)

            new_content += str(t)
            new_content += "\n"

            if "Subject Categories" in t:
                if_sub = True
                continue
            if "Object Categories" in t:
                if_sub = False
                if_ob = True
                continue

            if if_sub and t:
                t = get_first_noun(t)
                t = plural_to_singular(t)
                INDEX = 0
                typer_list = []
                while (True):
                    INDEX += 1
                    if INDEX > 50:
                        break
                    print("request the", INDEX)
                    try:
                        typer_list = get_topic_from_oxford_dir(t)
                        break
                    except:
                        print("request error and try again")
                        time.sleep(3)

                if typer_list and typer_list not in new_type_sub:
                    new_type_sub.append(typer_list)
                    print(t, "->", typer_list)
                else:
                    new_type_sub.append(t)
                    print(t, "->", t)

                if t.lower() not in new_content_sub:
                    new_content_sub.append(t)

            if if_ob and t:
                t = get_first_noun(t)
                t = plural_to_singular(t)
                INDEX = 0
                typer_list = []
                while (True):
                    INDEX += 1
                    if INDEX > 50:
                        break
                    print("request the", INDEX)
                    try:
                        typer_list = get_topic_from_oxford_dir(t)
                        break
                    except:
                        print("request error and try again")
                        time.sleep(3)

                if typer_list and typer_list not in new_content_ob:
                    new_type_ob.append(typer_list)
                    print(t, "->", typer_list)
                else:
                    new_type_ob.append(t)
                    print(t, "->", t)

                if t.lower() not in new_content_ob:
                    new_content_ob.append(t)

        print(verb)
        print(new_content_sub)
        print(new_content_ob)
        print("-----------------")
        print(new_type_sub)
        print(new_type_ob)
        print("-----------------")


        cw.writerow([i, verb, new_type_sub, new_type_ob, new_content_sub, new_content_ob])
        print(i, "correct writted")
def convert_VUAverb_verb_lists_to_oxford_topic_k(source_file, target_file):
    import csv

    f = open(source_file, "r")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    TOP_K = 3
    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        if i > end:
            break

        label = row[1]
        sent = row[2]
        index = row[3]
        verb = row[4]
        svo = eval(row[5])

        sub_lists = []
        ob_lists = []
        for kk, s in enumerate(svo):

            if len(s) == 3 and verb in s[1]:
                sub_list = svo_to_topic(TOP_K, s[0])
                ob_list = svo_to_topic(TOP_K, s[2])
                if sub_list:
                    sub_lists += sub_list
                if ob_list:
                    ob_lists += ob_list
            elif len(s) == 2 and verb in s[1]:
                sub_list = svo_to_topic(TOP_K, s[0])
                if sub_list:
                    sub_lists += sub_list
            elif len(s) == 2 and verb in s[0]:
                ob_list = svo_to_topic(TOP_K, s[1])
                if ob_list:
                    ob_lists += ob_list
            else:
                print("svo error", s)

        print("s->sub_list", s, "->", sub_lists)
        print("s->ob_list", s, "->", ob_lists)

        print(svo)
        print([sub_lists, ob_lists])
        print(sent)
        print("-----------------")

        cw.writerow([i, index, verb, sent, label, [sub_lists, ob_lists]])
def convert_VUAverb_sent_svo_to_oxford_topic_k(source_file, target_file):
    import csv

    f = open(source_file, "r")
    ff = open(target_file, "a", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    TOP_K = 3
    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        if i > end:
            break

        svo = eval(row[5])
        sent = row[2]

        new_svo = []
        for kk, s in enumerate(svo):

            if kk == 0 or kk == 1:
                pos_s = get_top_k_noun(TOP_K, s)
            else:
                pos_s = [s]

            print("get top" + str(TOP_K) + ":", s, "->", pos_s)

            new_s = []
            for ss in pos_s:
                if if_people_pronoun(ss):
                    new_s.append("people")
                else:
                    new_s.append(ss)

            ns_list = []
            for ns in new_s:
                if (kk == 0 or kk == 1) and ns and ns != "people" and ns != "none" and ns != "-":
                    INDEX = 0
                    typer_list = []
                    while (True):
                        INDEX += 1
                        if INDEX > 50:
                            break
                        print("request the", INDEX)
                        try:
                            typer_list = get_topic_from_oxford_dir(ns)
                            break
                        except:
                            print("request error and try again")
                            time.sleep(3)
                    if typer_list:
                        print("hyper exist:", ns, "->", typer_list)
                        ns_list.append(typer_list)
                    else:
                        print("hyper is none:", ns, "->", "none&" + ns)
                        ns_list.append("none&" + ns)
                else:
                    ns_list.append(ns)

            new_svo.append(ns_list)
            print("new_s->ns_list:", new_s, "->", ns_list)

        print(svo)
        print(new_svo)
        print(sent)
        print("-----------------")

        cw.writerow([row[0], row[1], row[2], row[3], row[4], new_svo])



def MOX_deel_NoneType_k_in_synonyms_and_hyper(source_file, target_file):
    import csv

    f = open(source_file, "r", errors="ignore")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    basic_noun_TOP_K = 2
    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        if i > end:
            break

        svo = eval(row[5])
        assert len(svo) == 4
        sub_list = svo[0]
        ob_list = svo[1]
        adv_list = svo[2]
        pron_list = svo[3]

        if not isinstance(sub_list, list):
            sub_list = [sub_list]
        if not isinstance(ob_list, list):
            ob_list = [ob_list]

        new_sub_list = convert_old_by_add_basic_sense_and_oxford_topic(basic_noun_TOP_K, sub_list)
        new_ob_list = convert_old_by_add_basic_sense_and_oxford_topic(basic_noun_TOP_K, ob_list)

        print(sub_list)
        print(ob_list)
        print(new_sub_list)
        print(new_ob_list)
        print("-----------------")

        cw.writerow([row[0], row[1], row[2], row[3], row[4], [new_sub_list, new_ob_list, adv_list, pron_list]])
def MOX_deel_NoneType_k_in_oxford_topic(source_file, target_file):
    import csv

    f = open(source_file, "r", errors="ignore")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    basic_noun_TOP_K = 2
    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        if i > end:
            break

        svo = eval(row[5])
        assert len(svo) == 4
        sub_list = svo[0]
        ob_list = svo[1]
        adv_list = svo[2]
        pron_list = svo[3]

        if not isinstance(sub_list, list):
            sub_list = [sub_list]
        if not isinstance(ob_list, list):
            ob_list = [ob_list]

        new_sub_list = convert_old_by_add_basic_sense_and_oxford_topic(basic_noun_TOP_K, sub_list)
        new_ob_list = convert_old_by_add_basic_sense_and_oxford_topic(basic_noun_TOP_K, ob_list)

        print(sub_list)
        print(ob_list)
        print(new_sub_list)
        print(new_ob_list)
        print("-----------------")

        cw.writerow([row[0], row[1], row[2], row[3], row[4], [new_sub_list, new_ob_list, adv_list, pron_list]])
def TroFi_deel_NoneType_k_in_hypernyms(source_file, target_file):
    import csv

    f = open(source_file, "r")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    basic_noun_TOP_K = 2
    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        if i > end:
            break

        svo = eval(row[5])
        assert len(svo) == 4
        sub_list = svo[0]
        ob_list = svo[1]
        adv_list = svo[2]
        pron_list = svo[3]

        if not isinstance(sub_list, list):
            sub_list = [sub_list]
        if not isinstance(ob_list, list):
            ob_list = [ob_list]

        new_sub_list = convert_old_by_add_basic_sense_and_oxford_topic(basic_noun_TOP_K, sub_list)
        new_ob_list = convert_old_by_add_basic_sense_and_oxford_topic(basic_noun_TOP_K, ob_list)

        print(sub_list)
        print(ob_list)
        print(new_sub_list)
        print(new_ob_list)
        print("-----------------")

        cw.writerow([row[0], row[1], row[2], row[3], row[4], [new_sub_list, new_ob_list, adv_list, pron_list]])
def TroFi_deel_NoneType_k_in_oxford_topic(source_file, target_file):
    import csv

    f = open(source_file, "r", errors="ignore")
    ff = open(target_file, "w", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    basic_noun_TOP_K = 2
    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        if i > end:
            break

        svo = eval(row[5])
        assert len(svo) == 4
        sub_list = svo[0]
        ob_list = svo[1]
        adv_list = svo[2]
        pron_list = svo[3]

        if not isinstance(sub_list, list):
            sub_list = [sub_list]
        if not isinstance(ob_list, list):
            ob_list = [ob_list]

        new_sub_list = convert_old_by_add_basic_sense_and_oxford_topic(basic_noun_TOP_K, sub_list)
        new_ob_list = convert_old_by_add_basic_sense_and_oxford_topic(basic_noun_TOP_K, ob_list)

        print(sub_list)
        print(ob_list)
        print(new_sub_list)
        print(new_ob_list)
        print("-----------------")

        cw.writerow([row[0], row[1], row[2], row[3], row[4], [new_sub_list, new_ob_list, adv_list, pron_list]])
def VUAverb_deel_NoneType_k_in_oxford_topic(source_file, target_file):
    import csv

    f = open(source_file, "r", errors="ignore")
    ff = open(target_file, "a", newline="")

    cr = csv.reader(f)
    cw = csv.writer(ff)

    basic_noun_TOP_K = 2
    start = -1
    end = 10000

    for i, row in enumerate(cr):

        if i <= start:
            continue
        if i > end:
            break

        svo = eval(row[5])
        assert len(svo) == 2
        sub_list = svo[0]
        ob_list = svo[1]

        if not isinstance(sub_list, list):
            sub_list = [sub_list]
        if not isinstance(ob_list, list):
            ob_list = [ob_list]

        new_sub_list = convert_old_by_add_basic_sense_and_oxford_topic(basic_noun_TOP_K, sub_list)
        new_ob_list = convert_old_by_add_basic_sense_and_oxford_topic(basic_noun_TOP_K, ob_list)

        print(sub_list)
        print(ob_list)
        print(new_sub_list)
        print(new_ob_list)
        print("-----------------")

        cw.writerow([row[0], row[1], row[2], row[3], row[4], [new_sub_list, new_ob_list]])


def cal_gpt_label_acc(source_file):

    import csv
    f = open(source_file, "r")
    csv_reader = csv.reader(f)

    labels = []
    preds = []

    for row in csv_reader:
        true_label = row[4]
        pre_label = row[5]

        if "yes" in pre_label or "Yes" in pre_label or "YES" in pre_label:
            pre_label = 1
        elif "no" in pre_label or "No" in pre_label or "NO" in pre_label:
            pre_label = 0
        else:
            print("error - >", pre_label)
            continue

        labels.append(int(true_label))
        preds.append(int(pre_label))

    true_positives = sum(1 for t, p in zip(labels, preds) if t == p and t == 1)
    false_positives = sum(1 for t, p in zip(labels, preds) if t != p and t == 0)
    true_negatives = sum(1 for t, p in zip(labels, preds) if t == p and t == 0)
    false_negatives = sum(1 for t, p in zip(labels, preds) if t != p and t == 1)

    accuracy = (true_positives + true_negatives) / len(labels)
    recall = true_positives / (true_positives + false_negatives)
    precision = true_positives / (true_positives + false_positives)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print("Accuracy:", accuracy)
    print("Recall:", recall)
    print("Precision:", precision)
    print("F1 Score:", f1_score)


def MOX_judge_by_hypernyms(sent_file, verb_lists_file):

    import csv
    f1 = open(sent_file, "r")
    cr1 = csv.reader(f1)

    verb_sub_dir, verb_ob_dir = get_verb_dir_total(1000, verb_lists_file)

    preds = []
    labels = []

    error_len = 0

    for c1 in cr1:

        verb = c1[1]

        assert len(eval(c1[5])) == 4

        verb_sub = eval(c1[5])[0]
        verb_ob = eval(c1[5])[1]

        verb_sub = get_top_k_in_double_list(100, verb_sub)
        verb_ob = get_top_k_in_double_list(100, verb_ob)

        verb_sub_list = verb_sub_dir[verb]
        verb_ob_list = verb_ob_dir[verb]

        if_sub_literal = False
        if_ob_literal = False

        if SVO_not_none(verb_sub):
            if_sub_literal = list1_if_in_list22(verb_sub, verb_sub_list)

        if SVO_not_none(verb_ob):
            if_ob_literal = list1_if_in_list22(verb_ob, verb_ob_list)


        if SVO_not_none(verb_sub) and not SVO_not_none(verb_ob):
            if_literal = if_sub_literal
        elif not SVO_not_none(verb_sub) and SVO_not_none(verb_ob):
            if_literal = if_ob_literal
        elif not SVO_not_none(verb_sub) and not SVO_not_none(verb_ob):
            error_len += 1
            continue
        else:
            if_literal = if_sub_literal and if_ob_literal

        if_metaphor = not if_literal


        preds.append(int(if_metaphor))
        labels.append(int(c1[4]))

    true_positives = sum(1 for t, p in zip(labels, preds) if t == p and t == 1)
    false_positives = sum(1 for t, p in zip(labels, preds) if t != p and t == 0)
    true_negatives = sum(1 for t, p in zip(labels, preds) if t == p and t == 0)
    false_negatives = sum(1 for t, p in zip(labels, preds) if t != p and t == 1)


    accuracy = (true_positives + true_negatives) / len(labels)
    recall = true_positives / (true_positives + false_negatives)
    precision = true_positives / (true_positives + false_positives)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print("Accuracy:", accuracy)
    print("Recall:", recall)
    print("Precision:", precision)
    print("F1 Score:", f1_score)
    return round(f1_score, 3)
def Metaphor_judge_by_sym_and_hyper(sent_file, verb_lists_file):

    TOP_K = 10

    import csv
    f1 = open(sent_file, "r")
    cr1 = csv.reader(f1)
    f2 = open(verb_lists_file, "r")
    cr2 = csv.reader(f2)

    verb_sym_sub_dir = {}
    verb_sym_ob_dir = {}
    verb_hyper_sub_dir = {}
    verb_hyper_ob_dir = {}

    for c2 in cr2:

        verb = c2[0]
        # print(c2[1], c2[2])
        sym_subs = eval(c2[1])
        sym_obs = eval(c2[2])
        hyper_subs = eval(c2[3])
        hyper_obs = eval(c2[4])

        new_sym_subs = []
        for sub in sym_subs:
            sub = get_top_k_content(TOP_K, sub)
            new_sym_subs.append(sub)

        new_sym_obs = []
        for ob in sym_obs:
            ob = get_top_k_content(TOP_K, ob)
            new_sym_obs.append(ob)

        new_hyper_subs = []
        for sub in hyper_subs:
            sub = get_top_k_content(TOP_K, sub)
            new_hyper_subs.append(sub)

        new_hyper_obs = []
        for ob in hyper_obs:
            ob = get_top_k_content(TOP_K, ob)
            new_hyper_obs.append(ob)

        verb_sym_sub_dir[verb] = new_sym_subs
        verb_sym_ob_dir[verb] = new_sym_obs
        verb_hyper_sub_dir[verb] = new_hyper_subs
        verb_hyper_ob_dir[verb] = new_hyper_obs


    preds = []
    labels = []

    ttt = 0
    all = 0

    for c1 in cr1:

        verb = c1[1]

        assert len(eval(c1[5])) == 4

        verb_sym_sub = eval(c1[5])[0]
        verb_sym_ob = eval(c1[5])[1]
        verb_hyper_sub = eval(c1[6])[0]
        verb_hyper_ob = eval(c1[6])[1]


        verb_sym_sub = get_top_k_content(TOP_K, verb_sym_sub)
        verb_sym_ob = get_top_k_content(TOP_K, verb_sym_ob)
        verb_hyper_sub = get_top_k_content(TOP_K, verb_hyper_sub)
        verb_hyper_ob = get_top_k_content(TOP_K, verb_hyper_ob)

        sym_sub_list = verb_sym_sub_dir[verb]
        sym_ob_list = verb_sym_ob_dir[verb]
        hyper_sub_list = verb_hyper_sub_dir[verb]
        hyper_ob_list = verb_hyper_ob_dir[verb]

        if_sym_sub = False
        if_sym_ob = False
        if_hyper_sub = False
        if_hyper_ob = False

        if verb_hyper_sub != "none":
            if_hyper_sub = list1_if_in_list2(verb_hyper_sub, hyper_sub_list)

        if verb_hyper_ob != "none":
            if_hyper_ob = list1_if_in_list2(verb_hyper_ob, hyper_ob_list)

        if verb_sym_sub != "none":
            if_sym_sub = list1_if_in_list2(verb_sym_sub, sym_sub_list)

        if verb_sym_ob != "none":
            if_sym_ob = list1_if_in_list2(verb_sym_ob, sym_ob_list)


        if verb_hyper_sub == "none" and verb_hyper_ob != "none":
            if_literal = if_hyper_ob or if_sym_ob
        elif verb_hyper_sub != "none" and verb_hyper_ob == "none":
            if_literal = if_hyper_sub or if_sym_sub
        else:
            if_literal = (if_hyper_sub or if_sym_sub) and (if_hyper_ob or if_sym_ob)

        if_metaphor = not if_literal


        if int(c1[4]):
            print(verb, c1[2], if_metaphor, c1[4])
            if int(if_metaphor) == int(c1[4]):
                ttt += 1
            all += 1

        preds.append(int(if_metaphor))
        labels.append(int(c1[4]))

    print(ttt, all)


    true_positives = sum(1 for t, p in zip(labels, preds) if t == p and t == 1)
    false_positives = sum(1 for t, p in zip(labels, preds) if t != p and t == 0)
    true_negatives = sum(1 for t, p in zip(labels, preds) if t == p and t == 0)
    false_negatives = sum(1 for t, p in zip(labels, preds) if t != p and t == 1)


    accuracy = (true_positives + true_negatives) / len(labels)
    recall = true_positives / (true_positives + false_negatives)
    precision = true_positives / (true_positives + false_positives)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print("Accuracy:", accuracy)
    print("Recall:", recall)
    print("Precision:", precision)
    print("F1 Score:", f1_score)


def MOX_judge_by_oxford_topic(k1, k2, sent_file, verb_lists_file):

    import csv
    f1 = open(sent_file, "r", errors="ignore")
    cr1 = csv.reader(f1)

    verb_sub_dir, verb_ob_dir = get_verb_dir(k1, verb_lists_file)

    preds = []
    labels = []

    error_len = 0

    for c1 in cr1:

        verb = c1[1]

        assert len(eval(c1[5])) == 4

        verb_sub = eval(c1[5])[0]
        verb_ob = eval(c1[5])[1]

        verb_sub = get_top_k_in_double_list(k2, verb_sub)
        verb_ob = get_top_k_in_double_list(k2, verb_ob)

        verb_sub_list = verb_sub_dir[verb]
        verb_ob_list = verb_ob_dir[verb]

        if_sub_literal = False
        if_ob_literal = False

        if SVO_not_none(verb_sub):
            if_sub_literal = list1_if_in_list22(verb_sub, verb_sub_list)

        if SVO_not_none(verb_ob):
            if_ob_literal = list1_if_in_list22(verb_ob, verb_ob_list)


        if SVO_not_none(verb_sub) and not SVO_not_none(verb_ob):
            if_literal = if_sub_literal
        elif not SVO_not_none(verb_sub) and SVO_not_none(verb_ob):
            if_literal = if_ob_literal
        elif not SVO_not_none(verb_sub) and not SVO_not_none(verb_ob):
            error_len += 1
            continue
        else:
            if_literal = if_sub_literal and if_ob_literal

        if_metaphor = not if_literal


        preds.append(int(if_metaphor))
        labels.append(int(c1[4]))



    true_positives = sum(1 for t, p in zip(labels, preds) if t == p and t == 1)
    false_positives = sum(1 for t, p in zip(labels, preds) if t != p and t == 0)
    true_negatives = sum(1 for t, p in zip(labels, preds) if t == p and t == 0)
    false_negatives = sum(1 for t, p in zip(labels, preds) if t != p and t == 1)


    accuracy = (true_positives + true_negatives) / len(labels)
    recall = true_positives / (true_positives + false_negatives)
    precision = true_positives / (true_positives + false_positives)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(k1, k2)
    print("Accuracy:", accuracy)
    print("Recall:", recall)
    print("Precision:", precision)
    print("F1 Score:", f1_score)
    return round(f1_score, 3)
def MOX_judge_by_oxford_topic_k(k1, k2, sent_file, verb_lists_file):

    import csv
    f1 = open(sent_file, "r", errors="ignore")
    cr1 = csv.reader(f1)

    verb_sub_dir, verb_ob_dir = get_verb_dir(k1, verb_lists_file)

    preds = []
    labels = []

    for i, c1 in enumerate(cr1):

        verb = c1[1]

        assert len(eval(c1[5])) == 4
        verb_sub = eval(c1[5])[0]
        verb_ob = eval(c1[5])[1]

        verb_sub = get_top_k_in_double_list(k2, verb_sub)
        verb_ob = get_top_k_in_double_list(k2, verb_ob)

        verb_sub_list = verb_sub_dir[verb]
        verb_ob_list = verb_ob_dir[verb]

        if_sub_literal = False
        if_ob_literal = False


        if SVO_not_none(verb_sub):
            if_sub_literal = list1_if_in_list22(verb_sub, verb_sub_list)
        if SVO_not_none(verb_ob):
            if_ob_literal = list1_if_in_list22(verb_ob, verb_ob_list)


        if SVO_not_none(verb_sub) and not SVO_not_none(verb_ob):
            if_literal = if_sub_literal
        elif not SVO_not_none(verb_sub) and SVO_not_none(verb_ob):
            if_literal = if_ob_literal
        elif not SVO_not_none(verb_sub) and not SVO_not_none(verb_ob):
            continue
        else:
            if_literal = if_sub_literal and if_ob_literal

        if_metaphor = not if_literal


        preds.append(int(if_metaphor))
        labels.append(int(c1[4]))



    true_positives = sum(1 for t, p in zip(labels, preds) if t == p and t == 1)
    false_positives = sum(1 for t, p in zip(labels, preds) if t != p and t == 0)
    true_negatives = sum(1 for t, p in zip(labels, preds) if t == p and t == 0)
    false_negatives = sum(1 for t, p in zip(labels, preds) if t != p and t == 1)


    accuracy = (true_positives + true_negatives) / len(labels)
    recall = true_positives / (true_positives + false_negatives)
    precision = true_positives / (true_positives + false_positives)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(k1, k2)
    print("Accuracy:", accuracy)
    print("Recall:", recall)
    print("Precision:", precision)
    print("F1 Score:", f1_score)
def TroFi_judge_by_wn_topic(k1, k2, sent_file, verb_lists_file):

    import csv
    f1 = open(sent_file, "r", errors="ignore")
    cr1 = csv.reader(f1)

    verb_sub_dir, verb_ob_dir = get_verb_dir(k1, verb_lists_file)

    preds = []
    labels = []


    for c1 in cr1:

        verb = c1[1]

        assert len(eval(c1[5])) == 4

        verb_sub = eval(c1[5])[0]
        verb_ob = eval(c1[5])[1]

        verb_sub = get_top_k_in_double_list2(k2, verb_sub)
        verb_ob = get_top_k_in_double_list2(k2, verb_ob)

        verb_sub_list = verb_sub_dir[verb]
        verb_ob_list = verb_ob_dir[verb]

        if_sub_literal = False
        if_ob_literal = False

        if SVO_not_none(verb_sub):
            if_sub_literal = list1_if_in_list22(verb_sub, verb_sub_list)

        if SVO_not_none(verb_ob):
            if_ob_literal = list1_if_in_list22(verb_ob, verb_ob_list)


        if SVO_not_none(verb_sub) and not SVO_not_none(verb_ob):
            if_literal = if_sub_literal
        elif not SVO_not_none(verb_sub) and SVO_not_none(verb_ob):
            if_literal = if_ob_literal
        elif not SVO_not_none(verb_sub) and not SVO_not_none(verb_ob):
            continue
        else:
            if_literal = if_sub_literal and if_ob_literal

        if_metaphor = not if_literal

        preds.append(int(if_metaphor))
        labels.append(int(c1[4]))

    true_positives = sum(1 for t, p in zip(labels, preds) if t == p and t == 1)
    false_positives = sum(1 for t, p in zip(labels, preds) if t != p and t == 0)
    true_negatives = sum(1 for t, p in zip(labels, preds) if t == p and t == 0)
    false_negatives = sum(1 for t, p in zip(labels, preds) if t != p and t == 1)

    accuracy = (true_positives + true_negatives) / len(labels)
    recall = true_positives / (true_positives + false_negatives)
    precision = true_positives / (true_positives + false_positives)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(k1, k2)
    print("Accuracy:", accuracy)
    print("Recall:", recall)
    print("Precision:", precision)
    print("F1 Score:", f1_score)
def TroFi_judge_by_wn_topic_k(k1, k2, sent_file, verb_lists_file):

    import csv
    f1 = open(sent_file, "r", errors="ignore")
    cr1 = csv.reader(f1)

    verb_sub_dir, verb_ob_dir = get_verb_dir(k1, verb_lists_file)

    preds = []
    labels = []


    for c1 in cr1:

        verb = c1[1]

        assert len(eval(c1[5])) == 4

        verb_sub = eval(c1[5])[0]
        verb_ob = eval(c1[5])[1]

        verb_sub = get_top_k_in_double_list(k2, verb_sub)
        verb_ob = get_top_k_in_double_list(k2, verb_ob)

        verb_sub_list = verb_sub_dir[verb]
        verb_ob_list = verb_ob_dir[verb]

        if_sub_literal = False
        if_ob_literal = False

        if verb_sub[0] != "none":
            if_sub_literal = list1_if_in_list22(verb_sub, verb_sub_list)

        if verb_ob[0] != "none":
            if_ob_literal = list1_if_in_list22(verb_ob, verb_ob_list)


        if verb_sub[0] != "none" and verb_ob[0] == "none":
            if_literal = if_sub_literal
        elif verb_sub[0] == "none" and verb_ob[0] != "none":
            if_literal = if_ob_literal
        else:
            if_literal = if_sub_literal and if_ob_literal

        if_metaphor = not if_literal

        preds.append(int(if_metaphor))
        labels.append(int(c1[4]))



    true_positives = sum(1 for t, p in zip(labels, preds) if t == p and t == 1)
    false_positives = sum(1 for t, p in zip(labels, preds) if t != p and t == 0)
    true_negatives = sum(1 for t, p in zip(labels, preds) if t == p and t == 0)
    false_negatives = sum(1 for t, p in zip(labels, preds) if t != p and t == 1)


    accuracy = (true_positives + true_negatives) / len(labels)
    recall = true_positives / (true_positives + false_negatives)
    precision = true_positives / (true_positives + false_positives)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(k1, k2)
    print("Accuracy:", accuracy)
    print("Recall:", recall)
    print("Precision:", precision)
    print("F1 Score:", f1_score)
def TroFi_judge_by_oxford_topic(k1, k2, sent_file, verb_lists_file):
    import csv
    f1 = open(sent_file, "r", errors="ignore")
    cr1 = csv.reader(f1)

    verb_sub_dir, verb_ob_dir = get_verb_dir(k1, verb_lists_file)

    preds = []
    labels = []

    for c1 in cr1:

        verb = c1[1]

        assert len(eval(c1[5])) == 4

        verb_sub = eval(c1[5])[0]
        verb_ob = eval(c1[5])[1]

        verb_sub = get_top_k_content(k2, verb_sub)
        verb_ob = get_top_k_content(k2, verb_ob)

        verb_sub_list = verb_sub_dir[verb]
        verb_ob_list = verb_ob_dir[verb]

        if_sub_literal = False
        if_ob_literal = False

        if verb_sub[0] != "none":
            if_sub_literal = list1_if_in_list22(verb_sub, verb_sub_list)

        if verb_ob[0] != "none":
            if_ob_literal = list1_if_in_list22(verb_ob, verb_ob_list)

        if verb_sub[0] != "none" and verb_ob[0] == "none":
            if_literal = if_sub_literal
        elif verb_sub[0] == "none" and verb_ob[0] != "none":
            if_literal = if_ob_literal
        else:
            if_literal = if_sub_literal and if_ob_literal

        if_metaphor = not if_literal



        preds.append(int(if_metaphor))
        labels.append(int(c1[4]))

    true_positives = sum(1 for t, p in zip(labels, preds) if t == p and t == 1)
    false_positives = sum(1 for t, p in zip(labels, preds) if t != p and t == 0)
    true_negatives = sum(1 for t, p in zip(labels, preds) if t == p and t == 0)
    false_negatives = sum(1 for t, p in zip(labels, preds) if t != p and t == 1)

    accuracy = (true_positives + true_negatives) / len(labels)
    recall = true_positives / (true_positives + false_negatives)
    precision = true_positives / (true_positives + false_positives)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(k1, k2)
    print("Accuracy:", accuracy)
    print("Recall:", recall)
    print("Precision:", precision)
    print("F1 Score:", f1_score)

    return f1_score
def TroFi_judge_by_oxford_topic_k(k1, k2, sent_file, verb_lists_file):
    import csv
    f1 = open(sent_file, "r")
    cr1 = csv.reader(f1)

    verb_sub_dir, verb_ob_dir = get_verb_dir(k1, verb_lists_file)

    preds = []
    labels = []

    for c1 in cr1:

        verb = c1[1]

        try:
            assert len(eval(c1[5])) == 4
        except:
            continue

        verb_sub = eval(c1[5])[0]
        verb_ob = eval(c1[5])[1]

        verb_sub = get_top_k_in_double_list(k2, verb_sub)
        verb_ob = get_top_k_in_double_list(k2, verb_ob)

        verb_sub_list = verb_sub_dir[verb]
        verb_ob_list = verb_ob_dir[verb]

        if_sub_literal = False
        if_ob_literal = False

        if verb_sub[0] != "none":
            if_sub_literal = list1_if_in_list22(verb_sub, verb_sub_list)

        if verb_ob[0] != "none":
            if_ob_literal = list1_if_in_list22(verb_ob, verb_ob_list)


        if verb_sub[0] != "none" and verb_ob[0] == "none":
            if_literal = if_sub_literal
        elif verb_sub[0] == "none" and verb_ob[0] != "none":
            if_literal = if_ob_literal
        else:
            if_literal = if_sub_literal and if_ob_literal

        if_metaphor = not if_literal

        preds.append(int(if_metaphor))
        labels.append(int(c1[4]))

    true_positives = sum(1 for t, p in zip(labels, preds) if t == p and t == 1)
    false_positives = sum(1 for t, p in zip(labels, preds) if t != p and t == 0)
    true_negatives = sum(1 for t, p in zip(labels, preds) if t == p and t == 0)
    false_negatives = sum(1 for t, p in zip(labels, preds) if t != p and t == 1)

    accuracy = (true_positives + true_negatives) / len(labels)
    recall = true_positives / (true_positives + false_negatives)
    precision = true_positives / (true_positives + false_positives)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(k1, k2)
    print("Accuracy:", accuracy)
    print("Recall:", recall)
    print("Precision:", precision)
    print("F1 Score:", f1_score)
def VUAverb_judge_by_topic_k(k1, k2, sent_file, verb_lists_file):

    import csv
    import copy

    f1 = open(sent_file, "r", errors="ignore")
    cr1 = csv.reader(f1)

    verb_sub_dir, verb_ob_dir = get_verb_dir(k1, verb_lists_file)

    preds = []
    labels = []

    error_len = 0

    for c1 in cr1:

        verb = c1[1]

        try:
            assert len(eval(c1[5])) == 2
        except:
            continue

        verb_sub = eval(c1[5])[0]
        verb_ob = eval(c1[5])[1]

        verb_sub = get_top_k_in_double_list(k2, verb_sub)
        verb_ob = get_top_k_in_double_list(k2, verb_ob)

        new_verb_sub = []
        new_verb_ob = []

        for vs in verb_sub:
            if len(vs.split("&")) > 1 and vs.split("&")[0] == "none":
                continue
            else:
                new_verb_sub.append(vs)

        for vo in verb_ob:
            if len(vo.split("&")) > 1 and vo.split("&")[0] == "none":
                continue
            else:
                new_verb_ob.append(vo)

        verb_sub = copy.deepcopy(new_verb_sub)
        verb_ob = copy.deepcopy(new_verb_ob)

        verb_sub_list = verb_sub_dir[verb]
        verb_ob_list = verb_ob_dir[verb]

        if_sub_literal = False
        if_ob_literal = False

        if SVO_not_none(verb_sub):
            if_sub_literal = list1_if_in_list22(verb_sub, verb_sub_list)
            # print("sub", if_sub_literal, label, verb_sub, verb_sub_list)

        if SVO_not_none(verb_ob):
            if_ob_literal = list1_if_in_list22(verb_ob, verb_ob_list)
            # print("ob", if_ob_literal, label, verb_ob, verb_ob_list)


        if SVO_not_none(verb_sub) and not SVO_not_none(verb_ob):
            if_literal = if_sub_literal
        elif not SVO_not_none(verb_sub) and SVO_not_none(verb_ob):
            if_literal = if_ob_literal
        elif not SVO_not_none(verb_sub) and not SVO_not_none(verb_ob):
            error_len += 1
        else:
            if_literal = if_sub_literal and if_ob_literal


        if_metaphor = not if_literal

        preds.append(int(if_metaphor))
        labels.append(int(c1[4]))

    true_positives = sum(1 for t, p in zip(labels, preds) if t == p and t == 1)
    false_positives = sum(1 for t, p in zip(labels, preds) if t != p and t == 0)
    true_negatives = sum(1 for t, p in zip(labels, preds) if t == p and t == 0)
    false_negatives = sum(1 for t, p in zip(labels, preds) if t != p and t == 1)

    accuracy = (true_positives + true_negatives) / len(labels)
    recall = true_positives / (true_positives + false_negatives)
    precision = true_positives / (true_positives + false_positives)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(k1, k2)
    print("Accuracy:", accuracy)
    print("Recall:", recall)
    print("Precision:", precision)
    print("F1 Score:", f1_score)




def plant_k1_k2():
    import numpy as np
    import matplotlib.pyplot as plt

    data = [
        [0.661, 0.665, 0.665, 0.666, 0.666, 0.666, 0.666, 0.666, 0.666],
        [0.666, 0.671, 0.67, 0.672, 0.672, 0.672, 0.672, 0.672, 0.672],
        [0.672, 0.672, 0.679, 0.676, 0.679, 0.679, 0.679, 0.676, 0.677],
        [0.677, 0.68, 0.682, 0.68, 0.68, 0.678, 0.68, 0.676, 0.677],
        [0.677, 0.685, 0.692, 0.684, 0.681, 0.679, 0.682, 0.678, 0.678],
        [0.679, 0.689, 0.698, 0.69, 0.686, 0.683, 0.686, 0.682, 0.683],
        [0.684, 0.686, 0.695, 0.688, 0.684, 0.681, 0.684, 0.68, 0.68],
        [0.681, 0.686, 0.697, 0.692, 0.689, 0.686, 0.686, 0.682, 0.682],
        [0.682, 0.689, 0.701, 0.694, 0.689, 0.687, 0.686, 0.682, 0.683]
    ]

    plt.figure(figsize=(6, 4))
    plt.imshow(data, cmap='YlGnBu', aspect='auto', interpolation='bilinear')

    plt.gca().invert_yaxis()

    x_labels = [str(i) for i in range(1, 10)]
    y_labels = [str(i) for i in range(1, 10)]
    plt.xticks(np.arange(9), x_labels)
    plt.yticks(np.arange(9), y_labels)

    plt.xlabel(r'$\bf{k2}$', fontsize=15)
    plt.ylabel(r'$\bf{k1}$', fontsize=15)

    cbar = plt.colorbar()
    cbar.set_label(r'$\bf{f1 score}$', rotation=270, labelpad=15, fontsize=12)

    plt.savefig('heatmap.pdf', format='pdf', bbox_inches='tight')
    plt.show()




def get_llama2():
    from transformers import AutoTokenizer
    import transformers
    import torch

    model = "meta-llama/Llama-2-7b-chat-hf"

    tokenizer = AutoTokenizer.from_pretrained(model)
    pipeline = transformers.pipeline(
        "text-generation",
        model=model,
        torch_dtype=torch.float16,
        device_map="auto",
    )

    return tokenizer, pipeline
def Add_Subject_and_Object_by_llama2(source_file, target_file):

    import csv

    tokenizer, pipeline = get_llama2()

    start = -1
    end = 10000

    with open(source_file, 'r') as source, \
            open(target_file, 'w', newline='') as new_csv:

        verb_list = eval(source.read())
        csv_writer = csv.writer(new_csv)

        for i, verb in enumerate(verb_list):

            if i <= start:
                continue
            if i > end:
                break

            content = "Please provide as many examples as possible of subject and object subject categories that go with the verb " + verb + " in non-metaphorical or literal usage. Format: Subject Categories:\n1.\n2.\n Object Categories:\n1.\n2."
            print(content)

            sequences = pipeline(
                content,
                do_sample=True,
                top_k=10,
                num_return_sequences=1,
                eos_token_id=tokenizer.eos_token_id,
                max_length=200,
            )

            sequences = sequences[0]['generated_text']

            print("--------------------------------------------")
            print()
            print()
            print("output:", sequences)


            csv_writer.writerow([i, verb, sequences])
            print(i, "has been written")