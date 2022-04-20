"""
Kora S. Hughes
Blackout Poetry Project

The purpose of this project is to create poetry with a posative message out of hateful things

The origin of this idea stemmed from making a series of blackout poetry pieces
transcribing famous poems from transgender poets out of JK Rowling's transphobic tweets

In the future:
-I'd love to expand this to cover a wider range of topics
-conjure more examples of blackout pieces
-create automated ways of visualizing the blackout pieces instead of just links
-format my code into a poetry piece of its own (since variables can be named anything, I can put comments anywhere, and lots of expressions in python are more or less english, I figured I could make a poem given the code's restrictions)
"""

# text coloration for testing
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Test Data -> dict collections with link:text structure
jk_trans_tweets = {
    "https://twitter.com/jk_rowling/status/1269382518362509313?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1269382518362509313%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.glamour.com%2Fstory%2Fa-complete-breakdown-of-the-jk-rowling-transgender-comments-controversy":"‘People who menstruate.’ I’m sure there used to be a word for those people. Someone help me out. Wumben? Wimpund? Woomud? Opinion: Creating a more equal post-COVID-19 world for people who menstruate",
    "https://twitter.com/jk_rowling/status/1269389298664701952?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1269389298664701952%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.glamour.com%2Fstory%2Fa-complete-breakdown-of-the-jk-rowling-transgender-comments-controversy":"If sex isn’t real, there’s no same-sex attraction. If sex isn’t real, the lived reality of women globally is erased. I know and love trans people, but erasing the concept of sex removes the ability of many to meaningfully discuss their lives. It isn’t hate to speak the truth.",
    "https://twitter.com/jk_rowling/status/1269406094595588096?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1269406094595588096%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.glamour.com%2Fstory%2Fa-complete-breakdown-of-the-jk-rowling-transgender-comments-controversy":"The idea that women like me, who’ve been empathetic to trans people for decades, feeling kinship because they’re vulnerable in the same way as women - ie, to male violence - ‘hate’ trans people because they think sex is real and has lived consequences - is a nonsense.",
    "https://twitter.com/jk_rowling/status/1269407862234775552?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1269407862234775552%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.glamour.com%2Fstory%2Fa-complete-breakdown-of-the-jk-rowling-transgender-comments-controversy":"I respect every trans person’s right to live any way that feels authentic and comfortable to them. I’d march with you if you were discriminated against on the basis of being trans. At the same time, my life has been shaped by being female. I do not believe it’s hateful to say so.",
    "https://twitter.com/jk_rowling/status/1269409838318182401?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1269409838318182401%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.glamour.com%2Fstory%2Fa-complete-breakdown-of-the-jk-rowling-transgender-comments-controversy":"I've never felt as shouted down, ignored, and targeted as a lesbian *within* our supposed GLBT community as I have over the past couple of years."
} # primary src: https://www.glamour.com/story/a-complete-breakdown-of-the-jk-rowling-transgender-comments-controversy
# secondary src: https://twitter.com/jk_rowling?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor

poem_citation = "Day, M. (2014). Batter My Heart, Transgender’d God. Retrieved from https://poets.org/poem/batter-my-heart-transgenderd-god. "
artist_poem = "Batter my heart, transgender’d god, for yours is the only ear that hears: place fear in my heart where faith has grown my senses dull & reassures my blood that it will never spill. Show every part to every stranger’s anger, surprise them with my drawers full up of maps that lead to vacancies & chart the distance from my pride, my core. Terror, do not depart but nest in the hollows of my loins & keep me on all fours. My knees, bring me to them; force my head to bow again. Replay the murders of my kin until my mind’s made new; let Adam’s bite obstruct my breath ’til I respire men & press his rib against my throat until my lips turn blue. You, O duo, O twin, whose likeness is kind: unwind my confidence & noose it round your fist so I might know you in vivid impermanence."


# helper methods
def find_word_by_letter(word, src):
    """ find a word, letter by letter in a given src """
    assert len(word) > 0
    i = 0
    letter = word[i]
    for j, src_letter in enumerate(src):
        if src_letter == letter:
            i += 1
            if i == len(word):
                return True
            letter = word[i]
    return False


# main code
def main():
    print(bcolors.HEADER + "\nFinding words that occur in various sources...\n" + bcolors.ENDC)
    curr_data = jk_trans_tweets

    poem_words = artist_poem.lower().replace("?","").replace("&", "and").replace("!","").replace(".","").replace(",","").replace(")","").replace("(","").replace(":","").replace(";","").replace("’","").split(" ")
    if "" in poem_words:
        poem_words.remove("")
    print("poem in question:", poem_words, "\n")

    # tests
    assert find_word_by_letter("hello","uajheaalasbjlaso")
    assert not find_word_by_letter("hello", "ollehsm")

    # actual code
    output = {}
    for link, text in curr_data.items():
        words_found = []
        for word in poem_words:
            if word in text.lower():
                words_found.append("*")  # word in src
            elif find_word_by_letter(word, text):
                words_found.append("l")  # word piecemeal in src
            else:
                words_found.append("-")  # word not in src
        # print("In link", link, "\nfound:", words_found, "\n")
        output[link] = words_found

    # find best result
    print(bcolors.HEADER + "calculating...\n\n" + bcolors.ENDC)
    final_result = []
    for i in range(len(poem_words)):
        found_lst = []  # list of kinds of values found per word
        for lst  in output.values():
            found_lst.append(lst[i])
        # print("Found List:", found_lst)
        if "*" in found_lst:
            for link, lst in output.items():
                if lst[i] == "*":
                    final_result.append((link, "*"))
                    break
        elif "l" in found_lst:
            for link, lst in output.items():
                if lst[i] == "l":
                    final_result.append((link, "l"))
                    break
        else:
            assert found_lst == (["-"]*len(curr_data.keys()))  # saftey check
            final_result.append(("", "-"))
            print(bcolors.FAIL + "****Word #" + str(i) + " (" + poem_words[i] + ") not found in sources"  + bcolors.ENDC)
        print(bcolors.OKBLUE + poem_words[i] + bcolors.ENDC + " (" +final_result[-1][1] + ") =>\n" + final_result[-1][0] + "\n")

if __name__ == "__main__":
    main()