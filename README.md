RoboCup@Home YOLO 视觉识别系统
本项目为 Agoratalker/yolo_test 仓库，基于 Python 开发，旨在实现 RoboCup@Home 比赛中的物体识别与人物感知任务。
📂 核心文件说明
• 训练脚本: train.py (模型训练入口) 及 yolov8n.pt (预训练 Nano 权重)。
• 预处理工具: XMLtoTXT.py (标签格式转换)、splitDataset.py (训练/验证集划分)、ViewCategory.py (类别查询)。
• 说明文档: 启动方式.txt (包含具体运行指令)。
🎯 关键识别任务
• 标准物体: 识别 30 种以上家庭用品，包含餐具、食品、重物、易碎品及微小物体等。
• 人物特征: 识别人脸、性别、大致年龄及衣服颜色。
• 行为感知: 检测挥手、指向等社交手势。
• 环境状态: 识别门、洗碗机或抽屉的开闭状态。
