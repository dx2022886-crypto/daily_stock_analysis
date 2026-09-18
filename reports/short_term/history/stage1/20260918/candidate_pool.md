# 《A股短线候选池（改造第1阶段）》

> 本报告只做四套原版模型自动合并、去重和模型共振统计；尚未加入题材、涨停梯队、市场情绪、竞价和开盘确认。

## 测试概况

- 阶段：`short_term_candidate_pool_v1`
- 市场：`cn`
- 每套模型返回数量：`10`
- 合并去重后的候选数量：`40`
- 报告输出数量：`30`

## 模型运行状态

| 模型 | 标签 | 状态 | 候选数量 |
| --- | --- | --- | ---: |
| `volume_breakout` | 放量突破 | success | 10 |
| `capital_heat` | 资金热度 | success | 10 |
| `momentum_quality` | 动量质量 | success | 10 |
| `oversold_reversal` | 超跌反转 | success | 10 |

## 候选池优先级

排序依次为：共振模型数量（降序）、多个模型平均原始评分（降序）、最佳模型排名（升序）。这里的排序仅表示候选池优先级，不是买入评分。

| 排名 | 股票代码 | 股票名称 | 共振数 | 入选模型 | 平均原始分 | 最佳名次 |
| ---: | --- | --- | ---: | --- | ---: | ---: |
| 1 | 600016 | 民生银行 | 1 | 超跌反转 | 88.3385 | 1 |
| 2 | 688385 | 复旦微电 | 1 | 放量突破 | 80.2255 | 1 |
| 3 | 002292 | 奥飞娱乐 | 1 | 放量突破 | 78.6402 | 2 |
| 4 | 002258 | 利尔化学 | 1 | 超跌反转 | 77.5074 | 2 |
| 5 | 002487 | 大金重工 | 1 | 超跌反转 | 77.3092 | 3 |
| 6 | 600256 | 广汇能源 | 1 | 超跌反转 | 77.1646 | 4 |
| 7 | 000425 | 徐工机械 | 1 | 超跌反转 | 76.4352 | 5 |
| 8 | 000550 | 江铃汽车 | 1 | 超跌反转 | 76.2545 | 6 |
| 9 | 002468 | 申通快递 | 1 | 超跌反转 | 76.2031 | 7 |
| 10 | 300850 | 新强联 | 1 | 超跌反转 | 75.7836 | 8 |
| 11 | 600176 | 中国巨石 | 1 | 超跌反转 | 75.7604 | 9 |
| 12 | 002008 | 大族激光 | 1 | 资金热度 | 75.6841 | 1 |
| 13 | 002156 | 通富微电 | 1 | 资金热度 | 75.2897 | 2 |
| 14 | 000725 | 京东方A | 1 | 资金热度 | 75.1053 | 3 |
| 15 | 601318 | 中国平安 | 1 | 动量质量 | 74.9241 | 1 |
| 16 | 300014 | 亿纬锂能 | 1 | 资金热度 | 74.556 | 4 |
| 17 | 300223 | 君正股份 | 1 | 资金热度 | 74.3684 | 5 |
| 18 | 605111 | 新洁能 | 1 | 资金热度 | 74.3449 | 6 |
| 19 | 000811 | 冰轮环境 | 1 | 资金热度 | 74.3023 | 7 |
| 20 | 601328 | 交通银行 | 1 | 动量质量 | 74.1674 | 2 |
| 21 | 300623 | 捷捷微电 | 1 | 资金热度 | 74.0455 | 8 |
| 22 | 601288 | 农业银行 | 1 | 动量质量 | 74.0438 | 3 |
| 23 | 688362 | 甬矽电子 | 1 | 资金热度 | 74.0438 | 9 |
| 24 | 601218 | 吉鑫科技 | 1 | 超跌反转 | 74.043 | 10 |
| 25 | 300475 | 香农芯创 | 1 | 资金热度 | 73.7787 | 10 |
| 26 | 600036 | 招商银行 | 1 | 动量质量 | 73.6257 | 4 |
| 27 | 603867 | 新化股份 | 1 | 放量突破 | 73.5152 | 3 |
| 28 | 601398 | 工商银行 | 1 | 动量质量 | 73.2146 | 5 |
| 29 | 600030 | 中信证券 | 1 | 动量质量 | 73.1051 | 6 |
| 30 | 002612 | 朗姿股份 | 1 | 放量突破 | 72.5724 | 4 |

## 模型明细与原始候选字段

完整的每套模型返回结果、每只股票的原始候选字段和策略明细请以同目录的 `candidate_pool.json` 为准。

```json
[
  {
    "code": "600016",
    "name": "民生银行",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 1,
    "best_score": 88.3385,
    "average_score": 88.3385,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 1,
        "score": 88.3385,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 1,
          "code": "600016",
          "name": "民生银行",
          "score": 88.3385,
          "screen_score": 83.93845206349206,
          "reason": "本地后置评分: value_quality、controlled_reversal",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 3.46,
          "change_pct": -2.54,
          "amount": 1293957789.0,
          "industry": "",
          "factor_scores": {
            "value": 89.8075,
            "liquidity": 87.3016,
            "momentum": 48.245,
            "reversal": 87.52,
            "activity": 79.516,
            "stability": 70.38,
            "size": 98.4127,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "600016",
              "name": "民生银行",
              "source": "tencent",
              "fetched_at": "2026-09-18T13:48:50.209568+00:00",
              "price": 3.46,
              "change_pct": -2.54,
              "change_amount": -0.09,
              "volume": 372173300,
              "amount": 1293957789.0,
              "volume_ratio": 1.36,
              "turnover_rate": 1.05,
              "amplitude": 2.82,
              "open_price": 3.54,
              "high": 3.55,
              "low": 3.45,
              "pre_close": 3.55,
              "pe_ratio": 5.27,
              "pb_ratio": 0.26,
              "total_mv": 151487000000.0,
              "circ_mv": 122699000000.0
            },
            "fundamentals": {
              "market": "cn",
              "status": "partial",
              "coverage": {
                "valuation": "not_supported",
                "growth": "failed",
                "earnings": "failed",
                "institution": "failed",
                "capital_flow": "failed",
                "dragon_tiger": "failed",
                "boards": "failed"
              },
              "valuation": {
                "status": "not_supported",
                "data": {
                  "pe_ratio": null,
                  "pb_ratio": null,
                  "total_mv": null,
                  "circ_mv": null
                }
              },
              "growth": {
                "status": "failed",
                "data": {}
              },
              "earnings": {
                "status": "failed",
                "data": {}
              },
              "institution": {
                "status": "failed",
                "data": {}
              },
              "capital_flow": {
                "status": "failed",
                "data": {}
              },
              "boards": {
                "status": "failed",
                "data": {}
              },
              "errors": [
                "fundamental_valuation timeout",
                "fundamental stage timeout",
                "fundamental stage timeout"
              ]
            },
            "news": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "events": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "warnings": []
          },
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "DSA行情: 现价 3.46, 涨跌幅 -2.54%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 1,
            "code": "600016",
            "name": "民生银行",
            "final_score": 88.3385,
            "screen_score": 83.93845206349206,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 3.46,
            "change_pct": -2.54,
            "amount": 1293957789.0,
            "total_mv": 151487168017.0,
            "turnover_rate": 1.05,
            "volume_ratio": 1.36,
            "pe_ratio": 5.27462284,
            "pb_ratio": 0.26127487,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 89.8075,
              "liquidity": 87.3016,
              "momentum": 48.245,
              "reversal": 87.52,
              "activity": 79.516,
              "stability": 70.38,
              "size": 98.4127,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: value_quality、controlled_reversal"
            },
            "post_analysis_score_deltas": {
              "scorecard": 4.4
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "value_quality",
                  "controlled_reversal"
                ]
              }
            },
            "post_analysis_tags": [
              "value_quality",
              "controlled_reversal"
            ],
            "dsa_context": {
              "enriched": true,
              "profile": "pre_rank_light",
              "news_included": false,
              "events_included": false,
              "quote": {
                "code": "600016",
                "name": "民生银行",
                "source": "tencent",
                "fetched_at": "2026-09-18T13:48:50.209568+00:00",
                "price": 3.46,
                "change_pct": -2.54,
                "change_amount": -0.09,
                "volume": 372173300,
                "amount": 1293957789.0,
                "volume_ratio": 1.36,
                "turnover_rate": 1.05,
                "amplitude": 2.82,
                "open_price": 3.54,
                "high": 3.55,
                "low": 3.45,
                "pre_close": 3.55,
                "pe_ratio": 5.27,
                "pb_ratio": 0.26,
                "total_mv": 151487000000.0,
                "circ_mv": 122699000000.0
              },
              "fundamentals": {
                "market": "cn",
                "status": "partial",
                "coverage": {
                  "valuation": "not_supported",
                  "growth": "failed",
                  "earnings": "failed",
                  "institution": "failed",
                  "capital_flow": "failed",
                  "dragon_tiger": "failed",
                  "boards": "failed"
                },
                "valuation": {
                  "status": "not_supported",
                  "data": {
                    "pe_ratio": null,
                    "pb_ratio": null,
                    "total_mv": null,
                    "circ_mv": null
                  }
                },
                "growth": {
                  "status": "failed",
                  "data": {}
                },
                "earnings": {
                  "status": "failed",
                  "data": {}
                },
                "institution": {
                  "status": "failed",
                  "data": {}
                },
                "capital_flow": {
                  "status": "failed",
                  "data": {}
                },
                "boards": {
                  "status": "failed",
                  "data": {}
                },
                "errors": [
                  "fundamental_valuation timeout",
                  "fundamental stage timeout",
                  "fundamental stage timeout"
                ]
              },
              "news": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "events": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "warnings": []
            },
            "dsa_news": [],
            "dsa_analysis_summary": "DSA行情: 现价 3.46, 涨跌幅 -2.54%",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "688385",
    "name": "复旦微电",
    "resonance_count": 1,
    "strategies": [
      "volume_breakout"
    ],
    "strategy_labels": [
      "放量突破"
    ],
    "best_rank": 1,
    "best_score": 80.2255,
    "average_score": 80.2255,
    "strategy_details": {
      "volume_breakout": {
        "rank": 1,
        "score": 80.2255,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 1,
          "code": "688385",
          "name": "复旦微电",
          "score": 80.2255,
          "screen_score": 78.025462844,
          "reason": "本地后置评分: capital_confirmed",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 59.59,
          "change_pct": 7.08,
          "amount": 1481494988.0,
          "industry": "",
          "factor_scores": {
            "value": 35.8985,
            "liquidity": 100.0,
            "momentum": 74.3262,
            "reversal": 5.0,
            "activity": 81.0674,
            "stability": 55.422,
            "size": 100.0,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "688385",
              "name": "复旦微电",
              "source": "tencent",
              "fetched_at": "2026-09-18T13:44:46.770103+00:00",
              "price": 59.59,
              "change_pct": 7.08,
              "change_amount": 3.94,
              "volume": 25203672,
              "amount": 1481494988.0,
              "volume_ratio": 2.61,
              "turnover_rate": 4.67,
              "amplitude": 8.81,
              "open_price": 56.3,
              "high": 60.55,
              "low": 55.65,
              "pre_close": 55.65,
              "pe_ratio": 55.28,
              "pb_ratio": 7.03,
              "total_mv": 49085000000.0,
              "circ_mv": 32142000000.0
            },
            "fundamentals": {
              "market": "cn",
              "status": "partial",
              "coverage": {
                "valuation": "not_supported",
                "growth": "failed",
                "earnings": "failed",
                "institution": "failed",
                "capital_flow": "failed",
                "dragon_tiger": "failed",
                "boards": "failed"
              },
              "valuation": {
                "status": "not_supported",
                "data": {
                  "pe_ratio": null,
                  "pb_ratio": null,
                  "total_mv": null,
                  "circ_mv": null
                }
              },
              "growth": {
                "status": "failed",
                "data": {}
              },
              "earnings": {
                "status": "failed",
                "data": {}
              },
              "institution": {
                "status": "failed",
                "data": {}
              },
              "capital_flow": {
                "status": "failed",
                "data": {}
              },
              "boards": {
                "status": "failed",
                "data": {}
              },
              "errors": [
                "fundamental_valuation timeout",
                "fundamental stage timeout",
                "fundamental stage timeout"
              ]
            },
            "news": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "events": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "warnings": []
          },
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "DSA行情: 现价 59.59, 涨跌幅 7.08%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 1,
            "code": "688385",
            "name": "复旦微电",
            "final_score": 80.2255,
            "screen_score": 78.025462844,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 59.59,
            "change_pct": 7.08,
            "amount": 1481494988.0,
            "total_mv": 49085430108.0,
            "turnover_rate": 4.67,
            "volume_ratio": 2.61,
            "pe_ratio": 55.2840404,
            "pb_ratio": 7.027888,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": -7.2529,
            "signal_score": 72.0,
            "ma_bullish": false,
            "price_above_ma20": true,
            "macd_status": "bullish",
            "rsi_status": "neutral",
            "breakout_20d_pct": 3.2398,
            "range_20d_pct": 19.901,
            "volume_ratio_20d": 2.2611,
            "body_pct": 5.8437,
            "pullback_to_ma20_pct": 9.8595,
            "consolidation_days_20d": 9,
            "volatility_20d_pct": 53.8399,
            "max_drawdown_20d_pct": -9.4576,
            "atr_20_pct": 3.9168,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:AkshareFetcher",
            "factor_scores": {
              "value": 35.8985,
              "liquidity": 100.0,
              "momentum": 74.3262,
              "reversal": 5.0,
              "activity": 81.0674,
              "stability": 55.422,
              "size": 100.0,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: capital_confirmed"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.2
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "capital_confirmed"
                ]
              }
            },
            "post_analysis_tags": [
              "capital_confirmed"
            ],
            "dsa_context": {
              "enriched": true,
              "profile": "pre_rank_light",
              "news_included": false,
              "events_included": false,
              "quote": {
                "code": "688385",
                "name": "复旦微电",
                "source": "tencent",
                "fetched_at": "2026-09-18T13:44:46.770103+00:00",
                "price": 59.59,
                "change_pct": 7.08,
                "change_amount": 3.94,
                "volume": 25203672,
                "amount": 1481494988.0,
                "volume_ratio": 2.61,
                "turnover_rate": 4.67,
                "amplitude": 8.81,
                "open_price": 56.3,
                "high": 60.55,
                "low": 55.65,
                "pre_close": 55.65,
                "pe_ratio": 55.28,
                "pb_ratio": 7.03,
                "total_mv": 49085000000.0,
                "circ_mv": 32142000000.0
              },
              "fundamentals": {
                "market": "cn",
                "status": "partial",
                "coverage": {
                  "valuation": "not_supported",
                  "growth": "failed",
                  "earnings": "failed",
                  "institution": "failed",
                  "capital_flow": "failed",
                  "dragon_tiger": "failed",
                  "boards": "failed"
                },
                "valuation": {
                  "status": "not_supported",
                  "data": {
                    "pe_ratio": null,
                    "pb_ratio": null,
                    "total_mv": null,
                    "circ_mv": null
                  }
                },
                "growth": {
                  "status": "failed",
                  "data": {}
                },
                "earnings": {
                  "status": "failed",
                  "data": {}
                },
                "institution": {
                  "status": "failed",
                  "data": {}
                },
                "capital_flow": {
                  "status": "failed",
                  "data": {}
                },
                "boards": {
                  "status": "failed",
                  "data": {}
                },
                "errors": [
                  "fundamental_valuation timeout",
                  "fundamental stage timeout",
                  "fundamental stage timeout"
                ]
              },
              "news": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "events": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "warnings": []
            },
            "dsa_news": [],
            "dsa_analysis_summary": "DSA行情: 现价 59.59, 涨跌幅 7.08%",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "002292",
    "name": "奥飞娱乐",
    "resonance_count": 1,
    "strategies": [
      "volume_breakout"
    ],
    "strategy_labels": [
      "放量突破"
    ],
    "best_rank": 2,
    "best_score": 78.6402,
    "average_score": 78.6402,
    "strategy_details": {
      "volume_breakout": {
        "rank": 2,
        "score": 78.6402,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 2,
          "code": "002292",
          "name": "奥飞娱乐",
          "score": 78.6402,
          "screen_score": 76.44024588738462,
          "reason": "本地后置评分: capital_confirmed",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 8.88,
          "change_pct": 2.9,
          "amount": 580913098.24,
          "industry": "",
          "factor_scores": {
            "value": 34.8771,
            "liquidity": 84.6154,
            "momentum": 74.1488,
            "reversal": 8.0201,
            "activity": 81.7116,
            "stability": 72.18,
            "size": 92.3077,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "002292",
              "name": "奥飞娱乐",
              "source": "tencent",
              "fetched_at": "2026-09-18T13:44:57.671913+00:00",
              "price": 8.88,
              "change_pct": 2.9,
              "change_amount": 0.25,
              "volume": 65338400,
              "amount": 580913098.0,
              "volume_ratio": 2.03,
              "turnover_rate": 6.42,
              "amplitude": 5.79,
              "open_price": 8.6,
              "high": 9.02,
              "low": 8.52,
              "pre_close": 8.63,
              "pe_ratio": 62.81,
              "pb_ratio": 4.33,
              "total_mv": 13131000000.0,
              "circ_mv": 9039000000.0
            },
            "fundamentals": {
              "market": "cn",
              "status": "partial",
              "coverage": {
                "valuation": "not_supported",
                "growth": "failed",
                "earnings": "failed",
                "institution": "failed",
                "capital_flow": "failed",
                "dragon_tiger": "failed",
                "boards": "failed"
              },
              "valuation": {
                "status": "not_supported",
                "data": {
                  "pe_ratio": null,
                  "pb_ratio": null,
                  "total_mv": null,
                  "circ_mv": null
                }
              },
              "growth": {
                "status": "failed",
                "data": {}
              },
              "earnings": {
                "status": "failed",
                "data": {}
              },
              "institution": {
                "status": "failed",
                "data": {}
              },
              "capital_flow": {
                "status": "failed",
                "data": {}
              },
              "boards": {
                "status": "failed",
                "data": {}
              },
              "errors": [
                "fundamental_valuation timeout",
                "fundamental stage timeout",
                "fundamental stage timeout"
              ]
            },
            "news": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "events": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "warnings": []
          },
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "DSA行情: 现价 8.88, 涨跌幅 2.9%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 2,
            "code": "002292",
            "name": "奥飞娱乐",
            "final_score": 78.6402,
            "screen_score": 76.44024588738462,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 8.88,
            "change_pct": 2.9,
            "amount": 580913098.24,
            "total_mv": 13130853309.0,
            "turnover_rate": 6.42,
            "volume_ratio": 2.03,
            "pe_ratio": 62.8070017,
            "pb_ratio": 4.33171553,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": 35.1598,
            "signal_score": 74.0,
            "ma_bullish": true,
            "price_above_ma20": true,
            "macd_status": "neutral",
            "rsi_status": "neutral",
            "breakout_20d_pct": -0.5599,
            "range_20d_pct": 17.9085,
            "volume_ratio_20d": 1.4751,
            "body_pct": 3.2558,
            "pullback_to_ma20_pct": 5.2756,
            "consolidation_days_20d": 17,
            "volatility_20d_pct": 38.4562,
            "max_drawdown_20d_pct": -6.3636,
            "atr_20_pct": 3.6036,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:AkshareFetcher",
            "factor_scores": {
              "value": 34.8771,
              "liquidity": 84.6154,
              "momentum": 74.1488,
              "reversal": 8.0201,
              "activity": 81.7116,
              "stability": 72.18,
              "size": 92.3077,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: capital_confirmed"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.2
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "capital_confirmed"
                ]
              }
            },
            "post_analysis_tags": [
              "capital_confirmed"
            ],
            "dsa_context": {
              "enriched": true,
              "profile": "pre_rank_light",
              "news_included": false,
              "events_included": false,
              "quote": {
                "code": "002292",
                "name": "奥飞娱乐",
                "source": "tencent",
                "fetched_at": "2026-09-18T13:44:57.671913+00:00",
                "price": 8.88,
                "change_pct": 2.9,
                "change_amount": 0.25,
                "volume": 65338400,
                "amount": 580913098.0,
                "volume_ratio": 2.03,
                "turnover_rate": 6.42,
                "amplitude": 5.79,
                "open_price": 8.6,
                "high": 9.02,
                "low": 8.52,
                "pre_close": 8.63,
                "pe_ratio": 62.81,
                "pb_ratio": 4.33,
                "total_mv": 13131000000.0,
                "circ_mv": 9039000000.0
              },
              "fundamentals": {
                "market": "cn",
                "status": "partial",
                "coverage": {
                  "valuation": "not_supported",
                  "growth": "failed",
                  "earnings": "failed",
                  "institution": "failed",
                  "capital_flow": "failed",
                  "dragon_tiger": "failed",
                  "boards": "failed"
                },
                "valuation": {
                  "status": "not_supported",
                  "data": {
                    "pe_ratio": null,
                    "pb_ratio": null,
                    "total_mv": null,
                    "circ_mv": null
                  }
                },
                "growth": {
                  "status": "failed",
                  "data": {}
                },
                "earnings": {
                  "status": "failed",
                  "data": {}
                },
                "institution": {
                  "status": "failed",
                  "data": {}
                },
                "capital_flow": {
                  "status": "failed",
                  "data": {}
                },
                "boards": {
                  "status": "failed",
                  "data": {}
                },
                "errors": [
                  "fundamental_valuation timeout",
                  "fundamental stage timeout",
                  "fundamental stage timeout"
                ]
              },
              "news": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "events": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "warnings": []
            },
            "dsa_news": [],
            "dsa_analysis_summary": "DSA行情: 现价 8.88, 涨跌幅 2.9%",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "002258",
    "name": "利尔化学",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 2,
    "best_score": 77.5074,
    "average_score": 77.5074,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 2,
        "score": 77.5074,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 2,
          "code": "002258",
          "name": "利尔化学",
          "score": 77.5074,
          "screen_score": 75.50735507936508,
          "reason": "本地后置评分: controlled_reversal",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 14.69,
          "change_pct": -2.46,
          "amount": 356926592.1,
          "industry": "",
          "factor_scores": {
            "value": 67.7639,
            "liquidity": 60.3175,
            "momentum": 48.505,
            "reversal": 86.48,
            "activity": 84.8665,
            "stability": 70.62,
            "size": 53.9683,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "002258",
              "name": "利尔化学",
              "source": "tencent",
              "fetched_at": "2026-09-18T13:49:10.104889+00:00",
              "price": 14.69,
              "change_pct": -2.46,
              "change_amount": -0.37,
              "volume": 24090800,
              "amount": 356926592.0,
              "volume_ratio": 1.0,
              "turnover_rate": 3.01,
              "amplitude": 3.59,
              "open_price": 15.06,
              "high": 15.19,
              "low": 14.65,
              "pre_close": 15.06,
              "pe_ratio": 25.69,
              "pb_ratio": 1.47,
              "total_mv": 11758000000.0,
              "circ_mv": 11738000000.0
            },
            "fundamentals": {
              "market": "cn",
              "status": "partial",
              "coverage": {
                "valuation": "not_supported",
                "growth": "failed",
                "earnings": "failed",
                "institution": "failed",
                "capital_flow": "failed",
                "dragon_tiger": "failed",
                "boards": "failed"
              },
              "valuation": {
                "status": "not_supported",
                "data": {
                  "pe_ratio": null,
                  "pb_ratio": null,
                  "total_mv": null,
                  "circ_mv": null
                }
              },
              "growth": {
                "status": "failed",
                "data": {}
              },
              "earnings": {
                "status": "failed",
                "data": {}
              },
              "institution": {
                "status": "failed",
                "data": {}
              },
              "capital_flow": {
                "status": "failed",
                "data": {}
              },
              "boards": {
                "status": "failed",
                "data": {}
              },
              "errors": [
                "fundamental_valuation timeout",
                "fundamental stage timeout",
                "fundamental stage timeout"
              ]
            },
            "news": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "events": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "warnings": []
          },
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "DSA行情: 现价 14.69, 涨跌幅 -2.46%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: controlled_reversal"
          },
          "post_analysis_tags": [
            "controlled_reversal"
          ],
          "raw": {
            "rank": 2,
            "code": "002258",
            "name": "利尔化学",
            "final_score": 77.5074,
            "screen_score": 75.50735507936508,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 14.69,
            "change_pct": -2.46,
            "amount": 356926592.1,
            "total_mv": 11758422879.0,
            "turnover_rate": 3.01,
            "volume_ratio": 1.0,
            "pe_ratio": 25.6875317,
            "pb_ratio": 1.47411516,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 67.7639,
              "liquidity": 60.3175,
              "momentum": 48.505,
              "reversal": 86.48,
              "activity": 84.8665,
              "stability": 70.62,
              "size": 53.9683,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: controlled_reversal"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.0
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "controlled_reversal"
                ]
              }
            },
            "post_analysis_tags": [
              "controlled_reversal"
            ],
            "dsa_context": {
              "enriched": true,
              "profile": "pre_rank_light",
              "news_included": false,
              "events_included": false,
              "quote": {
                "code": "002258",
                "name": "利尔化学",
                "source": "tencent",
                "fetched_at": "2026-09-18T13:49:10.104889+00:00",
                "price": 14.69,
                "change_pct": -2.46,
                "change_amount": -0.37,
                "volume": 24090800,
                "amount": 356926592.0,
                "volume_ratio": 1.0,
                "turnover_rate": 3.01,
                "amplitude": 3.59,
                "open_price": 15.06,
                "high": 15.19,
                "low": 14.65,
                "pre_close": 15.06,
                "pe_ratio": 25.69,
                "pb_ratio": 1.47,
                "total_mv": 11758000000.0,
                "circ_mv": 11738000000.0
              },
              "fundamentals": {
                "market": "cn",
                "status": "partial",
                "coverage": {
                  "valuation": "not_supported",
                  "growth": "failed",
                  "earnings": "failed",
                  "institution": "failed",
                  "capital_flow": "failed",
                  "dragon_tiger": "failed",
                  "boards": "failed"
                },
                "valuation": {
                  "status": "not_supported",
                  "data": {
                    "pe_ratio": null,
                    "pb_ratio": null,
                    "total_mv": null,
                    "circ_mv": null
                  }
                },
                "growth": {
                  "status": "failed",
                  "data": {}
                },
                "earnings": {
                  "status": "failed",
                  "data": {}
                },
                "institution": {
                  "status": "failed",
                  "data": {}
                },
                "capital_flow": {
                  "status": "failed",
                  "data": {}
                },
                "boards": {
                  "status": "failed",
                  "data": {}
                },
                "errors": [
                  "fundamental_valuation timeout",
                  "fundamental stage timeout",
                  "fundamental stage timeout"
                ]
              },
              "news": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "events": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "warnings": []
            },
            "dsa_news": [],
            "dsa_analysis_summary": "DSA行情: 现价 14.69, 涨跌幅 -2.46%",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "002487",
    "name": "大金重工",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 3,
    "best_score": 77.3092,
    "average_score": 77.3092,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 3,
        "score": 77.3092,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 3,
          "code": "002487",
          "name": "大金重工",
          "score": 77.3092,
          "screen_score": 78.30918015873016,
          "reason": "本地后置评分: controlled_reversal",
          "risk_level": "low",
          "risk_flags": [
            "high_turnover"
          ],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 39.6,
          "change_pct": -3.91,
          "amount": 3401154741.76,
          "industry": "",
          "factor_scores": {
            "value": 55.4742,
            "liquidity": 95.2381,
            "momentum": 43.7925,
            "reversal": 94.67,
            "activity": 43.0075,
            "stability": 59.21,
            "size": 84.127,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "002487",
              "name": "大金重工",
              "source": "tencent",
              "fetched_at": "2026-09-18T13:49:00.931646+00:00",
              "price": 39.6,
              "change_pct": -3.91,
              "change_amount": -1.61,
              "volume": 85372800,
              "amount": 3401154742.0,
              "volume_ratio": 0.88,
              "turnover_rate": 13.53,
              "amplitude": 3.62,
              "open_price": 40.8,
              "high": 40.88,
              "low": 39.39,
              "pre_close": 41.21,
              "pe_ratio": 25.32,
              "pb_ratio": 2.03,
              "total_mv": 29307000000.0,
              "circ_mv": 24984000000.0
            },
            "fundamentals": {
              "market": "cn",
              "status": "partial",
              "coverage": {
                "valuation": "not_supported",
                "growth": "failed",
                "earnings": "failed",
                "institution": "failed",
                "capital_flow": "failed",
                "dragon_tiger": "failed",
                "boards": "failed"
              },
              "valuation": {
                "status": "not_supported",
                "data": {
                  "pe_ratio": null,
                  "pb_ratio": null,
                  "total_mv": null,
                  "circ_mv": null
                }
              },
              "growth": {
                "status": "failed",
                "data": {}
              },
              "earnings": {
                "status": "failed",
                "data": {}
              },
              "institution": {
                "status": "failed",
                "data": {}
              },
              "capital_flow": {
                "status": "failed",
                "data": {}
              },
              "boards": {
                "status": "failed",
                "data": {}
              },
              "errors": [
                "fundamental_valuation timeout",
                "fundamental stage timeout",
                "fundamental stage timeout"
              ]
            },
            "news": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "events": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "warnings": []
          },
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "DSA行情: 现价 39.6, 涨跌幅 -3.91%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: controlled_reversal"
          },
          "post_analysis_tags": [
            "controlled_reversal"
          ],
          "raw": {
            "rank": 3,
            "code": "002487",
            "name": "大金重工",
            "final_score": 77.3092,
            "screen_score": 78.30918015873016,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 39.6,
            "change_pct": -3.91,
            "amount": 3401154741.76,
            "total_mv": 29307399620.0,
            "turnover_rate": 13.53,
            "volume_ratio": 0.88,
            "pe_ratio": 25.32287086,
            "pb_ratio": 2.02999647,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 55.4742,
              "liquidity": 95.2381,
              "momentum": 43.7925,
              "reversal": 94.67,
              "activity": 43.0075,
              "stability": 59.21,
              "size": 84.127,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 25.0,
            "risk_level": "low",
            "risk_penalty": 3.0,
            "risk_flags": [
              "high_turnover"
            ],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: controlled_reversal"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.0
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "controlled_reversal"
                ]
              }
            },
            "post_analysis_tags": [
              "controlled_reversal"
            ],
            "dsa_context": {
              "enriched": true,
              "profile": "pre_rank_light",
              "news_included": false,
              "events_included": false,
              "quote": {
                "code": "002487",
                "name": "大金重工",
                "source": "tencent",
                "fetched_at": "2026-09-18T13:49:00.931646+00:00",
                "price": 39.6,
                "change_pct": -3.91,
                "change_amount": -1.61,
                "volume": 85372800,
                "amount": 3401154742.0,
                "volume_ratio": 0.88,
                "turnover_rate": 13.53,
                "amplitude": 3.62,
                "open_price": 40.8,
                "high": 40.88,
                "low": 39.39,
                "pre_close": 41.21,
                "pe_ratio": 25.32,
                "pb_ratio": 2.03,
                "total_mv": 29307000000.0,
                "circ_mv": 24984000000.0
              },
              "fundamentals": {
                "market": "cn",
                "status": "partial",
                "coverage": {
                  "valuation": "not_supported",
                  "growth": "failed",
                  "earnings": "failed",
                  "institution": "failed",
                  "capital_flow": "failed",
                  "dragon_tiger": "failed",
                  "boards": "failed"
                },
                "valuation": {
                  "status": "not_supported",
                  "data": {
                    "pe_ratio": null,
                    "pb_ratio": null,
                    "total_mv": null,
                    "circ_mv": null
                  }
                },
                "growth": {
                  "status": "failed",
                  "data": {}
                },
                "earnings": {
                  "status": "failed",
                  "data": {}
                },
                "institution": {
                  "status": "failed",
                  "data": {}
                },
                "capital_flow": {
                  "status": "failed",
                  "data": {}
                },
                "boards": {
                  "status": "failed",
                  "data": {}
                },
                "errors": [
                  "fundamental_valuation timeout",
                  "fundamental stage timeout",
                  "fundamental stage timeout"
                ]
              },
              "news": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "events": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "warnings": []
            },
            "dsa_news": [],
            "dsa_analysis_summary": "DSA行情: 现价 39.6, 涨跌幅 -3.91%",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "600256",
    "name": "广汇能源",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 4,
    "best_score": 77.1646,
    "average_score": 77.1646,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 4,
        "score": 77.1646,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 4,
          "code": "600256",
          "name": "广汇能源",
          "score": 77.1646,
          "screen_score": 75.1646096031746,
          "reason": "本地后置评分: controlled_reversal",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 6.72,
          "change_pct": -1.9,
          "amount": 858018332.0,
          "industry": "",
          "factor_scores": {
            "value": 65.1806,
            "liquidity": 76.1905,
            "momentum": 50.325,
            "reversal": 79.2,
            "activity": 81.3573,
            "stability": 72.3,
            "size": 88.8889,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: controlled_reversal"
          },
          "post_analysis_tags": [
            "controlled_reversal"
          ],
          "raw": {
            "rank": 4,
            "code": "600256",
            "name": "广汇能源",
            "final_score": 77.1646,
            "screen_score": 75.1646096031746,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 6.72,
            "change_pct": -1.9,
            "amount": 858018332.0,
            "total_mv": 42954259918.0,
            "turnover_rate": 1.99,
            "volume_ratio": 1.02,
            "pe_ratio": 24.26472778,
            "pb_ratio": 1.71892223,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 65.1806,
              "liquidity": 76.1905,
              "momentum": 50.325,
              "reversal": 79.2,
              "activity": 81.3573,
              "stability": 72.3,
              "size": 88.8889,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: controlled_reversal"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.0
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "controlled_reversal"
                ]
              }
            },
            "post_analysis_tags": [
              "controlled_reversal"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "000425",
    "name": "徐工机械",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 5,
    "best_score": 76.4352,
    "average_score": 76.4352,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 5,
        "score": 76.4352,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 5,
          "code": "000425",
          "name": "徐工机械",
          "score": 76.4352,
          "screen_score": 74.03524591269841,
          "reason": "本地后置评分: value_quality",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 7.45,
          "change_pct": -1.19,
          "amount": 884547927.77,
          "industry": "",
          "factor_scores": {
            "value": 77.7044,
            "liquidity": 77.7778,
            "momentum": 52.6325,
            "reversal": 69.97,
            "activity": 78.8091,
            "stability": 74.43,
            "size": 93.6508,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality"
          },
          "post_analysis_tags": [
            "value_quality"
          ],
          "raw": {
            "rank": 5,
            "code": "000425",
            "name": "徐工机械",
            "final_score": 76.4352,
            "screen_score": 74.03524591269841,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 7.45,
            "change_pct": -1.19,
            "amount": 884547927.77,
            "total_mv": 87248517845.0,
            "turnover_rate": 1.32,
            "volume_ratio": 0.99,
            "pe_ratio": 14.12741863,
            "pb_ratio": 1.35148955,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 77.7044,
              "liquidity": 77.7778,
              "momentum": 52.6325,
              "reversal": 69.97,
              "activity": 78.8091,
              "stability": 74.43,
              "size": 93.6508,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: value_quality"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.4
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "value_quality"
                ]
              }
            },
            "post_analysis_tags": [
              "value_quality"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "000550",
    "name": "江铃汽车",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 6,
    "best_score": 76.2545,
    "average_score": 76.2545,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 6,
        "score": 76.2545,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 6,
          "code": "000550",
          "name": "江铃汽车",
          "score": 76.2545,
          "screen_score": 71.85451694444446,
          "reason": "本地后置评分: value_quality、controlled_reversal",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 16.69,
          "change_pct": -3.75,
          "amount": 98943573.98,
          "industry": "",
          "factor_scores": {
            "value": 81.4028,
            "liquidity": 11.1111,
            "momentum": 44.3125,
            "reversal": 96.75,
            "activity": 79.6679,
            "stability": 66.75,
            "size": 68.254,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 6,
            "code": "000550",
            "name": "江铃汽车",
            "final_score": 76.2545,
            "screen_score": 71.85451694444446,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 16.69,
            "change_pct": -3.75,
            "amount": 98943573.98,
            "total_mv": 14407041660.0,
            "turnover_rate": 1.13,
            "volume_ratio": 1.33,
            "pe_ratio": 12.07085044,
            "pb_ratio": 1.20423007,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 81.4028,
              "liquidity": 11.1111,
              "momentum": 44.3125,
              "reversal": 96.75,
              "activity": 79.6679,
              "stability": 66.75,
              "size": 68.254,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: value_quality、controlled_reversal"
            },
            "post_analysis_score_deltas": {
              "scorecard": 4.4
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "value_quality",
                  "controlled_reversal"
                ]
              }
            },
            "post_analysis_tags": [
              "value_quality",
              "controlled_reversal"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "002468",
    "name": "申通快递",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 7,
    "best_score": 76.2031,
    "average_score": 76.2031,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 7,
        "score": 76.2031,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 7,
          "code": "002468",
          "name": "申通快递",
          "score": 76.2031,
          "screen_score": 74.20312452380952,
          "reason": "本地后置评分: controlled_reversal",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 14.9,
          "change_pct": -2.04,
          "amount": 387116653.32,
          "industry": "",
          "factor_scores": {
            "value": 71.256,
            "liquidity": 61.9048,
            "momentum": 49.87,
            "reversal": 81.02,
            "activity": 81.2552,
            "stability": 71.88,
            "size": 79.3651,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: controlled_reversal"
          },
          "post_analysis_tags": [
            "controlled_reversal"
          ],
          "raw": {
            "rank": 7,
            "code": "002468",
            "name": "申通快递",
            "final_score": 76.2031,
            "screen_score": 74.20312452380952,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 14.9,
            "change_pct": -2.04,
            "amount": 387116653.32,
            "total_mv": 22808952273.0,
            "turnover_rate": 1.76,
            "volume_ratio": 2.02,
            "pe_ratio": 11.69555428,
            "pb_ratio": 1.93994513,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 71.256,
              "liquidity": 61.9048,
              "momentum": 49.87,
              "reversal": 81.02,
              "activity": 81.2552,
              "stability": 71.88,
              "size": 79.3651,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: controlled_reversal"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.0
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "controlled_reversal"
                ]
              }
            },
            "post_analysis_tags": [
              "controlled_reversal"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "300850",
    "name": "新强联",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 8,
    "best_score": 75.7836,
    "average_score": 75.7836,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 8,
        "score": 75.7836,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 8,
          "code": "300850",
          "name": "新强联",
          "score": 75.7836,
          "screen_score": 73.7835861904762,
          "reason": "本地后置评分: controlled_reversal",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 28.85,
          "change_pct": -1.84,
          "amount": 452835969.4,
          "industry": "",
          "factor_scores": {
            "value": 72.8512,
            "liquidity": 65.0794,
            "momentum": 50.52,
            "reversal": 78.42,
            "activity": 75.8185,
            "stability": 72.48,
            "size": 55.5556,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: controlled_reversal"
          },
          "post_analysis_tags": [
            "controlled_reversal"
          ],
          "raw": {
            "rank": 8,
            "code": "300850",
            "name": "新强联",
            "final_score": 75.7836,
            "screen_score": 73.7835861904762,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 28.85,
            "change_pct": -1.84,
            "amount": 452835969.4,
            "total_mv": 11946376340.0,
            "turnover_rate": 5.12,
            "volume_ratio": 0.68,
            "pe_ratio": 14.39532703,
            "pb_ratio": 1.63831963,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 72.8512,
              "liquidity": 65.0794,
              "momentum": 50.52,
              "reversal": 78.42,
              "activity": 75.8185,
              "stability": 72.48,
              "size": 55.5556,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: controlled_reversal"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.0
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "controlled_reversal"
                ]
              }
            },
            "post_analysis_tags": [
              "controlled_reversal"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "600176",
    "name": "中国巨石",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 9,
    "best_score": 75.7604,
    "average_score": 75.7604,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 9,
        "score": 75.7604,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 9,
          "code": "600176",
          "name": "中国巨石",
          "score": 75.7604,
          "screen_score": 73.7604355952381,
          "reason": "本地后置评分: controlled_reversal",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 45.02,
          "change_pct": -4.52,
          "amount": 17750491171.0,
          "industry": "",
          "factor_scores": {
            "value": 27.9702,
            "liquidity": 100.0,
            "momentum": 40.796,
            "reversal": 86.74,
            "activity": 61.6866,
            "stability": 64.44,
            "size": 100.0,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: controlled_reversal"
          },
          "post_analysis_tags": [
            "controlled_reversal"
          ],
          "raw": {
            "rank": 9,
            "code": "600176",
            "name": "中国巨石",
            "final_score": 75.7604,
            "screen_score": 73.7604355952381,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 45.02,
            "change_pct": -4.52,
            "amount": 17750491171.0,
            "total_mv": 180221215495.0,
            "turnover_rate": 9.89,
            "volume_ratio": 1.35,
            "pe_ratio": 39.76886883,
            "pb_ratio": 5.43571827,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 27.9702,
              "liquidity": 100.0,
              "momentum": 40.796,
              "reversal": 86.74,
              "activity": 61.6866,
              "stability": 64.44,
              "size": 100.0,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: controlled_reversal"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.0
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "controlled_reversal"
                ]
              }
            },
            "post_analysis_tags": [
              "controlled_reversal"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "002008",
    "name": "大族激光",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 1,
    "best_score": 75.6841,
    "average_score": 75.6841,
    "strategy_details": {
      "capital_heat": {
        "rank": 1,
        "score": 75.6841,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 1,
          "code": "002008",
          "name": "大族激光",
          "score": 75.6841,
          "screen_score": 73.28412789473684,
          "reason": "本地后置评分: capital_confirmed",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 99.6,
          "change_pct": 5.05,
          "amount": 5820857507.42,
          "industry": "",
          "factor_scores": {
            "value": 53.8074,
            "liquidity": 97.8947,
            "momentum": 72.9125,
            "reversal": 5.0,
            "activity": 81.4428,
            "stability": 62.85,
            "size": 96.8421,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "002008",
              "name": "大族激光",
              "source": "tencent",
              "fetched_at": "2026-09-18T13:46:31.273472+00:00",
              "price": 99.6,
              "change_pct": 5.05,
              "change_amount": 4.79,
              "volume": 59650300,
              "amount": 5820857507.0,
              "volume_ratio": 1.62,
              "turnover_rate": 6.23,
              "amplitude": 7.69,
              "open_price": 97.03,
              "high": 100.89,
              "low": 93.6,
              "pre_close": 94.81,
              "pe_ratio": 51.55,
              "pb_ratio": 4.78,
              "total_mv": 102548000000.0,
              "circ_mv": 95290000000.0
            },
            "fundamentals": {
              "market": "cn",
              "status": "partial",
              "coverage": {
                "valuation": "not_supported",
                "growth": "failed",
                "earnings": "failed",
                "institution": "failed",
                "capital_flow": "failed",
                "dragon_tiger": "failed",
                "boards": "failed"
              },
              "valuation": {
                "status": "not_supported",
                "data": {
                  "pe_ratio": null,
                  "pb_ratio": null,
                  "total_mv": null,
                  "circ_mv": null
                }
              },
              "growth": {
                "status": "failed",
                "data": {}
              },
              "earnings": {
                "status": "failed",
                "data": {}
              },
              "institution": {
                "status": "failed",
                "data": {}
              },
              "capital_flow": {
                "status": "failed",
                "data": {}
              },
              "boards": {
                "status": "failed",
                "data": {}
              },
              "errors": [
                "fundamental_valuation timeout",
                "fundamental stage timeout",
                "fundamental stage timeout"
              ]
            },
            "news": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "events": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "warnings": []
          },
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "DSA行情: 现价 99.6, 涨跌幅 5.05%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 1,
            "code": "002008",
            "name": "大族激光",
            "final_score": 75.6841,
            "screen_score": 73.28412789473684,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 99.6,
            "change_pct": 5.05,
            "amount": 5820857507.42,
            "total_mv": 102548499437.0,
            "turnover_rate": 6.23,
            "volume_ratio": 1.62,
            "pe_ratio": 51.54493112,
            "pb_ratio": 4.77828203,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 53.8074,
              "liquidity": 97.8947,
              "momentum": 72.9125,
              "reversal": 5.0,
              "activity": 81.4428,
              "stability": 62.85,
              "size": 96.8421,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: capital_confirmed"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.4
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "capital_confirmed"
                ]
              }
            },
            "post_analysis_tags": [
              "capital_confirmed"
            ],
            "dsa_context": {
              "enriched": true,
              "profile": "pre_rank_light",
              "news_included": false,
              "events_included": false,
              "quote": {
                "code": "002008",
                "name": "大族激光",
                "source": "tencent",
                "fetched_at": "2026-09-18T13:46:31.273472+00:00",
                "price": 99.6,
                "change_pct": 5.05,
                "change_amount": 4.79,
                "volume": 59650300,
                "amount": 5820857507.0,
                "volume_ratio": 1.62,
                "turnover_rate": 6.23,
                "amplitude": 7.69,
                "open_price": 97.03,
                "high": 100.89,
                "low": 93.6,
                "pre_close": 94.81,
                "pe_ratio": 51.55,
                "pb_ratio": 4.78,
                "total_mv": 102548000000.0,
                "circ_mv": 95290000000.0
              },
              "fundamentals": {
                "market": "cn",
                "status": "partial",
                "coverage": {
                  "valuation": "not_supported",
                  "growth": "failed",
                  "earnings": "failed",
                  "institution": "failed",
                  "capital_flow": "failed",
                  "dragon_tiger": "failed",
                  "boards": "failed"
                },
                "valuation": {
                  "status": "not_supported",
                  "data": {
                    "pe_ratio": null,
                    "pb_ratio": null,
                    "total_mv": null,
                    "circ_mv": null
                  }
                },
                "growth": {
                  "status": "failed",
                  "data": {}
                },
                "earnings": {
                  "status": "failed",
                  "data": {}
                },
                "institution": {
                  "status": "failed",
                  "data": {}
                },
                "capital_flow": {
                  "status": "failed",
                  "data": {}
                },
                "boards": {
                  "status": "failed",
                  "data": {}
                },
                "errors": [
                  "fundamental_valuation timeout",
                  "fundamental stage timeout",
                  "fundamental stage timeout"
                ]
              },
              "news": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "events": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "warnings": []
            },
            "dsa_news": [],
            "dsa_analysis_summary": "DSA行情: 现价 99.6, 涨跌幅 5.05%",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "002156",
    "name": "通富微电",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 2,
    "best_score": 75.2897,
    "average_score": 75.2897,
    "strategy_details": {
      "capital_heat": {
        "rank": 2,
        "score": 75.2897,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 2,
          "code": "002156",
          "name": "通富微电",
          "score": 75.2897,
          "screen_score": 72.88974894736842,
          "reason": "本地后置评分: capital_confirmed",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 61.38,
          "change_pct": 5.26,
          "amount": 7245757813.1,
          "industry": "",
          "factor_scores": {
            "value": 52.6575,
            "liquidity": 98.9474,
            "momentum": 73.595,
            "reversal": 5.0,
            "activity": 78.8778,
            "stability": 62.22,
            "size": 95.7895,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "002156",
              "name": "通富微电",
              "source": "tencent",
              "fetched_at": "2026-09-18T13:46:40.377807+00:00",
              "price": 61.38,
              "change_pct": 5.26,
              "change_amount": 3.07,
              "volume": 119168400,
              "amount": 7245757813.0,
              "volume_ratio": 2.34,
              "turnover_rate": 7.85,
              "amplitude": 5.66,
              "open_price": 59.7,
              "high": 62.23,
              "low": 58.93,
              "pre_close": 58.31,
              "pe_ratio": 38.76,
              "pb_ratio": 4.65,
              "total_mv": 97827000000.0,
              "circ_mv": 93141000000.0
            },
            "fundamentals": {
              "market": "cn",
              "status": "partial",
              "coverage": {
                "valuation": "not_supported",
                "growth": "failed",
                "earnings": "failed",
                "institution": "failed",
                "capital_flow": "failed",
                "dragon_tiger": "failed",
                "boards": "failed"
              },
              "valuation": {
                "status": "not_supported",
                "data": {
                  "pe_ratio": null,
                  "pb_ratio": null,
                  "total_mv": null,
                  "circ_mv": null
                }
              },
              "growth": {
                "status": "failed",
                "data": {}
              },
              "earnings": {
                "status": "failed",
                "data": {}
              },
              "institution": {
                "status": "failed",
                "data": {}
              },
              "capital_flow": {
                "status": "failed",
                "data": {}
              },
              "boards": {
                "status": "failed",
                "data": {}
              },
              "errors": [
                "fundamental_valuation timeout",
                "fundamental stage timeout",
                "fundamental stage timeout"
              ]
            },
            "news": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "events": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "warnings": []
          },
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "DSA行情: 现价 61.38, 涨跌幅 5.26%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 2,
            "code": "002156",
            "name": "通富微电",
            "final_score": 75.2897,
            "screen_score": 72.88974894736842,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 61.38,
            "change_pct": 5.26,
            "amount": 7245757813.1,
            "total_mv": 97827303194.0,
            "turnover_rate": 7.85,
            "volume_ratio": 2.34,
            "pe_ratio": 38.75769113,
            "pb_ratio": 5.80838753,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 52.6575,
              "liquidity": 98.9474,
              "momentum": 73.595,
              "reversal": 5.0,
              "activity": 78.8778,
              "stability": 62.22,
              "size": 95.7895,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: capital_confirmed"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.4
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "capital_confirmed"
                ]
              }
            },
            "post_analysis_tags": [
              "capital_confirmed"
            ],
            "dsa_context": {
              "enriched": true,
              "profile": "pre_rank_light",
              "news_included": false,
              "events_included": false,
              "quote": {
                "code": "002156",
                "name": "通富微电",
                "source": "tencent",
                "fetched_at": "2026-09-18T13:46:40.377807+00:00",
                "price": 61.38,
                "change_pct": 5.26,
                "change_amount": 3.07,
                "volume": 119168400,
                "amount": 7245757813.0,
                "volume_ratio": 2.34,
                "turnover_rate": 7.85,
                "amplitude": 5.66,
                "open_price": 59.7,
                "high": 62.23,
                "low": 58.93,
                "pre_close": 58.31,
                "pe_ratio": 38.76,
                "pb_ratio": 4.65,
                "total_mv": 97827000000.0,
                "circ_mv": 93141000000.0
              },
              "fundamentals": {
                "market": "cn",
                "status": "partial",
                "coverage": {
                  "valuation": "not_supported",
                  "growth": "failed",
                  "earnings": "failed",
                  "institution": "failed",
                  "capital_flow": "failed",
                  "dragon_tiger": "failed",
                  "boards": "failed"
                },
                "valuation": {
                  "status": "not_supported",
                  "data": {
                    "pe_ratio": null,
                    "pb_ratio": null,
                    "total_mv": null,
                    "circ_mv": null
                  }
                },
                "growth": {
                  "status": "failed",
                  "data": {}
                },
                "earnings": {
                  "status": "failed",
                  "data": {}
                },
                "institution": {
                  "status": "failed",
                  "data": {}
                },
                "capital_flow": {
                  "status": "failed",
                  "data": {}
                },
                "boards": {
                  "status": "failed",
                  "data": {}
                },
                "errors": [
                  "fundamental_valuation timeout",
                  "fundamental stage timeout",
                  "fundamental stage timeout"
                ]
              },
              "news": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "events": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "warnings": []
            },
            "dsa_news": [],
            "dsa_analysis_summary": "DSA行情: 现价 61.38, 涨跌幅 5.26%",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "000725",
    "name": "京东方A",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 3,
    "best_score": 75.1053,
    "average_score": 75.1053,
    "strategy_details": {
      "capital_heat": {
        "rank": 3,
        "score": 75.1053,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 3,
          "code": "000725",
          "name": "京东方A",
          "score": 75.1053,
          "screen_score": 72.70531000000001,
          "reason": "本地后置评分: value_quality",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 5.92,
          "change_pct": 2.96,
          "amount": 12355533158.78,
          "industry": "",
          "factor_scores": {
            "value": 82.2925,
            "liquidity": 100.0,
            "momentum": 66.12,
            "reversal": 6.84,
            "activity": 83.4332,
            "stability": 69.12,
            "size": 100.0,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality"
          },
          "post_analysis_tags": [
            "value_quality"
          ],
          "raw": {
            "rank": 3,
            "code": "000725",
            "name": "京东方A",
            "final_score": 75.1053,
            "screen_score": 72.70531000000001,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 5.92,
            "change_pct": 2.96,
            "amount": 12355533158.78,
            "total_mv": 219302422139.0,
            "turnover_rate": 5.97,
            "volume_ratio": 1.9,
            "pe_ratio": 27.90909254,
            "pb_ratio": 1.64719993,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 82.2925,
              "liquidity": 100.0,
              "momentum": 66.12,
              "reversal": 6.84,
              "activity": 83.4332,
              "stability": 69.12,
              "size": 100.0,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: value_quality"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.4
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "value_quality"
                ]
              }
            },
            "post_analysis_tags": [
              "value_quality"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "601318",
    "name": "中国平安",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 1,
    "best_score": 74.9241,
    "average_score": 74.9241,
    "strategy_details": {
      "momentum_quality": {
        "rank": 1,
        "score": 74.9241,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 1,
          "code": "601318",
          "name": "中国平安",
          "score": 74.9241,
          "screen_score": 73.12414318771626,
          "reason": "本地后置评分: value_quality",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 53.37,
          "change_pct": 0.04,
          "amount": 3266258427.0,
          "industry": "",
          "factor_scores": {
            "value": 85.6484,
            "liquidity": 96.3668,
            "momentum": 56.63,
            "reversal": 60.48,
            "activity": 68.9849,
            "stability": 77.88,
            "size": 98.0969,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "601318",
              "name": "中国平安",
              "source": "tencent",
              "fetched_at": "2026-09-18T13:47:20.382660+00:00",
              "price": 53.37,
              "change_pct": 0.04,
              "change_amount": 0.02,
              "volume": 61166700,
              "amount": 3266258427.0,
              "volume_ratio": 1.21,
              "turnover_rate": 0.57,
              "amplitude": 1.44,
              "open_price": 53.32,
              "high": 53.8,
              "low": 53.03,
              "pre_close": 53.35,
              "pe_ratio": 6.07,
              "pb_ratio": 0.96,
              "total_mv": 966404999999.9999,
              "circ_mv": 568928000000.0
            },
            "fundamentals": {
              "market": "cn",
              "status": "partial",
              "coverage": {
                "valuation": "not_supported",
                "growth": "failed",
                "earnings": "failed",
                "institution": "failed",
                "capital_flow": "failed",
                "dragon_tiger": "failed",
                "boards": "failed"
              },
              "valuation": {
                "status": "not_supported",
                "data": {
                  "pe_ratio": null,
                  "pb_ratio": null,
                  "total_mv": null,
                  "circ_mv": null
                }
              },
              "growth": {
                "status": "failed",
                "data": {}
              },
              "earnings": {
                "status": "failed",
                "data": {}
              },
              "institution": {
                "status": "failed",
                "data": {}
              },
              "capital_flow": {
                "status": "failed",
                "data": {}
              },
              "boards": {
                "status": "failed",
                "data": {}
              },
              "errors": [
                "fundamental_valuation timeout",
                "fundamental stage timeout",
                "fundamental stage timeout"
              ]
            },
            "news": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "events": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "warnings": []
          },
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "DSA行情: 现价 53.37, 涨跌幅 0.04%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality"
          },
          "post_analysis_tags": [
            "value_quality"
          ],
          "raw": {
            "rank": 1,
            "code": "601318",
            "name": "中国平安",
            "final_score": 74.9241,
            "screen_score": 73.12414318771626,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 53.37,
            "change_pct": 0.04,
            "amount": 3266258427.0,
            "total_mv": 966404853273.0,
            "turnover_rate": 0.57,
            "volume_ratio": 1.21,
            "pe_ratio": 6.06596232,
            "pb_ratio": 0.94000573,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 85.6484,
              "liquidity": 96.3668,
              "momentum": 56.63,
              "reversal": 60.48,
              "activity": 68.9849,
              "stability": 77.88,
              "size": 98.0969,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: value_quality"
            },
            "post_analysis_score_deltas": {
              "scorecard": 1.8
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "value_quality"
                ]
              }
            },
            "post_analysis_tags": [
              "value_quality"
            ],
            "dsa_context": {
              "enriched": true,
              "profile": "pre_rank_light",
              "news_included": false,
              "events_included": false,
              "quote": {
                "code": "601318",
                "name": "中国平安",
                "source": "tencent",
                "fetched_at": "2026-09-18T13:47:20.382660+00:00",
                "price": 53.37,
                "change_pct": 0.04,
                "change_amount": 0.02,
                "volume": 61166700,
                "amount": 3266258427.0,
                "volume_ratio": 1.21,
                "turnover_rate": 0.57,
                "amplitude": 1.44,
                "open_price": 53.32,
                "high": 53.8,
                "low": 53.03,
                "pre_close": 53.35,
                "pe_ratio": 6.07,
                "pb_ratio": 0.96,
                "total_mv": 966404999999.9999,
                "circ_mv": 568928000000.0
              },
              "fundamentals": {
                "market": "cn",
                "status": "partial",
                "coverage": {
                  "valuation": "not_supported",
                  "growth": "failed",
                  "earnings": "failed",
                  "institution": "failed",
                  "capital_flow": "failed",
                  "dragon_tiger": "failed",
                  "boards": "failed"
                },
                "valuation": {
                  "status": "not_supported",
                  "data": {
                    "pe_ratio": null,
                    "pb_ratio": null,
                    "total_mv": null,
                    "circ_mv": null
                  }
                },
                "growth": {
                  "status": "failed",
                  "data": {}
                },
                "earnings": {
                  "status": "failed",
                  "data": {}
                },
                "institution": {
                  "status": "failed",
                  "data": {}
                },
                "capital_flow": {
                  "status": "failed",
                  "data": {}
                },
                "boards": {
                  "status": "failed",
                  "data": {}
                },
                "errors": [
                  "fundamental_valuation timeout",
                  "fundamental stage timeout",
                  "fundamental stage timeout"
                ]
              },
              "news": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "events": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "warnings": []
            },
            "dsa_news": [],
            "dsa_analysis_summary": "DSA行情: 现价 53.37, 涨跌幅 0.04%",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "300014",
    "name": "亿纬锂能",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 4,
    "best_score": 74.556,
    "average_score": 74.556,
    "strategy_details": {
      "capital_heat": {
        "rank": 4,
        "score": 74.556,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 4,
          "code": "300014",
          "name": "亿纬锂能",
          "score": 74.556,
          "screen_score": 72.1559552631579,
          "reason": "本地后置评分: capital_confirmed",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 51.56,
          "change_pct": 6.9,
          "amount": 3669459749.34,
          "industry": "",
          "factor_scores": {
            "value": 80.8894,
            "liquidity": 95.2632,
            "momentum": 75.805,
            "reversal": 5.0,
            "activity": 77.5938,
            "stability": 57.3,
            "size": 97.8947,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 4,
            "code": "300014",
            "name": "亿纬锂能",
            "final_score": 74.556,
            "screen_score": 72.1559552631579,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 51.56,
            "change_pct": 6.9,
            "amount": 3669459749.34,
            "total_mv": 112055189969.0,
            "turnover_rate": 3.39,
            "volume_ratio": 2.66,
            "pe_ratio": 19.21924831,
            "pb_ratio": 2.23366259,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 80.8894,
              "liquidity": 95.2632,
              "momentum": 75.805,
              "reversal": 5.0,
              "activity": 77.5938,
              "stability": 57.3,
              "size": 97.8947,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: capital_confirmed"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.4
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "capital_confirmed"
                ]
              }
            },
            "post_analysis_tags": [
              "capital_confirmed"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "300223",
    "name": "君正股份",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 5,
    "best_score": 74.3684,
    "average_score": 74.3684,
    "strategy_details": {
      "capital_heat": {
        "rank": 5,
        "score": 74.3684,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 5,
          "code": "300223",
          "name": "君正股份",
          "score": 74.3684,
          "screen_score": 71.96843184210526,
          "reason": "本地后置评分: capital_confirmed",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 142.97,
          "change_pct": 5.86,
          "amount": 5109552060.08,
          "industry": "",
          "factor_scores": {
            "value": 48.5909,
            "liquidity": 96.8421,
            "momentum": 75.545,
            "reversal": 5.0,
            "activity": 75.2046,
            "stability": 60.42,
            "size": 92.6316,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 5,
            "code": "300223",
            "name": "君正股份",
            "final_score": 74.3684,
            "screen_score": 71.96843184210526,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 142.97,
            "change_pct": 5.86,
            "amount": 5109552060.08,
            "total_mv": 73622639831.0,
            "turnover_rate": 8.53,
            "volume_ratio": 2.07,
            "pe_ratio": 53.71275404,
            "pb_ratio": 5.4128834,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 48.5909,
              "liquidity": 96.8421,
              "momentum": 75.545,
              "reversal": 5.0,
              "activity": 75.2046,
              "stability": 60.42,
              "size": 92.6316,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: capital_confirmed"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.4
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "capital_confirmed"
                ]
              }
            },
            "post_analysis_tags": [
              "capital_confirmed"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "605111",
    "name": "新洁能",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 6,
    "best_score": 74.3449,
    "average_score": 74.3449,
    "strategy_details": {
      "capital_heat": {
        "rank": 6,
        "score": 74.3449,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 6,
          "code": "605111",
          "name": "新洁能",
          "score": 74.3449,
          "screen_score": 71.94488815789475,
          "reason": "本地后置评分: capital_confirmed",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 62.85,
          "change_pct": 6.11,
          "amount": 1697328532.0,
          "industry": "",
          "factor_scores": {
            "value": 43.5993,
            "liquidity": 83.1579,
            "momentum": 76.3575,
            "reversal": 5.0,
            "activity": 82.2794,
            "stability": 59.67,
            "size": 72.1053,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 6,
            "code": "605111",
            "name": "新洁能",
            "final_score": 74.3449,
            "screen_score": 71.94488815789475,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 62.85,
            "change_pct": 6.11,
            "amount": 1697328532.0,
            "total_mv": 26103651836.0,
            "turnover_rate": 6.59,
            "volume_ratio": 2.09,
            "pe_ratio": 66.6118121,
            "pb_ratio": 5.80050643,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 43.5993,
              "liquidity": 83.1579,
              "momentum": 76.3575,
              "reversal": 5.0,
              "activity": 82.2794,
              "stability": 59.67,
              "size": 72.1053,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: capital_confirmed"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.4
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "capital_confirmed"
                ]
              }
            },
            "post_analysis_tags": [
              "capital_confirmed"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "000811",
    "name": "冰轮环境",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 7,
    "best_score": 74.3023,
    "average_score": 74.3023,
    "strategy_details": {
      "capital_heat": {
        "rank": 7,
        "score": 74.3023,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 7,
          "code": "000811",
          "name": "冰轮环境",
          "score": 74.3023,
          "screen_score": 71.90228210526317,
          "reason": "本地后置评分: capital_confirmed",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 41.52,
          "change_pct": 7.4,
          "amount": 2713299049.86,
          "industry": "",
          "factor_scores": {
            "value": 40.7542,
            "liquidity": 92.1053,
            "momentum": 73.53,
            "reversal": 5.0,
            "activity": 81.628,
            "stability": 55.8,
            "size": 86.8421,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 7,
            "code": "000811",
            "name": "冰轮环境",
            "final_score": 74.3023,
            "screen_score": 71.90228210526317,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 41.52,
            "change_pct": 7.4,
            "amount": 2713299049.86,
            "total_mv": 41207685937.0,
            "turnover_rate": 6.96,
            "volume_ratio": 2.24,
            "pe_ratio": 67.59944821,
            "pb_ratio": 6.33417592,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 40.7542,
              "liquidity": 92.1053,
              "momentum": 73.53,
              "reversal": 5.0,
              "activity": 81.628,
              "stability": 55.8,
              "size": 86.8421,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: capital_confirmed"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.4
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "capital_confirmed"
                ]
              }
            },
            "post_analysis_tags": [
              "capital_confirmed"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "601328",
    "name": "交通银行",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 2,
    "best_score": 74.1674,
    "average_score": 74.1674,
    "strategy_details": {
      "momentum_quality": {
        "rank": 2,
        "score": 74.1674,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 2,
          "code": "601328",
          "name": "交通银行",
          "score": 74.1674,
          "screen_score": 71.16741282439445,
          "reason": "本地后置评分: value_quality、controlled_reversal",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 7.46,
          "change_pct": -1.58,
          "amount": 1635514714.0,
          "industry": "",
          "factor_scores": {
            "value": 87.7548,
            "liquidity": 89.4464,
            "momentum": 51.365,
            "reversal": 81.54,
            "activity": 70.1384,
            "stability": 73.26,
            "size": 97.4048,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 2,
            "code": "601328",
            "name": "交通银行",
            "final_score": 74.1674,
            "screen_score": 71.16741282439445,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 7.46,
            "change_pct": -1.58,
            "amount": 1635514714.0,
            "total_mv": 659193830304.0,
            "turnover_rate": 0.84,
            "volume_ratio": 1.25,
            "pe_ratio": 6.76234951,
            "pb_ratio": 0.5644556,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 87.7548,
              "liquidity": 89.4464,
              "momentum": 51.365,
              "reversal": 81.54,
              "activity": 70.1384,
              "stability": 73.26,
              "size": 97.4048,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: value_quality、controlled_reversal"
            },
            "post_analysis_score_deltas": {
              "scorecard": 3.0
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "value_quality",
                  "controlled_reversal"
                ]
              }
            },
            "post_analysis_tags": [
              "value_quality",
              "controlled_reversal"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "300623",
    "name": "捷捷微电",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 8,
    "best_score": 74.0455,
    "average_score": 74.0455,
    "strategy_details": {
      "capital_heat": {
        "rank": 8,
        "score": 74.0455,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 8,
          "code": "300623",
          "name": "捷捷微电",
          "score": 74.0455,
          "screen_score": 71.64547710526315,
          "reason": "本地后置评分: capital_confirmed",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 35.3,
          "change_pct": 7.26,
          "amount": 1592245350.68,
          "industry": "",
          "factor_scores": {
            "value": 52.6127,
            "liquidity": 82.1053,
            "momentum": 74.167,
            "reversal": 5.0,
            "activity": 85.5471,
            "stability": 56.22,
            "size": 75.7895,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 8,
            "code": "300623",
            "name": "捷捷微电",
            "final_score": 74.0455,
            "screen_score": 71.64547710526315,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 35.3,
            "change_pct": 7.26,
            "amount": 1592245350.68,
            "total_mv": 29372421141.0,
            "turnover_rate": 5.99,
            "volume_ratio": 2.35,
            "pe_ratio": 55.67489567,
            "pb_ratio": 4.73110171,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 52.6127,
              "liquidity": 82.1053,
              "momentum": 74.167,
              "reversal": 5.0,
              "activity": 85.5471,
              "stability": 56.22,
              "size": 75.7895,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: capital_confirmed"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.4
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "capital_confirmed"
                ]
              }
            },
            "post_analysis_tags": [
              "capital_confirmed"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "601288",
    "name": "农业银行",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 3,
    "best_score": 74.0438,
    "average_score": 74.0438,
    "strategy_details": {
      "momentum_quality": {
        "rank": 3,
        "score": 74.0438,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 3,
          "code": "601288",
          "name": "农业银行",
          "score": 74.0438,
          "screen_score": 71.04381810121107,
          "reason": "本地后置评分: value_quality、controlled_reversal",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 6.81,
          "change_pct": -1.16,
          "amount": 1956083841.0,
          "industry": "",
          "factor_scores": {
            "value": 85.4394,
            "liquidity": 91.6955,
            "momentum": 52.73,
            "reversal": 76.08,
            "activity": 66.5309,
            "stability": 74.52,
            "size": 99.654,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 3,
            "code": "601288",
            "name": "农业银行",
            "final_score": 74.0438,
            "screen_score": 71.04381810121107,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 6.81,
            "change_pct": -1.16,
            "amount": 1956083841.0,
            "total_mv": 2383384460675.0,
            "turnover_rate": 0.09,
            "volume_ratio": 1.05,
            "pe_ratio": 8.00029694,
            "pb_ratio": 0.8339303,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 85.4394,
              "liquidity": 91.6955,
              "momentum": 52.73,
              "reversal": 76.08,
              "activity": 66.5309,
              "stability": 74.52,
              "size": 99.654,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: value_quality、controlled_reversal"
            },
            "post_analysis_score_deltas": {
              "scorecard": 3.0
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "value_quality",
                  "controlled_reversal"
                ]
              }
            },
            "post_analysis_tags": [
              "value_quality",
              "controlled_reversal"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "688362",
    "name": "甬矽电子",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 9,
    "best_score": 74.0438,
    "average_score": 74.0438,
    "strategy_details": {
      "capital_heat": {
        "rank": 9,
        "score": 74.0438,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 9,
          "code": "688362",
          "name": "甬矽电子",
          "score": 74.0438,
          "screen_score": 71.64380131578949,
          "reason": "本地后置评分: capital_confirmed",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 64.79,
          "change_pct": 5.49,
          "amount": 2024000536.0,
          "industry": "",
          "factor_scores": {
            "value": 21.9497,
            "liquidity": 86.3158,
            "momentum": 74.3425,
            "reversal": 5.0,
            "activity": 81.0381,
            "stability": 61.53,
            "size": 75.2632,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 9,
            "code": "688362",
            "name": "甬矽电子",
            "final_score": 74.0438,
            "screen_score": 71.64380131578949,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 64.79,
            "change_pct": 5.49,
            "amount": 2024000536.0,
            "total_mv": 29364375833.0,
            "turnover_rate": 6.96,
            "volume_ratio": 2.11,
            "pe_ratio": 323.50209723,
            "pb_ratio": 7.66614203,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 21.9497,
              "liquidity": 86.3158,
              "momentum": 74.3425,
              "reversal": 5.0,
              "activity": 81.0381,
              "stability": 61.53,
              "size": 75.2632,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: capital_confirmed"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.4
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "capital_confirmed"
                ]
              }
            },
            "post_analysis_tags": [
              "capital_confirmed"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "601218",
    "name": "吉鑫科技",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 10,
    "best_score": 74.043,
    "average_score": 74.043,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 10,
        "score": 74.043,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 10,
          "code": "601218",
          "name": "吉鑫科技",
          "score": 74.043,
          "screen_score": 75.04298273809525,
          "reason": "本地后置评分: controlled_reversal",
          "risk_level": "low",
          "risk_flags": [
            "high_turnover"
          ],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 5.55,
          "change_pct": -3.31,
          "amount": 1330027102.0,
          "industry": "",
          "factor_scores": {
            "value": 58.0774,
            "liquidity": 90.4762,
            "momentum": 45.7425,
            "reversal": 97.53,
            "activity": 44.6481,
            "stability": 38.87,
            "size": 25.3968,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: controlled_reversal"
          },
          "post_analysis_tags": [
            "controlled_reversal"
          ],
          "raw": {
            "rank": 10,
            "code": "601218",
            "name": "吉鑫科技",
            "final_score": 74.043,
            "screen_score": 75.04298273809525,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 5.55,
            "change_pct": -3.31,
            "amount": 1330027102.0,
            "total_mv": 5378135992.0,
            "turnover_rate": 24.6,
            "volume_ratio": 1.65,
            "pe_ratio": 31.12729121,
            "pb_ratio": 1.76219478,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 58.0774,
              "liquidity": 90.4762,
              "momentum": 45.7425,
              "reversal": 97.53,
              "activity": 44.6481,
              "stability": 38.87,
              "size": 25.3968,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 25.0,
            "risk_level": "low",
            "risk_penalty": 3.0,
            "risk_flags": [
              "high_turnover"
            ],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: controlled_reversal"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.0
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "controlled_reversal"
                ]
              }
            },
            "post_analysis_tags": [
              "controlled_reversal"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "300475",
    "name": "香农芯创",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 10,
    "best_score": 73.7787,
    "average_score": 73.7787,
    "strategy_details": {
      "capital_heat": {
        "rank": 10,
        "score": 73.7787,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 10,
          "code": "300475",
          "name": "香农芯创",
          "score": 73.7787,
          "screen_score": 73.37874236842106,
          "reason": "本地后置评分: capital_confirmed",
          "risk_level": "low",
          "risk_flags": [
            "high_pb"
          ],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 174.32,
          "change_pct": 6.27,
          "amount": 5280184381.64,
          "industry": "",
          "factor_scores": {
            "value": 47.2548,
            "liquidity": 97.3684,
            "momentum": 76.8775,
            "reversal": 5.0,
            "activity": 78.8571,
            "stability": 59.19,
            "size": 94.2105,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "300475",
              "name": "香农芯创",
              "source": "tencent",
              "fetched_at": "2026-09-18T13:46:20.396940+00:00",
              "price": 174.32,
              "change_pct": 6.27,
              "change_amount": 10.29,
              "volume": 30780800,
              "amount": 5280184382.0,
              "volume_ratio": 1.55,
              "turnover_rate": 6.86,
              "amplitude": 5.59,
              "open_price": 168.69,
              "high": 174.97,
              "low": 165.8,
              "pre_close": 164.03,
              "pe_ratio": 20.32,
              "pb_ratio": 11.46,
              "total_mv": 81851000000.0,
              "circ_mv": 78182000000.0
            },
            "fundamentals": {
              "market": "cn",
              "status": "partial",
              "coverage": {
                "valuation": "not_supported",
                "growth": "failed",
                "earnings": "failed",
                "institution": "failed",
                "capital_flow": "failed",
                "dragon_tiger": "failed",
                "boards": "failed"
              },
              "valuation": {
                "status": "not_supported",
                "data": {
                  "pe_ratio": null,
                  "pb_ratio": null,
                  "total_mv": null,
                  "circ_mv": null
                }
              },
              "growth": {
                "status": "failed",
                "data": {}
              },
              "earnings": {
                "status": "failed",
                "data": {}
              },
              "institution": {
                "status": "failed",
                "data": {}
              },
              "capital_flow": {
                "status": "failed",
                "data": {}
              },
              "boards": {
                "status": "failed",
                "data": {}
              },
              "errors": [
                "fundamental_valuation timeout",
                "fundamental stage timeout",
                "fundamental stage timeout"
              ]
            },
            "news": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "events": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "warnings": []
          },
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "DSA行情: 现价 174.32, 涨跌幅 6.27%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 10,
            "code": "300475",
            "name": "香农芯创",
            "final_score": 73.7787,
            "screen_score": 73.37874236842106,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 174.32,
            "change_pct": 6.27,
            "amount": 5280184381.64,
            "total_mv": 81850520823.0,
            "turnover_rate": 6.86,
            "volume_ratio": 1.55,
            "pe_ratio": 20.31901855,
            "pb_ratio": 11.46498265,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 47.2548,
              "liquidity": 97.3684,
              "momentum": 76.8775,
              "reversal": 5.0,
              "activity": 78.8571,
              "stability": 59.19,
              "size": 94.2105,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 16.6667,
            "risk_level": "low",
            "risk_penalty": 2.0,
            "risk_flags": [
              "high_pb"
            ],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: capital_confirmed"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.4
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "capital_confirmed"
                ]
              }
            },
            "post_analysis_tags": [
              "capital_confirmed"
            ],
            "dsa_context": {
              "enriched": true,
              "profile": "pre_rank_light",
              "news_included": false,
              "events_included": false,
              "quote": {
                "code": "300475",
                "name": "香农芯创",
                "source": "tencent",
                "fetched_at": "2026-09-18T13:46:20.396940+00:00",
                "price": 174.32,
                "change_pct": 6.27,
                "change_amount": 10.29,
                "volume": 30780800,
                "amount": 5280184382.0,
                "volume_ratio": 1.55,
                "turnover_rate": 6.86,
                "amplitude": 5.59,
                "open_price": 168.69,
                "high": 174.97,
                "low": 165.8,
                "pre_close": 164.03,
                "pe_ratio": 20.32,
                "pb_ratio": 11.46,
                "total_mv": 81851000000.0,
                "circ_mv": 78182000000.0
              },
              "fundamentals": {
                "market": "cn",
                "status": "partial",
                "coverage": {
                  "valuation": "not_supported",
                  "growth": "failed",
                  "earnings": "failed",
                  "institution": "failed",
                  "capital_flow": "failed",
                  "dragon_tiger": "failed",
                  "boards": "failed"
                },
                "valuation": {
                  "status": "not_supported",
                  "data": {
                    "pe_ratio": null,
                    "pb_ratio": null,
                    "total_mv": null,
                    "circ_mv": null
                  }
                },
                "growth": {
                  "status": "failed",
                  "data": {}
                },
                "earnings": {
                  "status": "failed",
                  "data": {}
                },
                "institution": {
                  "status": "failed",
                  "data": {}
                },
                "capital_flow": {
                  "status": "failed",
                  "data": {}
                },
                "boards": {
                  "status": "failed",
                  "data": {}
                },
                "errors": [
                  "fundamental_valuation timeout",
                  "fundamental stage timeout",
                  "fundamental stage timeout"
                ]
              },
              "news": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "events": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "warnings": []
            },
            "dsa_news": [],
            "dsa_analysis_summary": "DSA行情: 现价 174.32, 涨跌幅 6.27%",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "600036",
    "name": "招商银行",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 4,
    "best_score": 73.6257,
    "average_score": 73.6257,
    "strategy_details": {
      "momentum_quality": {
        "rank": 4,
        "score": 73.6257,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 4,
          "code": "600036",
          "name": "招商银行",
          "score": 73.6257,
          "screen_score": 71.82574829152249,
          "reason": "本地后置评分: value_quality",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 40.59,
          "change_pct": -0.02,
          "amount": 1972732196.0,
          "industry": "",
          "factor_scores": {
            "value": 85.6367,
            "liquidity": 91.8685,
            "momentum": 56.435,
            "reversal": 61.26,
            "activity": 65.8004,
            "stability": 77.94,
            "size": 98.4429,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "600036",
              "name": "招商银行",
              "source": "tencent",
              "fetched_at": "2026-09-18T13:47:32.356337+00:00",
              "price": 40.59,
              "change_pct": -0.02,
              "change_amount": -0.01,
              "volume": 48520400,
              "amount": 1972732196.0,
              "volume_ratio": 0.77,
              "turnover_rate": 0.24,
              "amplitude": 1.21,
              "open_price": 40.53,
              "high": 40.92,
              "low": 40.43,
              "pre_close": 40.6,
              "pe_ratio": 6.75,
              "pb_ratio": 0.89,
              "total_mv": 1023674000000.0,
              "circ_mv": 837329000000.0001
            },
            "fundamentals": {
              "market": "cn",
              "status": "partial",
              "coverage": {
                "valuation": "not_supported",
                "growth": "failed",
                "earnings": "failed",
                "institution": "failed",
                "capital_flow": "failed",
                "dragon_tiger": "failed",
                "boards": "failed"
              },
              "valuation": {
                "status": "not_supported",
                "data": {
                  "pe_ratio": null,
                  "pb_ratio": null,
                  "total_mv": null,
                  "circ_mv": null
                }
              },
              "growth": {
                "status": "failed",
                "data": {}
              },
              "earnings": {
                "status": "failed",
                "data": {}
              },
              "institution": {
                "status": "failed",
                "data": {}
              },
              "capital_flow": {
                "status": "failed",
                "data": {}
              },
              "boards": {
                "status": "failed",
                "data": {}
              },
              "errors": [
                "fundamental_valuation timeout",
                "fundamental stage timeout",
                "fundamental stage timeout"
              ]
            },
            "news": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "events": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "warnings": []
          },
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "DSA行情: 现价 40.59, 涨跌幅 -0.02%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality"
          },
          "post_analysis_tags": [
            "value_quality"
          ],
          "raw": {
            "rank": 4,
            "code": "600036",
            "name": "招商银行",
            "final_score": 73.6257,
            "screen_score": 71.82574829152249,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 40.59,
            "change_pct": -0.02,
            "amount": 1972732196.0,
            "total_mv": 1023673532945.0,
            "turnover_rate": 0.24,
            "volume_ratio": 0.77,
            "pe_ratio": 6.74819068,
            "pb_ratio": 0.89400367,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 85.6367,
              "liquidity": 91.8685,
              "momentum": 56.435,
              "reversal": 61.26,
              "activity": 65.8004,
              "stability": 77.94,
              "size": 98.4429,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: value_quality"
            },
            "post_analysis_score_deltas": {
              "scorecard": 1.8
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "value_quality"
                ]
              }
            },
            "post_analysis_tags": [
              "value_quality"
            ],
            "dsa_context": {
              "enriched": true,
              "profile": "pre_rank_light",
              "news_included": false,
              "events_included": false,
              "quote": {
                "code": "600036",
                "name": "招商银行",
                "source": "tencent",
                "fetched_at": "2026-09-18T13:47:32.356337+00:00",
                "price": 40.59,
                "change_pct": -0.02,
                "change_amount": -0.01,
                "volume": 48520400,
                "amount": 1972732196.0,
                "volume_ratio": 0.77,
                "turnover_rate": 0.24,
                "amplitude": 1.21,
                "open_price": 40.53,
                "high": 40.92,
                "low": 40.43,
                "pre_close": 40.6,
                "pe_ratio": 6.75,
                "pb_ratio": 0.89,
                "total_mv": 1023674000000.0,
                "circ_mv": 837329000000.0001
              },
              "fundamentals": {
                "market": "cn",
                "status": "partial",
                "coverage": {
                  "valuation": "not_supported",
                  "growth": "failed",
                  "earnings": "failed",
                  "institution": "failed",
                  "capital_flow": "failed",
                  "dragon_tiger": "failed",
                  "boards": "failed"
                },
                "valuation": {
                  "status": "not_supported",
                  "data": {
                    "pe_ratio": null,
                    "pb_ratio": null,
                    "total_mv": null,
                    "circ_mv": null
                  }
                },
                "growth": {
                  "status": "failed",
                  "data": {}
                },
                "earnings": {
                  "status": "failed",
                  "data": {}
                },
                "institution": {
                  "status": "failed",
                  "data": {}
                },
                "capital_flow": {
                  "status": "failed",
                  "data": {}
                },
                "boards": {
                  "status": "failed",
                  "data": {}
                },
                "errors": [
                  "fundamental_valuation timeout",
                  "fundamental stage timeout",
                  "fundamental stage timeout"
                ]
              },
              "news": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "events": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "warnings": []
            },
            "dsa_news": [],
            "dsa_analysis_summary": "DSA行情: 现价 40.59, 涨跌幅 -0.02%",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "603867",
    "name": "新化股份",
    "resonance_count": 1,
    "strategies": [
      "volume_breakout"
    ],
    "strategy_labels": [
      "放量突破"
    ],
    "best_rank": 3,
    "best_score": 73.5152,
    "average_score": 73.5152,
    "strategy_details": {
      "volume_breakout": {
        "rank": 3,
        "score": 73.5152,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 3,
          "code": "603867",
          "name": "新化股份",
          "score": 73.5152,
          "screen_score": 71.31515849446154,
          "reason": "本地后置评分: capital_confirmed",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 32.5,
          "change_pct": 7.12,
          "amount": 375502696.0,
          "industry": "",
          "factor_scores": {
            "value": 82.9412,
            "liquidity": 61.5385,
            "momentum": 76.4166,
            "reversal": 5.0,
            "activity": 83.4498,
            "stability": 59.5747,
            "size": 53.8462,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "603867",
              "name": "XD新化股",
              "source": "tencent",
              "fetched_at": "2026-09-18T13:45:08.534865+00:00",
              "price": 32.5,
              "change_pct": 7.12,
              "change_amount": 2.16,
              "volume": 11693900,
              "amount": 375502696.0,
              "volume_ratio": 2.54,
              "turnover_rate": 5.42,
              "amplitude": 8.37,
              "open_price": 30.54,
              "high": 32.98,
              "low": 30.44,
              "pre_close": 30.34,
              "pe_ratio": 25.75,
              "pb_ratio": 2.29,
              "total_mv": 7068000000.000001,
              "circ_mv": 7009999999.999999
            },
            "fundamentals": {
              "market": "cn",
              "status": "partial",
              "coverage": {
                "valuation": "not_supported",
                "growth": "failed",
                "earnings": "failed",
                "institution": "failed",
                "capital_flow": "failed",
                "dragon_tiger": "failed",
                "boards": "failed"
              },
              "valuation": {
                "status": "not_supported",
                "data": {
                  "pe_ratio": null,
                  "pb_ratio": null,
                  "total_mv": null,
                  "circ_mv": null
                }
              },
              "growth": {
                "status": "failed",
                "data": {}
              },
              "earnings": {
                "status": "failed",
                "data": {}
              },
              "institution": {
                "status": "failed",
                "data": {}
              },
              "capital_flow": {
                "status": "failed",
                "data": {}
              },
              "boards": {
                "status": "failed",
                "data": {}
              },
              "errors": [
                "fundamental_valuation timeout",
                "fundamental stage timeout",
                "fundamental stage timeout"
              ]
            },
            "news": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "events": {
              "success": false,
              "skipped": true,
              "reason": "pre_rank_light_context",
              "results": []
            },
            "warnings": []
          },
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "DSA行情: 现价 32.5, 涨跌幅 7.12%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 3,
            "code": "603867",
            "name": "新化股份",
            "final_score": 73.5152,
            "screen_score": 71.31515849446154,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 32.5,
            "change_pct": 7.12,
            "amount": 375502696.0,
            "total_mv": 7068319148.0,
            "turnover_rate": 5.42,
            "volume_ratio": 2.54,
            "pe_ratio": 25.75003919,
            "pb_ratio": 2.25744968,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": -15.3646,
            "signal_score": 86.0,
            "ma_bullish": true,
            "price_above_ma20": true,
            "macd_status": "bullish",
            "rsi_status": "neutral",
            "breakout_20d_pct": 4.8725,
            "range_20d_pct": 17.6177,
            "volume_ratio_20d": 1.7503,
            "body_pct": 6.4178,
            "pullback_to_ma20_pct": 9.3172,
            "consolidation_days_20d": 20,
            "volatility_20d_pct": 48.0785,
            "max_drawdown_20d_pct": -5.4348,
            "atr_20_pct": 4.0769,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:AkshareFetcher",
            "factor_scores": {
              "value": 82.9412,
              "liquidity": 61.5385,
              "momentum": 76.4166,
              "reversal": 5.0,
              "activity": 83.4498,
              "stability": 59.5747,
              "size": 53.8462,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: capital_confirmed"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.2
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "capital_confirmed"
                ]
              }
            },
            "post_analysis_tags": [
              "capital_confirmed"
            ],
            "dsa_context": {
              "enriched": true,
              "profile": "pre_rank_light",
              "news_included": false,
              "events_included": false,
              "quote": {
                "code": "603867",
                "name": "XD新化股",
                "source": "tencent",
                "fetched_at": "2026-09-18T13:45:08.534865+00:00",
                "price": 32.5,
                "change_pct": 7.12,
                "change_amount": 2.16,
                "volume": 11693900,
                "amount": 375502696.0,
                "volume_ratio": 2.54,
                "turnover_rate": 5.42,
                "amplitude": 8.37,
                "open_price": 30.54,
                "high": 32.98,
                "low": 30.44,
                "pre_close": 30.34,
                "pe_ratio": 25.75,
                "pb_ratio": 2.29,
                "total_mv": 7068000000.000001,
                "circ_mv": 7009999999.999999
              },
              "fundamentals": {
                "market": "cn",
                "status": "partial",
                "coverage": {
                  "valuation": "not_supported",
                  "growth": "failed",
                  "earnings": "failed",
                  "institution": "failed",
                  "capital_flow": "failed",
                  "dragon_tiger": "failed",
                  "boards": "failed"
                },
                "valuation": {
                  "status": "not_supported",
                  "data": {
                    "pe_ratio": null,
                    "pb_ratio": null,
                    "total_mv": null,
                    "circ_mv": null
                  }
                },
                "growth": {
                  "status": "failed",
                  "data": {}
                },
                "earnings": {
                  "status": "failed",
                  "data": {}
                },
                "institution": {
                  "status": "failed",
                  "data": {}
                },
                "capital_flow": {
                  "status": "failed",
                  "data": {}
                },
                "boards": {
                  "status": "failed",
                  "data": {}
                },
                "errors": [
                  "fundamental_valuation timeout",
                  "fundamental stage timeout",
                  "fundamental stage timeout"
                ]
              },
              "news": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "events": {
                "success": false,
                "skipped": true,
                "reason": "pre_rank_light_context",
                "results": []
              },
              "warnings": []
            },
            "dsa_news": [],
            "dsa_analysis_summary": "DSA行情: 现价 32.5, 涨跌幅 7.12%",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "601398",
    "name": "工商银行",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 5,
    "best_score": 73.2146,
    "average_score": 73.2146,
    "strategy_details": {
      "momentum_quality": {
        "rank": 5,
        "score": 73.2146,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 5,
          "code": "601398",
          "name": "工商银行",
          "score": 73.2146,
          "screen_score": 71.41457480536332,
          "reason": "本地后置评分: value_quality",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 8.07,
          "change_pct": -0.86,
          "amount": 1996827590.0,
          "industry": "",
          "factor_scores": {
            "value": 86.4035,
            "liquidity": 92.0415,
            "momentum": 53.705,
            "reversal": 72.18,
            "activity": 66.0771,
            "stability": 75.42,
            "size": 100.0,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality"
          },
          "post_analysis_tags": [
            "value_quality"
          ],
          "raw": {
            "rank": 5,
            "code": "601398",
            "name": "工商银行",
            "final_score": 73.2146,
            "screen_score": 71.41457480536332,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 8.07,
            "change_pct": -0.86,
            "amount": 1996827590.0,
            "total_mv": 2876198494708.0,
            "turnover_rate": 0.09,
            "volume_ratio": 0.95,
            "pe_ratio": 7.68747209,
            "pb_ratio": 0.72588602,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 86.4035,
              "liquidity": 92.0415,
              "momentum": 53.705,
              "reversal": 72.18,
              "activity": 66.0771,
              "stability": 75.42,
              "size": 100.0,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: value_quality"
            },
            "post_analysis_score_deltas": {
              "scorecard": 1.8
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "value_quality"
                ]
              }
            },
            "post_analysis_tags": [
              "value_quality"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "600030",
    "name": "中信证券",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 6,
    "best_score": 73.1051,
    "average_score": 73.1051,
    "strategy_details": {
      "momentum_quality": {
        "rank": 6,
        "score": 73.1051,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 6,
          "code": "600030",
          "name": "中信证券",
          "score": 73.1051,
          "screen_score": 71.30513308823528,
          "reason": "本地后置评分: value_quality",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 26.54,
          "change_pct": 1.45,
          "amount": 2245282483.0,
          "industry": "",
          "factor_scores": {
            "value": 77.9325,
            "liquidity": 94.1176,
            "momentum": 61.2125,
            "reversal": 38.55,
            "activity": 68.2278,
            "stability": 73.65,
            "size": 96.0208,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality"
          },
          "post_analysis_tags": [
            "value_quality"
          ],
          "raw": {
            "rank": 6,
            "code": "600030",
            "name": "中信证券",
            "final_score": 73.1051,
            "screen_score": 71.30513308823528,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 26.54,
            "change_pct": 1.45,
            "amount": 2245282483.0,
            "total_mv": 414668184506.0,
            "turnover_rate": 0.7,
            "volume_ratio": 0.94,
            "pe_ratio": 10.45669535,
            "pb_ratio": 1.40339844,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": null,
            "signal_score": null,
            "ma_bullish": null,
            "price_above_ma20": null,
            "macd_status": "",
            "rsi_status": "",
            "breakout_20d_pct": null,
            "range_20d_pct": null,
            "volume_ratio_20d": null,
            "body_pct": null,
            "pullback_to_ma20_pct": null,
            "consolidation_days_20d": null,
            "volatility_20d_pct": null,
            "max_drawdown_20d_pct": null,
            "atr_20_pct": null,
            "daily_quality_score": null,
            "daily_quality_flags": "",
            "daily_source": "",
            "factor_scores": {
              "value": 77.9325,
              "liquidity": 94.1176,
              "momentum": 61.2125,
              "reversal": 38.55,
              "activity": 68.2278,
              "stability": 73.65,
              "size": 96.0208,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: value_quality"
            },
            "post_analysis_score_deltas": {
              "scorecard": 1.8
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "value_quality"
                ]
              }
            },
            "post_analysis_tags": [
              "value_quality"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  },
  {
    "code": "002612",
    "name": "朗姿股份",
    "resonance_count": 1,
    "strategies": [
      "volume_breakout"
    ],
    "strategy_labels": [
      "放量突破"
    ],
    "best_rank": 4,
    "best_score": 72.5724,
    "average_score": 72.5724,
    "strategy_details": {
      "volume_breakout": {
        "rank": 4,
        "score": 72.5724,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 4,
          "code": "002612",
          "name": "朗姿股份",
          "score": 72.5724,
          "screen_score": 70.37239480984616,
          "reason": "本地后置评分: capital_confirmed",
          "risk_level": "low",
          "risk_flags": [],
          "llm_score": null,
          "llm_confidence": null,
          "llm_sector": "",
          "llm_theme": "",
          "llm_tags": [],
          "llm_thesis": "",
          "llm_catalysts": [],
          "llm_risks": [],
          "llm_watch_items": [],
          "llm_invalidators": [],
          "llm_style_fit": "",
          "price": 17.1,
          "change_pct": 6.48,
          "amount": 243482205.77,
          "industry": "",
          "factor_scores": {
            "value": 83.4519,
            "liquidity": 46.1538,
            "momentum": 81.6886,
            "reversal": 5.0,
            "activity": 85.4793,
            "stability": 61.44,
            "size": 61.5385,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 4,
            "code": "002612",
            "name": "朗姿股份",
            "final_score": 72.5724,
            "screen_score": 70.37239480984616,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 17.1,
            "change_pct": 6.48,
            "amount": 243482205.77,
            "total_mv": 7565815913.0,
            "turnover_rate": 5.53,
            "volume_ratio": 2.9,
            "pe_ratio": 9.0851846,
            "pb_ratio": 2.69383027,
            "industry": "",
            "concepts": "",
            "industry_rank": null,
            "industry_change_pct": null,
            "industry_heat_score": null,
            "concept_heat_score": null,
            "board_heat_score": null,
            "board_heat_latest_score": null,
            "board_heat_trend_score": null,
            "board_heat_persistence_score": null,
            "board_heat_cooling_score": null,
            "board_heat_observations": null,
            "board_heat_state": "",
            "board_heat_summary": "",
            "change_60d": 51.1936,
            "signal_score": 74.0,
            "ma_bullish": true,
            "price_above_ma20": true,
            "macd_status": "neutral",
            "rsi_status": "neutral",
            "breakout_20d_pct": -0.1168,
            "range_20d_pct": 20.9286,
            "volume_ratio_20d": 1.876,
            "body_pct": 6.675,
            "pullback_to_ma20_pct": 8.0774,
            "consolidation_days_20d": 10,
            "volatility_20d_pct": 43.2306,
            "max_drawdown_20d_pct": -8.4524,
            "atr_20_pct": 3.9123,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:AkshareFetcher",
            "factor_scores": {
              "value": 83.4519,
              "liquidity": 46.1538,
              "momentum": 81.6886,
              "reversal": 5.0,
              "activity": 85.4793,
              "stability": 61.44,
              "size": 61.5385,
              "theme_heat": 50.0,
              "topic_alignment": 50.0
            },
            "llm_confidence": null,
            "llm_sector": "",
            "llm_theme": "",
            "llm_tags": [],
            "llm_catalysts": [],
            "llm_risks": [],
            "llm_thesis": "",
            "llm_style_fit": "",
            "llm_watch_items": [],
            "llm_invalidators": [],
            "risk_score": 0.0,
            "risk_level": "low",
            "risk_penalty": 0.0,
            "risk_flags": [],
            "excluded_by_risk": false,
            "portfolio_penalty": 0.0,
            "portfolio_flags": [],
            "post_analysis_status": {
              "scorecard": "completed"
            },
            "post_analysis_summaries": {
              "scorecard": "本地后置评分: capital_confirmed"
            },
            "post_analysis_score_deltas": {
              "scorecard": 2.2
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": [
                  "capital_confirmed"
                ]
              }
            },
            "post_analysis_tags": [
              "capital_confirmed"
            ],
            "dsa_context": {},
            "dsa_news": [],
            "dsa_analysis_summary": "",
            "deep_analysis_status": "not_requested",
            "deep_analysis_query_id": "",
            "deep_analysis_summary": "",
            "deep_analysis_error": "",
            "deep_analysis_result": null,
            "deep_analysis_signal_score": null,
            "deep_analysis_sentiment_score": null,
            "deep_analysis_operation_advice": "",
            "deep_analysis_trend_prediction": "",
            "deep_analysis_risk_flags": []
          }
        }
      }
    }
  }
]
```
