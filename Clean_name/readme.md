In CIQ sub names, strange things happened, and they are manually solved.

4 patterns appeared in CIQ sub name strings:

- \u00e2\u0080\uXXXX
- \u00e2\uXXXX
- \u00e3\uXXXX
- \u00e5\uXXXX

where \uXXXX can be a variety of codes, and the codes before \uXXXX are like prefixes which make \uXXXX have different meanings.

For example:

- "belulu limited (\u00e2\u0080\u009cbelulu\u00e2\u0080\u009d)"
- "iskone denim pazarlama a\u00e2\u00a7."
- "genmar orman \u00e3\u009cr\u00e3\u009cnleri pazarlama ve ticaret a.s."
- "\u00e5\u00bdemes vystymo fondas 21 uab."

These combinations of symbols have will produce bad bing search results. They are actually exotic symbols, like ancient European characters, euro/pound signs, and so on.  So I use 4 json - dict files [00e20080.json](https://github.com/FutureMathematician/TMA_match/blob/main/Clean_name/00e20080.json), [00e2.json](https://github.com/FutureMathematician/TMA_match/blob/main/Clean_name/00e2.json), [00e3.json](https://github.com/FutureMathematician/TMA_match/blob/main/Clean_name/00e3.json), and [00e5.json](https://github.com/FutureMathematician/TMA_match/blob/main/Clean_name/00e5.json) to replace these strange combinations of codes. These four json files are like dictionaries, on the left is the strange codes, and on the left is the translation, which is manually checked by me.
