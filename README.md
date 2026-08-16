# 老式记忆门票 / Vintage Travel Ticket

把旅行、城市街巷、风景、个人记忆或美食照片，重绘成一张 20 世纪中后期气质的中文老式门票。

它不是给照片加一层旧纸滤镜：每次生成会先抽取完整的票券原型，再改变比例、版式、纸张、套色、插画语言、做旧方式、字体和信息语法。票面不默认出现“XX券”“副券”或“存根”。

## 安装

将此仓库放入 Codex 的 skills 目录，例如：

```bash
git clone https://github.com/<your-github-username>/vintage-travel-ticket.git \
  ~/.codex/skills/vintage-travel-ticket
```

然后在对话中上传一张旅行、街景、风景、食物或个人照片，并说“做成老式门票”。

## 工作方式

1. 首次上传图片时，只询问地点/景区/美食名称，并顺带允许用户提供姓名与纪念日期。
2. 生成前核对官方或权威名称；姓名保持原样，日期统一为 `YYYY.MM.DD`。
3. 自动随机选择参考原型：宽横票、紧凑横票、地图票、木刻票、双联票、长条竖票、竖版纪念卡或黑金票等。
4. 自动重绘照片，而非保留原构图；印刷磨损会同时发生在插画、文字、票号和规则上。

## 公共版说明

原始 66 张参考门票素材为私有资料，**不包含在本仓库中**。公开版保留由其整理出的文字化风格系统与原型规则，因此可独立使用；如果你有自己的参考票，可在本地加入 `assets/reference-tickets/` 作为额外灵感，但不要直接复刻其中任何一张。

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
├── references/              # 风格、原型、字体规则
└── examples/                # 授权展示的原图与生成效果
```

示例照片与生成结果仅用于本仓库的展示；请勿将人物照片或参考素材用于未经授权的再发布。
