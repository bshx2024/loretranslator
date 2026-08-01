# LoreTranslator SEO 标题与描述标准化指南 (SOP & CRO 高转化红线)

> 本文档为 LoreTranslator 项目中所有页面（翻译器工具页、语言字典页、专效子落地页、文章指南页）的 **Title Tag (metaTitle)**、**H1 Title**、**Meta Description** 以及 **URL Slug** 的最高制定标准，**兼顾谷歌算法建权 (On-Page SEO) 与商业转化率 (CRO & CTR)**。

---

## 📌 一、 标题双轨分工与要求 (Meta Title vs. H1)

项目采用 **Meta Title（给搜索引擎与 AI 爬虫看）** 与 **H1 Title（给人类读者看）** 的双轨分工：

### 1. Meta Title (`meta_title` / `<title>`)
* **定位**：谷歌 Search Console (SERP) 及 ChatGPT / Perplexity / Gemini 等 AI 搜索引擎检索的第一权重。
* **核心公式 (ABC Title Formula)**：
  $$\text{Meta Title} = \text{[Primary Keyword / Tier 1]} + \text{[Secondary LSI / High-Intent CRO Keyword]} \mid \text{Lore}$$
* **字符与像素截断红线**：
  * **必须严格控制在 50 – 60 字符**（最大 600px 宽度以内）。
  * 确保末尾的 `| Lore` 品牌后缀不会被 Google 搜索结果截断或省略。
* **关键词布局**：必须包含 Tier 1 主关键词（0 位前置）以及高意向修饰词（如 `Tattoo`, `Ring Engravings`, `Write My Name`, `Dictionary`）。

### 2. H1 Title (`h1` / `<h1>`)
* **定位**：专为人类读者的阅读体验服务。
* **要求**：
  * 侧重主题完整性与技术/学术严谨度，不受 60 字符或 `| Lore` 品牌后缀限制。
  * **AST 语法红线**：整篇文章/页面在 H 标签层级树中，**只能有 1 个 H1 标签**。

---

## 🚀 二、 高转化率 (CRO & CTR) 五大黄金红线法则

为了确保任何搜索结果不仅排名靠前，更能带来**超高点击率 (CTR)** 与**站内工具使用转化 (Conversion)**，必须严格执行以下 5 法则：

1. **高商业意向词嵌入 (High Commercial Intent Modifiers)**：
   * Meta Title 中必须选择性嵌入 `Tattoo`, `Ring Engravings`, `Wedding Vows` 等极强转化磁力词（70%+ 搜索用户的真实落地需求）。
2. **情感唤醒与个人相关性 (Personal Emotional Connection)**：
   * 对于人名类/个人定制类工具页，优先使用 **`Write My Name`** 替代冷冰冰的 `Write Name`，触发强烈的个人相关性点击。
3. **零成本信任钩子 (Zero-Friction Trust Hook)**：
   * Description 开头统一使用 **`Free online...`** 或 **`Free...`**，第一时间消除用户对付费墙 (Paywall) 或强制注册账号的心理戒备。
4. **独家卖点强力 CTA 结尾 (USP Action Trigger)**：
   * Description 结尾统一以 **`Instant PNG exporter!`** 或 **`Free PNG stencil exporter!`** 作为 Call-to-Action。
   * *转化心理*：向 SERP 用户明确传递“本站可直接生成并免费下载透明背景矢量/高清手稿图”的独家卖点，对竞品形成降维打击。
5. **反夸大与实据兑现 (Clickbait Audit)**：
   * 标题和描述中承诺的任何卖点（如 `Instant PNG exporter` 或 `Dictionary`），正文中必须在交互工具中 100% 真实兑现（前端 HTML5 Canvas 0 毫秒即时导出）。

---

## 📝 三、 描述规范 (Meta Description)

AI 搜索引擎选源与过滤时，Meta Description 的权重仅次于 URL 和 Title。

* **字数与字符红线**：
  * **必须严格控制在 140 – 160 字符** 以内。
* **句式与语态要求**：
  * 必须使用**主动语态**（如 *Free online English to Sindarin... Translate text & names...*），行文干练直接。
* **三要素包含（SOP + CRO 必选组合）**：
  1. **Tier 1 主关键词**（100% 连续精准命中）
  2. **转化场景锚点**（如 `for tattoos & ring engravings`, `wedding vows`）
  3. **独家卖点 CTA 结尾**（`Instant PNG exporter!`）

---

## 🔗 四、 关联规范：URL Slug 常青命名策略

与标题配套的 URL 路径（Slug）遵循以下铁律：

1. **短平快原则**：简短、直接包含主关键词（如 `/translators/sindarin-translator.html`）。
2. **严禁包含日期/年份**：严禁在 Slug 中写入年份或易变动数字（使用 `/articles/tolkien-love-quotes.html`，绝不使用 `/articles/2026-tolkien-love-quotes.html`），确保内容后续定期刷新（Evergreen Refresh）时无需做 301 重定向。

---

## 📋 五、 100 分满分标杆范例对照表

以下范例全部取自 LoreTranslator 项目中经过全套 On-Page SEO 体检（98~100分）与 CRO 高转化验证的线上真实页面：

| 页面类型 / 属性 | Frontmatter metaTitle (Title Tag) | Frontmatter title (H1 标题) | Meta Description (Meta 描述) |
| :--- | :--- | :--- | :--- |
| **规则限制** | **50 – 60 字符** (Max 600px, 0位主词) | 单页面仅 1 个 `<h1>` | **140 – 160 字符** (含 PNG Exporter CTA) |
| **范例 1：工具主页**<br>*(Sindarin Translator)* | `Sindarin Translator: English to Elvish Tattoo Runes \| Lore`<br>*(恰好 59 字符)* | `Sindarin Translator & English to Elvish Dictionary` | `Free English to Sindarin translator & dictionary. Translate text & names into Tengwar Elvish runes for tattoos & ring engravings. Instant PNG exporter!`<br>*(恰好 153 字符)* |
| **范例 2：子专效页**<br>*(Sindarin Name)* | `Sindarin Name Translator: Write My Name in Elvish \| Lore`<br>*(恰好 57 字符)* | `Sindarin Name Translator & Write My Name in Elvish Generator` | `Free Sindarin name translator. Translate English male & female names into Tengwar Elvish runes for tattoos & ring engravings. Instant PNG exporter!`<br>*(恰好 151 字符)* |
| **范例 3：高地精灵语**<br>*(Quenya Translator)* | `Quenya Translator: English to High Elvish Tattoo \| Lore`<br>*(恰好 57 字符)* | `Quenya Translator & English to High Elvish Dictionary` | `Free online Quenya translator & dictionary. Translate English text & names into High Elvish Tengwar runes for custom tattoos & ring engravings. Instant PNG exporter!`<br>*(恰好 158 字符)* |
| **范例 4：高转化文章页**<br>*(Tolkien Love Quotes)* | `Tolkien Love Quotes: 25+ Romantic Ring Engravings \| Lore`<br>*(恰好 56 字符)* | `25+ Romantic Tolkien Love Quotes for Custom Wedding Ring Engravings` | `Discover romantic Tolkien love quotes for wedding vows & ring engravings. Includes Lord of the Rings lines, Elvish scripts & free PNG stencil exporter!`<br>*(恰好 153 字符)* |

---

## ⚙️ 六、 检查与发布 Checklists

新页面上线或更新前，必须通过以下 5 项红线校验：

- [ ] `metaTitle` 长度是否在 50-60 字符之间？0位是否前置 Tier 1 主词？末尾是否带有 `| Lore`？是否包含 `Tattoo` 或 `Write My Name` 等 CRO 磁力词？
- [ ] `metaDescription` 长度是否在 140-160 字符之间？是否为主动语态？结尾是否包含 `Instant PNG exporter!` 或 `free PNG stencil exporter!` 强力 CTA？
- [ ] 页面 DOM 中是否仅有 1 个 `<h1>` 标签？
- [ ] 正文中是否包含了支撑卖点的 100% 真实兑现交互工具/格式？
- [ ] URL Slug 是否保持短平快并剔除了年份与无意义停用词？
