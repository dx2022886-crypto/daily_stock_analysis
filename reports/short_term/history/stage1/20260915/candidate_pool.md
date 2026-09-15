# 《A股短线候选池（改造第1阶段）》

> 本报告只做四套原版模型自动合并、去重和模型共振统计；尚未加入题材、涨停梯队、市场情绪、竞价和开盘确认。

## 测试概况

- 阶段：`short_term_candidate_pool_v1`
- 市场：`cn`
- 每套模型返回数量：`10`
- 合并去重后的候选数量：`35`
- 报告输出数量：`30`

## 模型运行状态

| 模型 | 标签 | 状态 | 候选数量 |
| --- | --- | --- | ---: |
| `volume_breakout` | 放量突破 | success | 5 |
| `capital_heat` | 资金热度 | success | 10 |
| `momentum_quality` | 动量质量 | success | 10 |
| `oversold_reversal` | 超跌反转 | success | 10 |

## 候选池优先级

排序依次为：共振模型数量（降序）、多个模型平均原始评分（降序）、最佳模型排名（升序）。这里的排序仅表示候选池优先级，不是买入评分。

| 排名 | 股票代码 | 股票名称 | 共振数 | 入选模型 | 平均原始分 | 最佳名次 |
| ---: | --- | --- | ---: | --- | ---: | ---: |
| 1 | 000425 | 徐工机械 | 1 | 超跌反转 | 90.8641 | 1 |
| 2 | 600362 | 江西铜业 | 1 | 超跌反转 | 88.847 | 2 |
| 3 | 002497 | 雅化集团 | 1 | 超跌反转 | 88.1519 | 3 |
| 4 | 600578 | 京能电力 | 1 | 超跌反转 | 86.1058 | 4 |
| 5 | 300207 | 欣旺达 | 1 | 超跌反转 | 85.8181 | 5 |
| 6 | 002241 | 歌尔股份 | 1 | 超跌反转 | 85.7241 | 6 |
| 7 | 300413 | 芒果超媒 | 1 | 超跌反转 | 84.552 | 7 |
| 8 | 002130 | 沃尔核材 | 1 | 超跌反转 | 84.2644 | 8 |
| 9 | 600596 | 新安股份 | 1 | 超跌反转 | 83.9066 | 9 |
| 10 | 600711 | 盛屯矿业 | 1 | 超跌反转 | 83.3709 | 10 |
| 11 | 603236 | 移远通信 | 1 | 资金热度 | 75.3272 | 1 |
| 12 | 601318 | 中国平安 | 1 | 动量质量 | 74.5732 | 1 |
| 13 | 000657 | 中钨高新 | 1 | 资金热度 | 74.4855 | 2 |
| 14 | 300450 | 先导智能 | 1 | 资金热度 | 74.3243 | 3 |
| 15 | 601398 | 工商银行 | 1 | 动量质量 | 74.1289 | 2 |
| 16 | 600036 | 招商银行 | 1 | 动量质量 | 74.1069 | 3 |
| 17 | 000962 | 东方钽业 | 1 | 资金热度 | 73.8005 | 4 |
| 18 | 601166 | 兴业银行 | 1 | 动量质量 | 73.6688 | 4 |
| 19 | 601288 | 农业银行 | 1 | 动量质量 | 73.6338 | 5 |
| 20 | 002025 | 航天电器 | 1 | 资金热度 | 73.2831 | 5 |
| 21 | 601939 | 建设银行 | 1 | 动量质量 | 73.0733 | 6 |
| 22 | 600919 | 江苏银行 | 1 | 动量质量 | 72.628 | 7 |
| 23 | 603256 | 宏和科技 | 1 | 资金热度 | 72.4348 | 6 |
| 24 | 600030 | 中信证券 | 1 | 动量质量 | 72.188 | 8 |
| 25 | 601988 | 中国银行 | 1 | 动量质量 | 71.9661 | 9 |
| 26 | 002378 | 章源钨业 | 1 | 资金热度 | 71.9336 | 7 |
| 27 | 601169 | 北京银行 | 1 | 动量质量 | 71.7766 | 10 |
| 28 | 600549 | 厦门钨业 | 1 | 资金热度 | 70.4325 | 8 |
| 29 | 603000 | 人民网 | 1 | 资金热度 | 70.0125 | 9 |
| 30 | 002080 | 中材科技 | 1 | 资金热度 | 69.4233 | 10 |

## 模型明细与原始候选字段

完整的每套模型返回结果、每只股票的原始候选字段和策略明细请以同目录的 `candidate_pool.json` 为准。

```json
[
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
    "best_rank": 1,
    "best_score": 90.8641,
    "average_score": 90.8641,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 1,
        "score": 90.8641,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 1,
          "code": "000425",
          "name": "徐工机械",
          "score": 90.8641,
          "screen_score": 86.46407583333333,
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
          "price": 7.81,
          "change_pct": -3.58,
          "amount": 913933450.53,
          "industry": "",
          "factor_scores": {
            "value": 76.3933,
            "liquidity": 90.8889,
            "momentum": 44.865,
            "reversal": 98.96,
            "activity": 80.7524,
            "stability": 67.26,
            "size": 95.7778,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "000425",
              "name": "徐工机械",
              "source": "tencent",
              "fetched_at": "2026-09-15T09:43:23.870207+00:00",
              "price": 7.81,
              "change_pct": -3.58,
              "change_amount": -0.29,
              "volume": 115617200,
              "amount": 913933451.0,
              "volume_ratio": 1.45,
              "turnover_rate": 1.28,
              "amplitude": 4.07,
              "open_price": 8.07,
              "high": 8.11,
              "low": 7.78,
              "pre_close": 8.1,
              "pe_ratio": 14.81,
              "pb_ratio": 1.47,
              "total_mv": 91465000000.0,
              "circ_mv": 70275000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 7.81, 涨跌幅 -3.58%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 1,
            "code": "000425",
            "name": "徐工机械",
            "final_score": 90.8641,
            "screen_score": 86.46407583333333,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 7.81,
            "change_pct": -3.58,
            "amount": 913933450.53,
            "total_mv": 91464553607.0,
            "turnover_rate": 1.28,
            "volume_ratio": 1.45,
            "pe_ratio": 14.81008583,
            "pb_ratio": 1.41679642,
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
              "value": 76.3933,
              "liquidity": 90.8889,
              "momentum": 44.865,
              "reversal": 98.96,
              "activity": 80.7524,
              "stability": 67.26,
              "size": 95.7778,
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
                "code": "000425",
                "name": "徐工机械",
                "source": "tencent",
                "fetched_at": "2026-09-15T09:43:23.870207+00:00",
                "price": 7.81,
                "change_pct": -3.58,
                "change_amount": -0.29,
                "volume": 115617200,
                "amount": 913933451.0,
                "volume_ratio": 1.45,
                "turnover_rate": 1.28,
                "amplitude": 4.07,
                "open_price": 8.07,
                "high": 8.11,
                "low": 7.78,
                "pre_close": 8.1,
                "pe_ratio": 14.81,
                "pb_ratio": 1.47,
                "total_mv": 91465000000.0,
                "circ_mv": 70275000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 7.81, 涨跌幅 -3.58%",
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
    "code": "600362",
    "name": "江西铜业",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 2,
    "best_score": 88.847,
    "average_score": 88.847,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 2,
        "score": 88.847,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 2,
          "code": "600362",
          "name": "江西铜业",
          "score": 88.847,
          "screen_score": 86.84698722222223,
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
          "price": 42.97,
          "change_pct": -3.29,
          "amount": 2348976728.0,
          "industry": "",
          "factor_scores": {
            "value": 73.3589,
            "liquidity": 98.2222,
            "momentum": 45.8075,
            "reversal": 97.27,
            "activity": 81.5928,
            "stability": 68.13,
            "size": 98.0,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "600362",
              "name": "江西铜业",
              "source": "tencent",
              "fetched_at": "2026-09-15T09:43:13.206648+00:00",
              "price": 42.97,
              "change_pct": -3.29,
              "change_amount": -1.46,
              "volume": 54186900,
              "amount": 2348976728.0,
              "volume_ratio": 0.58,
              "turnover_rate": 2.61,
              "amplitude": 3.31,
              "open_price": 43.84,
              "high": 44.3,
              "low": 42.83,
              "pre_close": 44.43,
              "pe_ratio": 12.84,
              "pb_ratio": 1.7,
              "total_mv": 148793000000.0,
              "circ_mv": 89173000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 42.97, 涨跌幅 -3.29%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: controlled_reversal"
          },
          "post_analysis_tags": [
            "controlled_reversal"
          ],
          "raw": {
            "rank": 2,
            "code": "600362",
            "name": "江西铜业",
            "final_score": 88.847,
            "screen_score": 86.84698722222223,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 42.97,
            "change_pct": -3.29,
            "amount": 2348976728.0,
            "total_mv": 148793482533.0,
            "turnover_rate": 2.61,
            "volume_ratio": 0.58,
            "pe_ratio": 12.84089696,
            "pb_ratio": 1.69789021,
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
              "value": 73.3589,
              "liquidity": 98.2222,
              "momentum": 45.8075,
              "reversal": 97.27,
              "activity": 81.5928,
              "stability": 68.13,
              "size": 98.0,
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
                "code": "600362",
                "name": "江西铜业",
                "source": "tencent",
                "fetched_at": "2026-09-15T09:43:13.206648+00:00",
                "price": 42.97,
                "change_pct": -3.29,
                "change_amount": -1.46,
                "volume": 54186900,
                "amount": 2348976728.0,
                "volume_ratio": 0.58,
                "turnover_rate": 2.61,
                "amplitude": 3.31,
                "open_price": 43.84,
                "high": 44.3,
                "low": 42.83,
                "pre_close": 44.43,
                "pe_ratio": 12.84,
                "pb_ratio": 1.7,
                "total_mv": 148793000000.0,
                "circ_mv": 89173000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 42.97, 涨跌幅 -3.29%",
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
    "code": "002497",
    "name": "雅化集团",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 3,
    "best_score": 88.1519,
    "average_score": 88.1519,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 3,
        "score": 88.1519,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 3,
          "code": "002497",
          "name": "雅化集团",
          "score": 88.1519,
          "screen_score": 83.75187027777778,
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
          "price": 16.3,
          "change_pct": -3.21,
          "amount": 465399947.96,
          "industry": "",
          "factor_scores": {
            "value": 76.5711,
            "liquidity": 78.8889,
            "momentum": 46.0675,
            "reversal": 96.23,
            "activity": 85.5749,
            "stability": 68.37,
            "size": 77.3333,
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
            "code": "002497",
            "name": "雅化集团",
            "final_score": 88.1519,
            "screen_score": 83.75187027777778,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 16.3,
            "change_pct": -3.21,
            "amount": 465399947.96,
            "total_mv": 18786769076.0,
            "turnover_rate": 2.67,
            "volume_ratio": 1.41,
            "pe_ratio": 10.97080837,
            "pb_ratio": 1.5436193,
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
              "value": 76.5711,
              "liquidity": 78.8889,
              "momentum": 46.0675,
              "reversal": 96.23,
              "activity": 85.5749,
              "stability": 68.37,
              "size": 77.3333,
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
    "code": "600578",
    "name": "京能电力",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 4,
    "best_score": 86.1058,
    "average_score": 86.1058,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 4,
        "score": 86.1058,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 4,
          "code": "600578",
          "name": "京能电力",
          "score": 86.1058,
          "screen_score": 81.70577111111112,
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
          "price": 5.46,
          "change_pct": -2.85,
          "amount": 429166847.0,
          "industry": "",
          "factor_scores": {
            "value": 78.7094,
            "liquidity": 77.5556,
            "momentum": 47.2375,
            "reversal": 91.55,
            "activity": 77.371,
            "stability": 69.45,
            "size": 89.7778,
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
            "code": "600578",
            "name": "京能电力",
            "final_score": 86.1058,
            "screen_score": 81.70577111111112,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 5.46,
            "change_pct": -2.85,
            "amount": 429166847.0,
            "total_mv": 36552630742.0,
            "turnover_rate": 1.16,
            "volume_ratio": 0.8,
            "pe_ratio": 10.34374025,
            "pb_ratio": 1.46576125,
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
              "value": 78.7094,
              "liquidity": 77.5556,
              "momentum": 47.2375,
              "reversal": 91.55,
              "activity": 77.371,
              "stability": 69.45,
              "size": 89.7778,
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
    "code": "300207",
    "name": "欣旺达",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 5,
    "best_score": 85.8181,
    "average_score": 85.8181,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 5,
        "score": 85.8181,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 5,
          "code": "300207",
          "name": "欣旺达",
          "score": 85.8181,
          "screen_score": 83.81811583333334,
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
          "price": 17.74,
          "change_pct": -3.32,
          "amount": 1124992284.94,
          "industry": "",
          "factor_scores": {
            "value": 59.0033,
            "liquidity": 93.1111,
            "momentum": 45.71,
            "reversal": 97.66,
            "activity": 82.4264,
            "stability": 68.04,
            "size": 88.2222,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "300207",
              "name": "欣旺达",
              "source": "tencent",
              "fetched_at": "2026-09-15T09:43:35.271523+00:00",
              "price": 17.74,
              "change_pct": -3.32,
              "change_amount": -0.61,
              "volume": 62607300,
              "amount": 1124992285.0,
              "volume_ratio": 0.97,
              "turnover_rate": 3.65,
              "amplitude": 3.71,
              "open_price": 18.29,
              "high": 18.39,
              "low": 17.71,
              "pre_close": 18.35,
              "pe_ratio": 40.76,
              "pb_ratio": 1.36,
              "total_mv": 32774000000.0,
              "circ_mv": 30405000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 17.74, 涨跌幅 -3.32%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: controlled_reversal"
          },
          "post_analysis_tags": [
            "controlled_reversal"
          ],
          "raw": {
            "rank": 5,
            "code": "300207",
            "name": "欣旺达",
            "final_score": 85.8181,
            "screen_score": 83.81811583333334,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 17.74,
            "change_pct": -3.32,
            "amount": 1124992284.94,
            "total_mv": 32773983792.0,
            "turnover_rate": 3.65,
            "volume_ratio": 0.97,
            "pe_ratio": 40.76375525,
            "pb_ratio": 1.35635773,
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
              "value": 59.0033,
              "liquidity": 93.1111,
              "momentum": 45.71,
              "reversal": 97.66,
              "activity": 82.4264,
              "stability": 68.04,
              "size": 88.2222,
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
                "code": "300207",
                "name": "欣旺达",
                "source": "tencent",
                "fetched_at": "2026-09-15T09:43:35.271523+00:00",
                "price": 17.74,
                "change_pct": -3.32,
                "change_amount": -0.61,
                "volume": 62607300,
                "amount": 1124992285.0,
                "volume_ratio": 0.97,
                "turnover_rate": 3.65,
                "amplitude": 3.71,
                "open_price": 18.29,
                "high": 18.39,
                "low": 17.71,
                "pre_close": 18.35,
                "pe_ratio": 40.76,
                "pb_ratio": 1.36,
                "total_mv": 32774000000.0,
                "circ_mv": 30405000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 17.74, 涨跌幅 -3.32%",
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
    "code": "002241",
    "name": "歌尔股份",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 6,
    "best_score": 85.7241,
    "average_score": 85.7241,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 6,
        "score": 85.7241,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 6,
          "code": "002241",
          "name": "歌尔股份",
          "score": 85.7241,
          "screen_score": 83.72406138888888,
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
          "price": 21.37,
          "change_pct": -3.13,
          "amount": 1211658625.78,
          "industry": "",
          "factor_scores": {
            "value": 62.7156,
            "liquidity": 94.8889,
            "momentum": 46.3275,
            "reversal": 95.19,
            "activity": 80.1929,
            "stability": 68.61,
            "size": 94.4444,
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
            "rank": 6,
            "code": "002241",
            "name": "歌尔股份",
            "final_score": 85.7241,
            "screen_score": 83.72406138888888,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 21.37,
            "change_pct": -3.13,
            "amount": 1211658625.78,
            "total_mv": 76035797719.0,
            "turnover_rate": 1.78,
            "volume_ratio": 0.93,
            "pe_ratio": 19.05992419,
            "pb_ratio": 2.00062986,
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
              "value": 62.7156,
              "liquidity": 94.8889,
              "momentum": 46.3275,
              "reversal": 95.19,
              "activity": 80.1929,
              "stability": 68.61,
              "size": 94.4444,
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
    "code": "300413",
    "name": "芒果超媒",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 7,
    "best_score": 84.552,
    "average_score": 84.552,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 7,
        "score": 84.552,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 7,
          "code": "300413",
          "name": "芒果超媒",
          "score": 84.552,
          "screen_score": 82.5520463888889,
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
          "price": 16.73,
          "change_pct": -3.24,
          "amount": 1279409252.25,
          "industry": "",
          "factor_scores": {
            "value": 56.6406,
            "liquidity": 95.3333,
            "momentum": 45.97,
            "reversal": 96.62,
            "activity": 67.0926,
            "stability": 68.28,
            "size": 87.1111,
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
            "code": "300413",
            "name": "芒果超媒",
            "final_score": 84.552,
            "screen_score": 82.5520463888889,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 16.73,
            "change_pct": -3.24,
            "amount": 1279409252.25,
            "total_mv": 31297159235.0,
            "turnover_rate": 7.38,
            "volume_ratio": 0.55,
            "pe_ratio": 47.03259189,
            "pb_ratio": 1.35580221,
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
              "value": 56.6406,
              "liquidity": 95.3333,
              "momentum": 45.97,
              "reversal": 96.62,
              "activity": 67.0926,
              "stability": 68.28,
              "size": 87.1111,
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
    "code": "002130",
    "name": "沃尔核材",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 8,
    "best_score": 84.2644,
    "average_score": 84.2644,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 8,
        "score": 84.2644,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 8,
          "code": "002130",
          "name": "沃尔核材",
          "score": 84.2644,
          "screen_score": 82.26435694444444,
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
          "price": 16.93,
          "change_pct": -3.7,
          "amount": 959879419.79,
          "industry": "",
          "factor_scores": {
            "value": 54.6828,
            "liquidity": 91.5556,
            "momentum": 44.475,
            "reversal": 97.4,
            "activity": 78.2519,
            "stability": 66.9,
            "size": 82.2222,
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
            "code": "002130",
            "name": "沃尔核材",
            "final_score": 84.2644,
            "screen_score": 82.26435694444444,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 16.93,
            "change_pct": -3.7,
            "amount": 959879419.79,
            "total_mv": 23700093039.0,
            "turnover_rate": 4.86,
            "volume_ratio": 1.01,
            "pe_ratio": 20.56445379,
            "pb_ratio": 2.57806484,
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
              "value": 54.6828,
              "liquidity": 91.5556,
              "momentum": 44.475,
              "reversal": 97.4,
              "activity": 78.2519,
              "stability": 66.9,
              "size": 82.2222,
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
    "code": "600596",
    "name": "新安股份",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 9,
    "best_score": 83.9066,
    "average_score": 83.9066,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 9,
        "score": 83.9066,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 9,
          "code": "600596",
          "name": "新安股份",
          "score": 83.9066,
          "screen_score": 81.90664527777777,
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
          "price": 12.51,
          "change_pct": -3.17,
          "amount": 1125436082.0,
          "industry": "",
          "factor_scores": {
            "value": 55.5311,
            "liquidity": 93.3333,
            "momentum": 46.1975,
            "reversal": 95.71,
            "activity": 70.6611,
            "stability": 68.49,
            "size": 74.4444,
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
            "code": "600596",
            "name": "新安股份",
            "final_score": 83.9066,
            "screen_score": 81.90664527777777,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 12.51,
            "change_pct": -3.17,
            "amount": 1125436082.0,
            "total_mv": 16883459083.0,
            "turnover_rate": 6.54,
            "volume_ratio": 0.67,
            "pe_ratio": 50.85541659,
            "pb_ratio": 1.34289471,
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
              "value": 55.5311,
              "liquidity": 93.3333,
              "momentum": 46.1975,
              "reversal": 95.71,
              "activity": 70.6611,
              "stability": 68.49,
              "size": 74.4444,
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
    "code": "600711",
    "name": "盛屯矿业",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 10,
    "best_score": 83.3709,
    "average_score": 83.3709,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 10,
        "score": 83.3709,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 10,
          "code": "600711",
          "name": "盛屯矿业",
          "score": 83.3709,
          "screen_score": 81.37089472222222,
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
          "price": 10.73,
          "change_pct": -2.72,
          "amount": 645931452.0,
          "industry": "",
          "factor_scores": {
            "value": 71.2739,
            "liquidity": 85.1111,
            "momentum": 47.66,
            "reversal": 89.86,
            "activity": 78.9179,
            "stability": 69.84,
            "size": 88.4444,
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
            "code": "600711",
            "name": "盛屯矿业",
            "final_score": 83.3709,
            "screen_score": 81.37089472222222,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 10.73,
            "change_pct": -2.72,
            "amount": 645931452.0,
            "total_mv": 33162261942.0,
            "turnover_rate": 1.93,
            "volume_ratio": 0.53,
            "pe_ratio": 12.22448219,
            "pb_ratio": 1.85511141,
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
              "value": 71.2739,
              "liquidity": 85.1111,
              "momentum": 47.66,
              "reversal": 89.86,
              "activity": 78.9179,
              "stability": 69.84,
              "size": 88.4444,
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
    "code": "603236",
    "name": "移远通信",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 1,
    "best_score": 75.3272,
    "average_score": 75.3272,
    "strategy_details": {
      "capital_heat": {
        "rank": 1,
        "score": 75.3272,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 1,
          "code": "603236",
          "name": "移远通信",
          "score": 75.3272,
          "screen_score": 72.92718222222221,
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
          "price": 66.85,
          "change_pct": 6.64,
          "amount": 1901994880.0,
          "industry": "",
          "factor_scores": {
            "value": 67.9032,
            "liquidity": 88.8889,
            "momentum": 76.988,
            "reversal": 5.0,
            "activity": 82.36,
            "stability": 58.08,
            "size": 82.8283,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "603236",
              "name": "移远通信",
              "source": "tencent",
              "fetched_at": "2026-09-15T09:42:03.085194+00:00",
              "price": 66.85,
              "change_pct": 6.64,
              "change_amount": 4.16,
              "volume": 29028300,
              "amount": 1901994880.0,
              "volume_ratio": 2.56,
              "turnover_rate": 7.16,
              "amplitude": 6.84,
              "open_price": 63.09,
              "high": 66.98,
              "low": 62.69,
              "pre_close": 62.69,
              "pe_ratio": 27.99,
              "pb_ratio": 3.78,
              "total_mv": 27099000000.0,
              "circ_mv": 27099000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 66.85, 涨跌幅 6.64%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 1,
            "code": "603236",
            "name": "移远通信",
            "final_score": 75.3272,
            "screen_score": 72.92718222222221,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 66.85,
            "change_pct": 6.64,
            "amount": 1901994880.0,
            "total_mv": 27098660812.0,
            "turnover_rate": 7.16,
            "volume_ratio": 2.56,
            "pe_ratio": 27.98752212,
            "pb_ratio": 3.68054172,
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
              "value": 67.9032,
              "liquidity": 88.8889,
              "momentum": 76.988,
              "reversal": 5.0,
              "activity": 82.36,
              "stability": 58.08,
              "size": 82.8283,
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
                "code": "603236",
                "name": "移远通信",
                "source": "tencent",
                "fetched_at": "2026-09-15T09:42:03.085194+00:00",
                "price": 66.85,
                "change_pct": 6.64,
                "change_amount": 4.16,
                "volume": 29028300,
                "amount": 1901994880.0,
                "volume_ratio": 2.56,
                "turnover_rate": 7.16,
                "amplitude": 6.84,
                "open_price": 63.09,
                "high": 66.98,
                "low": 62.69,
                "pre_close": 62.69,
                "pe_ratio": 27.99,
                "pb_ratio": 3.78,
                "total_mv": 27099000000.0,
                "circ_mv": 27099000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 66.85, 涨跌幅 6.64%",
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
    "best_score": 74.5732,
    "average_score": 74.5732,
    "strategy_details": {
      "momentum_quality": {
        "rank": 1,
        "score": 74.5732,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 1,
          "code": "601318",
          "name": "中国平安",
          "score": 74.5732,
          "screen_score": 71.57319905378485,
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
          "price": 53.9,
          "change_pct": -1.52,
          "amount": 2677888136.0,
          "industry": "",
          "factor_scores": {
            "value": 84.7007,
            "liquidity": 96.4143,
            "momentum": 51.56,
            "reversal": 80.76,
            "activity": 67.1823,
            "stability": 73.44,
            "size": 97.8088,
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
              "fetched_at": "2026-09-15T09:42:33.904510+00:00",
              "price": 53.9,
              "change_pct": -1.52,
              "change_amount": -0.83,
              "volume": 49459400,
              "amount": 2677888136.0,
              "volume_ratio": 0.9,
              "turnover_rate": 0.46,
              "amplitude": 2.12,
              "open_price": 54.9,
              "high": 54.92,
              "low": 53.76,
              "pre_close": 54.73,
              "pe_ratio": 6.13,
              "pb_ratio": 0.97,
              "total_mv": 976002000000.0,
              "circ_mv": 574578000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 53.9, 涨跌幅 -1.52%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 1,
            "code": "601318",
            "name": "中国平安",
            "final_score": 74.5732,
            "screen_score": 71.57319905378485,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 53.9,
            "change_pct": -1.52,
            "amount": 2677888136.0,
            "total_mv": 976001903531.0,
            "turnover_rate": 0.46,
            "volume_ratio": 0.9,
            "pe_ratio": 6.12620141,
            "pb_ratio": 0.94934062,
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
              "value": 84.7007,
              "liquidity": 96.4143,
              "momentum": 51.56,
              "reversal": 80.76,
              "activity": 67.1823,
              "stability": 73.44,
              "size": 97.8088,
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
            "dsa_context": {
              "enriched": true,
              "profile": "pre_rank_light",
              "news_included": false,
              "events_included": false,
              "quote": {
                "code": "601318",
                "name": "中国平安",
                "source": "tencent",
                "fetched_at": "2026-09-15T09:42:33.904510+00:00",
                "price": 53.9,
                "change_pct": -1.52,
                "change_amount": -0.83,
                "volume": 49459400,
                "amount": 2677888136.0,
                "volume_ratio": 0.9,
                "turnover_rate": 0.46,
                "amplitude": 2.12,
                "open_price": 54.9,
                "high": 54.92,
                "low": 53.76,
                "pre_close": 54.73,
                "pe_ratio": 6.13,
                "pb_ratio": 0.97,
                "total_mv": 976002000000.0,
                "circ_mv": 574578000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 53.9, 涨跌幅 -1.52%",
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
    "code": "000657",
    "name": "中钨高新",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 2,
    "best_score": 74.4855,
    "average_score": 74.4855,
    "strategy_details": {
      "capital_heat": {
        "rank": 2,
        "score": 74.4855,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 2,
          "code": "000657",
          "name": "中钨高新",
          "score": 74.4855,
          "screen_score": 74.08546,
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
          "price": 62.23,
          "change_pct": 5.17,
          "amount": 6129100362.69,
          "industry": "",
          "factor_scores": {
            "value": 32.3723,
            "liquidity": 100.0,
            "momentum": 73.3025,
            "reversal": 5.0,
            "activity": 82.7845,
            "stability": 62.49,
            "size": 98.9899,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "000657",
              "name": "中钨高新",
              "source": "tencent",
              "fetched_at": "2026-09-15T09:41:51.987651+00:00",
              "price": 62.23,
              "change_pct": 5.17,
              "change_amount": 3.06,
              "volume": 98747800,
              "amount": 6129100363.0,
              "volume_ratio": 2.36,
              "turnover_rate": 6.8,
              "amplitude": 5.05,
              "open_price": 60.58,
              "high": 63.56,
              "low": 60.57,
              "pre_close": 59.17,
              "pe_ratio": 50.44,
              "pb_ratio": 12.57,
              "total_mv": 141796000000.0,
              "circ_mv": 90407000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 62.23, 涨跌幅 5.17%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 2,
            "code": "000657",
            "name": "中钨高新",
            "final_score": 74.4855,
            "screen_score": 74.08546,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 62.23,
            "change_pct": 5.17,
            "amount": 6129100362.69,
            "total_mv": 141796330859.0,
            "turnover_rate": 6.79,
            "volume_ratio": 2.36,
            "pe_ratio": 50.4382602,
            "pb_ratio": 12.5707506,
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
              "value": 32.3723,
              "liquidity": 100.0,
              "momentum": 73.3025,
              "reversal": 5.0,
              "activity": 82.7845,
              "stability": 62.49,
              "size": 98.9899,
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
                "code": "000657",
                "name": "中钨高新",
                "source": "tencent",
                "fetched_at": "2026-09-15T09:41:51.987651+00:00",
                "price": 62.23,
                "change_pct": 5.17,
                "change_amount": 3.06,
                "volume": 98747800,
                "amount": 6129100363.0,
                "volume_ratio": 2.36,
                "turnover_rate": 6.8,
                "amplitude": 5.05,
                "open_price": 60.58,
                "high": 63.56,
                "low": 60.57,
                "pre_close": 59.17,
                "pe_ratio": 50.44,
                "pb_ratio": 12.57,
                "total_mv": 141796000000.0,
                "circ_mv": 90407000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 62.23, 涨跌幅 5.17%",
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
    "code": "300450",
    "name": "先导智能",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 3,
    "best_score": 74.3243,
    "average_score": 74.3243,
    "strategy_details": {
      "capital_heat": {
        "rank": 3,
        "score": 74.3243,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 3,
          "code": "300450",
          "name": "先导智能",
          "score": 74.3243,
          "screen_score": 71.92430338383839,
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
          "price": 31.54,
          "change_pct": 5.56,
          "amount": 2105752642.33,
          "industry": "",
          "factor_scores": {
            "value": 72.3823,
            "liquidity": 89.899,
            "momentum": 74.57,
            "reversal": 5.0,
            "activity": 79.8074,
            "stability": 61.32,
            "size": 92.9293,
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
            "code": "300450",
            "name": "先导智能",
            "final_score": 74.3243,
            "screen_score": 71.92430338383839,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 31.54,
            "change_pct": 5.56,
            "amount": 2105752642.33,
            "total_mv": 52804944028.0,
            "turnover_rate": 4.32,
            "volume_ratio": 3.19,
            "pe_ratio": 29.67262344,
            "pb_ratio": 2.93539005,
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
              "value": 72.3823,
              "liquidity": 89.899,
              "momentum": 74.57,
              "reversal": 5.0,
              "activity": 79.8074,
              "stability": 61.32,
              "size": 92.9293,
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
    "code": "601398",
    "name": "工商银行",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 2,
    "best_score": 74.1289,
    "average_score": 74.1289,
    "strategy_details": {
      "momentum_quality": {
        "rank": 2,
        "score": 74.1289,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 2,
          "code": "601398",
          "name": "工商银行",
          "score": 74.1289,
          "screen_score": 71.1288608565737,
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
          "price": 8.13,
          "change_pct": -1.09,
          "amount": 1730279695.0,
          "industry": "",
          "factor_scores": {
            "value": 85.6599,
            "liquidity": 92.6295,
            "momentum": 52.9575,
            "reversal": 75.17,
            "activity": 65.3605,
            "stability": 74.73,
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
              "code": "601398",
              "name": "工商银行",
              "source": "tencent",
              "fetched_at": "2026-09-15T09:42:42.426071+00:00",
              "price": 8.13,
              "change_pct": -1.09,
              "change_amount": -0.09,
              "volume": 212565900,
              "amount": 1730279695.0,
              "volume_ratio": 0.8,
              "turnover_rate": 0.08,
              "amplitude": 1.58,
              "open_price": 8.21,
              "high": 8.22,
              "low": 8.09,
              "pre_close": 8.22,
              "pe_ratio": 7.74,
              "pb_ratio": 0.73,
              "total_mv": 2897583000000.0,
              "circ_mv": 2191947000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 8.13, 涨跌幅 -1.09%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 2,
            "code": "601398",
            "name": "工商银行",
            "final_score": 74.1289,
            "screen_score": 71.1288608565737,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 8.13,
            "change_pct": -1.09,
            "amount": 1730279695.0,
            "total_mv": 2897582870134.0,
            "turnover_rate": 0.08,
            "volume_ratio": 0.8,
            "pe_ratio": 7.74462801,
            "pb_ratio": 0.73128294,
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
              "value": 85.6599,
              "liquidity": 92.6295,
              "momentum": 52.9575,
              "reversal": 75.17,
              "activity": 65.3605,
              "stability": 74.73,
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
            "dsa_context": {
              "enriched": true,
              "profile": "pre_rank_light",
              "news_included": false,
              "events_included": false,
              "quote": {
                "code": "601398",
                "name": "工商银行",
                "source": "tencent",
                "fetched_at": "2026-09-15T09:42:42.426071+00:00",
                "price": 8.13,
                "change_pct": -1.09,
                "change_amount": -0.09,
                "volume": 212565900,
                "amount": 1730279695.0,
                "volume_ratio": 0.8,
                "turnover_rate": 0.08,
                "amplitude": 1.58,
                "open_price": 8.21,
                "high": 8.22,
                "low": 8.09,
                "pre_close": 8.22,
                "pe_ratio": 7.74,
                "pb_ratio": 0.73,
                "total_mv": 2897583000000.0,
                "circ_mv": 2191947000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 8.13, 涨跌幅 -1.09%",
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
    "best_score": 74.1069,
    "average_score": 74.1069,
    "strategy_details": {
      "momentum_quality": {
        "rank": 3,
        "score": 74.1069,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 3,
          "code": "600036",
          "name": "招商银行",
          "score": 74.1069,
          "screen_score": 71.10687749003984,
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
          "price": 41.1,
          "change_pct": -1.75,
          "amount": 2340692538.0,
          "industry": "",
          "factor_scores": {
            "value": 84.9193,
            "liquidity": 95.0199,
            "momentum": 50.8125,
            "reversal": 83.75,
            "activity": 66.625,
            "stability": 72.75,
            "size": 98.2072,
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
              "fetched_at": "2026-09-15T09:42:53.541221+00:00",
              "price": 41.1,
              "change_pct": -1.75,
              "change_amount": -0.73,
              "volume": 56779400,
              "amount": 2340692538.0,
              "volume_ratio": 0.92,
              "turnover_rate": 0.28,
              "amplitude": 1.84,
              "open_price": 41.78,
              "high": 41.78,
              "low": 41.01,
              "pre_close": 41.83,
              "pe_ratio": 6.83,
              "pb_ratio": 0.91,
              "total_mv": 1036536000000.0,
              "circ_mv": 847850000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 41.1, 涨跌幅 -1.75%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 3,
            "code": "600036",
            "name": "招商银行",
            "final_score": 74.1069,
            "screen_score": 71.10687749003984,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 41.1,
            "change_pct": -1.75,
            "amount": 2340692538.0,
            "total_mv": 1036535654201.0,
            "turnover_rate": 0.28,
            "volume_ratio": 0.92,
            "pe_ratio": 6.83297947,
            "pb_ratio": 0.90523653,
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
              "value": 84.9193,
              "liquidity": 95.0199,
              "momentum": 50.8125,
              "reversal": 83.75,
              "activity": 66.625,
              "stability": 72.75,
              "size": 98.2072,
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
            "dsa_context": {
              "enriched": true,
              "profile": "pre_rank_light",
              "news_included": false,
              "events_included": false,
              "quote": {
                "code": "600036",
                "name": "招商银行",
                "source": "tencent",
                "fetched_at": "2026-09-15T09:42:53.541221+00:00",
                "price": 41.1,
                "change_pct": -1.75,
                "change_amount": -0.73,
                "volume": 56779400,
                "amount": 2340692538.0,
                "volume_ratio": 0.92,
                "turnover_rate": 0.28,
                "amplitude": 1.84,
                "open_price": 41.78,
                "high": 41.78,
                "low": 41.01,
                "pre_close": 41.83,
                "pe_ratio": 6.83,
                "pb_ratio": 0.91,
                "total_mv": 1036536000000.0,
                "circ_mv": 847850000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 41.1, 涨跌幅 -1.75%",
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
    "code": "000962",
    "name": "东方钽业",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 4,
    "best_score": 73.8005,
    "average_score": 73.8005,
    "strategy_details": {
      "capital_heat": {
        "rank": 4,
        "score": 73.8005,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 4,
          "code": "000962",
          "name": "东方钽业",
          "score": 73.8005,
          "screen_score": 71.40046570707071,
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
          "price": 57.2,
          "change_pct": 4.86,
          "amount": 2234681761.43,
          "industry": "",
          "factor_scores": {
            "value": 26.775,
            "liquidity": 91.9192,
            "momentum": 72.295,
            "reversal": 5.0,
            "activity": 78.6321,
            "stability": 63.42,
            "size": 85.8586,
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
            "code": "000962",
            "name": "东方钽业",
            "final_score": 73.8005,
            "screen_score": 71.40046570707071,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 57.2,
            "change_pct": 4.86,
            "amount": 2234681761.43,
            "total_mv": 30166431152.0,
            "turnover_rate": 7.83,
            "volume_ratio": 2.27,
            "pe_ratio": 127.93627351,
            "pb_ratio": 7.50051984,
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
              "value": 26.775,
              "liquidity": 91.9192,
              "momentum": 72.295,
              "reversal": 5.0,
              "activity": 78.6321,
              "stability": 63.42,
              "size": 85.8586,
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
    "code": "601166",
    "name": "兴业银行",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 4,
    "best_score": 73.6688,
    "average_score": 73.6688,
    "strategy_details": {
      "momentum_quality": {
        "rank": 4,
        "score": 73.6688,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 4,
          "code": "601166",
          "name": "兴业银行",
          "score": 73.6688,
          "screen_score": 70.66884499501991,
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
          "price": 17.92,
          "change_pct": -1.27,
          "amount": 1250219742.0,
          "industry": "",
          "factor_scores": {
            "value": 89.3914,
            "liquidity": 86.8526,
            "momentum": 52.3725,
            "reversal": 77.51,
            "activity": 67.0319,
            "stability": 74.19,
            "size": 95.2191,
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
            "code": "601166",
            "name": "兴业银行",
            "final_score": 73.6688,
            "screen_score": 70.66884499501991,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 17.92,
            "change_pct": -1.27,
            "amount": 1250219742.0,
            "total_mv": 379238442473.0,
            "turnover_rate": 0.33,
            "volume_ratio": 0.97,
            "pe_ratio": 5.02575495,
            "pb_ratio": 0.45353793,
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
              "value": 89.3914,
              "liquidity": 86.8526,
              "momentum": 52.3725,
              "reversal": 77.51,
              "activity": 67.0319,
              "stability": 74.19,
              "size": 95.2191,
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
    "code": "601288",
    "name": "农业银行",
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
          "code": "601288",
          "name": "农业银行",
          "score": 73.6338,
          "screen_score": 70.63376362051791,
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
          "price": 6.9,
          "change_pct": -1.43,
          "amount": 1695450994.0,
          "industry": "",
          "factor_scores": {
            "value": 84.6026,
            "liquidity": 92.0319,
            "momentum": 51.8525,
            "reversal": 79.59,
            "activity": 65.5874,
            "stability": 73.71,
            "size": 99.6016,
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
            "code": "601288",
            "name": "农业银行",
            "final_score": 73.6338,
            "screen_score": 70.63376362051791,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 6.9,
            "change_pct": -1.43,
            "amount": 1695450994.0,
            "total_mv": 2414882933724.0,
            "turnover_rate": 0.08,
            "volume_ratio": 0.85,
            "pe_ratio": 8.10602773,
            "pb_ratio": 0.8449514,
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
              "value": 84.6026,
              "liquidity": 92.0319,
              "momentum": 51.8525,
              "reversal": 79.59,
              "activity": 65.5874,
              "stability": 73.71,
              "size": 99.6016,
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
    "code": "002025",
    "name": "航天电器",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 5,
    "best_score": 73.2831,
    "average_score": 73.2831,
    "strategy_details": {
      "capital_heat": {
        "rank": 5,
        "score": 73.2831,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 5,
          "code": "002025",
          "name": "航天电器",
          "score": 73.2831,
          "screen_score": 70.88310641414141,
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
          "price": 68.78,
          "change_pct": 5.33,
          "amount": 1447791396.79,
          "industry": "",
          "factor_scores": {
            "value": 37.1411,
            "liquidity": 83.8384,
            "momentum": 73.8225,
            "reversal": 5.0,
            "activity": 80.1599,
            "stability": 62.01,
            "size": 88.8889,
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
            "code": "002025",
            "name": "航天电器",
            "final_score": 73.2831,
            "screen_score": 70.88310641414141,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 68.78,
            "change_pct": 5.33,
            "amount": 1447791396.79,
            "total_mv": 31227479918.0,
            "turnover_rate": 4.67,
            "volume_ratio": 2.21,
            "pe_ratio": 139.26622733,
            "pb_ratio": 4.67877764,
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
              "value": 37.1411,
              "liquidity": 83.8384,
              "momentum": 73.8225,
              "reversal": 5.0,
              "activity": 80.1599,
              "stability": 62.01,
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
    "best_rank": 6,
    "best_score": 73.0733,
    "average_score": 73.0733,
    "strategy_details": {
      "momentum_quality": {
        "rank": 6,
        "score": 73.0733,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 6,
          "code": "601939",
          "name": "建设银行",
          "score": 73.0733,
          "screen_score": 70.07334482071711,
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
          "price": 10.93,
          "change_pct": -1.62,
          "amount": 1195500449.0,
          "industry": "",
          "factor_scores": {
            "value": 84.8187,
            "liquidity": 85.4582,
            "momentum": 51.235,
            "reversal": 82.06,
            "activity": 70.447,
            "stability": 73.14,
            "size": 99.8008,
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
            "code": "601939",
            "name": "建设银行",
            "final_score": 73.0733,
            "screen_score": 70.07334482071711,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 10.93,
            "change_pct": -1.62,
            "amount": 1195500449.0,
            "total_mv": 2859292169347.0,
            "turnover_rate": 1.14,
            "volume_ratio": 1.08,
            "pe_ratio": 8.25445062,
            "pb_ratio": 0.79863923,
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
              "value": 84.8187,
              "liquidity": 85.4582,
              "momentum": 51.235,
              "reversal": 82.06,
              "activity": 70.447,
              "stability": 73.14,
              "size": 99.8008,
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
    "code": "600919",
    "name": "江苏银行",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 7,
    "best_score": 72.628,
    "average_score": 72.628,
    "strategy_details": {
      "momentum_quality": {
        "rank": 7,
        "score": 72.628,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 7,
          "code": "600919",
          "name": "江苏银行",
          "score": 72.628,
          "screen_score": 69.62798090139442,
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
          "price": 12.35,
          "change_pct": -1.59,
          "amount": 1155065455.0,
          "industry": "",
          "factor_scores": {
            "value": 85.8501,
            "liquidity": 84.6614,
            "momentum": 51.3325,
            "reversal": 81.67,
            "activity": 68.3151,
            "stability": 73.23,
            "size": 91.8327,
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
            "rank": 7,
            "code": "600919",
            "name": "江苏银行",
            "final_score": 72.628,
            "screen_score": 69.62798090139442,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 12.35,
            "change_pct": -1.59,
            "amount": 1155065455.0,
            "total_mv": 226638857118.0,
            "turnover_rate": 0.51,
            "volume_ratio": 1.11,
            "pe_ratio": 6.2714498,
            "pb_ratio": 0.83520077,
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
              "value": 85.8501,
              "liquidity": 84.6614,
              "momentum": 51.3325,
              "reversal": 81.67,
              "activity": 68.3151,
              "stability": 73.23,
              "size": 91.8327,
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
    "code": "603256",
    "name": "宏和科技",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 6,
    "best_score": 72.4348,
    "average_score": 72.4348,
    "strategy_details": {
      "capital_heat": {
        "rank": 6,
        "score": 72.4348,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 6,
          "code": "603256",
          "name": "宏和科技",
          "score": 72.4348,
          "screen_score": 72.03480151515151,
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
          "price": 138.23,
          "change_pct": 5.79,
          "amount": 4588322829.0,
          "industry": "",
          "factor_scores": {
            "value": 11.9862,
            "liquidity": 96.9697,
            "momentum": 75.3175,
            "reversal": 5.0,
            "activity": 75.5538,
            "stability": 60.63,
            "size": 97.9798,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "603256",
              "name": "宏和科技",
              "source": "tencent",
              "fetched_at": "2026-09-15T09:42:13.523671+00:00",
              "price": 138.23,
              "change_pct": 5.79,
              "change_amount": 7.56,
              "volume": 32801700,
              "amount": 4588322829.0,
              "volume_ratio": 2.02,
              "turnover_rate": 3.63,
              "amplitude": 9.75,
              "open_price": 131.0,
              "high": 143.74,
              "low": 131.0,
              "pre_close": 130.67,
              "pe_ratio": 253.11,
              "pb_ratio": 42.4,
              "total_mv": 125041000000.00002,
              "circ_mv": 125041000000.00002
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
          "dsa_analysis_summary": "DSA行情: 现价 138.23, 涨跌幅 5.79%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 6,
            "code": "603256",
            "name": "宏和科技",
            "final_score": 72.4348,
            "screen_score": 72.03480151515151,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 138.23,
            "change_pct": 5.79,
            "amount": 4588322829.0,
            "total_mv": 125040984292.0,
            "turnover_rate": 3.63,
            "volume_ratio": 2.02,
            "pe_ratio": 253.10667998,
            "pb_ratio": 42.39645179,
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
              "value": 11.9862,
              "liquidity": 96.9697,
              "momentum": 75.3175,
              "reversal": 5.0,
              "activity": 75.5538,
              "stability": 60.63,
              "size": 97.9798,
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
                "code": "603256",
                "name": "宏和科技",
                "source": "tencent",
                "fetched_at": "2026-09-15T09:42:13.523671+00:00",
                "price": 138.23,
                "change_pct": 5.79,
                "change_amount": 7.56,
                "volume": 32801700,
                "amount": 4588322829.0,
                "volume_ratio": 2.02,
                "turnover_rate": 3.63,
                "amplitude": 9.75,
                "open_price": 131.0,
                "high": 143.74,
                "low": 131.0,
                "pre_close": 130.67,
                "pe_ratio": 253.11,
                "pb_ratio": 42.4,
                "total_mv": 125041000000.00002,
                "circ_mv": 125041000000.00002
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
            "dsa_analysis_summary": "DSA行情: 现价 138.23, 涨跌幅 5.79%",
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
    "best_score": 72.188,
    "average_score": 72.188,
    "strategy_details": {
      "momentum_quality": {
        "rank": 8,
        "score": 72.188,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 8,
          "code": "600030",
          "name": "中信证券",
          "score": 72.188,
          "screen_score": 70.38796780378485,
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
          "price": 26.35,
          "change_pct": -0.98,
          "amount": 2196175723.0,
          "industry": "",
          "factor_scores": {
            "value": 75.9776,
            "liquidity": 94.6215,
            "momentum": 53.315,
            "reversal": 73.74,
            "activity": 67.7474,
            "stability": 75.06,
            "size": 95.6175,
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
            "final_score": 72.188,
            "screen_score": 70.38796780378485,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 26.35,
            "change_pct": -0.98,
            "amount": 2196175723.0,
            "total_mv": 411699572786.0,
            "turnover_rate": 0.68,
            "volume_ratio": 0.85,
            "pe_ratio": 10.38183582,
            "pb_ratio": 1.3933515,
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
              "value": 75.9776,
              "liquidity": 94.6215,
              "momentum": 53.315,
              "reversal": 73.74,
              "activity": 67.7474,
              "stability": 75.06,
              "size": 95.6175,
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
    "best_score": 71.9661,
    "average_score": 71.9661,
    "strategy_details": {
      "momentum_quality": {
        "rank": 9,
        "score": 71.9661,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 9,
          "code": "601988",
          "name": "中国银行",
          "score": 71.9661,
          "screen_score": 70.16607141434262,
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
          "price": 6.57,
          "change_pct": -1.05,
          "amount": 1294905374.0,
          "industry": "",
          "factor_scores": {
            "value": 84.9636,
            "liquidity": 87.4502,
            "momentum": 53.0875,
            "reversal": 74.65,
            "activity": 65.7595,
            "stability": 74.85,
            "size": 99.2032,
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
            "final_score": 71.9661,
            "screen_score": 70.16607141434262,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 6.57,
            "change_pct": -1.05,
            "amount": 1294905374.0,
            "total_mv": 2116935545618.0,
            "turnover_rate": 0.09,
            "volume_ratio": 0.88,
            "pe_ratio": 8.50092981,
            "pb_ratio": 0.76960136,
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
              "value": 84.9636,
              "liquidity": 87.4502,
              "momentum": 53.0875,
              "reversal": 74.65,
              "activity": 65.7595,
              "stability": 74.85,
              "size": 99.2032,
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
    "code": "002378",
    "name": "章源钨业",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 7,
    "best_score": 71.9336,
    "average_score": 71.9336,
    "strategy_details": {
      "capital_heat": {
        "rank": 7,
        "score": 71.9336,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 7,
          "code": "002378",
          "name": "章源钨业",
          "score": 71.9336,
          "screen_score": 71.53360757575759,
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
          "price": 24.74,
          "change_pct": 5.73,
          "amount": 1481210748.96,
          "industry": "",
          "factor_scores": {
            "value": 43.2029,
            "liquidity": 84.8485,
            "momentum": 75.1225,
            "reversal": 5.0,
            "activity": 80.8488,
            "stability": 60.81,
            "size": 84.8485,
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
            "code": "002378",
            "name": "章源钨业",
            "final_score": 71.9336,
            "screen_score": 71.53360757575759,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 24.74,
            "change_pct": 5.73,
            "amount": 1481210748.96,
            "total_mv": 29723073057.0,
            "turnover_rate": 5.0,
            "volume_ratio": 3.5,
            "pe_ratio": 34.44386765,
            "pb_ratio": 10.30557203,
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
              "value": 43.2029,
              "liquidity": 84.8485,
              "momentum": 75.1225,
              "reversal": 5.0,
              "activity": 80.8488,
              "stability": 60.81,
              "size": 84.8485,
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
    "code": "601169",
    "name": "北京银行",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 10,
    "best_score": 71.7766,
    "average_score": 71.7766,
    "strategy_details": {
      "momentum_quality": {
        "rank": 10,
        "score": 71.7766,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 10,
          "code": "601169",
          "name": "北京银行",
          "score": 71.7766,
          "screen_score": 69.97664407370517,
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
          "price": 5.66,
          "change_pct": -0.35,
          "amount": 963339645.0,
          "industry": "",
          "factor_scores": {
            "value": 89.001,
            "liquidity": 79.6813,
            "momentum": 55.3625,
            "reversal": 65.55,
            "activity": 68.8052,
            "stability": 76.95,
            "size": 80.2789,
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
            "code": "601169",
            "name": "北京银行",
            "final_score": 71.7766,
            "screen_score": 69.97664407370517,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 5.66,
            "change_pct": -0.35,
            "amount": 963339645.0,
            "total_mv": 119669290980.0,
            "turnover_rate": 0.81,
            "volume_ratio": 0.98,
            "pe_ratio": 5.71677691,
            "pb_ratio": 0.41979503,
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
              "value": 89.001,
              "liquidity": 79.6813,
              "momentum": 55.3625,
              "reversal": 65.55,
              "activity": 68.8052,
              "stability": 76.95,
              "size": 80.2789,
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
    "code": "600549",
    "name": "厦门钨业",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 8,
    "best_score": 70.4325,
    "average_score": 70.4325,
    "strategy_details": {
      "capital_heat": {
        "rank": 8,
        "score": 70.4325,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 8,
          "code": "600549",
          "name": "厦门钨业",
          "score": 70.4325,
          "screen_score": 70.4325441919192,
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
          "price": 51.14,
          "change_pct": 3.56,
          "amount": 3115673634.0,
          "industry": "",
          "factor_scores": {
            "value": 67.5371,
            "liquidity": 94.9495,
            "momentum": 68.07,
            "reversal": 5.0,
            "activity": 76.8794,
            "stability": 67.32,
            "size": 95.9596,
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
            "code": "600549",
            "name": "厦门钨业",
            "final_score": 70.4325,
            "screen_score": 70.4325441919192,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 51.14,
            "change_pct": 3.56,
            "amount": 3115673634.0,
            "total_mv": 81189139142.0,
            "turnover_rate": 3.91,
            "volume_ratio": 2.09,
            "pe_ratio": 22.92957604,
            "pb_ratio": 4.34347019,
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
              "value": 67.5371,
              "liquidity": 94.9495,
              "momentum": 68.07,
              "reversal": 5.0,
              "activity": 76.8794,
              "stability": 67.32,
              "size": 95.9596,
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
    "code": "603000",
    "name": "人民网",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 9,
    "best_score": 70.0125,
    "average_score": 70.0125,
    "strategy_details": {
      "capital_heat": {
        "rank": 9,
        "score": 70.0125,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 9,
          "code": "603000",
          "name": "人民网",
          "score": 70.0125,
          "screen_score": 70.01249944444444,
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
          "price": 17.23,
          "change_pct": 3.98,
          "amount": 1321013575.0,
          "industry": "",
          "factor_scores": {
            "value": 41.0871,
            "liquidity": 77.7778,
            "momentum": 69.435,
            "reversal": 5.0,
            "activity": 84.0816,
            "stability": 66.06,
            "size": 74.7475,
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
            "code": "603000",
            "name": "人民网",
            "final_score": 70.0125,
            "screen_score": 70.01249944444444,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 17.23,
            "change_pct": 3.98,
            "amount": 1321013575.0,
            "total_mv": 19051056895.0,
            "turnover_rate": 6.77,
            "volume_ratio": 2.97,
            "pe_ratio": 79.67220086,
            "pb_ratio": 5.07707504,
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
              "value": 41.0871,
              "liquidity": 77.7778,
              "momentum": 69.435,
              "reversal": 5.0,
              "activity": 84.0816,
              "stability": 66.06,
              "size": 74.7475,
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
    "code": "002080",
    "name": "中材科技",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 10,
    "best_score": 69.4233,
    "average_score": 69.4233,
    "strategy_details": {
      "capital_heat": {
        "rank": 10,
        "score": 69.4233,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 10,
          "code": "002080",
          "name": "中材科技",
          "score": 69.4233,
          "screen_score": 69.42330535353535,
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
          "price": 53.77,
          "change_pct": 1.86,
          "amount": 3365503204.21,
          "industry": "",
          "factor_scores": {
            "value": 57.0726,
            "liquidity": 95.9596,
            "momentum": 62.545,
            "reversal": 29.94,
            "activity": 73.6278,
            "stability": 72.42,
            "size": 96.9697,
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
            "rank": 10,
            "code": "002080",
            "name": "中材科技",
            "final_score": 69.4233,
            "screen_score": 69.42330535353535,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 53.77,
            "change_pct": 1.86,
            "amount": 3365503204.21,
            "total_mv": 90232705112.0,
            "turnover_rate": 3.7,
            "volume_ratio": 1.54,
            "pe_ratio": 44.51961433,
            "pb_ratio": 4.42095527,
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
              "value": 57.0726,
              "liquidity": 95.9596,
              "momentum": 62.545,
              "reversal": 29.94,
              "activity": 73.6278,
              "stability": 72.42,
              "size": 96.9697,
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
