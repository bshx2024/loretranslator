# LoreTranslator.com AI 博文写作与防算法惩罚标准指南
(Anti-AI Spam & E-E-A-T Content Quality Guidelines)

为了防范谷歌核心算法更新（Helpful Content System & Scaled Content Abuse）的风控惩罚，所有在 `/articles/` 或 `/blog/` 目录下发布的文章必须严格执行本标准。

---

## 🎯 核心原则：提供“信息增量 (Information Gain)”
谷歌判定“AI 垃圾内容”的核心逻辑是：**如果你的文章只是对搜索结果前 10 名的结论进行重新洗牌和复述，没有任何独特的数据、工具或视角，就会被降权。**

我们必须通过以下方式注入“信息增量”：
1.  **注入工具数据**：博文中必须嵌入来自我们 `dict_db.json` 的真实学术对照表。
2.  **提供视觉预览**：每篇设计类文章必须包含 SVG 书法效果展示或 Canvas 导出的纹身排版范例。
3.  **第一人称实证**：使用 “We verified...”, “In our translation engine...” 等第一人称叙事，体现有人工测试和研发参与，满足 E-E-A-T 中的 Experience (经验)。

---

## 🚫 写作三大禁忌（消除 AI 写作痕迹）

AI（如 ChatGPT/Claude）在撰写长文时有极强的“词汇指纹”，这些指纹是谷歌垃圾内容过滤器检测的重点。必须在 prompt 中明确禁止并人工过滤以下内容：

### 1. 禁用 AI 套话与无意义过渡词
*   **严禁开头废话**：AI 喜欢用 "In the world of...", "Have you ever wondered...", "Since time immemorial..." 开头。文章必须直奔主题。
*   **严禁无用过渡词**：严禁出现 `In conclusion`, `Moreover`, `Furthermore`, `It is important to remember`, `Indeed`, `Additionally`。
*   **严禁 AI 标志性动词**：严禁使用 `delve into`, `testament to`, `tapestry`, `beacon`, `revolutionize` 等高频 AI 词汇。

### 2. 避免假学术（捏造事实）
*   AI 经常会“胡说八道”，编造不存在的精灵语单词或错误的卢恩字母映射。
*   **铁律**：文中引用的任何翻译对照，必须与我们程序工具中使用的 `dict_db.json`（学术整理版）保持 100% 一致。

### 3. 禁止无结构长段落
*   用户和搜索引擎都讨厌大段的文字。
*   **规范**：每个段落不得超过 3 行字。必须频繁使用 Markdown 粗体、引用块 (`>`)、无序列表 (`-`) 和对比表格 (`|`)。

---

## 📏 篇幅与配图规范 (Length & Image Standards)

### 1. 篇幅长度控制 (Word Count)
*   **字数底线**：每篇博文的有效英文单词量**不得低于 1,000 字**，推荐区间在 **1,000 - 1,500 字**。
*   **严禁无意义填充 (No Filler)**：这 1,000 字必须由**实质性内容**组成：包含详细背景历史、文法对照细节、改尺工艺步骤、FAQ 深度解答。禁止让 AI 复制车轱辘话来凑字数。

### 2. 独家配图规范 (Unique Visual Assets)
*   **拒绝无版权/同质化图库**：严禁直接从网络复制他人图片，或使用大路货的 stock photos（这会被谷歌图片库判重过滤）。
*   **强制工具效果图嵌入**：文章必须嵌入至少 2 张通过我们 `loretranslator.com` 工具 Canvas 渲染生成的**独家书法 SVG/PNG 效果图**（例如：包含滕格瓦字母或卢恩字母的纹身设计效果图、带刻字说明的戒指细节图）。
*   **Alt 标签深度优化**：每张图片必须配置极度详尽的英文 `alt` 属性，嵌入目标长尾词，坚决不留空。
    *   *错误示例*：`alt="elvish word"`
    *   *正确示例*：`alt="Elvish love quote translation in Tengwar calligraphy script for custom gold ring engraving"`

---

## 🤖 GEO (生成式搜索优化) 收录标准规范

为了让博文能够被 **Google SGE (AI Overviews)**、**SearchGPT** 和 **Perplexity** 等生成式 AI 搜索引擎抓取、理解并作为信源引用 (Citations)，文章必须符合以下 GEO 标准：

### 1. 结构化 Q&A / FAQ 模式
*   GEO 引擎极喜欢抓取符合自然语言问答结构的段落。
*   每篇博文中必须设计 2-3 个符合用户口语化提问的 **H3 级问答小节**（例如：`### How much does it cost to engrave Elvish on a ring?` 或 `### Is Quenya or Sindarin better for a tattoo?`）。
*   **紧跟直接回答 (Direct Attribution)**：在 H3 下方，第一句必须以强断言、结构化的句子作答，方便 LLM 提取为摘要卡片。

### 2. 权威信源引用与学术归因 (Cite Reputable Sources)
*   LLM 在汇总生成时，倾向于选择那些主动归因学术信源的站点，以此避免幻觉。
*   **规范**：文章中引用词根或历史时，必须明确写明来源。例如：
    *   *“According to Tolkien's linguistic papers published in the Parma Eldalamberon...”*
    *   *“Based on the official Navajo Nation linguistic code rules...”*
*   这不仅极大增加了谷歌 E-E-A-T 评分，也是 SearchGPT 和 Perplexity 最喜欢的信源归因格式。

### 3. Key-Value 键值对与表格优先
*   在说明流程或价格时，必须整理成 AI 极易读取的 **键值对列表** 或 **Markdown 表格**。相比大段的自然语言，生成式搜索引擎对表格的抓取和引用概率要高出 **300% 以上**。

---

## 📝 博文结构模版（ Helpful Content 落地规范）

每篇博文必须采用以下“漏斗式”结构进行撰写：

### 1. 首屏：痛点直达 (Direct Answer)
*   **字数**：150字以内。
*   **要求**：直接回答用户搜索词的核心问题。例如如果是 `how much does it cost to get a ring resized`，首段必须直接给出价格区间（如 `$20 - $150`），并给出加粗的结论。不要让用户往下滚屏寻找答案。

### 2. 核心可视化：Markdown 数据表
*   必须包含至少一个数据表（如不同材质改尺寸的价格对比、常见精灵语词汇的学术含义对照）。

### 3. 互动引导：引流组件 (Interactive CTA Widget)
*   博文中段必须插入一个显眼的交互卡片或一键复制链接，引导用户跳转到我们对应的翻译工具。
*   *例*：“*Want to see how your own names look in Tengwar? Go to our [Free Elvish Calligraphy Translator](file:///E:/kaifa/loretranslator/index.html) to export your design.*”

### 4. 商业税收点：联盟营销卡片 (Affiliate Card)
*   在涉及刻字、纹身或礼品的章节，植入设计精美、带有真实体验描述的定制引导（引导至定制珠宝商或纹身贴商家，赚取佣金）。

---

## 🔍 AI 生成博文审查清单 (Pre-Publish Checklist)
在发布任何新文章前，运行此清单自我审计：
*   [ ] 全文有效英文单词数是否达到 1,000 字以上？
*   [ ] 配图是否为本站生成的独家渲染图，且配置了详尽的 Alt 标签？
*   [ ] 是否包含至少一个口语化提问的 H3 问答小节，且首句为直接回答？
*   [ ] 是否有学术/权威信源（如 Parma Eldalamberon, Navajo Code）的明确归因？
*   [ ] 文章开头第一句是否直接回答了标题的问题？（没有铺垫废话）
*   [ ] 是否删除了所有的 "In conclusion" 和 "delve into"？
*   [ ] 是否包含至少一个 Markdown 对比表格？
*   [ ] 段落是否都拆分成了 3 行以内的小段？
*   [ ] 是否有指向我们本站 Translator 工具页面的内部链接？
*   [ ] 翻译的词汇是否在 `dict_db.json` 中可查，非 AI 捏造？
