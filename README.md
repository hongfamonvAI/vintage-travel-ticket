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
6. 国外地点可随机加入经过核实的英文或当地语言短信息，如官方名称、城市、街区/街道或已确认年份；只作点缀，不套用固定双语模板。
7. 每张成品必须同时具备票制结构证据与票务信息证据，例如边框/分栏/票联结构配合票号、票价、检票、印章、代码或持票人字段；长条比例和做旧纸张本身不算门票。

## 公共版说明

原始 66 张参考门票素材为私有资料，**不包含在 Git 历史中**。公开版逐张蒸馏了每张票的比例、版面结构、插画语言、纸张配色、字体角色、票务信息与真实印刷磨损，形成匿名设计索引以及可组合的规则系统。

仓库还包含两层可公开视觉参考：8 张略提清晰度、去元数据并带有 `STYLE ONLY` 标识的低清历史风格拼图，以及 1 张由最新生成门票组成的高清拼图。所有拼图都以原始比例完整容纳每张门票，不裁掉边框、票根、标题或纸边。前者负责历史票制结构、配色、字体轮廓与印刷磨损；后者只补充“这些规则如何落成完整门票”的执行范围。选择器最多返回一张历史拼图和这一张生成门票拼图，禁止照抄任何票面文字、标志、印章、票号、人物、地点内容或具体布局。

当前公开系统包含 16 类结构原型、18 套纸张配色、14 种插画语言、16 套字体角色配方和印刷做旧矩阵，并通过随机配方脚本保持各轴之间的时代与工艺一致性。普通 GitHub 用户会自动进入“1 张低清历史拼图 + 1 张高清生成门票拼图”的公共混合参考模式，无须额外配置。若创作者本人在本机的 `assets/private-reference/` 挂载完整 66 张原图，选择器会优先进入私有增强模式，每次只抽取 1–2 张兼容参考；该目录已被 Git 忽略，不会上传。

## 最新打版案例

以下原照片与生成结果均经过授权并已去除元数据。原照片只用于 README 展示对照，不属于素材库。选择器不会读取 `examples/`；`assets/generated-ticket-library/` 只允许收录完成的老门票，并通过 `gNN-*.jpg` 白名单阻止原照片进入生图风格参考路由。

### 巴黎 Paris

| 原照片 | 生成门票 |
| --- | --- |
| <img src="examples/paris-source.jpg" width="300" alt="Paris source photo"> | <img src="examples/paris-ticket.jpg" width="300" alt="Paris vintage ticket"> |

### 景德镇瓷宫 Porcelain Palace

| 原照片 | 生成门票 |
| --- | --- |
| <img src="examples/porcelain-palace-source.jpg" width="300" alt="Porcelain Palace source photo"> | <img src="examples/porcelain-palace-ticket.jpg" width="300" alt="Porcelain Palace vintage ticket"> |

### 芒通 Menton

| 原照片 | 生成门票 |
| --- | --- |
| <img src="examples/menton-source.jpg" width="300" alt="Menton source photo"> | <img src="examples/menton-ticket.jpg" width="500" alt="Menton vintage ticket"> |

### 济州岛 Jeju Island

| 原照片 | 生成门票 |
| --- | --- |
| <img src="examples/jeju-island-source.jpg" width="300" alt="Jeju Island source photo"> | <img src="examples/jeju-island-ticket.jpg" width="500" alt="Jeju Island vintage ticket"> |

### 青城山宿仙谷 Qingcheng Mountain Suxian Valley

| 原照片 | 生成门票 |
| --- | --- |
| <img src="examples/qingcheng-suxiangu-source.jpg" width="300" alt="Qingcheng Suxiangu source photo"> | <img src="examples/qingcheng-suxiangu-ticket.jpg" width="300" alt="Qingcheng Suxiangu vintage ticket"> |

### 西湖 West Lake

| 原照片 | 生成门票 |
| --- | --- |
| <img src="examples/west-lake-source.jpg" width="300" alt="West Lake source photo"> | <img src="examples/west-lake-ticket.jpg" width="300" alt="West Lake vintage ticket"> |

### 罗兰·加洛斯球场 Roland-Garros Stadium

| 原照片 | 生成门票 |
| --- | --- |
| <img src="examples/roland-garros-source.jpg" width="300" alt="Roland-Garros source photo"> | <img src="examples/roland-garros-ticket.jpg" width="500" alt="Roland-Garros vintage ticket"> |

### 维多利亚港 Victoria Harbour

| 原照片 | 生成门票 |
| --- | --- |
| <img src="examples/victoria-harbour-source.jpg" width="300" alt="Victoria Harbour source photo"> | <img src="examples/victoria-harbour-ticket.jpg" width="500" alt="Victoria Harbour vintage ticket"> |

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
├── assets/style-contact-sheets/ # 可公开分发的低清历史风格索引图
├── assets/generated-ticket-library/ # 一张高清生成门票拼图与内容索引
├── scripts/                 # 设计采样、视觉路由与公开素材构建
├── references/              # 匿名逐图索引与分层设计系统
└── examples/                # README 展示对比，不参与生成路由
```

示例照片与生成结果仅用于本仓库的展示；请勿将人物照片或参考素材用于未经授权的再发布。
