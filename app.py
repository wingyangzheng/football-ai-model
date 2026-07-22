from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

mock_matches = [
    {
        "id": 1,
        "league": "英超",
        "home_team": "曼联",
        "away_team": "利物浦",
        "match_time": "2024-01-15 20:30",
        "status": "未开始",
        "indices": {
            "home_win": 2.10,
            "draw": 3.20,
            "away_win": 3.50
        },
        "score_options": {
            "1:0": 9.00, "2:0": 13.0, "2:1": 8.50, "3:0": 18.0, "3:1": 15.0,
            "3:2": 18.0, "4:0": 25.0, "4:1": 28.0, "4:2": 50.0, "4:3": 80.0,
            "5:0": 40.0, "5:1": 60.0, "5:2": 100.0, "5:3": 150.0, "5:4": 200.0,
            "win_other": 250.0, "0:0": 7.50, "1:1": 6.00, "2:2": 10.0, "3:3": 40.0,
            "4:4": 150.0, "5:5": 400.0, "draw_other": 500.0,
            "0:1": 11.0, "0:2": 15.0, "1:2": 12.0, "0:3": 22.0, "1:3": 20.0,
            "2:3": 25.0, "0:4": 30.0, "1:4": 35.0, "2:4": 50.0, "3:4": 80.0,
            "0:5": 50.0, "1:5": 70.0, "2:5": 90.0, "3:5": 150.0, "4:5": 200.0,
            "lose_other": 250.0
        },
        "total_goals": {
            "0": 7.50, "1": 4.00, "2": 3.20, "3": 4.00, "4": 6.50, "5": 10.0, "6": 15.0, "7+": 25.0
        },
        "half_time_full_time": {
            "home_home": 3.50, "home_draw": 12.0, "home_away": 28.0,
            "draw_home": 6.50, "draw_draw": 5.00, "draw_away": 8.50,
            "away_home": 22.0, "away_draw": 13.0, "away_away": 6.00
        }
    },
    {
        "id": 2,
        "league": "西甲",
        "home_team": "巴塞罗那",
        "away_team": "皇马",
        "match_time": "2024-01-15 23:15",
        "status": "未开始",
        "indices": {
            "home_win": 2.30,
            "draw": 3.10,
            "away_win": 3.00
        },
                "score_options": {
            "1:0": 7.50, "2:0": 11.00, "2:1": 7.50, "3:0": 15.00, "3:1": 13.00,
            "3:2": 16.00, "4:0": 22.00, "4:1": 25.00, "4:2": 45.00, "4:3": 80.00,
            "5:0": 35.00, "5:1": 60.00, "5:2": 100.00, "5:3": 150.00, "5:4": 200.00, "win_other": 40.0,
            "0:0": 8.00, "1:1": 5.50, "2:2": 9.50, "3:3": 35.00, "4:4": 150.00, "5:5": 400.00, "draw_other": 50.0,
            "0:1": 9.50, "0:2": 13.00, "1:2": 9.00, "0:3": 18.00, "1:3": 16.00,
            "2:3": 22.00, "0:4": 25.00, "1:4": 30.00, "2:4": 45.00, "3:4": 80.00,
            "0:5": 45.00, "1:5": 65.00, "2:5": 85.00, "3:5": 150.00, "4:5": 200.00, "lose_other": 55.0
        },
        "total_goals": {
            "0": 8.00, "1": 4.20, "2": 3.00, "3": 3.80, "4": 6.00, "5": 9.50, "6": 14.0, "7+": 22.0
        },
        "half_time_full_time": {
            "home_home": 4.00, "home_draw": 11.0, "home_away": 25.0,
            "draw_home": 6.00, "draw_draw": 4.50, "draw_away": 7.50,
            "away_home": 20.0, "away_draw": 12.0, "away_away": 5.50
        }
    },
    {
        "id": 3,
        "league": "德甲",
        "home_team": "拜仁慕尼黑",
        "away_team": "多特蒙德",
        "match_time": "2024-01-16 01:30",
        "status": "未开始",
        "indices": {
            "home_win": 1.65,
            "draw": 4.20,
            "away_win": 5.50
        },
                "score_options": {
            "1:0": 6.00, "2:0": 7.50, "2:1": 6.50, "3:0": 8.50, "3:1": 9.00,
            "3:2": 12.00, "4:0": 10.00, "4:1": 12.00, "4:2": 25.00, "4:3": 80.00,
            "5:0": 13.00, "5:1": 60.00, "5:2": 100.00, "5:3": 150.00, "5:4": 200.00, "win_other": 20.0,
            "0:0": 9.00, "1:1": 7.00, "2:2": 9.00, "3:3": 30.00, "4:4": 150.00, "5:5": 400.00, "draw_other": 45.0,
            "0:1": 13.00, "0:2": 16.00, "1:2": 11.00, "0:3": 22.00, "1:3": 15.00,
            "2:3": 18.00, "0:4": 28.00, "1:4": 22.00, "2:4": 35.00, "3:4": 80.00,
            "0:5": 38.00, "1:5": 50.00, "2:5": 70.00, "3:5": 150.00, "4:5": 200.00, "lose_other": 50.0
        },
        "total_goals": {
            "0": 9.00, "1": 4.50, "2": 3.20, "3": 3.50, "4": 5.50, "5": 8.00, "6": 12.0, "7+": 18.0
        },
        "half_time_full_time": {
            "home_home": 2.80, "home_draw": 10.0, "home_away": 24.0,
            "draw_home": 5.50, "draw_draw": 5.50, "draw_away": 9.00,
            "away_home": 26.0, "away_draw": 15.0, "away_away": 8.50
        }
    },
    {
        "id": 4,
        "league": "意甲",
        "home_team": "AC米兰",
        "away_team": "尤文图斯",
        "match_time": "2024-01-16 03:45",
        "status": "未开始",
        "indices": {
            "home_win": 2.00,
            "draw": 3.30,
            "away_win": 3.80
        },
                "score_options": {
            "1:0": 7.50, "2:0": 10.00, "2:1": 8.00, "3:0": 14.00, "3:1": 12.00,
            "3:2": 15.00, "4:0": 20.00, "4:1": 22.00, "4:2": 40.00, "4:3": 80.00,
            "5:0": 32.00, "5:1": 60.00, "5:2": 100.00, "5:3": 150.00, "5:4": 200.00, "win_other": 38.0,
            "0:0": 7.00, "1:1": 5.50, "2:2": 8.50, "3:3": 35.00, "4:4": 150.00, "5:5": 400.00, "draw_other": 48.0,
            "0:1": 9.00, "0:2": 12.00, "1:2": 10.00, "0:3": 18.00, "1:3": 16.00,
            "2:3": 20.00, "0:4": 25.00, "1:4": 28.00, "2:4": 40.00, "3:4": 80.00,
            "0:5": 42.00, "1:5": 60.00, "2:5": 80.00, "3:5": 150.00, "4:5": 200.00, "lose_other": 52.0
        },
        "total_goals": {
            "0": 7.00, "1": 3.80, "2": 3.00, "3": 3.80, "4": 5.80, "5": 9.00, "6": 13.0, "7+": 20.0
        },
        "half_time_full_time": {
            "home_home": 3.50, "home_draw": 11.5, "home_away": 26.0,
            "draw_home": 6.00, "draw_draw": 5.00, "draw_away": 8.00,
            "away_home": 22.0, "away_draw": 13.0, "away_away": 7.00
        }
    },
    {
        "id": 5,
        "league": "法甲",
        "home_team": "巴黎圣日耳曼",
        "away_team": "里昂",
        "match_time": "2024-01-16 04:00",
        "status": "未开始",
        "indices": {
            "home_win": 1.55,
            "draw": 4.50,
            "away_win": 6.00
        },
                "score_options": {
            "1:0": 5.50, "2:0": 6.50, "2:1": 6.00, "3:0": 7.50, "3:1": 8.00,
            "3:2": 13.00, "4:0": 9.00, "4:1": 11.00, "4:2": 22.00, "4:3": 80.00,
            "5:0": 12.00, "5:1": 60.00, "5:2": 100.00, "5:3": 150.00, "5:4": 200.00, "win_other": 18.0,
            "0:0": 10.00, "1:1": 8.00, "2:2": 10.00, "3:3": 30.00, "4:4": 150.00, "5:5": 400.00, "draw_other": 48.0,
            "0:1": 14.00, "0:2": 18.00, "1:2": 12.00, "0:3": 25.00, "1:3": 16.00,
            "2:3": 20.00, "0:4": 32.00, "1:4": 25.00, "2:4": 35.00, "3:4": 80.00,
            "0:5": 45.00, "1:5": 60.00, "2:5": 80.00, "3:5": 150.00, "4:5": 200.00, "lose_other": 55.0
        },
        "total_goals": {
            "0": 10.0, "1": 5.00, "2": 3.50, "3": 3.20, "4": 5.00, "5": 7.50, "6": 11.0, "7+": 16.0
        },
        "half_time_full_time": {
            "home_home": 2.50, "home_draw": 9.50, "home_away": 23.0,
            "draw_home": 5.00, "draw_draw": 6.00, "draw_away": 9.50,
            "away_home": 28.0, "away_draw": 16.0, "away_away": 10.0
        }
    },
    {
        "id": 6,
        "league": "英超",
        "home_team": "曼城",
        "away_team": "阿森纳",
        "match_time": "2024-01-16 20:30",
        "status": "未开始",
        "indices": {
            "home_win": 1.80,
            "draw": 3.60,
            "away_win": 4.20
        },
                "score_options": {
            "1:0": 7.00, "2:0": 9.00, "2:1": 7.50, "3:0": 12.00, "3:1": 11.00,
            "3:2": 14.00, "4:0": 16.00, "4:1": 20.00, "4:2": 40.00, "4:3": 80.00,
            "5:0": 25.00, "5:1": 60.00, "5:2": 100.00, "5:3": 150.00, "5:4": 200.00, "win_other": 35.0,
            "0:0": 8.50, "1:1": 6.00, "2:2": 9.50, "3:3": 38.00, "4:4": 150.00, "5:5": 400.00, "draw_other": 50.0,
            "0:1": 10.00, "0:2": 14.00, "1:2": 10.50, "0:3": 20.00, "1:3": 17.00,
            "2:3": 19.00, "0:4": 28.00, "1:4": 30.00, "2:4": 45.00, "3:4": 80.00,
            "0:5": 48.00, "1:5": 65.00, "2:5": 85.00, "3:5": 150.00, "4:5": 200.00, "lose_other": 58.0
        },
        "total_goals": {
            "0": 8.50, "1": 4.20, "2": 3.10, "3": 3.60, "4": 5.50, "5": 8.50, "6": 12.5, "7+": 19.0
        },
        "half_time_full_time": {
            "home_home": 3.00, "home_draw": 11.0, "home_away": 25.0,
            "draw_home": 6.50, "draw_draw": 5.50, "draw_away": 9.50,
            "away_home": 24.0, "away_draw": 14.0, "away_away": 8.00
        }
    }
]

mock_rankings_week = [
    {"rank": 1, "nickname": "数据大师", "roi": 88.2, "win_rate": 78.5, "user_id": "QS001"},
    {"rank": 2, "nickname": "战术鬼才", "roi": 76.5, "win_rate": 72.3, "user_id": "QS002"},
    {"rank": 3, "nickname": "预测王者", "roi": 72.1, "win_rate": 69.8, "user_id": "QS003"},
    {"rank": 4, "nickname": "绿茵智者", "roi": 68.9, "win_rate": 67.2, "user_id": "QS004"},
    {"rank": 5, "nickname": "足球通", "roi": 65.3, "win_rate": 64.5, "user_id": "QS005"},
    {"rank": 6, "nickname": "盘路专家", "roi": 62.8, "win_rate": 61.9, "user_id": "QS006"},
    {"rank": 7, "nickname": "赛果先知", "roi": 59.4, "win_rate": 59.2, "user_id": "QS007"},
    {"rank": 8, "nickname": "数据狂人", "roi": 56.7, "win_rate": 56.8, "user_id": "QS008"},
    {"rank": 9, "nickname": "足球达人", "roi": 54.2, "win_rate": 54.1, "user_id": "QS009"},
    {"rank": 10, "nickname": "智算先锋", "roi": 51.8, "win_rate": 51.5, "user_id": "QS010"},
]

mock_rankings_total = [
    {"rank": 1, "nickname": "预测王者", "roi": 156.8, "win_rate": 71.2, "user_id": "QS003"},
    {"rank": 2, "nickname": "数据大师", "roi": 142.3, "win_rate": 75.6, "user_id": "QS001"},
    {"rank": 3, "nickname": "盘路专家", "roi": 128.9, "win_rate": 63.4, "user_id": "QS006"},
    {"rank": 4, "nickname": "战术鬼才", "roi": 115.7, "win_rate": 68.9, "user_id": "QS002"},
    {"rank": 5, "nickname": "绿茵智者", "roi": 98.5, "win_rate": 65.1, "user_id": "QS004"},
    {"rank": 6, "nickname": "赛果先知", "roi": 87.3, "win_rate": 58.7, "user_id": "QS007"},
    {"rank": 7, "nickname": "足球通", "roi": 76.2, "win_rate": 62.3, "user_id": "QS005"},
    {"rank": 8, "nickname": "数据狂人", "roi": 65.8, "win_rate": 55.4, "user_id": "QS008"},
    {"rank": 9, "nickname": "足球达人", "roi": 54.6, "win_rate": 53.2, "user_id": "QS009"},
    {"rank": 10, "nickname": "智算先锋", "roi": 43.1, "win_rate": 50.8, "user_id": "QS010"},
    {"rank": 11, "nickname": "比赛分析师", "roi": 38.5, "win_rate": 49.2, "user_id": "QS011"},
    {"rank": 12, "nickname": "战术分析师", "roi": 32.7, "win_rate": 47.1, "user_id": "QS012"},
    {"rank": 13, "nickname": "足彩高手", "roi": 25.4, "win_rate": 45.3, "user_id": "QS013"},
    {"rank": 14, "nickname": "赛事观察员", "roi": 18.9, "win_rate": 43.2, "user_id": "QS014"},
    {"rank": 15, "nickname": "足球爱好者", "roi": 12.3, "win_rate": 41.0, "user_id": "QS015"},
]

# 玩家详情数据（含资金曲线和历史投注）
mock_player_details = {
    "QS001": {
        "nickname": "数据大师", "user_id": "QS001", "avatar": "数",
        "level": 5, "title": "传奇量化分析师",
        "current_funds": 1280000, "initial_funds": 200000,
        "growth_rate": 540.0,
        "bankruptcy_records": [{"date": "2023-08-15", "time": "14:30"}, {"date": "2023-11-02", "time": "09:15"}],
        "stats": {"total_predictions": 456, "win_rate": 75.6, "roi": 142.3},
        "funds_curve": [
            {"date": "W1", "funds": 200000}, {"date": "W2", "funds": 235000},
            {"date": "W3", "funds": 218000}, {"date": "W4", "funds": 280000},
            {"date": "W5", "funds": 320000}, {"date": "W6", "funds": 385000},
            {"date": "W7", "funds": 450000}, {"date": "W8", "funds": 520000},
            {"date": "W9", "funds": 610000}, {"date": "W10", "funds": 750000},
            {"date": "W11", "funds": 890000}, {"date": "W12", "funds": 1280000}
        ],
        "bet_history": [
            {"league": "英超", "match": "曼城 vs 阿森纳", "option": "主胜", "odds": 1.80, "points": 10000, "result": "赢", "time": "2024-01-14"},
            {"league": "西甲", "match": "皇马 vs 马竞", "option": "平局", "odds": 3.20, "points": 5000, "result": "赢", "time": "2024-01-13"},
            {"league": "德甲", "match": "拜仁 vs 多特蒙德", "option": "客胜", "odds": 4.50, "points": 8000, "result": "输", "time": "2024-01-12"},
            {"league": "意甲", "match": "尤文 vs 国米", "option": "主胜", "odds": 2.10, "points": 12000, "result": "赢", "time": "2024-01-10"},
            {"league": "法甲", "match": "巴黎 vs 马赛", "option": "主胜", "odds": 1.55, "points": 15000, "result": "赢", "time": "2024-01-09"}
        ]
    },
    "QS002": {
        "nickname": "战术鬼才", "user_id": "QS002", "avatar": "战",
        "level": 4, "title": "资深战术分析师",
        "current_funds": 856000, "initial_funds": 200000,
        "growth_rate": 328.0,
        "bankruptcy_records": [{"date": "2023-09-20", "time": "16:45"}],
        "stats": {"total_predictions": 389, "win_rate": 68.9, "roi": 115.7},
        "funds_curve": [
            {"date": "W1", "funds": 200000}, {"date": "W2", "funds": 215000},
            {"date": "W3", "funds": 248000}, {"date": "W4", "funds": 275000},
            {"date": "W5", "funds": 310000}, {"date": "W6", "funds": 365000},
            {"date": "W7", "funds": 420000}, {"date": "W8", "funds": 485000},
            {"date": "W9", "funds": 560000}, {"date": "W10", "funds": 640000},
            {"date": "W11", "funds": 730000}, {"date": "W12", "funds": 856000}
        ],
        "bet_history": [
            {"league": "英超", "match": "利物浦 vs 切尔西", "option": "主胜", "odds": 1.90, "points": 8000, "result": "赢", "time": "2024-01-14"},
            {"league": "西甲", "match": "巴萨 vs 塞维利亚", "option": "客胜", "odds": 5.20, "points": 5000, "result": "输", "time": "2024-01-13"},
            {"league": "德甲", "match": "莱比锡 vs 勒沃库森", "option": "平局", "odds": 3.10, "points": 6000, "result": "赢", "time": "2024-01-11"}
        ]
    },
    "QS003": {
        "nickname": "预测王者", "user_id": "QS003", "avatar": "预",
        "level": 5, "title": "传奇预测大师",
        "current_funds": 2156000, "initial_funds": 200000,
        "growth_rate": 978.0,
        "bankruptcy_records": [],
        "stats": {"total_predictions": 523, "win_rate": 71.2, "roi": 156.8},
        "funds_curve": [
            {"date": "W1", "funds": 200000}, {"date": "W2", "funds": 265000},
            {"date": "W3", "funds": 340000}, {"date": "W4", "funds": 420000},
            {"date": "W5", "funds": 580000}, {"date": "W6", "funds": 750000},
            {"date": "W7", "funds": 980000}, {"date": "W8", "funds": 1250000},
            {"date": "W9", "funds": 1580000}, {"date": "W10", "funds": 1820000},
            {"date": "W11", "funds": 1980000}, {"date": "W12", "funds": 2156000}
        ],
        "bet_history": [
            {"league": "英超", "match": "热刺 vs 阿森纳", "option": "客胜", "odds": 2.80, "points": 20000, "result": "赢", "time": "2024-01-14"},
            {"league": "意甲", "match": "AC米兰 vs 罗马", "option": "主胜", "odds": 1.95, "points": 15000, "result": "赢", "time": "2024-01-13"},
            {"league": "西甲", "match": "马竞 vs 皇马", "option": "平局", "odds": 3.40, "points": 10000, "result": "赢", "time": "2024-01-12"}
        ]
    }
}

# 跟投记录（模拟）
follow_records = {}

mock_home_data = {
    "featured_matches": [
        {
            "id": 2,
            "league": "西甲",
            "home_team": "巴塞罗那",
            "away_team": "皇马",
            "match_time": "2024-01-15 23:15",
            "status": "未开始",
            "indices": {
                "home_win": 2.30,
                "draw": 3.10,
                "away_win": 3.00
            },
            "sentiment": {
                "home_win_percent": 78,
                "draw_percent": 12,
                "away_win_percent": 10
            }
        },
        {
            "id": 1,
            "league": "英超",
            "home_team": "曼联",
            "away_team": "利物浦",
            "match_time": "2024-01-15 20:30",
            "status": "未开始",
            "indices": {
                "home_win": 2.10,
                "draw": 3.20,
                "away_win": 3.50
            },
            "sentiment": {
                "home_win_percent": 45,
                "draw_percent": 28,
                "away_win_percent": 27
            }
        }
    ],
    "top_ranking": [
        {"rank": 1, "nickname": "数据大师", "win_rate": 78.5, "user_id": "QS001"},
        {"rank": 2, "nickname": "战术鬼才", "win_rate": 72.3, "user_id": "QS002"},
        {"rank": 3, "nickname": "预测王者", "win_rate": 69.8, "user_id": "QS003"}
    ],
    "article": {
        "title": "深度复盘：英超第20轮大数据量化分析报告",
        "summary": "通过机器学习模型对英超本赛季200+场比赛进行量化分析，发现控球率与胜率之间存在非线性关系...",
        "read_count": "2.3万"
    }
}

mock_user_profile = {
    "avatar": "球",
    "nickname": "懂球帝",
    "user_id": "#888888",
    "level": 3,
    "title": "资深量化分析师",
    "current_funds": 356000,
    "initial_funds": 100000,
    "growth_rate": 256.0,
    "stats": {
        "total_predictions": 128,
        "win_rate": 65.6,
        "roi": 45.2
    },
    "funds_curve": [
        {"date": "W1", "funds": 100000}, {"date": "W2", "funds": 112000},
        {"date": "W3", "funds": 98500}, {"date": "W4", "funds": 145000},
        {"date": "W5", "funds": 168000}, {"date": "W6", "funds": 155000},
        {"date": "W7", "funds": 198000}, {"date": "W8", "funds": 225000},
        {"date": "W9", "funds": 248000}, {"date": "W10", "funds": 285000},
        {"date": "W11", "funds": 312000}, {"date": "W12", "funds": 356000}
    ],
    "bet_history": [
        {"league": "英超", "match": "曼城 vs 阿森纳", "option": "主胜", "odds": 1.80, "points": 5000, "result": "赢", "time": "2024-01-14"},
        {"league": "西甲", "match": "皇马 vs 马竞", "option": "平局", "odds": 3.20, "points": 3000, "result": "赢", "time": "2024-01-13"},
        {"league": "德甲", "match": "拜仁 vs 沃尔夫斯堡", "option": "主胜", "odds": 1.45, "points": 10000, "result": "赢", "time": "2024-01-12"},
        {"league": "意甲", "match": "AC米兰 vs 国际米兰", "option": "客胜", "odds": 2.80, "points": 8000, "result": "输", "time": "2024-01-10"},
        {"league": "法甲", "match": "巴黎 vs 马赛", "option": "主胜", "odds": 1.55, "points": 6000, "result": "赢", "time": "2024-01-09"}
    ],
    "prediction_history": [
        {
            "id": 1,
            "league": "英超",
            "home_team": "曼城",
            "away_team": "阿森纳",
            "predict_option": "主胜",
            "predict_index": 1.80,
            "points": 5000,
            "status": "成功",
            "match_time": "2024-01-14 20:30"
        },
        {
            "id": 2,
            "league": "西甲",
            "home_team": "皇马",
            "away_team": "马竞",
            "predict_option": "平局",
            "predict_index": 3.20,
            "points": 3000,
            "status": "成功",
            "match_time": "2024-01-13 23:15"
        },
        {
            "id": 3,
            "league": "德甲",
            "home_team": "拜仁慕尼黑",
            "away_team": "沃尔夫斯堡",
            "predict_option": "主胜",
            "predict_index": 1.45,
            "points": 10000,
            "status": "待开盘",
            "match_time": "2024-01-16 01:30"
        },
        {
            "id": 4,
            "league": "意甲",
            "home_team": "AC米兰",
            "away_team": "国际米兰",
            "predict_option": "客胜",
            "predict_index": 2.80,
            "points": 8000,
            "status": "待开盘",
            "match_time": "2024-01-16 03:45"
        }
    ]
}

@app.route('/api/get_matches', methods=['GET'])
def get_matches():
    import copy
    matches = copy.deepcopy(mock_matches)
    for m in matches:
        hw = m['indices']['home_win']
        if hw < 1.8:
            m['handicap'] = -1
            m['handicap_label'] = '主队让1球'
            m['handicap_indices'] = {
                'home_win': round(hw * 2.2, 2),
                'draw': round(m['indices']['draw'] * 1.3, 2),
                'away_win': round(m['indices']['away_win'] * 0.55, 2)
            }
        elif hw > 2.5:
            m['handicap'] = 1
            m['handicap_label'] = '主队受让1球'
            m['handicap_indices'] = {
                'home_win': round(hw * 0.55, 2),
                'draw': round(m['indices']['draw'] * 1.2, 2),
                'away_win': round(m['indices']['away_win'] * 2.0, 2)
            }
        else:
            m['handicap'] = -1
            m['handicap_label'] = '主队让1球'
            m['handicap_indices'] = {
                'home_win': round(hw * 1.8, 2),
                'draw': round(m['indices']['draw'] * 1.15, 2),
                'away_win': round(m['indices']['away_win'] * 0.65, 2)
            }
    return jsonify({"status": "success", "data": matches})

@app.route('/api/get_rankings', methods=['GET'])
def get_rankings():
    chart_type = request.args.get('type', 'week')
    if chart_type == 'total':
        return jsonify({"status": "success", "data": mock_rankings_total})
    return jsonify({"status": "success", "data": mock_rankings_week})

@app.route('/api/get_player_detail', methods=['GET'])
def get_player_detail():
    user_id = request.args.get('user_id')
    if user_id in mock_player_details:
        return jsonify({"status": "success", "data": mock_player_details[user_id]})
    # 为没有预置详情的玩家生成通用数据
    nickname = ''
    for r in mock_rankings_week + mock_rankings_total:
        if r['user_id'] == user_id:
            nickname = r['nickname']
            break
    if not nickname:
        return jsonify({"status": "error", "message": "玩家不存在"}), 404
    import random
    base_funds = 200000
    funds = base_funds
    curve = []
    for i in range(12):
        funds = int(funds * (1 + random.uniform(0.05, 0.25)))
        curve.append({"date": f"W{i+1}", "funds": funds})
    detail = {
        "nickname": nickname, "user_id": user_id, "avatar": nickname[0] if nickname else "?",
        "level": 3, "title": "量化分析师",
        "current_funds": funds, "initial_funds": base_funds,
        "growth_rate": round((funds - base_funds) / base_funds * 100, 1),
        "bankruptcy_records": [{"date": "2023-10-05", "time": "11:20"}] if random.random() > 0.5 else [],
        "stats": {"total_predictions": random.randint(100, 400), "win_rate": round(random.uniform(50, 70), 1), "roi": round(random.uniform(30, 100), 1)},
        "funds_curve": curve,
        "bet_history": [
            {"league": "英超", "match": "曼联 vs 热刺", "option": "主胜", "odds": 2.00, "points": 8000, "result": "赢", "time": "2024-01-14"},
            {"league": "西甲", "match": "皇马 vs 皇家社会", "option": "客胜", "odds": 4.20, "points": 5000, "result": "输", "time": "2024-01-13"},
            {"league": "意甲", "match": "那不勒斯 vs 拉齐奥", "option": "平局", "odds": 3.10, "points": 6000, "result": "赢", "time": "2024-01-12"}
        ]
    }
    return jsonify({"status": "success", "data": detail})

@app.route('/api/follow_player', methods=['POST'])
def follow_player():
    data = request.get_json()
    user_id = data.get('user_id')
    follower = data.get('follower', 'me')
    if user_id not in follow_records:
        follow_records[user_id] = []
    if follower not in follow_records[user_id]:
        follow_records[user_id].append(follower)
    nickname = ''
    for r in mock_rankings_week + mock_rankings_total:
        if r['user_id'] == user_id:
            nickname = r['nickname']
            break
    return jsonify({"status": "success", "message": f"已成功跟投 {nickname}，该玩家下一笔方案下注时将通知您"})

@app.route('/api/get_home_data', methods=['GET'])
def get_home_data():
    return jsonify({"status": "success", "data": mock_home_data})

@app.route('/api/admin_verify', methods=['POST'])
def admin_verify():
    data = request.get_json()
    password = data.get('password', '')
    admin_pwd = os.environ.get('ADMIN_PASSWORD', 'Zrx19324105236')
    if password == admin_pwd:
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "密码错误"}), 403

@app.route('/api/get_user_profile', methods=['GET'])
def get_user_profile():
    return jsonify({"status": "success", "data": mock_user_profile})

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.errorhandler(404)
def not_found(e):
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)