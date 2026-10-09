# 《A股短线候选池（改造第1阶段）》

> 本报告只做四套原版模型自动合并、去重和模型共振统计；尚未加入题材、涨停梯队、市场情绪、竞价和开盘确认。

## 测试概况

- 阶段：`short_term_candidate_pool_v1`
- 市场：`cn`
- 每套模型返回数量：`10`
- 合并去重后的候选数量：`39`
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
| 1 | 600521 | 华海药业 | 2 | 放量突破、资金热度 | 75.48015 | 2 |
| 2 | 600150 | 中国船舶 | 1 | 超跌反转 | 91.6044 | 1 |
| 3 | 002074 | 国轩高科 | 1 | 超跌反转 | 90.0841 | 2 |
| 4 | 601975 | 招商南油 | 1 | 超跌反转 | 89.7194 | 3 |
| 5 | 300456 | 赛微电子 | 1 | 超跌反转 | 89.5463 | 4 |
| 6 | 002273 | 水晶光电 | 1 | 超跌反转 | 85.6391 | 5 |
| 7 | 601609 | 金田股份 | 1 | 超跌反转 | 85.6176 | 6 |
| 8 | 002008 | 大族激光 | 1 | 超跌反转 | 84.6968 | 7 |
| 9 | 603606 | 东方电缆 | 1 | 超跌反转 | 84.6839 | 8 |
| 10 | 300207 | 欣旺达 | 1 | 超跌反转 | 84.6554 | 9 |
| 11 | 603063 | 禾望电气 | 1 | 超跌反转 | 84.0582 | 10 |
| 12 | 300457 | 赢合科技 | 1 | 放量突破 | 79.4588 | 1 |
| 13 | 600988 | 赤峰黄金 | 1 | 资金热度 | 75.3049 | 1 |
| 14 | 600256 | 广汇能源 | 1 | 资金热度 | 74.8361 | 2 |
| 15 | 601398 | 工商银行 | 1 | 动量质量 | 74.7189 | 1 |
| 16 | 601318 | 中国平安 | 1 | 动量质量 | 74.6381 | 2 |
| 17 | 600036 | 招商银行 | 1 | 动量质量 | 74.5315 | 3 |
| 18 | 601328 | 交通银行 | 1 | 动量质量 | 74.3862 | 4 |
| 19 | 300418 | 昆仑万维 | 1 | 资金热度 | 74.2168 | 3 |
| 20 | 601939 | 建设银行 | 1 | 动量质量 | 73.6338 | 5 |
| 21 | 688099 | 晶晨股份 | 1 | 资金热度 | 73.519 | 4 |
| 22 | 601288 | 农业银行 | 1 | 动量质量 | 73.4069 | 6 |
| 23 | 601166 | 兴业银行 | 1 | 动量质量 | 73.3591 | 7 |
| 24 | 002460 | 赣锋锂业 | 1 | 资金热度 | 73.2374 | 5 |
| 25 | 600030 | 中信证券 | 1 | 动量质量 | 73.1272 | 8 |
| 26 | 601988 | 中国银行 | 1 | 动量质量 | 73.1033 | 9 |
| 27 | 603799 | 华友钴业 | 1 | 动量质量 | 72.7023 | 10 |
| 28 | 301238 | 瑞泰新材 | 1 | 放量突破 | 72.6329 | 3 |
| 29 | 002044 | 美年健康 | 1 | 放量突破 | 72.6161 | 4 |
| 30 | 603236 | 移远通信 | 1 | 资金热度 | 72.4233 | 6 |

## 模型明细与原始候选字段

完整的每套模型返回结果、每只股票的原始候选字段和策略明细请以同目录的 `candidate_pool.json` 为准。

```json
[
  {
    "code": "600521",
    "name": "华海药业",
    "resonance_count": 2,
    "strategies": [
      "volume_breakout",
      "capital_heat"
    ],
    "strategy_labels": [
      "放量突破",
      "资金热度"
    ],
    "best_rank": 2,
    "best_score": 78.5709,
    "average_score": 75.48015,
    "strategy_details": {
      "volume_breakout": {
        "rank": 2,
        "score": 78.5709,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 2,
          "code": "600521",
          "name": "华海药业",
          "score": 78.5709,
          "screen_score": 77.8708791671579,
          "reason": "本地后置评分: capital_confirmed",
          "risk_level": "low",
          "risk_flags": [
            "rsi_overbought"
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
          "price": 17.45,
          "change_pct": 4.8,
          "amount": 1238170946.0,
          "industry": "",
          "factor_scores": {
            "value": 43.293,
            "liquidity": 94.7368,
            "momentum": 74.0947,
            "reversal": 5.0,
            "activity": 81.199,
            "stability": 65.8274,
            "size": 94.7368,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "600521",
              "name": "华海药业",
              "source": "tencent",
              "fetched_at": "2026-10-09T16:24:16.694580+00:00",
              "price": 17.45,
              "change_pct": 4.8,
              "change_amount": 0.8,
              "volume": 72199500,
              "amount": 1238170946.0,
              "volume_ratio": 2.52,
              "turnover_rate": 4.82,
              "amplitude": 5.29,
              "open_price": 16.77,
              "high": 17.46,
              "low": 16.58,
              "pre_close": 16.65,
              "pe_ratio": 41.62,
              "pb_ratio": 2.74,
              "total_mv": 26127000000.0,
              "circ_mv": 26127000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 17.45, 涨跌幅 4.8%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 2,
            "code": "600521",
            "name": "华海药业",
            "final_score": 78.5709,
            "screen_score": 77.8708791671579,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 17.45,
            "change_pct": 4.8,
            "amount": 1238170946.0,
            "total_mv": 26127077135.0,
            "turnover_rate": 4.82,
            "volume_ratio": 2.52,
            "pe_ratio": 41.6154219,
            "pb_ratio": 2.73913113,
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
            "change_60d": 7.3186,
            "signal_score": 68.5615,
            "ma_bullish": false,
            "price_above_ma20": true,
            "macd_status": "bullish",
            "rsi_status": "overbought",
            "breakout_20d_pct": 2.0468,
            "range_20d_pct": 15.2475,
            "volume_ratio_20d": 3.3321,
            "body_pct": 4.0549,
            "pullback_to_ma20_pct": 8.3447,
            "consolidation_days_20d": 13,
            "volatility_20d_pct": 34.1741,
            "max_drawdown_20d_pct": -4.6819,
            "atr_20_pct": 2.6791,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:EfinanceFetcher",
            "factor_scores": {
              "value": 43.293,
              "liquidity": 94.7368,
              "momentum": 74.0947,
              "reversal": 5.0,
              "activity": 81.199,
              "stability": 65.8274,
              "size": 94.7368,
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
            "risk_score": 12.5,
            "risk_level": "low",
            "risk_penalty": 1.5,
            "risk_flags": [
              "rsi_overbought"
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
                "code": "600521",
                "name": "华海药业",
                "source": "tencent",
                "fetched_at": "2026-10-09T16:24:16.694580+00:00",
                "price": 17.45,
                "change_pct": 4.8,
                "change_amount": 0.8,
                "volume": 72199500,
                "amount": 1238170946.0,
                "volume_ratio": 2.52,
                "turnover_rate": 4.82,
                "amplitude": 5.29,
                "open_price": 16.77,
                "high": 17.46,
                "low": 16.58,
                "pre_close": 16.65,
                "pe_ratio": 41.62,
                "pb_ratio": 2.74,
                "total_mv": 26127000000.0,
                "circ_mv": 26127000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 17.45, 涨跌幅 4.8%",
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
      },
      "capital_heat": {
        "rank": 7,
        "score": 72.3894,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 7,
          "code": "600521",
          "name": "华海药业",
          "score": 72.3894,
          "screen_score": 69.98938756756758,
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
          "price": 17.45,
          "change_pct": 4.8,
          "amount": 1238170946.0,
          "industry": "",
          "factor_scores": {
            "value": 54.9542,
            "liquidity": 77.2973,
            "momentum": 72.1,
            "reversal": 5.0,
            "activity": 82.1065,
            "stability": 63.6,
            "size": 76.2162,
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
            "code": "600521",
            "name": "华海药业",
            "final_score": 72.3894,
            "screen_score": 69.98938756756758,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 17.45,
            "change_pct": 4.8,
            "amount": 1238170946.0,
            "total_mv": 26127077135.0,
            "turnover_rate": 4.82,
            "volume_ratio": 2.52,
            "pe_ratio": 41.6154219,
            "pb_ratio": 2.73913113,
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
              "value": 54.9542,
              "liquidity": 77.2973,
              "momentum": 72.1,
              "reversal": 5.0,
              "activity": 82.1065,
              "stability": 63.6,
              "size": 76.2162,
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
    "code": "600150",
    "name": "中国船舶",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 1,
    "best_score": 91.6044,
    "average_score": 91.6044,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 1,
        "score": 91.6044,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 1,
          "code": "600150",
          "name": "中国船舶",
          "score": 91.6044,
          "screen_score": 87.20438405844155,
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
          "price": 38.54,
          "change_pct": -3.19,
          "amount": 4087925871.0,
          "industry": "",
          "factor_scores": {
            "value": 78.6263,
            "liquidity": 98.7013,
            "momentum": 46.1325,
            "reversal": 95.97,
            "activity": 79.7324,
            "stability": 68.43,
            "size": 98.961,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "600150",
              "name": "中国船舶",
              "source": "tencent",
              "fetched_at": "2026-10-09T16:26:25.921675+00:00",
              "price": 38.54,
              "change_pct": -3.19,
              "change_amount": -1.27,
              "volume": 105602400,
              "amount": 4087925871.0,
              "volume_ratio": 1.13,
              "turnover_rate": 1.4,
              "amplitude": 5.75,
              "open_price": 39.99,
              "high": 40.47,
              "low": 38.18,
              "pre_close": 39.81,
              "pe_ratio": 20.68,
              "pb_ratio": 1.9,
              "total_mv": 290037000000.0,
              "circ_mv": 290037000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 38.54, 涨跌幅 -3.19%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 1,
            "code": "600150",
            "name": "中国船舶",
            "final_score": 91.6044,
            "screen_score": 87.20438405844155,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 38.54,
            "change_pct": -3.19,
            "amount": 4087925871.0,
            "total_mv": 290037444440.0,
            "turnover_rate": 1.4,
            "volume_ratio": 1.13,
            "pe_ratio": 20.680584,
            "pb_ratio": 1.90350436,
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
              "value": 78.6263,
              "liquidity": 98.7013,
              "momentum": 46.1325,
              "reversal": 95.97,
              "activity": 79.7324,
              "stability": 68.43,
              "size": 98.961,
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
                "code": "600150",
                "name": "中国船舶",
                "source": "tencent",
                "fetched_at": "2026-10-09T16:26:25.921675+00:00",
                "price": 38.54,
                "change_pct": -3.19,
                "change_amount": -1.27,
                "volume": 105602400,
                "amount": 4087925871.0,
                "volume_ratio": 1.13,
                "turnover_rate": 1.4,
                "amplitude": 5.75,
                "open_price": 39.99,
                "high": 40.47,
                "low": 38.18,
                "pre_close": 39.81,
                "pe_ratio": 20.68,
                "pb_ratio": 1.9,
                "total_mv": 290037000000.0,
                "circ_mv": 290037000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 38.54, 涨跌幅 -3.19%",
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
    "code": "002074",
    "name": "国轩高科",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 2,
    "best_score": 90.0841,
    "average_score": 90.0841,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 2,
        "score": 90.0841,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 2,
          "code": "002074",
          "name": "国轩高科",
          "score": 90.0841,
          "screen_score": 85.6840674025974,
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
          "price": 30.41,
          "change_pct": -2.84,
          "amount": 3451359095.78,
          "industry": "",
          "factor_scores": {
            "value": 81.3945,
            "liquidity": 98.4416,
            "momentum": 47.27,
            "reversal": 91.42,
            "activity": 74.6245,
            "stability": 69.48,
            "size": 92.7273,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "002074",
              "name": "国轩高科",
              "source": "tencent",
              "fetched_at": "2026-10-09T16:26:36.259295+00:00",
              "price": 30.41,
              "change_pct": -2.84,
              "change_amount": -0.89,
              "volume": 112261300,
              "amount": 3451359096.0,
              "volume_ratio": 1.72,
              "turnover_rate": 6.46,
              "amplitude": 6.87,
              "open_price": 30.36,
              "high": 32.0,
              "low": 29.85,
              "pre_close": 31.3,
              "pe_ratio": 16.22,
              "pb_ratio": 1.84,
              "total_mv": 55186000000.0,
              "circ_mv": 52812000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 30.41, 涨跌幅 -2.84%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 2,
            "code": "002074",
            "name": "国轩高科",
            "final_score": 90.0841,
            "screen_score": 85.6840674025974,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 30.41,
            "change_pct": -2.84,
            "amount": 3451359095.78,
            "total_mv": 55185797650.0,
            "turnover_rate": 6.46,
            "volume_ratio": 1.72,
            "pe_ratio": 16.21827653,
            "pb_ratio": 1.83139517,
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
              "value": 81.3945,
              "liquidity": 98.4416,
              "momentum": 47.27,
              "reversal": 91.42,
              "activity": 74.6245,
              "stability": 69.48,
              "size": 92.7273,
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
                "code": "002074",
                "name": "国轩高科",
                "source": "tencent",
                "fetched_at": "2026-10-09T16:26:36.259295+00:00",
                "price": 30.41,
                "change_pct": -2.84,
                "change_amount": -0.89,
                "volume": 112261300,
                "amount": 3451359096.0,
                "volume_ratio": 1.72,
                "turnover_rate": 6.46,
                "amplitude": 6.87,
                "open_price": 30.36,
                "high": 32.0,
                "low": 29.85,
                "pre_close": 31.3,
                "pe_ratio": 16.22,
                "pb_ratio": 1.84,
                "total_mv": 55186000000.0,
                "circ_mv": 52812000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 30.41, 涨跌幅 -2.84%",
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
    "code": "601975",
    "name": "招商南油",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 3,
    "best_score": 89.7194,
    "average_score": 89.7194,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 3,
        "score": 89.7194,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 3,
          "code": "601975",
          "name": "招商南油",
          "score": 89.7194,
          "screen_score": 85.31938675324676,
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
          "price": 4.78,
          "change_pct": -3.82,
          "amount": 2059249564.0,
          "industry": "",
          "factor_scores": {
            "value": 81.9036,
            "liquidity": 94.026,
            "momentum": 44.085,
            "reversal": 95.84,
            "activity": 60.769,
            "stability": 66.54,
            "size": 82.0779,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "601975",
              "name": "招商南油",
              "source": "tencent",
              "fetched_at": "2026-10-09T16:26:46.664819+00:00",
              "price": 4.78,
              "change_pct": -3.82,
              "change_amount": -0.19,
              "volume": 432855400,
              "amount": 2059249564.0,
              "volume_ratio": 2.56,
              "turnover_rate": 9.25,
              "amplitude": 10.87,
              "open_price": 4.98,
              "high": 5.08,
              "low": 4.54,
              "pre_close": 4.97,
              "pe_ratio": 14.4,
              "pb_ratio": 1.84,
              "total_mv": 22372000000.0,
              "circ_mv": 22372000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 4.78, 涨跌幅 -3.82%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 3,
            "code": "601975",
            "name": "招商南油",
            "final_score": 89.7194,
            "screen_score": 85.31938675324676,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 4.78,
            "change_pct": -3.82,
            "amount": 2059249564.0,
            "total_mv": 22372047561.0,
            "turnover_rate": 9.25,
            "volume_ratio": 2.56,
            "pe_ratio": 14.4026074,
            "pb_ratio": 1.835117,
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
              "value": 81.9036,
              "liquidity": 94.026,
              "momentum": 44.085,
              "reversal": 95.84,
              "activity": 60.769,
              "stability": 66.54,
              "size": 82.0779,
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
                "code": "601975",
                "name": "招商南油",
                "source": "tencent",
                "fetched_at": "2026-10-09T16:26:46.664819+00:00",
                "price": 4.78,
                "change_pct": -3.82,
                "change_amount": -0.19,
                "volume": 432855400,
                "amount": 2059249564.0,
                "volume_ratio": 2.56,
                "turnover_rate": 9.25,
                "amplitude": 10.87,
                "open_price": 4.98,
                "high": 5.08,
                "low": 4.54,
                "pre_close": 4.97,
                "pe_ratio": 14.4,
                "pb_ratio": 1.84,
                "total_mv": 22372000000.0,
                "circ_mv": 22372000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 4.78, 涨跌幅 -3.82%",
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
    "code": "300456",
    "name": "赛微电子",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 4,
    "best_score": 89.5463,
    "average_score": 89.5463,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 4,
        "score": 89.5463,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 4,
          "code": "300456",
          "name": "赛微电子",
          "score": 89.5463,
          "screen_score": 85.14634412337664,
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
          "price": 31.88,
          "change_pct": -3.57,
          "amount": 934646385.72,
          "industry": "",
          "factor_scores": {
            "value": 75.9536,
            "liquidity": 84.4156,
            "momentum": 44.8975,
            "reversal": 99.09,
            "activity": 78.4161,
            "stability": 67.29,
            "size": 82.3377,
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
            "code": "300456",
            "name": "赛微电子",
            "final_score": 89.5463,
            "screen_score": 85.14634412337664,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 31.88,
            "change_pct": -3.57,
            "amount": 934646385.72,
            "total_mv": 23342954712.0,
            "turnover_rate": 4.89,
            "volume_ratio": 1.07,
            "pe_ratio": 5.58936189,
            "pb_ratio": 2.5822242,
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
              "value": 75.9536,
              "liquidity": 84.4156,
              "momentum": 44.8975,
              "reversal": 99.09,
              "activity": 78.4161,
              "stability": 67.29,
              "size": 82.3377,
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
    "code": "002273",
    "name": "水晶光电",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 5,
    "best_score": 85.6391,
    "average_score": 85.6391,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 5,
        "score": 85.6391,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 5,
          "code": "002273",
          "name": "水晶光电",
          "score": 85.6391,
          "screen_score": 83.63908185064936,
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
          "price": 22.37,
          "change_pct": -3.37,
          "amount": 1289088416.88,
          "industry": "",
          "factor_scores": {
            "value": 61.1471,
            "liquidity": 89.3506,
            "momentum": 45.5475,
            "reversal": 98.31,
            "activity": 81.1739,
            "stability": 67.89,
            "size": 86.7532,
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
            "rank": 5,
            "code": "002273",
            "name": "水晶光电",
            "final_score": 85.6391,
            "screen_score": 83.63908185064936,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 22.37,
            "change_pct": -3.37,
            "amount": 1289088416.88,
            "total_mv": 31108442784.0,
            "turnover_rate": 4.25,
            "volume_ratio": 1.17,
            "pe_ratio": 26.0085497,
            "pb_ratio": 3.04793772,
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
              "value": 61.1471,
              "liquidity": 89.3506,
              "momentum": 45.5475,
              "reversal": 98.31,
              "activity": 81.1739,
              "stability": 67.89,
              "size": 86.7532,
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
    "code": "601609",
    "name": "金田股份",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 6,
    "best_score": 85.6176,
    "average_score": 85.6176,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 6,
        "score": 85.6176,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 6,
          "code": "601609",
          "name": "金田股份",
          "score": 85.6176,
          "screen_score": 81.21756438311688,
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
          "price": 10.78,
          "change_pct": -2.97,
          "amount": 474657602.0,
          "industry": "",
          "factor_scores": {
            "value": 77.914,
            "liquidity": 70.6494,
            "momentum": 46.8475,
            "reversal": 93.11,
            "activity": 82.8741,
            "stability": 69.09,
            "size": 77.1429,
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
            "code": "601609",
            "name": "金田股份",
            "final_score": 85.6176,
            "screen_score": 81.21756438311688,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 10.78,
            "change_pct": -2.97,
            "amount": 474657602.0,
            "total_mv": 18634719721.0,
            "turnover_rate": 2.55,
            "volume_ratio": 0.91,
            "pe_ratio": 22.68873291,
            "pb_ratio": 1.8270895,
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
              "value": 77.914,
              "liquidity": 70.6494,
              "momentum": 46.8475,
              "reversal": 93.11,
              "activity": 82.8741,
              "stability": 69.09,
              "size": 77.1429,
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
    "code": "002008",
    "name": "大族激光",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 7,
    "best_score": 84.6968,
    "average_score": 84.6968,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 7,
        "score": 84.6968,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 7,
          "code": "002008",
          "name": "大族激光",
          "score": 84.6968,
          "screen_score": 82.69677451298702,
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
          "price": 75.5,
          "change_pct": -3.34,
          "amount": 3016487600.44,
          "industry": "",
          "factor_scores": {
            "value": 46.736,
            "liquidity": 97.6623,
            "momentum": 45.645,
            "reversal": 97.92,
            "activity": 81.2631,
            "stability": 67.98,
            "size": 94.8052,
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
            "code": "002008",
            "name": "大族激光",
            "final_score": 84.6968,
            "screen_score": 82.69677451298702,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 75.5,
            "change_pct": -3.34,
            "amount": 3016487600.44,
            "total_mv": 77735057304.0,
            "turnover_rate": 4.2,
            "volume_ratio": 1.15,
            "pe_ratio": 39.07271385,
            "pb_ratio": 3.6220913,
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
              "value": 46.736,
              "liquidity": 97.6623,
              "momentum": 45.645,
              "reversal": 97.92,
              "activity": 81.2631,
              "stability": 67.98,
              "size": 94.8052,
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
    "code": "603606",
    "name": "东方电缆",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 8,
    "best_score": 84.6839,
    "average_score": 84.6839,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 8,
        "score": 84.6839,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 8,
          "code": "603606",
          "name": "东方电缆",
          "score": 84.6839,
          "screen_score": 82.6839002922078,
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
          "price": 36.3,
          "change_pct": -3.3,
          "amount": 1017885404.0,
          "industry": "",
          "factor_scores": {
            "value": 59.6977,
            "liquidity": 85.7143,
            "momentum": 45.775,
            "reversal": 97.4,
            "activity": 85.3949,
            "stability": 68.1,
            "size": 86.2338,
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
            "code": "603606",
            "name": "东方电缆",
            "final_score": 84.6839,
            "screen_score": 82.6839002922078,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 36.3,
            "change_pct": -3.3,
            "amount": 1017885404.0,
            "total_mv": 29940548114.0,
            "turnover_rate": 3.38,
            "volume_ratio": 1.79,
            "pe_ratio": 21.96291674,
            "pb_ratio": 3.54052726,
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
              "value": 59.6977,
              "liquidity": 85.7143,
              "momentum": 45.775,
              "reversal": 97.4,
              "activity": 85.3949,
              "stability": 68.1,
              "size": 86.2338,
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
    "code": "300207",
    "name": "欣旺达",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 9,
    "best_score": 84.6554,
    "average_score": 84.6554,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 9,
        "score": 84.6554,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 9,
          "code": "300207",
          "name": "欣旺达",
          "score": 84.6554,
          "screen_score": 82.65543211038961,
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
          "price": 20.66,
          "change_pct": -3.91,
          "amount": 3313374715.58,
          "industry": "",
          "factor_scores": {
            "value": 63.3276,
            "liquidity": 97.9221,
            "momentum": 43.7925,
            "reversal": 94.67,
            "activity": 62.9174,
            "stability": 66.27,
            "size": 89.3506,
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
            "code": "300207",
            "name": "欣旺达",
            "final_score": 84.6554,
            "screen_score": 82.65543211038961,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 20.66,
            "change_pct": -3.91,
            "amount": 3313374715.58,
            "total_mv": 38168574134.0,
            "turnover_rate": 9.17,
            "volume_ratio": 1.05,
            "pe_ratio": 47.47346017,
            "pb_ratio": 1.5796139,
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
              "value": 63.3276,
              "liquidity": 97.9221,
              "momentum": 43.7925,
              "reversal": 94.67,
              "activity": 62.9174,
              "stability": 66.27,
              "size": 89.3506,
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
    "code": "603063",
    "name": "禾望电气",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 10,
    "best_score": 84.0582,
    "average_score": 84.0582,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 10,
        "score": 84.0582,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 10,
          "code": "603063",
          "name": "禾望电气",
          "score": 84.0582,
          "screen_score": 82.05816762987014,
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
          "price": 25.76,
          "change_pct": -3.38,
          "amount": 475131710.0,
          "industry": "",
          "factor_scores": {
            "value": 70.714,
            "liquidity": 70.9091,
            "momentum": 45.515,
            "reversal": 98.44,
            "activity": 83.8716,
            "stability": 67.86,
            "size": 62.5974,
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
            "code": "603063",
            "name": "禾望电气",
            "final_score": 84.0582,
            "screen_score": 82.05816762987014,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 25.76,
            "change_pct": -3.38,
            "amount": 475131710.0,
            "total_mv": 11973643004.0,
            "turnover_rate": 4.03,
            "volume_ratio": 1.61,
            "pe_ratio": 26.92399022,
            "pb_ratio": 2.19306519,
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
              "value": 70.714,
              "liquidity": 70.9091,
              "momentum": 45.515,
              "reversal": 98.44,
              "activity": 83.8716,
              "stability": 67.86,
              "size": 62.5974,
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
    "code": "300457",
    "name": "赢合科技",
    "resonance_count": 1,
    "strategies": [
      "volume_breakout"
    ],
    "strategy_labels": [
      "放量突破"
    ],
    "best_rank": 1,
    "best_score": 79.4588,
    "average_score": 79.4588,
    "strategy_details": {
      "volume_breakout": {
        "rank": 1,
        "score": 79.4588,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 1,
          "code": "300457",
          "name": "赢合科技",
          "score": 79.4588,
          "screen_score": 77.25875206063158,
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
          "price": 22.72,
          "change_pct": 3.74,
          "amount": 736947392.18,
          "industry": "",
          "factor_scores": {
            "value": 72.2241,
            "liquidity": 78.9474,
            "momentum": 80.9919,
            "reversal": 5.0,
            "activity": 81.445,
            "stability": 71.6832,
            "size": 73.6842,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "300457",
              "name": "赢合科技",
              "source": "tencent",
              "fetched_at": "2026-10-09T16:24:28.586450+00:00",
              "price": 22.72,
              "change_pct": 3.74,
              "change_amount": 0.82,
              "volume": 32781000,
              "amount": 736947392.0,
              "volume_ratio": 2.36,
              "turnover_rate": 5.09,
              "amplitude": 6.62,
              "open_price": 21.78,
              "high": 23.2,
              "low": 21.75,
              "pre_close": 21.9,
              "pe_ratio": 23.72,
              "pb_ratio": 2.06,
              "total_mv": 14656000000.0,
              "circ_mv": 14624000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 22.72, 涨跌幅 3.74%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 1,
            "code": "300457",
            "name": "赢合科技",
            "final_score": 79.4588,
            "screen_score": 77.25875206063158,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 22.72,
            "change_pct": 3.74,
            "amount": 736947392.18,
            "total_mv": 14655919241.0,
            "turnover_rate": 5.09,
            "volume_ratio": 2.36,
            "pe_ratio": 23.72059354,
            "pb_ratio": 2.05917777,
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
            "change_60d": 13.8847,
            "signal_score": 90.8596,
            "ma_bullish": true,
            "price_above_ma20": true,
            "macd_status": "bullish",
            "rsi_status": "neutral",
            "breakout_20d_pct": 1.3833,
            "range_20d_pct": 17.0535,
            "volume_ratio_20d": 3.0118,
            "body_pct": 4.3159,
            "pullback_to_ma20_pct": 7.1976,
            "consolidation_days_20d": 12,
            "volatility_20d_pct": 40.4485,
            "max_drawdown_20d_pct": -8.5701,
            "atr_20_pct": 3.4837,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:AkshareFetcher",
            "factor_scores": {
              "value": 72.2241,
              "liquidity": 78.9474,
              "momentum": 80.9919,
              "reversal": 5.0,
              "activity": 81.445,
              "stability": 71.6832,
              "size": 73.6842,
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
                "code": "300457",
                "name": "赢合科技",
                "source": "tencent",
                "fetched_at": "2026-10-09T16:24:28.586450+00:00",
                "price": 22.72,
                "change_pct": 3.74,
                "change_amount": 0.82,
                "volume": 32781000,
                "amount": 736947392.0,
                "volume_ratio": 2.36,
                "turnover_rate": 5.09,
                "amplitude": 6.62,
                "open_price": 21.78,
                "high": 23.2,
                "low": 21.75,
                "pre_close": 21.9,
                "pe_ratio": 23.72,
                "pb_ratio": 2.06,
                "total_mv": 14656000000.0,
                "circ_mv": 14624000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 22.72, 涨跌幅 3.74%",
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
    "code": "600988",
    "name": "赤峰黄金",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 1,
    "best_score": 75.3049,
    "average_score": 75.3049,
    "strategy_details": {
      "capital_heat": {
        "rank": 1,
        "score": 75.3049,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 1,
          "code": "600988",
          "name": "赤峰黄金",
          "score": 75.3049,
          "screen_score": 72.90492756756758,
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
          "price": 41.38,
          "change_pct": 5.91,
          "amount": 3097807476.0,
          "industry": "",
          "factor_scores": {
            "value": 50.0485,
            "liquidity": 97.2973,
            "momentum": 75.7075,
            "reversal": 5.0,
            "activity": 78.157,
            "stability": 60.27,
            "size": 96.7568,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "600988",
              "name": "赤峰黄金",
              "source": "tencent",
              "fetched_at": "2026-10-09T16:24:59.298127+00:00",
              "price": 41.38,
              "change_pct": 5.91,
              "change_amount": 2.31,
              "volume": 76223100,
              "amount": 3097807476.0,
              "volume_ratio": 1.84,
              "turnover_rate": 4.58,
              "amplitude": 6.4,
              "open_price": 39.68,
              "high": 42.0,
              "low": 39.5,
              "pre_close": 39.07,
              "pe_ratio": 21.21,
              "pb_ratio": 5.49,
              "total_mv": 78639000000.0,
              "circ_mv": 68853000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 41.38, 涨跌幅 5.91%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 1,
            "code": "600988",
            "name": "赤峰黄金",
            "final_score": 75.3049,
            "screen_score": 72.90492756756758,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 41.38,
            "change_pct": 5.91,
            "amount": 3097807476.0,
            "total_mv": 78639014546.0,
            "turnover_rate": 4.58,
            "volume_ratio": 1.84,
            "pe_ratio": 21.20931373,
            "pb_ratio": 5.48930063,
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
              "value": 50.0485,
              "liquidity": 97.2973,
              "momentum": 75.7075,
              "reversal": 5.0,
              "activity": 78.157,
              "stability": 60.27,
              "size": 96.7568,
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
                "code": "600988",
                "name": "赤峰黄金",
                "source": "tencent",
                "fetched_at": "2026-10-09T16:24:59.298127+00:00",
                "price": 41.38,
                "change_pct": 5.91,
                "change_amount": 2.31,
                "volume": 76223100,
                "amount": 3097807476.0,
                "volume_ratio": 1.84,
                "turnover_rate": 4.58,
                "amplitude": 6.4,
                "open_price": 39.68,
                "high": 42.0,
                "low": 39.5,
                "pre_close": 39.07,
                "pe_ratio": 21.21,
                "pb_ratio": 5.49,
                "total_mv": 78639000000.0,
                "circ_mv": 68853000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 41.38, 涨跌幅 5.91%",
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
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 2,
    "best_score": 74.8361,
    "average_score": 74.8361,
    "strategy_details": {
      "capital_heat": {
        "rank": 2,
        "score": 74.8361,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 2,
          "code": "600256",
          "name": "广汇能源",
          "score": 74.8361,
          "screen_score": 72.43607324324326,
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
          "price": 7.2,
          "change_pct": 5.88,
          "amount": 2000957759.0,
          "industry": "",
          "factor_scores": {
            "value": 73.7706,
            "liquidity": 90.2703,
            "momentum": 75.61,
            "reversal": 5.0,
            "activity": 80.5773,
            "stability": 60.36,
            "size": 89.1892,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "600256",
              "name": "广汇能源",
              "source": "tencent",
              "fetched_at": "2026-10-09T16:25:12.304435+00:00",
              "price": 7.2,
              "change_pct": 5.88,
              "change_amount": 0.4,
              "volume": 279227900,
              "amount": 2000957759.0,
              "volume_ratio": 2.54,
              "turnover_rate": 4.37,
              "amplitude": 5.0,
              "open_price": 7.06,
              "high": 7.33,
              "low": 6.99,
              "pre_close": 6.8,
              "pe_ratio": 26.0,
              "pb_ratio": 1.84,
              "total_mv": 46022000000.0,
              "circ_mv": 46022000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 7.2, 涨跌幅 5.88%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 2,
            "code": "600256",
            "name": "广汇能源",
            "final_score": 74.8361,
            "screen_score": 72.43607324324326,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 7.2,
            "change_pct": 5.88,
            "amount": 2000957759.0,
            "total_mv": 46022421341.0,
            "turnover_rate": 4.37,
            "volume_ratio": 2.54,
            "pe_ratio": 25.99792262,
            "pb_ratio": 1.84170239,
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
              "value": 73.7706,
              "liquidity": 90.2703,
              "momentum": 75.61,
              "reversal": 5.0,
              "activity": 80.5773,
              "stability": 60.36,
              "size": 89.1892,
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
                "code": "600256",
                "name": "广汇能源",
                "source": "tencent",
                "fetched_at": "2026-10-09T16:25:12.304435+00:00",
                "price": 7.2,
                "change_pct": 5.88,
                "change_amount": 0.4,
                "volume": 279227900,
                "amount": 2000957759.0,
                "volume_ratio": 2.54,
                "turnover_rate": 4.37,
                "amplitude": 5.0,
                "open_price": 7.06,
                "high": 7.33,
                "low": 6.99,
                "pre_close": 6.8,
                "pe_ratio": 26.0,
                "pb_ratio": 1.84,
                "total_mv": 46022000000.0,
                "circ_mv": 46022000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 7.2, 涨跌幅 5.88%",
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
    "best_rank": 1,
    "best_score": 74.7189,
    "average_score": 74.7189,
    "strategy_details": {
      "momentum_quality": {
        "rank": 1,
        "score": 74.7189,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 1,
          "code": "601398",
          "name": "工商银行",
          "score": 74.7189,
          "screen_score": 71.71894810842433,
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
          "price": 8.22,
          "change_pct": -1.08,
          "amount": 2810588785.0,
          "industry": "",
          "factor_scores": {
            "value": 85.7159,
            "liquidity": 94.3838,
            "momentum": 52.99,
            "reversal": 75.04,
            "activity": 67.0832,
            "stability": 74.76,
            "size": 100.0,
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
            "rank": 1,
            "code": "601398",
            "name": "工商银行",
            "final_score": 74.7189,
            "screen_score": 71.71894810842433,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 8.22,
            "change_pct": -1.08,
            "amount": 2810588785.0,
            "total_mv": 2929659433272.0,
            "turnover_rate": 0.13,
            "volume_ratio": 1.14,
            "pe_ratio": 7.8303619,
            "pb_ratio": 0.73937832,
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
              "value": 85.7159,
              "liquidity": 94.3838,
              "momentum": 52.99,
              "reversal": 75.04,
              "activity": 67.0832,
              "stability": 74.76,
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
    "code": "601318",
    "name": "中国平安",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 2,
    "best_score": 74.6381,
    "average_score": 74.6381,
    "strategy_details": {
      "momentum_quality": {
        "rank": 2,
        "score": 74.6381,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 2,
          "code": "601318",
          "name": "中国平安",
          "score": 74.6381,
          "screen_score": 72.83808452613104,
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
          "price": 52.83,
          "change_pct": 0.3,
          "amount": 3153261224.0,
          "industry": "",
          "factor_scores": {
            "value": 84.9339,
            "liquidity": 95.9438,
            "momentum": 57.475,
            "reversal": 57.1,
            "activity": 68.2229,
            "stability": 77.1,
            "size": 98.2839,
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
              "fetched_at": "2026-10-09T16:25:43.140785+00:00",
              "price": 52.83,
              "change_pct": 0.3,
              "change_amount": 0.16,
              "volume": 59593600,
              "amount": 3153261224.0,
              "volume_ratio": 1.05,
              "turnover_rate": 0.56,
              "amplitude": 0.89,
              "open_price": 52.71,
              "high": 53.15,
              "low": 52.68,
              "pre_close": 52.67,
              "pe_ratio": 6.0,
              "pb_ratio": 0.95,
              "total_mv": 956627000000.0,
              "circ_mv": 563171000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 52.83, 涨跌幅 0.3%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality"
          },
          "post_analysis_tags": [
            "value_quality"
          ],
          "raw": {
            "rank": 2,
            "code": "601318",
            "name": "中国平安",
            "final_score": 74.6381,
            "screen_score": 72.83808452613104,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 52.83,
            "change_pct": 0.3,
            "amount": 3153261224.0,
            "total_mv": 956626726596.0,
            "turnover_rate": 0.56,
            "volume_ratio": 1.05,
            "pe_ratio": 6.00458665,
            "pb_ratio": 0.93049471,
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
              "value": 84.9339,
              "liquidity": 95.9438,
              "momentum": 57.475,
              "reversal": 57.1,
              "activity": 68.2229,
              "stability": 77.1,
              "size": 98.2839,
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
                "fetched_at": "2026-10-09T16:25:43.140785+00:00",
                "price": 52.83,
                "change_pct": 0.3,
                "change_amount": 0.16,
                "volume": 59593600,
                "amount": 3153261224.0,
                "volume_ratio": 1.05,
                "turnover_rate": 0.56,
                "amplitude": 0.89,
                "open_price": 52.71,
                "high": 53.15,
                "low": 52.68,
                "pre_close": 52.67,
                "pe_ratio": 6.0,
                "pb_ratio": 0.95,
                "total_mv": 956627000000.0,
                "circ_mv": 563171000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 52.83, 涨跌幅 0.3%",
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
    "best_rank": 3,
    "best_score": 74.5315,
    "average_score": 74.5315,
    "strategy_details": {
      "momentum_quality": {
        "rank": 3,
        "score": 74.5315,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 3,
          "code": "600036",
          "name": "招商银行",
          "score": 74.5315,
          "screen_score": 72.73152960218408,
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
          "price": 41.42,
          "change_pct": -0.7,
          "amount": 3607539112.0,
          "industry": "",
          "factor_scores": {
            "value": 84.6156,
            "liquidity": 97.1919,
            "momentum": 54.225,
            "reversal": 70.1,
            "activity": 69.8515,
            "stability": 75.9,
            "size": 98.5959,
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
              "fetched_at": "2026-10-09T16:25:55.962786+00:00",
              "price": 41.42,
              "change_pct": -0.7,
              "change_amount": -0.29,
              "volume": 86192400,
              "amount": 3607539112.0,
              "volume_ratio": 1.52,
              "turnover_rate": 0.42,
              "amplitude": 1.61,
              "open_price": 41.72,
              "high": 42.09,
              "low": 41.42,
              "pre_close": 41.71,
              "pe_ratio": 6.89,
              "pb_ratio": 0.91,
              "total_mv": 1044606000000.0,
              "circ_mv": 854451000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 41.42, 涨跌幅 -0.7%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality"
          },
          "post_analysis_tags": [
            "value_quality"
          ],
          "raw": {
            "rank": 3,
            "code": "600036",
            "name": "招商银行",
            "final_score": 74.5315,
            "screen_score": 72.73152960218408,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 41.42,
            "change_pct": -0.7,
            "amount": 3607539112.0,
            "total_mv": 1044606004793.0,
            "turnover_rate": 0.42,
            "volume_ratio": 1.52,
            "pe_ratio": 6.88618029,
            "pb_ratio": 0.9122846,
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
              "value": 84.6156,
              "liquidity": 97.1919,
              "momentum": 54.225,
              "reversal": 70.1,
              "activity": 69.8515,
              "stability": 75.9,
              "size": 98.5959,
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
                "fetched_at": "2026-10-09T16:25:55.962786+00:00",
                "price": 41.42,
                "change_pct": -0.7,
                "change_amount": -0.29,
                "volume": 86192400,
                "amount": 3607539112.0,
                "volume_ratio": 1.52,
                "turnover_rate": 0.42,
                "amplitude": 1.61,
                "open_price": 41.72,
                "high": 42.09,
                "low": 41.42,
                "pre_close": 41.71,
                "pe_ratio": 6.89,
                "pb_ratio": 0.91,
                "total_mv": 1044606000000.0,
                "circ_mv": 854451000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 41.42, 涨跌幅 -0.7%",
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
    "best_rank": 4,
    "best_score": 74.3862,
    "average_score": 74.3862,
    "strategy_details": {
      "momentum_quality": {
        "rank": 4,
        "score": 74.3862,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 4,
          "code": "601328",
          "name": "交通银行",
          "score": 74.3862,
          "screen_score": 72.58618308307332,
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
          "price": 7.78,
          "change_pct": -0.64,
          "amount": 2231787607.0,
          "industry": "",
          "factor_scores": {
            "value": 87.1862,
            "liquidity": 92.1997,
            "momentum": 54.42,
            "reversal": 69.32,
            "activity": 72.1274,
            "stability": 76.08,
            "size": 97.6599,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "601328",
              "name": "交通银行",
              "source": "tencent",
              "fetched_at": "2026-10-09T16:26:04.686802+00:00",
              "price": 7.78,
              "change_pct": -0.64,
              "change_amount": -0.05,
              "volume": 283824800,
              "amount": 2231787607.0,
              "volume_ratio": 1.49,
              "turnover_rate": 1.09,
              "amplitude": 1.92,
              "open_price": 7.84,
              "high": 7.92,
              "low": 7.77,
              "pre_close": 7.83,
              "pe_ratio": 7.05,
              "pb_ratio": 0.59,
              "total_mv": 687470000000.0,
              "circ_mv": 202844000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 7.78, 涨跌幅 -0.64%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality"
          },
          "post_analysis_tags": [
            "value_quality"
          ],
          "raw": {
            "rank": 4,
            "code": "601328",
            "name": "交通银行",
            "final_score": 74.3862,
            "screen_score": 72.58618308307332,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 7.78,
            "change_pct": -0.64,
            "amount": 2231787607.0,
            "total_mv": 687470241255.0,
            "turnover_rate": 1.09,
            "volume_ratio": 1.49,
            "pe_ratio": 7.05242348,
            "pb_ratio": 0.58866817,
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
              "value": 87.1862,
              "liquidity": 92.1997,
              "momentum": 54.42,
              "reversal": 69.32,
              "activity": 72.1274,
              "stability": 76.08,
              "size": 97.6599,
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
                "code": "601328",
                "name": "交通银行",
                "source": "tencent",
                "fetched_at": "2026-10-09T16:26:04.686802+00:00",
                "price": 7.78,
                "change_pct": -0.64,
                "change_amount": -0.05,
                "volume": 283824800,
                "amount": 2231787607.0,
                "volume_ratio": 1.49,
                "turnover_rate": 1.09,
                "amplitude": 1.92,
                "open_price": 7.84,
                "high": 7.92,
                "low": 7.77,
                "pre_close": 7.83,
                "pe_ratio": 7.05,
                "pb_ratio": 0.59,
                "total_mv": 687470000000.0,
                "circ_mv": 202844000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 7.78, 涨跌幅 -0.64%",
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
    "code": "300418",
    "name": "昆仑万维",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 3,
    "best_score": 74.2168,
    "average_score": 74.2168,
    "strategy_details": {
      "capital_heat": {
        "rank": 3,
        "score": 74.2168,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 3,
          "code": "300418",
          "name": "昆仑万维",
          "score": 74.2168,
          "screen_score": 71.81684567567568,
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
          "price": 41.15,
          "change_pct": 7.27,
          "amount": 2338896921.86,
          "industry": "",
          "factor_scores": {
            "value": 36.3576,
            "liquidity": 92.973,
            "momentum": 74.1215,
            "reversal": 5.0,
            "activity": 80.0118,
            "stability": 56.19,
            "size": 92.4324,
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
            "code": "300418",
            "name": "昆仑万维",
            "final_score": 74.2168,
            "screen_score": 71.81684567567568,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 41.15,
            "change_pct": 7.27,
            "amount": 2338896921.86,
            "total_mv": 52879178522.0,
            "turnover_rate": 5.07,
            "volume_ratio": 1.86,
            "pe_ratio": 150.72858998,
            "pb_ratio": 3.57269128,
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
              "value": 36.3576,
              "liquidity": 92.973,
              "momentum": 74.1215,
              "reversal": 5.0,
              "activity": 80.0118,
              "stability": 56.19,
              "size": 92.4324,
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
    "code": "601939",
    "name": "建设银行",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 5,
    "best_score": 73.6338,
    "average_score": 73.6338,
    "strategy_details": {
      "momentum_quality": {
        "rank": 5,
        "score": 73.6338,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 5,
          "code": "601939",
          "name": "建设银行",
          "score": 73.6338,
          "screen_score": 70.63383638845552,
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
          "price": 10.98,
          "change_pct": -1.52,
          "amount": 1405255982.0,
          "industry": "",
          "factor_scores": {
            "value": 84.5821,
            "liquidity": 87.0515,
            "momentum": 51.56,
            "reversal": 80.76,
            "activity": 72.0025,
            "stability": 73.44,
            "size": 99.844,
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
            "rank": 5,
            "code": "601939",
            "name": "建设银行",
            "final_score": 73.6338,
            "screen_score": 70.63383638845552,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 10.98,
            "change_pct": -1.52,
            "amount": 1405255982.0,
            "total_mv": 2872372188420.0,
            "turnover_rate": 1.32,
            "volume_ratio": 1.28,
            "pe_ratio": 8.29221115,
            "pb_ratio": 0.80229266,
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
              "value": 84.5821,
              "liquidity": 87.0515,
              "momentum": 51.56,
              "reversal": 80.76,
              "activity": 72.0025,
              "stability": 73.44,
              "size": 99.844,
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
    "code": "688099",
    "name": "晶晨股份",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 4,
    "best_score": 73.519,
    "average_score": 73.519,
    "strategy_details": {
      "capital_heat": {
        "rank": 4,
        "score": 73.519,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 4,
          "code": "688099",
          "name": "晶晨股份",
          "score": 73.519,
          "screen_score": 71.11898054054056,
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
          "price": 99.71,
          "change_pct": 5.44,
          "amount": 3913551804.0,
          "industry": "",
          "factor_scores": {
            "value": 40.6095,
            "liquidity": 98.3784,
            "momentum": 74.18,
            "reversal": 5.0,
            "activity": 72.403,
            "stability": 61.68,
            "size": 87.5676,
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
            "code": "688099",
            "name": "晶晨股份",
            "final_score": 73.519,
            "screen_score": 71.11898054054056,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 99.71,
            "change_pct": 5.44,
            "amount": 3913551804.0,
            "total_mv": 42209236701.0,
            "turnover_rate": 9.22,
            "volume_ratio": 3.6,
            "pe_ratio": 42.75626985,
            "pb_ratio": 5.29415235,
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
              "value": 40.6095,
              "liquidity": 98.3784,
              "momentum": 74.18,
              "reversal": 5.0,
              "activity": 72.403,
              "stability": 61.68,
              "size": 87.5676,
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
    "best_rank": 6,
    "best_score": 73.4069,
    "average_score": 73.4069,
    "strategy_details": {
      "momentum_quality": {
        "rank": 6,
        "score": 73.4069,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 6,
          "code": "601288",
          "name": "农业银行",
          "score": 73.4069,
          "screen_score": 71.60689321372855,
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
          "price": 6.98,
          "change_pct": -0.57,
          "amount": 2406076600.0,
          "industry": "",
          "factor_scores": {
            "value": 84.3138,
            "liquidity": 92.8237,
            "momentum": 54.6475,
            "reversal": 68.41,
            "activity": 67.102,
            "stability": 76.29,
            "size": 99.688,
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
            "code": "601288",
            "name": "农业银行",
            "final_score": 73.4069,
            "screen_score": 71.60689321372855,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 6.98,
            "change_pct": -0.57,
            "amount": 2406076600.0,
            "total_mv": 2442881576434.0,
            "turnover_rate": 0.11,
            "volume_ratio": 1.16,
            "pe_ratio": 8.20001066,
            "pb_ratio": 0.85474794,
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
              "value": 84.3138,
              "liquidity": 92.8237,
              "momentum": 54.6475,
              "reversal": 68.41,
              "activity": 67.102,
              "stability": 76.29,
              "size": 99.688,
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
    "code": "601166",
    "name": "兴业银行",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 7,
    "best_score": 73.3591,
    "average_score": 73.3591,
    "strategy_details": {
      "momentum_quality": {
        "rank": 7,
        "score": 73.3591,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 7,
          "code": "601166",
          "name": "兴业银行",
          "score": 73.3591,
          "screen_score": 71.55912745709827,
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
          "price": 18.05,
          "change_pct": -1.04,
          "amount": 1665697163.0,
          "industry": "",
          "factor_scores": {
            "value": 89.4085,
            "liquidity": 88.7676,
            "momentum": 53.12,
            "reversal": 74.52,
            "activity": 69.343,
            "stability": 74.88,
            "size": 96.4119,
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
            "code": "601166",
            "name": "兴业银行",
            "final_score": 73.3591,
            "screen_score": 71.55912745709827,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 18.05,
            "change_pct": -1.04,
            "amount": 1665697163.0,
            "total_mv": 381989707203.0,
            "turnover_rate": 0.43,
            "volume_ratio": 1.4,
            "pe_ratio": 5.06221534,
            "pb_ratio": 0.45682822,
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
              "value": 89.4085,
              "liquidity": 88.7676,
              "momentum": 53.12,
              "reversal": 74.52,
              "activity": 69.343,
              "stability": 74.88,
              "size": 96.4119,
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
    "code": "002460",
    "name": "赣锋锂业",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 5,
    "best_score": 73.2374,
    "average_score": 73.2374,
    "strategy_details": {
      "capital_heat": {
        "rank": 5,
        "score": 73.2374,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 5,
          "code": "002460",
          "name": "赣锋锂业",
          "score": 73.2374,
          "screen_score": 70.83735959459459,
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
          "price": 45.47,
          "change_pct": 2.85,
          "amount": 2623862284.35,
          "industry": "",
          "factor_scores": {
            "value": 79.9833,
            "liquidity": 96.2162,
            "momentum": 65.7625,
            "reversal": 9.15,
            "activity": 78.8849,
            "stability": 69.45,
            "size": 97.2973,
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
            "code": "002460",
            "name": "赣锋锂业",
            "final_score": 73.2374,
            "screen_score": 70.83735959459459,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 45.47,
            "change_pct": 2.85,
            "amount": 2623862284.35,
            "total_mv": 95336694550.0,
            "turnover_rate": 4.82,
            "volume_ratio": 1.81,
            "pe_ratio": 14.89313532,
            "pb_ratio": 1.97799237,
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
              "value": 79.9833,
              "liquidity": 96.2162,
              "momentum": 65.7625,
              "reversal": 9.15,
              "activity": 78.8849,
              "stability": 69.45,
              "size": 97.2973,
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
    "best_score": 73.1272,
    "average_score": 73.1272,
    "strategy_details": {
      "momentum_quality": {
        "rank": 8,
        "score": 73.1272,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 8,
          "code": "600030",
          "name": "中信证券",
          "score": 73.1272,
          "screen_score": 71.32720785881436,
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
          "price": 25.91,
          "change_pct": 2.01,
          "amount": 2720888490.0,
          "industry": "",
          "factor_scores": {
            "value": 75.9858,
            "liquidity": 94.2278,
            "momentum": 63.0325,
            "reversal": 26.79,
            "activity": 71.1993,
            "stability": 71.97,
            "size": 96.5679,
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
            "final_score": 73.1272,
            "screen_score": 71.32720785881436,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 25.91,
            "change_pct": 2.01,
            "amount": 2720888490.0,
            "total_mv": 404824893013.0,
            "turnover_rate": 0.87,
            "volume_ratio": 1.46,
            "pe_ratio": 10.20847689,
            "pb_ratio": 1.37008491,
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
              "value": 75.9858,
              "liquidity": 94.2278,
              "momentum": 63.0325,
              "reversal": 26.79,
              "activity": 71.1993,
              "stability": 71.97,
              "size": 96.5679,
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
    "code": "601988",
    "name": "中国银行",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 9,
    "best_score": 73.1033,
    "average_score": 73.1033,
    "strategy_details": {
      "momentum_quality": {
        "rank": 9,
        "score": 73.1033,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 9,
          "code": "601988",
          "name": "中国银行",
          "score": 73.1033,
          "screen_score": 71.30325797581901,
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
          "price": 6.77,
          "change_pct": -0.59,
          "amount": 2032058745.0,
          "industry": "",
          "factor_scores": {
            "value": 84.4581,
            "liquidity": 90.9516,
            "momentum": 54.5825,
            "reversal": 68.67,
            "activity": 67.3008,
            "stability": 76.23,
            "size": 99.532,
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
            "code": "601988",
            "name": "中国银行",
            "final_score": 73.1033,
            "screen_score": 71.30325797581901,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 6.77,
            "change_pct": -0.59,
            "amount": 2032058745.0,
            "total_mv": 2181378027981.0,
            "turnover_rate": 0.14,
            "volume_ratio": 1.18,
            "pe_ratio": 8.75971002,
            "pb_ratio": 0.79302911,
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
              "value": 84.4581,
              "liquidity": 90.9516,
              "momentum": 54.5825,
              "reversal": 68.67,
              "activity": 67.3008,
              "stability": 76.23,
              "size": 99.532,
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
    "code": "603799",
    "name": "华友钴业",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 10,
    "best_score": 72.7023,
    "average_score": 72.7023,
    "strategy_details": {
      "momentum_quality": {
        "rank": 10,
        "score": 72.7023,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 10,
          "code": "603799",
          "name": "华友钴业",
          "score": 72.7023,
          "screen_score": 70.90233067472698,
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
          "price": 35.6,
          "change_pct": 1.05,
          "amount": 1541264163.0,
          "industry": "",
          "factor_scores": {
            "value": 77.0638,
            "liquidity": 88.1435,
            "momentum": 59.9125,
            "reversal": 46.95,
            "activity": 75.8748,
            "stability": 74.85,
            "size": 73.0109,
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
            "code": "603799",
            "name": "华友钴业",
            "final_score": 72.7023,
            "screen_score": 70.90233067472698,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 35.6,
            "change_pct": 1.05,
            "amount": 1541264163.0,
            "total_mv": 67409579605.0,
            "turnover_rate": 2.32,
            "volume_ratio": 1.34,
            "pe_ratio": 9.75981793,
            "pb_ratio": 1.32511424,
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
              "value": 77.0638,
              "liquidity": 88.1435,
              "momentum": 59.9125,
              "reversal": 46.95,
              "activity": 75.8748,
              "stability": 74.85,
              "size": 73.0109,
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
    "code": "301238",
    "name": "瑞泰新材",
    "resonance_count": 1,
    "strategies": [
      "volume_breakout"
    ],
    "strategy_labels": [
      "放量突破"
    ],
    "best_rank": 3,
    "best_score": 72.6329,
    "average_score": 72.6329,
    "strategy_details": {
      "volume_breakout": {
        "rank": 3,
        "score": 72.6329,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 3,
          "code": "301238",
          "name": "瑞泰新材",
          "score": 72.6329,
          "screen_score": 71.93291520378948,
          "reason": "本地后置评分: capital_confirmed",
          "risk_level": "low",
          "risk_flags": [
            "rsi_overbought"
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
          "price": 17.43,
          "change_pct": 5.76,
          "amount": 659699021.28,
          "industry": "",
          "factor_scores": {
            "value": 64.3433,
            "liquidity": 73.6842,
            "momentum": 72.5207,
            "reversal": 5.0,
            "activity": 79.4706,
            "stability": 62.64,
            "size": 63.1579,
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
            "code": "301238",
            "name": "瑞泰新材",
            "final_score": 72.6329,
            "screen_score": 71.93291520378948,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 17.43,
            "change_pct": 5.76,
            "amount": 659699021.28,
            "total_mv": 12781999419.0,
            "turnover_rate": 5.26,
            "volume_ratio": 4.21,
            "pe_ratio": 39.77468661,
            "pb_ratio": 1.75346005,
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
            "change_60d": -1.0783,
            "signal_score": 66.0,
            "ma_bullish": false,
            "price_above_ma20": true,
            "macd_status": "bullish",
            "rsi_status": "overbought",
            "breakout_20d_pct": 4.6218,
            "range_20d_pct": 18.2796,
            "volume_ratio_20d": 5.2993,
            "body_pct": 6.9325,
            "pullback_to_ma20_pct": 10.299,
            "consolidation_days_20d": 20,
            "volatility_20d_pct": 33.7932,
            "max_drawdown_20d_pct": -4.872,
            "atr_20_pct": 2.7367,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:AkshareFetcher",
            "factor_scores": {
              "value": 64.3433,
              "liquidity": 73.6842,
              "momentum": 72.5207,
              "reversal": 5.0,
              "activity": 79.4706,
              "stability": 62.64,
              "size": 63.1579,
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
            "risk_score": 12.5,
            "risk_level": "low",
            "risk_penalty": 1.5,
            "risk_flags": [
              "rsi_overbought"
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
  },
  {
    "code": "002044",
    "name": "美年健康",
    "resonance_count": 1,
    "strategies": [
      "volume_breakout"
    ],
    "strategy_labels": [
      "放量突破"
    ],
    "best_rank": 4,
    "best_score": 72.6161,
    "average_score": 72.6161,
    "strategy_details": {
      "volume_breakout": {
        "rank": 4,
        "score": 72.6161,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 4,
          "code": "002044",
          "name": "美年健康",
          "score": 72.6161,
          "screen_score": 72.6160752303158,
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
          "price": 4.9,
          "change_pct": 8.41,
          "amount": 1234575413.06,
          "industry": "",
          "factor_scores": {
            "value": 43.8239,
            "liquidity": 89.4737,
            "momentum": 68.3421,
            "reversal": 5.0,
            "activity": 77.2098,
            "stability": 54.4367,
            "size": 89.4737,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "002044",
              "name": "美年健康",
              "source": "tencent",
              "fetched_at": "2026-10-09T16:24:39.607378+00:00",
              "price": 4.9,
              "change_pct": 8.41,
              "change_amount": 0.38,
              "volume": 259616700,
              "amount": 1234575413.0,
              "volume_ratio": 4.74,
              "turnover_rate": 6.7,
              "amplitude": 10.18,
              "open_price": 4.52,
              "high": 4.96,
              "low": 4.5,
              "pre_close": 4.52,
              "pe_ratio": 59.14,
              "pb_ratio": 2.41,
              "total_mv": 19180000000.0,
              "circ_mv": 18984000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 4.9, 涨跌幅 8.41%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: 未发现额外加分项"
          },
          "post_analysis_tags": [],
          "raw": {
            "rank": 4,
            "code": "002044",
            "name": "美年健康",
            "final_score": 72.6161,
            "screen_score": 72.6160752303158,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 4.9,
            "change_pct": 8.41,
            "amount": 1234575413.06,
            "total_mv": 19179844223.0,
            "turnover_rate": 6.7,
            "volume_ratio": 4.74,
            "pe_ratio": 59.14203791,
            "pb_ratio": 2.41227133,
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
            "change_60d": 11.1111,
            "signal_score": 63.8889,
            "ma_bullish": false,
            "price_above_ma20": true,
            "macd_status": "neutral",
            "rsi_status": "neutral",
            "breakout_20d_pct": 2.9412,
            "range_20d_pct": 15.3488,
            "volume_ratio_20d": 4.2287,
            "body_pct": 8.4071,
            "pullback_to_ma20_pct": 8.0009,
            "consolidation_days_20d": 20,
            "volatility_20d_pct": 43.2431,
            "max_drawdown_20d_pct": -8.2627,
            "atr_20_pct": 3.0102,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:EfinanceFetcher",
            "factor_scores": {
              "value": 43.8239,
              "liquidity": 89.4737,
              "momentum": 68.3421,
              "reversal": 5.0,
              "activity": 77.2098,
              "stability": 54.4367,
              "size": 89.4737,
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
                "code": "002044",
                "name": "美年健康",
                "source": "tencent",
                "fetched_at": "2026-10-09T16:24:39.607378+00:00",
                "price": 4.9,
                "change_pct": 8.41,
                "change_amount": 0.38,
                "volume": 259616700,
                "amount": 1234575413.0,
                "volume_ratio": 4.74,
                "turnover_rate": 6.7,
                "amplitude": 10.18,
                "open_price": 4.52,
                "high": 4.96,
                "low": 4.5,
                "pre_close": 4.52,
                "pe_ratio": 59.14,
                "pb_ratio": 2.41,
                "total_mv": 19180000000.0,
                "circ_mv": 18984000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 4.9, 涨跌幅 8.41%",
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
    "code": "603236",
    "name": "移远通信",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 6,
    "best_score": 72.4233,
    "average_score": 72.4233,
    "strategy_details": {
      "capital_heat": {
        "rank": 6,
        "score": 72.4233,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 6,
          "code": "603236",
          "name": "移远通信",
          "score": 72.4233,
          "screen_score": 70.02329945945948,
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
          "price": 72.2,
          "change_pct": 5.42,
          "amount": 1329209733.0,
          "industry": "",
          "factor_scores": {
            "value": 50.5198,
            "liquidity": 81.6216,
            "momentum": 74.115,
            "reversal": 5.0,
            "activity": 78.118,
            "stability": 61.74,
            "size": 79.4595,
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
            "code": "603236",
            "name": "移远通信",
            "final_score": 72.4233,
            "screen_score": 70.02329945945948,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 72.2,
            "change_pct": 5.42,
            "amount": 1329209733.0,
            "total_mv": 29339307087.0,
            "turnover_rate": 4.67,
            "volume_ratio": 1.76,
            "pe_ratio": 30.30166368,
            "pb_ratio": 3.98486643,
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
              "value": 50.5198,
              "liquidity": 81.6216,
              "momentum": 74.115,
              "reversal": 5.0,
              "activity": 78.118,
              "stability": 61.74,
              "size": 79.4595,
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
  }
]
```
