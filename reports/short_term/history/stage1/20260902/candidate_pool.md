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
| 1 | 000519 | 中兵红箭 | 2 | 放量突破、资金热度 | 69.58295 | 4 |
| 2 | 000783 | 长江证券 | 1 | 超跌反转 | 91.4018 | 1 |
| 3 | 601233 | 桐昆股份 | 1 | 超跌反转 | 90.96 | 2 |
| 4 | 603799 | 华友钴业 | 1 | 超跌反转 | 90.8107 | 3 |
| 5 | 000425 | 徐工机械 | 1 | 超跌反转 | 90.1237 | 4 |
| 6 | 600362 | 江西铜业 | 1 | 超跌反转 | 88.0563 | 5 |
| 7 | 600096 | 云天化 | 1 | 超跌反转 | 87.2109 | 6 |
| 8 | 000060 | 中金岭南 | 1 | 超跌反转 | 86.4374 | 7 |
| 9 | 301216 | 万凯新材 | 1 | 超跌反转 | 86.0813 | 8 |
| 10 | 000792 | 盐湖股份 | 1 | 超跌反转 | 85.9403 | 9 |
| 11 | 000830 | 鲁西化工 | 1 | 超跌反转 | 85.8939 | 10 |
| 12 | 300708 | 聚灿光电 | 1 | 放量突破 | 76.316 | 1 |
| 13 | 601398 | 工商银行 | 1 | 动量质量 | 74.6459 | 1 |
| 14 | 600036 | 招商银行 | 1 | 动量质量 | 74.0647 | 2 |
| 15 | 601328 | 交通银行 | 1 | 动量质量 | 73.5723 | 3 |
| 16 | 601658 | 邮储银行 | 1 | 动量质量 | 73.5573 | 4 |
| 17 | 601318 | 中国平安 | 1 | 动量质量 | 73.5409 | 5 |
| 18 | 601169 | 北京银行 | 1 | 动量质量 | 73.503 | 6 |
| 19 | 601288 | 农业银行 | 1 | 动量质量 | 73.45 | 7 |
| 20 | 601988 | 中国银行 | 1 | 动量质量 | 72.9327 | 8 |
| 21 | 600030 | 中信证券 | 1 | 动量质量 | 72.7895 | 9 |
| 22 | 601166 | 兴业银行 | 1 | 动量质量 | 71.9264 | 10 |
| 23 | 001696 | 宗申动力 | 1 | 资金热度 | 71.6531 | 1 |
| 24 | 603236 | 移远通信 | 1 | 资金热度 | 70.9436 | 2 |
| 25 | 000978 | 桂林旅游 | 1 | 放量突破 | 70.6977 | 2 |
| 26 | 603363 | 傲农生物 | 1 | 放量突破 | 70.337 | 3 |
| 27 | 600255 | 鑫科材料 | 1 | 放量突破 | 70.1688 | 4 |
| 28 | 302132 | 中航成飞 | 1 | 资金热度 | 70.0082 | 3 |
| 29 | 002106 | 莱宝高科 | 1 | 放量突破 | 69.2536 | 6 |
| 30 | 002765 | 蓝黛科技 | 1 | 放量突破 | 68.9809 | 7 |

## 模型明细与原始候选字段

完整的每套模型返回结果、每只股票的原始候选字段和策略明细请以同目录的 `candidate_pool.json` 为准。

```json
[
  {
    "code": "000519",
    "name": "中兵红箭",
    "resonance_count": 2,
    "strategies": [
      "volume_breakout",
      "capital_heat"
    ],
    "strategy_labels": [
      "放量突破",
      "资金热度"
    ],
    "best_rank": 4,
    "best_score": 70.1293,
    "average_score": 69.58295,
    "strategy_details": {
      "volume_breakout": {
        "rank": 5,
        "score": 70.1293,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 5,
          "code": "000519",
          "name": "中兵红箭",
          "score": 70.1293,
          "screen_score": 70.12929128,
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
          "price": 15.62,
          "change_pct": 6.69,
          "amount": 2090407457.48,
          "industry": "",
          "factor_scores": {
            "value": 57.068,
            "liquidity": 100.0,
            "momentum": 61.8555,
            "reversal": 5.0,
            "activity": 65.7948,
            "stability": 59.13,
            "size": 100.0,
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
            "rank": 5,
            "code": "000519",
            "name": "中兵红箭",
            "final_score": 70.1293,
            "screen_score": 70.12929128,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 15.62,
            "change_pct": 6.69,
            "amount": 2090407457.48,
            "total_mv": 21751771299.0,
            "turnover_rate": 9.77,
            "volume_ratio": 4.82,
            "pe_ratio": 181.85764539,
            "pb_ratio": 2.09531104,
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
            "change_60d": -17.4855,
            "signal_score": 60.0,
            "ma_bullish": false,
            "price_above_ma20": true,
            "macd_status": "neutral",
            "rsi_status": "neutral",
            "breakout_20d_pct": 2.4262,
            "range_20d_pct": 14.0568,
            "volume_ratio_20d": 3.9419,
            "body_pct": 7.7241,
            "pullback_to_ma20_pct": 7.056,
            "consolidation_days_20d": 20,
            "volatility_20d_pct": 37.5107,
            "max_drawdown_20d_pct": -8.1794,
            "atr_20_pct": 2.6472,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:AkshareFetcher",
            "factor_scores": {
              "value": 57.068,
              "liquidity": 100.0,
              "momentum": 61.8555,
              "reversal": 5.0,
              "activity": 65.7948,
              "stability": 59.13,
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
      },
      "capital_heat": {
        "rank": 4,
        "score": 69.0366,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 4,
          "code": "000519",
          "name": "中兵红箭",
          "score": 69.0366,
          "screen_score": 69.03661795698926,
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
          "price": 15.62,
          "change_pct": 6.69,
          "amount": 2090407457.48,
          "industry": "",
          "factor_scores": {
            "value": 54.698,
            "liquidity": 95.6989,
            "momentum": 76.7605,
            "reversal": 5.0,
            "activity": 64.8872,
            "stability": 57.93,
            "size": 90.3226,
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
            "rank": 4,
            "code": "000519",
            "name": "中兵红箭",
            "final_score": 69.0366,
            "screen_score": 69.03661795698926,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 15.62,
            "change_pct": 6.69,
            "amount": 2090407457.48,
            "total_mv": 21751771299.0,
            "turnover_rate": 9.77,
            "volume_ratio": 4.82,
            "pe_ratio": 181.85764539,
            "pb_ratio": 2.09531104,
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
              "value": 54.698,
              "liquidity": 95.6989,
              "momentum": 76.7605,
              "reversal": 5.0,
              "activity": 64.8872,
              "stability": 57.93,
              "size": 90.3226,
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
    "code": "000783",
    "name": "长江证券",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 1,
    "best_score": 91.4018,
    "average_score": 91.4018,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 1,
        "score": 91.4018,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 1,
          "code": "000783",
          "name": "长江证券",
          "score": 91.4018,
          "screen_score": 87.00176476950354,
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
          "price": 8.88,
          "change_pct": -3.58,
          "amount": 1008285513.5,
          "industry": "",
          "factor_scores": {
            "value": 81.8307,
            "liquidity": 89.2199,
            "momentum": 44.865,
            "reversal": 98.96,
            "activity": 80.2214,
            "stability": 67.26,
            "size": 88.3688,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "000783",
              "name": "长江证券",
              "source": "tencent",
              "fetched_at": "2026-09-02T09:37:34.111172+00:00",
              "price": 8.88,
              "change_pct": -3.58,
              "change_amount": -0.33,
              "volume": 112720400,
              "amount": 1008285514.0,
              "volume_ratio": 0.73,
              "turnover_rate": 2.04,
              "amplitude": 2.93,
              "open_price": 9.14,
              "high": 9.14,
              "low": 8.87,
              "pre_close": 9.21,
              "pe_ratio": 9.53,
              "pb_ratio": 1.33,
              "total_mv": 49107000000.0,
              "circ_mv": 49107000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 8.88, 涨跌幅 -3.58%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 1,
            "code": "000783",
            "name": "长江证券",
            "final_score": 91.4018,
            "screen_score": 87.00176476950354,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 8.88,
            "change_pct": -3.58,
            "amount": 1008285513.5,
            "total_mv": 49107047778.0,
            "turnover_rate": 2.04,
            "volume_ratio": 0.73,
            "pe_ratio": 9.5317053,
            "pb_ratio": 1.3306762,
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
              "value": 81.8307,
              "liquidity": 89.2199,
              "momentum": 44.865,
              "reversal": 98.96,
              "activity": 80.2214,
              "stability": 67.26,
              "size": 88.3688,
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
                "code": "000783",
                "name": "长江证券",
                "source": "tencent",
                "fetched_at": "2026-09-02T09:37:34.111172+00:00",
                "price": 8.88,
                "change_pct": -3.58,
                "change_amount": -0.33,
                "volume": 112720400,
                "amount": 1008285514.0,
                "volume_ratio": 0.73,
                "turnover_rate": 2.04,
                "amplitude": 2.93,
                "open_price": 9.14,
                "high": 9.14,
                "low": 8.87,
                "pre_close": 9.21,
                "pe_ratio": 9.53,
                "pb_ratio": 1.33,
                "total_mv": 49107000000.0,
                "circ_mv": 49107000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 8.88, 涨跌幅 -3.58%",
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
    "code": "601233",
    "name": "桐昆股份",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 2,
    "best_score": 90.96,
    "average_score": 90.96,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 2,
        "score": 90.96,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 2,
          "code": "601233",
          "name": "桐昆股份",
          "score": 90.96,
          "screen_score": 86.56002115248228,
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
          "price": 26.28,
          "change_pct": -3.28,
          "amount": 1444559193.0,
          "industry": "",
          "factor_scores": {
            "value": 77.6041,
            "liquidity": 93.0496,
            "momentum": 45.84,
            "reversal": 97.14,
            "activity": 81.7739,
            "stability": 68.16,
            "size": 92.1986,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "601233",
              "name": "桐昆股份",
              "source": "tencent",
              "fetched_at": "2026-09-02T09:37:43.207810+00:00",
              "price": 26.28,
              "change_pct": -3.28,
              "change_amount": -0.89,
              "volume": 55158800,
              "amount": 1444559193.0,
              "volume_ratio": 0.85,
              "turnover_rate": 2.32,
              "amplitude": 6.07,
              "open_price": 27.17,
              "high": 27.25,
              "low": 25.6,
              "pre_close": 27.17,
              "pe_ratio": 12.12,
              "pb_ratio": 1.48,
              "total_mv": 62520000000.00001,
              "circ_mv": 62405999999.99999
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
          "dsa_analysis_summary": "DSA行情: 现价 26.28, 涨跌幅 -3.28%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 2,
            "code": "601233",
            "name": "桐昆股份",
            "final_score": 90.96,
            "screen_score": 86.56002115248228,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 26.28,
            "change_pct": -3.28,
            "amount": 1444559193.0,
            "total_mv": 62520159157.0,
            "turnover_rate": 2.32,
            "volume_ratio": 0.85,
            "pe_ratio": 12.12058338,
            "pb_ratio": 1.46959829,
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
              "value": 77.6041,
              "liquidity": 93.0496,
              "momentum": 45.84,
              "reversal": 97.14,
              "activity": 81.7739,
              "stability": 68.16,
              "size": 92.1986,
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
                "code": "601233",
                "name": "桐昆股份",
                "source": "tencent",
                "fetched_at": "2026-09-02T09:37:43.207810+00:00",
                "price": 26.28,
                "change_pct": -3.28,
                "change_amount": -0.89,
                "volume": 55158800,
                "amount": 1444559193.0,
                "volume_ratio": 0.85,
                "turnover_rate": 2.32,
                "amplitude": 6.07,
                "open_price": 27.17,
                "high": 27.25,
                "low": 25.6,
                "pre_close": 27.17,
                "pe_ratio": 12.12,
                "pb_ratio": 1.48,
                "total_mv": 62520000000.00001,
                "circ_mv": 62405999999.99999
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
            "dsa_analysis_summary": "DSA行情: 现价 26.28, 涨跌幅 -3.28%",
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
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 3,
    "best_score": 90.8107,
    "average_score": 90.8107,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 3,
        "score": 90.8107,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 3,
          "code": "603799",
          "name": "华友钴业",
          "score": 90.8107,
          "screen_score": 86.41065716312058,
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
          "price": 37.94,
          "change_pct": -3.04,
          "amount": 1857669074.0,
          "industry": "",
          "factor_scores": {
            "value": 80.0339,
            "liquidity": 95.461,
            "momentum": 46.62,
            "reversal": 94.02,
            "activity": 83.971,
            "stability": 68.88,
            "size": 93.617,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "603799",
              "name": "华友钴业",
              "source": "tencent",
              "fetched_at": "2026-09-02T09:37:53.999221+00:00",
              "price": 37.94,
              "change_pct": -3.04,
              "change_amount": -1.19,
              "volume": 48856900,
              "amount": 1857669074.0,
              "volume_ratio": 1.12,
              "turnover_rate": 2.59,
              "amplitude": 2.61,
              "open_price": 38.75,
              "high": 38.75,
              "low": 37.73,
              "pre_close": 39.13,
              "pe_ratio": 10.4,
              "pb_ratio": 1.41,
              "total_mv": 71840000000.0,
              "circ_mv": 71616000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 37.94, 涨跌幅 -3.04%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality、controlled_reversal"
          },
          "post_analysis_tags": [
            "value_quality",
            "controlled_reversal"
          ],
          "raw": {
            "rank": 3,
            "code": "603799",
            "name": "华友钴业",
            "final_score": 90.8107,
            "screen_score": 86.41065716312058,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 37.94,
            "change_pct": -3.04,
            "amount": 1857669074.0,
            "total_mv": 71840433995.0,
            "turnover_rate": 2.59,
            "volume_ratio": 1.12,
            "pe_ratio": 10.40133405,
            "pb_ratio": 1.41221445,
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
              "value": 80.0339,
              "liquidity": 95.461,
              "momentum": 46.62,
              "reversal": 94.02,
              "activity": 83.971,
              "stability": 68.88,
              "size": 93.617,
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
                "code": "603799",
                "name": "华友钴业",
                "source": "tencent",
                "fetched_at": "2026-09-02T09:37:53.999221+00:00",
                "price": 37.94,
                "change_pct": -3.04,
                "change_amount": -1.19,
                "volume": 48856900,
                "amount": 1857669074.0,
                "volume_ratio": 1.12,
                "turnover_rate": 2.59,
                "amplitude": 2.61,
                "open_price": 38.75,
                "high": 38.75,
                "low": 37.73,
                "pre_close": 39.13,
                "pe_ratio": 10.4,
                "pb_ratio": 1.41,
                "total_mv": 71840000000.0,
                "circ_mv": 71616000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 37.94, 涨跌幅 -3.04%",
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
    "best_rank": 4,
    "best_score": 90.1237,
    "average_score": 90.1237,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 4,
        "score": 90.1237,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 4,
          "code": "000425",
          "name": "徐工机械",
          "score": 90.1237,
          "screen_score": 85.72368021276596,
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
          "price": 7.97,
          "change_pct": -3.28,
          "amount": 1227937995.78,
          "industry": "",
          "factor_scores": {
            "value": 75.3388,
            "liquidity": 90.922,
            "momentum": 45.84,
            "reversal": 97.14,
            "activity": 80.2585,
            "stability": 68.16,
            "size": 95.3191,
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
            "code": "000425",
            "name": "徐工机械",
            "final_score": 90.1237,
            "screen_score": 85.72368021276596,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 7.97,
            "change_pct": -3.28,
            "amount": 1227937995.78,
            "total_mv": 93338347279.0,
            "turnover_rate": 1.71,
            "volume_ratio": 1.0,
            "pe_ratio": 15.11349348,
            "pb_ratio": 1.4458217,
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
              "value": 75.3388,
              "liquidity": 90.922,
              "momentum": 45.84,
              "reversal": 97.14,
              "activity": 80.2585,
              "stability": 68.16,
              "size": 95.3191,
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
    "code": "600362",
    "name": "江西铜业",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 5,
    "best_score": 88.0563,
    "average_score": 88.0563,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 5,
        "score": 88.0563,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 5,
          "code": "600362",
          "name": "江西铜业",
          "score": 88.0563,
          "screen_score": 86.05629686170214,
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
          "price": 46.55,
          "change_pct": -3.18,
          "amount": 2973955421.0,
          "industry": "",
          "factor_scores": {
            "value": 70.7867,
            "liquidity": 98.2979,
            "momentum": 46.165,
            "reversal": 95.84,
            "activity": 83.4801,
            "stability": 68.46,
            "size": 98.156,
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
            "code": "600362",
            "name": "江西铜业",
            "final_score": 88.0563,
            "screen_score": 86.05629686170214,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 46.55,
            "change_pct": -3.18,
            "amount": 2973955421.0,
            "total_mv": 161190053803.0,
            "turnover_rate": 3.08,
            "volume_ratio": 0.75,
            "pe_ratio": 13.91072267,
            "pb_ratio": 1.83934814,
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
              "value": 70.7867,
              "liquidity": 98.2979,
              "momentum": 46.165,
              "reversal": 95.84,
              "activity": 83.4801,
              "stability": 68.46,
              "size": 98.156,
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
    "code": "600096",
    "name": "云天化",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 6,
    "best_score": 87.2109,
    "average_score": 87.2109,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 6,
        "score": 87.2109,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 6,
          "code": "600096",
          "name": "云天化",
          "score": 87.2109,
          "screen_score": 85.21086851063829,
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
          "price": 30.91,
          "change_pct": -3.29,
          "amount": 1449405747.0,
          "industry": "",
          "factor_scores": {
            "value": 68.2271,
            "liquidity": 93.1915,
            "momentum": 45.8075,
            "reversal": 97.27,
            "activity": 83.101,
            "stability": 68.13,
            "size": 91.2057,
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
            "code": "600096",
            "name": "云天化",
            "final_score": 87.2109,
            "screen_score": 85.21086851063829,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 30.91,
            "change_pct": -3.29,
            "amount": 1449405747.0,
            "total_mv": 56348643495.0,
            "turnover_rate": 2.55,
            "volume_ratio": 0.96,
            "pe_ratio": 10.5804412,
            "pb_ratio": 2.2180343,
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
              "value": 68.2271,
              "liquidity": 93.1915,
              "momentum": 45.8075,
              "reversal": 97.27,
              "activity": 83.101,
              "stability": 68.13,
              "size": 91.2057,
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
    "code": "000060",
    "name": "中金岭南",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 7,
    "best_score": 86.4374,
    "average_score": 86.4374,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 7,
        "score": 86.4374,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 7,
          "code": "000060",
          "name": "中金岭南",
          "score": 86.4374,
          "screen_score": 84.43737040780142,
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
          "price": 6.59,
          "change_pct": -3.65,
          "amount": 873107413.1,
          "industry": "",
          "factor_scores": {
            "value": 69.8754,
            "liquidity": 86.383,
            "momentum": 44.6375,
            "reversal": 98.05,
            "activity": 84.6396,
            "stability": 67.05,
            "size": 79.8582,
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
            "code": "000060",
            "name": "中金岭南",
            "final_score": 86.4374,
            "screen_score": 84.43737040780142,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 6.59,
            "change_pct": -3.65,
            "amount": 873107413.1,
            "total_mv": 29267326498.0,
            "turnover_rate": 2.99,
            "volume_ratio": 0.95,
            "pe_ratio": 21.13268629,
            "pb_ratio": 1.44525837,
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
              "value": 69.8754,
              "liquidity": 86.383,
              "momentum": 44.6375,
              "reversal": 98.05,
              "activity": 84.6396,
              "stability": 67.05,
              "size": 79.8582,
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
    "code": "301216",
    "name": "万凯新材",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 8,
    "best_score": 86.0813,
    "average_score": 86.0813,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 8,
        "score": 86.0813,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 8,
          "code": "301216",
          "name": "万凯新材",
          "score": 86.0813,
          "screen_score": 84.08133242907802,
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
          "price": 19.23,
          "change_pct": -3.51,
          "amount": 856820768.03,
          "industry": "",
          "factor_scores": {
            "value": 70.1775,
            "liquidity": 85.3901,
            "momentum": 45.0925,
            "reversal": 99.87,
            "activity": 67.3454,
            "stability": 67.47,
            "size": 45.1064,
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
            "code": "301216",
            "name": "万凯新材",
            "final_score": 86.0813,
            "screen_score": 84.08133242907802,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 19.23,
            "change_pct": -3.51,
            "amount": 856820768.03,
            "total_mv": 11157329824.0,
            "turnover_rate": 7.94,
            "volume_ratio": 1.05,
            "pe_ratio": 16.5200442,
            "pb_ratio": 1.70043788,
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
              "value": 70.1775,
              "liquidity": 85.3901,
              "momentum": 45.0925,
              "reversal": 99.87,
              "activity": 67.3454,
              "stability": 67.47,
              "size": 45.1064,
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
    "code": "000792",
    "name": "盐湖股份",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 9,
    "best_score": 85.9403,
    "average_score": 85.9403,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 9,
        "score": 85.9403,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 9,
          "code": "000792",
          "name": "盐湖股份",
          "score": 85.9403,
          "screen_score": 83.94032875886525,
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
          "price": 26.94,
          "change_pct": -3.27,
          "amount": 1891262147.19,
          "industry": "",
          "factor_scores": {
            "value": 59.0785,
            "liquidity": 96.0284,
            "momentum": 45.8725,
            "reversal": 97.01,
            "activity": 79.3442,
            "stability": 68.19,
            "size": 97.7305,
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
            "code": "000792",
            "name": "盐湖股份",
            "final_score": 85.9403,
            "screen_score": 83.94032875886525,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 26.94,
            "change_pct": -3.27,
            "amount": 1891262147.19,
            "total_mv": 142554964255.0,
            "turnover_rate": 1.33,
            "volume_ratio": 1.1,
            "pe_ratio": 11.8293871,
            "pb_ratio": 2.98535661,
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
              "value": 59.0785,
              "liquidity": 96.0284,
              "momentum": 45.8725,
              "reversal": 97.01,
              "activity": 79.3442,
              "stability": 68.19,
              "size": 97.7305,
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
    "code": "000830",
    "name": "鲁西化工",
    "resonance_count": 1,
    "strategies": [
      "oversold_reversal"
    ],
    "strategy_labels": [
      "超跌反转"
    ],
    "best_rank": 10,
    "best_score": 85.8939,
    "average_score": 85.8939,
    "strategy_details": {
      "oversold_reversal": {
        "rank": 10,
        "score": 85.8939,
        "reason": "本地后置评分: controlled_reversal",
        "raw_candidate": {
          "rank": 10,
          "code": "000830",
          "name": "鲁西化工",
          "score": 85.8939,
          "screen_score": 83.89388675531916,
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
          "price": 12.76,
          "change_pct": -3.63,
          "amount": 654191509.67,
          "industry": "",
          "factor_scores": {
            "value": 72.558,
            "liquidity": 80.5674,
            "momentum": 44.7025,
            "reversal": 98.31,
            "activity": 83.9414,
            "stability": 67.11,
            "size": 74.0426,
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
            "code": "000830",
            "name": "鲁西化工",
            "final_score": 85.8939,
            "screen_score": 83.89388675531916,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 12.76,
            "change_pct": -3.63,
            "amount": 654191509.67,
            "total_mv": 24299110580.0,
            "turnover_rate": 2.67,
            "volume_ratio": 1.05,
            "pe_ratio": 21.73944266,
            "pb_ratio": 1.24309862,
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
              "value": 72.558,
              "liquidity": 80.5674,
              "momentum": 44.7025,
              "reversal": 98.31,
              "activity": 83.9414,
              "stability": 67.11,
              "size": 74.0426,
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
    "code": "300708",
    "name": "聚灿光电",
    "resonance_count": 1,
    "strategies": [
      "volume_breakout"
    ],
    "strategy_labels": [
      "放量突破"
    ],
    "best_rank": 1,
    "best_score": 76.316,
    "average_score": 76.316,
    "strategy_details": {
      "volume_breakout": {
        "rank": 1,
        "score": 76.316,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 1,
          "code": "300708",
          "name": "聚灿光电",
          "score": 76.316,
          "screen_score": 74.11603082694738,
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
          "price": 8.58,
          "change_pct": 3.62,
          "amount": 349946293.15,
          "industry": "",
          "factor_scores": {
            "value": 64.2925,
            "liquidity": 68.4211,
            "momentum": 75.5237,
            "reversal": 5.0,
            "activity": 84.8208,
            "stability": 71.46,
            "size": 84.2105,
            "theme_heat": 50.0,
            "topic_alignment": 50.0
          },
          "dsa_context": {
            "enriched": true,
            "profile": "pre_rank_light",
            "news_included": false,
            "events_included": false,
            "quote": {
              "code": "300708",
              "name": "聚灿光电",
              "source": "tencent",
              "fetched_at": "2026-09-02T09:35:49.005378+00:00",
              "price": 8.58,
              "change_pct": 3.62,
              "change_amount": 0.3,
              "volume": 41124100,
              "amount": 349946293.0,
              "volume_ratio": 2.62,
              "turnover_rate": 5.76,
              "amplitude": 6.16,
              "open_price": 8.22,
              "high": 8.68,
              "low": 8.17,
              "pre_close": 8.28,
              "pe_ratio": 49.03,
              "pb_ratio": 2.75,
              "total_mv": 8094000000.0,
              "circ_mv": 6130000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 8.58, 涨跌幅 3.62%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 1,
            "code": "300708",
            "name": "聚灿光电",
            "final_score": 76.316,
            "screen_score": 74.11603082694738,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 8.58,
            "change_pct": 3.62,
            "amount": 349946293.15,
            "total_mv": 8093747410.0,
            "turnover_rate": 5.7,
            "volume_ratio": 2.62,
            "pe_ratio": 49.02569328,
            "pb_ratio": 2.74955795,
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
            "change_60d": -1.3793,
            "signal_score": 86.0,
            "ma_bullish": true,
            "price_above_ma20": true,
            "macd_status": "bullish",
            "rsi_status": "neutral",
            "breakout_20d_pct": 2.0214,
            "range_20d_pct": 15.7333,
            "volume_ratio_20d": 2.3045,
            "body_pct": 4.3796,
            "pullback_to_ma20_pct": 7.6199,
            "consolidation_days_20d": 13,
            "volatility_20d_pct": 37.0045,
            "max_drawdown_20d_pct": -7.7295,
            "atr_20_pct": 3.2284,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:AkshareFetcher",
            "factor_scores": {
              "value": 64.2925,
              "liquidity": 68.4211,
              "momentum": 75.5237,
              "reversal": 5.0,
              "activity": 84.8208,
              "stability": 71.46,
              "size": 84.2105,
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
                "code": "300708",
                "name": "聚灿光电",
                "source": "tencent",
                "fetched_at": "2026-09-02T09:35:49.005378+00:00",
                "price": 8.58,
                "change_pct": 3.62,
                "change_amount": 0.3,
                "volume": 41124100,
                "amount": 349946293.0,
                "volume_ratio": 2.62,
                "turnover_rate": 5.76,
                "amplitude": 6.16,
                "open_price": 8.22,
                "high": 8.68,
                "low": 8.17,
                "pre_close": 8.28,
                "pe_ratio": 49.03,
                "pb_ratio": 2.75,
                "total_mv": 8094000000.0,
                "circ_mv": 6130000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 8.58, 涨跌幅 3.62%",
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
    "best_score": 74.6459,
    "average_score": 74.6459,
    "strategy_details": {
      "momentum_quality": {
        "rank": 1,
        "score": 74.6459,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 1,
          "code": "601398",
          "name": "工商银行",
          "score": 74.6459,
          "screen_score": 72.84590934734513,
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
          "price": 8.22,
          "change_pct": 0.86,
          "amount": 3052234794.0,
          "industry": "",
          "factor_scores": {
            "value": 85.6303,
            "liquidity": 95.9292,
            "momentum": 59.295,
            "reversal": 49.82,
            "activity": 67.2554,
            "stability": 75.42,
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
              "fetched_at": "2026-09-02T09:36:58.772238+00:00",
              "price": 8.22,
              "change_pct": 0.86,
              "change_amount": 0.07,
              "volume": 371799900,
              "amount": 3052234794.0,
              "volume_ratio": 1.17,
              "turnover_rate": 0.14,
              "amplitude": 1.84,
              "open_price": 8.19,
              "high": 8.29,
              "low": 8.14,
              "pre_close": 8.15,
              "pe_ratio": 7.83,
              "pb_ratio": 0.74,
              "total_mv": 2929659000000.0,
              "circ_mv": 2216212000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 8.22, 涨跌幅 0.86%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality"
          },
          "post_analysis_tags": [
            "value_quality"
          ],
          "raw": {
            "rank": 1,
            "code": "601398",
            "name": "工商银行",
            "final_score": 74.6459,
            "screen_score": 72.84590934734513,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 8.22,
            "change_pct": 0.86,
            "amount": 3052234794.0,
            "total_mv": 2929659433272.0,
            "turnover_rate": 0.14,
            "volume_ratio": 1.17,
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
              "value": 85.6303,
              "liquidity": 95.9292,
              "momentum": 59.295,
              "reversal": 49.82,
              "activity": 67.2554,
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
            "dsa_context": {
              "enriched": true,
              "profile": "pre_rank_light",
              "news_included": false,
              "events_included": false,
              "quote": {
                "code": "601398",
                "name": "工商银行",
                "source": "tencent",
                "fetched_at": "2026-09-02T09:36:58.772238+00:00",
                "price": 8.22,
                "change_pct": 0.86,
                "change_amount": 0.07,
                "volume": 371799900,
                "amount": 3052234794.0,
                "volume_ratio": 1.17,
                "turnover_rate": 0.14,
                "amplitude": 1.84,
                "open_price": 8.19,
                "high": 8.29,
                "low": 8.14,
                "pre_close": 8.15,
                "pe_ratio": 7.83,
                "pb_ratio": 0.74,
                "total_mv": 2929659000000.0,
                "circ_mv": 2216212000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 8.22, 涨跌幅 0.86%",
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
    "best_score": 74.0647,
    "average_score": 74.0647,
    "strategy_details": {
      "momentum_quality": {
        "rank": 2,
        "score": 74.0647,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 2,
          "code": "600036",
          "name": "招商银行",
          "score": 74.0647,
          "screen_score": 72.26471886061945,
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
          "price": 40.87,
          "change_pct": 0.02,
          "amount": 2647880876.0,
          "industry": "",
          "factor_scores": {
            "value": 84.6679,
            "liquidity": 94.6903,
            "momentum": 56.565,
            "reversal": 60.74,
            "activity": 66.2339,
            "stability": 77.94,
            "size": 98.2301,
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
              "fetched_at": "2026-09-02T09:37:10.647870+00:00",
              "price": 40.87,
              "change_pct": 0.02,
              "change_amount": 0.01,
              "volume": 64861100,
              "amount": 2647880876.0,
              "volume_ratio": 0.81,
              "turnover_rate": 0.31,
              "amplitude": 0.91,
              "open_price": 40.9,
              "high": 41.0,
              "low": 40.63,
              "pre_close": 40.86,
              "pe_ratio": 6.79,
              "pb_ratio": 0.9,
              "total_mv": 1030735000000.0,
              "circ_mv": 843104999999.9999
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
          "dsa_analysis_summary": "DSA行情: 现价 40.87, 涨跌幅 0.02%",
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
            "final_score": 74.0647,
            "screen_score": 72.26471886061945,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 40.87,
            "change_pct": 0.02,
            "amount": 2647880876.0,
            "total_mv": 1030735089713.0,
            "turnover_rate": 0.31,
            "volume_ratio": 0.81,
            "pe_ratio": 6.79474139,
            "pb_ratio": 0.90017073,
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
              "value": 84.6679,
              "liquidity": 94.6903,
              "momentum": 56.565,
              "reversal": 60.74,
              "activity": 66.2339,
              "stability": 77.94,
              "size": 98.2301,
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
                "fetched_at": "2026-09-02T09:37:10.647870+00:00",
                "price": 40.87,
                "change_pct": 0.02,
                "change_amount": 0.01,
                "volume": 64861100,
                "amount": 2647880876.0,
                "volume_ratio": 0.81,
                "turnover_rate": 0.31,
                "amplitude": 0.91,
                "open_price": 40.9,
                "high": 41.0,
                "low": 40.63,
                "pre_close": 40.86,
                "pe_ratio": 6.79,
                "pb_ratio": 0.9,
                "total_mv": 1030735000000.0,
                "circ_mv": 843104999999.9999
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
            "dsa_analysis_summary": "DSA行情: 现价 40.87, 涨跌幅 0.02%",
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
    "best_rank": 3,
    "best_score": 73.5723,
    "average_score": 73.5723,
    "strategy_details": {
      "momentum_quality": {
        "rank": 3,
        "score": 73.5723,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 3,
          "code": "601328",
          "name": "交通银行",
          "score": 73.5723,
          "screen_score": 71.77227538716812,
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
          "price": 7.43,
          "change_pct": 0.95,
          "amount": 1552372670.0,
          "industry": "",
          "factor_scores": {
            "value": 87.5188,
            "liquidity": 86.3717,
            "momentum": 59.5875,
            "reversal": 48.65,
            "activity": 70.0851,
            "stability": 75.15,
            "size": 96.8142,
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
              "fetched_at": "2026-09-02T09:37:22.842317+00:00",
              "price": 7.43,
              "change_pct": 0.95,
              "change_amount": 0.07,
              "volume": 208998100,
              "amount": 1552372670.0,
              "volume_ratio": 1.27,
              "turnover_rate": 0.8,
              "amplitude": 1.49,
              "open_price": 7.4,
              "high": 7.48,
              "low": 7.37,
              "pre_close": 7.36,
              "pe_ratio": 6.74,
              "pb_ratio": 0.56,
              "total_mv": 656543000000.0,
              "circ_mv": 193718000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 7.43, 涨跌幅 0.95%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: value_quality"
          },
          "post_analysis_tags": [
            "value_quality"
          ],
          "raw": {
            "rank": 3,
            "code": "601328",
            "name": "交通银行",
            "final_score": 73.5723,
            "screen_score": 71.77227538716812,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 7.43,
            "change_pct": 0.95,
            "amount": 1552372670.0,
            "total_mv": 656542916777.0,
            "turnover_rate": 0.8,
            "volume_ratio": 1.27,
            "pe_ratio": 6.73515508,
            "pb_ratio": 0.56218567,
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
              "value": 87.5188,
              "liquidity": 86.3717,
              "momentum": 59.5875,
              "reversal": 48.65,
              "activity": 70.0851,
              "stability": 75.15,
              "size": 96.8142,
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
                "fetched_at": "2026-09-02T09:37:22.842317+00:00",
                "price": 7.43,
                "change_pct": 0.95,
                "change_amount": 0.07,
                "volume": 208998100,
                "amount": 1552372670.0,
                "volume_ratio": 1.27,
                "turnover_rate": 0.8,
                "amplitude": 1.49,
                "open_price": 7.4,
                "high": 7.48,
                "low": 7.37,
                "pre_close": 7.36,
                "pe_ratio": 6.74,
                "pb_ratio": 0.56,
                "total_mv": 656543000000.0,
                "circ_mv": 193718000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 7.43, 涨跌幅 0.95%",
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
    "code": "601658",
    "name": "邮储银行",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 4,
    "best_score": 73.5573,
    "average_score": 73.5573,
    "strategy_details": {
      "momentum_quality": {
        "rank": 4,
        "score": 73.5573,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 4,
          "code": "601658",
          "name": "邮储银行",
          "score": 73.5573,
          "screen_score": 71.75726355088496,
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
          "price": 5.56,
          "change_pct": 1.46,
          "amount": 1792049054.0,
          "industry": "",
          "factor_scores": {
            "value": 86.3613,
            "liquidity": 89.2035,
            "momentum": 61.245,
            "reversal": 38.34,
            "activity": 68.5529,
            "stability": 73.62,
            "size": 97.3451,
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
            "code": "601658",
            "name": "邮储银行",
            "final_score": 73.5573,
            "screen_score": 71.75726355088496,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 5.56,
            "change_pct": 1.46,
            "amount": 1792049054.0,
            "total_mv": 667728497416.0,
            "turnover_rate": 0.45,
            "volume_ratio": 1.21,
            "pe_ratio": 7.44576208,
            "pb_ratio": 0.63815694,
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
              "value": 86.3613,
              "liquidity": 89.2035,
              "momentum": 61.245,
              "reversal": 38.34,
              "activity": 68.5529,
              "stability": 73.62,
              "size": 97.3451,
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
    "best_score": 73.5409,
    "average_score": 73.5409,
    "strategy_details": {
      "momentum_quality": {
        "rank": 5,
        "score": 73.5409,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 5,
          "code": "601318",
          "name": "中国平安",
          "score": 73.5409,
          "screen_score": 71.74088246681416,
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
          "price": 56.63,
          "change_pct": -1.05,
          "amount": 3409288191.0,
          "industry": "",
          "factor_scores": {
            "value": 83.5201,
            "liquidity": 96.4602,
            "momentum": 53.0875,
            "reversal": 74.65,
            "activity": 67.0431,
            "stability": 74.85,
            "size": 98.0531,
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
            "final_score": 73.5409,
            "screen_score": 71.74088246681416,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 56.63,
            "change_pct": -1.05,
            "amount": 3409288191.0,
            "total_mv": 1025435766177.0,
            "turnover_rate": 0.56,
            "volume_ratio": 0.79,
            "pe_ratio": 6.43648953,
            "pb_ratio": 0.99742411,
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
              "value": 83.5201,
              "liquidity": 96.4602,
              "momentum": 53.0875,
              "reversal": 74.65,
              "activity": 67.0431,
              "stability": 74.85,
              "size": 98.0531,
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
    "code": "601169",
    "name": "北京银行",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 6,
    "best_score": 73.503,
    "average_score": 73.503,
    "strategy_details": {
      "momentum_quality": {
        "rank": 6,
        "score": 73.503,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 6,
          "code": "601169",
          "name": "北京银行",
          "score": 73.503,
          "screen_score": 71.70297765486727,
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
          "price": 5.54,
          "change_pct": 0.91,
          "amount": 1482861781.0,
          "industry": "",
          "factor_scores": {
            "value": 89.2011,
            "liquidity": 85.6637,
            "momentum": 59.4575,
            "reversal": 49.17,
            "activity": 70.7335,
            "stability": 75.27,
            "size": 82.3009,
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
            "code": "601169",
            "name": "北京银行",
            "final_score": 73.503,
            "screen_score": 71.70297765486727,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 5.54,
            "change_pct": 0.91,
            "amount": 1482861781.0,
            "total_mv": 117132132867.0,
            "turnover_rate": 1.27,
            "volume_ratio": 1.04,
            "pe_ratio": 5.59557316,
            "pb_ratio": 0.41089479,
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
              "value": 89.2011,
              "liquidity": 85.6637,
              "momentum": 59.4575,
              "reversal": 49.17,
              "activity": 70.7335,
              "stability": 75.27,
              "size": 82.3009,
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
    "best_score": 73.45,
    "average_score": 73.45,
    "strategy_details": {
      "momentum_quality": {
        "rank": 7,
        "score": 73.45,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 7,
          "code": "601288",
          "name": "农业银行",
          "score": 73.45,
          "screen_score": 71.64997234513274,
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
          "price": 7.06,
          "change_pct": 0.14,
          "amount": 2061995149.0,
          "industry": "",
          "factor_scores": {
            "value": 84.2294,
            "liquidity": 91.8584,
            "momentum": 56.955,
            "reversal": 59.18,
            "activity": 65.7595,
            "stability": 77.58,
            "size": 99.646,
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
            "final_score": 73.45,
            "screen_score": 71.64997234513274,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 7.06,
            "change_pct": 0.14,
            "amount": 2061995149.0,
            "total_mv": 2470880219143.0,
            "turnover_rate": 0.09,
            "volume_ratio": 0.88,
            "pe_ratio": 8.29399359,
            "pb_ratio": 0.86454448,
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
              "value": 84.2294,
              "liquidity": 91.8584,
              "momentum": 56.955,
              "reversal": 59.18,
              "activity": 65.7595,
              "stability": 77.58,
              "size": 99.646,
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
    "best_score": 72.9327,
    "average_score": 72.9327,
    "strategy_details": {
      "momentum_quality": {
        "rank": 8,
        "score": 72.9327,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 8,
          "code": "601988",
          "name": "中国银行",
          "score": 72.9327,
          "screen_score": 71.13267815265485,
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
          "price": 6.68,
          "change_pct": 0.15,
          "amount": 1689243035.0,
          "industry": "",
          "factor_scores": {
            "value": 84.6462,
            "liquidity": 88.8496,
            "momentum": 56.9875,
            "reversal": 59.05,
            "activity": 65.5499,
            "stability": 77.55,
            "size": 99.292,
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
            "code": "601988",
            "name": "中国银行",
            "final_score": 72.9327,
            "screen_score": 71.13267815265485,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 6.68,
            "change_pct": 0.15,
            "amount": 1689243035.0,
            "total_mv": 2152378910918.0,
            "turnover_rate": 0.12,
            "volume_ratio": 0.81,
            "pe_ratio": 8.64325893,
            "pb_ratio": 0.78248662,
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
              "value": 84.6462,
              "liquidity": 88.8496,
              "momentum": 56.9875,
              "reversal": 59.05,
              "activity": 65.5499,
              "stability": 77.55,
              "size": 99.292,
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
    "best_rank": 9,
    "best_score": 72.7895,
    "average_score": 72.7895,
    "strategy_details": {
      "momentum_quality": {
        "rank": 9,
        "score": 72.7895,
        "reason": "本地后置评分: value_quality、controlled_reversal",
        "raw_candidate": {
          "rank": 9,
          "code": "600030",
          "name": "中信证券",
          "score": 72.7895,
          "screen_score": 69.78952417035397,
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
          "price": 27.47,
          "change_pct": -1.96,
          "amount": 2842606814.0,
          "industry": "",
          "factor_scores": {
            "value": 75.4838,
            "liquidity": 95.3982,
            "momentum": 50.13,
            "reversal": 86.48,
            "activity": 68.1779,
            "stability": 72.12,
            "size": 95.9292,
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
            "rank": 9,
            "code": "600030",
            "name": "中信证券",
            "final_score": 72.7895,
            "screen_score": 69.78952417035397,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 27.47,
            "change_pct": -1.96,
            "amount": 2842606814.0,
            "total_mv": 429198757664.0,
            "turnover_rate": 0.85,
            "volume_ratio": 0.81,
            "pe_ratio": 10.82311309,
            "pb_ratio": 1.45257555,
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
              "value": 75.4838,
              "liquidity": 95.3982,
              "momentum": 50.13,
              "reversal": 86.48,
              "activity": 68.1779,
              "stability": 72.12,
              "size": 95.9292,
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
    "code": "601166",
    "name": "兴业银行",
    "resonance_count": 1,
    "strategies": [
      "momentum_quality"
    ],
    "strategy_labels": [
      "动量质量"
    ],
    "best_rank": 10,
    "best_score": 71.9264,
    "average_score": 71.9264,
    "strategy_details": {
      "momentum_quality": {
        "rank": 10,
        "score": 71.9264,
        "reason": "本地后置评分: value_quality",
        "raw_candidate": {
          "rank": 10,
          "code": "601166",
          "name": "兴业银行",
          "score": 71.9264,
          "screen_score": 70.12642671460175,
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
          "price": 17.9,
          "change_pct": -0.28,
          "amount": 1271804564.0,
          "industry": "",
          "factor_scores": {
            "value": 89.3582,
            "liquidity": 81.5929,
            "momentum": 55.59,
            "reversal": 64.64,
            "activity": 64.7631,
            "stability": 77.16,
            "size": 95.5752,
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
            "code": "601166",
            "name": "兴业银行",
            "final_score": 71.9264,
            "screen_score": 70.12642671460175,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 17.9,
            "change_pct": -0.28,
            "amount": 1271804564.0,
            "total_mv": 378815185283.0,
            "turnover_rate": 0.33,
            "volume_ratio": 0.47,
            "pe_ratio": 5.02014584,
            "pb_ratio": 0.45303175,
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
              "value": 89.3582,
              "liquidity": 81.5929,
              "momentum": 55.59,
              "reversal": 64.64,
              "activity": 64.7631,
              "stability": 77.16,
              "size": 95.5752,
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
    "code": "001696",
    "name": "宗申动力",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 1,
    "best_score": 71.6531,
    "average_score": 71.6531,
    "strategy_details": {
      "capital_heat": {
        "rank": 1,
        "score": 71.6531,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 1,
          "code": "001696",
          "name": "宗申动力",
          "score": 71.6531,
          "screen_score": 69.25313887096775,
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
          "price": 16.2,
          "change_pct": 5.19,
          "amount": 1376549539.96,
          "industry": "",
          "factor_scores": {
            "value": 59.4139,
            "liquidity": 87.0968,
            "momentum": 73.3675,
            "reversal": 5.0,
            "activity": 72.8466,
            "stability": 62.43,
            "size": 87.0968,
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
            "rank": 1,
            "code": "001696",
            "name": "宗申动力",
            "final_score": 71.6531,
            "screen_score": 69.25313887096775,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 16.2,
            "change_pct": 5.19,
            "amount": 1376549539.96,
            "total_mv": 18549436104.0,
            "turnover_rate": 9.79,
            "volume_ratio": 3.05,
            "pe_ratio": 32.06700559,
            "pb_ratio": 3.35096711,
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
              "value": 59.4139,
              "liquidity": 87.0968,
              "momentum": 73.3675,
              "reversal": 5.0,
              "activity": 72.8466,
              "stability": 62.43,
              "size": 87.0968,
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
    "code": "603236",
    "name": "移远通信",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 2,
    "best_score": 70.9436,
    "average_score": 70.9436,
    "strategy_details": {
      "capital_heat": {
        "rank": 2,
        "score": 70.9436,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 2,
          "code": "603236",
          "name": "移远通信",
          "score": 70.9436,
          "screen_score": 70.9436379032258,
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
          "price": 63.6,
          "change_pct": 1.61,
          "amount": 1556636111.0,
          "industry": "",
          "factor_scores": {
            "value": 60.2315,
            "liquidity": 90.3226,
            "momentum": 61.7325,
            "reversal": 35.19,
            "activity": 82.1894,
            "stability": 73.17,
            "size": 92.4731,
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
              "fetched_at": "2026-09-02T09:36:36.530961+00:00",
              "price": 63.6,
              "change_pct": 1.61,
              "change_amount": 1.01,
              "volume": 24352000,
              "amount": 1556636111.0,
              "volume_ratio": 1.61,
              "turnover_rate": 6.01,
              "amplitude": 7.29,
              "open_price": 61.79,
              "high": 65.92,
              "low": 61.36,
              "pre_close": 62.59,
              "pe_ratio": 26.63,
              "pb_ratio": 3.59,
              "total_mv": 25781000000.0,
              "circ_mv": 25781000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 63.6, 涨跌幅 1.61%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: 未发现额外加分项"
          },
          "post_analysis_tags": [],
          "raw": {
            "rank": 2,
            "code": "603236",
            "name": "移远通信",
            "final_score": 70.9436,
            "screen_score": 70.9436379032258,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 63.6,
            "change_pct": 1.61,
            "amount": 1556636111.0,
            "total_mv": 25781224049.0,
            "turnover_rate": 6.01,
            "volume_ratio": 1.61,
            "pe_ratio": 26.6268722,
            "pb_ratio": 3.50160738,
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
              "value": 60.2315,
              "liquidity": 90.3226,
              "momentum": 61.7325,
              "reversal": 35.19,
              "activity": 82.1894,
              "stability": 73.17,
              "size": 92.4731,
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
                "code": "603236",
                "name": "移远通信",
                "source": "tencent",
                "fetched_at": "2026-09-02T09:36:36.530961+00:00",
                "price": 63.6,
                "change_pct": 1.61,
                "change_amount": 1.01,
                "volume": 24352000,
                "amount": 1556636111.0,
                "volume_ratio": 1.61,
                "turnover_rate": 6.01,
                "amplitude": 7.29,
                "open_price": 61.79,
                "high": 65.92,
                "low": 61.36,
                "pre_close": 62.59,
                "pe_ratio": 26.63,
                "pb_ratio": 3.59,
                "total_mv": 25781000000.0,
                "circ_mv": 25781000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 63.6, 涨跌幅 1.61%",
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
    "code": "000978",
    "name": "桂林旅游",
    "resonance_count": 1,
    "strategies": [
      "volume_breakout"
    ],
    "strategy_labels": [
      "放量突破"
    ],
    "best_rank": 2,
    "best_score": 70.6977,
    "average_score": 70.6977,
    "strategy_details": {
      "volume_breakout": {
        "rank": 2,
        "score": 70.6977,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 2,
          "code": "000978",
          "name": "桂林旅游",
          "score": 70.6977,
          "screen_score": 68.49767059073685,
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
          "price": 6.55,
          "change_pct": 2.02,
          "amount": 205314998.64,
          "industry": "",
          "factor_scores": {
            "value": 33.3241,
            "liquidity": 42.1053,
            "momentum": 75.521,
            "reversal": 26.58,
            "activity": 83.6436,
            "stability": 76.4757,
            "size": 21.0526,
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
            "code": "000978",
            "name": "桂林旅游",
            "final_score": 70.6977,
            "screen_score": 68.49767059073685,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 6.55,
            "change_pct": 2.02,
            "amount": 205314998.64,
            "total_mv": 3066251500.0,
            "turnover_rate": 6.69,
            "volume_ratio": 3.33,
            "pe_ratio": 334.67305963,
            "pb_ratio": 2.84255472,
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
            "change_60d": 5.1364,
            "signal_score": 87.7978,
            "ma_bullish": true,
            "price_above_ma20": true,
            "macd_status": "bullish",
            "rsi_status": "neutral",
            "breakout_20d_pct": 2.0249,
            "range_20d_pct": 14.0203,
            "volume_ratio_20d": 4.0308,
            "body_pct": 1.7081,
            "pullback_to_ma20_pct": 6.2794,
            "consolidation_days_20d": 20,
            "volatility_20d_pct": 22.7343,
            "max_drawdown_20d_pct": -3.231,
            "atr_20_pct": 2.2366,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:AkshareFetcher",
            "factor_scores": {
              "value": 33.3241,
              "liquidity": 42.1053,
              "momentum": 75.521,
              "reversal": 26.58,
              "activity": 83.6436,
              "stability": 76.4757,
              "size": 21.0526,
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
  },
  {
    "code": "603363",
    "name": "傲农生物",
    "resonance_count": 1,
    "strategies": [
      "volume_breakout"
    ],
    "strategy_labels": [
      "放量突破"
    ],
    "best_rank": 3,
    "best_score": 70.337,
    "average_score": 70.337,
    "strategy_details": {
      "volume_breakout": {
        "rank": 3,
        "score": 70.337,
        "reason": "本地后置评分: capital_confirmed",
        "raw_candidate": {
          "rank": 3,
          "code": "603363",
          "name": "傲农生物",
          "score": 70.337,
          "screen_score": 71.13700188210525,
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
          "price": 3.13,
          "change_pct": 2.29,
          "amount": 307013606.0,
          "industry": "",
          "factor_scores": {
            "value": 37.5099,
            "liquidity": 63.1579,
            "momentum": 76.8872,
            "reversal": 20.91,
            "activity": 81.643,
            "stability": 57.7831,
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
              "code": "603363",
              "name": "傲农生物",
              "source": "tencent",
              "fetched_at": "2026-09-02T09:36:13.171512+00:00",
              "price": 3.13,
              "change_pct": 2.29,
              "change_amount": 0.07,
              "volume": 97418300,
              "amount": 307013606.0,
              "volume_ratio": 2.84,
              "turnover_rate": 4.54,
              "amplitude": 7.52,
              "open_price": 3.1,
              "high": 3.31,
              "low": 3.08,
              "pre_close": 3.06,
              "pe_ratio": -18.07,
              "pb_ratio": 2.89,
              "total_mv": 8548000000.0,
              "circ_mv": 6719000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 3.13, 涨跌幅 2.29%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: capital_confirmed"
          },
          "post_analysis_tags": [
            "capital_confirmed"
          ],
          "raw": {
            "rank": 3,
            "code": "603363",
            "name": "傲农生物",
            "final_score": 70.337,
            "screen_score": 71.13700188210525,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 3.13,
            "change_pct": 2.29,
            "amount": 307013606.0,
            "total_mv": 8548223515.0,
            "turnover_rate": 4.54,
            "volume_ratio": 2.84,
            "pe_ratio": -18.07204696,
            "pb_ratio": 2.88752512,
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
            "change_60d": 7.931,
            "signal_score": 88.7759,
            "ma_bullish": true,
            "price_above_ma20": true,
            "macd_status": "bullish",
            "rsi_status": "neutral",
            "breakout_20d_pct": 2.2876,
            "range_20d_pct": 19.0647,
            "volume_ratio_20d": 2.7246,
            "body_pct": 0.9677,
            "pullback_to_ma20_pct": 6.2097,
            "consolidation_days_20d": 20,
            "volatility_20d_pct": 37.2203,
            "max_drawdown_20d_pct": -6.2706,
            "atr_20_pct": 3.4185,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:AkshareFetcher",
            "factor_scores": {
              "value": 37.5099,
              "liquidity": 63.1579,
              "momentum": 76.8872,
              "reversal": 20.91,
              "activity": 81.643,
              "stability": 57.7831,
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
                "code": "603363",
                "name": "傲农生物",
                "source": "tencent",
                "fetched_at": "2026-09-02T09:36:13.171512+00:00",
                "price": 3.13,
                "change_pct": 2.29,
                "change_amount": 0.07,
                "volume": 97418300,
                "amount": 307013606.0,
                "volume_ratio": 2.84,
                "turnover_rate": 4.54,
                "amplitude": 7.52,
                "open_price": 3.1,
                "high": 3.31,
                "low": 3.08,
                "pre_close": 3.06,
                "pe_ratio": -18.07,
                "pb_ratio": 2.89,
                "total_mv": 8548000000.0,
                "circ_mv": 6719000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 3.13, 涨跌幅 2.29%",
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
    "code": "600255",
    "name": "鑫科材料",
    "resonance_count": 1,
    "strategies": [
      "volume_breakout"
    ],
    "strategy_labels": [
      "放量突破"
    ],
    "best_rank": 4,
    "best_score": 70.1688,
    "average_score": 70.1688,
    "strategy_details": {
      "volume_breakout": {
        "rank": 4,
        "score": 70.1688,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 4,
          "code": "600255",
          "name": "鑫科材料",
          "score": 70.1688,
          "screen_score": 70.1688484943158,
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
          "price": 3.52,
          "change_pct": 4.14,
          "amount": 701744407.0,
          "industry": "",
          "factor_scores": {
            "value": 38.1504,
            "liquidity": 89.4737,
            "momentum": 66.859,
            "reversal": 5.0,
            "activity": 65.9778,
            "stability": 66.16,
            "size": 68.4211,
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
            "rank": 4,
            "code": "600255",
            "name": "鑫科材料",
            "final_score": 70.1688,
            "screen_score": 70.1688484943158,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 3.52,
            "change_pct": 4.14,
            "amount": 701744407.0,
            "total_mv": 6357637282.0,
            "turnover_rate": 11.03,
            "volume_ratio": 3.78,
            "pe_ratio": 118.23369023,
            "pb_ratio": 4.23278313,
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
            "change_60d": -21.0762,
            "signal_score": 72.0,
            "ma_bullish": false,
            "price_above_ma20": true,
            "macd_status": "bullish",
            "rsi_status": "neutral",
            "breakout_20d_pct": -0.565,
            "range_20d_pct": 17.5159,
            "volume_ratio_20d": 3.2504,
            "body_pct": 4.7619,
            "pullback_to_ma20_pct": 5.6264,
            "consolidation_days_20d": 15,
            "volatility_20d_pct": 32.3261,
            "max_drawdown_20d_pct": -8.4058,
            "atr_20_pct": 3.1676,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:AkshareFetcher",
            "factor_scores": {
              "value": 38.1504,
              "liquidity": 89.4737,
              "momentum": 66.859,
              "reversal": 5.0,
              "activity": 65.9778,
              "stability": 66.16,
              "size": 68.4211,
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
    "code": "302132",
    "name": "中航成飞",
    "resonance_count": 1,
    "strategies": [
      "capital_heat"
    ],
    "strategy_labels": [
      "资金热度"
    ],
    "best_rank": 3,
    "best_score": 70.0082,
    "average_score": 70.0082,
    "strategy_details": {
      "capital_heat": {
        "rank": 3,
        "score": 70.0082,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 3,
          "code": "302132",
          "name": "中航成飞",
          "score": 70.0082,
          "screen_score": 72.00818693548389,
          "reason": "本地后置评分: 未发现额外加分项",
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
          "price": 63.4,
          "change_pct": 4.34,
          "amount": 1774102083.89,
          "industry": "",
          "factor_scores": {
            "value": 32.0883,
            "liquidity": 93.5484,
            "momentum": 70.605,
            "reversal": 5.0,
            "activity": 81.2459,
            "stability": 64.98,
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
              "code": "302132",
              "name": "中航成飞",
              "source": "tencent",
              "fetched_at": "2026-09-02T09:36:25.563209+00:00",
              "price": 63.4,
              "change_pct": 4.34,
              "change_amount": 2.64,
              "volume": 27960400,
              "amount": 1774102084.0,
              "volume_ratio": 3.23,
              "turnover_rate": 4.77,
              "amplitude": 9.23,
              "open_price": 60.3,
              "high": 65.91,
              "low": 60.3,
              "pre_close": 60.76,
              "pe_ratio": 52.47,
              "pb_ratio": 8.11,
              "total_mv": 169411000000.0,
              "circ_mv": 37157000000.0
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
          "dsa_analysis_summary": "DSA行情: 现价 63.4, 涨跌幅 4.34%",
          "post_analysis_summaries": {
            "scorecard": "本地后置评分: 未发现额外加分项"
          },
          "post_analysis_tags": [],
          "raw": {
            "rank": 3,
            "code": "302132",
            "name": "中航成飞",
            "final_score": 70.0082,
            "screen_score": 72.00818693548389,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 63.4,
            "change_pct": 4.34,
            "amount": 1774102083.89,
            "total_mv": 169410593238.0,
            "turnover_rate": 4.77,
            "volume_ratio": 3.23,
            "pe_ratio": 52.47287469,
            "pb_ratio": 8.10886073,
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
              "value": 32.0883,
              "liquidity": 93.5484,
              "momentum": 70.605,
              "reversal": 5.0,
              "activity": 81.2459,
              "stability": 64.98,
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
                "code": "302132",
                "name": "中航成飞",
                "source": "tencent",
                "fetched_at": "2026-09-02T09:36:25.563209+00:00",
                "price": 63.4,
                "change_pct": 4.34,
                "change_amount": 2.64,
                "volume": 27960400,
                "amount": 1774102084.0,
                "volume_ratio": 3.23,
                "turnover_rate": 4.77,
                "amplitude": 9.23,
                "open_price": 60.3,
                "high": 65.91,
                "low": 60.3,
                "pre_close": 60.76,
                "pe_ratio": 52.47,
                "pb_ratio": 8.11,
                "total_mv": 169411000000.0,
                "circ_mv": 37157000000.0
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
            "dsa_analysis_summary": "DSA行情: 现价 63.4, 涨跌幅 4.34%",
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
    "code": "002106",
    "name": "莱宝高科",
    "resonance_count": 1,
    "strategies": [
      "volume_breakout"
    ],
    "strategy_labels": [
      "放量突破"
    ],
    "best_rank": 6,
    "best_score": 69.2536,
    "average_score": 69.2536,
    "strategy_details": {
      "volume_breakout": {
        "rank": 6,
        "score": 69.2536,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 6,
          "code": "002106",
          "name": "莱宝高科",
          "score": 69.2536,
          "screen_score": 69.25362021978947,
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
          "price": 10.93,
          "change_pct": 5.0,
          "amount": 457878823.86,
          "industry": "",
          "factor_scores": {
            "value": 87.9917,
            "liquidity": 73.6842,
            "momentum": 59.7166,
            "reversal": 5.0,
            "activity": 83.9778,
            "stability": 64.2,
            "size": 78.9474,
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
            "code": "002106",
            "name": "莱宝高科",
            "final_score": 69.2536,
            "screen_score": 69.25362021978947,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 10.93,
            "change_pct": 5.0,
            "amount": 457878823.86,
            "total_mv": 7714570629.0,
            "turnover_rate": 6.03,
            "volume_ratio": 3.78,
            "pe_ratio": 48.69271284,
            "pb_ratio": 1.37684694,
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
            "change_60d": -16.8189,
            "signal_score": 60.0,
            "ma_bullish": false,
            "price_above_ma20": true,
            "macd_status": "neutral",
            "rsi_status": "neutral",
            "breakout_20d_pct": -0.9066,
            "range_20d_pct": 13.4694,
            "volume_ratio_20d": 2.5092,
            "body_pct": 6.323,
            "pullback_to_ma20_pct": 4.5683,
            "consolidation_days_20d": 10,
            "volatility_20d_pct": 37.5986,
            "max_drawdown_20d_pct": -6.2731,
            "atr_20_pct": 3.3806,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:AkshareFetcher",
            "factor_scores": {
              "value": 87.9917,
              "liquidity": 73.6842,
              "momentum": 59.7166,
              "reversal": 5.0,
              "activity": 83.9778,
              "stability": 64.2,
              "size": 78.9474,
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
    "code": "002765",
    "name": "蓝黛科技",
    "resonance_count": 1,
    "strategies": [
      "volume_breakout"
    ],
    "strategy_labels": [
      "放量突破"
    ],
    "best_rank": 7,
    "best_score": 68.9809,
    "average_score": 68.9809,
    "strategy_details": {
      "volume_breakout": {
        "rank": 7,
        "score": 68.9809,
        "reason": "本地后置评分: 未发现额外加分项",
        "raw_candidate": {
          "rank": 7,
          "code": "002765",
          "name": "蓝黛科技",
          "score": 68.9809,
          "screen_score": 68.98086748842105,
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
          "price": 7.42,
          "change_pct": 4.65,
          "amount": 242970359.91,
          "industry": "",
          "factor_scores": {
            "value": 73.7364,
            "liquidity": 52.6316,
            "momentum": 71.0475,
            "reversal": 5.0,
            "activity": 85.7061,
            "stability": 66.69,
            "size": 52.6316,
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
            "code": "002765",
            "name": "蓝黛科技",
            "final_score": 68.9809,
            "screen_score": 68.98086748842105,
            "llm_score": null,
            "ranking_reason": "",
            "risk_summary": "",
            "price": 7.42,
            "change_pct": 4.65,
            "amount": 242970359.91,
            "total_mv": 4838790428.0,
            "turnover_rate": 5.53,
            "volume_ratio": 2.95,
            "pe_ratio": 70.80585062,
            "pb_ratio": 1.85955488,
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
            "change_60d": -8.0545,
            "signal_score": 72.0,
            "ma_bullish": false,
            "price_above_ma20": true,
            "macd_status": "bullish",
            "rsi_status": "neutral",
            "breakout_20d_pct": -0.9346,
            "range_20d_pct": 14.2438,
            "volume_ratio_20d": 3.615,
            "body_pct": 5.2482,
            "pullback_to_ma20_pct": 4.3894,
            "consolidation_days_20d": 20,
            "volatility_20d_pct": 27.5606,
            "max_drawdown_20d_pct": -5.227,
            "atr_20_pct": 3.3356,
            "daily_quality_score": 100.0,
            "daily_quality_flags": "",
            "daily_source": "dsa:AkshareFetcher",
            "factor_scores": {
              "value": 73.7364,
              "liquidity": 52.6316,
              "momentum": 71.0475,
              "reversal": 5.0,
              "activity": 85.7061,
              "stability": 66.69,
              "size": 52.6316,
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
