# bilingual_book_maker

bilingual_book_maker 是一個 AI 翻譯工具，使用 ChatGPT 幫助使用者製作多語言版本的 ePub 文件和圖書。該工具僅適用於翻譯進入公共版權領域的 ePub 圖書，不適用於有版權的書籍。請在使用之前閱讀專案的 **[免責聲明](./disclaimer.md)**。

![image](https://user-images.githubusercontent.com/15976103/222317531-a05317c5-4eee-49de-95cd-04063d9539d9.png)


## 準備

1. ChatGPT or OpenAI token
2. epub books
3. 能正常聯網的環境或 proxy
4. python3.8+


## 使用

1. pip install -r requirements.txt
2. OpenAI API key，如果有多個可以用英文逗號分隔(xxx,xxx,xxx)，可以減少介面呼叫次數帶來的錯誤
3. 本地放了一個 animal_farm.epub 給大家測試
4. 預設用了 [GPT-3.5-turbo](https://openai.com/blog/introducing-chatgpt-and-whisper-apis) 模型，也就是 ChatGPT 正在使用的模型，用 `--model gpt3` 來使用 gpt3 模型
5. 加了 `--test` 命令，如果大家沒付費可以加上這個先看看效果（有 limit 稍微有些慢）
6. Set the target language like `--language "zh-hans"`. Default target language is `zh-hant`. Support language list please see the LANGUAGES at [utils.py](./book_maker/utils.py).
7. 加了 `--proxy` 參數，方便中國大陸的使用者在本地測試時使用代理，傳入類似 `http://127.0.0.1:7890` 的字串
8. 加入 `--resume` 命令，可以手動中斷後，加入命令繼續執行。
9. 如果你遇到了墙需要用 Cloudflare Workers 替换 api_base 请使用 `--api_base ${url}` 来替换。**请注意，此处你输入的api应该是"`https://xxxx/v1`"的字样，域名需要用引号包裹**
10. 翻译完会生成一本 ${book_name}_bilingual.epub 的双语书
10. 如果出现了错误或 CTRL + C 中断，不想接下来继续翻译了，会生成一本 ${book_name}_bilingual_temp.epub 的书，直接改成你想要的名字就可以了

使用範例

```shell
# 如果你想快速測一下
python3 make_book.py --book_name test_books/animal_farm.epub --openai_key ${openai_key} --no_limit --test
# or do it # Chinese
python3 make_book.py --book_name test_books/animal_farm.epub --openai_key ${openai_key} --language zh-hant
# or 用 gpt3 模型
export OPENAI_API_KEY=${your_api_key}
python3 make_book.py --book_name test_books/animal_farm.epub --model gpt3 --no_limit --language ja
```

## 注意

1. 有 limit 如果想要速度可以付費
2. PR welcome
3. 尤其是 batch translate 做完效果會好很多
4. DeepL 模型稍後更新

# 感謝

- @[yetone](https://github.com/yetone)

# 貢獻

- 任何 issue PR 都歡迎
- Issue 中有些 TODO 沒做的都可以選
- 提交程式碼前請先 `black make_book.py`

## 讚賞

謝謝就夠了

![image](https://user-images.githubusercontent.com/15976103/222407199-1ed8930c-13a8-402b-9993-aaac8ee84744.png)
