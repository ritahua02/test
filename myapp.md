---
title: 个人项目
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.22"

---

# 个人项目

Base URLs:

* <a href="http://127.0.0.1:8000">测试环境: http://127.0.0.1:8000</a>

# Authentication

# myapp

## POST 注册

POST /myapp/register/

> Body Parameters

```yaml
username: jiuhua
password: "123456"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» username|body|string| yes |none|
|» password|body|string| yes |none|

> Response Examples

> 成功

```json
{
  "code": 0,
  "msg": "注册成功！"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|

## POST 登陆

POST /myapp/login/

> Body Parameters

```yaml
username: jiuhua
password: "123456"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» username|body|string| yes |none|
|» password|body|string| yes |none|

> Response Examples

> 成功

```json
{
  "code": 0,
  "msg": "登陆成功"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|

## POST 增加会话和消息

POST /myapp/add_chat/

> Body Parameters

```yaml
username: jiuhua1
chat_id: "1"
chat_title: 请根据以下历史聊天字
chat_content: 可以填任意文本
chat_tpye: "0"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» username|body|string| yes |none|
|» chat_id|body|string| yes |none|
|» chat_title|body|string| yes |none|
|» chat_content|body|string| no |none|
|» chat_tpye|body|number| no |none|

> Response Examples

> 成功

```json
{
  "code": 0,
  "msg": "对话加入成功"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|

## POST 删除对话

POST /myapp/delete_chat/

> Body Parameters

```yaml
chat_id: "1"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» chat_id|body|number| yes |none|

> Response Examples

> 成功

```json
{
  "code": 0,
  "msg": "对话删除成功"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|

## POST 随机获取8条prompt示例

POST /myapp/get_prompt_fuction/

> Body Parameters

```yaml
{}

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|

> Response Examples

> 成功

```json
"['小红书账号介绍文案', '请输入您的小红书账号类型，我将为您提供小红书风格的账号介绍，比如“美妆博主”']['高情商大师', '碰见刁难或尴尬的问题不知道如何回答？试一试高情商大师的建议吧']"
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 增加prompt示例

POST /myapp/add_prompt_fuction/

> Body Parameters

```yaml
prompt_title: python数据处理
prompt_text: 我有五个excel表，每个表有6列。帮我写一段python，把这五个表合成一个表。

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» prompt_title|body|string| yes |none|
|» prompt_text|body|string| yes |none|

> Response Examples

> 成功

```json
{
  "code": 0,
  "prompt_title": "python数据处理",
  "prompt_text": "我有五个excel表，每个表有6列。帮我写一段python，把这五个表合成一个表。",
  "prompt_msg": "示例promp存储成功"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» prompt_title|string|true|none||none|
|» prompt_text|string|true|none||none|
|» prompt_msg|string|true|none||none|

## POST 获取历史数据

POST /myapp/get_history_chat/

> Body Parameters

```yaml
chat_title: 请根据以下历史聊天字

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» chat_title|body|string| yes |none|

> Response Examples

> 成功

```json
{
  "code": 0,
  "历史信息列表": [
    [
      "chatcar",
      "sdasdasdadadasdfas"
    ],
    [
      "chatcar",
      "sdasdasdadadasdfsdasdffdsfas"
    ],
    [
      "user",
      "sdasdasdadadasdfsdasdffdsfas"
    ]
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» 历史信息列表|[array]|true|none||none|

# Data Schema

