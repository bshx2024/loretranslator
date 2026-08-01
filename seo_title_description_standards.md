# LoreTranslator SEO 标题与描述标准化指南 (SOP)

> 本文档为 LoreTranslator 项目中所有页面（翻译器工具页、语言字典页、生成器工具页、文章指南页）的 **Title Tag (metaTitle)**、**H1 Title**、**Meta Description** 以及 **URL Slug** 的最高制定红线标准。

---

## 📌 一、 标题双轨分工与要求 (Meta Title vs. H1)

项目采用 **Meta Title（给搜索引擎与 AI 爬虫看）** 与 **H1 Title（给人类读者看）** 的双轨分工：

### 1. Meta Title (`meta_title` / `<title>`)
* **定位**：谷歌 Search Console (SERP) 及 ChatGPT / Perplexity / Gemini 等 AI 搜索引擎检索的第一权重。
* **核心公式 (ABC Title Formula)**：
  $$\text{Meta Title} = \text{[Primary Keyword / Tier 1]} + \text{[Secondary LSI / Benefit]} \mid \text{Lore}$$
* **字符与像素截断红线**：
  * **必须严格控制在 50 – 60 字符**（最大 600px 宽度以内）。
  * 确保末尾的 `| Lore` 品牌后缀不会被 Google 搜索结果截断或省略。
* **关键词布局**：必须包含 Tier 1 主关键词（如 `English to Sindarin Elvish Translator`）以及高意向修饰词（如 `Dictionary`, `Tengwar Runes`, `Names`）。

### 2. H1 Title (`h1` / `<h1>`)
* **定位**：专为人类读者的阅读体验服务。
* **要求**：
  * 侧重主题完整性与技术/学术严谨度，不受 60 字符或 `| Lore` 品牌后缀限制。
  * **AST 语法红线**：整篇文章/页面在 H 标签层级树中，**只能有 1 个 H1 标签**。

### 3. 标题行文的三大质量法则
1. **具象数字法则 (Specificity Standard)**：标题中优先使用具体数字、统计量或具体分类（如 `25+ Romantic Quotes`, `100+ Verified Words`），严禁使用 *"the best"*, *"revolutionary"* 等模糊空洞词。
2. **极客与爱好者同频口吻 (Humanized Community Tone)**：拒绝僵硬的公关腔，使用 Tolkien 粉丝、D&D 玩家、纹身/刻字爱好者同频的真实口吻（如 `Tengwar Runes`, `Calligraphy Stencils`, `Ring Engravings`）。
3. **反夸大与实据兑现 (Clickbait Audit)**：标题中承诺的任何卖点（如 `Dictionary` 或 `PNG Stencil Export`），正文中必须在交互工具或表格中 100% 真实兑现。

---

## 📝 二、 描述规范 (Meta Description)

AI 搜索引擎选源与过滤时，Meta Description 的权重仅次于 URL 和 Title。

* **字数与字符红线**：
  * **必须严格控制在 140 – 160 字符** 以内。
* **句式与语态要求**：
  * 必须使用**主动语态**（如 *Free English to Sindarin... Convert text, names...*），行文干练直接。
* **三要素包含**：
  * **Tier 1 主关键词**
  * **核心技术/工具卖点**（如 Tengwar 符文、字典查找、矢量 PNG 导出）
  * **转化与应用场景锚点**（如 Custom Tattoos, Ring Engravings, Wedding Vows）

---

## 🔗 三、 关联规范：URL Slug 常青命名策略

与标题配套的 URL 路径（Slug）遵循以下铁律：

1. **短平快原则**：简短、直接包含主关键词（如 `/translators/sindarin-translator.html`）。
2. **严禁包含日期/年份**：严禁在 Slug 中写入年份或易变动数字（使用 `/articles/tolkien-love-quotes.html`，绝不使用 `/articles/2026-tolkien-love-quotes.html`），确保内容后续定期刷新（Evergreen Refresh）时无需做 301 重定向。

---

## 📋 四、 标杆范例对照表

| 字段 / 属性 | Frontmatter metaTitle (Title Tag) | Frontmatter title (H1 标题) | Meta Description (Meta 描述) |
| :--- | :--- | :--- | :--- |
| **主要受众** | 谷歌爬虫 / SERP / AI 搜索引擎 | 人类读者 (极客/爱好者/开发者) | SERP 摘要 / AI 选源第 3 权重 |
| **字符限制** | **50 – 60 字符** (Max 600px) | 无严格字数限制 | **140 – 160 字符** |
| **基本格式** | `[ABC 标题公式] \| Lore` | 完整技术/工具指南标题 | 主动语态 + 主词 + 核心卖点 |
| **标杆范例 1 (工具页)** | `English to Sindarin Elvish Translator & Dictionary \| Lore`<br>*(恰好 56 字符)* | `Online English to Sindarin Elvish Translator & Dictionary` | `Free English to Sindarin Elvish translator and dictionary. Convert text, names, and phrases into Tengwar runes for custom Elvish tattoos and ring engravings.`<br>*(恰好 155 字符)* |
| **标杆范例 2 (文章页)** | `25+ Romantic Tolkien Love Quotes for Weddings & Ring Engravings`<br>*(恰好 63 字符)* | `25+ Romantic Tolkien Love Quotes for Custom Wedding Ring Engravings` | `Discover romantic J.R.R. Tolkien love quotes for wedding vows & ring engravings. Includes Lord of the Rings quotes, Beren & Lúthien lines & Elvish scripts.`<br>*(恰好 155 字符)* |

---

## ⚙️ 五、 检查与发布 Checklists

新页面上线或更新前，必须通过以下 4 项校验：

- [ ] `metaTitle` 长度是否在 50-60 字符之间？末尾是否带有 `| Lore`？
- [ ] `metaDescription` 长度是否在 140-160 字符之间？是否为主动语态？
- [ ] 页面 DOM 中是否仅有 1 个 `<h1>` 标签？
- [ ] URL Slug 是否剔除了年份与无意义停用词？
