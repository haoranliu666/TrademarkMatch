# Clean Name

| Raw data     | CRSP    | COMPUSTAT | CIQ     | TMA_assignor | TMA_assignee | TMC        |
| ------------ | ------- | --------- | ------- | ------------ | ------------ | ---------- |
| Observations | 106,249 | 40,221    | 725,373 | 1,170,748    | 1,116,051    | 22,135,386 |

## Pre-clean [(link)](https://github.com/FutureMathematician/TrademarkMatch/tree/main/Clean_name/Pre_clean)

> Purpose: provide unique raw company names, and assign each unique name a unique id, for the relink process afterward.

1. Get raw data: Compustat, CRSP, Capital IQ(CIQ), Trademark Assignor(TMA) assignor and assignee, Trademark Case File(TMC);
2. Drop duplicated name, and assign unique id;
3. For TMA and TMC, remove individual owner and companies outside US and CA;
4. Heath and Mace matched Trademark Case File to Compustat. We confirm his match result and dorp his matched names from TMC, TMA_assignor, and TMA assignee.
5. Own type cd greater than 40 is a sign of sold trademark, we can drop them.

| After Pre-clean | COMPUSTAT | CRSP   | CIQ     | TMA_assignor | TMA_assignee | TMC       |
| --------------- | --------- | ------ | ------- | ------------ | ------------ | --------- |
| Observations    | 40,220    | 41,812 | 700,632 | 537,327      | 446,377      | 2,554,580 |
| Dropped HM      |           |        |         | 520,141      | 424,163      | 2,499,201 |
| Dropped HM, >40 |           |        |         |              |              | 2,457,858 |

## Clean [(link)](https://github.com/FutureMathematician/TrademarkMatch/tree/main/Clean_name/Clean)

> Purpose: clean each data name for better Bing search result.

1. Change names to lower case;
   - !!!Manic Salamander, Inc.
   - !!!manic salamander, inc.

2. Replace ., to space;

- accurate casting co., inc.

- accurate casting co  inc.

3. Replacce x.y.z to xyz.;

- regency publishing group, l.l.c.
- regency publishing group, llc.

4. Map absurd characters using a dictionary [(link)](https://github.com/FutureMathematician/TrademarkMatch/blob/main/Clean_name/Clean/dict_char_replace.json);

- most of the absurd characters are european characters, they are in a unicode form, which cannot produce proper result in search engine, for example "\u00fc":

  <img src="https://tva1.sinaimg.cn/large/e6c9d24egy1gojekka5gtj21c00u01kx.jpg" alt="截屏2021-03-11 23.46.43" style="zoom: 50%;" />

- I'll look it up and find what it is, and find the best replacement solution for it, add the soultion to a dictionary:

  - According to wikipedia, "\u00fc" is Ü, and it can be replaced using U or UE;

    <img src="https://tva1.sinaimg.cn/large/e6c9d24egy1gojeoiy56qj21ts0mw4kp.jpg" alt="截屏2021-03-11 23.46.21" style="zoom:33%;" />

  - I'll take the original company name, and replace "\u00fc" to U, UE, or maybe V:

    <img src="https://tva1.sinaimg.cn/large/e6c9d24egy1gojeto644rj21eo0lwncc.jpg" alt="截屏2021-03-11 23.45.52" style="zoom:33%;" />

    <img src="https://tva1.sinaimg.cn/large/e6c9d24egy1gojetmozdaj217y0lsq7f.jpg" alt="截屏2021-03-11 23.45.58" style="zoom:33%;" />

    <img src="https://tva1.sinaimg.cn/large/e6c9d24egy1gojetl4pvrj218o0pktqa.jpg" alt="截屏2021-03-11 23.46.04" style="zoom:33%;" />

  - Turns out UE can produce the best result, and I'll add it to the dictionary.

    <img src="https://tva1.sinaimg.cn/large/e6c9d24egy1gojexej5u9j20h00xaaek.jpg" alt="截屏2021-03-14 14.20.53" style="zoom:33%;" />

  - Sometimes, the abusrd characters are actually ™ ® © or € ¥

    <img src="https://tva1.sinaimg.cn/large/e6c9d24egy1gojexmlq9gj20cy0g6q4e.jpg" alt="截屏2021-03-14 14.21.04" style="zoom:33%;" />

    

5. Replace . to space in the middle of the name to keep .com, .net;

- the trustee of the michaels trust  as patrica j. michaels  a u. s. citize
- the trustee of the michaels trust  as patrica j michaels  a u s citizen

6. Replace 'inc', 'co' and so on, it's better to just show the code:

```python
    name0 = name0.replace('.ltd.', ' ltd ')
    name0 = name0.replace('.ltd', ' ltd ')
    name0 = name0.replace('ltd.', ' ltd ')
    name0 = name0.replace('.limited', ' ltd ')
    name0 = name0.replace('.inc.', ' inc ')
    name0 = name0.replace('.inc', ' inc ')
    name0 = name0.replace('inc.', ' inc ')
    name0 = name0.replace('incorporated', ' inc ')
    name0 = name0.replace('incorporation', ' inc ')
    name0 = name0.replace('.co', ' co ')
    name0 = name0.replace('co.', ' co ')
    name0 = name0.replace('company', ' co ')
    name0 = name0.replace('.llc', ' llc ')
    name0 = name0.replace('llc.', ' llc ')
    name0 = name0.replace('corp.', ' corp ')
    name0 = name0.replace('.corp', ' corp ')
    name0 = name0.replace('.corporation', ' corp ')
    name0 = name0.replace('corporation', ' corp ')
```

7. Replace limited at the end of the name to ltd, not in the middle;

8. Clean extra white space;

- consolidated  business  systems   inc
- consolidated business systems inc

9. Take care of u s, u s a;

- wolff communications u s a inc
- wolff communications usa inc

10. For TMA and TMC, remove wrong names which contain "a corp... of...";

- ho-chunk, inc., a corporation organizedunder the laws of the winnebago tribe of nebraska, a federally-recognized indian tribe, which has adopted and is using the mark for specific classes of services as indicated herein through its related company
- ho-chunk, inc.,


| After Clean     | COMPUSTAT | CRSP   | CIQ     | TMA_assignor | TMA_assignee | TMC       | Total     |
| --------------- | --------- | ------ | ------- | ------------ | ------------ | --------- | --------- |
| Observations    | 40,204    | 41,799 | 698,695 | 509,103      | 422,415      | 2,085,101 | 3,013,094 |
| Dropped HM      |           |        |         | 495,565      | 403,248      | 2,064,771 | 3,005,901 |
| Dropped HM, >40 |           |        |         |              |              | 2,041,898 | 2,998,636 |

## Post-clean [(link)](https://github.com/FutureMathematician/TrademarkMatch/tree/main/Clean_name/Post_clean)

> Purpose: reduce duplication in cleaned names of TMA & TMC

### Introduction

We have a set of company names, and some of them are certainly the same company, for the most of the time, there are four different situations, or the mix of them:

1. Different order, like 
   - conard pyle co the
   - the conard pyle co
2. Spliting, like 
   - lamarick beauty products inc
   - la marick beauty products inc
3. Miss spelling, like
   - jean philippe frangrances inc
   - jean phillippe frangrances inc
4. Different suffix, like
   - lions gate entertainment corp
   - lions gate entertainment inc

How can we deal with these situtations conveniently?  An intuitive way is to define a distence between two company names, and we could make a big matrix, each row or a column represents a single company name from one dataset, let's say TMC, and the number in the matrix is the distance between the two company names. This will be a diagonal matrix and we can match two names if their distance is above a threshold, let's say distance > 0.9. The only thing we need is the definition of the distance between two company names, which are two strings.

Luckly, computer scientists have already came up with some distances, and the most popular and classic ones are [Levenshtein(1965)](https://en.wikipedia.org/wiki/Levenshtein_distance) and [Jaro-Winkler(1990)](https://en.wikipedia.org/wiki/Jaro–Winkler_distance) distance. And a new approach called [Term frequency - Inverse Document Frequency(2001)](https://en.wikipedia.org/wiki/Tf–idf) can also deal with this situation.

### Levenshtein distance

This distance is pretty intuitive, it counts how many time we need to edit one string, to become another string. The term 'edit' includes insertions, deletions or substitutions.

For example below, the distances between **a** with **b**, **c**, **d** string, are all 1.

- **a** = Haoran Liu Inc
- **b** = HaoranLiu Inc
- **c** = Haoran Li Inc
- **d** = Haoran Lim Inc

But the distance is not good enough, because Levenshtein distance between **e** and f also have distance 1, yet this pair looks much more similiar than the last pairs.

- **e** = Guangdong Guangzhou Sun Yat-sun University Haoran Liu Inc
- **f** = Guangdong Guangzhou Sun Yat-sun University Haoran Li Inc

We can simply define a new distance, to make the longer strings more similiar. The sqrtare root is for making the numerator and denominator the same unit.
$$
d(a, b) = \frac{Levenshtein(a, b)}{\sqrt{length(a)*length(b)}}
$$


### Jaro–Winkler distance

This is a pretty complicated distance. Generally, this distance has already dealt with the length of the strings, and another important thing is it gives a higher weight at the beginning of the string. a has a closer distance whih b than c.

- a = Haoran Liu
- b = Haoran Lim
- c = Baoran Liu

> textdistance.jaro_winkler("Haoran Liu", "Haoran Lim")
> 0.96
> textdistance.jaro_winkler("Haoran Liu", "Baoran Liu")
> 0.9333333333333332

The general difinition of Jaro–Winkler distance is [here](https://en.wikipedia.org/wiki/Jaro–Winkler_distance).

### Term frequency - Inverse Document Frequency

Levenshtein and Jaro-Winkler are great definitions, but after some testing, they are too slow for large datasets, and it becomes nearly impossible for our dataset, TMC, which is as big as 2 million. To run a traditional string distance matching on my laptop might will take several weeks. Well using TF-IDF, it only took two night to finish the matching computition. TF-IDF is pretty popular in matchine learning & NLP, and I accidently found a fast implenation in Python.

TF-IDF is a method to generate features from text by multiplying the frequency of a term (usually a word) in a document (the *Term Frequency*, or *TF*) by the importance (the *Inverse Document Frequency* or *IDF*) of the same term in an entire corpus. This last term weights less important words (e.g. the, it, and etc) down, and words that don’t occur frequently up. IDF is calculated as:
$$
IDF(t) = log_e(Total number of documents / Number of documents with term t in it).
$$
Consider a document containing 100 words in which the word cat appears 3 times. The term frequency (i.e., tf) for cat is then (3 / 100) = 0.03. Now, assume we have 10 million documents and the word cat appears in one thousand of these. Then, the inverse document frequency (i.e., idf) is calculated as log(10,000,000 / 1,000) = 4. Thus, the Tf-idf weight is the product of these quantities: 0.03 * 4 = 0.12.

TF-IDF is very useful in text classification and text clustering. It is used to transform documents into numeric vectors, that can easily be compared.

[More deatails about TF-IDF and fast grouping click here](https://bergvca.github.io/2017/10/14/super-fast-string-matching.html)

1. I've tried three different approaches above, Levenshtein and Jaro–Winkler are just to slow to implement. I did come up an idea: sort the name list first, and then calculate the neighbour only instead of mining full data. But the shortcoming is obvious: a lot of similiar names aren't neighbour after sorting. So I choose TF-IDF approach finally. ([link](https://github.com/FutureMathematician/TrademarkMatch/blob/main/Clean_name/Post_clean/group.py))

2. TF-IDF can automatically group strings, and it has a parameters to identify how much degree two similiar can be considered to be the same, the larger the prarameter, the harder two stings are grouped togther. I used TMC_assignor as a benchmark dataset, set the parameters as 0.7, 0.8, 0.85, 0.9, 0.95, run the TF-IDF algorithm, and random take 20 samples in each grouped dataset, manully check the correctness, here is the result:

   >keep if name != name0
   >count
   >sample 20, count
   >save sample0.7.dta, replace // 209,087 wrong 17, correctness rate 15%
   >save sample0.8.dta, replace // 87,046 wrong 7, correctness rate 65%
   >save sample0.85.dta, replace // 51,933 wrong 4, correctness rate 80%
   >save sample0.9.dta, replace // 28,293 wrong 0, correctness rate 100%
   >save sample0.95.dta, replace // 9,495 wrong 1, correctness rate 95%

   0.9 seems pretty great, the only wrong grouped pair is

   - vitek systems inc
   - mitek systems inc

   But this situation can be dealt in the next step in a big degree.

3. I'll relink the grouped data with the original data [(link)](https://github.com/FutureMathematician/TrademarkMatch/blob/main/Clean_name/Post_clean/link.do), and only keep the companies in the same state. Like, for the latter case,

   - vitek systems inc ---- MISSOURI
   - mitek systems inc ---- DELAWARE

   So this group won't be kept. Only when the two company names are extremely similiar, and they happened to be in the same state, they'll be misgrouped, but this odd is pretty low, since the mismatch rate before checking the state status is as low as 0%-5%.

   ![截屏2021-03-14 15.24.15](https://tva1.sinaimg.cn/large/e6c9d24egy1gojgpnrqx3j21bz0u0x6p.jpg)


| After Post-clean | COMPUSTAT | CRSP   | CIQ     | TMA_assignor | TMA_assignee | TMC       | Total     |
| ---------------- | --------- | ------ | ------- | ------------ | ------------ | --------- | --------- |
| Observations     | 40,204    | 41,799 | 698,695 | 499,327      | 413,176      | 2,014,748 | 2,954,241 |
| Dropped HM       |           | -      |         | 493,009      | 401,223      | 1,996,098 | 2,911,666 |
| Dropped >40      |           | -      |         |              |              | 1,975,236 | 2,905,517 |



## Cost

![截屏2021-03-14 14.49.35](https://tva1.sinaimg.cn/large/e6c9d24egy1gojfqddryhj21c00u0qv5.jpg)

| After Post-clean | Total     | Cost       |
| ---------------- | --------- | ---------- |
| Observations     | 2,954,241 | 68,775 HKD |
| Dropped HM       | 2,911,666 | 67,783 HKD |
| Dropped >40      | 2,905,517 | 67,640 HKD |

