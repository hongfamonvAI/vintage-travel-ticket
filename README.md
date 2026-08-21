# 老式记忆门票 / Vintage Travel Ticket

把旅行、城市街巷、风景、个人记忆或美食照片，重绘成一张 20 世纪中后期气质的中文老式门票。

它不是给照片加一层旧纸滤镜：每次生成会先抽取完整的票券原型，再改变比例、版式、纸张、套色、插画语言、做旧方式、字体和信息语法。票面不默认出现“XX券”“副券”或“存根”。

## 安装

将此仓库放入 Codex 的 skills 目录，例如：

```bash
git clone https://github.com/hongfamonvAI/vintage-travel-ticket.git \
  ~/.codex/skills/vintage-travel-ticket
```

然后在对话中上传一张旅行、街景、风景、食物或个人照片，并说“做成老式门票”。

## 工作方式

1. 首次上传图片时，只询问地点/景区/美食名称，并顺带允许用户提供姓名与纪念日期。
2. 生成前核对官方或权威名称；姓名保持原样，日期统一为 `YYYY.MM.DD`。
3. 自动从 16 类结构原型中选择完整设计 DNA，并联动比例、版式、纸张、套色、插画、字体、信息与做旧；不是把这些轴独立乱配。
4. 自动重绘照片，而非保留原构图；印刷磨损会同时发生在插画、文字、票号和规则上。
5. 每次只交付一张独立门票、一个最终版本；不会输出双方案、正反面拼图、对比稿或同画布多张票。

## 公共版说明

原始 66 张参考门票素材为私有资料，**不包含在 Git 历史中**。公开版逐张蒸馏了每张票的比例、版面结构、插画语言、纸张配色、字体角色、票务信息与真实印刷磨损，形成匿名设计索引以及可组合的规则系统。

仓库还包含 8 张低清、去元数据并带有 `STYLE ONLY` 标识的风格索引图。它们只帮助模型理解构图、配色、字体轮廓与印刷磨损，不提供可恢复的原图，也禁止照抄票面文字、标志、印章、票号或具体画面。

当前公开系统包含 16 类结构原型、18 套纸张配色、14 种插画语言、16 套字体角色配方和印刷做旧矩阵，并通过随机配方脚本保持各轴之间的时代与工艺一致性。若创作者本人在本机的 `assets/private-reference/` 挂载完整 66 张原图，选择器会自动进入私有增强模式，每次只抽取 1–2 张兼容参考；该目录已被 Git 忽略，不会上传。普通 GitHub 用户则自动使用公开索引图，无须额外配置。

## 效果示例

### 芒通 Menton

| 原照片 | 生成门票 |
| --- | --- |
| <img src="examples/menton-source.jpg" width="300" alt="Menton source photo"> | <img src="examples/menton-ticket.jpg" width="500" alt="Menton vintage ticket"> |

### 罗兰·加洛斯球场 Roland-Garros Stadium

| 原照片 | 生成门票 |
| --- | --- |
| <img src="examples/roland-garros-source.jpg" width="300" alt="Roland-Garros source photo"> | <img src="examples/roland-garros-ticket.jpg" width="500" alt="Roland-Garros vintage ticket"> |

### 重庆大厦 Chungking Mansions

| 原照片 | 生成门票 |
| --- | --- |
| <img src="examples/chungking-mansions-source.jpg" width="300" alt="Chungking Mansions source photo"> | <img src="examples/chungking-mansions-ticket.jpg" width="500" alt="Chungking Mansions vintage ticket"> |

### 阿尔伯克基 Albuquerque

| 原照片 | 生成门票 |
| --- | --- |
| <img src="examples/albuquerque-source.jpg" width="300" alt="Albuquerque source photo"> | <img src="examples/albuquerque-ticket.jpg" width="500" alt="Albuquerque vintage ticket"> |

### 厦门沙坡尾 Shapowei, Xiamen

| 原照片 | 生成门票 |
| --- | --- |
| <img src="examples/xiamen-shapowei-source.jpg" width="300" alt="Shapowei source photo"> | <img src="examples/xiamen-shapowei-ticket.jpg" width="500" alt="Shapowei vintage ticket"> |

### 泉州 Quanzhou

| 原照片 | 生成门票 |
| --- | --- |
| <img src="examples/quanzhou-source.jpg" width="300" alt="Quanzhou source photo"> | <img src="examples/quanzhou-ticket.jpg" width="500" alt="Quanzhou vintage ticket"> |

## 目录

```text
.
├── SKILL.md                 # 主流程与质量规则
├── agents/openai.yaml       # Codex skill 元数据
├── assets/style-contact-sheets/ # 可公开分发的低清风格索引图
├── scripts/                 # 设计 DNA 采样、视觉参考路由与索引图构建
├── references/              # 匿名逐图索引与分层设计系统
└── examples/                # 授权展示的原图与生成效果
```

示例照片与生成结果仅用于本仓库的展示；请勿将人物照片或参考素材用于未经授权的再发布。
