# 中文独立开发者 Vibe Coding 作品集

**中国独立开发者 Vibe Coding 项目列表 · 分享大家都在做什么**

> 你用 AI / Vibe Coding 做了个东西？发上来，让更多人看见。

[![投稿](https://img.shields.io/badge/欢迎-投稿-brightgreen?style=for-the-badge)](../../issues/new?template=submit-project.yml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-1f6feb?style=for-the-badge)](./CONTRIBUTING.md)
![语言](https://img.shields.io/badge/面向-中文独立开发者-orange?style=for-the-badge)

**这是一份由社区投稿、专门收录「中文独立开发者用 Vibe Coding 做出来的产品」的清单。**

Vibe Coding（借助 AI 辅助编程——Cursor / Claude Code / Codex / Copilot / Trae 等——把想法直接做成产品）
让一个人也能做出完整的东西。这里不放教程、不放资源合集、不放纯代码库——**只放能打开、能用的作品**，
以及做出它的那个人。

一个人 + 一个 AI + 一个周末，就能有个真东西。**把你的发上来。**

---

## 🧭 入选标准

1. **是能用的产品**：网站 / App / 小程序 / 桌面工具 / 浏览器插件等，有一个**能打开的链接**。不收教程、资源清单、纯 library。
2. **独立/个人开发者作品**：主要由一个人或很小的团队做出来，不是公司产品线。
3. **Vibe Coding 做的**：开发过程大量借助 AI 编程（欢迎在介绍里注明用了什么工具）。
4. **面向中文圈**：中文开发者，或主要服务中文用户的产品优先。

## 🏷 图例

| 标记 | 含义 |
|---|---|
| :white_check_mark: | 在运营 |
| :clock8: | 开发中 / 公测 |
| :x: | 已关闭 |

## 📝 条目格式

```
* :white_check_mark: [产品名](https://链接)：一句让人想点进去的介绍（做什么、解决什么）。🛠 用了 Cursor/Claude Code 等 · [仓库](https://github.com/...)
```

- 介绍写**具体、有吸引力**的一句话，别写「一个很好用的工具」这种正确的废话。
- 可选：标注用了哪些 AI 编程工具（🛠）、是否开源（附仓库链接）。

## 🚀 怎么投稿（两种方式，任选其一）

- **方式一 · 提 Issue（推荐，最省事）**：点 [这里填投稿表单](../../issues/new?template=submit-project.yml)，填好产品名、链接、一句话介绍即可，我们来整理进清单。
- **方式二 · 直接发 PR**：照上面的格式，把你的作品加到下面「作品清单」**最新日期那一节的最上面**（新增一节 `### YYYY 年 M 月`），提交 Pull Request。详见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

---

## 📦 作品清单

### 2026 年 7 月

#### [EloLin](https://github.com/DevEloLin)
* :white_check_mark: [EloGames](https://games.elolin.com)：即开即玩的网页小游戏平台，主打自研《Lifeverse》——在多元宇宙里反复「重开人生」的模拟器。
* :white_check_mark: [KinMate](https://kinmate.elolin.com)：本地优先的家庭健康档案库，把化验单、病历、宠物健康资料安全存在自己设备上，AI 帮你读懂每一项。
* :white_check_mark: [TestHive](https://testhive.elolin.com)：众测市场——开发者发布测试活动，测试者靠积分经济赚奖励，测试报告可公开分享。

> 👆 以上为示例条目（同时也是本清单发起人的作品）。**下一个就是你的**——[点此投稿](../../issues/new?template=submit-project.yml)。

---

## 📚 精选收录（整理自社区清单）

除社区投稿的 Vibe Coding 作品外，我们还整理了一份**高星中文独立开发者项目**（取自
[chinese-independent-developer](https://github.com/1c7/chinese-independent-developer) 与
[1000-chinese-independent-developer-plus](https://github.com/XiaomingX/1000-chinese-independent-developer-plus)，
GitHub 星标 ≥ 10、按 star 降序前 100），供发现与致敬——与上面的「作品清单」区分开。

👉 **[查看：精选收录 · 高星中文独立开发者项目 →](./pages/featured.md)**

## ⚙️ 维护与自动化（不使用 GitHub Actions）

收稿处理由 AI 技能 [`.claude/skills/process-submissions`](./.claude/skills/process-submissions/SKILL.md) 自主完成：
校验（链接存活 + 品类符合 + 归一化去重）→ 只增不删加进清单 → 感谢并关闭 Issue / 合并 PR。

**本仓库刻意不跑 GitHub Actions**，技能通过以下方式运行：

- **托管 Claude Routine 定时跑**（推荐，零 GitHub Actions）：在 Claude Code 里把本仓库 + 该技能配成一个定时 Routine（如每 6 小时），由 Anthropic 侧调度自动收稿。
- **维护者本地按需跑**：`claude "处理投稿"` 即触发该技能。

链接/格式/去重也可本地手动校验（纯标准库，无依赖）：

```bash
python scripts/validate_list.py
```

## ❓ 常见问题（FAQ）

**Vibe Coding 是什么？**
Vibe Coding（氛围编程）指主要通过向 AI 编程工具（Cursor、Claude Code、Codex、GitHub Copilot、Trae、Windsurf 等）描述需求，把想法直接做成能运行的软件，而不必手写全部代码。2025 年由 Andrej Karpathy 提出后迅速流行。

**这个清单收录什么？**
只收**中文独立开发者用 vibe coding 做出来、能打开能用的产品**——网站 / App / 小程序 / 桌面工具 / 浏览器插件。不收教程、课程、资源合集（awesome 类）、纯代码库或纯开发者工具。

**怎么投稿 / 怎么提 PR？**
两种方式：① 提 [Issue 填投稿表单](../../issues/new?template=submit-project.yml)；② 直接发 Pull Request。详见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

**用哪些 AI 工具做的算 vibe coding？**
Cursor、Claude Code、Codex、GitHub Copilot、Trae、Windsurf、v0、Bolt、Lovable 等 AI 辅助编程工具都算。欢迎在投稿里注明用了哪个。

**和「中国独立开发者项目列表」有什么区别？**
[那份清单](https://github.com/1c7/chinese-independent-developer)收录所有中文独立产品；本清单**专注 Vibe Coding（AI 编程）这一波**做出来的作品，定位更聚焦。

## In English

**Chinese Indie Vibe Coding** is a community-curated showcase of real, usable products **vibe-coded by Chinese independent (indie) developers** — built with AI coding tools such as Cursor, Claude Code, Codex, and GitHub Copilot. It lists websites, apps, mini-programs, desktop tools and browser extensions (not tutorials, courses or dev tools). Anyone can submit their product via a GitHub Issue or Pull Request.

## 🤝 参与与致谢

- 投稿指南见 [CONTRIBUTING.md](./CONTRIBUTING.md)。
- 灵感来自 [chinese-independent-developer](https://github.com/1c7/chinese-independent-developer)（中国独立开发者项目列表）——它收所有独立产品，本清单专注 **Vibe Coding** 这一波。
- 内容以 [CC0](./LICENSE) 释出，欢迎自由取用与二次整理。

---

> **关键词 / Keywords**：Vibe Coding · 氛围编程 · AI 编程 · AI 辅助编程 · **面向中文** · **面向中国独立开发者** · 中文独立开发者 · 中国独立开发者 · 独立开发者作品集 · 独立产品 · indie developer · indie hacker · AI 做的产品 · Cursor · Claude Code · Codex · GitHub Copilot · Trae · Windsurf · 作品投稿 · vibe coding 作品/项目清单

