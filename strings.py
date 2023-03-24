TITLE = "BELLE Playground"

ABSTRACT = """
Thanks to [BELLE](https://github.com/LianjiaTech/BELLE), this simple application runs BELLE which is instruction fine-tuned version of [LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/) from Meta AI.
 BELLE is *LLaMA Fine-Tuning* which is inspired by [Stanford Alpaca project](https://github.com/tatsu-lab/stanford_alpaca). 

"""

BOTTOM_LINE = """
In order to process batch generation, the common parameters in LLaMA are fixed. If you want to change the values of them, please do that in `generation_config.yaml`
"""

DEFAULT_EXAMPLES = [
    {
        "title": "1️⃣ 写一篇英文散文诗，主题是春雨，想象自己是春雨，和英国古代诗人莎士比亚交流",
        "examples": [
            ["1", "写一篇英文散文诗，主题是春雨，想象自己是春雨，和英国古代诗人莎士比亚交流"],
            ["2", "创作这首诗的作者当时是什么心理？"],
            ["3", "把这首诗改写成中文的七言律诗"],
        ],
    },
    {
        "title": "2️⃣ 小明的爸爸有三个孩子，老大叫王一，老二叫王二，老三叫什么？",
        "examples": [
            ["1", "小明的爸爸有三个孩子，老大叫王一，老二叫王二，老三叫什么？"],
            ["2", "王二和小明什么关系？"],
            ["3", "王二的爸爸和小明是什么关系？"],
            ["4", "父母都姓吴，取一些男宝宝和女宝宝的名字"],
        ],
    },
    {
        "title": "3️⃣ 今天天气怎么样，把这句话翻译成英语",
        "examples": [
            ["1", "今天天气怎么样，把这句话翻译成英语"],
        ]
    },
    {
        "title": "4️⃣ 使用python写一个二分查找的代码",
        "examples": [
            ["1", "使用python写一个二分查找的代码"],
            ["2", "could you explain how the code works?"]            
        ]
    }
]

SPECIAL_STRS = {
    "continue": "continue.",
    "summarize": "summarize our conversations so far in three sentences."
}