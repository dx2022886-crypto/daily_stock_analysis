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
| 1 | 601668 | 中国建筑 | 1 | 超跌反转 | 91.0962 | 1 |
| 2 | 600585 | 海螺水泥 | 1 | 超跌反转 | 89.2919 | 2 |
| 3 | 601117 | 中国化学 | 1 | 超跌反转 | 88.7167 | 3 |
| 4 | 600352 | 浙江龙盛 | 1 | 超跌反转 | 86.1995 | 4 |
| 5 | 603345 | 安井食品 | 1 | 超跌反转 | 85.9235 | 5 |
| 6 | 002237 | 恒邦股份 | 1 | 超跌反转 | 84.3153 | 6 |
| 7 | 000932 | 华菱钢铁 | 1 | 超跌反转 | 84.2454 | 7 |
| 8 | 601799 | 星宇股份 | 1 | 超跌反转 | 84.1841 | 8 |
| 9 | 000975 | 山金国际 | 1 | 超跌反转 | 83.948 | 9 |
| 10 | 300724 | 捷佳伟创 | 1 | 超跌反转 | 83.3607 | 10 |
| 11 | 688018 | 乐鑫科技 | 1 | 放量突破 | 79.2272 | 1 |
| 12 | 002292 | 奥飞娱乐 | 1 | 放量突破 | 77.5163 | 2 |
| 13 | 601169 | 北京银行 | 1 | 动量质量 | 76.4019 | 1 |
| 14 | 600547 | 山东黄金 | 1 | 资金热度 | 76.3309 | 1 |
| 15 | 002092 | 中泰化学 | 1 | 放量突破 | 76.0502 | 3 |
| 16 | 600036 | 招商银行 | 1 | 动量质量 | 75.302 | 2 |
| 17 | 601166 | 兴业银行 | 1 | 动量质量 | 74.6624 | 3 |
| 18 | 601398 | 工商银行 | 1 | 动量质量 | 74.5814 | 4 |
| 19 | 601318 | 中国平安 | 1 | 动量质量 | 74.2119 | 5 |
| 20 | 601288 | 农业银行 | 1 | 动量质量 | 74.0859 | 6 |
| 21 | 300347 | 泰格医药 | 1 | 资金热度 | 74.0214 | 2 |
| 22 | 601328 | 交通银行 | 1 | 动量质量 | 73.7376 | 7 |
| 23 | 601988 | 中国银行 | 1 | 动量质量 | 73.7309 | 8 |
| 24 | 601939 | 建设银行 | 1 | 动量质量 | 73.6749 | 9 |
| 25 | 688372 | 伟测科技 | 1 | 资金热度 | 73.5953 | 3 |
| 26 | 300747 | 锐科激光 | 1 | 资金热度 | 73.5807 | 4 |
| 27 | 688777 | 中控技术 | 1 | 资金热度 | 73.3632 | 5 |
| 28 | 688268 | 华特气体 | 1 | 资金热度 | 73.2675 | 6 |
| 29 | 300395 | 菲利华 | 1 | 资金热度 | 73.1599 | 7 |
| 30 | 600030 | 中信证券 | 1 | 动量质量 | 73.1021 | 10 |

## 模型明细与原始候选字段

完整的每套模型返回结果、每只股票的原始候选字段和策略明细请以同目录的 `candidate_pool.json` 为准。

```json
[
  {
    "code": "601668",
    "name": "中国建筑",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 1,
    "best_score": 91.0962,
    "average_score": 91.0962,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 1,
        "score": 91.0962,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 1,
          "code": "601668",
          "name": "中国建筑",
          "score": 91.0962,
          "screen_score": 86.696208488665,
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
          "price": 4.33,
          "change_pct": -2.91,
          "amount": 1854856109.0,
          "industry": "",
          "factor_scores": {
            "value": 89.9915,
            "liquidity": 93.4509,
            "momentum": 47.0425,
            "reversal": 92.33,
            "activity": 78.1735,
            "stability": 69.27,
            "size": 97.4811,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "601668",
              "name": "中国建筑",
              "source": "tencent",
              "fetched_at": "2026-08-31T09:33:57.289717+00:00",
              "price": 4.33,
              "change_pct": -2.91,
              "change_amount": -0.13,
              "volume": 424728500,
              "amount": 1854856109.0,
              "volume_ratio": 2.12,
              "turnover_rate": 1.03,
              "amplitude": 3.14,
              "open_price": 4.43,
              "high": 4.46,
              "low": 4.32,
              "pre_close": 4.46,
              "pe_ratio": 5.65,
              "pb_ratio": 0.36,
              "total_mv": 178917000000.0,
              "circ_mv": 178917000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 4.33, 涨跌幅 -2.91%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 1,
            "code": "601668",
            "name": "中国建筑",
            "final_score": 91.0962,
            "screen_score": 86.696208488665,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 4.33,
            "change_pct": -2.91,
            "amount": 1854856109.0,
            "total_mv": 178917290623.0,
            "turnover_rate": 1.03,
            "volume_ratio": 2.12,
            "pe_ratio": 5.64953973,
            "pb_ratio": 0.36148723,
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
              "value": 89.9915,
              "liquidity": 93.4509,
              "momentum": 47.0425,
              "reversal": 92.33,
              "activity": 78.1735,
              "stability": 69.27,
              "size": 97.4811,
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
                "code": "601668",
                "name": "中国建筑",
                "source": "tencent",
                "fetched_at": "2026-08-31T09:33:57.289717+00:00",
                "price": 4.33,
                "change_pct": -2.91,
                "change_amount": -0.13,
                "volume": 424728500,
                "amount": 1854856109.0,
                "volume_ratio": 2.12,
                "turnover_rate": 1.03,
                "amplitude": 3.14,
                "open_price": 4.43,
                "high": 4.46,
                "low": 4.32,
                "pre_close": 4.46,
                "pe_ratio": 5.65,
                "pb_ratio": 0.36,
                "total_mv": 178917000000.0,
                "circ_mv": 178917000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 4.33, 涨跌幅 -2.91%",
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
    "code": "600585",
    "name": "海螺水泥",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 2,
    "best_score": 89.2919,
    "average_score": 89.2919,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 2,
        "score": 89.2919,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 2,
          "code": "600585",
          "name": "海螺水泥",
          "score": 89.2919,
          "screen_score": 84.89187744962217,
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
          "price": 17.65,
          "change_pct": -3.23,
          "amount": 715100165.0,
          "industry": "",
          "factor_scores": {
            "value": 83.9783,
            "liquidity": 80.1008,
            "momentum": 46.0025,
            "reversal": 96.49,
            "activity": 79.6536,
            "stability": 68.31,
            "size": 94.4584,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "600585",
              "name": "海螺水泥",
              "source": "tencent",
              "fetched_at": "2026-08-31T09:34:09.830664+00:00",
              "price": 17.65,
              "change_pct": -3.23,
              "change_amount": -0.59,
              "volume": 39907900,
              "amount": 715100165.0,
              "volume_ratio": 1.43,
              "turnover_rate": 1.0,
              "amplitude": 4.39,
              "open_price": 18.33,
              "high": 18.42,
              "low": 17.62,
              "pre_close": 18.24,
              "pe_ratio": 14.96,
              "pb_ratio": 0.49,
              "total_mv": 93140000000.0,
              "circ_mv": 70202000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 17.65, 涨跌幅 -3.23%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 2,
            "code": "600585",
            "name": "海螺水泥",
            "final_score": 89.2919,
            "screen_score": 84.89187744962217,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 17.65,
            "change_pct": -3.23,
            "amount": 715100165.0,
            "total_mv": 93140109777.0,
            "turnover_rate": 1.0,
            "volume_ratio": 1.43,
            "pe_ratio": 14.96115989,
            "pb_ratio": 0.48705111,
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
              "value": 83.9783,
              "liquidity": 80.1008,
              "momentum": 46.0025,
              "reversal": 96.49,
              "activity": 79.6536,
              "stability": 68.31,
              "size": 94.4584,
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
                "code": "600585",
                "name": "海螺水泥",
                "source": "tencent",
                "fetched_at": "2026-08-31T09:34:09.830664+00:00",
                "price": 17.65,
                "change_pct": -3.23,
                "change_amount": -0.59,
                "volume": 39907900,
                "amount": 715100165.0,
                "volume_ratio": 1.43,
                "turnover_rate": 1.0,
                "amplitude": 4.39,
                "open_price": 18.33,
                "high": 18.42,
                "low": 17.62,
                "pre_close": 18.24,
                "pe_ratio": 14.96,
                "pb_ratio": 0.49,
                "total_mv": 93140000000.0,
                "circ_mv": 70202000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 17.65, 涨跌幅 -3.23%",
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
    "code": "601117",
    "name": "中国化学",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 3,
    "best_score": 88.7167,
    "average_score": 88.7167,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 3,
        "score": 88.7167,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 3,
          "code": "601117",
          "name": "中国化学",
          "score": 88.7167,
          "screen_score": 84.3167208186398,
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
          "price": 7.44,
          "change_pct": -2.87,
          "amount": 784433966.0,
          "industry": "",
          "factor_scores": {
            "value": 89.108,
            "liquidity": 81.1083,
            "momentum": 47.1725,
            "reversal": 91.81,
            "activity": 80.9658,
            "stability": 69.39,
            "size": 87.1537,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "601117",
              "name": "中国化学",
              "source": "tencent",
              "fetched_at": "2026-08-31T09:34:20.262417+00:00",
              "price": 7.44,
              "change_pct": -2.87,
              "change_amount": -0.22,
              "volume": 105424700,
              "amount": 784433966.0,
              "volume_ratio": 2.06,
              "turnover_rate": 1.73,
              "amplitude": 1.96,
              "open_price": 7.5,
              "high": 7.54,
              "low": 7.39,
              "pre_close": 7.66,
              "pe_ratio": 7.01,
              "pb_ratio": 0.65,
              "total_mv": 45425000000.0,
              "circ_mv": 45295000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 7.44, 涨跌幅 -2.87%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 3,
            "code": "601117",
            "name": "中国化学",
            "final_score": 88.7167,
            "screen_score": 84.3167208186398,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 7.44,
            "change_pct": -2.87,
            "amount": 784433966.0,
            "total_mv": 45425371325.0,
            "turnover_rate": 1.73,
            "volume_ratio": 2.06,
            "pe_ratio": 7.01027057,
            "pb_ratio": 0.64511753,
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
              "value": 89.108,
              "liquidity": 81.1083,
              "momentum": 47.1725,
              "reversal": 91.81,
              "activity": 80.9658,
              "stability": 69.39,
              "size": 87.1537,
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
                "code": "601117",
                "name": "中国化学",
                "source": "tencent",
                "fetched_at": "2026-08-31T09:34:20.262417+00:00",
                "price": 7.44,
                "change_pct": -2.87,
                "change_amount": -0.22,
                "volume": 105424700,
                "amount": 784433966.0,
                "volume_ratio": 2.06,
                "turnover_rate": 1.73,
                "amplitude": 1.96,
                "open_price": 7.5,
                "high": 7.54,
                "low": 7.39,
                "pre_close": 7.66,
                "pe_ratio": 7.01,
                "pb_ratio": 0.65,
                "total_mv": 45425000000.0,
                "circ_mv": 45295000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 7.44, 涨跌幅 -2.87%",
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
    "code": "600352",
    "name": "浙江龙盛",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 4,
    "best_score": 86.1995,
    "average_score": 86.1995,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 4,
        "score": 86.1995,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 4,
          "code": "600352",
          "name": "浙江龙盛",
          "score": 86.1995,
          "screen_score": 84.19945221032745,
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
          "price": 12.74,
          "change_pct": -3.26,
          "amount": 1001461883.0,
          "industry": "",
          "factor_scores": {
            "value": 69.6395,
            "liquidity": 86.6499,
            "momentum": 45.905,
            "reversal": 96.88,
            "activity": 84.4026,
            "stability": 68.22,
            "size": 85.3904,
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
            "code": "600352",
            "name": "浙江龙盛",
            "final_score": 86.1995,
            "screen_score": 84.19945221032745,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 12.74,
            "change_pct": -3.26,
            "amount": 1001461883.0,
            "total_mv": 41447447896.0,
            "turnover_rate": 2.42,
            "volume_ratio": 1.35,
            "pe_ratio": 21.75549493,
            "pb_ratio": 1.29172747,
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
              "value": 69.6395,
              "liquidity": 86.6499,
              "momentum": 45.905,
              "reversal": 96.88,
              "activity": 84.4026,
              "stability": 68.22,
              "size": 85.3904,
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
    "code": "603345",
    "name": "安井食品",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 5,
    "best_score": 85.9235,
    "average_score": 85.9235,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 5,
        "score": 85.9235,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 5,
          "code": "603345",
          "name": "安井食品",
          "score": 85.9235,
          "screen_score": 83.9235250440806,
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
          "price": 74.91,
          "change_pct": -3.37,
          "amount": 802762102.0,
          "industry": "",
          "factor_scores": {
            "value": 69.8051,
            "liquidity": 82.1159,
            "momentum": 45.5475,
            "reversal": 98.31,
            "activity": 84.5309,
            "stability": 67.89,
            "size": 75.5668,
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
            "code": "603345",
            "name": "安井食品",
            "final_score": 85.9235,
            "screen_score": 83.9235250440806,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 74.91,
            "change_pct": -3.37,
            "amount": 802762102.0,
            "total_mv": 24966673896.0,
            "turnover_rate": 3.62,
            "volume_ratio": 1.41,
            "pe_ratio": 16.58492312,
            "pb_ratio": 1.57669569,
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
              "value": 69.8051,
              "liquidity": 82.1159,
              "momentum": 45.5475,
              "reversal": 98.31,
              "activity": 84.5309,
              "stability": 67.89,
              "size": 75.5668,
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
    "code": "002237",
    "name": "恒邦股份",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 6,
    "best_score": 84.3153,
    "average_score": 84.3153,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 6,
        "score": 84.3153,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 6,
          "code": "002237",
          "name": "恒邦股份",
          "score": 84.3153,
          "screen_score": 82.31525621536524,
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
          "price": 15.04,
          "change_pct": -3.65,
          "amount": 746473366.92,
          "industry": "",
          "factor_scores": {
            "value": 64.7188,
            "liquidity": 80.6045,
            "momentum": 44.6375,
            "reversal": 98.05,
            "activity": 80.3571,
            "stability": 67.05,
            "size": 70.529,
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
            "code": "002237",
            "name": "恒邦股份",
            "final_score": 84.3153,
            "screen_score": 82.31525621536524,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 15.04,
            "change_pct": -3.65,
            "amount": 746473366.92,
            "total_mv": 21506754936.0,
            "turnover_rate": 4.25,
            "volume_ratio": 0.99,
            "pe_ratio": 21.64067533,
            "pb_ratio": 1.5659592,
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
              "value": 64.7188,
              "liquidity": 80.6045,
              "momentum": 44.6375,
              "reversal": 98.05,
              "activity": 80.3571,
              "stability": 67.05,
              "size": 70.529,
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
    "code": "000932",
    "name": "华菱钢铁",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 7,
    "best_score": 84.2454,
    "average_score": 84.2454,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 7,
        "score": 84.2454,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 7,
          "code": "000932",
          "name": "华菱钢铁",
          "score": 84.2454,
          "screen_score": 82.24543801007557,
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
          "price": 3.63,
          "change_pct": -3.71,
          "amount": 533762007.83,
          "industry": "",
          "factor_scores": {
            "value": 74.6363,
            "liquidity": 72.0403,
            "momentum": 44.4425,
            "reversal": 97.27,
            "activity": 84.2395,
            "stability": 66.87,
            "size": 75.3149,
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
            "code": "000932",
            "name": "华菱钢铁",
            "final_score": 84.2454,
            "screen_score": 82.24543801007557,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 3.63,
            "change_pct": -3.71,
            "amount": 533762007.83,
            "total_mv": 24874971251.0,
            "turnover_rate": 2.11,
            "volume_ratio": 1.64,
            "pe_ratio": 22.86976742,
            "pb_ratio": 0.45502818,
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
              "value": 74.6363,
              "liquidity": 72.0403,
              "momentum": 44.4425,
              "reversal": 97.27,
              "activity": 84.2395,
              "stability": 66.87,
              "size": 75.3149,
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
    "code": "601799",
    "name": "星宇股份",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 8,
    "best_score": 84.1841,
    "average_score": 84.1841,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 8,
        "score": 84.1841,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 8,
          "code": "601799",
          "name": "星宇股份",
          "score": 84.1841,
          "screen_score": 82.18407579345089,
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
          "price": 78.39,
          "change_pct": -3.79,
          "amount": 805032190.0,
          "industry": "",
          "factor_scores": {
            "value": 66.0161,
            "liquidity": 82.6196,
            "momentum": 44.1825,
            "reversal": 96.23,
            "activity": 82.1995,
            "stability": 66.63,
            "size": 72.796,
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
            "code": "601799",
            "name": "星宇股份",
            "final_score": 84.1841,
            "screen_score": 82.18407579345089,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 78.39,
            "change_pct": -3.79,
            "amount": 805032190.0,
            "total_mv": 22394409655.0,
            "turnover_rate": 3.65,
            "volume_ratio": 2.28,
            "pe_ratio": 14.11148726,
            "pb_ratio": 1.97681453,
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
              "value": 66.0161,
              "liquidity": 82.6196,
              "momentum": 44.1825,
              "reversal": 96.23,
              "activity": 82.1995,
              "stability": 66.63,
              "size": 72.796,
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
    "code": "000975",
    "name": "山金国际",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 9,
    "best_score": 83.948,
    "average_score": 83.948,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 9,
        "score": 83.948,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 9,
          "code": "000975",
          "name": "山金国际",
          "score": 83.948,
          "screen_score": 81.94796086272041,
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
          "price": 26.35,
          "change_pct": -3.52,
          "amount": 1987896688.87,
          "industry": "",
          "factor_scores": {
            "value": 39.8996,
            "liquidity": 94.4584,
            "momentum": 45.06,
            "reversal": 99.74,
            "activity": 86.2919,
            "stability": 67.44,
            "size": 92.4433,
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
            "code": "000975",
            "name": "山金国际",
            "final_score": 83.948,
            "screen_score": 81.94796086272041,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 26.35,
            "change_pct": -3.52,
            "amount": 1987896688.87,
            "total_mv": 73056097939.0,
            "turnover_rate": 3.03,
            "volume_ratio": 1.33,
            "pe_ratio": 19.26381639,
            "pb_ratio": 4.5888532,
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
              "value": 39.8996,
              "liquidity": 94.4584,
              "momentum": 45.06,
              "reversal": 99.74,
              "activity": 86.2919,
              "stability": 67.44,
              "size": 92.4433,
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
    "code": "300724",
    "name": "捷佳伟创",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 10,
    "best_score": 83.3607,
    "average_score": 83.3607,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 10,
        "score": 83.3607,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 10,
          "code": "300724",
          "name": "捷佳伟创",
          "score": 83.3607,
          "screen_score": 81.3606528211587,
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
          "price": 56.39,
          "change_pct": -3.13,
          "amount": 574872835.18,
          "industry": "",
          "factor_scores": {
            "value": 71.0318,
            "liquidity": 73.2997,
            "momentum": 46.3275,
            "reversal": 95.19,
            "activity": 83.3935,
            "stability": 68.61,
            "size": 68.7657,
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
            "code": "300724",
            "name": "捷佳伟创",
            "final_score": 83.3607,
            "screen_score": 81.3606528211587,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 56.39,
            "change_pct": -3.13,
            "amount": 574872835.18,
            "total_mv": 19640186218.0,
            "turnover_rate": 3.52,
            "volume_ratio": 1.08,
            "pe_ratio": 16.90823173,
            "pb_ratio": 1.47745074,
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
              "value": 71.0318,
              "liquidity": 73.2997,
              "momentum": 46.3275,
              "reversal": 95.19,
              "activity": 83.3935,
              "stability": 68.61,
              "size": 68.7657,
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
    "code": "688018",
    "name": "乐鑫科技",
    "resonance_count": 1,
    "strategies": [
      "volume_breakout"
    ],
    "strategy_labels": [
      "放量突破"
    ],
    "best_rank": 1,
    "best_score": 79.2272,
    "average_score": 79.2272,
    "strategy_details": {
      "volume_breakout": {
        "rank": 1,
        "score": 79.2272,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 1,
          "code": "688018",
          "name": "乐鑫科技",
          "score": 79.2272,
          "screen_score": 77.027169296,
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
          "price": 125.69,
          "change_pct": 8.47,
          "amount": 1048096713.0,
          "industry": "",
          "factor_scores": {
            "value": 25.8274,
            "liquidity": 100.0,
            "momentum": 75.4922,
            "reversal": 5.0,
            "activity": 76.1703,
            "stability": 55.42,
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
              "code": "688018",
              "name": "乐鑫科技",
              "source": "tencent",
              "fetched_at": "2026-08-31T09:32:14.183525+00:00",
              "price": 125.69,
              "change_pct": 8.47,
              "change_amount": 9.81,
              "volume": 8555282,
              "amount": 1048096713.0,
              "volume_ratio": 2.34,
              "turnover_rate": 3.65,
              "amplitude": 10.42,
              "open_price": 114.21,
              "high": 126.28,
              "low": 114.21,
              "pre_close": 115.88,
              "pe_ratio": 51.61,
              "pb_ratio": 6.26,
              "total_mv": 29460000000.000004,
              "circ_mv": 29460000000.000004
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
          "dsa_analysis_summary": "DSA行情: 现价 125.69, 涨跌幅 8.47%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 1,
            "code": "688018",
            "name": "乐鑫科技",
            "final_score": 79.2272,
            "screen_score": 77.027169296,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 125.69,
            "change_pct": 8.47,
            "amount": 1048096713.0,
            "total_mv": 29459764050.0,
            "turnover_rate": 3.65,
            "volume_ratio": 2.34,
            "pe_ratio": 51.61099592,
            "pb_ratio": 6.26068071,
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
            "change_60d": 4.5239,
            "signal_score": 73.5834,
            "ma_bullish": false,
            "price_above_ma20": true,
            "macd_status": "bullish",
            "rsi_status": "neutral",
            "breakout_20d_pct": 6.725,
            "range_20d_pct": 23.2,
            "volume_ratio_20d": 1.7651,
            "body_pct": 10.0517,
            "pullback_to_ma20_pct": 11.7398,
            "consolidation_days_20d": 17,
            "volatility_20d_pct": 43.1254,
            "max_drawdown_20d_pct": -5.3813,
            "atr_20_pct": 3.8336,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:AkshareFetcher",
            "factor_scores": {
              "value": 25.8274,
              "liquidity": 100.0,
              "momentum": 75.4922,
              "reversal": 5.0,
              "activity": 76.1703,
              "stability": 55.42,
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
                "code": "688018",
                "name": "乐鑫科技",
                "source": "tencent",
                "fetched_at": "2026-08-31T09:32:14.183525+00:00",
                "price": 125.69,
                "change_pct": 8.47,
                "change_amount": 9.81,
                "volume": 8555282,
                "amount": 1048096713.0,
                "volume_ratio": 2.34,
                "turnover_rate": 3.65,
                "amplitude": 10.42,
                "open_price": 114.21,
                "high": 126.28,
                "low": 114.21,
                "pre_close": 115.88,
                "pe_ratio": 51.61,
                "pb_ratio": 6.26,
                "total_mv": 29460000000.000004,
                "circ_mv": 29460000000.000004
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
            "dsa_analysis_summary": "DSA行情: 现价 125.69, 涨跌幅 8.47%",
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
    "best_score": 77.5163,
    "average_score": 77.5163,
    "strategy_details": {
      "volume_breakout": {
        "rank": 2,
        "score": 77.5163,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 2,
          "code": "002292",
          "name": "奥飞娱乐",
          "score": 77.5163,
          "screen_score": 75.31633276876192,
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
          "price": 8.55,
          "change_pct": 5.95,
          "amount": 696153909.81,
          "industry": "",
          "factor_scores": {
            "value": 33.5625,
            "liquidity": 90.4762,
            "momentum": 73.2191,
            "reversal": 5.0,
            "activity": 77.6883,
            "stability": 62.2873,
            "size": 90.4762,
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
              "fetched_at": "2026-08-31T09:32:37.528525+00:00",
              "price": 8.55,
              "change_pct": 5.95,
              "change_amount": 0.48,
              "volume": 82783100,
              "amount": 696153910.0,
              "volume_ratio": 2.5,
              "turnover_rate": 8.13,
              "amplitude": 6.32,
              "open_price": 8.09,
              "high": 8.57,
              "low": 8.06,
              "pre_close": 8.07,
              "pe_ratio": 60.47,
              "pb_ratio": 4.17,
              "total_mv": 12643000000.0,
              "circ_mv": 8703000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 8.55, 涨跌幅 5.95%",
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
            "final_score": 77.5163,
            "screen_score": 75.31633276876192,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 8.55,
            "change_pct": 5.95,
            "amount": 696153909.81,
            "total_mv": 12642882409.0,
            "turnover_rate": 8.13,
            "volume_ratio": 2.5,
            "pe_ratio": 60.47295772,
            "pb_ratio": 4.17073961,
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
            "change_60d": 22.3176,
            "signal_score": 67.8112,
            "ma_bullish": false,
            "price_above_ma20": true,
            "macd_status": "neutral",
            "rsi_status": "neutral",
            "breakout_20d_pct": -0.2334,
            "range_20d_pct": 12.0261,
            "volume_ratio_20d": 2.0163,
            "body_pct": 5.686,
            "pullback_to_ma20_pct": 4.4594,
            "consolidation_days_20d": 11,
            "volatility_20d_pct": 39.5396,
            "max_drawdown_20d_pct": -8.1851,
            "atr_20_pct": 3.345,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:AkshareFetcher",
            "factor_scores": {
              "value": 33.5625,
              "liquidity": 90.4762,
              "momentum": 73.2191,
              "reversal": 5.0,
              "activity": 77.6883,
              "stability": 62.2873,
              "size": 90.4762,
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
                "fetched_at": "2026-08-31T09:32:37.528525+00:00",
                "price": 8.55,
                "change_pct": 5.95,
                "change_amount": 0.48,
                "volume": 82783100,
                "amount": 696153910.0,
                "volume_ratio": 2.5,
                "turnover_rate": 8.13,
                "amplitude": 6.32,
                "open_price": 8.09,
                "high": 8.57,
                "low": 8.06,
                "pre_close": 8.07,
                "pe_ratio": 60.47,
                "pb_ratio": 4.17,
                "total_mv": 12643000000.0,
                "circ_mv": 8703000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 8.55, 涨跌幅 5.95%",
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
    "best_rank": 1,
    "best_score": 76.4019,
    "average_score": 76.4019,
    "strategy_details": {
      "momentum_quality": {
        "rank": 1,
        "score": 76.4019,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 1,
          "code": "601169",
          "name": "北京银行",
          "score": 76.4019,
          "screen_score": 74.00191423449613,
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
          "price": 5.35,
          "change_pct": 5.11,
          "amount": 3143131155.0,
          "industry": "",
          "factor_scores": {
            "value": 89.7223,
            "liquidity": 96.124,
            "momentum": 72.1065,
            "reversal": 5.0,
            "activity": 71.0234,
            "stability": 62.67,
            "size": 83.876,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "601169",
              "name": "北京银行",
              "source": "tencent",
              "fetched_at": "2026-08-31T09:33:27.055626+00:00",
              "price": 5.35,
              "change_pct": 5.11,
              "change_amount": 0.26,
              "volume": 591613200,
              "amount": 3143131155.0,
              "volume_ratio": 4.51,
              "turnover_rate": 2.8,
              "amplitude": 3.73,
              "open_price": 5.2,
              "high": 5.38,
              "low": 5.19,
              "pre_close": 5.09,
              "pe_ratio": 5.4,
              "pb_ratio": 0.4,
              "total_mv": 113115000000.00002,
              "circ_mv": 113115000000.00002
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
          "dsa_analysis_summary": "DSA行情: 现价 5.35, 涨跌幅 5.11%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 1,
            "code": "601169",
            "name": "北京银行",
            "final_score": 76.4019,
            "screen_score": 74.00191423449613,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 5.35,
            "change_pct": 5.11,
            "amount": 3143131155.0,
            "total_mv": 113114965855.0,
            "turnover_rate": 2.8,
            "volume_ratio": 4.51,
            "pe_ratio": 5.40366722,
            "pb_ratio": 0.39680273,
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
              "value": 89.7223,
              "liquidity": 96.124,
              "momentum": 72.1065,
              "reversal": 5.0,
              "activity": 71.0234,
              "stability": 62.67,
              "size": 83.876,
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
                "code": "601169",
                "name": "北京银行",
                "source": "tencent",
                "fetched_at": "2026-08-31T09:33:27.055626+00:00",
                "price": 5.35,
                "change_pct": 5.11,
                "change_amount": 0.26,
                "volume": 591613200,
                "amount": 3143131155.0,
                "volume_ratio": 4.51,
                "turnover_rate": 2.8,
                "amplitude": 3.73,
                "open_price": 5.2,
                "high": 5.38,
                "low": 5.19,
                "pre_close": 5.09,
                "pe_ratio": 5.4,
                "pb_ratio": 0.4,
                "total_mv": 113115000000.00002,
                "circ_mv": 113115000000.00002
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
            "dsa_analysis_summary": "DSA行情: 现价 5.35, 涨跌幅 5.11%",
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
    "code": "600547",
    "name": "山东黄金",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 1,
    "best_score": 76.3309,
    "average_score": 76.3309,
    "strategy_details": {
      "capital_heat": {
        "rank": 1,
        "score": 76.3309,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 1,
          "code": "600547",
          "name": "山东黄金",
          "score": 76.3309,
          "screen_score": 73.93092889610391,
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
          "price": 37.85,
          "change_pct": 6.65,
          "amount": 7041882533.0,
          "industry": "",
          "factor_scores": {
            "value": 56.6883,
            "liquidity": 99.3506,
            "momentum": 76.9425,
            "reversal": 5.0,
            "activity": 80.0294,
            "stability": 58.05,
            "size": 99.3506,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "600547",
              "name": "山东黄金",
              "source": "tencent",
              "fetched_at": "2026-08-31T09:32:50.107299+00:00",
              "price": 37.85,
              "change_pct": 6.65,
              "change_amount": 2.36,
              "volume": 194958600,
              "amount": 7041882533.0,
              "volume_ratio": 1.61,
              "turnover_rate": 5.39,
              "amplitude": 12.65,
              "open_price": 33.67,
              "high": 38.09,
              "low": 33.6,
              "pre_close": 35.49,
              "pe_ratio": 31.87,
              "pb_ratio": 5.34,
              "total_mv": 174486000000.0,
              "circ_mv": 136807000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 37.85, 涨跌幅 6.65%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 1,
            "code": "600547",
            "name": "山东黄金",
            "final_score": 76.3309,
            "screen_score": 73.93092889610391,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 37.85,
            "change_pct": 6.65,
            "amount": 7041882533.0,
            "total_mv": 174485832521.0,
            "turnover_rate": 5.39,
            "volume_ratio": 1.61,
            "pe_ratio": 31.87334596,
            "pb_ratio": 5.26642639,
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
              "value": 56.6883,
              "liquidity": 99.3506,
              "momentum": 76.9425,
              "reversal": 5.0,
              "activity": 80.0294,
              "stability": 58.05,
              "size": 99.3506,
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
                "code": "600547",
                "name": "山东黄金",
                "source": "tencent",
                "fetched_at": "2026-08-31T09:32:50.107299+00:00",
                "price": 37.85,
                "change_pct": 6.65,
                "change_amount": 2.36,
                "volume": 194958600,
                "amount": 7041882533.0,
                "volume_ratio": 1.61,
                "turnover_rate": 5.39,
                "amplitude": 12.65,
                "open_price": 33.67,
                "high": 38.09,
                "low": 33.6,
                "pre_close": 35.49,
                "pe_ratio": 31.87,
                "pb_ratio": 5.34,
                "total_mv": 174486000000.0,
                "circ_mv": 136807000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 37.85, 涨跌幅 6.65%",
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
    "code": "002092",
    "name": "中泰化学",
    "resonance_count": 1,
    "strategies": [
      "volume_breakout"
    ],
    "strategy_labels": [
      "放量突破"
    ],
    "best_rank": 3,
    "best_score": 76.0502,
    "average_score": 76.0502,
    "strategy_details": {
      "volume_breakout": {
        "rank": 3,
        "score": 76.0502,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 3,
          "code": "002092",
          "name": "中泰化学",
          "score": 76.0502,
          "screen_score": 76.85022413714286,
          "reason": "本地后置评分: capital_confirmed",
          "risk_level": "low",
          "risk_flags": [
            "negative_or_invalid_pe"
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
          "price": 4.9,
          "change_pct": 2.08,
          "amount": 686270112.44,
          "industry": "",
          "factor_scores": {
            "value": 63.5625,
            "liquidity": 85.7143,
            "momentum": 76.6,
            "reversal": 25.32,
            "activity": 84.4278,
            "stability": 58.413,
            "size": 85.7143,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "002092",
              "name": "中泰化学",
              "source": "tencent",
              "fetched_at": "2026-08-31T09:32:24.596625+00:00",
              "price": 4.9,
              "change_pct": 2.08,
              "change_amount": 0.1,
              "volume": 141456100,
              "amount": 686270112.0,
              "volume_ratio": 2.7,
              "turnover_rate": 5.49,
              "amplitude": 6.25,
              "open_price": 4.82,
              "high": 4.96,
              "low": 4.66,
              "pre_close": 4.8,
              "pe_ratio": -638.16,
              "pb_ratio": 0.59,
              "total_mv": 12621000000.0,
              "circ_mv": 12621000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 4.9, 涨跌幅 2.08%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 3,
            "code": "002092",
            "name": "中泰化学",
            "final_score": 76.0502,
            "screen_score": 76.85022413714286,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 4.9,
            "change_pct": 2.08,
            "amount": 686270112.44,
            "total_mv": 12621123633.0,
            "turnover_rate": 5.49,
            "volume_ratio": 2.7,
            "pe_ratio": -638.16087261,
            "pb_ratio": 0.58434772,
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
            "change_60d": 7.9295,
            "signal_score": 88.7753,
            "ma_bullish": true,
            "price_above_ma20": true,
            "macd_status": "bullish",
            "rsi_status": "neutral",
            "breakout_20d_pct": 1.6598,
            "range_20d_pct": 14.023,
            "volume_ratio_20d": 2.6863,
            "body_pct": 1.6598,
            "pullback_to_ma20_pct": 8.2634,
            "consolidation_days_20d": 20,
            "volatility_20d_pct": 29.503,
            "max_drawdown_20d_pct": -5.3996,
            "atr_20_pct": 2.9388,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:AkshareFetcher",
            "factor_scores": {
              "value": 63.5625,
              "liquidity": 85.7143,
              "momentum": 76.6,
              "reversal": 25.32,
              "activity": 84.4278,
              "stability": 58.413,
              "size": 85.7143,
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
              "negative_or_invalid_pe"
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
                "code": "002092",
                "name": "中泰化学",
                "source": "tencent",
                "fetched_at": "2026-08-31T09:32:24.596625+00:00",
                "price": 4.9,
                "change_pct": 2.08,
                "change_amount": 0.1,
                "volume": 141456100,
                "amount": 686270112.0,
                "volume_ratio": 2.7,
                "turnover_rate": 5.49,
                "amplitude": 6.25,
                "open_price": 4.82,
                "high": 4.96,
                "low": 4.66,
                "pre_close": 4.8,
                "pe_ratio": -638.16,
                "pb_ratio": 0.59,
                "total_mv": 12621000000.0,
                "circ_mv": 12621000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 4.9, 涨跌幅 2.08%",
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
    "best_score": 75.302,
    "average_score": 75.302,
    "strategy_details": {
      "momentum_quality": {
        "rank": 2,
        "score": 75.302,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 2,
          "code": "600036",
          "name": "招商银行",
          "score": 75.302,
          "screen_score": 73.50197335271316,
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
          "price": 40.12,
          "change_pct": 1.96,
          "amount": 4545240512.0,
          "industry": "",
          "factor_scores": {
            "value": 85.501,
            "liquidity": 98.2946,
            "momentum": 62.87,
            "reversal": 27.84,
            "activity": 70.9548,
            "stability": 72.12,
            "size": 98.4496,
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
              "fetched_at": "2026-08-31T09:33:46.585312+00:00",
              "price": 40.12,
              "change_pct": 1.96,
              "change_amount": 0.77,
              "volume": 113625100,
              "amount": 4545240512.0,
              "volume_ratio": 1.66,
              "turnover_rate": 0.55,
              "amplitude": 1.98,
              "open_price": 39.51,
              "high": 40.28,
              "low": 39.5,
              "pre_close": 39.35,
              "pe_ratio": 6.67,
              "pb_ratio": 0.88,
              "total_mv": 1011820000000.0001,
              "circ_mv": 827633000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 40.12, 涨跌幅 1.96%",
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
            "final_score": 75.302,
            "screen_score": 73.50197335271316,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 40.12,
            "change_pct": 1.96,
            "amount": 4545240512.0,
            "total_mv": 1011820205512.0,
            "turnover_rate": 0.55,
            "volume_ratio": 1.66,
            "pe_ratio": 6.67005198,
            "pb_ratio": 0.88365181,
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
              "value": 85.501,
              "liquidity": 98.2946,
              "momentum": 62.87,
              "reversal": 27.84,
              "activity": 70.9548,
              "stability": 72.12,
              "size": 98.4496,
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
                "fetched_at": "2026-08-31T09:33:46.585312+00:00",
                "price": 40.12,
                "change_pct": 1.96,
                "change_amount": 0.77,
                "volume": 113625100,
                "amount": 4545240512.0,
                "volume_ratio": 1.66,
                "turnover_rate": 0.55,
                "amplitude": 1.98,
                "open_price": 39.51,
                "high": 40.28,
                "low": 39.5,
                "pre_close": 39.35,
                "pe_ratio": 6.67,
                "pb_ratio": 0.88,
                "total_mv": 1011820000000.0001,
                "circ_mv": 827633000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 40.12, 涨跌幅 1.96%",
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
    "best_score": 74.6624,
    "average_score": 74.6624,
    "strategy_details": {
      "momentum_quality": {
        "rank": 3,
        "score": 74.6624,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 3,
          "code": "601166",
          "name": "兴业银行",
          "score": 74.6624,
          "screen_score": 72.86239854651161,
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
          "price": 17.54,
          "change_pct": 0.63,
          "amount": 2272753848.0,
          "industry": "",
          "factor_scores": {
            "value": 89.6793,
            "liquidity": 92.5581,
            "momentum": 58.5475,
            "reversal": 52.81,
            "activity": 67.9038,
            "stability": 76.11,
            "size": 96.2791,
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
            "code": "601166",
            "name": "兴业银行",
            "final_score": 74.6624,
            "screen_score": 72.86239854651161,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 17.54,
            "change_pct": 0.63,
            "amount": 2272753848.0,
            "total_mv": 371196555858.0,
            "turnover_rate": 0.61,
            "volume_ratio": 0.94,
            "pe_ratio": 4.91918202,
            "pb_ratio": 0.4439205,
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
              "value": 89.6793,
              "liquidity": 92.5581,
              "momentum": 58.5475,
              "reversal": 52.81,
              "activity": 67.9038,
              "stability": 76.11,
              "size": 96.2791,
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
    "best_score": 74.5814,
    "average_score": 74.5814,
    "strategy_details": {
      "momentum_quality": {
        "rank": 4,
        "score": 74.5814,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 4,
          "code": "601398",
          "name": "工商银行",
          "score": 74.5814,
          "screen_score": 72.7813703488372,
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
          "change_pct": 2.67,
          "amount": 3227091269.0,
          "industry": "",
          "factor_scores": {
            "value": 86.5246,
            "liquidity": 96.7442,
            "momentum": 65.1775,
            "reversal": 12.93,
            "activity": 68.1535,
            "stability": 69.99,
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
            "final_score": 74.5814,
            "screen_score": 72.7813703488372,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 8.07,
            "change_pct": 2.67,
            "amount": 3227091269.0,
            "total_mv": 2876198494708.0,
            "turnover_rate": 0.15,
            "volume_ratio": 1.36,
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
              "value": 86.5246,
              "liquidity": 96.7442,
              "momentum": 65.1775,
              "reversal": 12.93,
              "activity": 68.1535,
              "stability": 69.99,
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
    "code": "601318",
    "name": "中国平安",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 5,
    "best_score": 74.2119,
    "average_score": 74.2119,
    "strategy_details": {
      "momentum_quality": {
        "rank": 5,
        "score": 74.2119,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 5,
          "code": "601318",
          "name": "中国平安",
          "score": 74.2119,
          "screen_score": 72.41190019379843,
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
          "price": 55.82,
          "change_pct": -0.05,
          "amount": 3052052822.0,
          "industry": "",
          "factor_scores": {
            "value": 84.4114,
            "liquidity": 95.969,
            "momentum": 56.3375,
            "reversal": 61.65,
            "activity": 66.1825,
            "stability": 77.85,
            "size": 98.2946,
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
            "code": "601318",
            "name": "中国平安",
            "final_score": 74.2119,
            "screen_score": 72.41190019379843,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 55.82,
            "change_pct": -0.05,
            "amount": 3052052822.0,
            "total_mv": 1010768576161.0,
            "turnover_rate": 0.51,
            "volume_ratio": 0.64,
            "pe_ratio": 6.34442602,
            "pb_ratio": 0.98315758,
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
              "value": 84.4114,
              "liquidity": 95.969,
              "momentum": 56.3375,
              "reversal": 61.65,
              "activity": 66.1825,
              "stability": 77.85,
              "size": 98.2946,
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
    "best_rank": 6,
    "best_score": 74.0859,
    "average_score": 74.0859,
    "strategy_details": {
      "momentum_quality": {
        "rank": 6,
        "score": 74.0859,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 6,
          "code": "601288",
          "name": "农业银行",
          "score": 74.0859,
          "screen_score": 72.2858796996124,
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
          "price": 6.92,
          "change_pct": 1.91,
          "amount": 2725430832.0,
          "industry": "",
          "factor_scores": {
            "value": 85.1866,
            "liquidity": 94.5736,
            "momentum": 62.7075,
            "reversal": 28.89,
            "activity": 67.3649,
            "stability": 72.27,
            "size": 99.6899,
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
            "final_score": 74.0859,
            "screen_score": 72.2858796996124,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 6.92,
            "change_pct": 1.91,
            "amount": 2725430832.0,
            "total_mv": 2421882594401.0,
            "turnover_rate": 0.12,
            "volume_ratio": 1.21,
            "pe_ratio": 8.12952346,
            "pb_ratio": 0.84740054,
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
              "value": 85.1866,
              "liquidity": 94.5736,
              "momentum": 62.7075,
              "reversal": 28.89,
              "activity": 67.3649,
              "stability": 72.27,
              "size": 99.6899,
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
    "code": "300347",
    "name": "泰格医药",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 2,
    "best_score": 74.0214,
    "average_score": 74.0214,
    "strategy_details": {
      "capital_heat": {
        "rank": 2,
        "score": 74.0214,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 2,
          "code": "300347",
          "name": "泰格医药",
          "score": 74.0214,
          "screen_score": 71.62143350649352,
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
          "price": 52.79,
          "change_pct": 5.9,
          "amount": 1639283360.8,
          "industry": "",
          "factor_scores": {
            "value": 43.7677,
            "liquidity": 84.4156,
            "momentum": 75.675,
            "reversal": 5.0,
            "activity": 80.9605,
            "stability": 60.3,
            "size": 87.013,
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
            "rank": 2,
            "code": "300347",
            "name": "泰格医药",
            "final_score": 74.0214,
            "screen_score": 71.62143350649352,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 52.79,
            "change_pct": 5.9,
            "amount": 1639283360.8,
            "total_mv": 45453565180.0,
            "turnover_rate": 5.51,
            "volume_ratio": 1.72,
            "pe_ratio": 497.33946063,
            "pb_ratio": 2.33367857,
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
              "value": 43.7677,
              "liquidity": 84.4156,
              "momentum": 75.675,
              "reversal": 5.0,
              "activity": 80.9605,
              "stability": 60.3,
              "size": 87.013,
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
    "best_rank": 7,
    "best_score": 73.7376,
    "average_score": 73.7376,
    "strategy_details": {
      "momentum_quality": {
        "rank": 7,
        "score": 73.7376,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 7,
          "code": "601328",
          "name": "交通银行",
          "score": 73.7376,
          "screen_score": 71.93762088178292,
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
          "price": 7.24,
          "change_pct": 1.97,
          "amount": 1542217037.0,
          "industry": "",
          "factor_scores": {
            "value": 88.1378,
            "liquidity": 87.1318,
            "momentum": 62.9025,
            "reversal": 27.63,
            "activity": 71.4276,
            "stability": 72.09,
            "size": 97.5194,
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
            "code": "601328",
            "name": "交通银行",
            "final_score": 73.7376,
            "screen_score": 71.93762088178292,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 7.24,
            "change_pct": 1.97,
            "amount": 1542217037.0,
            "total_mv": 639753797775.0,
            "turnover_rate": 0.82,
            "volume_ratio": 1.55,
            "pe_ratio": 6.56292365,
            "pb_ratio": 0.54780946,
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
              "value": 88.1378,
              "liquidity": 87.1318,
              "momentum": 62.9025,
              "reversal": 27.63,
              "activity": 71.4276,
              "stability": 72.09,
              "size": 97.5194,
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
    "best_rank": 8,
    "best_score": 73.7309,
    "average_score": 73.7309,
    "strategy_details": {
      "momentum_quality": {
        "rank": 8,
        "score": 73.7309,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 8,
          "code": "601988",
          "name": "中国银行",
          "score": 73.7309,
          "screen_score": 73.73093108527132,
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
          "price": 6.51,
          "change_pct": 5.17,
          "amount": 3198569046.0,
          "industry": "",
          "factor_scores": {
            "value": 85.913,
            "liquidity": 96.5891,
            "momentum": 71.7555,
            "reversal": 5.0,
            "activity": 71.2,
            "stability": 62.49,
            "size": 99.3798,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "601988",
              "name": "中国银行",
              "source": "tencent",
              "fetched_at": "2026-08-31T09:33:36.681253+00:00",
              "price": 6.51,
              "change_pct": 5.17,
              "change_amount": 0.32,
              "volume": 497716900,
              "amount": 3198569046.0,
              "volume_ratio": 1.96,
              "turnover_rate": 0.24,
              "amplitude": 4.68,
              "open_price": 6.24,
              "high": 6.52,
              "low": 6.23,
              "pre_close": 6.19,
              "pe_ratio": 8.42,
              "pb_ratio": 0.76,
              "total_mv": 2097603000000.0,
              "circ_mv": 1372084000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 6.51, 涨跌幅 5.17%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: 未发现额外加分项"
          },
          "post_analysis_tags": [],
          "raw": {
            "rank": 8,
            "code": "601988",
            "name": "中国银行",
            "final_score": 73.7309,
            "screen_score": 73.73093108527132,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 6.51,
            "change_pct": 5.17,
            "amount": 3198569046.0,
            "total_mv": 2097602800909.0,
            "turnover_rate": 0.24,
            "volume_ratio": 1.96,
            "pe_ratio": 8.42329575,
            "pb_ratio": 0.76257304,
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
              "value": 85.913,
              "liquidity": 96.5891,
              "momentum": 71.7555,
              "reversal": 5.0,
              "activity": 71.2,
              "stability": 62.49,
              "size": 99.3798,
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
                "code": "601988",
                "name": "中国银行",
                "source": "tencent",
                "fetched_at": "2026-08-31T09:33:36.681253+00:00",
                "price": 6.51,
                "change_pct": 5.17,
                "change_amount": 0.32,
                "volume": 497716900,
                "amount": 3198569046.0,
                "volume_ratio": 1.96,
                "turnover_rate": 0.24,
                "amplitude": 4.68,
                "open_price": 6.24,
                "high": 6.52,
                "low": 6.23,
                "pre_close": 6.19,
                "pe_ratio": 8.42,
                "pb_ratio": 0.76,
                "total_mv": 2097603000000.0,
                "circ_mv": 1372084000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 6.51, 涨跌幅 5.17%",
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
    "best_rank": 9,
    "best_score": 73.6749,
    "average_score": 73.6749,
    "strategy_details": {
      "momentum_quality": {
        "rank": 9,
        "score": 73.6749,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 9,
          "code": "601939",
          "name": "建设银行",
          "score": 73.6749,
          "screen_score": 71.8748718992248,
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
          "price": 10.98,
          "change_pct": 2.71,
          "amount": 1633578724.0,
          "industry": "",
          "factor_scores": {
            "value": 85.5498,
            "liquidity": 88.3721,
            "momentum": 65.3075,
            "reversal": 12.09,
            "activity": 73.2295,
            "stability": 69.87,
            "size": 99.845,
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
            "code": "601939",
            "name": "建设银行",
            "final_score": 73.6749,
            "screen_score": 71.8748718992248,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 10.98,
            "change_pct": 2.71,
            "amount": 1633578724.0,
            "total_mv": 2872372188420.0,
            "turnover_rate": 1.56,
            "volume_ratio": 1.36,
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
              "value": 85.5498,
              "liquidity": 88.3721,
              "momentum": 65.3075,
              "reversal": 12.09,
              "activity": 73.2295,
              "stability": 69.87,
              "size": 99.845,
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
    "code": "688372",
    "name": "伟测科技",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 3,
    "best_score": 73.5953,
    "average_score": 73.5953,
    "strategy_details": {
      "capital_heat": {
        "rank": 3,
        "score": 73.5953,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 3,
          "code": "688372",
          "name": "伟测科技",
          "score": 73.5953,
          "screen_score": 71.1952601948052,
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
          "price": 130.72,
          "change_pct": 6.25,
          "amount": 1519590331.0,
          "industry": "",
          "factor_scores": {
            "value": 46.1297,
            "liquidity": 82.4675,
            "momentum": 76.8125,
            "reversal": 5.0,
            "activity": 79.6266,
            "stability": 59.25,
            "size": 74.6753,
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
            "code": "688372",
            "name": "伟测科技",
            "final_score": 73.5953,
            "screen_score": 71.1952601948052,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 130.72,
            "change_pct": 6.25,
            "amount": 1519590331.0,
            "total_mv": 22091226402.0,
            "turnover_rate": 7.1,
            "volume_ratio": 1.91,
            "pe_ratio": 61.12150201,
            "pb_ratio": 5.22508625,
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
              "value": 46.1297,
              "liquidity": 82.4675,
              "momentum": 76.8125,
              "reversal": 5.0,
              "activity": 79.6266,
              "stability": 59.25,
              "size": 74.6753,
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
    "code": "300747",
    "name": "锐科激光",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 4,
    "best_score": 73.5807,
    "average_score": 73.5807,
    "strategy_details": {
      "capital_heat": {
        "rank": 4,
        "score": 73.5807,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 4,
          "code": "300747",
          "name": "锐科激光",
          "score": 73.5807,
          "screen_score": 71.18068246753249,
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
          "price": 39.76,
          "change_pct": 5.8,
          "amount": 1200534126.91,
          "industry": "",
          "factor_scores": {
            "value": 35.3842,
            "liquidity": 77.9221,
            "momentum": 75.35,
            "reversal": 5.0,
            "activity": 83.3613,
            "stability": 60.6,
            "size": 75.3247,
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
            "code": "300747",
            "name": "锐科激光",
            "final_score": 73.5807,
            "screen_score": 71.18068246753249,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 39.76,
            "change_pct": 5.8,
            "amount": 1200534126.91,
            "total_mv": 22329216000.0,
            "turnover_rate": 5.95,
            "volume_ratio": 1.9,
            "pe_ratio": 90.13452552,
            "pb_ratio": 6.30835238,
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
              "value": 35.3842,
              "liquidity": 77.9221,
              "momentum": 75.35,
              "reversal": 5.0,
              "activity": 83.3613,
              "stability": 60.6,
              "size": 75.3247,
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
    "code": "688777",
    "name": "中控技术",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 5,
    "best_score": 73.3632,
    "average_score": 73.3632,
    "strategy_details": {
      "capital_heat": {
        "rank": 5,
        "score": 73.3632,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 5,
          "code": "688777",
          "name": "中控技术",
          "score": 73.3632,
          "screen_score": 70.96317012987014,
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
          "price": 97.81,
          "change_pct": 6.15,
          "amount": 2516484874.0,
          "industry": "",
          "factor_scores": {
            "value": 20.0947,
            "liquidity": 88.3117,
            "momentum": 76.4875,
            "reversal": 5.0,
            "activity": 75.7225,
            "stability": 59.55,
            "size": 94.8052,
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
            "code": "688777",
            "name": "中控技术",
            "final_score": 73.3632,
            "screen_score": 70.96317012987014,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 97.81,
            "change_pct": 6.15,
            "amount": 2516484874.0,
            "total_mv": 77386247636.0,
            "turnover_rate": 3.45,
            "volume_ratio": 2.2,
            "pe_ratio": 319.14249962,
            "pb_ratio": 7.8527353,
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
              "value": 20.0947,
              "liquidity": 88.3117,
              "momentum": 76.4875,
              "reversal": 5.0,
              "activity": 75.7225,
              "stability": 59.55,
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
    "code": "688268",
    "name": "华特气体",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 6,
    "best_score": 73.2675,
    "average_score": 73.2675,
    "strategy_details": {
      "capital_heat": {
        "rank": 6,
        "score": 73.2675,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 6,
          "code": "688268",
          "name": "华特气体",
          "score": 73.2675,
          "screen_score": 70.86749967532468,
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
          "price": 153.57,
          "change_pct": 6.5,
          "amount": 1243263980.0,
          "industry": "",
          "factor_scores": {
            "value": 28.6377,
            "liquidity": 79.2208,
            "momentum": 77.625,
            "reversal": 5.0,
            "activity": 79.6506,
            "stability": 58.5,
            "size": 71.4286,
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
            "code": "688268",
            "name": "华特气体",
            "final_score": 73.2675,
            "screen_score": 70.86749967532468,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 153.57,
            "change_pct": 6.5,
            "amount": 1243263980.0,
            "total_mv": 19608130576.0,
            "turnover_rate": 6.69,
            "volume_ratio": 1.59,
            "pe_ratio": 130.47842802,
            "pb_ratio": 7.37114604,
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
              "value": 28.6377,
              "liquidity": 79.2208,
              "momentum": 77.625,
              "reversal": 5.0,
              "activity": 79.6506,
              "stability": 58.5,
              "size": 71.4286,
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
    "code": "300395",
    "name": "菲利华",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 7,
    "best_score": 73.1599,
    "average_score": 73.1599,
    "strategy_details": {
      "capital_heat": {
        "rank": 7,
        "score": 73.1599,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 7,
          "code": "300395",
          "name": "菲利华",
          "score": 73.1599,
          "screen_score": 72.75987064935066,
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
          "price": 95.5,
          "change_pct": 6.36,
          "amount": 3140839916.96,
          "industry": "",
          "factor_scores": {
            "value": 28.2501,
            "liquidity": 91.5584,
            "momentum": 77.17,
            "reversal": 5.0,
            "activity": 79.729,
            "stability": 58.92,
            "size": 90.2597,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "300395",
              "name": "菲利华",
              "source": "tencent",
              "fetched_at": "2026-08-31T09:33:03.224130+00:00",
              "price": 95.5,
              "change_pct": 6.36,
              "change_amount": 5.71,
              "volume": 33739300,
              "amount": 3140839917.0,
              "volume_ratio": 1.52,
              "turnover_rate": 6.58,
              "amplitude": 8.84,
              "open_price": 88.75,
              "high": 95.5,
              "low": 87.56,
              "pre_close": 89.79,
              "pe_ratio": 97.25,
              "pb_ratio": 9.59,
              "total_mv": 50207000000.0,
              "circ_mv": 48947000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 95.5, 涨跌幅 6.36%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 7,
            "code": "300395",
            "name": "菲利华",
            "final_score": 73.1599,
            "screen_score": 72.75987064935066,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 95.5,
            "change_pct": 6.36,
            "amount": 3140839916.96,
            "total_mv": 50206936331.0,
            "turnover_rate": 6.58,
            "volume_ratio": 1.52,
            "pe_ratio": 97.25470209,
            "pb_ratio": 9.58590303,
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
              "value": 28.2501,
              "liquidity": 91.5584,
              "momentum": 77.17,
              "reversal": 5.0,
              "activity": 79.729,
              "stability": 58.92,
              "size": 90.2597,
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
                "code": "300395",
                "name": "菲利华",
                "source": "tencent",
                "fetched_at": "2026-08-31T09:33:03.224130+00:00",
                "price": 95.5,
                "change_pct": 6.36,
                "change_amount": 5.71,
                "volume": 33739300,
                "amount": 3140839917.0,
                "volume_ratio": 1.52,
                "turnover_rate": 6.58,
                "amplitude": 8.84,
                "open_price": 88.75,
                "high": 95.5,
                "low": 87.56,
                "pre_close": 89.79,
                "pe_ratio": 97.25,
                "pb_ratio": 9.59,
                "total_mv": 50207000000.0,
                "circ_mv": 48947000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 95.5, 涨跌幅 6.36%",
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
    "best_rank": 10,
    "best_score": 73.1021,
    "average_score": 73.1021,
    "strategy_details": {
      "momentum_quality": {
        "rank": 10,
        "score": 73.1021,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 10,
          "code": "600030",
          "name": "中信证券",
          "score": 73.1021,
          "screen_score": 71.30205460271316,
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
          "price": 27.8,
          "change_pct": -0.47,
          "amount": 3147754952.0,
          "industry": "",
          "factor_scores": {
            "value": 75.8676,
            "liquidity": 96.2791,
            "momentum": 54.9725,
            "reversal": 67.11,
            "activity": 69.2826,
            "stability": 76.59,
            "size": 96.5891,
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
            "code": "600030",
            "name": "中信证券",
            "final_score": 73.1021,
            "screen_score": 71.30205460271316,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 27.8,
            "change_pct": -0.47,
            "amount": 3147754952.0,
            "total_mv": 434354767494.0,
            "turnover_rate": 0.93,
            "volume_ratio": 0.99,
            "pe_ratio": 10.95313229,
            "pb_ratio": 1.4700255,
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
              "value": 75.8676,
              "liquidity": 96.2791,
              "momentum": 54.9725,
              "reversal": 67.11,
              "activity": 69.2826,
              "stability": 76.59,
              "size": 96.5891,
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
  }
]
```
