# 《A股短线候选池（改造第1阶段）》

> 本报告只做四套原版模型自动合并、去重和模型共振统计；尚未加入题材、涨停梯队、市场情绪、竞价和开盘确认。

## 测试概况

- 阶段：`short_term_candidate_pool_v1`
- 市场：`cn`
- 每套模型返回数量：`10`
- 合并去重后的候选数量：`33`
- 报告输出数量：`30`

## 模型运行状态

| 模型 | 标签 | 状态 | 候选数量 |
| --- | --- | --- | ---: |
| `volume_breakout` | 放量突破 | success | 3 |
| `capital_heat` | 资金热度 | success | 10 |
| `momentum_quality` | 动量质量 | success | 10 |
| `oversold_reversal` | 超跌反转 | success | 10 |

## 候选池优先级

排序依次为：共振模型数量（降序）、多个模型平均原始评分（降序）、最佳模型排名（升序）。这里的排序仅表示候选池优先级，不是买入评分。

| 排名 | 股票代码 | 股票名称 | 共振数 | 入选模型 | 平均原始分 | 最佳名次 |
| ---: | --- | --- | ---: | --- | ---: | ---: |
| 1 | 600426 | 华鲁恒升 | 1 | 超跌反转 | 89.4851 | 1 |
| 2 | 000963 | 华东医药 | 1 | 超跌反转 | 88.7174 | 2 |
| 3 | 600216 | 浙江医药 | 1 | 超跌反转 | 87.6764 | 3 |
| 4 | 600196 | 复星医药 | 1 | 超跌反转 | 86.9588 | 4 |
| 5 | 000960 | 锡业股份 | 1 | 超跌反转 | 86.509 | 5 |
| 6 | 600711 | 盛屯矿业 | 1 | 超跌反转 | 86.2832 | 6 |
| 7 | 000725 | 京东方A | 1 | 超跌反转 | 85.7622 | 7 |
| 8 | 600522 | 中天科技 | 1 | 超跌反转 | 85.4723 | 8 |
| 9 | 300009 | 安科生物 | 1 | 超跌反转 | 84.4456 | 9 |
| 10 | 600141 | 兴发集团 | 1 | 超跌反转 | 84.3998 | 10 |
| 11 | 601318 | 中国平安 | 1 | 动量质量 | 75.3746 | 1 |
| 12 | 600036 | 招商银行 | 1 | 动量质量 | 74.6066 | 2 |
| 13 | 601166 | 兴业银行 | 1 | 动量质量 | 74.0852 | 3 |
| 14 | 601398 | 工商银行 | 1 | 动量质量 | 74.0199 | 4 |
| 15 | 601919 | 中远海控 | 1 | 动量质量 | 73.6454 | 5 |
| 16 | 601601 | 中国太保 | 1 | 动量质量 | 73.6165 | 6 |
| 17 | 601288 | 农业银行 | 1 | 动量质量 | 73.3378 | 7 |
| 18 | 600030 | 中信证券 | 1 | 动量质量 | 72.9623 | 8 |
| 19 | 000426 | 兴业银锡 | 1 | 资金热度 | 72.7624 | 1 |
| 20 | 300390 | 天华新能 | 1 | 资金热度 | 72.5149 | 2 |
| 21 | 601020 | 华钰矿业 | 1 | 资金热度 | 72.4308 | 3 |
| 22 | 000651 | 格力电器 | 1 | 动量质量 | 72.2234 | 9 |
| 23 | 000001 | 平安银行 | 1 | 动量质量 | 72.1011 | 10 |
| 24 | 001337 | 四川黄金 | 1 | 资金热度 | 71.7641 | 4 |
| 25 | 002469 | 三维化学 | 1 | 放量突破 | 71.7398 | 1 |
| 26 | 601958 | 金钼股份 | 1 | 资金热度 | 71.1467 | 5 |
| 27 | 601069 | 西部黄金 | 1 | 资金热度 | 70.8788 | 6 |
| 28 | 002466 | 天齐锂业 | 1 | 资金热度 | 70.4829 | 7 |
| 29 | 002460 | 赣锋锂业 | 1 | 资金热度 | 70.1991 | 8 |
| 30 | 688596 | 正帆科技 | 1 | 资金热度 | 69.9349 | 9 |

## 模型明细与原始候选字段

完整的每套模型返回结果、每只股票的原始候选字段和策略明细请以同目录的 `candidate_pool.json` 为准。

```json
[
  {
    "code": "600426",
    "name": "华鲁恒升",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 1,
    "best_score": 89.4851,
    "average_score": 89.4851,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 1,
        "score": 89.4851,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 1,
          "code": "600426",
          "name": "华鲁恒升",
          "score": 89.4851,
          "screen_score": 85.08510522151899,
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
          "price": 20.12,
          "change_pct": -3.13,
          "amount": 670623937.0,
          "industry": "",
          "factor_scores": {
            "value": 80.6487,
            "liquidity": 86.4979,
            "momentum": 46.3275,
            "reversal": 95.19,
            "activity": 80.2281,
            "stability": 68.61,
            "size": 92.4051,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "600426",
              "name": "华鲁恒升",
              "source": "tencent",
              "fetched_at": "2026-08-24T03:57:46.044455+00:00",
              "price": 20.12,
              "change_pct": -3.13,
              "change_amount": -0.65,
              "volume": 33248900,
              "amount": 670623937.0,
              "volume_ratio": 1.81,
              "turnover_rate": 1.21,
              "amplitude": 5.15,
              "open_price": 20.71,
              "high": 20.9,
              "low": 19.83,
              "pre_close": 20.77,
              "pe_ratio": 13.5,
              "pb_ratio": 1.58,
              "total_mv": 55329000000.0,
              "circ_mv": 55322000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 20.12, 涨跌幅 -3.13%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 1,
            "code": "600426",
            "name": "华鲁恒升",
            "final_score": 89.4851,
            "screen_score": 85.08510522151899,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 20.12,
            "change_pct": -3.13,
            "amount": 670623937.0,
            "total_mv": 55328853462.0,
            "turnover_rate": 1.21,
            "volume_ratio": 1.81,
            "pe_ratio": 13.9321835,
            "pb_ratio": 1.63503861,
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
              "value": 80.6487,
              "liquidity": 86.4979,
              "momentum": 46.3275,
              "reversal": 95.19,
              "activity": 80.2281,
              "stability": 68.61,
              "size": 92.4051,
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
                "code": "600426",
                "name": "华鲁恒升",
                "source": "tencent",
                "fetched_at": "2026-08-24T03:57:46.044455+00:00",
                "price": 20.12,
                "change_pct": -3.13,
                "change_amount": -0.65,
                "volume": 33248900,
                "amount": 670623937.0,
                "volume_ratio": 1.81,
                "turnover_rate": 1.21,
                "amplitude": 5.15,
                "open_price": 20.71,
                "high": 20.9,
                "low": 19.83,
                "pre_close": 20.77,
                "pe_ratio": 13.5,
                "pb_ratio": 1.58,
                "total_mv": 55329000000.0,
                "circ_mv": 55322000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 20.12, 涨跌幅 -3.13%",
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
    "code": "000963",
    "name": "华东医药",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 2,
    "best_score": 88.7174,
    "average_score": 88.7174,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 2,
        "score": 88.7174,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 2,
          "code": "000963",
          "name": "华东医药",
          "score": 88.7174,
          "screen_score": 84.31744457805908,
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
          "price": 27.19,
          "change_pct": -3.24,
          "amount": 522398002.87,
          "industry": "",
          "factor_scores": {
            "value": 77.3455,
            "liquidity": 83.1224,
            "momentum": 45.97,
            "reversal": 96.62,
            "activity": 77.9358,
            "stability": 68.28,
            "size": 91.3502,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "000963",
              "name": "华东医药",
              "source": "tencent",
              "fetched_at": "2026-08-24T03:58:07.339237+00:00",
              "price": 27.19,
              "change_pct": -3.24,
              "change_amount": -0.91,
              "volume": 19025700,
              "amount": 522398003.0,
              "volume_ratio": 0.98,
              "turnover_rate": 1.09,
              "amplitude": 2.67,
              "open_price": 27.8,
              "high": 27.9,
              "low": 27.15,
              "pre_close": 28.1,
              "pe_ratio": 13.62,
              "pb_ratio": 1.93,
              "total_mv": 47684000000.0,
              "circ_mv": 47664000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 27.19, 涨跌幅 -3.24%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 2,
            "code": "000963",
            "name": "华东医药",
            "final_score": 88.7174,
            "screen_score": 84.31744457805908,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 27.19,
            "change_pct": -3.24,
            "amount": 522398002.87,
            "total_mv": 47684104897.0,
            "turnover_rate": 1.09,
            "volume_ratio": 0.98,
            "pe_ratio": 14.07269903,
            "pb_ratio": 1.91504541,
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
              "value": 77.3455,
              "liquidity": 83.1224,
              "momentum": 45.97,
              "reversal": 96.62,
              "activity": 77.9358,
              "stability": 68.28,
              "size": 91.3502,
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
                "code": "000963",
                "name": "华东医药",
                "source": "tencent",
                "fetched_at": "2026-08-24T03:58:07.339237+00:00",
                "price": 27.19,
                "change_pct": -3.24,
                "change_amount": -0.91,
                "volume": 19025700,
                "amount": 522398003.0,
                "volume_ratio": 0.98,
                "turnover_rate": 1.09,
                "amplitude": 2.67,
                "open_price": 27.8,
                "high": 27.9,
                "low": 27.15,
                "pre_close": 28.1,
                "pe_ratio": 13.62,
                "pb_ratio": 1.93,
                "total_mv": 47684000000.0,
                "circ_mv": 47664000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 27.19, 涨跌幅 -3.24%",
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
    "code": "600216",
    "name": "浙江医药",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 3,
    "best_score": 87.6764,
    "average_score": 87.6764,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 3,
        "score": 87.6764,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 3,
          "code": "600216",
          "name": "浙江医药",
          "score": 87.6764,
          "screen_score": 83.2764354535865,
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
          "price": 12.74,
          "change_pct": -3.7,
          "amount": 335276403.0,
          "industry": "",
          "factor_scores": {
            "value": 84.1577,
            "liquidity": 69.4093,
            "momentum": 44.475,
            "reversal": 97.4,
            "activity": 82.9589,
            "stability": 66.9,
            "size": 58.8608,
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
            "code": "600216",
            "name": "浙江医药",
            "final_score": 87.6764,
            "screen_score": 83.2764354535865,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 12.74,
            "change_pct": -3.7,
            "amount": 335276403.0,
            "total_mv": 12251264935.0,
            "turnover_rate": 2.75,
            "volume_ratio": 0.77,
            "pe_ratio": 16.9337723,
            "pb_ratio": 1.13182895,
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
              "value": 84.1577,
              "liquidity": 69.4093,
              "momentum": 44.475,
              "reversal": 97.4,
              "activity": 82.9589,
              "stability": 66.9,
              "size": 58.8608,
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
    "code": "600196",
    "name": "复星医药",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 4,
    "best_score": 86.9588,
    "average_score": 86.9588,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 4,
        "score": 86.9588,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 4,
          "code": "600196",
          "name": "复星医药",
          "score": 86.9588,
          "screen_score": 82.55881815400842,
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
          "price": 22.93,
          "change_pct": -2.67,
          "amount": 546012820.0,
          "industry": "",
          "factor_scores": {
            "value": 81.7141,
            "liquidity": 83.9662,
            "momentum": 47.8225,
            "reversal": 89.21,
            "activity": 78.1439,
            "stability": 69.99,
            "size": 94.0928,
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
            "rank": 4,
            "code": "600196",
            "name": "复星医药",
            "final_score": 86.9588,
            "screen_score": 82.55881815400842,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 22.93,
            "change_pct": -2.67,
            "amount": 546012820.0,
            "total_mv": 61232944422.0,
            "turnover_rate": 1.11,
            "volume_ratio": 1.01,
            "pe_ratio": 18.09664125,
            "pb_ratio": 1.28015223,
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
              "value": 81.7141,
              "liquidity": 83.9662,
              "momentum": 47.8225,
              "reversal": 89.21,
              "activity": 78.1439,
              "stability": 69.99,
              "size": 94.0928,
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
    "code": "000960",
    "name": "锡业股份",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 5,
    "best_score": 86.509,
    "average_score": 86.509,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 5,
        "score": 86.509,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 5,
          "code": "000960",
          "name": "锡业股份",
          "score": 86.509,
          "screen_score": 84.50901864978903,
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
          "price": 35.77,
          "change_pct": -3.58,
          "amount": 1350624335.15,
          "industry": "",
          "factor_scores": {
            "value": 59.7036,
            "liquidity": 93.4599,
            "momentum": 44.865,
            "reversal": 98.96,
            "activity": 84.961,
            "stability": 67.26,
            "size": 93.8819,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "000960",
              "name": "锡业股份",
              "source": "tencent",
              "fetched_at": "2026-08-24T03:57:56.550621+00:00",
              "price": 35.77,
              "change_pct": -3.58,
              "change_amount": -1.33,
              "volume": 37261600,
              "amount": 1350624335.0,
              "volume_ratio": 1.6,
              "turnover_rate": 2.26,
              "amplitude": 5.04,
              "open_price": 37.39,
              "high": 37.5,
              "low": 35.63,
              "pre_close": 37.1,
              "pe_ratio": 24.44,
              "pb_ratio": 2.74,
              "total_mv": 58857000000.00001,
              "circ_mv": 58857000000.00001
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
          "dsa_analysis_summary": "DSA行情: 现价 35.77, 涨跌幅 -3.58%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: controlled_reversal"
          },
          "post_analysis_tags": [
            "controlled_reversal"
          ],
          "raw": {
            "rank": 5,
            "code": "000960",
            "name": "锡业股份",
            "final_score": 86.509,
            "screen_score": 84.50901864978903,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 35.77,
            "change_pct": -3.58,
            "amount": 1350624335.15,
            "total_mv": 58857100923.0,
            "turnover_rate": 2.26,
            "volume_ratio": 1.6,
            "pe_ratio": 25.35176073,
            "pb_ratio": 2.84361058,
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
              "value": 59.7036,
              "liquidity": 93.4599,
              "momentum": 44.865,
              "reversal": 98.96,
              "activity": 84.961,
              "stability": 67.26,
              "size": 93.8819,
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
                "code": "000960",
                "name": "锡业股份",
                "source": "tencent",
                "fetched_at": "2026-08-24T03:57:56.550621+00:00",
                "price": 35.77,
                "change_pct": -3.58,
                "change_amount": -1.33,
                "volume": 37261600,
                "amount": 1350624335.0,
                "volume_ratio": 1.6,
                "turnover_rate": 2.26,
                "amplitude": 5.04,
                "open_price": 37.39,
                "high": 37.5,
                "low": 35.63,
                "pre_close": 37.1,
                "pe_ratio": 24.44,
                "pb_ratio": 2.74,
                "total_mv": 58857000000.00001,
                "circ_mv": 58857000000.00001
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
            "dsa_analysis_summary": "DSA行情: 现价 35.77, 涨跌幅 -3.58%",
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
    "code": "600711",
    "name": "盛屯矿业",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 6,
    "best_score": 86.2832,
    "average_score": 86.2832,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 6,
        "score": 86.2832,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 6,
          "code": "600711",
          "name": "盛屯矿业",
          "score": 86.2832,
          "screen_score": 81.88318643459917,
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
          "price": 11.82,
          "change_pct": -2.31,
          "amount": 1139478541.0,
          "industry": "",
          "factor_scores": {
            "value": 75.539,
            "liquidity": 92.1941,
            "momentum": 48.9925,
            "reversal": 84.53,
            "activity": 86.2668,
            "stability": 71.07,
            "size": 88.6076,
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
            "code": "600711",
            "name": "盛屯矿业",
            "final_score": 86.2832,
            "screen_score": 81.88318643459917,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 11.82,
            "change_pct": -2.31,
            "amount": 1139478541.0,
            "total_mv": 36531028533.0,
            "turnover_rate": 3.1,
            "volume_ratio": 1.82,
            "pe_ratio": 13.78529678,
            "pb_ratio": 2.09197093,
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
              "value": 75.539,
              "liquidity": 92.1941,
              "momentum": 48.9925,
              "reversal": 84.53,
              "activity": 86.2668,
              "stability": 71.07,
              "size": 88.6076,
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
    "code": "000725",
    "name": "京东方A",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 7,
    "best_score": 85.7622,
    "average_score": 85.7622,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 7,
        "score": 85.7622,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 7,
          "code": "000725",
          "name": "京东方A",
          "score": 85.7622,
          "screen_score": 83.76221133966244,
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
          "price": 5.76,
          "change_pct": -4.0,
          "amount": 5532965477.62,
          "industry": "",
          "factor_scores": {
            "value": 64.528,
            "liquidity": 99.1561,
            "momentum": 43.5,
            "reversal": 93.5,
            "activity": 83.1606,
            "stability": 66.0,
            "size": 99.5781,
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
            "code": "000725",
            "name": "京东方A",
            "final_score": 85.7622,
            "screen_score": 83.76221133966244,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 5.76,
            "change_pct": -4.0,
            "amount": 5532965477.62,
            "total_mv": 213375329649.0,
            "turnover_rate": 2.68,
            "volume_ratio": 0.87,
            "pe_ratio": 37.35444812,
            "pb_ratio": 1.63314457,
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
              "value": 64.528,
              "liquidity": 99.1561,
              "momentum": 43.5,
              "reversal": 93.5,
              "activity": 83.1606,
              "stability": 66.0,
              "size": 99.5781,
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
    "code": "600522",
    "name": "中天科技",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 8,
    "best_score": 85.4723,
    "average_score": 85.4723,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 8,
        "score": 85.4723,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 8,
          "code": "600522",
          "name": "中天科技",
          "score": 85.4723,
          "screen_score": 83.47234870253165,
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
          "price": 32.22,
          "change_pct": -3.62,
          "amount": 3135486746.0,
          "industry": "",
          "factor_scores": {
            "value": 50.1092,
            "liquidity": 98.1013,
            "momentum": 44.735,
            "reversal": 98.44,
            "activity": 83.2109,
            "stability": 67.14,
            "size": 97.2574,
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
            "code": "600522",
            "name": "中天科技",
            "final_score": 85.4723,
            "screen_score": 83.47234870253165,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 32.22,
            "change_pct": -3.62,
            "amount": 3135486746.0,
            "total_mv": 109965237787.0,
            "turnover_rate": 2.82,
            "volume_ratio": 0.77,
            "pe_ratio": 35.7257233,
            "pb_ratio": 3.00148195,
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
              "value": 50.1092,
              "liquidity": 98.1013,
              "momentum": 44.735,
              "reversal": 98.44,
              "activity": 83.2109,
              "stability": 67.14,
              "size": 97.2574,
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
    "code": "300009",
    "name": "安科生物",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 9,
    "best_score": 84.4456,
    "average_score": 84.4456,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 9,
        "score": 84.4456,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 9,
          "code": "300009",
          "name": "安科生物",
          "score": 84.4456,
          "screen_score": 82.44557759493671,
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
          "price": 8.65,
          "change_pct": -3.57,
          "amount": 560404438.99,
          "industry": "",
          "factor_scores": {
            "value": 58.8671,
            "liquidity": 84.3882,
            "momentum": 44.8975,
            "reversal": 99.09,
            "activity": 79.0495,
            "stability": 67.29,
            "size": 65.8228,
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
            "code": "300009",
            "name": "安科生物",
            "final_score": 84.4456,
            "screen_score": 82.44557759493671,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 8.65,
            "change_pct": -3.57,
            "amount": 560404438.99,
            "total_mv": 14451561124.0,
            "turnover_rate": 5.13,
            "volume_ratio": 1.4,
            "pe_ratio": 21.60083979,
            "pb_ratio": 3.15934409,
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
              "value": 58.8671,
              "liquidity": 84.3882,
              "momentum": 44.8975,
              "reversal": 99.09,
              "activity": 79.0495,
              "stability": 67.29,
              "size": 65.8228,
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
    "code": "600141",
    "name": "兴发集团",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 10,
    "best_score": 84.3998,
    "average_score": 84.3998,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 10,
        "score": 84.3998,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 10,
          "code": "600141",
          "name": "兴发集团",
          "score": 84.3998,
          "screen_score": 82.39976651898733,
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
          "price": 29.81,
          "change_pct": -2.84,
          "amount": 569644255.0,
          "industry": "",
          "factor_scores": {
            "value": 74.212,
            "liquidity": 85.0211,
            "momentum": 47.27,
            "reversal": 91.42,
            "activity": 79.3007,
            "stability": 69.48,
            "size": 88.1857,
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
            "code": "600141",
            "name": "兴发集团",
            "final_score": 84.3998,
            "screen_score": 82.39976651898733,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 29.81,
            "change_pct": -2.84,
            "amount": 569644255.0,
            "total_mv": 35823865137.0,
            "turnover_rate": 1.57,
            "volume_ratio": 0.9,
            "pe_ratio": 25.63775323,
            "pb_ratio": 1.47390227,
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
              "value": 74.212,
              "liquidity": 85.0211,
              "momentum": 47.27,
              "reversal": 91.42,
              "activity": 79.3007,
              "stability": 69.48,
              "size": 88.1857,
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
    "best_score": 75.3746,
    "average_score": 75.3746,
    "strategy_details": {
      "momentum_quality": {
        "rank": 1,
        "score": 75.3746,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 1,
          "code": "601318",
          "name": "中国平安",
          "score": 75.3746,
          "screen_score": 73.574579803719,
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
          "price": 55.17,
          "change_pct": 3.41,
          "amount": 5076589284.0,
          "industry": "",
          "factor_scores": {
            "value": 84.3585,
            "liquidity": 99.1736,
            "momentum": 67.5825,
            "reversal": 5.0,
            "activity": 72.4244,
            "stability": 67.77,
            "size": 97.5207,
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
              "fetched_at": "2026-08-24T03:57:12.291863+00:00",
              "price": 55.17,
              "change_pct": 3.41,
              "change_amount": 1.82,
              "volume": 93051100,
              "amount": 5076589284.0,
              "volume_ratio": 2.67,
              "turnover_rate": 0.87,
              "amplitude": 3.6,
              "open_price": 53.34,
              "high": 55.22,
              "low": 53.3,
              "pre_close": 53.35,
              "pe_ratio": 6.27,
              "pb_ratio": 0.97,
              "total_mv": 998999000000.0,
              "circ_mv": 588116000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 55.17, 涨跌幅 3.41%",
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
            "final_score": 75.3746,
            "screen_score": 73.574579803719,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 55.17,
            "change_pct": 3.41,
            "amount": 5076589284.0,
            "total_mv": 998998608864.0,
            "turnover_rate": 0.87,
            "volume_ratio": 2.67,
            "pe_ratio": 6.06368915,
            "pb_ratio": 0.93965347,
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
              "value": 84.3585,
              "liquidity": 99.1736,
              "momentum": 67.5825,
              "reversal": 5.0,
              "activity": 72.4244,
              "stability": 67.77,
              "size": 97.5207,
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
                "fetched_at": "2026-08-24T03:57:12.291863+00:00",
                "price": 55.17,
                "change_pct": 3.41,
                "change_amount": 1.82,
                "volume": 93051100,
                "amount": 5076589284.0,
                "volume_ratio": 2.67,
                "turnover_rate": 0.87,
                "amplitude": 3.6,
                "open_price": 53.34,
                "high": 55.22,
                "low": 53.3,
                "pre_close": 53.35,
                "pe_ratio": 6.27,
                "pb_ratio": 0.97,
                "total_mv": 998999000000.0,
                "circ_mv": 588116000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 55.17, 涨跌幅 3.41%",
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
    "best_rank": 2,
    "best_score": 74.6066,
    "average_score": 74.6066,
    "strategy_details": {
      "momentum_quality": {
        "rank": 2,
        "score": 74.6066,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 2,
          "code": "600036",
          "name": "招商银行",
          "score": 74.6066,
          "screen_score": 72.80655198002754,
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
          "price": 39.61,
          "change_pct": 1.83,
          "amount": 2567379565.0,
          "industry": "",
          "factor_scores": {
            "value": 84.8578,
            "liquidity": 95.3168,
            "momentum": 62.4475,
            "reversal": 30.57,
            "activity": 70.4444,
            "stability": 72.51,
            "size": 97.2452,
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
              "fetched_at": "2026-08-24T03:57:24.432904+00:00",
              "price": 39.61,
              "change_pct": 1.83,
              "change_amount": 0.71,
              "volume": 65251900,
              "amount": 2567379565.0,
              "volume_ratio": 1.73,
              "turnover_rate": 0.32,
              "amplitude": 2.26,
              "open_price": 38.87,
              "high": 39.65,
              "low": 38.77,
              "pre_close": 38.9,
              "pe_ratio": 6.63,
              "pb_ratio": 0.9,
              "total_mv": 998958000000.0,
              "circ_mv": 817112000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 39.61, 涨跌幅 1.83%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality"
          },
          "post_analysis_tags": [
            "value_quality"
          ],
          "raw": {
            "rank": 2,
            "code": "600036",
            "name": "招商银行",
            "final_score": 74.6066,
            "screen_score": 72.80655198002754,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 39.61,
            "change_pct": 1.83,
            "amount": 2567379565.0,
            "total_mv": 998958084256.0,
            "turnover_rate": 0.32,
            "volume_ratio": 1.73,
            "pe_ratio": 6.5079371,
            "pb_ratio": 0.86637359,
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
              "value": 84.8578,
              "liquidity": 95.3168,
              "momentum": 62.4475,
              "reversal": 30.57,
              "activity": 70.4444,
              "stability": 72.51,
              "size": 97.2452,
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
                "fetched_at": "2026-08-24T03:57:24.432904+00:00",
                "price": 39.61,
                "change_pct": 1.83,
                "change_amount": 0.71,
                "volume": 65251900,
                "amount": 2567379565.0,
                "volume_ratio": 1.73,
                "turnover_rate": 0.32,
                "amplitude": 2.26,
                "open_price": 38.87,
                "high": 39.65,
                "low": 38.77,
                "pre_close": 38.9,
                "pe_ratio": 6.63,
                "pb_ratio": 0.9,
                "total_mv": 998958000000.0,
                "circ_mv": 817112000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 39.61, 涨跌幅 1.83%",
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
    "code": "601166",
    "name": "兴业银行",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 3,
    "best_score": 74.0852,
    "average_score": 74.0852,
    "strategy_details": {
      "momentum_quality": {
        "rank": 3,
        "score": 74.0852,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 3,
          "code": "601166",
          "name": "兴业银行",
          "score": 74.0852,
          "screen_score": 72.28523737947658,
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
          "price": 18.28,
          "change_pct": 0.99,
          "amount": 1378283225.0,
          "industry": "",
          "factor_scores": {
            "value": 89.4342,
            "liquidity": 88.1543,
            "momentum": 59.7175,
            "reversal": 48.13,
            "activity": 69.8624,
            "stability": 75.03,
            "size": 93.6639,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "601166",
              "name": "兴业银行",
              "source": "tencent",
              "fetched_at": "2026-08-24T03:57:35.911855+00:00",
              "price": 18.28,
              "change_pct": 0.99,
              "change_amount": 0.18,
              "volume": 75923600,
              "amount": 1378283225.0,
              "volume_ratio": 1.57,
              "turnover_rate": 0.36,
              "amplitude": 1.49,
              "open_price": 18.05,
              "high": 18.29,
              "low": 18.02,
              "pre_close": 18.1,
              "pe_ratio": 4.99,
              "pb_ratio": 0.47,
              "total_mv": 386857000000.0,
              "circ_mv": 386857000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 18.28, 涨跌幅 0.99%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality"
          },
          "post_analysis_tags": [
            "value_quality"
          ],
          "raw": {
            "rank": 3,
            "code": "601166",
            "name": "兴业银行",
            "final_score": 74.0852,
            "screen_score": 72.28523737947658,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 18.28,
            "change_pct": 0.99,
            "amount": 1378283225.0,
            "total_mv": 386857071898.0,
            "turnover_rate": 0.36,
            "volume_ratio": 1.57,
            "pe_ratio": 4.94223285,
            "pb_ratio": 0.46153557,
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
              "value": 89.4342,
              "liquidity": 88.1543,
              "momentum": 59.7175,
              "reversal": 48.13,
              "activity": 69.8624,
              "stability": 75.03,
              "size": 93.6639,
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
                "code": "601166",
                "name": "兴业银行",
                "source": "tencent",
                "fetched_at": "2026-08-24T03:57:35.911855+00:00",
                "price": 18.28,
                "change_pct": 0.99,
                "change_amount": 0.18,
                "volume": 75923600,
                "amount": 1378283225.0,
                "volume_ratio": 1.57,
                "turnover_rate": 0.36,
                "amplitude": 1.49,
                "open_price": 18.05,
                "high": 18.29,
                "low": 18.02,
                "pre_close": 18.1,
                "pe_ratio": 4.99,
                "pb_ratio": 0.47,
                "total_mv": 386857000000.0,
                "circ_mv": 386857000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 18.28, 涨跌幅 0.99%",
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
    "best_rank": 4,
    "best_score": 74.0199,
    "average_score": 74.0199,
    "strategy_details": {
      "momentum_quality": {
        "rank": 4,
        "score": 74.0199,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 4,
          "code": "601398",
          "name": "工商银行",
          "score": 74.0199,
          "screen_score": 72.21991844008264,
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
          "price": 7.9,
          "change_pct": 1.67,
          "amount": 1852634602.0,
          "industry": "",
          "factor_scores": {
            "value": 85.707,
            "liquidity": 92.8375,
            "momentum": 61.9275,
            "reversal": 33.93,
            "activity": 67.9829,
            "stability": 72.99,
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
            "rank": 4,
            "code": "601398",
            "name": "工商银行",
            "final_score": 74.0199,
            "screen_score": 72.21991844008264,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 7.9,
            "change_pct": 1.67,
            "amount": 1852634602.0,
            "total_mv": 2815609431003.0,
            "turnover_rate": 0.09,
            "volume_ratio": 1.37,
            "pe_ratio": 7.4573825,
            "pb_ratio": 0.7023747,
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
              "value": 85.707,
              "liquidity": 92.8375,
              "momentum": 61.9275,
              "reversal": 33.93,
              "activity": 67.9829,
              "stability": 72.99,
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
    "code": "601919",
    "name": "中远海控",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 5,
    "best_score": 73.6454,
    "average_score": 73.6454,
    "strategy_details": {
      "momentum_quality": {
        "rank": 5,
        "score": 73.6454,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 5,
          "code": "601919",
          "name": "中远海控",
          "score": 73.6454,
          "screen_score": 71.84539817493113,
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
          "price": 17.33,
          "change_pct": 1.88,
          "amount": 1868685132.0,
          "industry": "",
          "factor_scores": {
            "value": 78.9535,
            "liquidity": 93.3884,
            "momentum": 62.61,
            "reversal": 29.52,
            "activity": 73.1598,
            "stability": 72.36,
            "size": 91.1846,
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
            "code": "601919",
            "name": "中远海控",
            "final_score": 73.6454,
            "screen_score": 71.84539817493113,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 17.33,
            "change_pct": 1.88,
            "amount": 1868685132.0,
            "total_mv": 264596570983.0,
            "turnover_rate": 0.86,
            "volume_ratio": 1.9,
            "pe_ratio": 10.36746856,
            "pb_ratio": 1.10191876,
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
              "value": 78.9535,
              "liquidity": 93.3884,
              "momentum": 62.61,
              "reversal": 29.52,
              "activity": 73.1598,
              "stability": 72.36,
              "size": 91.1846,
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
    "code": "601601",
    "name": "中国太保",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 6,
    "best_score": 73.6165,
    "average_score": 73.6165,
    "strategy_details": {
      "momentum_quality": {
        "rank": 6,
        "score": 73.6165,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 6,
          "code": "601601",
          "name": "中国太保",
          "score": 73.6165,
          "screen_score": 71.81651317148759,
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
          "price": 31.18,
          "change_pct": 2.5,
          "amount": 1505200479.0,
          "industry": "",
          "factor_scores": {
            "value": 85.2228,
            "liquidity": 89.8072,
            "momentum": 64.625,
            "reversal": 16.5,
            "activity": 72.1206,
            "stability": 70.5,
            "size": 91.7355,
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
            "code": "601601",
            "name": "中国太保",
            "final_score": 73.6165,
            "screen_score": 71.81651317148759,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 31.18,
            "change_pct": 2.5,
            "amount": 1505200479.0,
            "total_mv": 299962246567.0,
            "turnover_rate": 0.71,
            "volume_ratio": 2.61,
            "pe_ratio": 5.42760042,
            "pb_ratio": 0.91567258,
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
              "value": 85.2228,
              "liquidity": 89.8072,
              "momentum": 64.625,
              "reversal": 16.5,
              "activity": 72.1206,
              "stability": 70.5,
              "size": 91.7355,
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
    "code": "601288",
    "name": "农业银行",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 7,
    "best_score": 73.3378,
    "average_score": 73.3378,
    "strategy_details": {
      "momentum_quality": {
        "rank": 7,
        "score": 73.3378,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 7,
          "code": "601288",
          "name": "农业银行",
          "score": 73.3378,
          "screen_score": 71.537776119146,
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
          "price": 6.85,
          "change_pct": 1.03,
          "amount": 1596148641.0,
          "industry": "",
          "factor_scores": {
            "value": 84.0733,
            "liquidity": 90.6336,
            "momentum": 59.8475,
            "reversal": 47.37,
            "activity": 66.5496,
            "stability": 74.91,
            "size": 99.449,
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
            "rank": 7,
            "code": "601288",
            "name": "农业银行",
            "final_score": 73.3378,
            "screen_score": 71.537776119146,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 6.85,
            "change_pct": 1.03,
            "amount": 1596148641.0,
            "total_mv": 2397383782030.0,
            "turnover_rate": 0.07,
            "volume_ratio": 1.07,
            "pe_ratio": 8.06294694,
            "pb_ratio": 0.83948709,
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
              "value": 84.0733,
              "liquidity": 90.6336,
              "momentum": 59.8475,
              "reversal": 47.37,
              "activity": 66.5496,
              "stability": 74.91,
              "size": 99.449,
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
    "best_rank": 8,
    "best_score": 72.9623,
    "average_score": 72.9623,
    "strategy_details": {
      "momentum_quality": {
        "rank": 8,
        "score": 72.9623,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 8,
          "code": "600030",
          "name": "中信证券",
          "score": 72.9623,
          "screen_score": 71.16226103650136,
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
          "price": 27.29,
          "change_pct": 0.63,
          "amount": 1859506495.0,
          "industry": "",
          "factor_scores": {
            "value": 75.5114,
            "liquidity": 93.1129,
            "momentum": 58.5475,
            "reversal": 52.81,
            "activity": 70.3101,
            "stability": 76.11,
            "size": 94.4904,
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
            "rank": 8,
            "code": "600030",
            "name": "中信证券",
            "final_score": 72.9623,
            "screen_score": 71.16226103650136,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 27.29,
            "change_pct": 0.63,
            "amount": 1859506495.0,
            "total_mv": 426386388665.0,
            "turnover_rate": 0.56,
            "volume_ratio": 1.51,
            "pe_ratio": 10.68521394,
            "pb_ratio": 1.43406804,
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
              "value": 75.5114,
              "liquidity": 93.1129,
              "momentum": 58.5475,
              "reversal": 52.81,
              "activity": 70.3101,
              "stability": 76.11,
              "size": 94.4904,
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
    "code": "000426",
    "name": "兴业银锡",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 1,
    "best_score": 72.7624,
    "average_score": 72.7624,
    "strategy_details": {
      "capital_heat": {
        "rank": 1,
        "score": 72.7624,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 1,
          "code": "000426",
          "name": "兴业银锡",
          "score": 72.7624,
          "screen_score": 72.76236470588236,
          "reason": "本地后置评分: 未发现额外加分项",
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
          "price": 41.3,
          "change_pct": 1.03,
          "amount": 4993170893.2,
          "industry": "",
          "factor_scores": {
            "value": 52.7036,
            "liquidity": 98.8235,
            "momentum": 59.8475,
            "reversal": 47.37,
            "activity": 83.62,
            "stability": 74.91,
            "size": 95.2941,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "000426",
              "name": "兴业银锡",
              "source": "tencent",
              "fetched_at": "2026-08-24T03:56:41.871556+00:00",
              "price": 41.3,
              "change_pct": 1.03,
              "change_amount": 0.42,
              "volume": 120932800,
              "amount": 4993170893.0,
              "volume_ratio": 3.04,
              "turnover_rate": 6.81,
              "amplitude": 8.12,
              "open_price": 40.89,
              "high": 43.02,
              "low": 39.7,
              "pre_close": 40.88,
              "pe_ratio": 27.49,
              "pb_ratio": 6.77,
              "total_mv": 73334000000.0,
              "circ_mv": 73316000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 41.3, 涨跌幅 1.03%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: 未发现额外加分项"
          },
          "post_analysis_tags": [],
          "raw": {
            "rank": 1,
            "code": "000426",
            "name": "兴业银锡",
            "final_score": 72.7624,
            "screen_score": 72.76236470588236,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 41.3,
            "change_pct": 1.03,
            "amount": 4993170893.2,
            "total_mv": 73333756021.0,
            "turnover_rate": 6.81,
            "volume_ratio": 3.04,
            "pe_ratio": 27.21144433,
            "pb_ratio": 6.70529886,
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
              "value": 52.7036,
              "liquidity": 98.8235,
              "momentum": 59.8475,
              "reversal": 47.37,
              "activity": 83.62,
              "stability": 74.91,
              "size": 95.2941,
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
              "scorecard": "本地后置评分: 未发现额外加分项"
            },
            "post_analysis_score_deltas": {
              "scorecard": 0.0
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": []
              }
            },
            "post_analysis_tags": [],
            "dsa_context": {
              "enriched": true,
              "profile": "pre_rank_light",
              "news_included": false,
              "events_included": false,
              "quote": {
                "code": "000426",
                "name": "兴业银锡",
                "source": "tencent",
                "fetched_at": "2026-08-24T03:56:41.871556+00:00",
                "price": 41.3,
                "change_pct": 1.03,
                "change_amount": 0.42,
                "volume": 120932800,
                "amount": 4993170893.0,
                "volume_ratio": 3.04,
                "turnover_rate": 6.81,
                "amplitude": 8.12,
                "open_price": 40.89,
                "high": 43.02,
                "low": 39.7,
                "pre_close": 40.88,
                "pe_ratio": 27.49,
                "pb_ratio": 6.77,
                "total_mv": 73334000000.0,
                "circ_mv": 73316000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 41.3, 涨跌幅 1.03%",
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
    "code": "300390",
    "name": "天华新能",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 2,
    "best_score": 72.5149,
    "average_score": 72.5149,
    "strategy_details": {
      "capital_heat": {
        "rank": 2,
        "score": 72.5149,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 2,
          "code": "300390",
          "name": "天华新能",
          "score": 72.5149,
          "screen_score": 72.51486911764707,
          "reason": "本地后置评分: 未发现额外加分项",
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
          "price": 67.85,
          "change_pct": 3.64,
          "amount": 3141178820.82,
          "industry": "",
          "factor_scores": {
            "value": 67.8179,
            "liquidity": 96.4706,
            "momentum": 68.33,
            "reversal": 5.0,
            "activity": 83.2356,
            "stability": 67.08,
            "size": 94.1176,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "300390",
              "name": "天华新能",
              "source": "tencent",
              "fetched_at": "2026-08-24T03:56:52.053061+00:00",
              "price": 67.85,
              "change_pct": 3.64,
              "change_amount": 2.38,
              "volume": 45514300,
              "amount": 3141178821.0,
              "volume_ratio": 2.15,
              "turnover_rate": 6.4,
              "amplitude": 5.13,
              "open_price": 67.61,
              "high": 70.8,
              "low": 67.44,
              "pre_close": 65.47,
              "pe_ratio": 20.24,
              "pb_ratio": 4.11,
              "total_mv": 56366000000.0,
              "circ_mv": 48275000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 67.85, 涨跌幅 3.64%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: 未发现额外加分项"
          },
          "post_analysis_tags": [],
          "raw": {
            "rank": 2,
            "code": "300390",
            "name": "天华新能",
            "final_score": 72.5149,
            "screen_score": 72.51486911764707,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 67.85,
            "change_pct": 3.64,
            "amount": 3141178820.82,
            "total_mv": 56366440966.0,
            "turnover_rate": 6.4,
            "volume_ratio": 2.15,
            "pe_ratio": 19.52698548,
            "pb_ratio": 3.96324177,
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
              "value": 67.8179,
              "liquidity": 96.4706,
              "momentum": 68.33,
              "reversal": 5.0,
              "activity": 83.2356,
              "stability": 67.08,
              "size": 94.1176,
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
              "scorecard": "本地后置评分: 未发现额外加分项"
            },
            "post_analysis_score_deltas": {
              "scorecard": 0.0
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": []
              }
            },
            "post_analysis_tags": [],
            "dsa_context": {
              "enriched": true,
              "profile": "pre_rank_light",
              "news_included": false,
              "events_included": false,
              "quote": {
                "code": "300390",
                "name": "天华新能",
                "source": "tencent",
                "fetched_at": "2026-08-24T03:56:52.053061+00:00",
                "price": 67.85,
                "change_pct": 3.64,
                "change_amount": 2.38,
                "volume": 45514300,
                "amount": 3141178821.0,
                "volume_ratio": 2.15,
                "turnover_rate": 6.4,
                "amplitude": 5.13,
                "open_price": 67.61,
                "high": 70.8,
                "low": 67.44,
                "pre_close": 65.47,
                "pe_ratio": 20.24,
                "pb_ratio": 4.11,
                "total_mv": 56366000000.0,
                "circ_mv": 48275000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 67.85, 涨跌幅 3.64%",
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
    "code": "601020",
    "name": "华钰矿业",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 3,
    "best_score": 72.4308,
    "average_score": 72.4308,
    "strategy_details": {
      "capital_heat": {
        "rank": 3,
        "score": 72.4308,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 3,
          "code": "601020",
          "name": "华钰矿业",
          "score": 72.4308,
          "screen_score": 70.03081382352941,
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
          "price": 23.25,
          "change_pct": 5.01,
          "amount": 996363109.0,
          "industry": "",
          "factor_scores": {
            "value": 64.025,
            "liquidity": 75.2941,
            "momentum": 72.7825,
            "reversal": 5.0,
            "activity": 82.8441,
            "stability": 62.97,
            "size": 64.7059,
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
            "rank": 3,
            "code": "601020",
            "name": "华钰矿业",
            "final_score": 72.4308,
            "screen_score": 70.03081382352941,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 23.25,
            "change_pct": 5.01,
            "amount": 996363109.0,
            "total_mv": 19064179229.0,
            "turnover_rate": 5.34,
            "volume_ratio": 3.33,
            "pe_ratio": 21.21708398,
            "pb_ratio": 4.22174973,
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
              "value": 64.025,
              "liquidity": 75.2941,
              "momentum": 72.7825,
              "reversal": 5.0,
              "activity": 82.8441,
              "stability": 62.97,
              "size": 64.7059,
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
    "code": "000651",
    "name": "格力电器",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 9,
    "best_score": 72.2234,
    "average_score": 72.2234,
    "strategy_details": {
      "momentum_quality": {
        "rank": 9,
        "score": 72.2234,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 9,
          "code": "000651",
          "name": "格力电器",
          "score": 72.2234,
          "screen_score": 70.42338613980715,
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
          "price": 41.48,
          "change_pct": 0.58,
          "amount": 1435527800.78,
          "industry": "",
          "factor_scores": {
            "value": 75.6911,
            "liquidity": 88.9807,
            "momentum": 58.385,
            "reversal": 53.46,
            "activity": 70.8344,
            "stability": 76.26,
            "size": 89.5317,
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
            "rank": 9,
            "code": "000651",
            "name": "格力电器",
            "final_score": 72.2234,
            "screen_score": 70.42338613980715,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 41.48,
            "change_pct": 0.58,
            "amount": 1435527800.78,
            "total_mv": 232346310137.0,
            "turnover_rate": 0.63,
            "volume_ratio": 1.57,
            "pe_ratio": 7.91623076,
            "pb_ratio": 1.5195073,
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
              "value": 75.6911,
              "liquidity": 88.9807,
              "momentum": 58.385,
              "reversal": 53.46,
              "activity": 70.8344,
              "stability": 76.26,
              "size": 89.5317,
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
    "code": "000001",
    "name": "平安银行",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 10,
    "best_score": 72.1011,
    "average_score": 72.1011,
    "strategy_details": {
      "momentum_quality": {
        "rank": 10,
        "score": 72.1011,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 10,
          "code": "000001",
          "name": "平安银行",
          "score": 72.1011,
          "screen_score": 70.30113768939393,
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
          "price": 11.56,
          "change_pct": 1.31,
          "amount": 885829193.75,
          "industry": "",
          "factor_scores": {
            "value": 89.0148,
            "liquidity": 78.7879,
            "momentum": 60.7575,
            "reversal": 41.49,
            "activity": 69.5526,
            "stability": 74.07,
            "size": 88.7052,
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
            "rank": 10,
            "code": "000001",
            "name": "平安银行",
            "final_score": 72.1011,
            "screen_score": 70.30113768939393,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 11.56,
            "change_pct": 1.31,
            "amount": 885829193.75,
            "total_mv": 224332414369.0,
            "turnover_rate": 0.4,
            "volume_ratio": 1.47,
            "pe_ratio": 5.09495218,
            "pb_ratio": 0.47290668,
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
              "value": 89.0148,
              "liquidity": 78.7879,
              "momentum": 60.7575,
              "reversal": 41.49,
              "activity": 69.5526,
              "stability": 74.07,
              "size": 88.7052,
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
    "code": "001337",
    "name": "四川黄金",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 4,
    "best_score": 71.7641,
    "average_score": 71.7641,
    "strategy_details": {
      "capital_heat": {
        "rank": 4,
        "score": 71.7641,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 4,
          "code": "001337",
          "name": "四川黄金",
          "score": 71.7641,
          "screen_score": 71.3641455882353,
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
          "price": 55.2,
          "change_pct": 7.25,
          "amount": 1549983190.74,
          "industry": "",
          "factor_scores": {
            "value": 41.3821,
            "liquidity": 82.3529,
            "momentum": 74.2125,
            "reversal": 5.0,
            "activity": 84.3381,
            "stability": 56.25,
            "size": 72.9412,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "001337",
              "name": "四川黄金",
              "source": "tencent",
              "fetched_at": "2026-08-24T03:57:02.187815+00:00",
              "price": 55.2,
              "change_pct": 7.25,
              "change_amount": 3.73,
              "volume": 28787900,
              "amount": 1549983191.0,
              "volume_ratio": 2.85,
              "turnover_rate": 6.85,
              "amplitude": 11.29,
              "open_price": 51.97,
              "high": 56.62,
              "low": 50.81,
              "pre_close": 51.47,
              "pe_ratio": 33.61,
              "pb_ratio": 11.26,
              "total_mv": 23184000000.0,
              "circ_mv": 23184000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 55.2, 涨跌幅 7.25%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 4,
            "code": "001337",
            "name": "四川黄金",
            "final_score": 71.7641,
            "screen_score": 71.3641455882353,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 55.2,
            "change_pct": 7.25,
            "amount": 1549983190.74,
            "total_mv": 23184000000.0,
            "turnover_rate": 6.85,
            "volume_ratio": 2.85,
            "pe_ratio": 31.33993868,
            "pb_ratio": 10.50196713,
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
              "value": 41.3821,
              "liquidity": 82.3529,
              "momentum": 74.2125,
              "reversal": 5.0,
              "activity": 84.3381,
              "stability": 56.25,
              "size": 72.9412,
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
                "code": "001337",
                "name": "四川黄金",
                "source": "tencent",
                "fetched_at": "2026-08-24T03:57:02.187815+00:00",
                "price": 55.2,
                "change_pct": 7.25,
                "change_amount": 3.73,
                "volume": 28787900,
                "amount": 1549983191.0,
                "volume_ratio": 2.85,
                "turnover_rate": 6.85,
                "amplitude": 11.29,
                "open_price": 51.97,
                "high": 56.62,
                "low": 50.81,
                "pre_close": 51.47,
                "pe_ratio": 33.61,
                "pb_ratio": 11.26,
                "total_mv": 23184000000.0,
                "circ_mv": 23184000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 55.2, 涨跌幅 7.25%",
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
    "code": "002469",
    "name": "三维化学",
    "resonance_count": 1,
    "strategies": [
      "volume_breakout"
    ],
    "strategy_labels": [
      "放量突破"
    ],
    "best_rank": 1,
    "best_score": 71.7398,
    "average_score": 71.7398,
    "strategy_details": {
      "volume_breakout": {
        "rank": 1,
        "score": 71.7398,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 1,
          "code": "002469",
          "name": "三维化学",
          "score": 71.7398,
          "screen_score": 71.73977980266667,
          "reason": "本地后置评分: 未发现额外加分项",
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
          "price": 6.69,
          "change_pct": 3.08,
          "amount": 200137196.81,
          "industry": "",
          "factor_scores": {
            "value": 57.5,
            "liquidity": 66.6667,
            "momentum": 71.4929,
            "reversal": 5.0,
            "activity": 83.1955,
            "stability": 69.0066,
            "size": 66.6667,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "002469",
              "name": "三维化学",
              "source": "tencent",
              "fetched_at": "2026-08-24T03:56:10.808914+00:00",
              "price": 6.69,
              "change_pct": 3.08,
              "change_amount": 0.2,
              "volume": 30333600,
              "amount": 200137197.0,
              "volume_ratio": 3.04,
              "turnover_rate": 4.82,
              "amplitude": 9.55,
              "open_price": 6.3,
              "high": 6.85,
              "low": 6.23,
              "pre_close": 6.49,
              "pe_ratio": 42.71,
              "pb_ratio": 1.7,
              "total_mv": 4341000000.0,
              "circ_mv": 4208000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 6.69, 涨跌幅 3.08%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: 未发现额外加分项"
          },
          "post_analysis_tags": [],
          "raw": {
            "rank": 1,
            "code": "002469",
            "name": "三维化学",
            "final_score": 71.7398,
            "screen_score": 71.73977980266667,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 6.69,
            "change_pct": 3.08,
            "amount": 200137196.81,
            "total_mv": 4340890995.0,
            "turnover_rate": 4.82,
            "volume_ratio": 3.04,
            "pe_ratio": 41.43581807,
            "pb_ratio": 1.6453481,
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
            "change_60d": 1.5649,
            "signal_score": 72.5477,
            "ma_bullish": false,
            "price_above_ma20": true,
            "macd_status": "bullish",
            "rsi_status": "neutral",
            "breakout_20d_pct": 2.8526,
            "range_20d_pct": 22.6415,
            "volume_ratio_20d": 3.9377,
            "body_pct": 6.7434,
            "pullback_to_ma20_pct": 10.581,
            "consolidation_days_20d": 15,
            "volatility_20d_pct": 50.4648,
            "max_drawdown_20d_pct": -4.4374,
            "atr_20_pct": 3.1048,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:AkshareFetcher",
            "factor_scores": {
              "value": 57.5,
              "liquidity": 66.6667,
              "momentum": 71.4929,
              "reversal": 5.0,
              "activity": 83.1955,
              "stability": 69.0066,
              "size": 66.6667,
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
              "scorecard": "本地后置评分: 未发现额外加分项"
            },
            "post_analysis_score_deltas": {
              "scorecard": 0.0
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": []
              }
            },
            "post_analysis_tags": [],
            "dsa_context": {
              "enriched": true,
              "profile": "pre_rank_light",
              "news_included": false,
              "events_included": false,
              "quote": {
                "code": "002469",
                "name": "三维化学",
                "source": "tencent",
                "fetched_at": "2026-08-24T03:56:10.808914+00:00",
                "price": 6.69,
                "change_pct": 3.08,
                "change_amount": 0.2,
                "volume": 30333600,
                "amount": 200137197.0,
                "volume_ratio": 3.04,
                "turnover_rate": 4.82,
                "amplitude": 9.55,
                "open_price": 6.3,
                "high": 6.85,
                "low": 6.23,
                "pre_close": 6.49,
                "pe_ratio": 42.71,
                "pb_ratio": 1.7,
                "total_mv": 4341000000.0,
                "circ_mv": 4208000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 6.69, 涨跌幅 3.08%",
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
    "code": "601958",
    "name": "金钼股份",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 5,
    "best_score": 71.1467,
    "average_score": 71.1467,
    "strategy_details": {
      "capital_heat": {
        "rank": 5,
        "score": 71.1467,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 5,
          "code": "601958",
          "name": "金钼股份",
          "score": 71.1467,
          "screen_score": 68.74672235294119,
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
          "price": 23.33,
          "change_pct": 6.34,
          "amount": 2308818381.0,
          "industry": "",
          "factor_scores": {
            "value": 69.9321,
            "liquidity": 89.4118,
            "momentum": 77.105,
            "reversal": 5.0,
            "activity": 66.733,
            "stability": 58.82,
            "size": 96.4706,
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
            "code": "601958",
            "name": "金钼股份",
            "final_score": 71.1467,
            "screen_score": 68.74672235294119,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 23.33,
            "change_pct": 6.34,
            "amount": 2308818381.0,
            "total_mv": 75276680652.0,
            "turnover_rate": 3.02,
            "volume_ratio": 5.04,
            "pe_ratio": 20.14846155,
            "pb_ratio": 3.4250181,
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
              "value": 69.9321,
              "liquidity": 89.4118,
              "momentum": 77.105,
              "reversal": 5.0,
              "activity": 66.733,
              "stability": 58.82,
              "size": 96.4706,
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
    "code": "601069",
    "name": "西部黄金",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 6,
    "best_score": 70.8788,
    "average_score": 70.8788,
    "strategy_details": {
      "capital_heat": {
        "rank": 6,
        "score": 70.8788,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 6,
          "code": "601069",
          "name": "西部黄金",
          "score": 70.8788,
          "screen_score": 70.87878647058824,
          "reason": "本地后置评分: 未发现额外加分项",
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
          "price": 33.14,
          "change_pct": 3.34,
          "amount": 1782718732.0,
          "industry": "",
          "factor_scores": {
            "value": 53.7179,
            "liquidity": 85.8824,
            "momentum": 67.355,
            "reversal": 5.0,
            "activity": 84.2358,
            "stability": 67.98,
            "size": 84.7059,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: 未发现额外加分项"
          },
          "post_analysis_tags": [],
          "raw": {
            "rank": 6,
            "code": "601069",
            "name": "西部黄金",
            "final_score": 70.8788,
            "screen_score": 70.87878647058824,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 33.14,
            "change_pct": 3.34,
            "amount": 1782718732.0,
            "total_mv": 30190510936.0,
            "turnover_rate": 6.16,
            "volume_ratio": 3.42,
            "pe_ratio": 30.09677322,
            "pb_ratio": 5.55779674,
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
              "value": 53.7179,
              "liquidity": 85.8824,
              "momentum": 67.355,
              "reversal": 5.0,
              "activity": 84.2358,
              "stability": 67.98,
              "size": 84.7059,
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
              "scorecard": "本地后置评分: 未发现额外加分项"
            },
            "post_analysis_score_deltas": {
              "scorecard": 0.0
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": []
              }
            },
            "post_analysis_tags": [],
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
    "code": "002466",
    "name": "天齐锂业",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 7,
    "best_score": 70.4829,
    "average_score": 70.4829,
    "strategy_details": {
      "capital_heat": {
        "rank": 7,
        "score": 70.4829,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 7,
          "code": "002466",
          "name": "天齐锂业",
          "score": 70.4829,
          "screen_score": 70.48289323529413,
          "reason": "本地后置评分: 未发现额外加分项",
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
          "price": 49.52,
          "change_pct": 2.36,
          "amount": 2792558270.73,
          "industry": "",
          "factor_scores": {
            "value": 70.2393,
            "liquidity": 92.9412,
            "momentum": 64.17,
            "reversal": 19.44,
            "activity": 79.3154,
            "stability": 70.92,
            "size": 97.6471,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: 未发现额外加分项"
          },
          "post_analysis_tags": [],
          "raw": {
            "rank": 7,
            "code": "002466",
            "name": "天齐锂业",
            "final_score": 70.4829,
            "screen_score": 70.48289323529413,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 49.52,
            "change_pct": 2.36,
            "amount": 2792558270.73,
            "total_mv": 84832969900.0,
            "turnover_rate": 3.78,
            "volume_ratio": 2.73,
            "pe_ratio": 37.09309644,
            "pb_ratio": 1.78806069,
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
              "value": 70.2393,
              "liquidity": 92.9412,
              "momentum": 64.17,
              "reversal": 19.44,
              "activity": 79.3154,
              "stability": 70.92,
              "size": 97.6471,
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
              "scorecard": "本地后置评分: 未发现额外加分项"
            },
            "post_analysis_score_deltas": {
              "scorecard": 0.0
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": []
              }
            },
            "post_analysis_tags": [],
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
    "code": "002460",
    "name": "赣锋锂业",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 8,
    "best_score": 70.1991,
    "average_score": 70.1991,
    "strategy_details": {
      "capital_heat": {
        "rank": 8,
        "score": 70.1991,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 8,
          "code": "002460",
          "name": "赣锋锂业",
          "score": 70.1991,
          "screen_score": 70.19912294117648,
          "reason": "本地后置评分: 未发现额外加分项",
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
          "price": 55.83,
          "change_pct": 3.16,
          "amount": 2621685167.74,
          "industry": "",
          "factor_scores": {
            "value": 70.3536,
            "liquidity": 91.7647,
            "momentum": 66.77,
            "reversal": 5.0,
            "activity": 78.9228,
            "stability": 68.52,
            "size": 98.8235,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: 未发现额外加分项"
          },
          "post_analysis_tags": [],
          "raw": {
            "rank": 8,
            "code": "002460",
            "name": "赣锋锂业",
            "final_score": 70.1991,
            "screen_score": 70.19912294117648,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 55.83,
            "change_pct": 3.16,
            "amount": 2621685167.74,
            "total_mv": 117058448575.0,
            "turnover_rate": 3.86,
            "volume_ratio": 2.58,
            "pe_ratio": 29.81359754,
            "pb_ratio": 2.4424542,
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
              "value": 70.3536,
              "liquidity": 91.7647,
              "momentum": 66.77,
              "reversal": 5.0,
              "activity": 78.9228,
              "stability": 68.52,
              "size": 98.8235,
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
              "scorecard": "本地后置评分: 未发现额外加分项"
            },
            "post_analysis_score_deltas": {
              "scorecard": 0.0
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": []
              }
            },
            "post_analysis_tags": [],
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
    "code": "688596",
    "name": "正帆科技",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 9,
    "best_score": 69.9349,
    "average_score": 69.9349,
    "strategy_details": {
      "capital_heat": {
        "rank": 9,
        "score": 69.9349,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 9,
          "code": "688596",
          "name": "正帆科技",
          "score": 69.9349,
          "screen_score": 69.93490588235295,
          "reason": "本地后置评分: 未发现额外加分项",
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
          "price": 69.32,
          "change_pct": 4.56,
          "amount": 1570776587.0,
          "industry": "",
          "factor_scores": {
            "value": 29.5321,
            "liquidity": 83.5294,
            "momentum": 71.32,
            "reversal": 5.0,
            "activity": 78.985,
            "stability": 64.32,
            "size": 70.5882,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {},
          "dsa_news": [],
          "dsa_events": [],
          "dsa_analysis_summary": "",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: 未发现额外加分项"
          },
          "post_analysis_tags": [],
          "raw": {
            "rank": 9,
            "code": "688596",
            "name": "正帆科技",
            "final_score": 69.9349,
            "screen_score": 69.93490588235295,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 69.32,
            "change_pct": 4.56,
            "amount": 1570776587.0,
            "total_mv": 22020916772.0,
            "turnover_rate": 7.19,
            "volume_ratio": 1.84,
            "pe_ratio": 276.10541578,
            "pb_ratio": 5.81051416,
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
              "value": 29.5321,
              "liquidity": 83.5294,
              "momentum": 71.32,
              "reversal": 5.0,
              "activity": 78.985,
              "stability": 64.32,
              "size": 70.5882,
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
              "scorecard": "本地后置评分: 未发现额外加分项"
            },
            "post_analysis_score_deltas": {
              "scorecard": 0.0
            },
            "post_analysis_results": {
              "scorecard": {
                "risk_flags": [],
                "tags": []
              }
            },
            "post_analysis_tags": [],
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
