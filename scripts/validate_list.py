#!/usr/bin/env python3
"""校验 README 作品清单：条目格式 + 链接存活 + 归一化去重。

- 格式错误 → 失败（exit 1），PR 门禁拦下。
- 死链 / 重复 → 警告（不失败，避免 CI 因偶发网络抖动误杀；重复由处理 skill 兜底）。

只用标准库，无需 pip 依赖。
"""
import re
import sys
import urllib.request
import urllib.error

README = "README.md"

# 条目行：* :status: [名字](http(s)://url)：介绍
ENTRY_RE = re.compile(
    r"^\* :(white_check_mark|clock8|x): \[[^\]]+\]\((https?://[^)]+)\)：.+"
)
# 疑似条目（以 * : 开头）但格式不对，用于报格式错
LOOSE_RE = re.compile(r"^\* :")


def normalize(url: str) -> str:
    u = url.strip().lower()
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    u = re.sub(r"/+$", "", u)
    return u


def link_alive(url: str) -> bool:
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(
                url, method=method, headers={"User-Agent": "civc-linkcheck/1.0"}
            )
            with urllib.request.urlopen(req, timeout=12) as r:
                if r.status < 400:
                    return True
        except urllib.error.HTTPError as e:
            if e.code < 400:
                return True
        except Exception:
            continue
    return False


def main() -> int:
    with open(README, encoding="utf-8") as f:
        lines = f.readlines()

    fmt_errors: list[str] = []
    urls: list[tuple[int, str]] = []
    in_fence = False

    for i, raw in enumerate(lines, 1):
        line = raw.rstrip("\n")
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue  # 跳过代码块里的格式示例
        if not LOOSE_RE.match(line):
            continue
        m = ENTRY_RE.match(line)
        if not m:
            fmt_errors.append(f"  第 {i} 行格式不符：{line[:80]}")
            continue
        urls.append((i, m.group(2)))

    print(f"扫描到 {len(urls)} 条合规条目。")

    # 归一化去重
    seen: dict[str, int] = {}
    dups: list[str] = []
    for ln, url in urls:
        n = normalize(url)
        if n in seen:
            dups.append(f"  第 {ln} 行与第 {seen[n]} 行重复：{url}")
        else:
            seen[n] = ln

    # 死链（软警告）
    dead: list[str] = []
    for ln, url in urls:
        if not link_alive(url):
            dead.append(f"  第 {ln} 行链接打不开：{url}")

    if dups:
        print("⚠️ 疑似重复（请处理 skill 复核，不阻断）：")
        print("\n".join(dups))
    if dead:
        print("⚠️ 死链（软警告，不阻断；请提交者确认）：")
        print("\n".join(dead))

    if fmt_errors:
        print("❌ 条目格式错误（必须修复）：")
        print("\n".join(fmt_errors))
        print("\n正确格式：* :white_check_mark: [产品名](https://链接)：一句话介绍")
        return 1

    print("✅ 格式校验通过。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
