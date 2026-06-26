# LoreTranslator - Programmatic SEO Translator Website

LoreTranslator 是一个专门针对奇幻语言（如精灵语、阿凡达纳威语、古挪威卢恩文字、苏美尔楔形文字等）及古老历史语言的**程序化 SEO (pSEO) 静态网站生成器**。项目通过 Python 脚本将海量字典数据库与高阶前端模版融合，自动编译出一个支持在线翻译、实时字帖渲染、Canvas 画布导出的轻量级、高性能静态网站。

---

## 🌟 项目核心特性

1. **多语种翻译引擎**：
   * **精灵语 (Elvish)**：支持辛达林语 (Sindarin) 与昆雅语 (Quenya)。
   * **历史/古语言**：支持古英语 (Old English)、古诺斯/卢恩文字 (Old Norse/Runic)、阿兰文 (Aramaic)、科普特文 (Coptic)、苏美尔楔形文字 (Sumerian Cuneiform)、古希腊语 (Ancient Greek)。
   * **奇幻/科幻语言**：纳威语 (Na'vi)、外星符号 (Alien)、莎士比亚拟古腔 (Shakespearean)。
2. **实时书法画布 (Calligraphy Canvas)**：
   * 前端使用 Canvas 引擎实时绘制翻译结果，支持调整字体大小、文字颜色、背景，一键导出 PNG 透明字帖。
3. **程序化 SEO 架构**：
   * 自动生成支持 SEO 规范的子页面，拥有独立的 TDK (Title, Description, Keywords) 优化。
   * 自动编译和同步 `sitemap.xml` 和 `robots.txt`，保障搜索引擎收录。
4. **零后台静态部署**：
   * 所有翻译与字贴渲染逻辑全部在浏览器端（Client-side JS）运行，可直接挂载至 Cloudflare Pages、Vercel 或 GitHub Pages 等静态托管平台，承载百万流量。

---

## 📂 项目目录结构

```text
loretranslator/
├── dict_db.json                   # 核心数据库（包含各语种词典、卢恩/音节对照表等）
├── generate_site.py               # 核心建站构建脚本（读取模板，编译输出 HTML 页面）
├── verify_site.py                 # 站点预发布质量审计脚本 (QA Audit)
├── build_lore_db.py               # 词汇与设定数据库编译生成器
├── templates/                     # 前端 HTML & CSS 页面模板
│   ├── homepage.html              # 网站首页模板
│   ├── translator_subpage.html    # 翻译器子页面模板
│   ├── name_generator.html        # 精灵起名生成器模板
│   ├── engraving_guide.html       # 戒指刻字指南模板
│   ├── article.html               # 深度 SEO 知识文章模板
│   └── base.css                   # 全局样式文件
├── dist/                          # 编译输出目录（生成的完整静态网站，部署此目录即可）
│   ├── index.html
│   ├── sitemap.xml
│   ├── robots.txt
│   └── translators/
│       ├── sindarin-translator.html
│       └── ...
└── README.md                      # 本说明文档
```

---

## 🚀 快速开始与本地开发

### 1. 环境准备
确保您的本地环境安装了 **Python 3.x**（无需安装任何额外的第三方包，仅使用 Python 标准库）。

### 2. 编译生成静态站点
在项目根目录下运行生成脚本，它将读取 `templates/` 和 `dict_db.json`，在 `dist/` 目录下生成完整的网页资产：
```bash
python generate_site.py
```

### 3. 本地预览测试
定位到生成的静态目录并启动 Python 本地 Web 服务：
```bash
cd dist
python -m http.server 8080
```
启动后在浏览器中打开 [http://localhost:8080](http://localhost:8080) 即可进行体验与调试。

### 4. 运行预发布 QA 审计
在将 `dist/` 部署到生产环境之前，建议运行审计脚本来检测 sitemap 完整度、TDK 缺失、破损链接等 SEO 指标：
```bash
python verify_site.py
```

---

## 🔧 常见维护操作

### 添加新词汇或语种词典
直接编辑项目根目录下的 `dict_db.json`，在对应语种（如 `"elvish"."sindarin"`）下以 `键-值` 格式增加词条，例如：
```json
"love": "meleth"
```
编辑完成后，重新运行 `python generate_site.py` 即可更新全站的编译和前端翻译逻辑。
